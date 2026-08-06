import sys, pathlib, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.yamlish import parse, YamlishError
from tests import fixtures


class TestYamlish(unittest.TestCase):
    def test_flat_scalars(self):
        self.assertEqual(
            parse('title: "The Naïve Voyager"\nplanned: 32\nassisted: true\nsub: ""'),
            {"title": "The Naïve Voyager", "planned": 32, "assisted": True,
             "sub": ""},
        )

    def test_comments_and_blank_lines_ignored(self):
        self.assertEqual(parse("# a comment\n\nlanguage: pt-BR  # trailing\n"),
                         {"language": "pt-BR"})

    def test_nested_mapping(self):
        text = "paths:\n  manuscript: manuscript/\n  layout: chapter\n"
        self.assertEqual(parse(text),
                         {"paths": {"manuscript": "manuscript/", "layout": "chapter"}})

    def test_inline_list(self):
        self.assertEqual(parse("formats: [docx, pdf]"), {"formats": ["docx", "pdf"]})

    def test_empty_inline_list(self):
        self.assertEqual(parse("address: []"), {"address": []})

    def test_comma_inside_quotes_does_not_split_an_inline_list(self):
        self.assertEqual(
            parse('address: ["Rua das Oliveiras, 12", "Interior - SP"]'),
            {"address": ["Rua das Oliveiras, 12", "Interior - SP"]})

    def test_block_list(self):
        text = "title_page:\n  - contact\n  - wordcount\n"
        self.assertEqual(parse(text), {"title_page": ["contact", "wordcount"]})

    def test_deep_nesting(self):
        text = "profiles:\n  submission:\n    font: Courier New\n    size: 12pt\n"
        self.assertEqual(parse(text),
                         {"profiles": {"submission": {"font": "Courier New",
                                                      "size": "12pt"}}})

    def test_sibling_after_nested_block(self):
        text = "paths:\n  layout: flat\nstatus:\n  phase: draft\n"
        self.assertEqual(parse(text), {"paths": {"layout": "flat"},
                                       "status": {"phase": "draft"}})

    def test_hash_inside_quotes_is_not_a_comment(self):
        self.assertEqual(parse('scene_break: "#"'), {"scene_break": "#"})

    def test_rejects_tabs_with_line_number(self):
        with self.assertRaises(YamlishError) as ctx:
            parse("paths:\n\tlayout: flat\n")
        self.assertEqual(ctx.exception.line, 2)

    def test_parses_a_full_project_yaml(self):
        data = parse((fixtures.BOOK / ".project" / "config" / "project.yaml")
                     .read_text(encoding="utf-8"))
        self.assertEqual(data["paths"]["layout"], "chapter")
        self.assertEqual(data["paths"]["naming"], "{act}.{n}.md")
        self.assertEqual(data["language"], "en")
        self.assertEqual(data["genre"]["audience"], "adult")
        self.assertEqual(data["structure"]["planned_total"], 4)
        self.assertEqual(data["ai"]["density_ceiling_total"], 8.0)
        self.assertIs(data["ai"]["assisted"], True)

    def test_the_shipped_config_files_parse(self):
        # No value assertions: init-project rewrites project.yaml, and this
        # suite travels into every book cloned from the template.
        config = pathlib.Path(__file__).resolve().parents[1] / ".project" / "config"
        for name in ("project.yaml", "export.yaml"):
            path = config / name
            if path.exists():
                self.assertIsInstance(
                    parse(path.read_text(encoding="utf-8")), dict, name)


if __name__ == "__main__":
    unittest.main()
