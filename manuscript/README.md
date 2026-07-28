# Manuscript

Your chapters live here, in plain markdown.

---

## Suggested structure

```
manuscript/
├── Act 01/
│   ├── 01.01.md
│   ├── 01.02.md
│   └── ...
├── Act 02/
│   └── ...
└── Interludes/
    └── ...
```

Adjust to your book. Record the actual convention in:
- `.project/config/project.yaml` → `paths` and `structure`
- The root `CLAUDE.md` → "Manuscript structure"

---

## Naming

Default convention: `{act}.{chapter}.md` — e.g. `02.03.md` for Act 2, Chapter 3.

This makes chapters sort correctly and gives skills a predictable target when you say "analyze 02.03".

---

## Analysis files

By default, `analyze-chapter` writes `{chapter}_analysis.md` **next to the chapter**:

```
Act 02/
├── 02.03.md
└── 02.03_analysis.md
```

If you prefer the manuscript folders to hold only prose, switch `paths.analyses` in `project.yaml` to `.project/reports/technical/`.

---

## Chapter file format

Plain markdown. No front matter required.

```markdown
# Chapter title

Prose starts here.
```

Formatting conventions for dialogue, scene breaks, and in-world documents belong in `.project/config/style-guide.md` — decide once, apply everywhere.
