---
name: restructure-chapter
description: Rebuilds the obligations of a chapter that already exists, from what is actually on the page, then proposes reordering, merging, cutting, or adding scenes to fix a diagnosed structural problem. Delivers a plan against the current structure — never rewrites the manuscript. Use when the user asks to restructure a chapter, when a chapter's problem is scene-level rather than sentence-level, or when check-arc, review-book, or revise-passage identified a structural fault.
---

# Skill: restructure-chapter

**What it does.** Takes a chapter that already exists and has a **structural** problem — not a prose problem — reconstructs its obligations from what is on the page, and proposes a new scene architecture. The counterpart of `outline-chapter` for text that already exists.

**Triggers**
- "restructure chapter X.Y"
- "/restructure-chapter X.Y"
- "this chapter's problem isn't the sentences"
- "chapter X drags in the middle" / "nothing happens in X"
- Routed here by `revise-passage` when a passage's problem is upstream, or by `check-arc` / `review-book` when a finding is scene-level
- Equivalent phrasing in the project's output language

**Input.** The chapter, plus the diagnosis if one exists (a `check-arc` finding, a `review-book` note, or the author's own complaint). If none is given, the skill diagnoses first.

**Output.** `{chapter}_restructure.md` next to the chapter — a plan, presented against the current structure. **Never applied to the manuscript.** Once validated, the author executes it, or hands individual scenes to `draft-scene` and `expand-beat`.

> **Write the plan in the project's output language.**

---

## Core principle

> **Restructuring is diagnosis plus a plan, not a rewrite. The scenes that work are not touched.**

This skill exists to close a gap: `check-arc` and `review-book` find structural faults but cannot act on them; `revise-passage` explicitly refuses them ("if more than ~60% needs replacing, the problem is upstream"); `outline-chapter` only builds chapters that do not yet exist. Without this skill, a diagnosed structural problem ends at "have a conversation".

Two rules follow from that:

**The existing chapter is evidence, not a draft to be replaced.** Whatever is already working — a scene that lands, a turn that earns itself, a line the author loves — survives the restructure by default. The plan says explicitly what it is preserving.

**Structural problems are the author's territory more than any other.** Scene order, what a chapter is *for*, what gets cut — these are dramatic decisions. The skill proposes options with trade-offs; it does not pick.

---

## What counts as a structural problem

Route here, not to `revise-passage`:

| Symptom | Why it is structural |
|---|---|
| Scenes that serve no obligation | Cutting sentences will not give them a purpose |
| The turn arrives in the wrong scene | Prose cannot fix sequence |
| Two scenes doing the same work | One has to go, or they merge |
| The chapter has no exit — nothing is different at the end | Sentence-level polish cannot manufacture a turn |
| A reveal lands before it is earned | The fix is upstream, often in an earlier chapter |
| Uniform pacing — every scene the same weight | A shape problem, not a rhythm problem |
| Flat stretch flagged by `check-arc` | Presence without movement is a scene-design fault |

**Route away** if the diagnosis is density, voice, dialogue texture, or a passage that reads badly but sits in the right place. Those are `analyze-chapter` and `revise-passage`. Say so and hand off — a structural intervention on a prose problem destroys working material.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language, structure
2. **The chapter, in full** — plus the previous and following chapters, for the debt it inherits and the debt it owes
3. The existing `{chapter}_outline.md`, **if one exists** — but read it *after* the chapter, never before
4. `{chapter}_analysis.md` — a chapter that is dense *and* structurally broken gets restructured first; the analysis is re-run afterwards on new text
5. `.project/knowledge/characters/` — arc positions of everyone on stage
6. `.project/knowledge/worldbuilding.md` — the deliberately-unexplained list and knowledge states
7. `.project/knowledge/timeline.md` — what story time this chapter occupies
8. `.project/reports/literary/` — prior `check-arc` and `review-book` findings touching this chapter

### Step 2 — Map what is actually there

Before judging anything, build the honest inventory. For each existing scene:

- **What it does** — the obligation it actually serves, which may not be the one intended
- **Conflict** — what resists, or "nothing"
- **Turn** — what is different at the end, or "nothing"
- **Length** — words, and share of the chapter
- **On stage** — who, and whose state moves

A scene with no conflict and no turn is not automatically cut — it may be a transition doing real work, or a deliberate rest. Record it as-is and judge in Step 4.

### Step 3 — Recompute the obligations from the page

The same three obligations `outline-chapter` uses, derived backwards from the manuscript rather than forwards from intent:

- **Debt** — what earlier chapters left open that this one is positioned to pay. Which does it actually pay? Which does it drop silently?
- **Planting** — what later chapters need seeded here. If later chapters exist, read them: an unplanted reveal downstream is a fault in *this* chapter.
- **Protection** — what must not be revealed or resolved here. Restructuring is the operation most likely to leak a mystery, because moving a scene moves what the reader knows when.

**Where intent and page diverge, present both.** Sometimes the chapter found something better than the outline planned. That is a reason to update the outline, not to restructure the chapter.

### Step 4 — Diagnose

State the structural fault in one or two sentences, citing scenes. If the author supplied a diagnosis, verify it against the map before accepting it — the complaint is usually accurate about *where* something feels wrong and often wrong about *why*.

**If the chapter is structurally sound, say so.** "The structure holds; the problem is density in scene 2" is a legitimate and valuable outcome. Do not manufacture a restructure to justify the invocation.

### Step 5 — Propose

Present the plan as **the current structure against the proposed one**, scene by scene, with a verdict on each:

| Verdict | Meaning |
|---|---|
| **Keep** | Untouched. Say what it is doing right |
| **Move** | Same scene, different position. Say what the new position buys |
| **Merge** | Absorbed into another scene. Say what survives from each |
| **Compress** | Kept, reduced. Say what goes |
| **Cut** | Removed. Say where its load-bearing content relocates |
| **New** | A scene the chapter needs and does not have. Full contract: purpose, conflict, turn, on stage, length |

Two disciplines:

**Every cut names its debt.** If a cut scene carried information, a planting, or a beat of an arc, the plan says which surviving scene now carries it. An orphaned obligation is how restructuring breaks books.

**Offer alternatives where the trade-off is real.** Reordering versus cutting is usually a genuine fork, with different costs. Present both with their consequences and let the author rule; do not collapse the decision.

### Step 6 — Check the blast radius

Restructuring is the only operation in the system that routinely breaks *other* chapters. Before delivering, check:

- **Knowledge states** — does moving a scene mean a character now knows something earlier, or later, than the rest of the book assumes?
- **Timeline** — do the story-time markers still reconcile?
- **Protection** — does the new order leak anything from the deliberately-unexplained list?
- **Downstream references** — does a later chapter refer back to something this plan cuts or moves?
- **Recurrences** — does merging two scenes put two versions of the same image side by side?

List every downstream chapter the plan touches. If the blast radius is large, say so plainly — the author may prefer a smaller fix.

### Step 7 — Deliver

```markdown
# Restructure — Chapter {number}

**Diagnosis:** {the structural fault, citing scenes}
**Preserving:** {what works and is not being touched}

## Current structure
{the Step 2 map}

## Proposed structure
{scene by scene, with verdicts and reasoning}

## Alternatives
{where the trade-off is genuine, both paths with their costs}

## Relocated obligations
{every cut scene's load-bearing content, and where it now lives}

## Blast radius
{downstream chapters affected, and how}

## Open questions
{plot decisions this plan needs from the author and cannot make}
```

Close with the execution route: which scenes the author rewrites themselves, which go to `draft-scene` (new scenes with a full contract), which go to `expand-beat` (a beat that needs texture), and a note to re-run `analyze-chapter` on the result.

---

## What to avoid

**Restructuring a prose problem.** The most destructive misfire. A chapter that reads badly but sits right does not need its scenes moved — it needs `revise-passage`. Verify the diagnosis before proposing architecture.

**Rewriting under cover of restructuring.** The output is a plan. The moment it starts containing drafted prose, it has stopped being a plan and started stealing decisions that belong to drafting.

**Orphaning obligations.** A cut scene's plantings, reveals, and arc beats have to land somewhere. Cutting without relocating is how a restructured chapter breaks chapter 14.

**Tidying.** Not every chapter needs three scenes with escalating stakes. A chapter that works oddly, works. Judge against the book's own shape, not against structural convention.

**Ignoring the author's attachment.** If the author loves a scene the plan wants to cut, that is data about what the book is, not resistance to be overcome. Propose the alternative that keeps it and let them see both costs.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `check-arc` | Primary upstream source — flat stretches and rushed turns route here |
| `review-book` | Its structural findings route here, chapter by chapter |
| `revise-passage` | Hands off here when a passage's problem is upstream of the sentences |
| `outline-chapter` | Same obligations model, forwards instead of backwards; produces contracts for the plan's new scenes |
| `draft-scene` | Executes the new scenes this plan specifies |
| `check-consistency` | Run after execution — restructuring is the operation most likely to break knowledge states |
| `analyze-chapter` | Re-run on the restructured chapter; the density figures of the old version no longer apply |
