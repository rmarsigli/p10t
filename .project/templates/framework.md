# Framework — 14 Categories of AI Markers in Prose

This document is the **brain of the technical analysis**. It defines the stylistic tics typical of LLM generation in literary prose: definition, why it reads as a tic, detection signals, default ceiling, and default treatment.

**Generic.** Works for any assisted fiction manuscript. Detection signals are language-specific — `[pt-BR]` and `[en]` sections are provided; add `[es]`, `[fr]`, etc. as needed.

> **None of these constructions is an error.** All are legitimate figures of speech. The problem is always **density** — and density only becomes visible when you count.

---

## Language note

Instructions are in English. **Detection signals and examples appear in the target language**, because tics manifest through language-specific syntax.

**All analysis output must be written in the project's output language**, defined in `config/project.yaml`.

**Coverage.** `[pt-BR]` and `[en]` signals are calibrated. Other languages: the definitions, ceilings, and treatments still apply, but the signals must be adapted — note the adaptation in `config/style-guide.md` so analyses stay comparable across chapters.

---

## How density is measured

**The unit is occurrences per 1,000 words of chapter text.** One unit, everywhere: `analyze-chapter`, `review-revision`, `draft-scene` budgets, `consolidate-style` ceilings, `review-book` aggregates.

```
density = (occurrences in the chapter / chapter word count) × 1000
```

Reported to one decimal place: `3,4/1k`.

**Why per-1k and not a raw count:** a 5,000-word chapter with 12 antitheses and a 2,000-word chapter with 12 antitheses are not the same chapter. Per-1k is the only figure comparable across chapters and across drafts — which is what the revision trajectory (`before → after`) depends on.

**Counting rules — apply them identically every time, or the numbers are worthless:**

1. **Count the chapter's prose words**, including dialogue. Exclude the title, epigraphs, and any `_analysis`/`_outline` scaffolding.
2. **One occurrence = one instance of the pattern**, not one word. `"Sem casa. Sem nome. Sem hora."` is **one** negation list, not three.
3. **An instance belongs to one category only** — its dominant one. A triad that also closes a paragraph aphoristically counts in category 2 *or* 5, not both. State the call in the analysis when it is close.
4. **PRESERVE and persona-signature instances are not counted.** They are not tics by definition; counting them would make the density figure argue against the author's own decisions.
5. **RECURRENCE instances are counted**, and additionally flagged.

### Three categories that do not use per-1k

Forcing every category into one unit would produce a nonsense number. These three carry their own unit, always labelled:

| Category | Unit | Why |
|---|---|---|
| **8 — Lexical repetition** | per-1k **of the individual word** | The phenomenon is one word recurring, not a construction. Measure each flagged word separately. |
| **9 — Symmetrical dialogue** | exchanges per chapter | The unit is an exchange, not a sentence. A per-1k figure would reward long chapters. |
| **13 — Single-line endings** | % of chapters in the book | The tic only exists across chapters. A single chapter cannot have a density here. |

### Default ceilings

Each category below carries a **default ceiling**, marked *(calibratable)*. They are starting points derived from revised literary prose, not laws.

**Overriding them is expected.** A project sets its own in `config/style-guide.md → Density ceilings`, and a construction declared in `config/persona.md → Personal signatures` has no ceiling at all — it is not a tic. Precedence:

```
persona.md (signature → no ceiling)  >  style-guide.md (project override)  >  framework default
```

**Total ceiling: 8,0/1k** — the sum of all per-1k categories in a revised chapter. Deliberately lower than the sum of the individual ceilings, because the categories are not supposed to peak at once. A chapter under every individual ceiling but above 8,0/1k total is still too dense.

---

## 1. Binary antithesis

**Definition.** A short sentence negating a proposition, immediately followed by a short sentence asserting the opposite. Pattern: `Not X. Y.`

**Why it is a tic.** LLMs reach for binary parallelism because it is an easy way to manufacture apparent depth. Across a full book it becomes mechanical meter.

**Detection signals** `[pt-BR]`
- `"Não X. Y."` — short opposing sentences
- `"Não no sentido de X, mas no sentido de Y"`
- `"X, mas Y"` at high density
- Dialogue echoing `"Não Z"` / `"Z"`
- `"Não A. Não B. C."` — double negation plus assertion

