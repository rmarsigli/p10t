# Template — Whole-Book Literary Report

Skeleton for the complete report, produced by the `review-book` skill at the end of each Act.

Unlike the technical analysis — which is per-chapter and purely mechanical — this one looks at the **whole book**: plot, character, theme, pacing, and viability.

> **Write the report in the project's output language.**

---

```markdown
# Complete Analysis — {Title}

_Date: {date}_
_Scope: {whole book | Act X}_
_Estimated length: {N}k words_

---

## 0. Executive summary

{3-5 paragraphs. What the book is, what it does well, what needs work, and the commercial verdict in one line.}

---

## 1. Literary review

### 1.1 Overall architecture
{Act structure. Function of each part. Symmetries and echoes.}

### 1.2 Concept and premise
{What holds the book up. Originality. Internal coherence.}

### 1.3 Characters
{One paragraph per relevant character: arc, what works, what is missing.}

### 1.4 Prose and voice
{Narrative modes. Dialogue. Pacing. Formal devices.}

### 1.5 Themes and thesis
{What the book is saying. Does the thesis hold from start to finish?}

### 1.6 Strengths
{Numbered, specific.}

### 1.7 Weaknesses and risks
{Numbered, each with a suggested treatment.}

---

## 2. Commercial potential

### 2.1 Genre positioning
{Where this book lives in a bookstore. Classification risks.}

### 2.2 Comparable titles
{3-5 titles, nearest to furthest, with justification.}

**Elevator pitch:**
> {2-3 sentences}

**One line for a book fair:**
> {1 sentence}

### 2.3 Length and format
{Word count, estimated pages, market fit.}

### 2.4 Target readership
{Primary, secondary, tertiary reader.}

### 2.5 Publishing paths
{Plausible publishers, with justification. Domestic and international.}

### 2.6 Commercial risks
{List, each with mitigation.}

### 2.7 Probability (qualitative)
{Scenarios: unagented, agented, post professional edit, self-published.}

---

## 3. Technical analysis of AI use

### 3.1 Conclusion
{Current density across the scope, in /1k, against the total ceiling. Aggregated from the per-chapter analyses — not re-estimated here.}

### 3.2 Markers present
{Reference the 14-category framework. Which categories dominate in this book, with their aggregate /1k figures.}

### 3.3 Where AI shows most
{Highest-density chapters, named, with figures.}

### 3.4 Where it reads human
{Chapters and decisions that betray real authorship. Lowest-density chapters, plus the qualitative markers: rewrites that beat the suggestion, rejected corrections that became signatures.}

### 3.5 Nature of the collaboration by layer

**Not a percentage table.** Percentages of "how much is AI" are not measurable from prose and would be invented — which defeats the purpose of a section whose whole job is to be defensible. Each layer is classified, and each classification carries its evidence.

**Classification:**
- **Authorial** — the decision was the author's, and the text is theirs or was rewritten by them
- **Assisted** — the author wrote or decided; generation contributed revision, expansion, or alternatives
- **Generated-and-curated** — generation produced the first version; the author curated item by item

| Layer | Nature | Evidence |
|---|---|---|
| Concept / premise | | |
| Macro structure | | |
| Scene outline | | |
| Dialogue | | |
| Description | | |
| Interiority | | |
| Aphorisms | | |
| Final revision | | |

**Evidence must be citable** — a revision-log figure, a decision count, a density trajectory, an outline validated before drafting. A layer with no record says so: `no record` is an honest cell, an invented classification is not.

### 3.6 Trajectory

{Density before → after, per Act, from `revision-log.md`. Number of decisions logged. This is the strongest evidence the project has, because it is counted rather than asserted.}

### 3.7 Ethical and commercial position
{Where this project sits on the declared-use spectrum. Recommended wording for the declaration, written so the author could paste it into a submission letter.}

### 3.8 Reduction plan
{Which framework categories are still over ceiling, and which revision passes address them. Effort estimate.}

---

## 4. Practical recommendations

{Ordered by priority, each with an effort estimate.}

---

## Closing notes

{Personal impression. What lingers after finishing the book.}
```

---

## Filling notes

**Honesty over kindness.** A report that only praises is useless. One that only criticizes is demoralizing and equally useless. The target is precision: say what works *and why*, what fails *and how to fix it*.

**Real comparables.** Do not invent titles or force flattering comparisons. A good comparable is one an editor would recognize instantly.

**Section 3 is the most delicate.** Every claim must come with explicit reasoning — which markers, at what density, in which chapters. Numbers without evidence are worthless, and invented numbers are worse than none: this section may end up backing a public declaration of AI use, where a fabricated figure is a reputational liability for the author rather than a reporting flaw.

**Aggregate, never re-estimate.** Section 3's figures come from the per-chapter `_analysis.md` files and from `revision-log.md`. If a chapter was never analyzed, its data is missing — say so and exclude it, rather than eyeballing a density.

**Run at the end of each Act**, not only at the end of the book. Structural problems caught early cost far less to fix.
