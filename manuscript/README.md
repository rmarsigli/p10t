# Manuscript

Your chapters live here, in plain markdown.

---

## Layout

Two arrangements, declared in `.project/config/project.yaml` → `paths.layout`. **Declared, never guessed** — skills resolve chapter files from that field, and a wrong guess produces a partial chapter list instead of an error.

### `flat` — every chapter file in this directory

```
manuscript/
├── 01.01.md
├── 01.01_analysis.md
├── 01.02.md
└── 01.02_analysis.md
```

### `chapter` — one directory per chapter, named the chapter id

```
manuscript/
├── 01.01/
│   ├── 01.01.md
│   ├── 01.01_outline.md
│   └── 01.01_analysis.md
└── 01.02/
    ├── 01.02.md
    └── 01.02_analysis.md
```

`flat` is right below ~15 chapters. `chapter` earns itself once each chapter carries an outline, an analysis, and a draft — a 32-chapter book is otherwise ~130 files in one directory.

Note that the chapter file **repeats its id** inside its own directory (`01.01/01.01.md`, not `01.01/chapter.md`). That is what makes switching layouts a pure file move rather than a rename, so history follows.

Full rules — ordering, act scoping, migration: `.project/templates/layout.md`.

---

## Naming

Default convention: `{act}.{chapter}.md` — e.g. `02.03.md` for Act 2, Chapter 3. A book without acts uses `{chapter}.md`.

**Zero-pad the numbers.** Ordering is lexicographic, so `10` sorts before `2` when unpadded — and reading order is what cross-chapter sweeps and timeline checks depend on.

This gives skills a predictable target when you say "analyze 02.03", in either layout.

If your book has more than one *kind* of chapter (interludes, appendices), add a suffix to the id — `02.03i.md` — rather than a separate numbering sequence. `02.03` < `02.03i` < `02.04` holds in string ordering; a parallel sequence would put reading order and file order out of step.

Record the actual convention in:

- `.project/config/project.yaml` → `paths` and `structure`
- The root `CLAUDE.md` → "Manuscript structure"

---

## Analysis files

By default, `analyze-chapter` writes `{chapter}_analysis.md` **next to the chapter** — this directory under `flat`, the chapter's own directory under `chapter`:

```
02.03/
├── 02.03.md
└── 02.03_analysis.md
```

If you prefer the manuscript folders to hold only prose, switch `paths.analyses` in `project.yaml` to `.project/reports/technical/`. That field is independent of `paths.layout`; every combination works.

---

## Chapter file format

Plain markdown. No front matter required. One `#` per file.

```markdown
# Chapter title

Prose starts here.
```

Formatting conventions for dialogue, scene breaks, and in-world documents belong in `.project/config/style-guide.md` — decide once, apply everywhere.

---

## Scene headers while drafting — optional

A chapter being drafted may carry its scene contracts as `##` headers, each ending in the word budget from the outline:

```markdown
# 3

## 1 · The count — 250

Prose.

## 2 · The six minutes — 900

Prose.

## 3 · Not separating — 450
```

The last header sits over an empty section on purpose: you write *under* a budget rather than *against* a table in another file. `scripts/scene-budget` reads those headers back and reports words written against words planned.

**They are scaffolding, and scaffolding comes down.** When the chapter is finished the `##` headers are deleted and only the `#` survives — that removal is the signal that the chapter is done, not a chore bolted onto export.

### The rule that matters, and it binds the agent

> **A chapter with no scene headers is a choice, not an omission. Never ask for them, never flag their absence, never add them unprompted.**

Plenty of chapters are written straight through, and the author is the one who decides which. `scene-budget` reports such a file as a plain word count with no warning, and every skill that reads a chapter does the same. Treating a missing header as a defect would turn an optional aid into a demand — and a tool that nags about its own conventions stops being used.

The corollary: **do not read structural meaning into the headers either.** They are a drafting aid. A chapter's real structure is what the prose does, which is what `restructure-chapter` and `check-arc` judge — from the page, never from the markup.