**Detection signals** `[en]`
- `"Not X. Y."` — the canonical form
- `"It wasn't X. It was Y."` / `"This isn't X — it's Y."`
- `"Not because X, but because Y"`
- `"X, but not X"` — the self-qualifying echo
- Dialogue answering a question by negating its premise first

**Default ceiling:** 2,0/1k *(calibratable)*

**Default treatment**
- Cut 50% of occurrences
- Convert to a flowing sentence: `"Não era X — era Y"` instead of `"Não era X. Era Y."`
- Rewrite without the parallelism where possible
- Preserve when it carries the book's thesis

---

## 2. Triads and parallel lists

**Definition.** Three (or four) parallel elements in series, usually for emotional or philosophical weight.

**Why it is a tic.** Models train heavily on triadic rhythm, an anglophone pattern. At high density it reads as formulaic — including in English, where the training bias is strongest.

**Detection signals** `[pt-BR]`
- `"A, B, e C"` in rhetorical construction
- Adjectival triads: `"morna, amarga e ruim"`
- Triple anaphora: `"Eu fiz X. Eu fiz Y. Eu fiz Z."`
- Quartets — rarer, but the same marker
- Prepositional series: `"pra X, pra Y, pra Z"`
- Verb lists: `"dividiu, descreveu, segurou"`

**Detection signals** `[en]`
- Adjectival triads: `"cold, patient, and certain"`
- Triple anaphora: `"He counted. He waited. He counted again."`
- The rhetorical rule of three closing a paragraph
- `"of X, of Y, of Z"` — prepositional series
- Verb triads with no subordination: `"she turned, stopped, listened"`
- Asyndetic triads (no conjunction) — the model's favourite literary flourish

**Default ceiling:** 2,0/1k *(calibratable)*

**Default treatment**
- Cut 40%
- Reduce triad to two elements: drop the weakest
- Replace with a single concrete comparison
- Vary element length to break symmetry
- Preserve thesis triads (mottos, inscriptions, central lines)

---

## 3. Philosophical hedging

**Definition.** Enumerating possibilities in series as a performance of depth.

**Why it is a tic.** The model thinks aloud because hedging is safe — but accumulated hedges read as stylistic weakness. The reader senses simulated indecision.

**Detection signals** `[pt-BR]`
- `"Talvez X. Ou talvez Y. Ou talvez Z."` — three or more
- `"Pode ser X. Pode ser Y."`
- `"X. Ou Y. Ou nada disso."`
- Repeated `"não sei se X ou Y"`
- Sentences enumerating options without committing

**Detection signals** `[en]`
- `"Maybe X. Maybe Y. Or maybe Z."` — three or more
- `"Perhaps X. Perhaps not."`
- `"It could have been X. It could have been nothing."`
- `"Or maybe that was the point."` — the hedge as paragraph closer
- `"He wasn't sure whether X or Y"` repeated across scenes
- Rhetorical questions the narrator declines to answer, in series

**Default ceiling:** 1,0/1k *(calibratable)*

**Default treatment**
- Aggressive cut (60%)
- Pick one option and commit
- When indecision *is* the theme (a character in epistemic collapse), keep but reduce the count
- Replace with a single concrete image

---

## 4. Ironic meta-commentary

**Definition.** The narrator commenting on the narrator — observing their own thought, ironizing their own reaction, commenting on their own line.

**Why it is a tic.** It generates text without committing to the scene. At high density it becomes posturing: the narrator seems to be performing narration.

**Detection signals** `[pt-BR]`
- `"Essa frase deveria me preocupar mais do que me preocupou."`
- Professional self-classification: `"eu sou X em Y"`
- Self-interruption: `"aliás, X?"`
- Parenthetical self-comment: `"(muitos) anos"`
- Commentary on the character's trade
- Direct address: `"eu sei como isso soa"`
- Commenting on someone else's line: `"boa pergunta. Quase boa demais."`
- Manual-style enumeration: `"primeiro X e segundo Y"`
- Ironic self-labelling: `"eu sou o pior X do mundo"`

