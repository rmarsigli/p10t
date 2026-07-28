---
name: expand-beat
description: Turns a one-line beat or rough fragment into drafted prose — adding texture, interiority, and gesture without inventing plot beyond the beat. The author's fragments are load-bearing. Use when the user asks to expand a beat, turn a note into a scene, or develop a fragment.
---

# Skill: expand-beat

**What it does.** Turns a one-line beat ("the girl realizes he knows") or a rough fragment into drafted prose. The lightweight sibling of `draft-scene` — for when the author has a seed but not a full scene contract.

**Triggers**
- "expand this beat: {...}"
- "/expand-beat"
- "turn this note into a scene"
- "I have this fragment, develop it"
- Equivalent phrasing in the project's output language

**Input.** The beat or fragment, plus (asked if missing): who is on stage, where it sits in the chapter, target length.

**Output.** Drafted passage in a `_draft` block or file, marked for curation. **Never written into the manuscript.**

> **Write the prose in the project's output language.**

---

## Core principle

> **The beat is the author's plot decision. Expansion adds texture, not events.**

The line between expanding and inventing:

- Beat: *"the merchant admits he sent the letter"* → the expansion may add hesitation, gesture, the room, the pause before the admission — **but not** a second revelation, a new character arriving, or a consequence the beat doesn't contain.

If the expansion needs a plot decision the beat doesn't carry ("does she believe him?"), **stop and ask**. One question at the boundary beats a paragraph of invented plot.

---

## Execution protocol

### Step 1 — Load context

Lighter than `draft-scene`, but never zero:

1. `.project/config/project.yaml` — output language
2. `.project/config/persona.md` — voice, ceilings, model passages
3. Character sheets for whoever is on stage — Voice sections
4. `.project/knowledge/worldbuilding.md` — protection list (even a small expansion can leak a mystery)
5. `.project/reports/recurrences.md` — blocklist
6. Surrounding text, if the beat sits inside an existing chapter

### Step 2 — Establish the frame

If not provided, ask (briefly, once): who is present, where this lands in the chapter, and the target length. Three answers, then work.

### Step 3 — Expand

- Stay inside the beat's plot content. Texture, interiority, gesture, setting — yes. New events — no.
- If the input is a fragment of the author's prose, **their sentences are load-bearing**: build around them, never replace them.
- Respect density budgets and the self-audit discipline from `draft-scene` (run the 14 categories mentally before delivering).
- Match the register of the surrounding text if it exists.

### Step 4 — Deliver marked

Present with the same honesty as `draft-scene`, scaled down:

```markdown
**Expanded from:** "{the beat}"
**Choices to review:** {interpretive calls made}
**Stopped at:** {plot boundaries hit, questions not answered}
```

---

## What to avoid

**Plot smuggling.** Adding events under cover of expansion. The single defining failure of this skill.

**Drowning the fragment.** When the author gives prose, the ratio matters: expansion should feel like their fragment grew, not like it was swallowed.

**Skipping context because it's "just a beat".** A three-line expansion in the wrong character voice costs more trust than it saves time.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `draft-scene` | Heavyweight sibling — full contract, full load |
| `outline-chapter` | Beats often come from its scene lists |
| `revise-passage` | Downstream: expanded prose gets revised like any other |
