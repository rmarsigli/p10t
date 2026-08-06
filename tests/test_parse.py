import sys, pathlib, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.chapters import ChapterFile, find_chapters
from p10t_export.parse import parse_chapter, count_words, Block


def _chapter(tmp, text, chapter_id="01.01"):
    path = pathlib.Path(tmp) / (chapter_id + ".md")
    path.write_text(text, encoding="utf-8")
    return ChapterFile(chapter_id, path)


CLEAN = """\
# 1

O terceiro vidro trincou. Ninguém percebeu.

Melvile é uma cidade de interior.
"""

WITH_SCENES = """\
# 3

## 1 - A contagem - 250

— Contagem.

Estávamos em um lugar vazio.

## 2 — Os seis minutos — 900

— O trem parou a 3 quilômetros.
"""

SCAFFOLDED = """\
# 4

<!-- ANDAIME. As linhas em { } são para você sobrescrever. -->

| # | Cena | Palavras |
| --- | --- | --- |
| 1 | Dentro do duto | 400 |

## 1 - Dentro do duto - 400

{ O duto é largo, escuro e fedido. }

**Dentro:**

- Por que é seguro: é coberto.
"""


class TestWordCount(unittest.TestCase):
    def test_bare_em_dash_is_not_a_word(self):
        self.assertEqual(count_words("— Contagem."), 1)

    def test_numbers_count(self):
        self.assertEqual(count_words("O trem parou a 3 quilômetros."), 6)


class TestCleanChapter(unittest.TestCase):
    def test_title_and_paragraphs(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertTrue(parsed.accepted)
        self.assertEqual(parsed.title, "1")
        self.assertEqual([b.kind for b in parsed.blocks],
                         ["paragraph", "paragraph"])
        self.assertTrue(parsed.blocks[0].text.startswith("O terceiro vidro"))

    def test_word_count_excludes_the_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertEqual(parsed.words, 12)

    def test_absence_of_scene_headers_is_not_a_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, CLEAN))
        self.assertEqual(parsed.refusals, [])
        self.assertEqual(parsed.scene_breaks, 0)

    def test_missing_heading_falls_back_to_the_chapter_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, "Só prosa, sem título.\n"))
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
        text = "# 4\n\n## 2 - O labirinto - 1.100 - SET PIECE\n\nProsa.\n"
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, text))
        self.assertTrue(parsed.accepted)

    def test_budget_and_name_do_not_reach_the_word_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, WITH_SCENES, "01.03"))
        self.assertEqual(parsed.words, 12)

    def test_a_plain_heading_is_not_a_scene_header(self):
        text = "# 4\n\n## Tabela de guia\n\nProsa.\n"
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
            parsed = parse_chapter(_chapter(tmp, "# 1\n\nProsa.\n\n---\n"))
        self.assertEqual([r.kind for r in parsed.refusals], ["rule"])

    def test_hyphen_dialogue_is_refused_because_pandoc_would_bullet_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, "# 1\n\n- Contagem.\n"))
        self.assertEqual([r.kind for r in parsed.refusals], ["list"])

    def test_multiline_comment_refuses_every_line(self):
        text = "# 1\n\n<!-- nota\n  segue\n  fim -->\n\nProsa.\n"
        with tempfile.TemporaryDirectory() as tmp:
            parsed = parse_chapter(_chapter(tmp, text))
        self.assertEqual([r.line for r in parsed.refusals], [3, 4, 5])


class TestRealBook(unittest.TestCase):
    def test_three_chapters_accepted_and_the_plan_refused(self):
        book = pathlib.Path(
            "/home/rafhael/projects/books/gods-between-us/manuscript")
        if not book.is_dir():
            self.skipTest("reference book not present")
        results = {c.chapter_id: parse_chapter(c)
                   for c in find_chapters(book, "chapter", "{act}.{n}.md")}
        self.assertTrue(results["01.01"].accepted)
        self.assertTrue(results["01.02"].accepted)
        self.assertTrue(results["01.03"].accepted)
        self.assertFalse(results["01.04"].accepted)
        self.assertGreater(len(results["01.04"].refusals), 100)
        self.assertEqual(results["01.03"].scene_breaks, 5)


if __name__ == "__main__":
    unittest.main()
