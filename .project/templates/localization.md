# Localization

How a **target-language edition** is laid out, decided, and kept honest. This is the single resolver for the localization subsystem: `define-localization`, `translate-chapter` and `review-translation` follow it rather than improvising.

The subsystem is **additive**. It modifies no existing skill and no existing `.project/` file. Deleting `translations/` returns the project to its previous state exactly.

---

## Language is not locale

A book's prose language and its setting are independent, and in practice they diverge. A book written in `pt-BR` and set in the United States has an American setting on page one, in Portuguese.

Four fields, not two:

| Field | Meaning |
| --- | --- |
| `prose_language` | the language the manuscript is written in — `project.yaml → language` |
| `setting_locale` | where the book takes place |
| `target_prose_language` | the language of this edition |
| `setting_locale`, target edition | **identical to the source. Always.** |

### The setting never moves

> A French edition of a book set in the United States keeps the county, the federal agents, the carbine, the sycamore. It says *comté*, *platane d'Occident*. It does not relocate the town to France.

Translation changes the language, never the map. Every target edition inherits this rule and no contract may override it.

---

## The two kinds of regional item

They look alike and behave differently. Separating them is what makes a second target language cheap.

**Leak** — culture of the *prose language* that entered a text set somewhere else. A Brazilian television format, a Brazilian tree species, a Brazilian school-system term, in a book set in the US. These are defects of the source against its own setting: target-independent, and worth fixing **in the source language too**.

**Referent** — how a thing that genuinely belongs to the setting is said in the target language. One column per target.

Leaks are listed once. Referents get a column per target edition.

---

## Layout

```text
translations/
├── en-US/
│   ├── localization.md      the crossing contract
│   ├── lexicon.md           locked pairs
│   ├── referents.md         the target column of the setting's referents
│   ├── status.md            per-chapter state
│   └── manuscript/
│       ├── 01.01/
│       │   ├── 01.01.md
│       │   └── 01.01_report.md
│       └── 01.02/
│           └── ...
└── fr-FR/
    └── (same shape)
```

The directory name is a **BCP 47 tag** — `en-US`, `fr-FR`, `pt-PT`. Region included even when it feels redundant: `en-US` and `en-GB` take different verdicts on punctuation, spelling and idiom, and a bare `en` cannot say which.

`manuscript/` inside a target folder **mirrors `paths.layout`** — `flat` or `chapter`, whichever the project declares. `templates/layout.md` resolves it unchanged: same ids, same ordering, same satellite rules. There is no second resolver, and no per-target layout.

The chapter file keeps the source id. `01.01.md` in `translations/fr-FR/manuscript/01.01/` is chapter `01.01`, in French. Ids are the primary key of the whole system and translation does not get to renumber.

---

## The crossing contract — `localization.md`

Written once per target language by `define-localization`, before a single line is translated. It is to translation what `persona.md` is to drafting: the translation consults it and decides nothing on its own.

### The three verdicts

Every rule in `style-guide.md` and every signature in `persona.md` gets exactly one:

| Verdict | Meaning | Required alongside |
| --- | --- | --- |
| **crosses intact** | the same device works in the target language | nothing |
| **crosses with another tool** | same effect, different mechanism | the substitute, named |
| **does not cross** | unavailable, or an error, in the target | a declared replacement — or retirement with the ceiling set to zero |

**There is no fourth outcome.** A rule left unclassified is not a gap to fill later: `translate-chapter` refuses to run against an incomplete contract, for the same reason `layout.md` refuses a mixed manuscript. A missing verdict does not raise an error — it silently produces prose the author has no basis to evaluate.

### Why "does not cross" is common, and not a failure

Devices bind to grammar. Three that recur:

- **Subject elision.** Portuguese, Spanish and Italian drop the subject and let the conjugation carry it. English, French and German cannot. Any rule whose *tool* is the null subject — most often a cap on how often characters are named — loses its tool on crossing and needs a declared replacement: an action beat, an identifying gesture, a reordered line.
- **The comma splice.** A stylistic tic with a ceiling in Portuguese; a grammatical error in English and French. Its ceiling goes to zero and the rule retires. This usually costs nothing: it is a drafting artefact in most personas, not a signature.
- **Dialogue marking.** The dash is standard in pt-BR and fr-FR, quotation marks in en-US, guillemets in fr-FR for quoted speech. The same mark takes opposite verdicts across two targets — which is exactly why the contract is per language and there is no global one.

### The other four sections

**Typographic profile.** Dialogue marking, punctuation inside or outside quotes, thousands separator, decimal mark, date format, dash spacing, the marking of any in-world register the book uses (italics for radio, brackets for documents).

