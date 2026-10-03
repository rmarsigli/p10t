---
name: translate-chapter
description: Produces one chapter of a target-language edition by transcreation under the crossing contract — the book's own rules outrank fidelity to the source sentence — and delivers it with a report in the project's output language explaining every choice, so an author who cannot judge the target language can still rule on the work. Hard-stops on open lexicon terms and on an incomplete contract. Use when the user asks to translate a chapter or produce a chapter of a target-language edition.
---

# Skill: translate-chapter

**What it does.** Translates one chapter into a target-language edition, obeying `translations/{locale}/localization.md`. **Context-expensive by design**, for the same reason as `draft-scene`: prose born inside the voice, not prose cleaned afterwards.

**Triggers**
- "translate chapter 01.03 to English"
- "/translate-chapter en-US 01.03"
- "produce the French version of chapter X"
- Equivalent phrasing in the project's output language

**Input.** A target locale and a chapter id.

**Output.** Two files in `translations/{locale}/manuscript/`, resolved through `paths.layout`:

| File | Language | Purpose |
|---|---|---|
| `{chapter}.md` | target | the prose |
| `{chapter}_report.md` | **output language** | **the primary deliverable** — what the author actually rules on |

**Read `.project/templates/localization.md` before starting.**

---

## Core principle

> **The book's rules outrank the source sentence.**

This is transcreation, not translation. Where a faithful rendering of the source sentence would break a rule the book imposes on itself, the rule wins and the sentence is rebuilt. The target edition obeys the same law as the source — not the same syntax.

**And the principle that follows from who reads the output:**

> **When the author cannot judge the target language, the report is the deliverable and the prose is the attachment.**

An author who reads functional English but not literary English cannot rule on "does this sound native". They can rule on "here is what I did, here is why, here is what it cost". Every choice that is not obvious gets an argument, in a language they command.

---

## Hard rules (before anything else)

1. **No complete contract, no translation.** If `localization.md` is missing, or any rule in `style-guide.md` or signature in `persona.md` carries no verdict, stop and route to `define-localization`. Name the unclassified rules. An incomplete contract does not fail loudly — it silently produces prose with no basis for evaluation.

2. **An open lexicon entry is a hard stop.** If the chapter contains a term, designation or preserved phrase whose target form is `[?]`, stop. Name the term, name what it depends on, and stop. **Do not choose. Do not propose a provisional. Do not proceed with a footnote.** These words appear in every chapter; a wrong one is discovered late and costs the whole edition.

3. **The lexicon is validated against the source.** Every source term in `lexicon.md` must still exist in `knowledge/glossary.md`. On a mismatch, refuse and name the term — it means the source renamed something and the edition is translating a word the book no longer uses.

4. **Never touch the source.** The source manuscript, `persona.md`, `style-guide.md`, `glossary.md` and `preserve-list.md` are read-only here. Findings about the source go in the report; the author rules.

5. **Never convert a measurement.** Consult `referents.md`. If the measurement is not listed, it is a finding, not a calculation. Probabilities, percentages, milliseconds and counts are never converted at all.

6. **Never move the setting.**

---

## Execution protocol

### Step 1 — Eligibility

Check whether the chapter has been revised in the source language (`project.yaml → status`, `reports/revision-log.md`).

If it has not: **warn and ask**, do not refuse. Transcreation has no partial update, so a later `restructure-chapter` invalidates this work wholesale — say so with the cost named. A pilot translation to calibrate the contract is a legitimate override, and the first chapter usually is one.

### Step 2 — Full context load

1. `.project/config/project.yaml` — output language, `paths.layout`, `paths.naming`
2. `.project/templates/layout.md` — how to resolve the chapter file, in both trees
3. **`translations/{locale}/localization.md`** — the contract. Read every verdict; they are the operating instructions for the rest of this run
4. **`translations/{locale}/lexicon.md`** — locked pairs. Run hard rules 2 and 3 now, before any prose
5. `translations/{locale}/referents.md`
6. **The source chapter**
7. `.project/config/persona.md` — the signatures, read *through* the contract's verdicts
8. `.project/config/style-guide.md`
9. `.project/knowledge/worldbuilding.md` and the character sheets for anyone on stage — voice sections above all
10. `.project/reports/preserve-list.md` — each entry's locked target form
11. **The previously translated chapter**, if one exists — continuity of the target voice matters as much as continuity of the source voice
12. `translations/{locale}/status.md`

### Step 3 — Build the crossing sheet

Before writing a line, compile (internally) what this specific chapter needs:

- **Active verdicts** — which contract entries this chapter actually triggers. A dialogue-heavy chapter triggers different ones than an interior one
- **Replacements in play** — for every *does not cross* verdict active here, the declared substitute, ready to apply. This is where the null-subject replacement gets planned rather than improvised
- **Locked pairs present** — every term, designation and preserved phrase appearing in this chapter, with its one target form
- **Referents present** — including measurements, taken from the file, not computed
- **Watchlist for this chapter** — the target-language AI markers most likely here, and the pre-registered signature collisions that must **not** be treated as tics
- **Length signal** — the source word count. Expect drift: en-US typically runs shorter than pt-BR, fr-FR longer. Report the delta; do not pad or compress to hit a number

