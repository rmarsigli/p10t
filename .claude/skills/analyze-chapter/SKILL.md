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

**Output.** `{chapter}_analysis.md`, at the location set in `.project/config/project.yaml → paths.analyses` — next to the chapter, or centralized in `.project/reports/technical/`. That field is the single source of truth for this choice.

> "Next to the chapter" resolves through `paths.layout`: the manuscript root under `flat`, the chapter's own directory under `chapter`. The two fields are **independent axes** and every combination is legal — see `.project/templates/layout.md`.

> **Write the analysis in the project's output language** (`config/project.yaml → language`), not in English.

---

## Execution protocol

### Step 1 — Load context

Read, in this order:

1. **`.project/config/project.yaml`** — output language, `paths.analyses`, total density ceiling
2. **`.project/templates/framework.md`** — the 14 categories, signals, counting rules, default ceilings
3. **`.project/config/style-guide.md`** — project overrides to the ceilings, and any language adaptation
4. **`.project/config/persona.md`** — author signatures that are **not** tics
5. **`.project/reports/preserve-list.md`** — phrases that must never be flagged
6. **`.project/reports/recurrences.md`** — cross-chapter duplications
7. **`.project/templates/chapter-analysis.md`** — output skeleton

### Step 2 — Read the chapter and count its words

Read it in full. Do not skim, do not summarize mentally — the analysis depends on literal quotation.

**Count the chapter's prose words before analyzing anything** and record the figure in the header. Every density number derives from it, so it must be one number used consistently. Exclude title, epigraphs, and any analysis scaffolding; include dialogue.

### Step 3 — Sweep by category

For each of the 14 categories:

a) Scan for the signals listed in the framework, in the project's language.

b) For every occurrence:
   - **Quote the exact text.** Never paraphrase.
   - **Check `persona.md`** → if the construction is a declared signature, **do not flag it and do not count it**.
   - **Check `preserve-list.md`** → if listed, mark **(PRESERVE — thesis)** with a note on its narrative weight, and **do not count it**.
   - **Check `recurrences.md`** → if it appears elsewhere, mark **(RECURRENCE — also in ch. X, Y)** plus the decision. Counted, and prioritized in the verdict.
   - Otherwise → **suggest a concrete treatment** from the framework.

c) **Compute the density:** `(occurrences / word count) × 1000`, one decimal. Categories 8, 9, and 13 use their own units — per-word per-1k, exchanges per chapter, and % of the book's chapters respectively.

d) **Compare against the ceiling** — the `style-guide.md` override if one exists, otherwise the framework default. The cut target is the number of occurrences that must go to land under it.

e) After all categories: **sum the per-1k ones** into the chapter total and compare against `project.yaml → density_ceiling_total`.

### Step 4 — Section 15: other tics

Capture what does not fit categories 1–14: caps lock, misplaced references, invented proverbs, recurring personification, internal dialogue between "parts of me", recycled phrases.

### Step 5 — Verdict

a) **Top 5–8 priorities**, ordered by **impact**:
   - Objective grammatical errors → immediate top
   - Literal cross-chapter recurrences → always top 3
   - Categories furthest above their ceiling, weighted by scene importance → top 5
   - Tics breaking rhythm at pivotal moments → top 5

b) **Keep intact (thesis)** — every (PRESERVE) phrase found in this chapter.

c) **Estimated revision time** — in hours.

d) **Target feeling** — one sentence on what the chapter should convey once revised.

### Step 6 — Write output

Follow `.project/templates/chapter-analysis.md`.

### Step 7 — Report back

Return: chapter word count, chapter density (`N,N`/1k) against the total ceiling, which categories are over, top 3 priorities, file path, time estimate.

---

## Critical rules

1. **Quotes are always literal.** For long sentences: opening + `[...]` + closing.

2. **Do not inflate.** Empty category → write "No relevant occurrences in this chapter." Never invent findings to fill a section.

3. **Persona overrides framework.** If the author declared a construction as their signature, it is not a tic. Always respect this.

4. **Thesis overrides tic.** A phrase in `preserve-list.md` goes to "Keep intact", never to a cut suggestion.

5. **Recurrence overrides generic suggestion.** If it is in `recurrences.md`, mark it as a recurrence.

6. **Never generate `R:` annotations.** The author writes those under each item afterwards.

7. **Honest density.** A clean chapter deserves the truth: "3,1/1k, under every ceiling. Tonal model." Do not hunt for tics that are not there.

8. **Count, never estimate.** Density figures come from an actual count against an actual word count. A guessed number breaks every downstream comparison — `review-revision`'s before/after, `review-book`'s trajectory, `consolidate-style`'s ceiling proposals. If a category is genuinely hard to count (7 and 8 often are), say what you counted and how.

9. **Surgical tone.** This is a working document, not literature.

10. **Output language.** Write the entire analysis in the project's output language.

---

## Special case: already-analyzed chapter

If an `_analysis.md` with `R:` annotations exists, **do not overwrite**. Ask the user:
- Full re-analysis (discards annotations)
- Diff analysis (compares versions, focuses on what changed)
- Cancel

## Special case: clean chapter

Chapter total under the ceiling, no category over → short verdict: top 3 small adjustments, longer "keep intact" list, 15–45 min estimate, target feeling "model chapter, micro-adjustments only". Also flag it as a `persona.md` §8 model-passage candidate.

---

## After the analysis

Suggest next steps:
- Other chapters in the same Act not yet analyzed
- If this was the last chapter of an Act → run `scan-recurrences`
- If new thesis-candidate phrases appeared → suggest adding them to `preserve-list.md`
