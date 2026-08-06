# Export

Turns the manuscript into the three files you actually send: a `.docx` for
agents, an `.epub` for beta readers, a `.pdf` for print.

```sh
scripts/export
```

---

## You do not need LaTeX

pandoc's own installation page says it makes PDFs with LaTeX and recommends
installing MiKTeX or MacTeX. **Ignore that here.** This script passes
`--pdf-engine=typst` and never calls LaTeX. Typst is a single self-contained
binary of about 15 MB.

Installing a gigabyte of TeX would do nothing for you.

## What you get with what you have installed

| Output | Used for | Requires |
|---|---|---|
| `.docx` | submitting to an agent or publisher | pandoc |
| `.epub` | sending to a beta reader | pandoc |
| `.pdf` | printing, or a fixed artifact | pandoc **and** typst |

`.docx` is what agents ask for. PDF cannot be annotated, and annotating is
what an editor does with your file — so unless a submission page explicitly
asks for PDF, send the Word file.

`.epub` is the right thing for a beta reader. It reflows, so it fits a phone
or an e-reader; a PDF makes them pinch and zoom.

**Without typst**, the other two formats are still written and the PDF is
skipped with a note. Nothing else in p10t depends on this script: delete it
and every skill still works.

## Installing

**pandoc** (required)

```
Windows  install the .msi from https://github.com/jgm/pandoc/releases
macOS    install the .pkg from the same page, or: brew install pandoc
Linux    apt install pandoc, or the .deb from the releases page
```

**typst** (only for PDF)

```
Windows  winget install --id Typst.Typst
macOS    brew install typst
Linux    download the release archive from
         https://github.com/typst/typst/releases and put it on PATH
```

Typst needs no root and no system libraries. Typst 0.11 or newer is required.

**Python 3.8+** — already present on most Linux systems. On Windows install
it from python.org; on macOS the first `python3` prompts to install the
Command Line Tools.

## Running it

```sh
scripts/export                        # both profiles, everything
scripts/export --profile submission   # .docx and .pdf
scripts/export --profile reading      # .epub and .pdf
scripts/export --out ~/Desktop/book   # somewhere other than export/
scripts/export --dump-templates       # write the templates and stop
scripts/export --root ../other-book   # a project other than this directory
scripts/export --quiet                # print nothing but errors
```

Output lands in `export/`, which is already git-ignored.

Exit codes: **0** everything written, **1** nothing written, **2** partial —
a chapter was refused, or the PDF was skipped for want of typst.

### The two profiles

**`submission`** is standard manuscript format: Times New Roman 12 pt, double
spaced, one-inch margins, ragged right and **unhyphenated**, each chapter on
a new page, a running head reading `Surname / Title / page`, and a title page
carrying your contact details and the rounded word count. It is deliberately
plain. It exists to be marked up, not admired.

**`reading`** is a book-shaped copy: a serif face, normal leading, no contact
block and no word count.

## Why a chapter is refused

Only three things are accepted inside a chapter file:

| In the file | Becomes |
|---|---|
| `# 3` | the chapter title, starting a new page |
| an ordinary paragraph, dialogue included | a paragraph |
| `## 2 - The six minutes - 900` | a scene break |

**Anything else refuses the chapter, by name and line number** — tables,
lists, `{ }` placeholders, HTML comments, `---` rules, `>` quotes, and lines
that are entirely bold or italic.

Nothing is ever stripped silently. A chapter still carrying its plan is not a
dirty chapter; it is a chapter that has not been written, and exporting four
surviving lines of it would be worse than refusing.

The fix is the one you already use: move the plan into `{id}_plot.md` and
leave the prose in the chapter file.

```
  01.03    ok        2.629 words, 5 scene breaks
  01.04    REFUSED
           line    3  comment        <!-- ANDAIME. As linhas em { } são...
           line    9  heading        ## Tabela de guia
           line   11  table          | # | Cena | Palavras | Peso |
           ... 100 more scaffolding lines

           This chapter is not written yet. Move the plan to
           01.04_plot.md and leave the prose behind.
```

Two things this deliberately does **not** do:

- **It never asks for scene headers.** A chapter written straight through
  exports as continuous prose, with no warning. Their absence is a choice.
- **It never reads meaning from a filename.** If your book interleaves
  chapter kinds, export does not detect, group, or format them differently.

One surprise worth knowing: a line beginning `- ` is refused as a list. If
you mark dialogue with a hyphen rather than an em dash, pandoc would turn it
into bullet points, so the refusal is protecting you. Use `—`.

## Configuration

Everything optional lives in `.project/config/export.yaml`. With that file
absent, export still runs on built-in defaults.

Title, author, language, genre and audience are **never** repeated there —
they come from `project.yaml`.

### Your contact details

```yaml
contact:
  name: "Your Name"
  address: ["Street 1", "City - ST"]
  phone: "+00 00 0000"
  email: "you@example.com"
```

**This block is committed to the repository**, and git history is not easily
erased. If your book repository may ever be public, leave it empty: the title
page is then generated without the contact block, which is exactly what you
want for a proof copy anyway.

### Labels

The title page prints words, and printed words follow the book's language —
`Word count:` on a Portuguese title page is wrong. Keys stay English, values
do not:

```yaml
labels:
  wordcount: "Contagem de palavras"
  byline: "por"
```

Defaults ship for `pt-BR` and `en`. Other languages inherit English; override
them here. The thousands separator follows the same setting: `80,000` in
English, `80.000` in Portuguese.

### Fonts

Times New Roman and Courier New ship with Windows and macOS and with neither
Linux nor most CI images. Each profile therefore carries a fallback chain of
metric-compatible substitutes:

```yaml
font: "Times New Roman"
font_fallback: ["Nimbus Roman", "Liberation Serif", "DejaVu Serif"]
```

The first one installed wins. Without a chain, typst warns and silently
substitutes its own default, which is not the typeface you asked for.

## Templates and precedence

The script generates every template it needs. To take control of one, put a
file in `.project/templates/export/`:

| File | Overrides |
|---|---|
| `submission.typ`, `reading.typ` | the generated Typst template |
| `epub.css` | the generated EPUB stylesheet |
| `reference.docx` | the derived Word reference document |

**Precedence: a file there → `export.yaml` → the built-in default.**

Start from what the script would have produced:

```sh
scripts/export --dump-templates
```

A `.typ` there is a *pandoc* template, so it must contain `$body$`.

The Word reference document is normally derived at run time from pandoc's own
default and patched with your profile's typography, which is why no binary
ships in this repository. A `reference.docx` you put in that directory is
your own binary, in the one place documented to hold one.

## Tests

```sh
python3 -m unittest discover -s tests -t .
```

Tests that need pandoc or typst skip themselves when the tool is absent.
