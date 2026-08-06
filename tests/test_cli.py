import io, sys, pathlib, shutil, tempfile, unittest
from contextlib import redirect_stdout, redirect_stderr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.cli import main

PROJECT = """\
language: pt-BR
title: "Deuses Entre Nós"
author: "Rafhael Marsigli"
genre:
  primary: "ficção especulativa"
  audience: "adulto"
paths:
  manuscript: "manuscript/"
  naming: "{act}.{n}.md"
  layout: "flat"
"""

CLEAN = "# 1\n\nO terceiro vidro trincou. Ninguém percebeu.\n"
CLEAN_TWO = "# 2\n\nA cidade esperava do outro lado.\n"
DIRTY = "# 3\n\n| a | b |\n\n{ placeholder }\n"


def _book(tmp, chapters, project=PROJECT):
    root = pathlib.Path(tmp)
    (root / ".project" / "config").mkdir(parents=True)
    (root / ".project" / "config" / "project.yaml").write_text(
        project, encoding="utf-8")
    (root / "manuscript").mkdir()
    for name, text in chapters.items():
        (root / "manuscript" / name).write_text(text, encoding="utf-8")
    return root


def _run(root, *args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = main(["--root", str(root)] + list(args))
    return code, out.getvalue() + err.getvalue()


class TestReporting(unittest.TestCase):
    def test_no_chapter_accepted_exits_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": DIRTY})
            code, output = _run(root, "--profile", "submission")
        self.assertEqual(code, 1)
        self.assertIn("REFUSED", output)

    def test_refusal_lists_line_numbers_and_the_fix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN, "01.02.md": DIRTY})
            _, output = _run(root, "--profile", "submission")
        self.assertIn("line", output)
        self.assertIn("01.02_plot.md", output)
        self.assertIn("table", output)

    def test_accepted_chapter_reports_its_word_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN})
            _, output = _run(root, "--profile", "submission")
        self.assertIn("01.01", output)
        self.assertIn("ok", output)


class TestExitCodes(unittest.TestCase):
    def test_partial_export_exits_two(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN, "01.02.md": DIRTY})
            code, _ = _run(root, "--profile", "submission")
        self.assertEqual(code, 2)

    def test_missing_manuscript_exits_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / ".project" / "config").mkdir(parents=True)
            (root / ".project" / "config" / "project.yaml").write_text(
                PROJECT, encoding="utf-8")
            code, _ = _run(root, "--profile", "submission")
        self.assertEqual(code, 1)

    def test_unfilled_project_yaml_exits_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN},
                         project='title: "{Title}"\nauthor: "X"\n')
            code, output = _run(root, "--profile", "submission")
        self.assertEqual(code, 1)
        self.assertIn("title", output)


class TestTemplates(unittest.TestCase):
    def test_dump_templates_writes_files_without_pandoc(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN})
            code, _ = _run(root, "--profile", "submission", "--dump-templates")
            produced = sorted(p.name for p in (root / "export").iterdir())
        self.assertEqual(code, 0)
        self.assertIn("submission.typ", produced)
        self.assertIn("epub.css", produced)


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestRealOutput(unittest.TestCase):
    def test_submission_produces_a_docx(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN, "01.02.md": CLEAN_TWO})
            code, _ = _run(root, "--profile", "submission")
            produced = list((root / "export").glob("Marsigli_*.docx"))
        self.assertIn(code, (0, 2))
        self.assertEqual(len(produced), 1)

    def test_reading_produces_an_epub_with_correct_metadata(self):
        import zipfile, re
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN, "01.02.md": CLEAN_TWO})
            _run(root, "--profile", "reading")
            produced = list((root / "export").glob("*.epub"))
            self.assertEqual(len(produced), 1)
            archive = zipfile.ZipFile(produced[0])
            opf = [n for n in archive.namelist() if n.endswith(".opf")][0]
            content = archive.read(opf).decode("utf-8")
            chapters = [n for n in archive.namelist()
                        if re.search(r"ch\d+\.xhtml$", n)]
        self.assertIn("Deuses Entre Nós", content)
        self.assertIn("Rafhael Marsigli", content)
        self.assertIn("pt-BR", content)
        self.assertEqual(len(chapters), 2)

    def test_docx_carries_the_title_page_and_a_page_break(self):
        import zipfile
        with tempfile.TemporaryDirectory() as tmp:
            root = _book(tmp, {"01.01.md": CLEAN, "01.02.md": CLEAN_TWO})
            _run(root, "--profile", "submission")
            produced = list((root / "export").glob("Marsigli_*.docx"))
            document = zipfile.ZipFile(produced[0]).read(
                "word/document.xml").decode("utf-8")
        self.assertIn("DEUSES ENTRE NÓS", document)
        self.assertIn('w:type="page"', document)


if __name__ == "__main__":
    unittest.main()
