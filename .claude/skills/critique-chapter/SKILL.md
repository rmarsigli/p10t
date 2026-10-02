---
name: critique-chapter
description: Critiques narrative quality — scene function, pacing, tension, clarity, motivation, exposition, point of view, dialogue, concreteness, wear, sentences — across 11 craft categories, producing a _critique.md with literal quotes, a reader effect for every finding, and a verdict decided by rule (works / works with reservations / does not work yet). No grades. Scopes: one scene, one chapter, a draft, a chapter list, an Act, or the whole book, with a cross-chapter synthesis. Use when the user asks to critique a chapter, asks whether a chapter or scene works, what is slow or not working, or for an editorial read.
---

# Skill: critique-chapter

**What it does.** Reads a chapter — or a scene, a draft, an Act — the way an editor reads it, and answers *does it work?* across 11 craft categories. Produces `{chapter}_critique.md` with literal quotes, a reader effect for every finding, the level where each fix lives, and a verdict decided by rule.

The counterpart of `analyze-chapter`. That skill counts the marks generation leaves in prose; this one judges whether the narrative works, whoever wrote it.

**Triggers**
- "critique chapter X.Y"
- "/critique-chapter X.Y"
- "does chapter X work?" / "is scene 2 of X working?"
- "what's slow in X?" / "what isn't working in X?"
- "give me an editorial read of X"
- "critique Act 2" / "critique chapters 02.01 to 02.05" / "critique the book"
- "critique the draft of X.Y"
- Equivalent phrasing in the project's output language

**Input.** A scope:

| Scope | How it is named | Resolves to |
|---|---|---|
| **Scene** | "scene {n} of {chapter}" | One scene, judged inside its chapter |
| **Chapter** | a chapter id | The chapter file — the default |
| **Draft** | "the draft of {chapter}", or the `_draft.md` path | `{chapter}_draft.md` |
| **List or range** | ids, or "{first} to {last}" | Each chapter, in reading order |
| **Act** | "Act {N}" | Every chapter whose id carries that act prefix |
| **Book** | "the book" | Every chapter |

**Output**

| Scope | Writes |
|---|---|
| Chapter | `{chapter}_critique.md` |
| Scene | A section appended to `{chapter}_critique.md` |
| Draft | `{chapter}_draft_critique.md` |
| List, range, Act, book | One `{chapter}_critique.md` per chapter **and** `.project/reports/literary/YYYY-MM-DD-critique-{scope}.md` |

`_critique.md` files are satellites and sit where `.project/config/project.yaml → paths.analyses` puts analyses — next to the chapter, or in `.project/reports/technical/`. One field decides both, so critiques and analyses for a chapter are always found together.

> **Write the critique in the project's output language** (`config/project.yaml → language`), not in English.

---

## Core principle

> **A finding without a reader effect is a preference. Read as a reader first; judge after.**

Two disciplines follow, and they are the whole difference between this and an opinion:

**Every finding names what happens to the reader** — *lost*, *disbelieves*, *impatient*, *indifferent*, *has seen it*, *distanced*, *ahead*, *told twice* (the closed list in `craft.md`). If the only person affected is the critic, the text is fine and the finding is dropped.

**The page comes before the diagnosis.** The first pass is a reading, logged as reactions in sequence, with no categories in mind. The categories come after, and the log is what keeps them honest — the same evidence-first order `check-arc` uses for beats.

**No grades.** Not per category, not per chapter. `craft.md` says why. The verdict is decided by rule from the findings, so the author contests it the only way that matters: by contesting a finding.

---

## Execution protocol

### Step 0 — Resolve the scope

- **Chapters, ranges, Acts, the book:** resolve through `.project/templates/layout.md` — never by globbing. An Act resolves from the id prefix. **A mixed manuscript stops the run**, with the offending paths named.
- **Scene:** scenes are derived from the prose — the breaks in place, time, or continuous action — **never from `##` headers**, which are optional drafting scaffolding and may be absent, stale, or deliberately missing. If the author's numbering is ambiguous, show the scene map and confirm which scene they mean before critiquing it.
- **Draft:** the `_draft.md` satellite of the named chapter. If it does not exist, say so and stop.

> **Drafting scaffolding is not prose.** `##` scene headers, HTML comment notes, and budget lines are excluded from word counts. Their **absence is never a finding** — see `manuscript/README.md → Scene headers while drafting`.

### Step 1 — Load context

Read, in this order:

