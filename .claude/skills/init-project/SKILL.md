---
name: init-project
description: Bootstraps a new book from the p10t template — seven-question interview, populates project.yaml, resets project-specific files, and routes to the right first steps (extraction path for existing manuscripts, creation path for blank pages). Never re-initializes an active project. Use when the user asks to init the project, set up this book, or start a new book.
---

# Skill: init-project

**What it does.** Bootstraps a new book from the p10t template: interviews the author for the essentials, populates `project.yaml`, resets project-specific files to blank templates, and verifies the generic machinery is intact. The first skill run in any new project.

**Triggers**
- "init the project"
- "/init-project"
- "set up this book"
- "start a new book here"
- Equivalent phrasing in any language

**Input.** None — everything is gathered by interview.

**Output.** A configured `.project/`, a filled `project.yaml`, an adjusted root `CLAUDE.md`, and a suggested first-steps plan.

---

## Core principle

> **Ask only what cannot be defaulted. Configure everything the answers imply.**

A bootstrap that asks twenty questions never gets finished. The interview is seven questions or fewer; everything else is derived or left at sensible defaults, explicitly listed at the end so the author knows what to adjust later.

---

## Execution protocol

### Step 1 — Detect the starting state

Check what exists:

- **Fresh clone** (config files still contain `{placeholders}`) → full bootstrap
- **Existing manuscript present** (files in `manuscript/` or elsewhere) → bootstrap + offer the extraction path (Step 5)
- **Already initialized** (`project.yaml` has a real title) → stop; offer to update settings instead of re-initializing. **Never reset an active project.**

### Step 2 — The interview

Seven questions, one message:

1. **Title** (working title is fine)
2. **Output language** — the language of the manuscript and of all generated output. **If it is not `pt-BR` or `en`, say so plainly**: the framework's detection signals are calibrated for those two, and other languages inherit the definitions, ceilings, and treatments but need their signals adapted. Note it in `style-guide.md → Density ceilings → Language adaptation` so analyses stay comparable
3. **Genre and audience** (one line)
4. **Structure** — chapters grouped in acts/parts? Interludes? Rough planned count?
5. **Manuscript location** — use `manuscript/` or point to an existing folder?
6. **Analyses next to chapters, or centralized** in `.project/reports/technical/`?
7. **AI-use stance** — the declaration line for `project.yaml` (offer the default: *"human curation item by item"*)

### Step 3 — Apply

- Fill `project.yaml` completely — including derived fields (naming pattern from the structure answer, paths from Q5–6)
- Update the root `CLAUDE.md`: title, structure section, paths
- Verify project-specific files are blank templates; if this is a copy from a previous book, **list any file still carrying old content** (previous persona, old preserve list) and confirm before clearing each — never silently wipe
- Confirm generic machinery intact: `.claude/skills/`, `.project/templates/`
- Offer to remove the template's own artifacts, which belong to p10t rather than to this book: `examples/`, `manuscript/README.md`, and this repo's `CHANGELOG.md`. Offer, do not delete — some authors keep `examples/` as a reference

### Step 4 — Report the configuration

Show what was set, what was defaulted, and where to change each thing later. One screen.

### Step 5 — Route to the right first step

The fork that matters:

**Existing manuscript** → suggest the extraction sequence:
1. `define-persona` (bootstrap mode — point it at the chapters you consider most yours)
2. `build-worldbuilding` + `create-character` (extract mode)
3. `analyze-chapter` on the first chapter → the revision cycle begins

**Blank page** → suggest the creation sequence:
1. `define-persona` (bootstrap mode — bring earlier writing produced without AI, the most valuable corpus)
2. `define-references`
3. `build-worldbuilding` + `create-character` (create mode)
4. `outline-chapter` → `draft-scene`

Either way, close with: the system starts weak and compounds. The first chapter's cycle teaches the next one.

---

## What to avoid

**Re-initializing an active project.** The one destructive mistake. Detection first, always.

**Silent wiping.** Leftover content from a previous book is listed and confirmed file by file.

**Interview sprawl.** Seven questions. Anything else has a default and a note.

**Configuring beyond knowledge.** Word-count targets, phase tracking, density targets — leave at defaults; they calibrate during use.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| All | This one makes the project they run inside |
| `define-persona` | Always the recommended next step |
