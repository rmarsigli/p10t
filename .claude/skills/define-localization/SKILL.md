---
name: define-localization
description: Builds the crossing contract for one target-language edition — every style rule and persona signature classified as crossing intact, crossing with another tool, or not crossing at all, plus the typographic profile, the target-language tic watchlist, and the edition's own AI declaration. Run once per target language, before any chapter is translated. Use when the user asks to set up a translation, add a target language, or define how the book crosses into another language.
---

# Skill: define-localization

**What it does.** Creates `translations/{locale}/localization.md` — the contract a translation obeys. Turns "translate it to English" into a decided position on every device the book uses.

**Triggers**
- "set up the English translation" / "add French as a target language"
- "/define-localization"
- "how does the book cross into {language}"
- Equivalent phrasing in the project's output language

**Input.** The target locale, as a BCP 47 tag.

**Output.** `translations/{locale}/localization.md`, plus the empty scaffolding for `lexicon.md`, `referents.md` and `status.md`.

> **Write the file in the project's output language** — it is a document the author rules on, not one the translation reads aloud. Quoted target-language examples stay in the target language.

**Read `.project/templates/localization.md` before starting.** It defines the layout, the three verdicts, and the rules this skill must not contradict.

---

## Core principle

> **Decide cold, once, in a document — never in the middle of a sentence.**

A translator meeting a rule conflict mid-paragraph resolves it in whichever direction the sentence pushes. The next chapter resolves it the other way. Neither decision is recorded, and the edition ends up with no position at all.

The contract exists so that `translate-chapter` never has to decide anything. Every conflict it can hit has already been ruled on.

**The second principle, which the author must state before anything else is written:**

> **The setting never moves.** The edition changes the language, never the map.

---

## Protocol

### Step 1 — Refuse to duplicate

If `translations/{locale}/localization.md` already exists, this is an **update**, not a build. Read it, ask what changed, and amend — never overwrite. A contract that has translated chapters behind it is load-bearing: changing a verdict invalidates the chapters that followed the old one. Say so, and name them from `status.md`.

### Step 2 — Load context

1. `.project/config/project.yaml` — output language, `paths.layout`, `paths.naming`
2. `.project/config/persona.md` — **the signatures are the real work of this skill**
3. `.project/config/style-guide.md` — the book's hard rules
4. `.project/knowledge/glossary.md` — thesis vocabulary
5. `.project/reports/preserve-list.md` — phrases that will need locked pairs
6. `.project/knowledge/worldbuilding.md` — for open questions a term depends on
7. Any hand-written regionalization notes the book already keeps

### Step 3 — Establish the four fields

Ask, and record:

- **`prose_language`** — from `project.yaml`
- **`setting_locale`** — where the book takes place. **Ask explicitly. Never infer it from the prose language.** A book written in Portuguese and set in the US is common and the whole contract depends on knowing it.
- **`target_prose_language`** — this edition
- The setting locale of the target edition, which is the source one, restated so it cannot be quietly changed later

If the author has never separated setting from language before, this question does real work on its own: it surfaces every place the source leaked its own culture into a setting that is not its own.

### Step 4 — Classify every rule and signature

The heart of the skill. Walk `style-guide.md` and `persona.md` item by item. Each gets **one of three verdicts** and nothing else:

**a) crosses intact** — the device works identically. Record it anyway; silence is not a verdict, and the next reader needs to know it was considered.

**b) crosses with another tool** — name the substitute concretely. "Adapt the punctuation" is not a verdict. *"Ellipsis marks trailing-off in English; self-interruption is the em-dash — translate the signal, not the glyph"* is.

**c) does not cross** — state why, then declare the replacement, or retire the rule with its ceiling at zero.

**Where to look hardest.** Devices bind to grammar, and these three break most often:

- **Anything whose tool is subject elision.** Portuguese, Spanish and Italian drop the subject; English, French and German cannot. A rule capping how often characters are named usually has the null subject as its mechanism — and loses it. The replacement is structural: action beat, identifying gesture, reordered line.
- **Anything that is a tic in the source and an error in the target.** The comma splice is the standard case. Ceiling to zero, rule retired, and it usually costs nothing.
- **Anything typographic.** Dialogue marking, quote nesting, dash spacing. The same device takes opposite verdicts across two targets, which is why this file is per language.

