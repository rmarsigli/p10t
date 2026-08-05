---
name: create-character
description: Builds or updates a character sheet in .project/knowledge/characters/ — voice-first (verbatim sample lines), consistency rules, and the want/need/fear/lie engine. Extract mode pulls the character from an existing manuscript and detects voice drift; create mode develops a new character through dialogue. Use when the user asks to create, develop, extract, or update a character.
---

# Skill: create-character

**What it does.** Builds or updates a character sheet in `.project/knowledge/characters/{name}.md`. Two modes: **extract** (pull a character from an existing manuscript) or **create** (develop a new character through dialogue).

**Triggers**
- "create a character"
- "/create-character {name}"
- "extract {character} from the manuscript"
- "let's develop {character}"
- "update {character}'s sheet"
- Equivalent phrasing in the project's output language

**Input.** Character name or designation; mode (`extract` | `create`), inferred from whether the character exists in the manuscript.

**Output.** `.project/knowledge/characters/{name}.md`, following `.project/templates/character.md`.

> **Write the sheet in the project's output language.**

---

## Core principle

> **A character sheet exists to keep the character writable, not to biograph them.**

The test for every field: *does this help write the next scene consistently?*

Childhood backstory that never pressures a scene is lore. The way a character dodges questions about their past — that is craft material. Record the second, skip the first unless it feeds it.

---

## The hierarchy of what matters

Not all sections are equal. In order of daily usefulness:

1. **Voice** — how they sound. The single most-consulted section during drafting.
2. **Consistency rules** — facts that must hold. What `check-consistency` reads.
3. **Want / Need / Fear / Lie** — the engine. What makes scenes possible.
4. **Arc** — where they start, turn, land.
5. Everything else — supporting material.

A sheet with only sections 1–3 filled is functional. A sheet with everything *but* those filled is useless.

---

## Protocol: extract mode

Use when the character already exists on the page.

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. `.project/templates/character.md` — skeleton
3. `.project/knowledge/worldbuilding.md` — the constraints they live inside
4. `.project/reports/preserve-list.md` — signature lines may already be listed there
5. Existing sheet, if updating

### Step 2 — Sweep the manuscript

Resolve the chapter list via `.project/templates/layout.md`, then read every scene the character appears in. Collect:

**For Voice:**
- Every line of dialogue they speak — verbatim
- Words only they use; words they never use
- Sentence length, rhythm, hesitations
- How their speech differs when talking to different characters

**For Consistency rules:**
- Physical facts stated (scars, height, age markers)
- Established history (what the text has committed to)
- Behavioural invariants (things they always/never do)
- Knowledge state: what they know, when they learned it, what they still don't know

**For the engine:**
- What they pursue on the page (want)
- What the narrative suggests they actually need
- What they avoid, flinch from, refuse to discuss (fear, lie)

**For Arc:**
- Their state at first appearance vs. latest appearance
- The scene(s) where something shifted

### Step 3 — Distinguish shown from inferred

Like worldbuilding's established/assumed split:

- **SHOWN** — on the page. Binding.
- **INFERRED** — your reading between the lines. Plausible, but the author may see it differently.

Mark inferences explicitly. When presenting, ask the author to confirm or correct each one — **the inferences are where the conversation gets valuable**, because sometimes the author didn't realize what the text implies.

### Step 4 — Detect drift

Voice drift is the most common character bug in long manuscripts: the terse character who starts giving speeches in Act 3, the formal one who drifts colloquial.

Compare early dialogue against late dialogue. If the shift is unexplained by the arc, flag it:
> "In 01.02 the innkeeper never exceeds three words. In 04.01 he has a 30-word line. Intentional (his barriers dropping) or drift?"

### Step 5 — Write and present

Fill the sheet. Report: what is SHOWN vs. INFERRED, drift flags, signature-line candidates for `preserve-list.md`, and open questions.

---

## Protocol: create mode

Use for characters who do not yet exist on the page.

### Step 1 — Function before person

First question: **what does the story need this character to do?**

Not "who are they" — that comes after. A character built without a narrative function becomes a beloved biography that never fits a scene.

- What role: protagonist, antagonist, catalyst, mirror, chorus?
- What scene *cannot happen* without them?
- Who do they pressure, and how?

### Step 2 — The engine

Build the four-part core, in dialogue with the author:

- **Want** — the conscious desire. What they'd say they're after.
- **Need** — the real lack, usually invisible to them. Often opposed to the want.
- **Fear** — what drives avoidance.
- **Lie** — what they tell themselves to keep going.

Push against easy symmetry. "Wants revenge / needs forgiveness" is a template, not a person. Ask the author: *"what's the version of this that would embarrass them if said aloud?"* — shame is more specific than desire.

### Step 3 — Voice before face

Most sheets over-invest in appearance and under-invest in sound. Reverse it.

Before any physical description, draft **three sample lines** with the author:
1. The character saying something ordinary (asking for food, greeting someone)
2. The character under pressure
3. The character talking about the thing they lie about

If the three lines could belong to any character in the book, the voice isn't found yet. Iterate.

Then extract the rules from the samples: register, rhythm, vocabulary, what they never say.

### Step 4 — Place them in the world

Cross-check `worldbuilding.md`:
- Which rules of the world do they know? Believe wrongly?
- What has the world cost them, specifically?
- Where do they sit in the social layer?

A character unmarked by the world's rules reads as imported from another book.

### Step 5 — Relationships as vectors

For each existing character they'll interact with: not "they are friends" but **what each wants from the other and doesn't get**. Flat relationship descriptions produce flat scenes; vectors produce friction.

### Step 6 — Consistency rules and traps

End by writing the two forward-looking sections:
- **Consistency rules** — the facts now locked
- **Writing notes** — the traps. Every character has a failure mode (the terse one becomes a gimmick, the wise one becomes a fortune cookie). Name it now.

### Step 7 — Validate

Present the sheet. Then run the test: draft one short sample exchange between this character and an existing one. If the author says "that's them", the sheet works. If not, the gap between sheet and instinct is the next conversation.

---

## What to avoid

**Biography mode.** Life history that never pressures a scene. The sheet is a writing tool, not a wiki page.

**Trait lists.** "Brave, loyal, stubborn" describes nobody. A trait only exists in the sheet if attached to a behaviour: *"stubborn — will re-ask a question three times rather than accept a deflection."*

**Voice by adjective.** "Speaks curtly" is weaker than one verbatim curt line. Quotes over descriptions, always.

**Premature physical detail.** Appearance is the least binding layer and the easiest to add later. Voice and engine first.

**Filling every field.** A chorus character needs Voice and Consistency rules. Padding the rest dilutes the useful parts.

**Overwriting author instinct.** In create mode, the skill structures the author's character — it does not invent one and hand it over. Propose, ask, iterate.

---

## Relationship to other skills

| Skill | How it uses character sheets |
|---|---|
| `draft-scene` | Loads the sheets of everyone in the scene — Voice and engine especially |
| `check-consistency` | Compares chapters against Consistency rules |
| `check-arc` | Reads Arc sections across the cast |
| `build-worldbuilding` | Characters' knowledge states are part of the world's rule distribution |

---

## Maintenance

- **After each Act:** re-run extract on main characters. New scenes create new commitments — and new drift risks.
- **When a signature line emerges:** add it to the sheet *and* propose it for `preserve-list.md`.
- **When the author corrects generated dialogue** ("she wouldn't say that"): that correction is voice data. Record what was wrong and why in Writing notes.
