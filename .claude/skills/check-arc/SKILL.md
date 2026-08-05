---
name: check-arc
description: Maps character trajectories, thematic development, and the tension curve from beats on the page, then compares against intent — finding flat stretches, rushed turns, abandoned threads, and unearned endings. Use when the user asks to check the arcs, map tension, or asks whether a character's arc is landing.
---

# Skill: check-arc

**What it does.** Maps the book's arcs — character trajectories, thematic development, and tension curve — against what the pages actually deliver. Finds flat stretches, rushed turns, and abandoned threads.

**Triggers**
- "check the arcs"
- "/check-arc {scope | character}"
- "is {character}'s arc landing?"
- "map the tension across Act {N}"
- Equivalent phrasing in the project's output language

**Input.** Scope: whole book (default), one Act, or one character/theme.

**Output.** Arc report in chat or `.project/reports/literary/YYYY-MM-DD-arcs-{scope}.md` if extensive.

> **Write the report in the project's output language.**

---

## Core principle

> **An arc is judged by beats on the page, not by intentions in the sheet.**

The character sheet says "starts closed, learns to trust". The question this skill answers: **in which chapters, through which events, does that movement actually happen — and does the spacing work?**

The method is evidence-first: build the beat map from the text, *then* compare against intent. Mapping intent first contaminates the reading.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language, `paths.layout`
2. The manuscript in scope — full read, **in order**. Resolve the chapter list and its ordering via `.project/templates/layout.md`; an Act scope resolves from the chapter id prefix, not from directory structure
3. `.project/knowledge/characters/*.md` — Arc and engine sections (intent)
4. Chapter outlines, if they exist — intended trajectory per chapter
5. `.project/reports/literary/` — previous arc reports, for trajectory over drafts

### Step 2 — Build the beat maps

**Per character in scope:** every scene where their state *moves* — a decision, a reveal to them, a relationship shift, a loss. Chapter, one-line description, direction of movement. Scenes where they appear but nothing moves are recorded as presence-without-movement (that pattern matters).

**Thematic:** where the book's thesis surfaces — stated, dramatized, tested, or contradicted. A thesis that is only *stated* repeatedly but never *tested* is a flag.

**Tension:** per chapter, what question keeps the reader reading, and does the chapter sharpen it, sustain it, or release it?

### Step 3 — Diagnose against the maps

**Flat stretches.** Three+ consecutive chapters of presence-without-movement for a main character. (For the protagonist, even two is worth flagging.)

**Rushed turns.** A state change without enough on-page pressure behind it — the trust that arrives one scene after the betrayal.

**Abandoned threads.** Movement that starts and silently stops. The secondary character whose arc evaporates mid-book.

**Unearned endings.** The final state the ending needs vs. the beats that actually built it. If the climax requires a capacity the character was never shown developing, the arc has a hole exactly there.

**Sheet-page divergence.** Where delivery differs from the sheet's intent — sometimes the page found something better (update the sheet), sometimes it drifted (fix the page). Present both readings; the author rules.

**Tension shape.** Chart the curve. Long plateaus, repeated identical peaks, or a mid-book slack line — named with chapters.

### Step 4 — Report

Per finding: the evidence (beat map excerpt), the diagnosis, and **where the fix would go** — which chapters have room to carry the missing beat. A rushed turn is usually fixed two chapters earlier, not at the turn itself.

This skill diagnoses; it does not restructure. Close by naming which findings are chapter-scoped enough to hand to `restructure-chapter`, and which are book-scoped and belong in a `review-book` pass instead.

---

## What to avoid

**Formula enforcement.** Not every character needs a transformation arc; a fixed character against a changing world is a legitimate design. Judge against the book's own intent, not a template.

**Intent-first reading.** Map the page, then compare. Never the reverse.

**Conflating flat with quiet.** A quiet chapter can carry enormous movement; an action chapter can be flat. Movement is state change, not event volume.

**Fixes at the symptom.** The report points to where the missing pressure belongs, which is usually upstream of where the problem shows.

---

## Cadence

End of each Act, and always before a full revision pass — arc fixes reorder revision priorities.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `create-character` | Sheets provide intent; divergences flow back as sheet updates |
| `outline-chapter` | Outlines carry intended beats; gaps found here become obligations there |
| `restructure-chapter` | Where findings become action — flat stretches and rushed turns route there, chapter by chapter |
| `review-book` | Consumes these findings for its structural sections |
