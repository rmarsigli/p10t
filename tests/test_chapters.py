import sys, pathlib, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.chapters import (find_chapters, naming_regex,
                                  MixedLayoutError, LayoutError)
from tests import fixtures

NAMING = "{act}.{n}.md"


def _touch(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# x\n", encoding="utf-8")


class TestNamingRegex(unittest.TestCase):
    def test_matches_padded_ids(self):
        rx = naming_regex(NAMING)
        self.assertTrue(rx.match("01.01"))
        self.assertTrue(rx.match("12.07"))

    def test_matches_variant_suffix(self):
        self.assertTrue(naming_regex(NAMING).match("02.03i"))

    def test_rejects_satellites_and_notes(self):
        rx = naming_regex(NAMING)
        self.assertIsNone(rx.match("01.01_analysis"))
        self.assertIsNone(rx.match("README"))
        self.assertIsNone(rx.match("_drafts"))

    def test_single_field_naming(self):
        rx = naming_regex("{chapter}.md")
        self.assertTrue(rx.match("07"))
        self.assertIsNone(rx.match("07_outline"))


class TestFlat(unittest.TestCase):
    def test_finds_chapters_and_ignores_satellites(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            for name in ("01.01.md", "01.02.md", "01.01_analysis.md",
                         "01.02_outline.md", "README.md", "_drafts.md"):
                _touch(m / name)
            found = find_chapters(m, "flat", NAMING)
        self.assertEqual([c.chapter_id for c in found], ["01.01", "01.02"])

    def test_sorts_lexicographically(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            for name in ("02.01.md", "01.10.md", "01.02.md"):
                _touch(m / name)
            found = find_chapters(m, "flat", NAMING)
        self.assertEqual([c.chapter_id for c in found],
                         ["01.02", "01.10", "02.01"])


class TestChapterLayout(unittest.TestCase):
    def test_finds_chapter_file_inside_its_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            _touch(m / "01.01" / "01.01.md")
            _touch(m / "01.01" / "01.01_analysis.md")
            _touch(m / "01.02" / "01.02.md")
            found = find_chapters(m, "chapter", NAMING)
        self.assertEqual([c.chapter_id for c in found], ["01.01", "01.02"])
        self.assertTrue(str(found[0].path).endswith("01.01/01.01.md"))

    def test_directory_without_its_chapter_file_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            _touch(m / "01.01" / "01.01.md")
            (m / "01.02").mkdir()
            with self.assertRaises(LayoutError) as ctx:
                find_chapters(m, "chapter", NAMING)
        self.assertIn("01.02", str(ctx.exception))


class TestMixedState(unittest.TestCase):
    def test_loose_file_beside_chapter_directories_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            _touch(m / "01.01" / "01.01.md")
            _touch(m / "01.02.md")
            with self.assertRaises(MixedLayoutError) as ctx:
                find_chapters(m, "chapter", NAMING)
        message = str(ctx.exception)
        self.assertIn("01.02.md", message)
        self.assertIn("01.01", message)

    def test_readme_beside_chapter_directories_is_not_mixed(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = pathlib.Path(tmp)
            _touch(m / "01.01" / "01.01.md")
            _touch(m / "README.md")
            _touch(m / "_drafts.md")
            found = find_chapters(m, "chapter", NAMING)
        self.assertEqual([c.chapter_id for c in found], ["01.01"])


class TestFixtureTrees(unittest.TestCase):
    """Both layouts resolved against a real tree, not a built one."""

    def test_chapter_layout(self):
        found = find_chapters(fixtures.BOOK_MANUSCRIPT, "chapter", NAMING)
        self.assertEqual([c.chapter_id for c in found],
                         ["01.01", "01.02", "01.03", "01.04"])

    def test_chapter_layout_ignores_satellites_and_notes(self):
        found = find_chapters(fixtures.BOOK_MANUSCRIPT, "chapter", NAMING)
        names = [c.path.name for c in found]
        self.assertNotIn("01.03_analysis.md", names)
        self.assertNotIn("01.01_outline.md", names)
        self.assertNotIn("README.md", names)
        self.assertNotIn("_drafts.md", names)

    def test_flat_layout(self):
        found = find_chapters(fixtures.FLAT_MANUSCRIPT, "flat", NAMING)
        self.assertEqual([c.chapter_id for c in found],
                         ["01.01", "01.02", "01.10"])

    def test_zero_padding_keeps_ten_after_two(self):
        found = find_chapters(fixtures.FLAT_MANUSCRIPT, "flat", NAMING)
        self.assertEqual(found[-1].chapter_id, "01.10")


if __name__ == "__main__":
    unittest.main()
