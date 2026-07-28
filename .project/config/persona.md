# Persona — {Your name}

_Version 0 — not yet filled_

> **This file is empty.** Run the `define-persona` skill to populate it.
>
> The skill reads your corpus, extracts hypotheses about your voice, and interviews you to refine them. Do not fill it in manually from scratch — extraction is more accurate than introspection.
>
> Full structure and instructions: `.project/templates/persona-template.md`.

---

## Why this file matters

It is the foundation of the system.

- **`analyze-chapter`** reads the "Personal signatures" section so it does **not** flag your style as a tic.
- **`review-revision`** feeds this file with what it learns from your decisions.
- **`draft-scene`** uses it as primary context. Without a solid persona, output is generic.
- **`consolidate-style`** proposes evidence-backed updates to it from your accumulated decisions.

---

## Before running `define-persona`

Gather, if available:

1. **Earlier writing produced without AI assistance.** Short stories, essays, another book, even long emails. This is the most valuable corpus possible — your voice without noise.
2. **The chapters of this book you consider most "yours".**
3. **Reference authors** and what specifically you take from each (this goes into `references.md`).

---

_Once filled, this file follows the structure in `templates/persona-template.md` and is written in the project's output language._
