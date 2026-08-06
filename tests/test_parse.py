import sys, pathlib, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.chapters import ChapterFile, find_chapters
from p10t_export.parse import parse_chapter, count_words, Block
from tests import fixtures


def _chapter(tmp, text, chapter_id="01.01"):
    path = pathlib.Path(tmp) / (chapter_id + ".md")
    path.write_text(text, encoding="utf-8")
    return ChapterFile(chapter_id, path)


CLEAN = """\
# 1

The third pane cracked. Nobody noticed.

Melvile is an inland town.
"""

WITH_SCENES = """\
# 3

## 1 - The count - 250

— Count off.

We were standing in an empty place.

## 2 — The six minutes — 900

— The train stopped 3 kilometres back.
"""

SCAFFOLDED = """\
# 4

<!-- SCAFFOLD. Lines in { } are to be overwritten. -->

| # | Scene | Words |
| --- | --- | --- |
| 1 | Inside the culvert | 400 |

## 1 - Inside the culvert - 400

{ The culvert is wide, dark and foul. }

**Inside:**

- Why it is safe: it is covered.
"""


class TestWordCount(unittest.TestCase):
    def test_bare_em_dash_is_not_a_word(self):
        self.assertEqual(count_words("— Yes."), 1)

    def test_numbers_count(self):
        self.assertEqual(count_words("The train stopped 3 kilometres back."), 6)


class TestCleanChapter(unittest.TestCase):
    def test_title_and_paragraphs(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertTrue(parsed.accepted)
        self.assertEqual(parsed.title, "1")
        self.assertEqual([b.kind for b in parsed.blocks],
                         ["paragraph", "paragraph"])
        self.assertTrue(parsed.blocks[0].text.startswith("The third pane"))

    def test_word_count_excludes_the_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertEqual(parsed.words, 11)

    def test_absence_of_scene_headers_is_not_a_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertEqual(parsed.refusals, [])
        self.assertEqual(parsed.scene_breaks, 0)

    def test_missing_heading_falls_back_to_the_chapter_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, "Just prose, no heading.\n"))
        self.assertEqual(parsed.title, "01.01")
        self.assertTrue(parsed.accepted)


class TestSceneHeaders(unittest.TestCase):
    def test_headers_become_breaks_and_the_first_is_suppressed(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, WITH_SCENES, "01.03"))
        self.assertTrue(parsed.accepted)
        self.assertEqual([b.kind for b in parsed.blocks],
                         ["paragraph", "paragraph", "scene_break", "paragraph"])

    def test_em_dash_separator_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, WITH_SCENES, "01.03"))
        self.assertIn(Block("scene_break", ""), parsed.blocks)

    def test_trailing_note_after_the_budget_is_accepted(self):
        text = "# 4\n\n## 2 - The maze - 1,100 - SET PIECE\n\nProse.\n"
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, text))
        self.assertTrue(parsed.accepted)

    def test_budget_and_name_do_not_reach_the_word_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, WITH_SCENES, "01.03"))
        self.assertEqual(parsed.words, 15)

    def test_a_plain_heading_is_not_a_scene_header(self):
        text = "# 4\n\n## Scene guide\n\nProse.\n"
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, text))
        self.assertEqual([r.kind for r in parsed.refusals], ["heading"])


class TestRefusal(unittest.TestCase):
    def test_scaffolded_chapter_is_refused_with_line_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, SCAFFOLDED, "01.04"))
        self.assertFalse(parsed.accepted)
        kinds = {r.kind for r in parsed.refusals}
        self.assertEqual(kinds, {"comment", "table", "placeholder",
                                 "emphasis-only", "list"})
        self.assertTrue(all(r.line > 0 for r in parsed.refusals))

    def test_comment_line_is_reported_at_its_own_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, SCAFFOLDED, "01.04"))
        comment = [r for r in parsed.refusals if r.kind == "comment"][0]
        self.assertEqual(comment.line, 3)

    def test_horizontal_rule_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, "# 1\n\nProse.\n\n---\n"))
        self.assertEqual([r.kind for r in parsed.refusals], ["rule"])

    def test_hyphen_dialogue_is_refused_because_pandoc_would_bullet_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, "# 1\n\n- Count off.\n"))
        self.assertEqual([r.kind for r in parsed.refusals], ["list"])

    def test_multiline_comment_refuses_every_line(self):
        text = "# 1\n\n<!-- note\n  continues\n  ends -->\n\nProse.\n"
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, text))
        self.assertEqual([r.line for r in parsed.refusals], [3, 4, 5])


class TestFixtureBook(unittest.TestCase):
    """The four states a chapter can be in, on a real tree."""

    def setUp(self):
        self.chapters = {
            chapter.chapter_id: parse_chapter(chapter)
            for chapter in find_chapters(fixtures.BOOK_MANUSCRIPT, "chapter",
                                         fixtures.NAMING)}

    def test_written_chapters_are_accepted(self):
        for chapter_id, words in (("01.01", 11), ("01.02", 38), ("01.03", 17)):
            parsed = self.chapters[chapter_id]
            self.assertTrue(parsed.accepted, chapter_id)
            self.assertEqual(parsed.words, words, chapter_id)

    def test_dialogue_dashes_are_not_counted_as_words(self):
        # 01.02 opens two lines with a bare em dash; neither dash counts.
        self.assertEqual(self.chapters["01.02"].words, 38)

    def test_a_chapter_written_straight_through_has_no_breaks(self):
        self.assertEqual(self.chapters["01.01"].scene_breaks, 0)
        self.assertTrue(self.chapters["01.01"].accepted)

    def test_three_scene_headers_produce_two_breaks(self):
        self.assertEqual(self.chapters["01.03"].scene_breaks, 2)

    def test_the_plan_is_refused_with_every_kind_named(self):
        parsed = self.chapters["01.04"]
        self.assertFalse(parsed.accepted)
        self.assertEqual(parsed.words, 0)
        self.assertEqual(
            sorted({refusal.kind for refusal in parsed.refusals}),
            ["comment", "emphasis-only", "heading", "list", "placeholder",
             "quote", "rule", "table"])

    def test_titles_come_from_the_heading(self):
        self.assertEqual([self.chapters[k].title
                          for k in sorted(self.chapters)],
                         ["1", "2", "3", "4"])


if __name__ == "__main__":
    unittest.main()
