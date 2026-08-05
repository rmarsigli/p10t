---
name: update-preserve-list
description: Harvests the author's protection decisions from R-annotated analyses into .project/reports/preserve-list.md, and retires entries whose phrases were cut — proposed in batch, never promoted silently. Use when the user asks to update the preserve list or migrate their thesis decisions, or after review-revision sessions accumulate protection decisions.
---

# Skill: update-preserve-list

**What it does.** Sweeps analysis files and revision history for phrases the author has decided to protect, and migrates them into `.project/reports/preserve-list.md`. Also retires entries whose phrases no longer exist in the manuscript. The bookkeeping skill that keeps the preserve list true.

**Triggers**
- "update the preserve list"
- "/update-preserve-list"
- "migrate my thesis decisions"
- Run automatically as a suggested step after `review-revision` sessions
- Equivalent phrasing in the project's output language

**Input.** Scope: all annotated analyses (default) or a specific chapter's.

**Output.** Updated `.project/reports/preserve-list.md` — **after author confirmation, never silently.**

> **Write entries in the project's output language.**

---

## Core principle

> **Propose, never promote. The author decides what is thesis.**

An `R:` annotation saying "kept it" is a fact. Whether it means *"this phrase is my thesis, protect it forever"* or just *"fine here, this once"* is an interpretation — and the difference matters, because everything on the preserve list becomes untouchable to every other skill.

So this skill collects candidates and presents them in batch. One confirmation session, then the migration.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. `.project/reports/preserve-list.md` — current state
3. All `_analysis.md` files with `R:` annotations in scope — searched **recursively**, since `chapter` layout nests them one level down
4. `.project/reports/revision-log.md` — confirmed-signature entries
5. The manuscript — to verify that listed phrases still exist. Resolve the chapter list via `.project/templates/layout.md`; a chapter missed here retires an entry whose phrase is still on the page

### Step 2 — Collect candidates

Sweep annotations for protection signals, strongest to weakest:

- **Explicit:** "this is my thesis", "preserve this", "never flag this again"
- **Strong:** "kept it" on an item the analysis had marked as recurring or structural — protecting something under fire implies attachment
- **Pattern:** the same phrase or motif kept in two or more chapters
- **Weak (usually skip):** a single "kept it" with no reasoning — probably situational, not thesis

Distinguish **phrase protection** (this exact wording is untouchable → preserve list) from **construction protection** (this *kind* of move is my style → belongs in `persona.md`, not here). Route each candidate to the right destination.

### Step 3 — Verify the existing list

For every current entry, check the phrase still exists in the manuscript:

- **Gone** (cut in revision) → propose retiring the entry, with a dated note
- **Changed** (reworded but recognizably alive) → propose updating the quote to the current wording
- **Moved** (different chapter after restructuring) → update the reference

### Step 4 — Present the batch

One structured confirmation, not twenty questions:

```markdown
## Preserve-list update — {date}

### Candidates to add ({N})
1. **"{phrase}"** ({chapter}) — signal: {explicit | kept-under-fire | pattern across chs. X, Y}
   → suggested section: {thesis | character motto | recurring image | pivotal line}

### Route to persona.md instead ({N})
1. **{construction}** — kept {N} times; this is a style signature, not a phrase

### Retire ({N})
1. **"{phrase}"** — no longer in manuscript (cut in {chapter} revision, {date})

### Update ({N})
1. **"{old}"** → **"{new}"** ({chapter})
```

The author answers once — approve all, or strike items. Then apply.

### Step 5 — Apply and report

Update the file with dated changes. Report the deltas and remind: the next `analyze-chapter` runs will respect the new entries.

---

## What to avoid

**Silent promotion.** The single forbidden move. Everything passes through the author.

**Over-collection.** A bloated preserve list blinds the analysis — if hundreds of phrases are protected, nothing is. When the candidate batch is large, say so and suggest a higher bar.

**Wrong destination.** Phrases here; constructions to `persona.md`. Mixing them corrupts both files.

**Letting the list rot.** A preserve list full of cut phrases misleads every downstream skill. The verification sweep (Step 3) is not optional.

---

## Cadence

After each Act's revisions are done, or whenever `review-revision` sessions have accumulated a handful of protection-flavored decisions.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `review-revision` | Produces the decisions this skill harvests |
| `analyze-chapter` | Consumes the list this skill maintains |
| `consolidate-style` | Sibling harvester — it collects constructions, this collects phrases |
| `define-persona` | Receives the routed construction candidates |
