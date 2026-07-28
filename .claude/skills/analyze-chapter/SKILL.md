---
name: analyze-chapter
description: Analyzes one manuscript chapter for AI-generation markers across 14 stylistic categories, producing a structured _analysis.md with literal quotes, suggested treatments, and a prioritized verdict. Cross-references the persona, preserve list, and recurrence map before flagging anything. Use when the user asks to analyze a chapter, check a chapter for AI tics, or run analyze-chapter.
---

# Skill: analyze-chapter

**What it does.** Analyzes one chapter for AI markers and produces a structured `_analysis.md` covering 14 categories, with a verdict and revision priorities.

**Triggers**
- "analyze chapter X.Y"
- "/analyze-chapter X.Y"
- "check chapter X.Y for AI tics"
- Equivalent phrasing in the project's output language

**Input.** Path to the chapter.

**Output.** `{chapter}_analysis.md`, next to the chapter or in `.project/reports/technical/` — follow the convention set in the project's root `CLAUDE.md`.

> **Write the analysis in the project's output language** (`config/project.yaml → language`), not in English.

---

## Execution protocol

### Step 1 — Load context

Read, in this order:

1. **`.project/config/project.yaml`** — output language and conventions
2. **`.project/templates/framework.md`** — the 14 categories, signals, treatments
3. **`.project/config/persona.md`** — author signatures that are **not** tics
4. **`.project/reports/preserve-list.md`** — phrases that must never be flagged
5. **`.project/reports/recurrences.md`** — cross-chapter duplications
6. **`.project/templates/chapter-analysis.md`** — output skeleton

### Step 2 — Read the chapter

Read it in full. Do not skim, do not summarize mentally — the analysis depends on literal quotation.

### Step 3 — Sweep by category

For each of the 14 categories:

a) Scan for the signals listed in the framework.

b) For every occurrence:
   - **Quote the exact text.** Never paraphrase.
   - **Check `persona.md`** → if the construction is a declared signature, **do not flag it**.
   - **Check `preserve-list.md`** → if listed, mark **(PRESERVE — thesis)** with a note on its narrative weight.
   - **Check `recurrences.md`** → if it appears elsewhere, mark **(RECURRENCE — also in ch. X, Y)** plus the decision.
   - Otherwise → **suggest a concrete treatment** from the framework.

c) Compute category density (~N).

d) Set a cut target (~M).

### Step 4 — Section 15: other tics

Capture what does not fit categories 1–14: caps lock, misplaced references, invented proverbs, recurring personification, internal dialogue between "parts of me", recycled phrases.

### Step 5 — Verdict

a) **Top 5–8 priorities**, ordered by **impact**:
   - Objective grammatical errors → immediate top
   - Literal cross-chapter recurrences → always top 3
   - High-density central scenes → top 5
   - Tics breaking rhythm at pivotal moments → top 5

b) **Keep intact (thesis)** — every (PRESERVE) phrase found in this chapter.

c) **Estimated revision time** — in hours.

d) **Target feeling** — one sentence on what the chapter should convey once revised.

### Step 6 — Write output

Follow `.project/templates/chapter-analysis.md`.

### Step 7 — Report back

Return: overall density, top 3 priorities, file path, time estimate.

---

## Critical rules

1. **Quotes are always literal.** For long sentences: opening + `[...]` + closing.

2. **Do not inflate.** Empty category → write "No relevant occurrences in this chapter." Never invent findings to fill a section.

3. **Persona overrides framework.** If the author declared a construction as their signature, it is not a tic. Always respect this.

4. **Thesis overrides tic.** A phrase in `preserve-list.md` goes to "Keep intact", never to a cut suggestion.

5. **Recurrence overrides generic suggestion.** If it is in `recurrences.md`, mark it as a recurrence.

6. **Never generate `R:` annotations.** The author writes those under each item afterwards.

7. **Honest density.** A clean chapter deserves the truth: "Low density. Tonal model." Do not hunt for tics that are not there.

8. **Surgical tone.** This is a working document, not literature.

9. **Output language.** Write the entire analysis in the project's output language.

---

## Special case: already-analyzed chapter

If an `_analysis.md` with `R:` annotations exists, **do not overwrite**. Ask the user:
- Full re-analysis (discards annotations)
- Diff analysis (compares versions, focuses on what changed)
- Cancel

## Special case: clean chapter

Low density → short verdict: top 3 small adjustments, longer "keep intact" list, 15–45 min estimate, target feeling "model chapter, micro-adjustments only".

---

## After the analysis

Suggest next steps:
- Other chapters in the same Act not yet analyzed
- If this was the last chapter of an Act → run `scan-recurrences`
- If new thesis-candidate phrases appeared → suggest adding them to `preserve-list.md`
