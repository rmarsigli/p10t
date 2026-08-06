"""Generates the per-format templates from a profile.

Nothing binary ships in the repository: the Word reference document is
derived from pandoc's own default and patched, at run time, into the output
directory. A hand-written template in .project/templates/export/ wins over
anything generated here.
"""
import re
import subprocess
import zipfile
from pathlib import Path

TYPST = """\
#let body-font = {font}

#set page(
  paper: "a4",
  margin: {margins},
  header: context {{
    // Not named `page`: that would shadow typst's own page element and
    // break `counter(page)` below.
    let current = counter(page).get().first()
    if current > 1 [
      #set text(font: body-font, size: {size})
      #align(right)[{running_head}]
    ]
  }},
)
#set text(font: body-font, size: {size}, lang: "{lang}", hyphenate: {hyphenate})
#set par(leading: {leading}, first-line-indent: {indent}, justify: false)

#show heading.where(level: 1): it => {{
  pagebreak(weak: true)
  v(4em)
  align(center)[#text(weight: "regular", size: {size})[#it.body]]
  v(2em)
}}

$body$
"""

CSS = """\
body {{
  font-family: {font};
  line-height: {line_height};
}}
h1 {{
  text-align: center;
  font-weight: normal;
  margin: 3em 0 2em 0;
}}
p {{
  text-indent: {indent};
  margin: 0;
}}
h1 + p {{
  text-indent: 0;
}}
.scene-break {{
  text-align: center;
  text-indent: 0;
  margin: 1.5em 0;
}}
"""

SCENE_BREAK_STYLE = (
    '<w:style w:type="paragraph" w:customStyle="1" w:styleId="SceneBreak">'
    '<w:name w:val="SceneBreak"/>'
    '<w:basedOn w:val="BodyText"/>'
    '<w:pPr>'
    '<w:spacing w:before="240" w:after="240"/>'
    '<w:ind w:firstLine="0"/>'
    '<w:jc w:val="center"/>'
    '</w:pPr>'
    '</w:style>'
)


def leading_to_typst(leading):
    """Typst's leading is the gap between lines, not the line height."""
    if str(leading).lower() == "double":
        return "1em"
    try:
        return "%gem" % (float(leading) * 0.5)
    except (TypeError, ValueError):
        return "0.65em"


def _lang(language):
    return (language or "en").split("-")[0]


def font_chain(profile):
    """The requested font first, then metric-compatible substitutes.

    Times New Roman and Courier New ship with Windows and macOS and with
    neither Linux nor most CI images. Without a chain, typst warns and
    silently falls back to its own default, which is not the typeface the
    profile asked for.
    """
    names = [profile.font]
    names.extend(name for name in getattr(profile, "font_fallback", [])
                 if name not in names)
    return names


def typst_font(profile):
    names = font_chain(profile)
    if len(names) == 1:
        return '"%s"' % names[0]
    return "(%s)" % ", ".join('"%s"' % name for name in names)


def typst_template(cfg, profile):
    head = (profile.running_head
            .replace("{author_last}", cfg.metadata.author_last)
            .replace("{title}", cfg.metadata.title)
            .replace("{page}", "#counter(page).display()"))
    return TYPST.format(
        margins=profile.margins,
        size=profile.size,
        font=typst_font(profile),
        lang=_lang(cfg.metadata.language),
        hyphenate="true" if profile.hyphenate else "false",
        leading=leading_to_typst(profile.leading),
        indent=profile.indent,
        running_head=head,
    )


def epub_css(profile):
    line_height = "2" if str(profile.leading).lower() == "double" \
        else str(profile.leading)
    family = ", ".join('"%s"' % name for name in font_chain(profile))
    return CSS.format(font=family + ", serif", line_height=line_height,
                      indent=profile.indent)


def resolve_override(root, filename):
    """A hand-written template beats anything generated."""
    candidate = Path(root) / ".project" / "templates" / "export" / filename
    return candidate if candidate.is_file() else None


def _half_points(size):
    return int(round(float(str(size).replace("pt", "").strip()) * 2))


def derive_reference_docx(profile, pandoc, dest):
    """Patch pandoc's own default reference.docx with the profile's typography.

    The default archive carries the font as w:ascii/w:hAnsi, the size as w:sz
    in half-points, and the line spacing as w:spacing w:line in twentieths of
    a point. Patching it keeps the repository free of binaries.
    """
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    default = dest.with_name(dest.stem + ".default.docx")
    with default.open("wb") as handle:
        subprocess.check_call(
            [pandoc, "--print-default-data-file", "reference.docx"],
            stdout=handle)

    size = _half_points(profile.size)
    line = "480" if str(profile.leading).lower() == "double" else "240"

    source = zipfile.ZipFile(default)
    try:
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as out:
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "word/styles.xml":
                    xml = data.decode("utf-8")
                    xml = re.sub(r'w:ascii="[^"]*"',
                                 'w:ascii="%s"' % profile.font, xml)
                    xml = re.sub(r'w:hAnsi="[^"]*"',
                                 'w:hAnsi="%s"' % profile.font, xml)
                    xml = re.sub(r'<w:sz w:val="\d+"\s*/>',
                                 '<w:sz w:val="%d"/>' % size, xml)
                    xml = re.sub(r'(<w:spacing[^/>]*?)w:line="\d+"',
                                 r'\1w:line="%s"' % line, xml)
                    xml = xml.replace("</w:styles>",
                                      SCENE_BREAK_STYLE + "</w:styles>")
                    data = xml.encode("utf-8")
                out.writestr(item, data)
    finally:
        source.close()
        default.unlink()
    return dest