**Two failure modes to name aloud when they appear:**

- A verdict of *crosses intact* given to a device the agent did not actually test against the target grammar. Ask: what would this sentence look like? If the answer is not producible, it is not a verdict.
- A signature classified as *does not cross* because it is hard, when the author would rather keep it. That is the author's ruling, not the skill's. Present the difficulty and the cost; let them decide.

### Step 5 — Build the typographic profile

Dialogue marking, punctuation placement relative to quotes, thousands separator, decimal mark, date format, dash spacing, and the marking of any in-world register the book uses.

⚠️ **Sort the semantic from the merely typographic.** A book marking radio speech in italics is not making a typographic choice — it is encoding *who can hear this*. That crosses as meaning and may need a different mark in the target. Ask, for each convention: *does the reader learn something from this mark, or only read more comfortably?*

### Step 6 — Build the target-language tic watchlist

`framework.md`'s categories are calibrated for the prose language. The target has its own AI markers. Write them for **this** target: the constructions a generated text in that language falls into.

Then do the part that matters more: **find the collisions.** Cross the watchlist against `persona.md` §"signatures". Where a genuine authorial signature coincides with a target-language AI marker, record both facts in one entry. Without this, `review-translation` flags the author's best construction every chapter, and the author learns to ignore the report.

### Step 7 — Write the edition's AI declaration

Draft it, and get the author's explicit approval on the wording.

State plainly what is true: the target prose is machine-produced, curated by the author, cleared or not cleared by a native reader. The source declaration does not apply here and must not be copied. This text goes on the edition's title page.

### Step 8 — Set the native-reader gate

Ask whether the author can judge literary prose in the target language — rhythm, register, whether a sentence reads as translated.

If they cannot, the gate is **required and blocking**: no chapter is submission-ready before a native reader clears it. Record what the clearance covers, and that `status.md` tracks it per chapter.

This question is not a formality. The answer decides whether the reports `translate-chapter` produces are a convenience or the only thing the author can actually rule on.

### Step 9 — Scaffold and hand off

Create `lexicon.md`, `referents.md` and `status.md` with their headers and the entry formats from `templates/localization.md`.

Then name what is still blocking, from the source's own open questions: every glossary term, designation and preserved phrase without a target form. **List them.** These are what `translate-chapter` will hard-stop on, and the author can rule on them now, cold, rather than being interrupted mid-chapter later.

---

## What to avoid

**Leaving a rule unclassified.** There is no fourth verdict. An unclassified rule does not raise an error later — it produces prose the author has no basis to evaluate.

**Copying the source AI declaration.** It is false of a generated translation, and `review-book` treats it as an evidence base.

**Deciding a lexicon entry here.** This file rules on *devices*. Terms are `lexicon.md`, and a term that depends on an open world question goes back to `worldbuilding.md` — it is not resolved in passing.

**Moving the setting.** If the author asks for it, they are asking for an adaptation, not a translation. Say so plainly, then do what they decide.

**Treating a hard signature as impossible.** Difficulty is a cost to present, not a verdict to issue.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `translate-chapter` | Refuses to run without a complete contract; consults it for every conflict |
| `review-translation` | Runs its tic pass against this file's watchlist, not against `framework.md` |
| `define-persona` | Source of the signatures being classified. **Never modified by this skill** |
| `consolidate-style` | When it adds a signature to `persona.md`, that signature has no verdict yet — this skill runs again |

---

## Maintenance

- **When `persona.md` or `style-guide.md` gains a rule**, the contract is incomplete again. Re-run in update mode.
- **When a verdict changes**, name the already-translated chapters it invalidates, from `status.md`. Changing a verdict silently leaves the edition internally inconsistent.
- **Per target language.** A second target inherits nothing from the first. Same book, different grammar, different verdicts.
