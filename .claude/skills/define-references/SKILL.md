---
name: define-references
description: Builds or updates the reference sheets in .project/config/references.md — turning admired authors into concrete borrowing instructions with explicit exclusion lines, so influence seasons the voice without becoming pastiche. Use when the user asks to define references, add an author as a reference, or work on the book's influences.
---

# Skill: define-references

**What it does.** Builds or updates `.project/config/references.md` — the sheets of authors and works informing this book's voice. Turns "I love Murakami" into instructions a generation skill can actually follow.

**Triggers**
- "define the references"
- "/define-references"
- "add {author} as a reference"
- "let's work on the influences"
- Equivalent phrasing in the project's output language

**Input.** Optionally, a starting list of authors/works from the author.

**Output.** `.project/config/references.md`, one sheet per reference.

> **Write the file in the project's output language.**

---

## Core principle

> **A reference is a borrowing instruction, not an homage.**

"I'm inspired by Vonnegut" is a feeling. It cannot be loaded into a generation pass. What can:

> *"From Vonnegut: the flat delivery of catastrophic events — one plain sentence where another author would write a paragraph. NOT the authorial intrusions or the refrain tags — this book's narrator doesn't address the reader."*

Every sheet must answer three questions:
1. **What exactly to take** — a concrete, imitable device
2. **What explicitly NOT to take** — the parts of that author that would poison this book
3. **Where it shows up** — a passage in the manuscript that already does it, or a place it should

The NOT list matters as much as the take list. Influence without exclusions drifts into pastiche.

---

## Protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. `.project/config/references.md` — current state
3. `.project/config/persona.md` — the author's own voice (references complement it, never override it)
4. Manuscript samples, if any exist — to ground "where it shows up"

### Step 2 — Elicit the raw list

Ask the author which authors/works inform **this book** — not their favourites in general. The distinction matters: a beloved author can be irrelevant to this project, and a book the author dislikes can still be a structural reference.

Also ask for **anti-references** directly: *"What should this book never be mistaken for?"*

### Step 3 — Interrogate each reference

This is the heart of the skill. For each author named, do not accept the name — drill until the borrowing is concrete:

**a) Locate the device.** *"When you say {author}, what specifically? A sentence rhythm? A way of handling time? How they enter scenes late? Their dialogue?"*

If the author struggles, offer candidates: name 3–4 recognizable devices of that writer and ask which one resonates. This usually unlocks the real answer, which is often "none of those — it's actually X".

**b) Make it imitable.** Push from adjective to mechanism:
- ❌ "The melancholy tone"
- ✅ "Emotion is never named at the moment it happens — it surfaces two scenes later, in a domestic detail"

The test: could a generation pass follow this instruction without having read the reference author? If not, it is not yet concrete.

**c) Draw the exclusion line.** *"What part of {author} would ruin this book?"* Every strong influence has a poison for a given project. Naming it is what prevents pastiche.

**d) Anchor it.** If a manuscript exists: *"Where do you already do this?"* Quote the passage into the sheet. If nowhere: *"Where should it show up?"* — this doubles as a revision note.

### Step 4 — Check for collisions

References can contradict each other or the persona:
- One reference pulls toward long recursive sentences, another toward telegraphic cuts — when does each apply? (Often the answer is per-register: narrator vs. interludes, calm vs. crisis.)
- A reference device the author already does naturally belongs in `persona.md` as their own signature, not here as borrowed.
- A reference that contradicts a persona signature: surface it, let the author rule.

Record resolution rules in the sheet ("applies only in X contexts").

### Step 5 — Build the anti-reference list

For each anti-reference: what specifically to avoid, stated as detectably as the positive devices. "Not generic epic fantasy" is weak; "no expository worldbuilding in dialogue, no invented-term glossaries" is checkable.

### Step 6 — Validate

Present the sheets. For each, ask: *"If a generation pass followed only this instruction, would the result feel like the influence you meant?"* Iterate on the ones that miss.

---

## What to avoid

**Name-dropping mode.** A list of admired authors with no devices attached. Loads nothing.

**Pastiche instructions.** "Write like {author}" is the failure case, not the goal. References season the author's voice; the persona is the dish.

**Too many references.** Past 5–6 active references, they cancel each other. If the list is long, ask which 3 matter most for *this* book and archive the rest.

**Vague exclusions.** An anti-reference without detectable markers cannot protect anything.

**Confusing reference with persona.** If the author already does the device naturally, it is theirs — move it to `persona.md`. This file is for what is consciously borrowed.

---

## Relationship to other skills

| Skill | How it uses references |
|---|---|
| `draft-scene` | Loads devices as seasoning instructions on top of the persona |
| `define-persona` | Receives devices reclassified as the author's own |
| `review-book` | Uses references for comparable-title reasoning |
| `analyze-chapter` | Anti-reference markers can inform section 15 (other tics) |

---

## Maintenance

- **When the author's revision patterns show an unlisted influence** ("this cut mirrors {author}'s economy"), propose adding it.
- **When a borrowed device becomes habitual** — appearing naturally in the author's unassisted writing — promote it to `persona.md`.
- **Per book.** References are project-specific. A new book inherits nothing automatically; re-run this skill.