**Detection signals** `[en]`
- `"Which should have worried me more than it did."`
- `"I know how that sounds."` — direct address to the reader
- Self-interruption: `"and yes, before you ask, X"`
- Deflating parenthetical: `"(many) years"`, `"(allegedly)"`
- Commenting on another character's line: `"Good question. Too good."`
- Ironic self-labelling: `"I'm the worst possible person for this."`
- `"For the record, X."` / `"In my defence, X."`
- The narrator rating their own metaphor

**Default ceiling:** 1,0/1k *(calibratable)*

**Default treatment**
- Cut 50%
- Maximum one meta move per scene
- Remove self-explanatory parentheticals
- Cut expository trade commentary if repeated across chapters
- Preserve when it does real characterization work (once)

---

## 5. Paragraph-closing aphorism

**Definition.** A short epigrammatic sentence closing a descriptive paragraph. A literary punchline.

**Why it is a tic.** It is a pleasing, repeatable move. At high density every paragraph turns into "drop a memorable line".

**Detection signals** `[pt-BR]`
- Mid-length paragraph ending in a 3–7 word sentence with philosophical weight
- `"Era X. E era Y."` as a closer
- An isolated `"Mas Z."` after description
- Moral aphorisms stated as universal truth

**Detection signals** `[en]`
- Mid-length paragraph ending in a 3–7 word sentence with philosophical weight
- `"It was X. It was also Y."` as a closer
- An isolated `"But it was."` / `"It didn't."` after description
- Gnomic present tense inside a past-tense narrative: `"Grief keeps its own hours."`
- `"That was the whole of it."` / `"That was all."`

**Default ceiling:** 1,5/1k *(calibratable)*

**Default treatment**
- Cut 35–45%
- Fold the aphorism into a longer final sentence
- Move it mid-paragraph — far less worn
- Let some paragraphs end on a plain observation; impact comes from sequence
- Preserve thesis aphorisms

---

## 6. Serial comparisons

**Definition.** Three or more parallel `like`/`as` constructions.

**Why it is a tic.** Effective once per scene. In sequence it reads formulaic and almost didactic.

**Detection signals** `[pt-BR]`
- `"Como X. Como Y. Como Z."` across three consecutive sentences
- `"Como X, como Y"` in parallel within one sentence
- Stacked `"Como se X / Como se Y"`

**Detection signals** `[en]`
- `"Like X. Like Y. Like Z."` across consecutive sentences
- `"As if X. As if Y."` — stacked
- `"the way X does, the way Y does"` in parallel
- A simile chain inside one sentence: `"like a door, like a held breath, like the end of something"`

**Default ceiling:** 0,3/1k *(calibratable — effectively one series per chapter)*

**Default treatment**
- Cut 50%
- Maximum one series per chapter
- Replace the others with a single comparison given more room
- Watch closely for exact repetition across chapters

---

## 7. Anglicized vocabulary / LLM literary register

**Definition.** Vocabulary the model over-selects in literary registers. In non-English languages it manifests as **calques of modern English**; in English there is no calque, but the same bias shows as a recognizable set of over-used "literary" words and phrasings.

**Why it is a tic.** It is the fingerprint of the training distribution: in translated text for other languages, in over-represented contemporary literary prose for English.

**Flagged words** `[pt-BR]`
`performance` · `interface` · `âncora` (fig.) · `filtro` (fig.) · `processar` (emotion) · `densidade` (fig.) · `dissolução` · `consistência` · `operacional` · `categorizar` · `arquetípico` · `genuíno` · `reconhecimento` (emotional) · `compreensão` (where `entender` fits) · `narrativa` (outside technical use)

**Suggested substitutions** `[pt-BR]`

| Anglicism | Alternatives |
|---|---|
| performance | atuação, encenação, papel |
| interface | ponto de contato |
| âncora | peso, lastro, fio, pedra |
| filtro | véu, camada, lente |
| processar | entender, engolir, digerir |
| genuíno | de verdade, real, honesto |
| reconhecimento | ver, saber que era |
| compreensão | entender |
| narrativa | história, versão |

