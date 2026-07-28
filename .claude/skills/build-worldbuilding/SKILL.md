---
name: build-worldbuilding
description: Builds or updates .project/knowledge/worldbuilding.md as a consistency contract — rules with costs and knowledge distribution, plus the deliberately-unexplained list that protects the book's mysteries. Extract mode pulls rules from an existing manuscript; create mode co-builds through dialogue. Use when the user asks to build the worldbuilding, extract world rules, or define the world.
---

# Skill: build-worldbuilding

**What it does.** Builds or updates `.project/knowledge/worldbuilding.md` — the consistency contract of the fictional world. Works in two modes: **extract** (pull rules from an existing manuscript) or **create** (co-build from scratch through dialogue).

**Triggers**
- "build the worldbuilding"
- "/build-worldbuilding"
- "extract the world rules from the manuscript"
- "let's define the world"
- Equivalent phrasing in the project's output language

**Input.** Mode: `extract` (default when a manuscript exists) or `create`.

**Output.** `.project/knowledge/worldbuilding.md` created or updated.

> **Write the document in the project's output language** (`config/project.yaml → language`).

---

## Core principle

> **This file is a consistency contract, not an encyclopaedia.**

The inclusion test for anything: *would contradicting this break a reader's trust?*

If yes, record it. If no, leave it out.

A worldbuilding file that documents the pantheon, the currency, and four centuries of dynastic history — none of which appears on the page — is a hobby, not a tool. It costs context to load and buys nothing.

What earns its place:
- Rules that **constrain what can happen**
- Facts the text has **already committed to**
- Mysteries deliberately left open, so nobody explains them by accident

---

## The three things every rule needs

A rule without these is decoration:

1. **What it makes possible** — the capability or phenomenon
2. **What it costs** — the price, limit, or side effect
3. **Who knows it** — characters' awareness is itself a rule

> Weak: *"Memory can be erased."*
> Strong: *"Erasure is progressive and physical — it removes structures, not only memories. Cost: nobody notices, because the memory of the erased thing goes with it. Known by: nobody in-world; the merchant suspects."*

The second version constrains scenes. The first does not.

---

## Protocol: extract mode

Use when a manuscript already exists, in whole or in part.

### Step 1 — Load context

1. `.project/config/project.yaml` — output language
2. `.project/knowledge/worldbuilding.md` — current state, if any
3. `.project/knowledge/glossary.md` and `timeline.md` — avoid duplicating what belongs there
4. The manuscript, in scope

### Step 2 — Read the manuscript

Read for **commitments**, not for plot. Every time the text asserts something about how the world works, that is a commitment the rest of the book must honour.

Collect:
- Explicit rule statements (a character explains something)
- Implicit rules (something happens that implies a mechanism)
- Physical facts (geography, distances, seasons, materials)
- Social facts (who has power, what is forbidden, how people earn)
- Limits demonstrated (someone tries something and fails)

### Step 3 — Separate established from assumed

Two categories, and the distinction matters:

- **Established** — stated or demonstrated on the page. Binding.
- **Assumed** — implied but never confirmed. Still changeable.

Mark them differently. The author can revise an assumption freely; revising an establishment means editing the manuscript.

### Step 4 — Detect contradictions

While reading, flag anything that conflicts:
- Two chapters stating incompatible rules
- A demonstrated limit later ignored
- Distances, timings, or quantities that do not reconcile

Log each in the contradictions table with chapter references. **Do not resolve them silently** — present them to the author.

### Step 5 — Identify the deliberate gaps

Some things are unexplained on purpose. Extract them explicitly so no future skill fills them in.

Signal to look for: the text circles something repeatedly without ever defining it. That is usually intentional.

Ask the author to confirm: *"The text never explains X. Deliberate mystery, or an unresolved gap?"*

### Step 6 — Write and present

Fill `worldbuilding.md`. Then report:
- How many rules extracted (established vs. assumed)
- Contradictions found
- Deliberate gaps identified
- Open questions needing the author's decision

---

## Protocol: create mode

Use when starting a new book, or when the world is still forming.

### Step 1 — Start from the premise

One sentence: **what is different from our world?**

Not a paragraph. One sentence. If it takes more, the premise is not yet clear enough to write from.

Then, before anything else, three questions:
- What does this make possible that was not possible before?
- What does it cost?
- Who knows it, and who is wrong about it?

### Step 2 — Build outward from constraint, not from lore

The interview follows what the story needs, in this order:

**a) The rule and its price.** Every capability gets a cost. No exceptions.

**b) What breaks.** *"If this is true, what stops working in a normal world? What institution, habit, or relationship changes shape?"* This is where worlds get interesting.

**c) The limit.** *"What is the boundary? What happens at the edge?"* A rule without an edge cannot generate tension.

**d) Distribution of knowledge.** *"Who knows this rule? Who is wrong about it? Who profits from the confusion?"*

**e) What stays mysterious.** *"What do you want the reader to feel but never have explained?"* Record it as a protected gap.

**f) The physical layer.** Geography, climate, materials — **only** as far as the story touches. Ask: *"Does a scene depend on this?"* If no, skip it.

### Step 3 — Pressure-test

For each rule, ask:
- **Does it constrain a scene?** If it never limits anything, cut it.
- **Is it contradicted by anything already written?**
- **Does it explain too much?** Some rules kill mystery by existing.

### Step 4 — Write and validate

Fill `worldbuilding.md`. Present it and ask: *"What is wrong? What is missing that a scene will need?"*

---

## What to avoid

**Encyclopaedia mode.** Building the world for its own pleasure. Symptom: sections nothing in the manuscript touches.

**Rules without costs.** A capability with no price generates no drama and no constraint.

**Explaining the mystery.** If the book works because something is unexplained, documenting the explanation is a liability — some future generation pass will leak it.

**Duplicating other files.** Terms belong in `glossary.md`. Chronology belongs in `timeline.md`. Character-specific facts belong in `characters/`. Keep each file doing one job.

**Silent resolution.** When two chapters contradict each other, that is an author decision, not a documentation decision. Present, do not choose.

---

## Relationship to other skills

| Skill | How it uses worldbuilding |
|---|---|
| `check-consistency` | Primary source of truth. Compares chapters against the rules |
| `create-character` | Characters exist inside these constraints |
| `draft-scene` | Loads relevant rules so generated prose does not violate them |
| `outline-chapter` | Uses limits to know what a scene can and cannot resolve |

---

## Maintenance

Worldbuilding is not written once.

- **After each Act:** re-run in `extract` mode. New chapters create new commitments.
- **When a contradiction is found:** log it, resolve with the author, record the resolution.
- **When an assumption becomes established:** promote it, and note the chapter that fixed it.

The contradictions table is the most valuable part of the file over time. It is the record of where the world nearly broke.
