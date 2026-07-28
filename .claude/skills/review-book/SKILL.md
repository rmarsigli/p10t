---
name: review-book
description: Produces the whole-book report — literary review, commercial assessment, and technical AI-use analysis — with evidence for every claim, saved to .project/reports/literary/. Run at the end of each Act, not only at the end of the manuscript. Use when the user asks to review the book, run the full report, or review an Act.
---

# Skill: review-book

**What it does.** Produces the whole-book report: literary review, commercial assessment, and technical AI-use analysis. The wide-angle counterpart to `analyze-chapter`'s microscope.

**Triggers**
- "review the book"
- "/review-book"
- "run the full report"
- "review Act {N}"
- Equivalent phrasing in the project's output language

**Input.** Scope: whole book (default) or a single Act.

**Output.** `.project/reports/literary/YYYY-MM-DD-review-{scope}.md`, following `.project/templates/book-review.md`.

> **Write the report in the project's output language.**

---

## Core principle

> **Honesty over kindness, precision over both.**

A report that only praises is useless. One that only criticizes is demoralizing and equally useless. The target: what works *and why*, what fails *and how to fix it*, with evidence for every claim.

Three audiences read this report: the author deciding what to revise, the author deciding whether to submit, and — potentially — the material behind an honest AI-use declaration. All three need evidence, not adjectives.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language, genre, targets
2. **The entire manuscript in scope** — read fully, in order. No skimming; structural judgments require having actually felt the pacing
3. `.project/knowledge/` — worldbuilding, characters, timeline (to judge delivery against intent)
4. `.project/reports/technical/` and existing `_analysis.md` files — per-chapter density data
5. `.project/reports/recurrences.md` and `revision-log.md` — revision history
6. `.project/config/references.md` — for comparable-title reasoning
7. `.project/templates/book-review.md` — the skeleton

### Step 2 — Literary review

Work through architecture, premise, characters, prose, themes. Discipline points:

- **Every structural claim cites chapters.** "The middle sags" is worthless; "chapters 08–10 repeat the same beat: discovery, retreat, notebook entry" is actionable.
- **Characters are judged by arc delivery**, not likability: does the page deliver what the sheet intends?
- **The thesis test:** state the book's thesis in one line, then check whether the ending pays it. Books that lose their thesis in the final act fail here even when every scene works locally.
- **Strengths get the same rigor as weaknesses.** The author needs to know what to protect during revision, not just what to fix.

### Step 3 — Commercial assessment

- **Comparables must be real and current** — titles an editor would recognize. If uncertain about the current market, say so rather than invent.
- **The elevator pitch is a deliverable**, not a summary: two sentences that sell, written as the author could use them.
- **Risks come with mitigations** or they are just anxiety.
- **Probability scenarios stay qualitative and honest** — no fake percentages with false precision.

### Step 4 — Technical AI-use analysis

- Aggregate the per-chapter density data into the layer table (concept / structure / dialogue / description / etc.).
- **Every estimate carries its reasoning:** which markers, what density, which chapters. Numbers without evidence are worthless.
- Chart the trajectory if revisions exist: density before → after, per Act. This is the evidence base for the declaration.
- Position the project on the declared-use spectrum and recommend the declaration language.

### Step 5 — Recommendations

Ordered by **impact per effort**. Each with an effort estimate. The author should be able to read only this section and know what to do next month.

### Step 6 — Deliver

Save to `reports/literary/`. Summarize in chat: verdict in three lines, top three recommendations, and one thing the book does well that revision must not break.

---

## What to avoid

**Chapter-analysis duplication.** This report does not re-list tics — it references the technical layer and aggregates. The microscope work stays in `analyze-chapter`.

**Praise inflation and hedge inflation.** "Promising", "interesting", "could be stronger" — banned without a concrete follow-up.

**Inventing market facts.** Comparable sales figures, submission odds, editor preferences — if not known, not stated.

**Reviewing the book it isn't.** Judge the book against its own thesis and genre contract, not against a different book the reviewer might prefer.

---

## Cadence

Run at the end of each Act, not only at the end of the manuscript. Structural problems caught at Act 1 cost a rewrite of one act; caught at the end, they cost the book.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `analyze-chapter` | Supplies the per-chapter density data this aggregates |
| `check-consistency` / `check-arc` | Narrower structural instruments; their findings feed section 1 |
| `define-references` | Supplies comparable-title grounding |
