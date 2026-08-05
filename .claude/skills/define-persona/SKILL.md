---
name: define-persona
description: Builds or updates the author's voice document (.project/config/persona.md) by extracting hypotheses from their corpus and refining them through interview — the persona is extracted, not invented. Runs in bootstrap mode (first build) or update mode (incorporate learnings). Use when the user asks to define or update their persona, or to work on their voice.
---

# Skill: define-persona

**What it does.** Builds or updates `.project/config/persona.md` — the document defining the author's voice. It is the foundation of the system: `draft-scene` writes from it, `analyze-chapter` refuses to flag what it declares as signature, `review-revision` feeds it new discoveries.

**Triggers**
- "define my persona"
- "/define-persona"
- "update the persona with what we learned"
- "let's work on the voice"
- Equivalent phrasing in the project's output language

**Input.** Mode: `bootstrap` (first build) or `update` (incorporate learnings).

**Output.** `.project/config/persona.md` created or updated.

> **Write the persona document in the project's output language.** Its examples are quotes from the author's own text, so it must live in that language.

---

## Why this skill exists

Without a defined persona, the AI writes generic literary prose. With one, it writes **as this author would write in this book**.

The difference is not cosmetic: it separates "text that needs cleaning afterwards" from "text born inside the voice".

---

## Core principle

> **The persona is not invented — it is extracted.**

Do not ask "how do you want to write?". Ask "what have you already written, and what in it is you?".

Two sources:
1. **Corpus** — text the author has already written, especially passages they confirmed as theirs
2. **Decisions** — the `R:` annotations in analysis files. Every "kept it" is gold

The interview exists to **confirm and refine**, not to build from nothing.

---

## Protocol: bootstrap mode

### Step 1 — Corpus analysis

Before asking anything, read:

1. **The cleanest chapters** — lowest AI density. This is where the author's voice shows with least noise.
2. **Already-revised chapters** — post-revision text is the consolidated voice.
3. **Every `_analysis.md` with `R:` annotations** (search **recursively** — under `chapter` layout they sit inside each chapter's directory) — each "kept it" is a style declaration.
4. **Earlier writing produced without AI assistance**, if any — the most valuable corpus available.

Extract:
- Characteristic vocabulary (what they use that is not generic)
- Syntactic constructions they defended
- Register (formal, colloquial, mixed)
- Slang, regionalism, profanity
- Typical sentence and paragraph length
- How they do humour
- How they handle emotion (show or name)
- How they close chapters

### Step 2 — Draft the persona

Produce a **filled-in** `persona.md`, with inferences marked:

> **[HYPOTHESIS]** You prefer elevated vocabulary over colloquial equivalents. Confirm?

**Never hand over a blank form.** The author corrects faster than they fill in.

### Step 3 — Refinement interview

Ask questions that are **specific and anchored in examples from their own text**, never generic.

❌ "What tone do you prefer?"
✅ "In chapter X you write in short sentences with a lot of white space. In Y the sentences are long and chained. Is that a conscious per-scene variation, or is X closer to *you*?"

Areas to cover, **one at a time** (do not dump everything at once):

**a) Vocabulary** — register level; words they love and want preserved; words they hate; slang and regionalism; profanity.

**b) Syntax** — long or short sentences and why they vary; dense or airy paragraphs; use of fragments; subordination vs. coordination.

**c) Personal signatures** — constructions they recognize as their own; tics they accept; tics they want gone.

**d) Tone** — how much irony and what kind; sentimentality; how they handle pain, death, loss; type of humour.

**e) Craft** — show or name emotion; dense or economical description; naturalistic or stylized dialogue; chapter endings.

**f) Anti-persona** — what they do **not** want to sound like; authors they consider bad and why; vices they recognize and avoid.

### Step 4 — Write `persona.md`

Structure in `.project/templates/persona-template.md`.

Every section needs **literal examples from the author's text**. "Cynical-but-tender tone" does not help generation. A real paragraph of theirs does.

### Step 5 — Validate

Present it and ask: "Is this you?" / "What is wrong?" / "What is missing?"

Iterate until they recognize their own voice in the document.

---

## Protocol: update mode

### Step 1 — Collect learnings

- `.project/reports/revision-log.md`
- New `_analysis.md` files with `R:` annotations
- Chapters revised since the last update

### Step 2 — Identify emerging patterns

- Signatures confirmed repeatedly ("kept it" on the same construction type, 3+ times)
- Substitution preferences (consistently swapping X for Y)
- New flagged words they reject
- Tonal evolution across parts of the book

### Step 3 — Propose changes

Present diffs; do not rewrite silently:

> "You kept antithetical constructions in 4 of the 5 revised chapters, always at turning points. I suggest moving that from 'signatures to watch' to 'personal signatures'. Agreed?"

### Step 4 — Apply and version

Update `persona.md`. Keep a changelog at the end — voice evolves, and the history matters.

---

## Critical rules

1. **Extract before asking.** Arrive with hypotheses, not a form.

2. **Anchor in real examples.** Every claim about the voice comes with a quote from their text.

3. **Distinguish author voice from narrator voice.** An author writes different narrators. The persona is what persists across them — the taste, not the mask. Record what is specific to this book.

4. **Do not normalize.** The goal is not to make the author write "well" by some standard. It is to capture how they write. Elevated vocabulary is a signature, not a defect.

5. **The persona is alive.** Not a final document. It has a date, a version, and a changelog.

6. **Persona ≠ style guide.** The persona **describes** how the author writes. `style-guide.md` **prescribes** project rules. Different files.

---

## Relationship to other skills

| Skill | How it uses the persona |
|---|---|
| `draft-scene` | Primary context. Without a solid persona, output is generic |
| `analyze-chapter` | Reads "personal signatures" to avoid flagging style as tic |
| `review-revision` | Feeds the persona new discoveries |
| `consolidate-style` | Refines it automatically from decision history |