**Target-language tic watchlist.** `framework.md`'s 14 categories are calibrated for the *prose* language. The target language has its own AI markers, and they are not the same list. English: *delve*, *tapestry*, *it's not X, it's Y*, the trailing self-correction, triads, *a testament to*. `review-translation` runs against this watchlist, not against `framework.md`.

⚠️ **The collision this section exists to catch.** A genuine authorial signature can coincide exactly with a target-language AI tic — a three-beat escalation is a signature in one book and the single most-flagged English AI marker. Both facts are true. The watchlist records the collision so the signature is pre-registered and not flagged every chapter.

**AI declaration for this edition.** The target edition does **not** inherit the source declaration. A generated translation is entirely generated sentences; a source declaration reading "no generated sentence enters the manuscript" is false of it. This is the text that goes on the edition's title page and into its `review-book`.

**Native-reader gate.** Whether a native reader of the target language must clear a chapter before submission, and what that clearance covers. Required whenever the author cannot judge literary prose in the target language. Recorded here as policy, tracked per chapter in `status.md`.

---

## The locked lexicon — `lexicon.md`

Terms, designations and preserved phrases, each with **one** target form, decided once and reused at every occurrence.

Three groups, and all three are mandatory before translation begins:

1. **Thesis vocabulary** — the words carrying what the book is about. Each entry needs its target form **and its prohibitions**: the plausible translations that would betray the book. The prohibition is half the value; without it the prose drifts into the wrong register by the third page.
2. **Designations** — names, titles, epithets. Whatever a character is called, they are called that consistently in the target edition.
3. **Preserved phrases** — every entry in `reports/preserve-list.md` gets a canonical target rendering. This is what keeps a motif a motif: without a locked pair, one recurring line becomes five different lines and the book's stitching comes apart.

### Entry format

```markdown
- **{source term}** — {target}: **{form}** · ⚠️ never: {prohibited}, {prohibited} · {note}
```

### Two hard rules

**Open entries block.** A term whose target form is `[?]` stops `translate-chapter` on any chapter containing it. The skill does not choose, does not propose a provisional, does not proceed with a note. Designations and thesis terms appear in every chapter — the cost of getting one wrong is the whole edition, discovered late.

**The lexicon is validated against the source.** Every source term listed here must still exist in `knowledge/glossary.md`. A mismatch refuses the run and names the term. This is what catches the day a term is renamed in the source and the target edition keeps translating a word the book no longer uses.

---

## Referents — `referents.md`

The setting's objects, institutions, measures and cultural products, in the target language. Inherits the leak/referent split above.

```markdown
- **{item}** — `{chapter}` · source: {as written} · {target}: {form} · {note}
```

### Measurements are curation, never arithmetic

When a narrator's precision is part of the voice, a computed conversion destroys it. `25 metros → 82.02 feet` is arithmetically correct and characterologically wrong; `80 feet` is the number a person would actually say. The decision is *which number reads as measured in the target system*, item by item, and it is taken by hand.

Skills consult this file. **No skill converts a measurement.**

Universal quantities — probabilities, percentages, milliseconds, counts — are never converted at all. Where the arithmetic of a scene depends on them, changing one breaks the scene silently.

---

## Chapter state — `status.md`

One row per translated chapter.

| Column | Meaning |
| --- | --- |
| `chapter` | the source id |
| `source_commit` | the commit of the source chapter this translation was made from |
| `stage` | `translated` · `reviewed` · `native-cleared` |
| `native_gate` | who cleared it, when — or `pending` |

### Drift

`source_commit` makes staleness exact:

```sh
git log <source_commit>..HEAD -- <source chapter path>
```

Empty output means the translation is current. Any output names precisely what changed since. No heuristics, no timestamps, no diffing two languages against each other.

⚠️ **Do not attempt a line-level diff between editions.** Under transcreation the target edition legitimately reorders, merges and rebuilds sentences. An alignment that "works" on a descriptive chapter fails on the chapter that most needed restructuring, and reports a clean state for the worst case.

---

## Eligibility

A chapter is eligible for translation when it has been **revised in the source language**.

Translating a draft chapter is paid for twice: a later `restructure-chapter` invalidates the translation wholesale, because transcreation has no partial update. `translate-chapter` warns and asks for confirmation rather than refusing — a pilot translation to calibrate the contract is a legitimate reason to override, and the first one usually is.

---

## What the localization skills never do

- **Commit.** Same rule that binds every other skill. They may suggest a commit line.
- **Write into `manuscript/`.** The source manuscript is never touched by a translation run, in either direction.
- **Modify `.project/`.** Findings about the source — a leak worth fixing in Portuguese, an uncatalogued referent, a glossary term that drifted — are *reported*, and the author rules.
- **Convert a measurement.**
- **Move the setting.**