**Flagged register** `[en]`

Single words: `palpable` · `visceral` · `liminal` · `ineffable` · `cacophony` · `myriad` · `testament` · `tapestry` · `symphony` (fig.) · `dance` (fig.) · `weight` (emotional) · `hum` (fig.) · `ache` (as noun) · `unspooled` · `crystallized` (fig.)

Phrasings — more diagnostic than the words:

| Over-used construction | Why it reads generated |
|---|---|
| `a testament to X` | Editorializing abstraction the scene should carry |
| `a quiet kind of X` / `a certain kind of Y` | Vagueness dressed as precision |
| `the weight of X settled over Y` | The model's default for unnamed emotion |
| `something shifted` / `something had changed` | Event without content |
| `X, and something in her Y'd` | Displaced agency to avoid naming |
| `it was the kind of X that Y` | Formula for manufacturing significance |
| `part of him knew X` | Split-self interiority (see also cat. 15) |
| `the air itself seemed to X` | Pathetic fallacy on autopilot |

**Default ceiling:** 1,0/1k *(calibratable)*

**Operating rule.**
- `[pt-BR]` and other non-English: if the word exists naturally in the target language's pre-2010 literary register, it is legitimate. If it is a calque of a modern English term, substitute.
- `[en]`: the words are all legitimate English. Flag on **frequency and reflex**, not on existence — a `palpable` chosen after considering three alternatives is style; a `palpable` reached for automatically is register noise. The phrasings table is the stronger signal; treat a hit there as a flag regardless of count.

> **Important.** Elevated native vocabulary does **not** belong here. High register is a legitimate stylistic choice; calqued anglicism and reflex register are training noise. Check `config/persona.md` before flagging.

---

## 8. Excessive lexical repetition

**Definition.** Theme words returning too often, losing weight where they should resonate.

**Why it is a tic.** Models do not vary vocabulary because consistency is safer than variation. The reader feels lexical fatigue.

**Commonly overused** `[pt-BR]`
`presença` / `ausência` · `cansado` / `cansaço` · `honesto` · `vazio` · `decisão` / `decidir` · `real` / `realidade` · `importar` · `tipo` (meaning "like")

**Commonly overused** `[en]`
`presence` / `absence` · `tired` / `exhaustion` · `honest` · `empty` / `emptiness` · `real` / `reality` · `matter` (verb) · `moment` · `silence` · `just` (adverbial filler) · `almost` · `somehow` · `still` (adverbial)

**Unit and ceiling.** Measured **per word, per 1k** — not as a category total.

**Default ceiling:** 1,5/1k for any single non-function word *(calibratable)*. A word above this is a candidate; whether it is thesis or habit is the author's call.

**Default treatment**
- Dedicated lexical variation pass
- For each flagged word: report its per-1k figure, ask "is this thesis or habit?"
- Thesis: keep, and consider it for `preserve-list.md`. Habit: substitute with something concrete, or cut
- Prefer sensory synonyms over abstract ones

---

## 9. Symmetrical dialogue

**Definition.** Exchanges where every reply mirrors the previous one grammatically. Ping-pong.

**Why it is a tic.** It works once; scene after scene it reads choreographed. The reader senses the model assembling the exchange.

**Detection signals**
- Four or more short replies in identical meter
- `"X?"` / `"X."` echo sequences
- Question-answer-question-answer with no description between
- Dialogic chiasmus
- Every line 1–3 words long

**Unit and ceiling.** Measured in **symmetrical exchanges per chapter**, not per-1k.

**Default ceiling:** 1 per chapter *(calibratable)*

**Default treatment**
- Diversify format in 40% of scenes
- Add description between lines: gesture, pause, environment
- Lengthen one reply to break the meter
- If A asks short, have B answer long
- Use free indirect speech in some scenes
- Diegetic minimalism (character designed to be terse) — keep, but add gesture

> **Watch for the inverted problem.** Fixing ping-pong easily overloads the scene with narrative commentary. One gesture between lines is enough; two is already dense.

---

## 10. Negation lists

**Definition.** Parallel construction enumerating absences.

