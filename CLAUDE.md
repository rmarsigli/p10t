# CLAUDE.md — {BOOK TITLE}

> Replace `{BOOK TITLE}` and adjust the marked sections. This file teaches the AI agent how to use this project.

This project uses [p10t](https://github.com/{user}/p10t): skills in `.claude/skills/`, book knowledge in `.project/`.

---

## Language

**System language:** English (skills, templates).
**Output language:** defined in `.project/config/project.yaml` under `language`.

All generated content — analyses, reports, drafts, feedback — must be written in the **output language**, not in English. The English is only for the machinery.

---

## Layout

Two roots, one job each:

- **`.claude/skills/`** — what the system **does**. Seventeen skills, auto-discovered by Claude Code. Generic: identical across all books.
- **`.project/`** — what the system **knows**. Config (persona, references, style guide), knowledge (world, characters, timeline), reports (analyses, preserve list, recurrence map), templates. Book-specific.

Skills read from and write to `.project/`; the manuscript lives in `manuscript/`.

## Skills

| Skill | Triggered by |
|---|---|
| **init-project** | "set up this book", "start a new book here" |
| **analyze-chapter** | "analyze chapter X", "check chapter X for AI tics" |
| **scan-recurrences** | "find duplications", "what repeats across chapters" |
| **review-revision** | "check my notes and chapter X", "review my revision" |
| **define-persona** | "define my persona", "let's work on the voice" |
| **define-references** | "define the references", "add {author} as a reference" |
| **build-worldbuilding** | "build the worldbuilding", "extract the world rules" |
| **create-character** | "create/extract/develop {character}" |
| **outline-chapter** | "outline chapter X" |
| **draft-scene** | "draft scene N of chapter X" |
| **revise-passage** | "revise this passage", "rework this dialogue" |
| **expand-beat** | "expand this beat", "turn this note into a scene" |
| **review-book** | "review the book", "run the full report" |
| **check-consistency** | "check consistency", "does chapter X contradict anything" |
| **check-arc** | "check the arcs", "is {character}'s arc landing" |
| **update-preserve-list** | "update the preserve list" |
| **consolidate-style** | "consolidate the style", "what have you learned about my voice" |

Users may invoke skills in the output language — match by intent, not exact wording. In environments without skill auto-discovery, read the matching `.claude/skills/<name>/SKILL.md` and follow it literally.

## Standard workflow

The chapter revision cycle:

1. `analyze-chapter` produces `{chapter}_analysis.md`
2. The author reads, decides item by item, annotates `**R:**` under each point
3. The author rewrites the chapter
4. `review-revision` evaluates the result and answers the author's questions
5. Learnings feed `persona.md` and `preserve-list.md`

At the end of each Act: `scan-recurrences`, `check-consistency`, `check-arc`, and optionally `review-book`.

## Manuscript structure

> **Adjust this section** to match your actual organization.

- Manuscript in `manuscript/`, plain markdown, one file per chapter
- Naming: `{act}.{chapter}.md` (e.g. `02.03.md`)

## Operating notes

- The author writes in plain markdown, versioned in git.
- **Active human curation:** the AI proposes, the author decides. Accept/reject annotations are marked with `**R:**` inside analysis files.
- Phrases listed in `.project/reports/preserve-list.md` are **never** suggested for cutting.
- Constructions listed under "Personal signatures" in `.project/config/persona.md` are **never** flagged as tics.
- Generated drafts go to `_draft` files — **never** directly into manuscript files.
- Quality target: defined by the author in `.project/config/style-guide.md`.
