---
name: draft-scene
description: Generates scene prose from a validated outline contract, loading the full project context — persona, references, style guide, world rules, character voices, preserve list, recurrence blocklist — and self-auditing against the 14 tic categories before delivery. The draft is a proposal marked for curation, never written into the manuscript. Use when the user asks to draft a scene or write a scene covered by an outline.
---

# Skill: draft-scene

**What it does.** Generates scene prose from a validated outline contract, carrying the full weight of the project's knowledge: persona, references, style guide, world rules, character voices, preserve list, recurrence map, and the 14-category framework as negative constraints. **Context-expensive by design** — the point is prose born inside the voice, not prose cleaned afterwards.

**Triggers**
- "draft scene 2 of chapter X.Y"
- "/draft-scene X.Y scene-2"
- "write the scene where {...}" *(only if an outline covers it)*
- Equivalent phrasing in the project's output language

**Input.** A scene from a validated `{chapter}_outline.md`, or an ad-hoc brief containing at minimum: purpose, conflict, turn, who is on stage, protection constraints.

**Output.** `{chapter}_draft.md` (or appended scene block), explicitly marked as a draft for curation. **Never written into the manuscript file itself.**

> **Write the prose in the project's output language.**

---

## Core principle

> **The draft is a proposal. The measure of success is how much survives the author's curation.**

This skill does not produce finished prose. It produces the best possible starting material — prose that already respects the voice, the world, and the constraints, so the author's revision energy goes into *making it theirs* instead of *removing the machine*.

Expected trajectory: early drafts survive curation at maybe 40–60%. As `persona.md`, `preserve-list.md`, and `revision-log.md` accumulate, survival should rise. If it does not, the persona is not yet sharp enough — say so and propose a `define-persona` update session.

---

## Hard rules (before anything else)

1. **No contract, no draft.** If there is no validated outline covering the scene and the author has not provided a brief with purpose/conflict/turn/protection, stop and build one first. Drafting without a contract produces plot, and plot decisions belong to the author.

2. **Protection constraints are absolute.** The outline's "must NOT happen" list and worldbuilding's deliberately-unexplained list are inviolable. If drafting seems to require touching one, stop and surface the conflict.

3. **Open questions are hard stops.** Where the outline says "the author hasn't decided", the draft ends or routes around. Never invent the undecided.

4. **Never touch the manuscript file.** Output goes to a `_draft` file. The author moves text into the manuscript; the skill does not.

---

## Execution protocol

### Step 1 — Full context load

Read, in this order (yes, all of it — this is the expensive part and the entire point):

1. `.project/config/project.yaml` — output language
2. **The scene contract** — the outline entry or ad-hoc brief
3. **The previous scene/chapter** — continuity of action, tone, and story time
4. `.project/config/persona.md` — the voice. **Re-read the model passages (section 8) immediately before drafting; they are the tonal calibration.** Note the anti-models (section 9) as what to avoid. Note the per-1k ceilings in "signatures to watch" (section 4)
5. `.project/config/references.md` — borrowing instructions and their exclusion lines
6. `.project/config/style-guide.md` — hard formatting and vocabulary rules, plus the project's ceiling overrides
7. `.project/knowledge/worldbuilding.md` — active rules, costs, knowledge distribution, **deliberately-unexplained list**
8. **Character sheets** for everyone on stage — Voice sections above all; sample lines are calibration
9. `.project/reports/preserve-list.md` — thesis phrases (may echo intentionally *only* if the contract calls for it)
10. `.project/reports/recurrences.md` — phrases already used; **never generate them again**
11. `.project/templates/framework.md` — the 14 categories as negative constraints

### Step 2 — Compile the constraint sheet

Before writing a word, produce (internally) the scene's constraint sheet:

