import sys, pathlib, shutil, tempfile, unittest, zipfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.config import Profile, DEFAULT_PROFILES
from p10t_export.templates import (typst_template, epub_css, leading_to_typst,
                                   derive_reference_docx, resolve_override)
from tests.test_render import make_cfg

SUBMISSION = Profile(name="submission", **DEFAULT_PROFILES["submission"])
READING = Profile(name="reading", **DEFAULT_PROFILES["reading"])


class TestTypstTemplate(unittest.TestCase):
    def test_carries_font_size_and_margins(self):
        out = typst_template(make_cfg(), SUBMISSION)
        self.assertIn('font: "Courier New"', out)
        self.assertIn("size: 12pt", out)
        self.assertIn("margin: 2.54cm", out)

    def test_running_head_is_interpolated_and_suppressed_on_page_one(self):
        out = typst_template(make_cfg(), SUBMISSION)
        self.assertIn("Marsigli / Deuses Entre Nós /", out)
        self.assertIn("if page > 1", out)

    def test_body_placeholder_present_for_pandoc(self):
        self.assertIn("$body$", typst_template(make_cfg(), SUBMISSION))

    def test_language_reaches_hyphenation(self):
        self.assertIn('lang: "pt"', typst_template(make_cfg(), SUBMISSION))

    def test_chapter_headings_start_a_new_page(self):
        out = typst_template(make_cfg(), SUBMISSION)
        self.assertIn("heading.where(level: 1)", out)
        self.assertIn("pagebreak", out)

    def test_reading_head_has_no_author(self):
        out = typst_template(make_cfg(), READING)
        self.assertIn("align(right)[Deuses Entre Nós]", out)


class TestLeading(unittest.TestCase):
    def test_double_maps_to_one_em(self):
        self.assertEqual(leading_to_typst("double"), "1em")

    def test_numeric_leading_is_converted(self):
        self.assertEqual(leading_to_typst("1.3"), "0.65em")

    def test_nonsense_falls_back_to_the_typst_default(self):
        self.assertEqual(leading_to_typst("wide"), "0.65em")


class TestEpubCss(unittest.TestCase):
    def test_centres_the_scene_break(self):
        css = epub_css(READING)
        self.assertIn(".scene-break", css)
        self.assertIn("text-align: center", css)

    def test_double_leading_becomes_a_line_height_of_two(self):
        self.assertIn("line-height: 2;", epub_css(SUBMISSION))


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestReferenceDocx(unittest.TestCase):
    def test_patches_font_size_and_adds_the_scene_break_style(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = derive_reference_docx(SUBMISSION, shutil.which("pandoc"),
                                        pathlib.Path(tmp) / "ref.docx")
            styles = zipfile.ZipFile(out).read("word/styles.xml").decode("utf-8")
            leftovers = list(pathlib.Path(tmp).glob("*.default.docx"))
        self.assertIn('w:ascii="Courier New"', styles)
        self.assertIn('w:val="24"', styles)
        self.assertIn("SceneBreak", styles)
        self.assertIn('w:line="480"', styles)
        self.assertEqual(leftovers, [])

    def test_the_result_is_a_valid_docx_pandoc_accepts(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            reference = derive_reference_docx(SUBMISSION,
                                              shutil.which("pandoc"),
                                              tmp / "ref.docx")
            source = tmp / "in.md"
            source.write_text("# 1\n\nProsa.\n", encoding="utf-8")
            target = tmp / "out.docx"
            import subprocess
            subprocess.check_call([shutil.which("pandoc"), str(source),
                                   "-o", str(target),
                                   "--reference-doc", str(reference)])
            self.assertTrue(target.exists())


class TestOverride(unittest.TestCase):
    def test_hand_written_template_wins(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            target = root / ".project" / "templates" / "export"
            target.mkdir(parents=True)
            (target / "submission.typ").write_text("mine", encoding="utf-8")
            self.assertIsNotNone(resolve_override(root, "submission.typ"))
            self.assertIsNone(resolve_override(root, "reading.typ"))


if __name__ == "__main__":
    unittest.main()
