# Recurrences — Cross-Chapter Duplication Map

_Version 0 — no sweep run yet_
_Last sweep: —_

> **Write entries in the project's output language** (the phrases are quotes from the manuscript).

Phrases and structures appearing in multiple chapters. Maintained by the `scan-recurrences` skill or by hand.

The `analyze-chapter` skill reads this file to mark occurrences as **(RECURRENCE — also in ch. X, Y)**, flagging them as high-priority cuts.

---

## Why this file matters

**Literal cross-chapter duplication is the most damaging AI marker**, because it has no stylistic defence. A human author may have tics; they rarely repeat the same striking sentence three times without noticing.

Chapter-by-chapter analysis cannot see this. Only a global sweep can.

---

## Entry format

```markdown
### "{phrase}"
Appears in:
- {ch}: {brief context}
- {ch}: {brief context}
**Decision:** keep {ch}. Cut {chs}. {Justification}
**Status:** {pending | ✓ resolved on DD/MM}
```

---

## Literal duplications (cut down to one)

_Type A — the same sentence, or 80%+ identical, in two or more chapters._

_(to fill)_

---

## Recurring formulas (watch density)

_Type B — not the same sentence, but the same syntactic mould repeated._

_(to fill)_

---

## Recycled images

_Type C — the same metaphor in different contexts._

_(to fill)_

---

## Repeated character aphorisms

_Type D — a character restating the same thing without diegetic reason._

_(to fill)_

---

## Intentional recurrences (PRESERVE)

_Motifs that stitch the book together. Never cut. Cross-referenced with `preserve-list.md`._

_(to fill)_

---

## Grey zone (author decision pending)

_Repetitions that could be deliberate but are not clearly so._

```markdown
### "{phrase}"
Appears in: {chs}
**Question:** deliberate echo or duplication?
```

_(to fill)_

---

## Worked example

```markdown
## Literal duplications

### "Isso não me faz querer ir embora. Me faz querer ficar mais."
Appears in:
- 02.02: chapter closing
- 02.03: notebook entry closing
**Decision:** keep 02.03 — it lands harder after the village rejects him. Rewrite 02.02.
**Status:** pending
```