**Why it is a tic.** Alongside triads, one of the most identifiable LLM markers.

**Detection signals** `[pt-BR]`
- `"Sem X. Sem Y. Sem Z."` — three or more
- `"Sem X, sem Y, e sem Z"` in one sentence
- `"Não X, nem Y, nem Z"`
- Closing with `"nem nada"`

**Detection signals** `[en]`
- `"No X. No Y. No Z."` — three or more
- `"Without X, without Y, without Z"` in one sentence
- `"Not X, not Y, not anything at all."`
- `"There was no X. There was no Y."` — existential anaphora
- Closing with `"nothing at all"` / `"and nothing else"`

**Default ceiling:** 0,8/1k *(calibratable)*

**Default treatment**
- Cut 60%
- Reduce to one negation followed by a concrete image
- Replace with a positive verb
- Diegetic (absence as theme) — keep, sparingly

---

## 11. Em-dash overuse

**Definition.** Heavy use of `—` where the target language would normally use a comma, period, colon, or parentheses.

**Why it is a tic.** A strong LLM signature — arguably the single most recognized one among readers. Many languages punctuate differently; overuse reads as translated English.

**Problem types**
- **A** — replacing a comma
- **B** — double dash as parenthesis (`X — description — Y`)
- **C** — opening a narrative sentence (not dialogue) — a punctuation error in `[pt-BR]`
- **D** — interrupted thought (acceptable; only a problem at density)

**Default ceiling:** 2,0/1k narrative dashes *(calibratable)*

**Counting note.** `[pt-BR]` excludes dialogue-opening dashes from the count — they are the national standard, not a tic. `[en]` counts every em-dash in narrative and dialogue alike, since English marks dialogue with quotation marks.

**Default treatment**
- Aggressive reduction (60%) of narrative dashes
- Type A → comma. Type B → parentheses or recast. Type C → period + capital
- `[pt-BR]` **Brazilian standard:** em-dash only to open dialogue
- `[en]` No national rule to lean on — the ceiling *is* the rule. Semicolons, colons, and periods are all under-used by comparison

---

## 12. Rhythmic summaries

**Definition.** Sequences of short parallel clauses summarizing actions or states.

**Why it is a tic.** Works once per chapter. Beyond that it becomes a mantra.

**Detection signals** `[pt-BR]`
- Subject anaphora across three or more consecutive sentences
- Short parallel verbs without subordination
- Chains of 3+ actions

**Detection signals** `[en]`
- `"I did X. I did Y. I did Z."` — subject anaphora across consecutive sentences
- Sentence-initial `"And"` repeated across a paragraph
- Participial chains: `"Walking, thinking, not looking back."`
- Time-stamped summary runs: `"Monday, X. Tuesday, Y."`

**Default ceiling:** 1,0/1k *(calibratable)*

**Default treatment**
- Cut 50%
- Reduce three parallels to two, or one with weight
- Vary subject or verb
- Subordinate instead of coordinating

---

## 13. Single-line chapter endings

**Definition.** Chapters closing on an isolated short sentence in its own paragraph, carrying emotional weight.

**Why it is a tic.** Worn but literary. The problem is frequency: if every chapter closes this way, it becomes formula.

**Detection signals**
- Final paragraph of 5–12 words, isolated
- Recurring formulas across chapters
- Isolated aphoristic closure

**Unit and ceiling.** Measured as **% of the book's chapters**, not per-1k. A single chapter cannot be dense here — the tic only exists in aggregate.

**Default ceiling:** 35% of chapters *(calibratable)*

**Default treatment — vary formats across the book**
- ~1/3 of chapters on a single line (keep; it is effective)
- ~1/3 on a mid-length paragraph
- ~1/5 on dialogue
- The rest on neutral sensory description

Eliminate literal recurring formulas.

---

## 14. Named emotion

**Definition.** The narrator names the emotion instead of showing it through gesture, breath, or micro-expression.

**Why it is a tic.** Naming solves the task quickly. Experienced writers leave emotion implicit, carried by action.

