# Template — Craft Critique Output

Skeletons followed by the `critique-chapter` skill: the per-chapter `{chapter}_critique.md`, the scene-scoped section appended to it, the draft critique, and the synthesis written when the scope spans several chapters.

> **Write the actual critique in the project's output language.** The headings below are placeholders — translate them.

**No grades, no density.** Findings carry a reader effect, a severity, and a level; the verdict is decided by rule. All of it is defined in `craft.md`. The only numbers are counts: words per scene, shares, finding totals.

---

## Chapter critique — `{chapter}_critique.md`

```markdown
# Critique — Chapter {number}: {title}

**Scope:** chapter
**Length:** {N} words · {S} scenes
**Load-bearing scene:** scene {n} — {the turn, one sentence} — or "none: the chapter does not turn"
**Verdict:** {Works | Works with reservations | Does not work yet} — {one sentence naming the finding that decides it}
**Main level:** {sentence | scene | chapter | book} — {where most of the weight sits, one sentence}
**Findings:** {B} breaks · {F} frictions · {N} notes

{Under an `mcp` source only — the source fingerprint, exactly as `source.md` rule 6 specifies.}

---

## Reader's log

_Written during the first read, before any diagnosis._

- **Scene 1, opening → "{first words of the passage}"** — {held | dropped | lost | accelerated}. {One line: what the reader was doing.}
- **Scene 1, "{…}" → "{…}"** — {…}
- …

---

## Scene map

| # | Scene (one line) | Words | Share | Conflict | Turn |
|---|---|---|---|---|---|
| 1 | {what happens} | {N} | {N}% | {what resists — or "none"} | {what is different at the end — or "none" / "rest"} |
| 2 | … | | | | |

---

## What works

1. **"{literal quote}"** (scene {n}) — {the mechanism that makes it work, and what revision must not break}
2. …

---

## 1. Scene function

1. **"{literal quote}"** (scene {n}) — **{break | friction | note}** · {reader effect} · {level}
   {Mechanism.} {Treatment.}

2. …

---

## 2. Pacing
[same format — cite the scene map's counts as evidence]

## 3. Tension and the dramatic question
[same format]

---

## 4. Clarity and orientation
[same format]

## 5. Logic, motivation and agency
[same format]

---

## 6. Exposition
[same format]

## 7. Point of view and distance
[same format]

## 8. Dialogue
[same format]

## 9. Concreteness
[same format]

## 10. Wear
[same format]

## 11. Sentence
[same format]

---

## Outside this instrument

- {problem, one line} → `{skill}` ({why it belongs there})
- {objective error noticed, with location}

---

## VERDICT

**{Works | Works with reservations | Does not work yet}.** Decided by: {the deciding finding(s), by category and number}.

**Priorities:**

1. {most urgent — the break in the load-bearing scene, or the missing turn}
2. {next}
3. …

**Route:**
- **Scene level / chapter level:** {findings} → `restructure-chapter` or the author
- **Sentence level:** {findings} → `revise-passage` or the author
- **Book level:** {findings} → `check-arc` / `check-consistency`

**Keep:** {the short list of what works — what revision must protect}

**Open questions:** {plot or intent decisions the critique cannot make — "is the coincidence in scene 3 meant to be read as fate?"}
```

---

## Scene section — appended to `{chapter}_critique.md`

When the scope is one scene, this section is **appended** to the chapter's critique file (creating the file with only a header if it does not exist). It never replaces a chapter critique, and never touches a section carrying `R:` annotations.

```markdown
---

## Scope: scene {n} — {date}

**Scene:** {one line} · {N} words ({N}% of the chapter)
**Function in the chapter:** {what the scene is there to do}
**Conflict:** {…} · **Turn:** {… — or "none" / "rest"}
**Verdict:** {Fulfils | Fulfils in part | Does not fulfil} — {the deciding finding}

### Reader's log
- …

### What works
1. …

### Findings
1. **[{category number} {category}]** **"{literal quote}"** — **{severity}** · {reader effect} · {level}
   {Mechanism.} {Treatment.}

### Route
- …
```

