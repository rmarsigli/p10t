"""Separates prose from scaffolding, and refuses rather than guessing.

A written chapter in this workflow is plain paragraphs and a title. The
presence of scaffolding is not dirt to be cleaned; it is the signal that the
chapter is still a plan. Nothing is ever dropped silently.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

SEPARATORS = r"[-–—·]"

#: "## 2 - Os seis minutos - 900", optionally followed by another
#: separator and a note. The separator set matches scripts/scene-budget.
SCENE_HEADER = re.compile(
    r"^##\s+\S+\s*" + SEPARATORS + r"\s*.+?\s*" + SEPARATORS +
    r"\s*[\d.,]+\s*(?:" + SEPARATORS + r".*)?$")

TITLE = re.compile(r"^#\s+(.*\S)\s*$")
LIST_ITEM = re.compile(r"^([-*+]\s|\d+[.)]\s)")
HORIZONTAL_RULE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
EMPHASIS_ONLY = re.compile(r"^(\*\*|__|\*|_).*(\*\*|__|\*|_)$")


@dataclass(frozen=True)
class Refusal:
    line: int
    kind: str
    text: str


@dataclass(frozen=True)
class Block:
    kind: str
    text: str


@dataclass
class ParsedChapter:
    chapter_id: str
    path: Path
    title: str = ""
    blocks: list = field(default_factory=list)
    words: int = 0
    refusals: list = field(default_factory=list)

    @property
    def accepted(self):
        return not self.refusals

    @property
    def scene_breaks(self):
        return sum(1 for block in self.blocks if block.kind == "scene_break")


def count_words(text):
    """Count tokens carrying at least one alphanumeric character.

    A bare em dash opening a line of dialogue is punctuation, not a word,
    and counting it would inflate the figure printed on the title page.
    """
    return sum(1 for token in text.split()
               if any(char.isalnum() for char in token))


def _classify(line):
    """Return a refusal kind for a non-prose line, or None if it is prose."""
    if line.startswith("|"):
        return "table"
    if line.startswith("{"):
        return "placeholder"
    if line.startswith(">"):
        return "quote"
    if HORIZONTAL_RULE.match(line):
        return "rule"
    if LIST_ITEM.match(line):
        return "list"
    if line.startswith("#"):
        return "heading"
    if EMPHASIS_ONLY.match(line):
        return "emphasis-only"
    return None


def parse_chapter(chapter):
    parsed = ParsedChapter(chapter_id=chapter.chapter_id, path=chapter.path)
    text = Path(chapter.path).read_text(encoding="utf-8")

    in_comment = False
    seen_scene = False
    seen_title = False

    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()

        if in_comment:
            parsed.refusals.append(Refusal(number, "comment", line))
            if "-->" in line:
                in_comment = False
            continue
        if line.startswith("<!--"):
            parsed.refusals.append(Refusal(number, "comment", line))
            in_comment = "-->" not in line
            continue

        if not line:
            continue

        if not seen_title:
            match = TITLE.match(line)
            if match:
                parsed.title = match.group(1)
                seen_title = True
                continue

        if SCENE_HEADER.match(line):
            if seen_scene:
                parsed.blocks.append(Block("scene_break", ""))
            seen_scene = True
            continue

        kind = _classify(line)
        if kind:
            parsed.refusals.append(Refusal(number, kind, line))
            continue

        parsed.blocks.append(Block("paragraph", line))

    if not parsed.title:
        # A chapter with no heading still has to start on its own page.
        parsed.title = parsed.chapter_id

    parsed.words = sum(count_words(block.text) for block in parsed.blocks
                       if block.kind == "paragraph")
    return parsed
