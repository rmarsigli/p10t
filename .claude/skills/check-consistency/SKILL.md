---
name: check-consistency
description: Checks chapters against the project's established facts — world rules, timeline math, character invariants, and knowledge states (who knows what, when). Flags only real contradictions with citations from both sides; never resolves silently. Use when the user asks to check consistency, run a continuity check, or asks whether a chapter contradicts anything.
---

# Skill: check-consistency

**What it does.** Checks chapters against the project's established facts: world rules, timeline markers, character consistency rules, and knowledge states. Finds contradictions before readers do.

**Triggers**
- "check consistency of chapter X.Y"
- "/check-consistency {scope}"
- "does chapter X contradict anything?"
- "run a continuity check on Act {N}"
- Equivalent phrasing in the project's output language

**Input.** Scope: one chapter, an Act, or the whole book.

**Output.** Report in chat; confirmed contradictions logged to the contradictions table in `.project/knowledge/worldbuilding.md`.

> **Write the report in the project's output language.**

---

## Core principle

> **Flag only what is actually contradicted, with evidence from both sides. Never resolve silently.**

A consistency check that cries wolf trains the author to ignore it. Every flag must cite **two passages that cannot both be true** — or one passage against one established rule. Ambiguity, stylistic variation, and things merely *unstated* are not contradictions.

And when a real contradiction is found, which side wins is an **author decision**. The skill presents; it never picks.

---

## Execution protocol

### Step 1 — Load the sources of truth

1. `.project/config/project.yaml` — output language
2. `.project/knowledge/worldbuilding.md` — rules (ESTABLISHED ones especially) and their costs
3. `.project/knowledge/timeline.md` — chronology and the time-markers table
4. `.project/knowledge/characters/*.md` — Consistency rules sections and knowledge states
5. `.project/knowledge/glossary.md` — canonical spellings and term usage

### Step 2 — Read the scope against them

Four sweeps:

**a) World-rule sweep.** Does anything in the text violate an established rule, ignore a stated cost, or exceed a demonstrated limit?

**b) Time sweep.** Do stated durations, sequences, and markers reconcile? ("three days later" chains are the classic breakage — sum them and check.)

**c) Character sweep.** Physical facts, behavioural invariants, voice register (flagrant breaks only — fine voice drift belongs to `create-character`'s extract mode).

**d) Knowledge sweep.** The subtlest and most valuable: **does any character use information they cannot yet have?** Check reveals against who was present, who was told, and when.

### Step 3 — Classify each finding

- **CONTRADICTION** — two citations that cannot both hold. Severity: does a plot point depend on it?
- **STRAIN** — not strictly contradictory, but requires a generous reading. Worth surfacing, marked as such.
- **GAP** — the text is silent where a fact is expected. Usually fine; listed only if a future chapter will need the answer.

### Step 4 — Report

Per finding:

```markdown
### {short label} — {CONTRADICTION | STRAIN | GAP}
**Side A:** "{quote}" ({chapter})
**Side B:** "{quote}" ({chapter}) — or: rule/sheet entry
**Stakes:** {what depends on this}
**Options:** {the 2-3 ways it could be resolved — no recommendation unless asked}
```

### Step 5 — Log resolutions

When the author decides, record it in the worldbuilding contradictions table with date and resolution. If the resolution changes a rule or a character fact, update the relevant file (with the author's confirmation).

---

## What to avoid

**Pedantry.** An unnamed weekday is not a gap. A metaphor is not a rule violation. The bar is *would a careful reader trip here?*

**Silent resolution.** Even an "obvious" fix changes the manuscript's commitments. Present, don't decide.

**Re-litigating decisions.** A contradiction the author already resolved (it's in the log) stays resolved.

**Treating ASSUMED rules as binding.** Only ESTABLISHED rules generate contradictions. An assumption in tension with the text is a signal to *update the assumption*, and is reported as such.

---

## Cadence

After each Act, and before any `draft-scene` session that touches long-established material.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `build-worldbuilding` | Owns the rules and the contradictions log |
| `create-character` | Owns consistency rules; receives voice-drift cases |
| `draft-scene` | Its world guards draw on the same sources |
| `review-book` | Aggregates these findings at the structural level |
