import sys, pathlib, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.config import (Metadata, Contact, Profile, ExportConfig,
                                DEFAULT_PROFILES, default_labels)
from p10t_export.parse import ParsedChapter, Block
from p10t_export.render import (slugify, round_wordcount, output_name,
                                render_title_page, render_body,
                                render_document, typst_escape,
                                markdown_escape)


def make_cfg(title="Deuses Entre Nós", contact=None):
    meta = Metadata(title=title, author="Rafhael Marsigli", language="pt-BR",
                    audience="adulto", genre="ficção especulativa")
    if contact is None:
        contact = Contact(name="Rafhael Marsigli", address=["Rua X, 1"],
                          phone="+55 11 0000", email="r@example.com")
    return ExportConfig(
        metadata=meta, contact=contact, labels=default_labels("pt-BR"),
        profiles={n: Profile(name=n, **d) for n, d in DEFAULT_PROFILES.items()},
        manuscript=pathlib.Path("manuscript"), layout="chapter",
        naming="{act}.{n}.md", root=pathlib.Path("."))


def make_chapters():
    return [ParsedChapter("01.01", pathlib.Path("a.md"), "1",
                          [Block("paragraph", "Primeiro."),
                           Block("scene_break", ""),
                           Block("paragraph", "Segundo.")], 2, [])]


class TestSlug(unittest.TestCase):
    def test_strips_characters_windows_forbids(self):
        self.assertEqual(slugify('Deuses: A Queda/Parte "1"'),
                         "Deuses-A-Queda-Parte-1")

    def test_keeps_accents(self):
        self.assertEqual(slugify("Deuses Entre Nós"), "Deuses-Entre-Nós")


class TestWordcount(unittest.TestCase):
    def test_rounds_to_the_nearest_thousand(self):
        self.assertEqual(round_wordcount(79640), 80000)
        self.assertEqual(round_wordcount(80400), 80000)

    def test_short_manuscripts_round_to_the_nearest_hundred(self):
        self.assertEqual(round_wordcount(3688), 3700)


class TestOutputName(unittest.TestCase):
    def test_submission_name_carries_author_and_title(self):
        cfg = make_cfg()
        name = output_name(cfg, cfg.profiles["submission"], "docx")
        self.assertTrue(name.startswith("Marsigli_Deuses-Entre-Nós_"))
        self.assertTrue(name.endswith(".docx"))

    def test_colon_in_the_title_never_reaches_the_filename(self):
        cfg = make_cfg(title="Deuses: A Queda")
        name = output_name(cfg, cfg.profiles["submission"], "pdf")
        self.assertNotIn(":", name)


class TestTypstEscape(unittest.TestCase):
    def test_escapes_the_characters_typst_reads_as_syntax(self):
        self.assertEqual(typst_escape("r@example.com"), "r\\@example.com")
        self.assertEqual(typst_escape("#1 [a]"), "\\#1 \\[a\\]")

    def test_escapes_emphasis_markers(self):
        # "* * *" is an unclosed strong-emphasis delimiter in typst content
        # mode, and it is the default scene break of the reading profile.
        self.assertEqual(typst_escape("* * *"), "\\* \\* \\*")
        self.assertEqual(typst_escape("_x_"), "\\_x\\_")


class TestMarkdownEscape(unittest.TestCase):
    def test_escapes_a_bare_hash(self):
        self.assertEqual(markdown_escape("#"), "\\#")

    def test_escapes_an_asterisk_rule(self):
        self.assertEqual(markdown_escape("* * *"), "\\* \\* \\*")


class TestTitlePage(unittest.TestCase):
    def test_submission_page_has_contact_and_wordcount(self):
        cfg = make_cfg()
        page = render_title_page(cfg, cfg.profiles["submission"], 80000, "typst")
        self.assertIn("Contagem de palavras: 80.000", page)
        self.assertIn("example.com", page)
        self.assertIn("DEUSES ENTRE NÓS", page)
        self.assertIn("por Rafhael Marsigli", page)
        self.assertIn("adulto", page)
        self.assertIn("ficção especulativa", page)

    def test_reading_page_has_neither_contact_nor_wordcount(self):
        cfg = make_cfg()
        page = render_title_page(cfg, cfg.profiles["reading"], 80000, "typst")
        self.assertNotIn("example.com", page)
        self.assertNotIn("Contagem", page)
        self.assertIn("Deuses Entre Nós", page)

    def test_empty_contact_block_is_simply_absent(self):
        cfg = make_cfg(contact=Contact())
        page = render_title_page(cfg, cfg.profiles["submission"], 1000, "typst")
        self.assertIn("Contagem de palavras", page)
        self.assertNotIn("Rua X", page)


class TestBody(unittest.TestCase):
    def test_chapter_title_becomes_a_heading(self):
        cfg = make_cfg()
        body = render_body(make_chapters(), cfg.profiles["submission"], "typst")
        self.assertIn("# 1", body)

    def test_scene_break_is_raw_typst(self):
        cfg = make_cfg()
        body = render_body(make_chapters(), cfg.profiles["submission"], "typst")
        self.assertIn("```{=typst}", body)
        self.assertIn("#align(center)", body)

    def test_scene_break_is_a_custom_style_div_for_docx(self):
        cfg = make_cfg()
        body = render_body(make_chapters(), cfg.profiles["submission"], "docx")
        self.assertIn('custom-style="SceneBreak"', body)

    def test_scene_break_is_raw_html_for_epub(self):
        cfg = make_cfg()
        body = render_body(make_chapters(), cfg.profiles["reading"], "epub")
        self.assertIn('<p class="scene-break">', body)

    def test_docx_marker_is_escaped_so_pandoc_does_not_eat_it(self):
        # A bare "#" on its own line is an empty heading, and "* * *" is a
        # horizontal rule: either one silently swallows the scene break.
        cfg = make_cfg()
        body = render_body(make_chapters(), cfg.profiles["submission"], "docx")
        self.assertIn("\\#", body)
        self.assertNotIn("\n#\n", body)

    def test_asterisk_marker_is_escaped_for_docx(self):
        cfg = make_cfg()
        profile = cfg.profiles["reading"]
        profile.scene_break = "* * *"
        body = render_body(make_chapters(), profile, "docx")
        self.assertIn("\\*", body)


class TestDocument(unittest.TestCase):
    def test_epub_has_no_hand_built_title_page(self):
        cfg = make_cfg()
        doc = render_document(cfg, cfg.profiles["reading"], make_chapters(),
                              "epub")
        self.assertTrue(doc.startswith("# 1"))

    def test_docx_separates_the_title_page_with_a_page_break(self):
        cfg = make_cfg()
        doc = render_document(cfg, cfg.profiles["submission"], make_chapters(),
                              "docx")
        self.assertIn('w:br w:type="page"', doc)
        self.assertIn("DEUSES ENTRE NÓS", doc)


if __name__ == "__main__":
    unittest.main()
