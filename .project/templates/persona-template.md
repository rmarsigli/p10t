# Template — persona.md

Skeleton for the author's voice document. Reusable across books.

Every claim must be anchored in a **literal quote** from the author's text. A persona full of abstract adjectives is useless for generation; one full of real examples is gold.

> **Write the persona in the project's output language** — its examples are quotes from the author's own prose.

---

```markdown
# Persona — {Author name}

_Version {N} — {date}_
_Base corpus: {which texts were analyzed}_

> Items marked **[HYPOTHESIS]** await confirmation.
> Items marked **[CONFIRMED]** come from an explicit author statement.

---

## 1. Register and vocabulary

### Register level
{Elevated? Colloquial? Mixed? In what proportion, and when does it shift?}

**Example:**
> {quote}

### Preferred vocabulary (preserve)
- {word or type} — {why, with example}

### Rejected vocabulary
- {word} → {author's preferred substitution}

### Slang and regionalism
{Allowed? Which register?}

### Profanity
{Yes / no / sparingly. In what context.}

---

## 2. Syntax and rhythm

### Sentence length
{Typical pattern. When and why it varies.}

**Short example:**
> {quote}

**Long example:**
> {quote}

### Paragraph
{Dense or airy? Average sentence count?}

### Fragments
{Uses verbless sentences? To what end?}

### Characteristic punctuation
{Em-dash, colon, ellipsis, parentheses.}

---

## 3. Personal signatures (PRESERVE)

Constructions the author recognizes as their own. `analyze-chapter` must **not** flag these as tics.

- **{construction}** — {literal example}. {Acceptable frequency.}

---

## 4. Signatures to watch

Legitimate constructions that become tics at high density.

- **{construction}** — suggested ceiling: {N} per chapter.

---

## 5. Tone

### Irony
{How much? What kind? Aimed at what?}

**Example:**
> {quote}

### Emotion
{Shown or named? How is pain, loss, tenderness handled?}

### Humour
{Dry? Absurd? Physical? Self-deprecating?}

**Example:**
> {quote}

### What it avoids
{Sentimentality? Grandiloquence? Cheap cynicism?}

---

## 6. Narrative craft

### Description
{Dense or economical? Sensory or conceptual?}

### Dialogue
{Naturalistic or stylized? How is character voice marked?}

### Emotion: show vs. name
{Declared preference.}

### Chapter endings
{Hook? Aphorism? Gesture? Varies?}

---

## 7. Anti-persona (what NOT to sound like)

- {vice to avoid} — {why}

---

## 8. Model passages

Excerpts of the author's own writing at its best. `draft-scene` uses these as primary tonal reference.

### {Passage name} — {location}
> {1-3 paragraph quote}

**Why it is a model:** {what this passage gets right}

---

## 9. Anti-models

Excerpts of the author's own writing with high tic density.

### {Passage name} — {location}
**Problem:** {what is wrong}

---

## 10. Notes specific to this book

{Voice decisions that apply only to this project, not to the author in general.}

---

## Open questions

{Items needing an author decision before the next version.}

---

## Changelog

- **v{N}** ({date}) — {what changed and why}
```

---

## Filling notes

**Sections 8 and 9 matter most** for generation. A model and an anti-model teach more than any abstract description.

**Separate author from narrator.** If a signature belongs to this book's narrator rather than the author in general, record it in section 10.

**Always version.** Voice evolves. The changelog matters.

**Never hand over a blank form.** The `define-persona` skill fills it with hypotheses extracted from the corpus and the author corrects. An empty questionnaire wastes the author's time.