**Detection signals** `[pt-BR]`
- `"Eu senti X"` where X is an emotion
- `"Ele estava genuinamente Y"`
- `"Eu vi o medo nos olhos dele"`
- `"Naquele instante eu entendi que era amor / medo / raiva"`
- Direct attribution of another's thoughts
- Double labelling: `"eu sentia um sentimento horrível"`

**Detection signals** `[en]`
- `"I felt X"` where X is an emotion
- `"She was genuinely Y"`
- `"I saw the fear in his eyes"`
- `"In that moment I understood it was love / fear / rage"`
- `"A wave of X washed over her"` — the metaphor that still names
- Direct attribution of another's interiority from an unprivileged POV
- Double labelling: `"a terrible feeling of dread"`

**Default ceiling:** 2,0/1k *(calibratable)*

**Default treatment**
- Cut 50%
- Replace with gesture or bodily reaction:

| Named `[pt-BR]` | Shown |
|---|---|
| Eu senti alívio | O ar saiu inteiro pelos pulmões |
| Vi o medo nos olhos dele | Os olhos dele não saíram dos meus por tempo demais |
| Senti uma raiva incontrolável | A mão fechou sem perguntar |
| Eu estava com medo | *(cut — let the scene work)* |

| Named `[en]` | Shown |
|---|---|
| I felt relief | The breath went out of me all at once |
| I saw the fear in his eyes | He held my look a beat too long |
| A rage I couldn't control | My hand closed without asking |
| I was afraid | *(cut — let the scene work)* |

---

## 15. Other tics

Open category. Always include it in the analysis output to capture whatever is specific to the work:

- Caps lock for emotional emphasis (use italics instead)
- Misplaced erudite references (Schrödinger in a medieval setting)
- Invented proverbs in quotes
- Anchor phrases recycled literally across chapters
- Object personification as recurring humour
- Internal dialogue between "parts of me"
- Ritualized closings

No ceiling — this category is descriptive. Occurrences here are reported with a count and, when a pattern stabilizes across three or more chapters, proposed for promotion into the project's `style-guide.md` as a named local tic with its own ceiling.

---

## How to apply this in an analysis

1. **Count the chapter's words first.** Every density figure depends on it; record it in the analysis header.
2. For each category (1–14), sweep the chapter for the listed signals in the project's language.
3. For each occurrence:
   - **Quote the exact text.** Never paraphrase.
   - Cross-check `config/persona.md` → if the construction is a declared author signature, **do not flag it and do not count it**.
   - Cross-check `reports/preserve-list.md` → if listed, mark **(PRESERVE — thesis)** and **do not count it**.
   - Cross-check `reports/recurrences.md` → if it appears elsewhere, mark **(RECURRENCE — also in ch. X, Y)**. Counted, and prioritized.
   - Otherwise, suggest a concrete treatment from the defaults above.
4. **Compute the density** for each category: `(occurrences / word count) × 1000`, one decimal. Use each category's own unit for 8, 9, and 13.
5. **Compare against the ceiling** — project override from `style-guide.md` if present, otherwise the framework default. Set the cut target as the number of occurrences that must go to land under it.
6. Generate section 15 with chapter-specific tics.
7. **Compute the chapter total** (sum of per-1k categories) and compare against the total ceiling (default 8,0/1k).
8. Write the **Verdict**: top 5–8 priorities by impact, untouchables, time estimate.

### Verdict priority order

1. Objective grammatical errors (rare, but first)
2. Literal cross-chapter recurrences (indefensible)
3. Categories furthest above their ceiling, weighted by scene importance
4. Tics breaking rhythm at pivotal moments
5. The rest, by volume

### Suggested revision pass order

Work one category at a time, chapter by chapter — not everything at once:

1. **Em-dashes** — mechanical, fast, visually relieves ~30%
2. **Binary antithesis** — immediately changes the rhythm
3. **Hedging** — commit to choices
4. **Triads** — reduce to two or one
5. **Negation lists** — cut aggressively
6. **Meta-commentary and aphorisms** — together
7. **Vocabulary and lexical repetition** — thesaurus pass with judgement
8. **Dialogue** — rebuild key scenes without symmetry
9. **Named emotion** — show vs. tell
10. **Chapter endings** — vary formats across the book
