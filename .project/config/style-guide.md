# Style Guide — {Book title}

_Version 0 — to fill_

**Hard rules** for this project. Unlike `persona.md`, which *describes* how you write, this file *prescribes* what holds in this specific book.

> **Write this file in the project's output language.**

---

## Important distinction

| File | Nature | Example |
|---|---|---|
| `persona.md` | Descriptive — how you write | "I use elevated vocabulary and like a self-correcting tag at sentence end" |
| `style-guide.md` | Prescriptive — rules for this book | "In this book, no character has a proper name except two" |

---

## Structural decisions

{Choices that hold across the whole book and cannot be violated without breaking the project.}

- {decision} — {reason}

**Example:**
> - No character has a proper name, except two. Reason: the erasure consumes names; the absence of names is the thesis made form.

---

## Formatting conventions

- **Dialogue:** {em-dash? quotation marks? which national standard?}
- **Thought:** {italics? unmarked?}
- **In-world documents** (letter, diary, inscription): {how to mark}
- **Scene break:** {`***`? blank line? asterisks?}
- **Chapter numbering:** {file naming format}

---

## Vocabulary rules

### Forbidden in this book
{Words or registers that break the setting.}

- {word} — {why}

**Example:**
> - No modern technical terms. Pre-industrial setting.

### Required
{Terms to be used consistently.}

---

## World rules affecting the prose

{Diegetic constraints limiting what can be written.}

**Example:**
> - The narrator cannot describe colours the blind character does not know, unless someone described them earlier in the narrative.

---

## Density ceilings

Overrides for `templates/framework.md`. Density is measured in **occurrences per 1,000 words**; categories 8, 9, and 13 carry their own units.

**Precedence:** a construction declared in `persona.md → Personal signatures` has no ceiling at all — it is not a tic. Below that, this file overrides the framework defaults. List only what you are changing; everything unlisted uses the default.

```markdown
- **cat. {N} ({name}):** {N,N}/1k — overrides the default of {N,N}/1k. {Reason.}
```

**Example:**
> - **cat. 1 (binary antithesis):** 3,5/1k — overrides the default of 2,0/1k. At turning points this is a signature (`persona.md` §3); the raised ceiling covers its use elsewhere.
> - **cat. 11 (em-dash):** 0,5/1k — stricter than the 2,0/1k default. This book uses the dash only to open dialogue; a narrative dash is an error, not a density problem.
> - **Total:** 6,0/1k — stricter than the 8,0/1k default in `project.yaml`.

**Language adaptation.** If the manuscript is not in `[pt-BR]` or `[en]`, record here how the framework's detection signals were adapted — otherwise analyses stop being comparable across chapters.

_(to fill)_

---

## Quality target

{How you define "done" for this project.}

**Example:**
> - No framework category above its ceiling after revision; chapter total under 8,0/1k.
> - Zero literal cross-chapter duplications.
> - Every revised chapter passed `review-revision` with an approving verdict.

---

## AI use declaration

{This project's position, for editorial submission.}

**Example:**
> LLM assistance used for prose generation, with human curation item by item. Structure, concept, dramatic decisions, and final revision are authorial. Transparent declaration in the submission letter.
