"""Builds the clean markdown handed to pandoc.

Scene breaks and the title page are emitted per target format: no plain
markdown construct centres a line in typst, docx and epub alike, and a
scene-break marker that is not centred means nothing.
"""
import datetime
import re

from .config import format_number

_FORBIDDEN = re.compile(r'[<>:"/\\|?*]+')
_SPACES = re.compile(r"\s+")
_TYPST_SPECIAL = re.compile(r"([\\#\[\]$@*_])")
_MARKDOWN_SPECIAL = re.compile(r"([#*_~>|+-])")

OPENXML_PAGE_BREAK = (
    "```{=openxml}\n"
    '<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n'
    "```"
)


def slugify(text):
    """Strip what Windows forbids in a filename and collapse whitespace."""
    cleaned = _FORBIDDEN.sub(" ", text)
    cleaned = _SPACES.sub(" ", cleaned).strip()
    return cleaned.replace(" ", "-")


def typst_escape(text):
    return _TYPST_SPECIAL.sub(r"\\\1", str(text))


def markdown_escape(text):
    """Escape a scene-break marker so pandoc reads it as text.

    A bare "#" on its own line is an empty heading, and "* * *" is a
    horizontal rule. Either one silently swallows the marker.
    """
    return _MARKDOWN_SPECIAL.sub(r"\\\1", str(text))


def round_wordcount(n):
    """Round the way a title page states a length: never spuriously exact."""
    if n < 10000:
        return int(round(n / 100.0) * 100)
    return int(round(n / 1000.0) * 1000)


def output_name(cfg, profile, extension):
    stamp = datetime.date.today().strftime("%Y-%m")
    if profile.name == "submission":
        stem = "%s_%s_%s" % (slugify(cfg.metadata.author_last),
                             slugify(cfg.metadata.title), stamp)
    else:
        stem = slugify(cfg.metadata.title).lower()
    return "%s.%s" % (stem, extension)


def _scene_break(marker, fmt):
    if fmt == "typst":
        return ("```{=typst}\n#v(1em)\n#align(center)[%s]\n#v(1em)\n```"
                % typst_escape(marker))
    if fmt == "docx":
        return ('::: {custom-style="SceneBreak"}\n%s\n:::'
                % markdown_escape(marker))
    return '<p class="scene-break">%s</p>' % marker


def _page_break(fmt):
    if fmt == "typst":
        return "```{=typst}\n#pagebreak()\n```"
    if fmt == "docx":
        return OPENXML_PAGE_BREAK
    return ""


def _title_text(cfg, profile):
    return cfg.metadata.title.upper() if profile.title_case == "upper" \
        else cfg.metadata.title


def _contact_lines(cfg):
    contact = cfg.contact
    lines = [contact.name or cfg.metadata.author]
    lines.extend(contact.address)
    if contact.phone:
        lines.append(contact.phone)
    if contact.email:
        lines.append(contact.email)
    return lines


def _title_page_parts(cfg, profile, words):
    """Return the title page as (element, [lines]) pairs, in order."""
    parts = []
    for element in profile.title_page:
        if element == "contact":
            if not cfg.contact.is_empty:
                parts.append(("contact", _contact_lines(cfg)))
        elif element == "wordcount":
            parts.append(("wordcount", ["%s: %s" % (
                cfg.labels["wordcount"],
                format_number(round_wordcount(words), cfg.metadata.language))]))
        elif element == "title":
            parts.append(("title", [_title_text(cfg, profile)]))
        elif element == "byline":
            parts.append(("byline", ["%s %s" % (cfg.labels["byline"],
                                                cfg.metadata.author)]))
        elif element == "audience" and cfg.metadata.audience:
            parts.append(("audience", [cfg.metadata.audience]))
        elif element == "genre" and cfg.metadata.genre:
            parts.append(("genre", [cfg.metadata.genre]))
    return parts


def render_title_page(cfg, profile, words, fmt):
    parts = _title_page_parts(cfg, profile, words)
    if fmt != "typst":
        return "\n\n".join("\\\n".join(lines) for _, lines in parts)

    def block(name):
        for element, lines in parts:
            if element == name:
                return " \\\n".join(typst_escape(line) for line in lines)
        return None

    head_left = block("contact") or ""
    head_right = block("wordcount") or ""
    centre = [block("title"), block("byline")]
    foot = [block("audience"), block("genre")]

    out = ["```{=typst}", "#[", "  #set align(top)"]
    if head_left or head_right:
        out.append("  #grid(columns: (1fr, 1fr), gutter: 1em,")
        out.append("    align(left)[%s]," % head_left)
        out.append("    align(right)[%s]," % head_right)
        out.append("  )")
    out.append("  #v(10em)")
    for line in centre:
        if line:
            out.append("  #align(center)[%s]" % line)
            out.append("  #v(1.5em)")
    if any(foot):
        out.append("  #v(1fr)")
        out.append("  #align(right)[%s]"
                   % " \\\n".join(line for line in foot if line))
    out.append("]")
    out.append("```")
    return "\n".join(out)


def render_body(chapters, profile, fmt):
    parts = []
    for index, chapter in enumerate(chapters):
        # Typst starts chapters on a new page through a show rule, and EPUB
        # reflows, so only docx needs the break spelled out here.
        if fmt == "docx" and index > 0:
            parts.append(OPENXML_PAGE_BREAK)
        parts.append("# %s" % chapter.title)
        for block in chapter.blocks:
            if block.kind == "scene_break":
                parts.append(_scene_break(profile.scene_break, fmt))
            else:
                parts.append(block.text)
    return "\n\n".join(parts) + "\n"


def render_document(cfg, profile, chapters, fmt):
    body = render_body(chapters, profile, fmt)
    if fmt == "epub":
        # pandoc builds the EPUB title page from the metadata it is given.
        return body
    words = sum(chapter.words for chapter in chapters)
    title_page = render_title_page(cfg, profile, words, fmt)
    return "%s\n\n%s\n\n%s" % (title_page, _page_break(fmt), body)
