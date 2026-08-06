import sys, pathlib, shutil, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from p10t_export.engines import (find_tool, install_hint, run_pandoc,
                                 EngineError, MissingTool)


class TestDetection(unittest.TestCase):
    def test_missing_tool_is_none(self):
        self.assertIsNone(find_tool("definitely-not-a-real-binary-xyz"))

    def test_hint_names_all_three_platforms(self):
        hint = install_hint("typst")
        for token in ("Windows", "macOS", "Linux"):
            self.assertIn(token, hint)

    def test_typst_hint_says_no_latex_is_needed(self):
        hint = install_hint("typst")
        self.assertIn("LaTeX", hint)
        self.assertIn("winget", hint)
        self.assertIn("brew", hint)

    def test_pandoc_hint_mentions_the_installers(self):
        hint = install_hint("pandoc")
        self.assertIn(".msi", hint)
        self.assertIn(".pkg", hint)

    def test_missing_tool_error_carries_the_hint(self):
        with self.assertRaises(MissingTool) as ctx:
            raise MissingTool("typst")
        self.assertEqual(ctx.exception.tool, "typst")
        self.assertIn("winget", str(ctx.exception))


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestPandoc(unittest.TestCase):
    def test_produces_a_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp) / "in.md"
            source.write_text("# 1\n\nProse.\n", encoding="utf-8")
            dest = pathlib.Path(tmp) / "out.docx"
            run_pandoc(shutil.which("pandoc"), source, dest, [])
            self.assertTrue(dest.exists())

    def test_error_carries_stderr(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp) / "in.md"
            source.write_text("x\n", encoding="utf-8")
            dest = pathlib.Path(tmp) / "out.pdf"
            with self.assertRaises(EngineError) as ctx:
                run_pandoc(shutil.which("pandoc"), source, dest,
                           ["--pdf-engine=definitely-not-real"])
            self.assertTrue(str(ctx.exception).strip())


if __name__ == "__main__":
    unittest.main()
