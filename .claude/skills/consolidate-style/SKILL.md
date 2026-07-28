---
name: consolidate-style
description: Mines the accumulated decision history — R annotations, revision log, the author's own rewrites — for patterns (three occurrences make a pattern; one makes an anecdote) and proposes evidence-backed updates to persona.md, applied only after the author's ruling. Use when the user asks to consolidate the style, or every 3-5 revised chapters.
---

# Skill: consolidate-style

**What it does.** Periodically reads the accumulated decision history — `R:` annotations, revision log, the author's own rewrites — finds patterns, and proposes evidence-backed updates to `.project/config/persona.md`. The engine behind `define-persona`'s update mode: this skill builds the diff; that one applies it through conversation.

**Triggers**
- "consolidate the style"
- "/consolidate-style"
- "what has the system learned about my voice?"
- Suggested automatically after every 3–5 chapters revised
- Equivalent phrasing in the project's output language

**Input.** None required; optionally a scope (since last consolidation — the default).

**Output.** A proposed diff to `persona.md`, presented for the author's ruling. Applied only after approval, with a changelog entry.

> **Write the proposal in the project's output language.**

---

## Core principle

> **Three occurrences make a pattern. One makes an anecdote.**

The persona must not chase every decision — a single "kept it" may be situational, a single rewrite may be mood. This skill's value is the **threshold**: it only proposes what the evidence supports, and it shows the evidence.

Every proposed change carries its receipts: the decisions, chapters, and quotes that back it. A persona built on receipts is one the author trusts — and one `draft-scene` can bet on.

---

## Execution protocol

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. `.project/config/persona.md` — current state, including its changelog (what was already consolidated)
3. `.project/reports/revision-log.md` — the decision history
4. All `_analysis.md` files with `R:` annotations since the last consolidation
5. Revised chapters vs. their pre-revision analyses — **the author's own rewrites are the richest data**

### Step 2 — Mine four pattern types

**a) Defended constructions.** The same construction type kept under analysis fire in 3+ chapters → candidate for "Personal signatures". *(Example: antithesis kept specifically at turning points, cut elsewhere — the pattern includes the context.)*

**b) Substitution habits.** When the author rewrites, what do they consistently do? Replace X-type words with Y-type; shorten; convert named emotion to gesture in their own way. These are the most generative findings — they teach `draft-scene` and `revise-passage` what the author would do.

**c) Rejection patterns.** Suggestions consistently refused (3+): the analysis is misfiring somewhere → propose raising that category's `/1k` ceiling, or adding an exception note. Check the revision-log densities first: if the chapters landed under the total ceiling anyway, the refusals are evidence the default was wrong for this book, not that the author is over-attached.

**d) Drift and evolution.** The author's revisions trending somewhere the persona doesn't describe — leaner over time, new devices appearing in their unassisted rewrites. Voice evolves; the persona must follow, dated.

### Step 3 — Check for internal conflicts

New evidence can contradict existing persona entries. Never overwrite — surface:

> "Persona v1 says you avoid sentence fragments. In the last four revised chapters you introduced eleven, all in high-tension beats. Update the entry to 'fragments in tension scenes' or keep the old rule?"

### Step 4 — Build the diff

```markdown
## Persona consolidation — {date}
_Scope: chapters {X–Y}, {N} decisions reviewed_

### Add to "Personal signatures" ({N})
1. **{construction}** — kept in {chs}, {N} decisions
   Evidence: "{quote}" ({ch}); "{quote}" ({ch})

### Adjust ceilings ({N})
1. cat. {N} ({name}): {old}/1k → {new}/1k — you kept {N} occurrences across chs. {X–Y} and the chapters still landed under the total ceiling
   Destination: `style-guide.md → Density ceilings` (project-wide) or `persona.md` §4 (voice-specific)

### Substitution habits to record ({N})
1. {pattern} — seen in {N} rewrites
   Example: "{before}" → "{after}" ({ch})

### Conflicts needing your ruling ({N})
1. {the conflict, both readings, no default}

### Model-passage candidates ({N})
1. {chapter/passage} — post-revision prose that outperforms current section-8 models
```

### Step 5 — Apply after ruling

The author approves, strikes, or amends. Apply the approved diff to `persona.md`, bump the version, write the changelog entry with the evidence scope. Report which skills benefit immediately (`analyze-chapter` stops flagging X; `draft-scene` gains Y).

---

## What to avoid

**Anecdote promotion.** Below threshold, no proposal. The persona's authority depends on its evidence bar.

**Silent application.** Every change passes the author. This file is the author's voice; they own every line.

**Averaging the voice away.** Patterns can conflict by register (lean narrator, lush interludes). Record the *conditional* pattern — "X in context Y" — never flatten to the mean.

**Ignoring the changelog.** Re-proposing something the author already struck wastes trust. The changelog is memory; read it.

**Freezing evolution.** When the current voice contradicts old entries, that is not noise — it may be growth. Date it, present it, let the author decide which self wins.

---

## Cadence

Every 3–5 revised chapters, or at each Act boundary. Late consolidation loses compounding: every chapter drafted with a stale persona costs curation effort the update would have saved.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `define-persona` | This builds the update diff; that applies it in conversation |
| `review-revision` | Primary producer of the decision data |
| `update-preserve-list` | Sibling harvester — phrases there, constructions here |
| `draft-scene` / `revise-passage` | Chief beneficiaries: sharper persona, higher survival rate |
