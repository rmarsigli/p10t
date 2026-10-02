# Craft — 11 Categories of Narrative Quality

This document is the **brain of the craft critique**. Where `framework.md` asks *what marks did the machine leave in this prose*, this one asks a different question: **does the narrative work?** — does the scene earn its place, does the reader follow, believe, keep turning pages.

**Generic.** Works for any fiction manuscript, assisted or not. Nothing here is specific to AI-generated prose: a chapter written entirely by hand can fail every category, and a heavily assisted one can pass them all.

> **None of this is measured per 1,000 words.** Density is the right unit for a construction that repeats. A scene that does not turn, a motive that does not convince, a reveal placed before the reader cares — these happen once and sink the chapter. They are judged, with evidence, never counted into a rate.

---

## Language note

Instructions are in English. Most craft signals are **structural and language-independent** — a scene without a turn has no turn in any language. Where a signal lives in the wording (exposition in dialogue, stock phrases, filter verbs, sentence-level problems), examples are given in `[pt-BR]` and `[en]`.

**All critique output must be written in the project's output language**, defined in `config/project.yaml`.

---

## What this framework refuses to do

**No grades.** No score per category, no score per chapter, no average. Three reasons, all of them the same reason `review-book` refuses a "% human" figure:

1. **A grade is not measurable from prose.** It would be invented, and an invented number reads as a measurement.
2. **A model's grade drifts.** The same chapter scores 6 today and 8 tomorrow. The system's promise — the same figure next week — would break on the first re-run.
3. **Grades inflate and flatten.** Everything lands between 7 and 8, and the one problem that sinks the chapter averages away against ten things that are fine.

What replaces the grade is a **finding with a reader effect** (below) and a **verdict decided by rule** (see *Verdict*). Both are arguable item by item, which a number never is.

**Count what is countable; never score what is not.** Words per scene, a scene's share of the chapter, words per chapter across an Act — these are real counts and they are reported as such, because they are the hardest evidence available for a pacing finding. Nothing else gets a number.

**Not a genre template.** The book is judged against its own contract — its genre (`project.yaml → genre`), its references, its declared choices — never against a structural convention or a different book the critic might prefer. Not every chapter needs three escalating scenes. A chapter that works oddly, works.

---

## How a finding is recorded

Every finding carries five fields. A finding missing one is not finished.

| Field | What it holds |
|---|---|
| **Location and quote** | Scene number plus the **literal** text. For a long passage: opening + `[...]` + closing. A structural finding quotes the sentence where the problem is visible |
| **Reader effect** | What happens to the reader, from the closed list below |
| **Mechanism** | Why the text produces that effect — the part that teaches |
| **Severity** | `break`, `friction`, or `note` |
| **Level** | Where the fix lives — and therefore which instrument takes it |

### Reader effects — the closed list

This list does for the critique what the per-1k unit does for the analysis: it makes findings **comparable across chapters**. A finding phrased as "this feels off" cannot be compared with anything; "the reader is lost about who is speaking" can.

| Effect | `[pt-BR]` label | The reader… |
|---|---|---|
| **lost** | *se perde* | cannot tell who, where, when, or what physically happened |
| **disbelieves** | *desacredita* | stops accepting an action, a motive, or a coincidence |
| **impatient** | *se impacienta* | is held on something that does not matter, or kept from something that does, without the delay doing work |
| **indifferent** | *não se importa* | does not know what is at stake, or why this should matter to them |
| **has seen it** | *já viu isso* | recognizes the move — phrase, image, plot turn — before it completes |
| **distanced** | *se distancia* | is pushed out of the experience: the scene is summarized, explained, or narrated from outside when it should be lived |
| **ahead** | *se adianta* | predicts the outcome, and the text does nothing with that knowledge |
| **told twice** | *ouve duas vezes* | receives the same information or beat again with no new charge |

> **A finding with no reader effect is a preference, not a finding. Drop it.** "I would have written this differently" is not a critique. If the only person affected is the critic, the text is fine.

Dramatic irony is not *ahead*: the reader knowing more than the character is a device when the scene uses the gap. Delay is not *impatient* when it is the suspense. Each category below says where its line falls.

### Severity

