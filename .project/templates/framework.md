# Framework — 14 Categories of AI Markers in Prose

This document is the **brain of the technical analysis**. It defines the stylistic tics typical of LLM generation in literary prose: definition, why it reads as a tic, detection signals, and default treatment.

**Generic.** Works for any assisted fiction manuscript. Detection signals include language-specific examples — extend the language sections as needed.

> **None of these constructions is an error.** All are legitimate figures of speech. The problem is always **density** — and density only becomes visible when you count.

---

## Language note

Instructions are in English. **Detection signals and examples appear in the target language**, because tics manifest through language-specific syntax. Sections marked `[pt-BR]` hold Portuguese examples; add `[en]`, `[es]`, etc. as needed.

**All analysis output must be written in the project's output language**, defined in `config/project.yaml`.

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

**Default treatment**
- Cut 50% of occurrences
- Convert to a flowing sentence: `"Não era X — era Y"` instead of `"Não era X. Era Y."`
- Rewrite without the parallelism where possible
- Preserve when it carries the book's thesis

---

## 2. Triads and parallel lists

**Definition.** Three (or four) parallel elements in series, usually for emotional or philosophical weight.

**Why it is a tic.** Models train heavily on triadic rhythm, an anglophone pattern. At high density in other languages it reads as formulaic.

**Detection signals** `[pt-BR]`
- `"A, B, e C"` in rhetorical construction
- Adjectival triads: `"morna, amarga e ruim"`
- Triple anaphora: `"Eu fiz X. Eu fiz Y. Eu fiz Z."`
- Quartets — rarer, but the same marker
- Prepositional series: `"pra X, pra Y, pra Z"`
- Verb lists: `"dividiu, descreveu, segurou"`

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

**Detection signals**
- Mid-length paragraph ending in a 3–7 word sentence with philosophical weight
- `"Era X. E era Y."` as a closer
- An isolated `"Mas Z."` after description
- Moral aphorisms stated as universal truth

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

**Default treatment**
- Cut 50%
- Maximum one series per chapter
- Replace the others with a single comparison given more room
- Watch closely for exact repetition across chapters

---

## 7. Anglicized vocabulary

**Definition.** Abstract words calqued from modern English that LLMs favour in literary registers. In other languages they read slightly artificial.

**Why it is a tic.** They are literal translations of contemporary English vocabulary — the fingerprint of training on translated text.

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

**Operating rule.** If the word exists naturally in the target language's pre-2010 literary register, it is legitimate. If it is a calque of a modern English term, substitute.

> **Important.** Elevated native vocabulary does **not** belong here. High register is a legitimate stylistic choice; calqued anglicism is training noise. Check `config/persona.md` before flagging.

---

## 8. Excessive lexical repetition

**Definition.** Theme words returning too often, losing weight where they should resonate.

**Why it is a tic.** Models do not vary vocabulary because consistency is safer than variation. The reader feels lexical fatigue.

**Commonly overused** `[pt-BR]`
`presença` / `ausência` · `cansado` / `cansaço` · `honesto` · `vazio` · `decisão` / `decidir` · `real` / `realidade` · `importar` · `tipo` (meaning "like")

**Default treatment**
- Dedicated lexical variation pass
- For each flagged word: count occurrences, ask "is this thesis or habit?"
- Thesis: keep. Habit: substitute with something concrete, or cut
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

**Default treatment**
- Cut 60%
- Reduce to one negation followed by a concrete image
- Replace with a positive verb
- Diegetic (absence as theme) — keep, sparingly

---

## 11. Em-dash overuse

**Definition.** Heavy use of `—` where the target language would normally use a comma, period, colon, or parentheses.

**Why it is a tic.** A strong LLM signature. Many languages punctuate differently; overuse reads as translated English.

**Problem types**
- **A** — replacing a comma
- **B** — double dash as parenthesis (`X — description — Y`)
- **C** — opening a narrative sentence (not dialogue) — a punctuation error
- **D** — interrupted thought (acceptable; only a problem at density)

**Default treatment**
- Aggressive reduction (60%) of narrative dashes, excluding dialogue openers
- Type A → comma. Type B → parentheses or recast. Type C → period + capital
- `[pt-BR]` **Brazilian standard:** em-dash only to open dialogue

---

## 12. Rhythmic summaries

**Definition.** Sequences of short parallel clauses summarizing actions or states.

**Why it is a tic.** Works once per chapter. Beyond that it becomes a mantra.

**Detection signals**
- Subject anaphora across three or more consecutive sentences
- Short parallel verbs without subordination
- Chains of 3+ actions

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

**Default treatment — vary formats across the book**
- 4–5 chapters on a single line (keep; it is effective)
- 4–5 on a mid-length paragraph
- 3–4 on dialogue
- 2–3 on neutral sensory description

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

**Default treatment**
- Cut 50%
- Replace with gesture or bodily reaction:

| Named `[pt-BR]` | Shown |
|---|---|
| Eu senti alívio | O ar saiu inteiro pelos pulmões |
| Vi o medo nos olhos dele | Os olhos dele não saíram dos meus por tempo demais |
| Senti uma raiva incontrolável | A mão fechou sem perguntar |
| Eu estava com medo | *(cut — let the scene work)* |

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

---

## How to apply this in an analysis

1. For each category (1–14), sweep the chapter for the listed signals.
2. For each occurrence:
   - **Quote the exact text.** Never paraphrase.
   - Cross-check `config/persona.md` → if the construction is a declared author signature, **do not flag it**.
   - Cross-check `reports/preserve-list.md` → if listed, mark **(PRESERVE — thesis)**.
   - Cross-check `reports/recurrences.md` → if it appears elsewhere, mark **(RECURRENCE — also in ch. X, Y)**.
   - Otherwise, suggest a concrete treatment from the defaults above.
3. Compute category density (~N occurrences).
4. Set a cut target (~M, usually half).
5. Generate section 15 with chapter-specific tics.
6. Write the **Verdict**: top 5–8 priorities by impact, untouchables, time estimate.

### Verdict priority order

1. Objective grammatical errors (rare, but first)
2. Literal cross-chapter recurrences (indefensible)
3. Central scenes with high density
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
10. **Chapter endings** — vary formats
