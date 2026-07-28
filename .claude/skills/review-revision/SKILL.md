---
name: review-revision
description: Evaluates the author's revision of a chapter against the R-annotated analysis file — introduced errors, rewrite quality, inverted problems, residual density, continuity gaps — and explicitly answers every question the author left in their annotations. Use when the user asks to check their notes and a chapter, review their revision, or evaluate their edits.
---

# Skill: review-revision

**What it does.** After the author revises a chapter using an `_analysis.md` annotated with `R:`, this evaluates the result: what works, what needs adjustment, errors introduced during revision, and whether the quality target was met.

**Triggers**
- "check my notes and chapter X"
- "review my revision of X.Y"
- "/review-revision X.Y"
- "how did chapter X turn out after my edits"
- Equivalent phrasing in the project's output language

**Inputs**
- Path to the revised chapter
- (Implicit) The matching `_analysis.md` with `R:` annotations

**Output**
- Structured chat response
- Optionally, an entry in `.project/reports/revision-log.md`

> **Write all output in the project's output language.**

---

## Why this skill exists

The cycle is:

1. `analyze-chapter` produces the report
2. The author decides item by item, annotates `R:`
3. The author rewrites
4. **`review-revision`** closes the loop

Without step 4, the author revises blind. This skill is the **fresh pair of eyes** that says "this landed, this got worse, and you left an agreement error here".

It is also where the system **learns**: author decisions feed `persona.md` and `preserve-list.md`.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. The `_analysis.md` with `R:` annotations
3. The revised chapter
4. `.project/config/persona.md` — author signatures (do not correct what is their style)
5. `.project/reports/preserve-list.md`
6. `.project/templates/framework.md` — to re-assess density

If git is available, use `git diff` to see exactly what changed. Otherwise compare against the quotes in the `_analysis.md`.

### Step 2 — Map the author's decisions

Categorize each `R:`:

- **Accepted and applied** → check whether the application landed
- **Accepted but done differently** → evaluate the alternative (often better than the suggestion)
- **Rejected ("kept it")** → record as a style signature. Candidate for `persona.md`
- **Removed entirely** → check whether the cut left a hole
- **Asked for feedback** ("what do you think?", "like this?") → **answer explicitly, high priority**

### Step 3 — Read the revised chapter in full

Not just the altered passages. A revision can break rhythm in untouched places — a transition that depended on a cut sentence, for instance.

### Step 4 — Evaluate across five axes

**Axis 1 — Introduced errors (top priority).**
Manual revision introduces errors. Look for:
- Subject-verb and noun agreement
- Government/preposition errors
- Wrong-word substitutions (the word exists but means something else)
- Typos
- Double spacing, orphan punctuation
- Sentences left without subject or verb after a cut

List them all, with location.

**Axis 2 — Rewrite quality.**
For each significant change: better, worse, or neutral? If worse, say why and offer an alternative. If better, **say why** — the author needs to know what worked, not only what failed.

**Axis 3 — Inverted problems.**
The most common revision error: over-correcting into the opposite flaw.
- Dialogue was dry ping-pong → became overloaded with narrative commentary
- Paragraph was aphoristic → became expository
- Prose was lean → became verbose

Flag it when it happens.

**Axis 4 — Residual density.**
Re-assess the 14 categories on the new text. Which tics remain? How far did density fall (estimate before → after)?

**Axis 5 — Holes and continuity.**
- Necessary information lost in a cut?
- Abrupt transition?
- Contradiction with another chapter? (cross-check `knowledge/`)

### Step 5 — Answer direct questions

If the author left questions in the annotations, **answer each in its own section**. Do not bury them in the general analysis. Be honest when the answer is "yes, keep it" — often the author is right and the original suggestion was unnecessary.

### Step 6 — Update learnings

When the author rejected something as a personal signature, **ask** whether to add it to `persona.md`. When they marked a phrase as thesis, suggest `preserve-list.md`.

Never do this automatically. The author decides what becomes a rule.

### Step 7 — Structure the response

```markdown
## Overall verdict
{1-2 paragraphs: did the revision work? right direction?}

## Errors to fix
{numbered list, with location and correction}

## What landed well
{specific praise with technical justification}

## Points for discussion
{decisions worth revisiting, with concrete suggestions}

## Answers to your questions
{each question answered explicitly}

## Practical summary
{3-5 concrete next actions}
{density: before → after}
```

---

## Critical rules

1. **Grammatical errors come first.** An agreement error matters more than a tic.

2. **Praise precisely.** "Better now" is useless. Explaining *what* the change solved teaches.

3. **Acknowledge when the author beat the suggestion.** It happens often. Say so explicitly.

4. **Do not re-suggest what was consciously rejected.** If they noted "kept it, I like it", respect that — unless it creates an objective problem, and then explain why.

5. **The author owns the work.** The skill advises. Language: "consider", "I'd suggest", "worth weighing" — not "fix this" (except for objective errors).

6. **Be honest about the result.** If the revision did not improve enough, say so. The goal is quality, not reassurance.

7. **Estimate density honestly.** Do not inflate progress.

---

## Special case: author's first revision

Calibrate the tone:
- More explanation of *why* behind each assessment
- Establish shared vocabulary (what counts as "tic", what counts as "signature")
- Identify decision patterns that will repeat

## Special case: heavily rewritten chapter

If more than 50% changed, item-by-item comparison loses meaning. Treat it as new text: fresh analysis, compare global density, focus on what the rewrite gained and lost.

---

## Revision log entry

```markdown
## {Chapter} — revised on {date}

**Density:** {before} → {after}
**Decisions:** {N} accepted, {M} rejected, {K} done differently
**Confirmed signatures:** {what the author kept as style}
**Errors corrected:** {N}
**Status:** {✓ approved | needs another pass}
```

This builds the history that `consolidate-style` will later draw on.