| Severity | `[pt-BR]` | Meaning |
|---|---|---|
| **break** | *quebra* | The reader stops understanding or stops believing. A careful reader rereads in confusion, or loses faith in the story |
| **friction** | *atrito* | The reading slows, dilutes, or cools — but continues |
| **note** | *nota* | Worth knowing; no action required |

Severity is a property of the **effect**, not of the location. A friction in the chapter's most important scene is still a friction — its location is recorded, and the verdict rule (below) is what gives location its weight. Upgrading severity because a scene matters would hide the distinction the verdict depends on.

### Level — where the fix lives

| Level | The fix is… | Goes to |
|---|---|---|
| **sentence** | rewording, inside the passage | `revise-passage`, or the author |
| **scene** | the scene's design: what it does, where it enters and exits | the author; `restructure-chapter` if the scene must move, merge, or go |
| **chapter** | the order or set of scenes | `restructure-chapter` |
| **book** | upstream of this chapter — a missing plant, an arc beat that never happened | `check-arc`, `check-consistency`, `review-book` |

**The level is often the most valuable thing the critique says.** An author polishing sentences in a scene that has no reason to exist is wasting the week. "The problem is not the sentences" is a finding in its own right.

---

## Precedence and protections

The critique reads the project's declared decisions **before** judging, and they win:

```
worldbuilding.md → Deliberately unexplained
  >  persona.md (signatures, §2 syntax, §6 narrative craft)
  >  style-guide.md (structural decisions, world rules affecting the prose)
  >  preserve-list.md
  >  genre contract (project.yaml → genre, references.md)
  >  this framework's defaults
```

1. **Deliberately unexplained.** Withheld information listed there is **never** a clarity, exposition, or motivation finding. The reader not knowing is the design. The protection covers the *mystery*, not the *staging*: a reader who cannot tell who is speaking in a scene about the mystery is still lost, and that is still a finding.
2. **Declared choices.** A construction or craft choice declared in `persona.md` — a contemplative pace, long description, an expository narrator, fragments — is never flagged **for being that choice**. A finding inside a declared choice must name an effect the choice does not account for: "within the declared slow pace, the turn itself is summarized" is a finding; "this is slow" is not.
3. **Structural decisions.** A rule in `style-guide.md` is a constraint to work within, never a problem to report. If the book forbids proper names, a speaker-attribution finding proposes orientation that respects the rule — never "name the character".
4. **Preserve list.** A protected phrase is never proposed for cutting and never flagged as worn.
5. **Genre contract.** What the genre requires is not wear and not exposition: the detective's summation, the heist briefing, the meet-cute.

---

## Boundaries — one finding, one home

The critique does not duplicate other instruments. When a problem belongs elsewhere, the critique names it in one line under **Outside this instrument** and routes it.

| Problem | Home |
|---|---|
| Emotion named instead of shown, as a construction | `framework.md` cat. 14 → `analyze-chapter` |
| Dialogue in mirrored meter | `framework.md` cat. 9 → `analyze-chapter` |
| A word or phrase overused inside this chapter | `framework.md` cat. 8 → `analyze-chapter` |
| A phrase or image repeated across chapters | `scan-recurrences` |
| LLM literary register, anglicisms | `framework.md` cat. 7 → `analyze-chapter` |
| Contradiction with an established fact, timeline, or knowledge state | `check-consistency` |
| A character's arc across chapters; the book's tension curve | `check-arc` |
| Objective grammar errors | `review-revision` axis 1 — the critique lists those it notices, without hunting them |

What stays here: the POV breach (cat. 7), what dialogue *does* (cat. 8), wear from the reader's library rather than this book (cat. 10), implausibility inside the scene (cat. 5), tension inside the chapter (cat. 3).

---

## The 11 categories

Three groups. **Structure** decides whether the chapter has a reason to exist in this shape; **sense** decides whether the reader follows and believes; **execution** decides how the page delivers it. Work in that order — a sentence-level fix in a scene that will be cut is wasted.

