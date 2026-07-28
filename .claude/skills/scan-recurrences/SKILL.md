---
name: scan-recurrences
description: Sweeps the entire book for phrases, images, and structures repeated across chapters, distinguishing intentional motifs from accidental duplication, and updates the recurrence map in .project/reports/recurrences.md. Use when the user asks to find duplications, run scan-recurrences, or asks what repeats across chapters.
---

# Skill: scan-recurrences

**What it does.** Sweeps the entire book for phrases, images, and structures appearing in multiple chapters. Distinguishes **intentional recurrence** (a motif stitching the work together) from **accidental duplication** (the same aphorism recycled). Updates `.project/reports/recurrences.md`.

**Triggers**
- "run scan-recurrences"
- "/scan-recurrences"
- "find duplications in the book"
- "what repeats across chapters?"
- Equivalent phrasing in the project's output language

**Optional inputs**
- Scope: whole book (default), a single Act, or a chapter list
- Mode: `full` (complete sweep) or `incremental` (only new/modified chapters)

**Output**
- Updated `.project/reports/recurrences.md`
- Chat report of new duplications

> **Write all output in the project's output language.**

---

## Why this skill exists

Chapter-by-chapter analysis is blind to the whole book. It can see that a serial comparison is a tic — but not that the same sentence appears in three different chapters.

**Literal cross-chapter duplication is the most damaging marker for a critical reader**, because it has no stylistic defence. A human author may have tics; they rarely repeat the same striking sentence three times without noticing.

This skill is the only way to catch it.

---

## Execution protocol

### Step 1 — Load context

1. **`.project/config/project.yaml`** — output language
2. **`.project/reports/recurrences.md`** — current state (for incremental mode and to preserve decisions)
3. **`.project/reports/preserve-list.md`** — recurrences of thesis phrases are **intentional**
4. Chapter list within scope

### Step 2 — Read all chapters

Read the manuscript text (not the `_analysis.md` files). The first pass must be a real read; targeted grep can refine afterwards.

### Step 3 — Detect candidates

Four types:

**Type A — Literal duplication.** The same sentence (or 80%+ identical) in two or more chapters.

**Type B — Recurring structural formula.** Not the same sentence, but the same syntactic mould repeated.
> e.g. an identical closing formula used in four different chapters.

**Type C — Recycled image or comparison.** The same metaphor applied in different contexts.

**Type D — Repeated character aphorism.** The same character saying essentially the same thing in different scenes, without the repetition being diegetic.

### Step 4 — Classify

**INTENTIONAL RECURRENCE (preserve)**
- The phrase is in `preserve-list.md`
- It is a declared motif of the book
- The repetition has a function: ritual, mantra, character obsession, deliberate echo

> Canonical example: a mantra a character repeats daily. It repeats because it **is** a ritual — cutting it would destroy the character.

**ACCIDENTAL DUPLICATION (cut down to one)**
- A striking line recycled
- A comparison reused in a different context
- A repeated closing formula
- Character self-description repeated without function

**GREY ZONE (decide with the author)**
- Repetition that *could* be intentional but is not clearly so
- List with an explicit question: "deliberate echo or duplication?"

### Step 5 — Recommend which instance to keep

Criteria, in order:

1. **First occurrence takes precedence** — usually where it lands hardest.
2. **Unless the second is dramatically stronger** — if it returns at a climax carrying more weight, keep the later one.
3. **Diegetic beats narrative** — a character's line beats the narrator's observation.
4. **Chapter closing beats mid-paragraph.**

Always justify in one sentence.

### Step 6 — Update `recurrences.md`

```markdown
### "{phrase}"
Appears in:
- {ch}: {brief context}
- {ch}: {brief context}
**Decision:** keep {ch}. Cut {chs}. {Justification}
**Status:** {pending | ✓ resolved on DD/MM}
```

**Preserve existing decisions.** An item marked `✓ resolved` does not return. Author `R:` annotations are respected.

### Step 7 — Report

- How many new duplications, by type
- Top 3 most damaging
- Grey-zone items awaiting a decision
- Updated file path

---

## Critical rules

1. **Thesis is not duplication.** Cross-check `preserve-list.md` before flagging anything. A mantra appearing dozens of times may be exactly the point.

2. **Motif is not duplication.** A good book has images that return. A word that opens a relationship in chapter 3 and closes the book in chapter 20 is architecture, not laziness.

3. **The reader test:** *if the reader notices the repetition, will they think "how lovely, it came back" or "I've read this already"?* If the latter, it is duplication.

4. **Do not inflate.** Two shared words is not a recurrence. The threshold: a full sentence or a distinctive syntactic structure, in comparable context.

5. **Preserve history.** In incremental mode, never rewrite from scratch.

6. **Count honestly.** If it appears four times, say four — not "several". The count is what gives the argument weight.

---

## Incremental mode

1. Read `recurrences.md` to see what is already mapped
2. Identify chapters modified since the last sweep
3. Compare only new/modified chapters against the full corpus
4. Add only new findings
5. Mark `✓ resolved` any duplication that has disappeared

---

## After the sweep

- Many new duplications → suggest re-running `analyze-chapter` on affected chapters (now with an updated map)
- Grey-zone items → list the questions for the author
- Phrase confirmed as intentional → suggest moving it to `preserve-list.md`
