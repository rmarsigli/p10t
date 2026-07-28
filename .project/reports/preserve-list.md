# Preserve List — Phrases That Must Never Be Flagged

_Version 0 — to fill_

> **Write entries in the project's output language** (the phrases are quotes from the manuscript).

Phrases carrying narrative or thematic weight that must **not** be marked as tics, even when they structurally resemble one (antithesis, triad, single-line, aphorism).

Maintained manually by the author. Add an entry every time you decide "this phrase is mine".

---

## How it works

The `analyze-chapter` skill reads this file before generating any analysis. Phrases listed here arrive marked **(PRESERVE — thesis)** in the report, and appear in the verdict under "Keep intact" — never under a cut suggestion.

Without this file, the system would suggest cutting the mantra that holds a character together, simply because it repeats.

---

## Entry format

```markdown
- **"{literal phrase}"** — {chapter}. {Brief justification of its weight.}
```

---

## Central thesis

{Phrases stating what the book is about.}

_(to fill)_

---

## Character mottos

{Lines belonging to a specific character, often repeated by design.}

### {Character}
_(to fill)_

---

## Recurring images

{Phrases returning deliberately to stitch the book together.}

_(to fill)_

---

## Pivotal lines

{Single moments that turn the book. Usually untouchable regardless of form.}

_(to fill)_

---

## Worked example

```markdown
## Character mottos

### The warrior
- **"Eu fico."** — recurring from 02.04 onward. The last phrase left before his collapse; the whole arc compresses into it.
- **"Ela existe."** — recurring. First of the five morning-ritual phrases. Repetition is the ritual; cutting it destroys the character.

## Recurring images
- **"Roxo cheira fundo."** — 02.02, echoed in 03.04, 04.01, 04.05. Central sensory thesis; the phrase that survives the erasure.
```

---

## How to update

When the author annotates **R: this is my thesis** or **R: preserve — narrative weight** in an analysis file, move the phrase here under the appropriate heading.

When a listed phrase is later cut or replaced during revision, remove it (leave a dated comment).

The `update-preserve-list` skill (roadmap) will automate this migration.