| Group | # | Category |
|---|---|---|
| Structure | 1 | Scene function |
| | 2 | Pacing |
| | 3 | Tension and the dramatic question |
| Sense | 4 | Clarity and orientation |
| | 5 | Logic, motivation and agency |
| Execution | 6 | Exposition |
| | 7 | Point of view and distance |
| | 8 | Dialogue |
| | 9 | Concreteness |
| | 10 | Wear |
| | 11 | Sentence |

---

## 1. Scene function

**Definition.** Every scene changes something — a state, a relationship, what the reader knows, the question the reader is carrying. Two tests: **conflict** (what resists?) and **turn** (what is different at the end?).

**Typical effects.** *indifferent*, *impatient*, *told twice*.

**Signals**
- The scene ends with everyone exactly where they began
- The scene delivers information another scene already delivers
- A beat repeats without escalating — the second argument about the same thing, at the same pitch
- **The cut test:** remove the scene mentally. If nothing later becomes confusing or weaker, the scene was not carrying anything

**Not a finding**
- A deliberate rest after a climax — the reader needs it, and the chapter's shape uses it
- A transition doing real work: time passing, a planting, a change of place the next scene depends on
- A scene the outline declares as a rest, if the rest is placed where the chapter needs one

Record such scenes as *rest* in the scene map and judge them in the chapter's context, not in isolation.

**Default treatment**
- Give it a turn: what could be different at the end?
- Merge it with the scene doing similar work
- Compress it to a paragraph of summary
- Cut it — through `restructure-chapter`, which relocates whatever it was carrying

**Typical level.** Scene, chapter.

---

## 2. Pacing

**Definition.** The proportion between **page time** and **dramatic weight**. What matters gets scene — moment by moment. Connective tissue gets summary. Pacing fails when that proportion inverts.

**Typical effects.** *impatient*, *distanced*.

**Evidence.** The scene map's word counts and shares. "Scene 3 is slow" is an opinion; "the turn gets 140 words (6%) and the drive to the house gets 900 (38%)" is evidence.

**Signals**
- **Inverted proportion** — the turn summarized in a sentence while transit or routine gets pages
- **Entering early** — arrival, greetings, small talk, the coffee being poured, before the conflict starts
- **Leaving late** — after the turn the scene keeps going: goodbyes, a recap, a character reflecting on what the reader just watched
- **Halting at the peak** — a block of description, backstory or interiority dropped into the moment of highest pull
- **Uniform weight** — every scene the same length and pitch, so nothing reads as more important
- **A repeated realization** — the character arrives at the same insight twice
- **A flashback at the wrong moment** — interrupting the present exactly where forward pull is strongest

**Not a finding**
- **Delay that raises the question.** Stretching the moment before a reveal *is* pacing working. The test: does the delay sharpen what the reader wants to know, or dissipate it?
- A pace the persona declares — contemplative, lingering, digressive — when the slowness is the voice and not a proportion error. A turn summarized inside a slow book is still a finding

**Default treatment**
- Enter late, leave early — cut to the first line where something resists, end on the turn
- Expand the turn into scene; compress the transit into summary
- Move interiority before the peak or after it, never through it
- Cut the repeated beat

**Typical level.** Scene; chapter when the problem is the shape (uniform weight).

---

## 3. Tension and the dramatic question

**Definition.** At every point the reader should be carrying a question — *what will happen, will they, why did she*. At chapter level: the **opening** gives the reader a reason to continue, and the **exit** leaves the question sharpened, sustained, or deliberately released.

**Typical effects.** *indifferent*, *ahead*, *impatient*.

**Signals**
- An opening of weather, waking up, or description that runs for paragraphs before any question forms
- A question answered as soon as it is asked
- **Unclear stakes** — the reader does not know what is lost if this fails
- The conflict resolved by an outside force rather than by a character's choice
- An exit that closes everything, with nothing pulling forward — outside an Act or book ending
- **False tension** — danger the reader already knows is not real

**Not a finding**
- A released ending at an Act close, or a breather chapter after a peak
- **Quiet is not flat.** A chapter with no action can carry enormous tension through an internal question; an action chapter can carry none. Tension is an open question, not event volume

**Default treatment**
- Name the stakes earlier — what does the character lose?
- Delay the answer; let one question open before the previous one closes
- Move the question into the first paragraph
- End the chapter on the open element, not on its resolution

