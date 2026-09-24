---
name: review-translation
description: Verifies a translated chapter independently of the pass that produced it — blind back-translation to expose meaning drift, a tic sweep against the target language's own markers, locked-pair and contract compliance, and staleness against the source commit. Produces its report in the project's output language, for an author who cannot audit the target language directly. Use when the user asks to review a translation, check a translated chapter, or clear a chapter for the native-reader gate.
---

# Skill: review-translation

**What it does.** Audits `translations/{locale}/manuscript/{chapter}.md` against the source, the contract, and the target language itself. Closes the loop `translate-chapter` opens.

**Triggers**
- "review the English translation of 01.03"
- "/review-translation en-US 01.03"
- "is this translation still current"
- Equivalent phrasing in the project's output language

**Input.** A target locale and a chapter id.

**Output.** `{chapter}_report.md` gains a **Review** section, and `status.md` is updated. **In the project's output language.**

**Read `.project/templates/localization.md` before starting.**

---

## Core principle

> **The author cannot check this work, so the verification has to be structural.**

Everything else in p10t rests on the author reading the output and ruling on it. Here that assumption fails: an author with functional but not literary command of the target language cannot tell a faithful sentence from a plausible one, or native rhythm from translated rhythm.

So this skill does not ask the author to judge the prose. It produces **evidence about the prose, in a language they command** — and it states, without softening, what it could not verify.

---

## Hard rules

1. **Never rewrite.** This skill reports. Fixes are a second `translate-chapter` pass or the author's own hand.
2. **Never clear the native gate.** Only a named human reader clears it. The skill records the state; it does not grant it.
3. **Never touch the source.**
4. **Never soften residual risk.** An honest "I cannot verify this" is the most valuable line in the report.

---

## Execution protocol

### Step 1 — Back-translate first, before anything else

**Do this before reading the source chapter.** Once the source is loaded, the back-translation is contaminated: the pass reproduces what it knows the source said instead of what the target text actually says.

1. Read only `translations/{locale}/manuscript/{chapter}.md`.
2. Render it back into the output language — plainly, literally, no repair. **Translate what is on the page, not what it was probably meant to say.** A clumsy back-translation of a clumsy sentence is a finding, not something to tidy.
3. Write it down before proceeding.

⚠️ **State the limitation in the report.** A single pass that produced the translation and then reviews it is not a truly independent reader, however the steps are ordered. Ordering reduces contamination; it does not eliminate it. This is exactly why the native gate exists, and the report must say so rather than implying the check is stronger than it is.

### Step 2 — Load everything else

1. `.project/config/project.yaml` — output language, layout
2. **The source chapter**
3. `translations/{locale}/localization.md` — verdicts and watchlist
4. `translations/{locale}/lexicon.md` and `referents.md`
5. `.project/config/persona.md`, `.project/config/style-guide.md`
6. `.project/reports/preserve-list.md`
7. `translations/{locale}/manuscript/{chapter}_report.md` — what the translation pass claimed it did
8. `translations/{locale}/status.md`

### Step 3 — Meaning drift

Compare the back-translation against the source. Classify each divergence:

| Class | Meaning | Action |
|---|---|---|
| **Sanctioned** | a rebuild the contract required, and section 2 of the report declares it | none — verify it is declared |
| **Undeclared** | the target says something different, and the report does not mention it | **finding** — quote both sides |
| **Loss** | something in the source is simply not in the target | **finding**, with what was lost named |
| **Addition** | the target says something the source does not | **finding** — usually the machine explaining what the source left implicit |

⚠️ **Addition is the class to hunt hardest.** A generated translation's characteristic failure is not error, it is *helpfulness*: filling an ellipsis, resolving an ambiguity the book kept open, naming an emotion the source delivered as procedure. Every one of those is a book decision quietly reversed, and it reads as good prose.

Cross-check additions against `worldbuilding.md`'s deliberately-unexplained list. An addition that touches one is the most severe finding this skill can produce.

### Step 4 — Contract compliance

For every verdict active in this chapter:

