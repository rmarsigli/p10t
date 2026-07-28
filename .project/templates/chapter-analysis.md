# Template — Technical Analysis Output

Skeleton followed by the `analyze-chapter` skill when producing `{chapter}_analysis.md`.

> **Write the actual analysis in the project's output language.** The headings below are placeholders — translate them.

---

```markdown
# Analysis — Chapter {number}: {title}

**AI density:** {Low | Medium | High | Very high}. {1-2 sentences: what kind of scene it is, which tics concentrate.}
**Priority:** {Low | Medium | High | Critical}. {1 sentence.}

---

## 1. Binary antithesis

1. **"{literal quote}"** — {classification}. {Suggested treatment, or "(PRESERVE — thesis)", or "(RECURRENCE — also in ch. X)"}

2. **"{literal quote}"** — {classification}. {Treatment}

**Total: ~N. Target: M.**

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

## 7. Anglicized vocabulary

- **"{word}"** ({N}x) — {suggested substitution}

**Target: replace N.**

---

## 8. Lexical repetition

- **"{word}"** — Nx. {Thesis or habit? Vary with X, Y.}

---

## 9. Symmetrical dialogue

**{Scene identification}:**
> {literal dialogue quote}

→ {analysis + suggestion}

---

## 10. Negation lists
[same format as 1-6]

---

## 11. Em-dashes

**Count:** ~N narrative dashes (excluding dialogue openers).

{representative examples}

**Target: reduce to ~M.**

---

## 12. Rhythmic summaries
[same format]

---

## 13. Single-line ending

> {chapter's final sentence}

→ {does it work? is it a recurring formula?}

---

## 14. Named emotion
[same format]

---

## 15. Other tics

[chapter-specific patterns outside 1-14]

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

**Author `R:` annotations.** The author adds lines starting with `**R:**` under each item, marking what they accepted, changed, or rejected. **Never generate these** — only the author writes them.

Example of the file after the author has worked through it (author writing in Portuguese):

```markdown
6. **"Depois de (muitos) anos nesse trabalho"** — The "(muitos)"
   parenthetical is a strong LLM tic. Remove it.
   **R:** removi o (muitos)

8. **"aliás, onde estão as crianças?"** — Self-interruption. Tic.
   **R:** por hora mantive, gostei. É um tique forte?
```

**Empty categories.** If there are no occurrences, write "No relevant occurrences in this chapter." rather than skipping the section. This keeps analyses comparable.

**Quotes.** Always literal. For very long sentences: opening + `[...]` + closing.

**(PRESERVE — thesis).** For phrases in `preserve-list.md`. Also list them in the verdict under "Keep intact".

**(RECURRENCE — also in ch. X, Y).** For phrases in `recurrences.md`. High priority in the verdict.

**Verdict.** Order by **impact**, not by category order. Literal cross-chapter recurrences are almost always top 3.