**Typical level.** Chapter; scene for a single collapsed question.

---

## 4. Clarity and orientation

**Definition.** The reader knows who is present, who is speaking, where they are, when it is, and what physically happened.

**Typical effects.** *lost*.

**Signals**
- **White room** — a scene that runs beyond its first lines without anchoring place, time, or who is present
- A run of dialogue where the speaker can no longer be tracked
- A pronoun with two candidate referents
- An unmarked jump in time or place
- Impossible or untraceable blocking — a character sitting, then at the door, with no movement between
- An action whose outcome is unclear — did the blow land, did she leave?
- Several new names introduced in a cluster

**Not a finding**
- Disorientation as the effect — a dream, a concussion, a deliberately withheld identity — especially when listed in `worldbuilding.md → Deliberately unexplained` or declared in `style-guide.md`

**The test:** is the reader confused about what the book *wants them to wonder about*, or about something the book *wants them to know*? Only the second is a finding.

**Default treatment**
- Anchor in the first lines: one concrete sensory detail, one person, one time cue
- Add action beats that identify speakers without tags
- Replace the ambiguous pronoun with the name or a role
- Mark the jump — a scene break, a time cue in the first sentence

**Typical level.** Sentence, scene.

---

## 5. Logic, motivation and agency

**Definition.** Actions follow from what characters want, fear, and know. Events are caused, not convenient. The protagonist drives the story rather than being carried by it.

**Typical effects.** *disbelieves*, *indifferent*.

**Signals**
- A character acts against their established want or fear with no on-page pressure to explain it — check the character sheet's want/need/fear/lie engine
- **The resolving coincidence** — chance that *creates* trouble is fair; chance that *solves* it is not
- **The ignored obvious solution** — the reader asks "why don't they just…?" and the page never answers
- An antagonist made foolish so the plot can proceed
- **The passive protagonist** — things happen to them; others make the decisions that matter
- A plot that requires a character not to ask the question anyone would ask

**Not a finding**
- Irrational action shown *as* irrational, driven by the fear or lie the character sheet declares
- A motive the book deliberately withholds and later pays — protected if listed as deliberately unexplained; flag as a *note* if not listed, asking whether it should be
- A contradiction with an established fact — that is `check-consistency`, not this

**Default treatment**
- Plant the pressure earlier — the fix for an unconvincing decision is almost always upstream of it
- Give the character the decision that a coincidence or another character is making
- Turn the coincidence into a consequence of something already on the page
- Acknowledge the obvious solution on the page and close it

**Typical level.** Scene; book when the missing pressure belongs chapters earlier.

---

## 6. Exposition

**Definition.** Information the reader needs, delivered where they need it, through the scene rather than around it.

**Typical effects.** *impatient*, *distanced*, *told twice*.

**Signals**
- **Info dump** — a block of backstory or world explanation that stops the scene
- **Telling each other what both know** — dialogue whose only audience is the reader
- **Explaining the dramatized** — the narrator interprets the gesture the scene just showed
- Information delivered before the reader has any reason to want it
- The same information delivered twice
- Terms defined in apposition at first mention, glossary-style

**Detection signals** `[pt-BR]`
- `"Como você sabe,"` / `"Como você bem sabe"` in dialogue
- `"Ou seja,"` / `"Isso significava que"` right after a dramatized beat
- `"Ele explicou que"` followed by a paragraph of information
- `"Desde que X acontecera, Y"` opening a backstory block mid-scene

**Detection signals** `[en]`
- `"As you know,"` / `"As you're aware"` in dialogue
- `"In other words,"` / `"Which meant that"` right after a dramatized beat
- `"She explained that"` followed by a paragraph of information
- `"Ever since X, Y had"` opening a backstory block mid-scene

**Not a finding**
- Exposition the genre contract expects — the summation, the briefing, the lecture a character is known for
- A narrator whose voice is expository by declared persona — then judge placement, not presence

**Default treatment**
- Cut, and trust the scene to have delivered it
- Distribute — one fact per beat, attached to an action
- Convert to conflict: someone wants the information, and getting it costs
- Delay until the reader is asking for it

**Typical level.** Sentence, scene.

---