- **crosses intact** — did the device actually survive? Quote where.
- **crosses with another tool** — was the *declared* substitute used, or a different one improvised?
- **does not cross** — was the replacement applied, and does the target meet what the source rule measured? Where the source caps a count, count it in the target and give the figure.

Report per-1k figures for anything the contract kept a ceiling on, in the same unit the rest of the system uses.

### Step 5 — Target-language tic sweep

Against the contract's watchlist, **not** `framework.md`.

Pre-registered signature collisions are not findings. Everything else is, with a literal quote and a per-1k figure.

⚠️ **This is where risk concentrates.** The source manuscript may be entirely the author's own prose; the target chapter is entirely machine-produced. It is the single place in the project where an AI-tic sweep is auditing genuinely generated text, and it should be read as the most load-bearing section of the report.

### Step 6 — Locked pairs and referents

- Every term, designation and preserved phrase: **one** form, everywhere. List any that varied, with all forms found.
- Every prohibition in `lexicon.md`: absent. List any that appeared.
- Every referent: matches `referents.md`. Flag anything rendered from instinct instead.
- Every measurement: matches the file. **A measurement not in the file is a finding regardless of whether the number is right** — a correct guess is still an ungoverned conversion, and the next chapter's will not be.
- Source terms in `lexicon.md` still present in `glossary.md`.

### Step 7 — Staleness

```sh
git log <source_commit>..HEAD -- <source chapter path>
```

`source_commit` comes from `status.md`. Empty output: current. Otherwise, name the commits and say what changed — and whether it is a copy-edit or a rebuild, because under transcreation there is no partial update and a rebuild means retranslating the chapter.

⚠️ **Do not diff the two editions line by line.** Transcreation legitimately reorders and rebuilds; an alignment that works on a descriptive chapter fails on the chapter that was restructured most, and reports clean for the worst case.

### Step 8 — Write the review and update state

Append to `{chapter}_report.md`:

```markdown
## Review — {date}

### Verdict
Ready for the native gate · needs fixes · stale, retranslate.

### Meaning drift
Undeclared, losses, additions. Source quote · back-translation quote · severity.

### Contract compliance
Per active verdict: honoured / improvised / missed. Figures where a ceiling applies.

### Target-language tics
Per watchlist entry: occurrences, per-1k, literal quotes. Collisions excluded and named as excluded.

### Locked pairs and referents
Variations, prohibitions breached, ungoverned conversions.

### Staleness
Source commit, current commit, what changed.

### What I could not verify
Plainly. Rhythm, idiomatic naturalness, register, whether a sentence reads as translated —
and the fact that this review shares a pass with the translation it audits.
Native gate: {state}.
```

Update `status.md`: stage `reviewed` when the verdict is clean, native gate unchanged unless a human cleared it and the author says so.

Close by naming the top three things to fix, in priority order. Suggest a commit line; **do not commit**.

---

## What to avoid

**Grading the prose you just wrote.** Order the steps as written. Back-translation before the source, always.

**Confidence about the target language.** The value here is structural checks and honest limits, not an opinion on whether English prose sings.

**Flagging pre-registered signatures.** They are in the contract precisely so they are not flagged every chapter. Flag them once and the author stops reading the report.

**Silently accepting an addition because it improves the sentence.** Improvement is not the standard. The source is.

**Clearing the native gate.** Not this skill's to grant, ever.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `translate-chapter` | Produces what this audits. Fixes are a second pass of it |
| `define-localization` | Owns the watchlist and the verdicts this checks against |
| `review-revision` | The source-language analogue. Independent: neither reads the other's log |
| `review-book` | A target edition's whole-book report uses this edition's AI declaration, never the source's |

---

## Maintenance

- **When the same tic recurs across three chapters**, it is a contract gap, not three defects. Route to `define-localization`.
- **When drift additions cluster on one kind of passage** — implied emotion, open endings — that is a systematic behaviour of the translation pass. Name it as a pattern and add it to the watchlist.
- **When a native reader returns corrections**, they outrank everything in this report. Record what they caught, and check whether the contract could have caught it — that is how the watchlist gets real.
