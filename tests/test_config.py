import sys, pathlib, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.config import (load_config, default_labels, format_number,
                                ConfigError)

PROJECT_YAML = """\
language: pt-BR
title: "Deuses Entre Nós"
author: "Rafhael Marsigli"
genre:
  primary: "ficção especulativa"
  audience: "adulto"
paths:
  manuscript: "manuscript/"
  naming: "{act}.{n}.md"
  layout: "chapter"
"""

EXPORT_YAML = """\
contact:
  name: "Rafhael Marsigli"
  address: []
  phone: ""
  email: ""
labels:
  wordcount: "Contagem de palavras"
profiles:
  submission:
    formats: [docx, pdf]
    font: "Courier New"
    scene_break: "#"
"""


def _project(tmp, project_yaml=PROJECT_YAML, export_yaml=EXPORT_YAML):
    root = pathlib.Path(tmp)
    (root / ".project" / "config").mkdir(parents=True)
    (root / ".project" / "config" / "project.yaml").write_text(
        project_yaml, encoding="utf-8")
    if export_yaml is not None:
        (root / ".project" / "config" / "export.yaml").write_text(
            export_yaml, encoding="utf-8")
    return root


class TestConfig(unittest.TestCase):
    def test_metadata_comes_from_project_yaml(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_config(_project(tmp))
        self.assertEqual(cfg.metadata.title, "Deuses Entre Nós")
        self.assertEqual(cfg.metadata.author, "Rafhael Marsigli")
        self.assertEqual(cfg.metadata.author_last, "Marsigli")
        self.assertEqual(cfg.metadata.audience, "adulto")
        self.assertEqual(cfg.metadata.genre, "ficção especulativa")
        self.assertEqual(cfg.layout, "chapter")

    def test_profile_falls_back_to_builtin_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_config(_project(tmp))
        profile = cfg.profiles["submission"]
        self.assertEqual(profile.font, "Courier New")   # from export.yaml
        self.assertEqual(profile.leading, "double")     # from the default
        self.assertEqual(profile.margins, "2.54cm")
        self.assertIn("Nimbus Roman", profile.font_fallback)

    def test_reading_profile_exists_even_when_unconfigured(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_config(_project(tmp))
        self.assertIn("reading", cfg.profiles)
        self.assertEqual(cfg.profiles["reading"].formats, ["epub", "pdf"])

    def test_labels_merge_over_language_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_config(_project(tmp))
        self.assertEqual(cfg.labels["wordcount"], "Contagem de palavras")
        self.assertEqual(cfg.labels["byline"], "por")

    def test_missing_export_yaml_is_not_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_config(_project(tmp, export_yaml=None))
        self.assertEqual(cfg.profiles["submission"].font, "Times New Roman")
        self.assertTrue(cfg.contact.is_empty)

    def test_missing_title_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _project(tmp, project_yaml='author: "X"\nlanguage: en\n')
            with self.assertRaises(ConfigError):
                load_config(root)

    def test_unfilled_template_placeholder_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _project(tmp,
                            project_yaml='title: "{Title}"\nauthor: "X"\n')
            with self.assertRaises(ConfigError):
                load_config(root)

    def test_default_labels_per_language(self):
        self.assertEqual(default_labels("en")["byline"], "by")
        self.assertEqual(default_labels("pt-BR")["byline"], "por")
        self.assertEqual(default_labels("es")["byline"], "by")

    def test_number_formatting_follows_language(self):
        self.assertEqual(format_number(80000, "pt-BR"), "80.000")
        self.assertEqual(format_number(80000, "en"), "80,000")

    def test_loads_the_real_book(self):
        book = pathlib.Path("/home/rafhael/projects/books/gods-between-us")
        if not book.is_dir():
            self.skipTest("reference book not present")
        cfg = load_config(book)
        self.assertEqual(cfg.layout, "chapter")
        self.assertEqual(cfg.naming, "{act}.{n}.md")
        self.assertEqual(cfg.metadata.author_last, "Marsigli")


if __name__ == "__main__":
    unittest.main()