- **Voice targets:** register, rhythm, the 2–3 persona devices active in this kind of scene
- **Density budget:** convert the ceilings into an **absolute allowance for this scene's target length**. Ceilings are per-1k (persona §4 and `style-guide.md` overrides, otherwise the framework defaults); a 900-word scene against a 2,0/1k ceiling gets 1,8 → **1 occurrence**. Round down: a scene is not entitled to its full share of every category at once. Write the allowance out per category before drafting, or the self-audit in Step 4 has nothing to check against
- **Character voice keys:** one line per character on stage — their register, their never-says
- **World guards:** which rules are active in this scene; who on stage knows what
- **Protection list:** what this scene must not reveal or resolve
- **Recurrence blocklist:** striking phrases from the map that must not reappear
- **Length target:** from the contract's length signal

### Step 3 — Draft

Write the scene against the constraint sheet.

Guidance that matters most in practice:

- **Purpose discipline.** Every beat serves the scene's stated purpose. Beautiful digressions that serve nothing get cut before the author ever sees them.
- **Emotion through the body.** Category 14 is the most common generation failure. Gesture, breath, timing — not labels.
- **Dialogue asymmetry.** Category 9's inverted problem too: vary reply lengths, one gesture between lines, not two.
- **Endings are not punchlines by default.** Check what the recent chapters' scenes did; vary.
- **When in doubt, under-write.** The author can expand a lean draft; deflating an overwritten one costs more.

### Step 4 — Self-audit (before the author sees anything)

Run the draft through the 14 categories as if it were a hostile `analyze-chapter` pass:

- Count the drafted words, then count each category against the Step 2 allowance
- Anything over budget → revise now, and re-count after revising
- Check every striking phrase against the recurrence blocklist
- Check protection constraints one final time
- Check each character's lines against their never-says

**The author should never receive a draft that would fail the project's own analysis.** If a tic survives self-audit because it genuinely serves the scene, keep it — but flag it in the delivery notes.

### Step 5 — Deliver with honest notes

Present the draft with a short delivery note:

```markdown
## Draft notes — {scene}

**Self-audit:** {N,N}/1k over {N} words — {clean | N flags kept deliberately, listed below}
**Choices you should review:**
- {a voice call, a pacing call, an interpretation of the contract — anything the skill decided that the author might decide differently}
**Where I stopped:** {open questions respected, boundaries hit}
**Length:** {target vs. delivered}
```

The "choices you should review" list is mandatory. A draft with zero flagged choices means the skill is hiding its uncertainty, not that it had none.

### Step 6 — Iterate on feedback

When the author reacts ("she wouldn't say that", "too fast here", "this whole beat is wrong"):

- Revise **only** what the feedback touches. Do not silently rewrite untouched passages.
- Every voice correction is data: propose recording it — character sheet Writing notes for "she wouldn't say that", persona for style corrections.
- If the author rewrites a passage themselves, **their version wins** and becomes reference material for the next scene's calibration.

---

## What to avoid

**Drafting to impress.** The failure mode of every generation pass: reaching for the striking phrase. The persona's model passages define what "good" means here — not general literary ambition. Restraint survives curation; flourish gets cut.

**Resolving what the contract left open.** The most expensive failure. When the draft needs an answer the author hasn't given, the draft stops.

**Recycling the book's own hits.** A phrase that worked in chapter 3 is not available in chapter 9. That is what the recurrence blocklist is for.

**Uniform pacing.** Scene contracts carry length signals. A "brief" scene drafted at full weight breaks the chapter's shape.

**Silent confidence.** Every interpretive choice goes in the delivery notes. The author curates; the skill discloses.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `outline-chapter` | Provides the contract this skill executes |
| `define-persona` | Provides the voice; receives corrections back |
| `create-character` | Provides voice keys; receives "wouldn't say that" data back |
| `build-worldbuilding` | Provides guards and the protected mysteries |
| `analyze-chapter` | Its criteria run here as self-audit before delivery |
| `scan-recurrences` | Its map is the blocklist |
| `revise-passage` | Sibling: same context load, applied to existing text instead of a blank page |
