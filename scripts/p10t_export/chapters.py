"""Chapter resolution, enumeration and ordering.

The rules live in .project/templates/layout.md and are implemented only
here. Layout is declared, never detected: a wrong guess does not fail, it
returns a partial book, and everything downstream inherits the lie.
"""
import re
from dataclasses import dataclass
from pathlib import Path

_FIELD = re.compile(r"\{[^}]*\}")


class LayoutError(Exception):
    pass


class MixedLayoutError(LayoutError):
    def __init__(self, loose, dirs):
        self.loose = list(loose)
        self.dirs = list(dirs)
        super().__init__(
            "the manuscript is in a mixed layout state and will not be "
            "resolved.\n"
            "  loose chapter files: %s\n"
            "  chapter directories: %s\n"
            "Move one form to the other and set paths.layout to match, in a "
            "single chore: commit." % (
                ", ".join(p.name for p in self.loose),
                ", ".join(p.name for p in self.dirs)))


@dataclass(frozen=True)
class ChapterFile:
    chapter_id: str
    path: Path


def naming_regex(naming):
    """Turn paths.naming into a regex matching a chapter id (the stem).

    Every {field} becomes one number with an optional alphabetic suffix:
    layout.md makes any kind-marking suffix part of the id, and the
    resolver only ever sorts it.
    """
    stem = naming[:-3] if naming.endswith(".md") else naming
    literals = _FIELD.split(stem)
    fields = _FIELD.findall(stem)
    pieces = []
    for index, literal in enumerate(literals):
        pieces.append(re.escape(literal))
        if index < len(fields):
            pieces.append("[0-9]+[A-Za-z]*")
    return re.compile("^" + "".join(pieces) + "$")


def find_chapters(manuscript, layout, naming):
    manuscript = Path(manuscript)
    if not manuscript.is_dir():
        raise LayoutError("manuscript directory not found: %s" % manuscript)
    rx = naming_regex(naming)

    loose = [p for p in sorted(manuscript.glob("*.md")) if rx.match(p.stem)]
    dirs = [p for p in sorted(manuscript.iterdir())
            if p.is_dir() and rx.match(p.name)]

    if loose and dirs:
        raise MixedLayoutError(loose, dirs)

    if layout == "flat":
        return [ChapterFile(p.stem, p) for p in loose]

    if layout != "chapter":
        raise LayoutError(
            "unknown paths.layout: %r (expected flat or chapter)" % layout)

    found = []
    for directory in dirs:
        chapter_file = directory / (directory.name + ".md")
        if not chapter_file.is_file():
            raise LayoutError(
                "chapter directory %s has no %s inside it. The chapter file "
                "must repeat the directory's id." % (directory.name,
                                                     chapter_file.name))
        found.append(ChapterFile(directory.name, chapter_file))
    return sorted(found, key=lambda chapter: chapter.chapter_id)
