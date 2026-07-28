---
name: revise-passage
description: Surgically rewrites a specific passage applying the full project checklist — diagnoses before cutting, preserves every author word that can stay, and presents the result as an annotated comparison, never applied directly. If the passage is fine, says so. Use when the user asks to revise, rework, or fix a specific passage, paragraph, or dialogue.
---

# Skill: revise-passage

**What it does.** Rewrites a specific passage of existing text applying the full project checklist — persona, framework, world guards, character voices. Sibling of `draft-scene`: same context load, applied to existing prose instead of a blank page.

**Triggers**
- "revise this passage: {...}"
- "/revise-passage"
- "rewrite this paragraph without the tics"
- "this dialogue isn't working, rework it"
- Equivalent phrasing in the project's output language

**Input.** The passage (pasted or located by chapter + quote), plus optionally **what bothers the author** about it. If no complaint is given, run the full checklist.

**Output.** Proposed revision(s) in chat, presented **against the original** — never applied to the manuscript directly.

> **Write revisions in the project's output language.**

---

## Core principle

> **Surgical, not sweeping. The author's words survive wherever they can.**

The failure mode of revision passes is rewriting everything — replacing the author's 70%-good passage with the machine's 100%-different one. That is theft dressed as help.

The rule: **every word of the original that can stay, stays.** The revision touches what is broken and leaves fingerprints nowhere else.

---

## Execution protocol

### Step 1 — Load context

Same load as `draft-scene`, scoped to the passage:

1. `.project/config/project.yaml` — output language
2. `.project/config/persona.md` — voice, signatures, ceilings, model passages
3. `.project/templates/framework.md` — the 14 categories
4. `.project/reports/preserve-list.md` — if the passage contains a thesis phrase, it is untouchable
5. `.project/reports/recurrences.md` — the revision must not introduce a blocked phrase
6. Character sheets for anyone speaking in the passage
7. `.project/knowledge/worldbuilding.md` — guards, if the passage touches rules
8. Surrounding text — at least the paragraph before and after, for seam quality

### Step 2 — Diagnose before cutting

State what is actually wrong, in one or two lines, before proposing anything:

- If the author named the complaint → verify it and check for adjacent issues they didn't name
- If not → run the 14 categories on the passage and identify the dominant problems

**If the passage is fine, say so.** "This doesn't need revision; what bothered you?" is a legitimate and valuable answer. Do not invent problems to justify the invocation.

### Step 3 — Revise minimally

- Fix the diagnosed problems. Nothing else.
- Preserve the author's sentences wherever they work — recombine before replacing.
- Respect preserve-list phrases absolutely.
- Check the revision itself against the density budgets (a fix that introduces a new tic is not a fix).
- Mind the seams: the revised passage must sit naturally against what precedes and follows.

### Step 4 — Present as comparison

Always show:

```markdown
**Original:**
> {original passage}

**Diagnosis:** {what is wrong, in one or two lines}

**Revision:**
> {proposed text}

**What changed and why:**
- {change} → {reason, tied to the diagnosis}

**What I deliberately kept:** {the author's phrases that survived and why}
```

For high-stakes passages (chapter openings/endings, pivotal beats), offer **two alternatives** with different trade-offs rather than one authoritative answer.

### Step 5 — Iterate

The author may take the revision whole, take pieces, or counter-propose. Their counter-proposal wins and — as always — becomes voice data worth recording.

---

## What to avoid

**Total rewrite.** If more than ~60% of the passage needs replacing, the problem is upstream — scene design, not sentences. Say so and hand off to `restructure-chapter`, which diagnoses at scene level, instead of pretending sentence surgery will fix a structural wound.

**Style upgrade drift.** The job is fixing the diagnosed problem in the author's voice — not making the passage "better" by the machine's taste.

**Fixing what was declared.** Persona signatures and preserve-list phrases are not problems. Flagging them wastes the author's trust.

**Invisible changes.** Every alteration is listed and justified. No silent touch-ups.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `draft-scene` | Sibling — same context, blank page vs. existing text |
| `analyze-chapter` | Its findings often feed passages here |
| `review-revision` | Evaluates the author's own revisions; this one proposes revisions |
| `restructure-chapter` | Downstream escape hatch when the problem is scene design, not sentences |