## 7. Point of view and distance

**Definition.** The narration stays within what its point-of-view character can perceive and know, and its **distance** from that character moves on purpose.

**Typical effects.** *distanced*, *lost*, *disbelieves*.

**Signals**
- **Head-hopping** — another character's thought rendered from inside, within a scene held by one POV
- **Impossible knowledge** — the POV perceives what they cannot: their own expression, an event in another room, *"unaware that…"*
- **Narratorial foreshadowing** breaking a close POV
- **Unmotivated distance shifts** — close, then distant, then close again inside a paragraph
- **Filter verbs** stacking distance in a close POV — the character *sees*, *notices*, *feels* instead of the thing simply appearing

**Detection signals** `[pt-BR]`
- `"Mal sabia ela que"` / `"Sem saber que"`
- `"Ela viu que"`, `"percebeu que"`, `"sentiu que"`, `"notou que"` in series
- Another character's `"pensou"` inside a scene held by one POV

**Detection signals** `[en]`
- `"Little did she know"` / `"Unaware that"`
- `"She saw that"`, `"she noticed"`, `"she felt"`, `"she realized"` in series
- Another character's `"thought"` inside a scene held by one POV

**Not a finding**
- An omniscient narrator declared in `style-guide.md` or `persona.md`
- A distance shift used as a device — pulling out at a death, closing in at a revelation

**Boundary.** Named emotion as a construction is `framework.md` cat. 14. Here the question is narrower: *could this POV know or perceive this?*

**Default treatment**
- Route the information through what the POV can perceive — a gesture, a sound, a silence
- Cut the foreshadowing
- Drop the filter verb and let the thing appear

**Typical level.** Sentence, scene.

---

## 8. Dialogue

**Definition.** Every line does work — advances, reveals, resists, characterizes — and every speaker sounds like themselves.

**Typical effects.** *impatient*, *distanced*, *disbelieves*.

**Signals**
- **On the nose** — characters state exactly what they feel and mean, with nothing underneath
- **Interchangeable voices** — cover the attributions: can you tell who is speaking? Compare against the character sheets' verbatim voice samples
- Greetings, small talk, and goodbyes with no function
- **Monologue in disguise** — one speaker lectures while the other prompts (*"And then?"*)
- **No resistance** — everyone agrees; nobody wants something the other will not give
- Attributions and adverbs doing the acting

**Detection signals** `[pt-BR]`
- `"Eu estou com raiva de você porque…"` — the feeling as the line itself
- `"E então?"` / `"Continue."` as the other speaker's only contribution
- `"disse, irritado"` / `"respondeu, com tristeza"`

**Detection signals** `[en]`
- `"I'm angry at you because…"` — the feeling as the line itself
- `"And then?"` / `"Go on."` as the other speaker's only contribution
- `"she said angrily"` / `"he replied sadly"`

**Not a finding**
- Small talk carrying subtext — the conversation about the weather that is really about the divorce
- Symmetrical meter — that is `framework.md` cat. 9

**Default treatment**
- Give each speaker a want inside the exchange
- Replace the stated feeling with what they do instead of saying it
- Cut the entry and exit lines; start mid-exchange
- Rewrite one line per speaker against their character sheet's voice samples

**Typical level.** Sentence, scene.

---

## 9. Concreteness

**Definition.** The specific detail that only this place, this person, this moment could have — over the generic one any book could.

**Typical effects.** *distanced*, *has seen it*.

**Signals**
- A generic noun where a specific one exists, at a point of attention — *a tree* where the book's world has a species
- Abstractions stacked — sadness, memory, silence, time — with no sensory anchor
- Description by category: *a typical office*, *an ordinary house*
- Sensory monotony — sight only, chapter after chapter
- Adjectives doing what a precise noun would do alone

**Detection signals** `[pt-BR]`
- `"uma árvore"`, `"um pássaro"`, `"uma flor"` at a point of attention, where `"um ipê"`, `"um sabiá"` exist
- `"um silêncio"`, `"uma tristeza"`, `"uma memória"` as the sentence's only content

**Detection signals** `[en]`
- `"a tree"`, `"a bird"`, `"some flowers"` at a point of attention, where `"a sycamore"`, `"a grackle"` exist
- `"a silence"`, `"a sadness"`, `"a memory"` as the sentence's only content