Findings in a scene section are listed in one sequence, each tagged with its category, ordered by priority — a single scene rarely fills more than three or four categories, and eleven empty headings would bury them.

---

## Draft critique — `{chapter}_draft_critique.md`

Same shape as the scene section, written as its own file, with this header in place of `## Scope`:

```markdown
# Critique — Draft for chapter {number}

**Draft:** `{chapter}_draft.md` · {N} words
**Contract:** {the scene contract from `{chapter}_outline.md`, if one exists — purpose, conflict, turn}
**Verdict:** {Fulfils | Fulfils in part | Does not fulfil} — {the deciding finding}
```

A draft critique is kept separate from the chapter's because the draft is not yet the book: mixing its findings into `{chapter}_critique.md` would make the chapter's record argue about text the author has not accepted.

---

## Synthesis — `reports/literary/YYYY-MM-DD-critique-{scope}.md`

Written once per multi-chapter run, after every chapter in scope has a current critique.

```markdown
# Critique synthesis — {scope}

_Date: {date}_
_Chapters: {first}–{last} ({N} chapters, {N} words)_
_Critiqued in this run: {list} · Reused, unchanged since their critique: {list}_

---

## Verdict map

| Chapter | Verdict | Load-bearing scene | Breaks | Frictions | Main level |
|---|---|---|---|---|---|
| {id} | {verdict} | {scene n — or "none"} | {N} | {N} | {level} |

---

## Patterns across chapters

### Habits (3+ chapters)

1. **{category} — {mechanism}** — chs. {X, Y, Z}
   Evidence: "{quote}" ({ch}); "{quote}" ({ch}); "{quote}" ({ch})
   Proposal: rule in `style-guide.md` **or** declared choice in `persona.md` §6 — author's ruling

### Pacing across chapters

| Chapter | Words | Load-bearing scene share | Rest or turn |
|---|---|---|---|
| {id} | {N} | {N}% | {turn | rest} |

{Stretches: consecutive rest chapters, uniform weight — named with chapters.}

### Repeated structural devices

- **Openings:** {pattern} — chs. {…}
- **Exits:** {pattern} — chs. {…}

---

## What the sequence does well

1. …

---

## Route

1. {chapter-scoped findings → `restructure-chapter`, by chapter}
2. {book-scoped findings → `check-arc` / `review-book`}
3. {habits → `style-guide.md` or `persona.md`, pending ruling}

**Arc and tension curve:** {cite the latest `check-arc` report, or "no `check-arc` report for this scope — run it before structural revision"}
```

---

## Filling notes

**Reader's log first.** It is written during the read, before the scene map and before any category. A log written after diagnosis is a justification, not evidence.

**Quotes are literal.** For long passages: opening + `[...]` + closing.

**Empty categories.** Write "No findings in this chapter." Never skip the heading in a chapter critique — it keeps critiques comparable, and an empty category is information.

**Every finding carries five fields** — location and quote, reader effect, mechanism, severity, level. No reader effect, no finding.

**Treatments are directions, not rewrites.** At most one illustrative sentence where the direction is unclear without it. Rewriting is `revise-passage`'s job, and the author's.

**Author `R:` annotations.** The author adds lines starting with `**R:**` under each finding — accepted, done differently, rejected, or a question. **Never generate these.** Example:

```markdown
2. **"Chegaram à casa no fim da tarde. [...] e só então ela abriu a carta."**
   (scene 2) — **friction** · impatient · scene
   The drive gets 900 words before the letter, which is the scene's turn; the
   reader knows the letter exists from scene 1 and waits through the road.
   Enter at the door.
   **R:** concordo, cortei a estrada até a chegada.

5. **"Ela viu que ele estava mentindo."** (scene 3) — **friction** · distanced · sentence
   Filter verb in a close POV: the reader is told she saw instead of seeing it.
   **R:** mantive — essa narradora sempre relata o que percebe. É escolha.
```

The second annotation is the kind `consolidate-style` harvests: three of them, and "the narrator reports perception" becomes a declared choice in `persona.md` §6 — and stops being flagged.