### Step 4 — Transcreate

Write the chapter against the crossing sheet.

**Where the source sentence and a rule collide, the rule wins and the sentence is rebuilt.** Record the collision — it is a report entry, not a silent fix.

**Three things to hold throughout:**

- **Signatures marked *crosses intact* must actually appear.** A translation that renders the meaning and drops the author's constructions is the failure mode this whole subsystem exists to prevent. If a signature had no opportunity in this chapter, that is fine and reportable; if it had one and was not used, that is a defect.
- **Substitutes are used deliberately, not opportunistically.** A *crosses with another tool* verdict names one mechanism. Use that one.
- **The register the source breaks, the target breaks too.** Where the source shifts from formal to blunt, the target shifts at the same point, by the same distance, with the target's own materials.

### Step 5 — Self-audit before delivery

Check the produced prose, in this order, and fix what fails:

1. **Locked pairs** — every occurrence uses the one agreed form. No synonyms, no "for variety".
2. **Prohibitions** — none of the forbidden renderings from `lexicon.md` appear anywhere.
3. **Verdicts honoured** — every active *does not cross* rule actually used its declared replacement. Count what the source rule counted: if the source caps namings per paragraph, count namings per paragraph in the target.
4. **Target-language tics** — against the contract's watchlist. Pre-registered signature collisions are **not** flagged.
5. **Typographic profile** — dialogue marking, numbers, dates, in-world registers.
6. **Setting integrity** — no referent quietly relocated, no measurement computed.

### Step 6 — Write the report

**In the project's output language.** This is the deliverable.

```markdown
# {chapter} — {locale} · translation report

## 1. Summary
Source words → target words (delta). Verdicts triggered. Findings count. What needs a ruling.

## 2. Rebuilt passages
Every place a rule outranked the source sentence.
Source quote · target quote · which rule · what the substitute was · what it cost.

## 3. Choices that needed an argument
Anything not mechanical: register, idiom, a term with two defensible renderings,
a joke rebuilt on different material. One short paragraph of reasoning each.

## 4. Signatures
Per signature active in this chapter: whether it appears, where, and how it was carried.
Anything that had an opportunity and did not land is listed as a defect, not an omission.

## 5. Findings for the author — needs a ruling
- **Uncatalogued referents** — found in the source, not in `referents.md`. Proposed entries.
- **Leaks** — source-language culture in a setting that is not its own. Worth fixing in the
  source too; propose the source-language wording as well.
- **Open terms encountered** — if the run stopped, this is the whole report.
- **Source problems** — contradictions, drift, anything translation surfaced. Reported, never fixed.

## 6. Residual risk
What the machine cannot verify about its own output in this language, stated plainly.
The native-reader gate state for this chapter.
```

⚠️ **Section 5 never edits anything.** Referents, leaks and glossary drift are proposals. The author rules; `define-localization` or the author's own hand applies.

### Step 7 — Update state and hand off

Append or update this chapter's row in `status.md`: source id, **the current commit of the source chapter** (`git log -1 --format=%H -- <source path>`) — or, under an `mcp` source, the chapter's **short fingerprint** (`.project/templates/source.md` rule 6) — stage `translated`, native gate `pending`.

Then: report the length delta, name the findings count, and say what is next — `review-translation` for this chapter, or a ruling on the findings first. Suggest a commit line; **do not commit**.

---

## What to avoid

**Translating fluently past a rule.** The most dangerous output of this skill is a correct, natural translation that quietly breaks the book's own constraints. It reads well and passes every check the author can personally run.

**Silent fixes.** A rebuilt sentence that is not in section 2 is a decision the author never got to make.

**Variety in a locked pair.** Prose instinct says vary the word. A motif says do not. The lexicon wins.

**Padding to the source length.** Languages have different densities. Report the delta.

**Inventing a referent.** If it is not in `referents.md`, it is a finding.

**Doing `review-translation`'s job.** The self-audit checks this skill's own compliance. Blind back-translation and the independent tic pass belong to the review skill, and doing them here means the same pass grading itself.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `define-localization` | Provides the contract. This skill refuses to run without a complete one |
| `review-translation` | Runs after; verifies independently and updates the stage |
| `analyze-chapter` | **Untouched.** Its 14 categories are calibrated for the source language; the watchlist is used instead |
| `restructure-chapter` | Restructuring a translated source chapter invalidates its translation wholesale |
| `commit` | Suggested, never invoked |

---

## Maintenance

- **When a contract verdict changes**, chapters translated under the old one are stale. `status.md` names them.
- **When the source chapter changes**, `git log <source_commit>..HEAD -- <path>` says exactly what — or, under an `mcp` source, the fingerprint comparison of `source.md` rule 7 says which scenes.
- **When findings accumulate unruled**, stop translating. Each unresolved referent multiplies across every remaining chapter.