1. **`.project/config/project.yaml`** — output language, genre, `paths.layout`, `paths.analyses`
2. **`.project/templates/craft.md`** — the 11 categories, reader effects, severities, levels, protections, verdict rules
3. **`.project/knowledge/worldbuilding.md`** — above all **Deliberately unexplained**: withheld information there is never a finding
4. **`.project/config/persona.md`** — personal signatures, §2 syntax and rhythm, **§6 narrative craft**: declared choices are never flagged for being those choices
5. **`.project/config/style-guide.md`** — structural decisions and world rules affecting the prose: constraints to work within
6. **`.project/reports/preserve-list.md`** — never proposed for cutting, never flagged as worn
7. **`.project/config/references.md`** — with `genre`, the contract the book is judged against
8. **`.project/knowledge/characters/`** — sheets for everyone on stage: voice samples (dialogue, cat. 8) and the want/need/fear/lie engine (motivation, cat. 5)
9. **The neighbours** — the previous chapter, for what this one inherits; the next, if it exists, for what this one owes
10. **`.project/templates/chapter-critique.md`** — output skeleton

Read **after** the first pass (Step 2), never before:

11. `{chapter}_outline.md`, if it exists — intent, compared against the page, never used to read it
12. `{chapter}_analysis.md`, if it exists — to route marker problems there instead of duplicating them
13. An existing `{chapter}_critique.md` — see *Special cases*

### Step 2 — Read as a reader

Read the full text **once, in order, without categories in mind**. Log reactions as they happen — where attention held, dropped, got lost, accelerated — each anchored to the passage that caused it. This is the **Reader's log**.

Do not diagnose during this pass. A log written to support a diagnosis is a justification, not evidence.

For a scene scope, read the **whole chapter**, and log the target scene in detail. Function, pacing and tension exist only relative to the neighbouring scenes: a scene read alone looks slow when it is the planned rest after the climax.

### Step 3 — Map the scenes

For each scene, from the prose: one-line description, **word count**, share of the chapter, conflict, turn. Then **name the load-bearing scene** — the one where the chapter turns. If none turns, record it: that is the deciding finding.

**Count, never estimate.** The scene map is the only numeric evidence the critique has, and pacing findings cite it. Count words the same way `analyze-chapter` does: prose including dialogue, excluding title, epigraphs, and scaffolding.

### Step 4 — Sweep the 11 categories

In order — structure (1–3), sense (4–5), execution (6–11). For every candidate finding:

a) **Quote literally.** Never paraphrase.

b) **Check the protections**, in `craft.md`'s precedence order — deliberately unexplained, persona, style guide, preserve list, genre contract. A protected item is not a finding.

c) **Check the boundaries.** A problem that belongs to another instrument — a marker, a cross-chapter repetition, a contradiction with an established fact — goes to **Outside this instrument** in one line, with its destination.

d) **Name the reader effect** from the closed list. None fits → drop the finding.

e) **Record mechanism, severity, level, and a treatment.** The treatment is a direction, not a rewrite: at most one illustrative sentence where the direction is unclear without it.

Empty category → "No findings in this chapter." Never invent findings to fill one.

### Step 5 — Record what works

With the same rigor as the findings: literal quote, and the mechanism that makes it work. This section tells the author what revision must not break — a critique that only lists problems leaves them revising the strengths away.

### Step 6 — Verdict, priorities, route

a) **Apply the verdict rule** from `craft.md` — chapter rule for chapters, scene rule for scenes and drafts. Name the deciding finding.

b) **Priorities**, in `craft.md`'s order: the break in the load-bearing scene (or the missing turn) first, then scene- and chapter-level problems, then other breaks, then clustered frictions.

c) **Route by level** — chapter and scene level to `restructure-chapter` or the author, sentence level to `revise-passage` or the author, book level to `check-arc` / `check-consistency`.

d) **Open questions** — the intent and plot decisions the critique cannot make. Ask them; do not answer them.

### Step 7 — Write and report back

Follow `.project/templates/chapter-critique.md`. Report back in chat: verdict and the finding that decides it, main level, counts by severity, top three priorities, file path.

---

## Multi-chapter scope

For a list, a range, an Act, or the book:

1. **Chapter by chapter, in reading order.** Each chapter gets the full protocol above, with its neighbours as context. Critiquing an Act in one undifferentiated pass degrades the reading of every chapter in it.
2. **Reuse what is still current.** A `{chapter}_critique.md` is current when the chapter has not changed since it was written: the chapter has **no uncommitted changes**, and **no commit touching the chapter is newer** than the latest commit touching the critique (`git log -1 --format=%ct -- <file>` on both). A critique not yet committed counts as current against a clean chapter. Reuse current critiques and say which were reused. When git cannot answer, re-critique — a stale critique reused is a confident report on text that no longer exists.
3. **Never overwrite a critique carrying `R:`** — see *Special cases*. In a multi-chapter run, a stale annotated critique is listed as stale and left alone, and the synthesis uses it with that caveat.
4. **Then the synthesis.** Read the per-chapter critiques and the chapters' scene maps, and look for what only exists across chapters (`craft.md → Patterns across chapters`): pacing across chapters, repeated openings and exits, habits (same category and mechanism in three or more chapters), and the verdict map.
5. **Cite `check-arc`, never rebuild it.** The book's tension curve and arcs belong to `check-arc`. If its latest report covers the scope, cite it; if not, say so and recommend running it before structural revision.

---

## Critical rules

1. **Quotes are always literal.** For long passages: opening + `[...]` + closing.

2. **No grades.** No score, no average, no number that is not a count. The verdict is decided by rule.

3. **Reader effect or nothing.** A finding without one is dropped.

4. **Protections override the framework.** Deliberately unexplained, declared choices, structural rules, preserved phrases, and the genre contract are never findings.

5. **One finding, one home.** Markers go to `analyze-chapter`, cross-chapter repetition to `scan-recurrences`, contradictions to `check-consistency`. Route in one line; do not duplicate.

6. **Do not inflate.** A chapter that works deserves the truth: "Works. No breaks; three frictions, all sentence level." Do not manufacture problems to justify the invocation.

7. **Strengths get the same rigor.** Quote and mechanism, never "the dialogue is good".

8. **Judge the book it is.** Against its own genre, references, and declared choices — never against a structural convention or a book the critic would prefer.

9. **Never rewrite.** Treatments are directions. Rewriting belongs to the author and to `revise-passage`; restructuring plans to `restructure-chapter`.

10. **Never generate `R:` annotations.** The author writes those.

11. **Never touch the manuscript.** The critique is a satellite file. It never edits the chapter, the draft, or any `.project/` file.

12. **Output language.** Write the entire critique in the project's output language.

---

## Special cases

**Chapter already critiqued, with `R:` annotations.** Do not overwrite. Ask:
- Full re-critique (discards the annotations)
- Diff critique — compare against the previous critique, focus on what changed, and say which earlier findings were resolved
- Cancel

**Scene scope on a chapter that already has a critique.** Append the scene section; never rewrite the existing sections. If the existing chapter critique already has a finding about this scene, reference it instead of repeating it.

**Draft scope.** Write `{chapter}_draft_critique.md`, never into `{chapter}_critique.md` — the draft is not yet the book, and the chapter's record must not argue about text the author has not accepted. If `{chapter}_outline.md` holds a contract for the drafted scene, judge the draft against it **after** the reader's pass: does the page deliver the purpose, conflict, and turn the contract specified?

**A chapter that works.** Short critique: the verdict, the frictions worth a look, a longer **What works**. Flag it as a `persona.md` §8 model-passage candidate if the craft is exemplary.

**The author's diagnosis.** If the author said "the middle drags", verify it against the log and the scene map before accepting it. The complaint is usually accurate about *where* something feels wrong and often wrong about *why*.

**First critique of the project.** Calibrate: explain the reader effects and the verdict rule once, briefly, so the vocabulary of the next critiques is shared.

---

## After the critique

Suggest next steps:
- Chapter- or scene-level findings → `restructure-chapter`, **before** `analyze-chapter`: counting the markers of prose about to be restructured is wasted work
- Sentence-level findings only → `analyze-chapter`, then the `R:` cycle
- The author annotates `R:` under each finding, commits the chapter, then rewrites — `review-revision` evaluates the rewrite against both files
- A habit found in a multi-chapter synthesis → the author rules: rule in `style-guide.md`, or declared choice in `persona.md` §6

Suggest a commit line if the author wants one (`analyze({chapter}): critique the {title}`); never commit.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `analyze-chapter` | Sibling microscope — markers counted there, craft judged here. Run this one first |
| `restructure-chapter` | Where scene- and chapter-level findings become a plan |
| `revise-passage` | Where sentence-level findings become a rewrite |
| `check-arc` | Owns the book's tension curve and arcs; the synthesis cites it |
| `check-consistency` | Owns contradictions with established facts |
| `scan-recurrences` | Owns repetition across chapters; wear here is the reader's library, not the book |
| `review-revision` | Evaluates the rewrite against the `R:`-annotated critique, and logs the verdict before → after |
| `consolidate-style` | Harvests rejected craft findings as declared choices for `persona.md` §6 |
| `review-book` | Aggregates the chapter verdicts; never re-judges them |