**Not a finding**
- Generic by design: a fable register, a narrator's indifference to a place, a world where things have lost their names — check `style-guide.md` and `worldbuilding.md`
- A deliberately abstract passage the persona declares

**Default treatment**
- At the point of attention, replace one generic per paragraph with the specific — not every noun
- Anchor the abstraction in one object
- Add one non-visual sense

**Typical level.** Sentence.

---

## 10. Wear

**Definition.** Language, images, and moves the reader has met many times **outside this book** — stock phrases, dead images, genre conventions executed on autopilot.

**Typical effects.** *has seen it*, *ahead*.

**Three kinds**
- **Stock phrases** — the body reacting in the language of every other book
- **Stock images** — rain at the funeral, the protagonist described in a mirror, the chapter that opens with waking up
- **Autopilot conventions** — a genre move executed exactly the way the reader has seen it most often, with nothing turned

**The test: chosen or default?** A convention is a tool. The question is never *is this a trope* but *does the book do something with it* — turn it, specify it, comment on it, or simply execute it better than the reader expects. A convention done by default is wear; the same convention chosen is craft.

**Detection signals** `[pt-BR]`
- `"o coração disparou"`, `"o sangue gelou"`, `"um frio na espinha"`
- `"um silêncio ensurdecedor"`, `"lágrimas rolaram"`
- `"soltou o ar que nem sabia que estava prendendo"`
- `"o tempo parou"`, `"como se o mundo tivesse parado"`

**Detection signals** `[en]`
- `"her heart raced"`, `"his blood ran cold"`, `"a chill ran down her spine"`
- `"a deafening silence"`, `"tears streamed down"`
- `"let out a breath she didn't know she was holding"`
- `"time stood still"`, `"as if the world had stopped"`

**Not a finding**
- What the genre contract requires — the conventions readers of this genre come for
- A phrase in `preserve-list.md`
- A cliché in a character's mouth as characterization — the character who speaks in clichés

**Boundary.** Repetition *inside this book* is `scan-recurrences` and `framework.md` cat. 8; LLM register is cat. 7. Wear is the reader's library, not this manuscript.

**Never invent evidence.** Calling a move common does not require a citation, and must never get a fabricated one — no invented titles, no invented "as in X's novel".

**Default treatment**
- Replace the stock phrase with the specific physical sensation of *this* character
- Keep the convention; turn one element of it
- Cut — the stock phrase usually stands where nothing was needed

**Typical level.** Sentence for phrases and images; scene or book for conventions.

---

## 11. Sentence

**Definition.** Sentences the reader has to read twice for the wrong reason.

**Typical effects.** *lost*, *impatient*.

**Signals**
- **Syntactic ambiguity** — a modifier attaching to the wrong noun
- **Overload** — subordinate stacked on subordinate until the subject is lost
- **Monotonous rhythm** — a run of sentences of the same length and shape
- **Weak verb plus adverb** where a precise verb exists
- **Nominalization chains** — the action buried in nouns
- **Local echo** — the same word twice within a sentence or two, unintentionally (distinct from `framework.md` cat. 8, which measures density across the chapter)

**Detection signals** `[pt-BR]`
- `"Viu o homem com o binóculo"` — who holds the binoculars?
- `"realizou a verificação da documentação"` for *"verificou os papéis"*
- Unintended rhyme and cacophony: `-ão … -ão`, `-mente … -mente` in one sentence

**Detection signals** `[en]`
- `"She saw the man with the binoculars"` — who holds them?
- `"conducted an examination of the documents"` for *"examined the papers"*
- `"walked slowly"` where `"ambled"`, `"trudged"` exist

**Not a finding**
- Syntax the persona declares — long periodic sentences, fragments, run-ons as voice (`persona.md` §2)
- Deliberate difficulty as an effect

**Objective grammar errors** are listed under *Outside this instrument* when noticed, not hunted — that sweep is `review-revision`'s first axis.

**Default treatment**
- Split the sentence; put subject and verb early
- Replace verb-plus-adverb with the precise verb
- Vary length at the point of emphasis — the short sentence lands only after longer ones

