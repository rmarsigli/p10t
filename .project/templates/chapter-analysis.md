# Template — Technical Analysis Output

Skeleton followed by the `analyze-chapter` skill when producing `{chapter}_analysis.md`.

> **Write the actual analysis in the project's output language.** The headings below are placeholders — translate them.

**Density unit:** occurrences per 1,000 words, one decimal (`3,4/1k`). Counting rules and per-category ceilings live in `framework.md → How density is measured`. Categories 8, 9, and 13 carry their own units.

---

```markdown
# Analysis — Chapter {number}: {title}

**Length:** {N} words
**Chapter density:** {N,N}/1k — ceiling {N,N}/1k. {1-2 sentences: what kind of scene it is, which categories carry the load.}
**Priority:** {Low | Medium | High | Critical}. {1 sentence.}
**Over ceiling:** {cat. N ({N,N}/1k), cat. M ({N,N}/1k)} — or "none"

---

## 1. Binary antithesis

1. **"{literal quote}"** — {classification}. {Suggested treatment, or "(PRESERVE — thesis)", or "(RECURRENCE — also in ch. X)"}

2. **"{literal quote}"** — {classification}. {Treatment}

**Occurrences: {N} | Density: {N,N}/1k | Ceiling: {N,N}/1k | Target: cut {M}**

---

## 2. Triads and parallel lists
[same format]

## 3. Philosophical hedging
[same format]

## 4. Ironic meta-commentary
[same format]

## 5. Paragraph-closing aphorisms
[same format]

## 6. Serial comparisons
[same format]

---

## 7. Anglicized vocabulary / LLM literary register

- **"{word or construction}"** ({N}x, {N,N}/1k) — {suggested substitution}

**Occurrences: {N} | Density: {N,N}/1k | Ceiling: {N,N}/1k | Target: replace {M}**

---

## 8. Lexical repetition

_Unit: per-1k of each individual word. The ceiling applies per word, not to the category._

- **"{word}"** — {N}x, {N,N}/1k. {Thesis or habit? Vary with X, Y.}

**Words over ceiling: {N}**

---

## 9. Symmetrical dialogue

_Unit: symmetrical exchanges per chapter._

**{Scene identification}:**
> {literal dialogue quote}

→ {analysis + suggestion}

**Exchanges: {N} | Ceiling: {N} per chapter**

---

## 10. Negation lists
[same format as 1-6]

---

## 11. Em-dashes

**Occurrences: {N} narrative dashes | Density: {N,N}/1k | Ceiling: {N,N}/1k | Target: cut {M}**

{representative examples, by problem type A/B/C/D}

---

## 12. Rhythmic summaries
[same format]

---

## 13. Chapter ending

_Unit: % of the book's chapters closing on a single line. A single chapter has no density here._

> {chapter's final sentence}

→ {single-line or not? does it work? is it a recurring formula?}

**Book so far: {N} of {M} chapters ({N}%) close on a single line | Ceiling: {N}%**

---

## 14. Named emotion
[same format]

---

## 15. Other tics

[chapter-specific patterns outside 1-14, with counts. No ceiling — descriptive.]

---

## VERDICT

**Top 5-8 priorities:**

1. {most urgent problem}
2. {next}
...

**Keep intact (thesis):**
- "{phrase}"
- "{phrase}"

**Estimated revision time:** {N} hours.

**Target feeling:** {1 sentence on what the chapter should convey once revised}
```

---

## Filling notes

**Word count first.** Every density figure depends on it. Record it in the header before analyzing anything, and use the same count throughout.

**PRESERVE and persona signatures are not counted.** They appear in the item list, marked, but never enter the density figure — counting them would make the metric argue against the author's own decisions. RECURRENCE instances *are* counted.

**One occurrence, one category.** A triad that also closes a paragraph aphoristically counts once, in its dominant category. State which call you made when it is close.

**Author `R:` annotations.** The author adds lines starting with `**R:**` under each item, marking what they accepted, changed, or rejected. **Never generate these** — only the author writes them.

Example of the file after the author has worked through it (author writing in Portuguese):

```markdown
6. **"Depois de (muitos) anos nesse trabalho"** — The "(muitos)"
   parenthetical is a strong LLM tic. Remove it.
   **R:** removi o (muitos)

8. **"aliás, onde estão as crianças?"** — Self-interruption. Tic.
   **R:** por hora mantive, gostei. É um tique forte?
```

**Empty categories.** If there are no occurrences, write "No relevant occurrences in this chapter." and record `0,0/1k` rather than skipping the section. This keeps analyses comparable.

**Quotes.** Always literal. For very long sentences: opening + `[...]` + closing.

**(PRESERVE — thesis).** For phrases in `preserve-list.md`. Also list them in the verdict under "Keep intact".

**(RECURRENCE — also in ch. X, Y).** For phrases in `recurrences.md`. High priority in the verdict.

**Verdict.** Order by **impact**, not by category order. Literal cross-chapter recurrences are almost always top 3; after those, the categories furthest above their ceiling.
