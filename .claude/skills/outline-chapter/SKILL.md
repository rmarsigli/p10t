---
name: outline-chapter
description: Builds a chapter's structure before any prose exists — obligations (debt to pay, seeds to plant, protections that must NOT happen) and scene contracts with purpose, conflict, and turn. The validated outline is the contract draft-scene executes against. Use when the user asks to outline a chapter or structure the next chapter.
---

# Skill: outline-chapter

**What it does.** Builds the structure of a chapter before any prose exists: beats, scenes, obligations, and constraints. The outline is the **contract** that `draft-scene` executes against.

**Triggers**
- "outline chapter X.Y"
- "/outline-chapter X.Y"
- "let's structure the next chapter"
- Equivalent phrasing in the project's output language

**Input.** Chapter position; whatever the author already knows about it (can be one sentence or nothing).

**Output.** `{chapter}_outline.md` next to where the chapter will live, following `.project/templates/chapter-outline.md`.

> **Write the outline in the project's output language.**

---

## Core principle

> **An outline is a set of obligations, not a summary written in advance.**

The difference: a summary describes what happens; an obligation list states what the chapter must accomplish, plant, and protect. Prose drafted from obligations has direction. Prose drafted from a summary has only sequence.

Every chapter carries three kinds of obligation:

1. **Debt** — what previous chapters promised that this one must pay (or explicitly defer)
2. **Planting** — what future chapters need seeded here, invisibly
3. **Protection** — what must NOT happen: mysteries that stay closed, information characters cannot yet have, reveals that belong to later chapters

The third is the one outlines usually forget, and the one that prevents the worst generation failures.

---

## Protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language, structure
2. The **previous chapter** (and the next, if it exists) — continuity in both directions
3. `.project/knowledge/timeline.md` — where we are in story time
4. `.project/knowledge/worldbuilding.md` — active rules and the **deliberately unexplained** list
5. `.project/knowledge/characters/` — sheets of everyone likely on stage (arc positions especially)
6. `.project/config/style-guide.md` — structural rules (POV, tense, chapter length norms)

### Step 2 — Collect the author's intent

Ask what they know, however vague: "the chapter where the merchant admits it" is enough to start. If the author has nothing, propose 2–3 candidate directions based on open debt, and let them choose.

**The author's intent wins over structural neatness, always.**

### Step 3 — Compute the obligations

**Debt.** Sweep recent chapters for open promises: questions raised, characters in motion, tensions unresolved. List which ones this chapter pays, and which it deliberately lets ride.

**Planting.** Ask what later chapters (if known) will need to have been established. A reveal only lands if planted at least once before.

**Protection.** From `worldbuilding.md`'s deliberately-unexplained list and the characters' knowledge states: what must this chapter *not* reveal, resolve, or let a character know too early? Write these as explicit constraints — they are `draft-scene`'s guardrails.

### Step 4 — Break into scenes

For each scene, five fields:

- **Purpose** — the one obligation this scene serves. A scene serving no obligation gets cut or merged.
- **Conflict** — what resists. A scene where nothing resists is a transition; make it short or absorb it.
- **Turn** — what is different when the scene ends. If nothing changed, the scene has no exit.
- **On stage** — who is present; which character sheets `draft-scene` must load.
- **Length signal** — rough weight (brief / standard / extended) so pacing is decided here, not improvised during drafting.

### Step 5 — Check the shape

- Does the chapter's ending create the pull toward the next one?
- Does pacing vary, or is every scene the same weight?
- Cross-check `analyze-chapter` history: if the book's endings over-use one closing pattern (single-line, aphorism), flag what this chapter's ending should *not* be.

### Step 6 — Present and iterate

Present the outline as a proposal. The author cuts, reorders, overrides. Only the validated version becomes the contract.

---

## What to avoid

**Over-specification.** The outline fixes purpose and constraints — not sentences. If it starts containing prose, it is stealing decisions that belong to drafting (where the author's voice, via persona, does the work).

**Beat inflation.** Not every chapter needs five scenes. A single-scene chapter with one strong turn is a legitimate shape.

**Ignoring the protection list.** The most expensive failure: an outline that lets a scene casually resolve a mystery the book needs closed. Protection constraints are non-negotiable inputs to `draft-scene`.

**Outlining past the author.** If the author says "I don't know yet what happens after the door opens" — stop there. An honest partial outline beats a complete invented one.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `draft-scene` | Executes this contract, scene by scene |
| `check-arc` | Reads outlines to see intended trajectory vs. delivered |
| `check-consistency` | Protection constraints come from its same sources |
| `restructure-chapter` | Same obligations model, applied backwards to a chapter that already exists |
