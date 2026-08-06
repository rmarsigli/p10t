"""Finds and runs the external tools. pandoc is required; typst is not."""
import shutil
import subprocess
from pathlib import Path


HINTS = {
    "pandoc": (
        "  Windows  install the .msi from https://github.com/jgm/pandoc/releases\n"
        "  macOS    install the .pkg from the same page, or: brew install pandoc\n"
        "  Linux    apt install pandoc, or the .deb from the releases page"
    ),
    "typst": (
        "  Windows  winget install --id Typst.Typst\n"
        "  macOS    brew install typst\n"
        "  Linux    download the release archive from\n"
        "           https://github.com/typst/typst/releases and put it on PATH\n"
        "\n"
        "  Typst is one self-contained binary of about 15 MB and needs no root.\n"
        "  You do NOT need LaTeX or MiKTeX, whatever pandoc's own install page\n"
        "  says: this script passes --pdf-engine=typst and never calls LaTeX."
    ),
}


def install_hint(tool):
    return HINTS.get(tool, "  see docs/export.md")


class MissingTool(Exception):
    def __init__(self, tool):
        self.tool = tool
        super().__init__("%s is not installed.\n%s" % (tool, install_hint(tool)))


class EngineError(Exception):
    pass


def find_tool(name):
    return shutil.which(name)


def run_pandoc(pandoc, source, dest, extra):
    command = [pandoc, str(Path(source)), "-o", str(Path(dest))] + list(extra)
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    if process.returncode != 0:
        message = stderr.decode("utf-8", "replace").strip()
        raise EngineError(message or
                          "pandoc exited with status %d" % process.returncode)
