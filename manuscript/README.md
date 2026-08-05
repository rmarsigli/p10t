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

Plain markdown. No front matter required.

```markdown
# Chapter title

Prose starts here.
```

Formatting conventions for dialogue, scene breaks, and in-world documents belong in `.project/config/style-guide.md` — decide once, apply everywhere.