**Typical level.** Sentence.

---

## Verdict

The verdict answers *does it work?* — and it is **decided by rule from the findings**, never by impression. A verdict argued from findings can be contested item by item: an `R:` that overturns the deciding finding overturns the verdict, which is exactly the leverage the author should have.

### The load-bearing scene

Before judging, the critique names the chapter's **load-bearing scene**: the one where the chapter's turn happens. If no scene turns, there is no load-bearing scene — and that absence is itself the deciding finding.

### Chapter verdict

| Verdict | `[pt-BR]` | Rule |
|---|---|---|
| **Works** | *Funciona* | No `break` anywhere |
| **Works with reservations** | *Funciona com ressalvas* | At least one `break`, none in the load-bearing scene |
| **Does not work yet** | *Ainda não funciona* | A `break` in the load-bearing scene, **or** the chapter has no turn |

**Frictions never decide the verdict alone.** They are reported by accumulation — "nine frictions, six of them pacing, all in scenes 2 and 3" is often the most useful line in the critique, and it goes first in the priorities. But a chapter with many small frictions and no break *works*; saying otherwise would be the grade sneaking back in.

### Scene and draft verdict

For a single scene — in the manuscript or in a `_draft.md` — the question is narrower: does it fulfil its function in the chapter?

| Verdict | `[pt-BR]` | Rule |
|---|---|---|
| **Fulfils** | *Cumpre* | No `break` |
| **Fulfils in part** | *Cumpre em parte* | A `break`, but not in the scene's own turn |
| **Does not fulfil** | *Não cumpre* | A `break` in its turn, **or** no function — no turn, and not a rest the chapter needs |

---

## Patterns across chapters

Some problems exist only across chapters, the way `framework.md` cat. 13 does. A multi-chapter critique looks for them in its synthesis:

- **Pacing across chapters** — consecutive rest chapters, or every chapter the same weight. Evidence: words per chapter, and each chapter's load-bearing scene share
- **Repeated structural devices** — every chapter opens on waking, closes on a cliffhanger, follows the same scene shape
- **Habit against slip** — the same category *and* mechanism in **three or more chapters** is a habit; fewer is a local slip. Three occurrences make a pattern, one makes an anecdote — the same threshold `consolidate-style` uses
- **The verdict map** — every chapter's verdict and load-bearing scene, side by side

A habit is reported with its chapters and quotes and proposed as one of two things, both for the author to rule on: a **rule** in `style-guide.md` (if the author wants it prevented) or a **declared choice** in `persona.md` §6 (if the author defends it — it then stops being flagged).

**Boundary.** The tension curve of the book and the trajectory of arcs belong to `check-arc`. The synthesis cites its latest report when one exists and never rebuilds it.

---

## How to apply this in a critique

1. **Read as a reader first.** One full read, in order, logging reactions sequentially — where attention held, dropped, got lost, accelerated. **No diagnosis yet.** The log is evidence; diagnosis that comes first contaminates it.
2. **Map the scenes** from the prose — never from `##` headers, which are optional scaffolding. Count words per scene. Mark each scene's conflict and turn. Name the load-bearing scene.
3. **Sweep the 11 categories in order** — structure, sense, execution.
4. For each candidate finding:
   - **Quote literally.**
   - **Check the protections** in precedence order. A protected item is not a finding.
   - **Check the boundaries.** If it belongs to another instrument, route it in one line.
   - **Name the reader effect.** None → drop it.
   - Record mechanism, severity, level, and treatment.
5. **Record what works** — with the same rigor: quote, and the mechanism that makes it work. The author needs to know what revision must not break.
6. **Apply the verdict rule.**
7. **Prioritize** (order below) and **route** each finding by its level.

### Priority order

1. A `break` in the load-bearing scene — or the missing turn
2. Problems at chapter and scene level — they make sentence work premature
3. Other `break`s
4. Frictions clustered in one category or one scene
5. The rest, by reader effect

### Suggested working order

Structure before sense before execution: categories **1–3**, then **4–5**, then **6–11**. And the critique before `analyze-chapter`: counting the markers of prose that is about to be restructured is wasted work.
