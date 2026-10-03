# p10t

**A local hub for writing and revising long-form fiction with an AI agent - voice, craft and consistency, with human curation at its core.**

`p10t` is short for **palimpsest** - the scraped and rewritten manuscript, where the older text still shows through beneath the new. That is exactly what this system does: you write over the machine layer until only your voice remains.

---

## In plain terms

You are writing a book. You want a machine's help without the book ending up sounding like a machine wrote it.

The obvious approach - ask a chatbot to write a chapter, then edit it - fails in a specific way. The machine's fingerprints are not in its word choice, which you would catch. They are in the *shape* of its sentences, repeated across a hundred thousand words until the prose reads smooth and anonymous. You cannot edit that out by hand, because by chapter forty you no longer see it.

p10t attacks that from the other side. It is a set of twenty-three instructions an AI coding agent follows, plus a folder of files describing **your** book: how you write, who your characters are, what your world does not explain. Point it at a chapter and it does not rewrite anything. It hands the chapter back to you **measured** - every suspect construction quoted, counted, and compared against what you have already declared to be your own voice. You rule on each one. Your rulings become permanent, and the next chapter is judged against them.

The unit is `occurrences per 1,000 words`. That matters more than it sounds: an editor tells you a chapter feels overwritten, and you have an opinion to argue with. p10t tells you the figure is 4.5 against a ceiling of 2.0, and it will be the same figure next week.

It also reads the chapter the way an editor does, and asks the question the markers cannot: **does it work?** Does each scene earn its place, does the reader follow, believe, keep turning pages - and where it fails, is the problem in the sentences, the scene, or three chapters upstream? No grades: every finding names what happens to the reader (*lost*, *impatient*, *has seen it*), and the verdict is decided by rule from the findings, so you contest it by contesting a finding.

**Three things it does that a careful human reader cannot:**

- **Catches the sentence you reused in chapters 3, 11 and 24.** Nobody reading a book front to back over two weeks notices this. It is also the single most damaging thing a critical reader can find, because unlike a tic it has no stylistic defence.
- **Holds the continuity contract** - timeline arithmetic, and who knows what *when*, across the whole manuscript.
- **Remembers your decisions.** Protect a phrase once and nothing suggests cutting it again. Human editors forget; a new editor never knew.

**Who it is for:** anyone writing long-form fiction who wants a rigorous second reader that remembers every decision - and, when drafting with an AI agent, would rather the result be theirs. It is a working system, not a demo, and it runs entirely on your machine - plain markdown files in a git repository, no service, no account, nothing uploaded.

> **A note on language.** All instructions, skills, and templates are written in English - the language LLMs handle most reliably, and it keeps the project portable. **Your manuscript and all generated output stay in your language.** Set it in `.project/config/project.yaml`.

---

## The problem

Writing fiction with LLM assistance produces a peculiar result: the structure is yours, the concept is yours, the dramatic decisions are yours - but **the sentences belong to the machine**. And machine sentences have a signature.

It is not a signature of poor quality. It is a signature of *uniformity*: binary antithesis, triads, philosophical hedging, an aphorism closing every paragraph, em-dashes everywhere, emotion named instead of shown. In isolation, each is a legitimate figure of speech. Accumulated across an entire book, they become a mechanical meter that critical readers detect even without being able to name it.

The result is prose that reads as competent and impersonal at the same time. Good enough not to be rejected, generic enough not to be remembered.

**p10t exists to solve this.**

And it is only half the problem. Prose with every marker removed is clean, not good. A chapter can be free of tics and still fail: the scene that changes nothing, the turn summarized in a sentence while the drive to the house takes three pages, the motive the reader stops believing, the exposition that halts the scene at its peak. None of that is a machine signature - hand-written chapters fail the same way - and none of it shows up in a density count. So p10t carries a second instrument, judged rather than counted: eleven craft categories, each finding anchored to a literal quote and a reader effect.

---

## The principle

> The AI proposes. The author decides. The system learns.

Three commitments:

**1. Active human curation, always.**
No stylistic decision is automatic. The system flags, quotes, and suggests - the author responds item by item, marking what they accept, alter, or reject. Every rejection is information: it becomes a permanent rule.

**2. Extract the voice, do not invent it.**
The system does not ask "how do you want to write?". It reads what you have already written, identifies what is yours, and starts defending it. Elevated vocabulary is not a flaw if it is yours. A tic you recognize and want to keep stops being a tic - it becomes a signature.

**3. Preventing beats fixing.**
LLM tics mark sentence *structure*, not just word choice. Rewriting afterwards is cosmetic. The system's endgame is prose that is **born** in the right voice, carrying persona, world, and constraints from the first token.

---

## What p10t is not

Stated up front, because each of these is a fair question to ask of a system like this.

**It is not a way to make generated text pass as human.** This is the serious objection and it deserves a real answer rather than a slogan. The markers p10t removes are markers of *uniformity* - triads, binary antithesis, an aphorism closing every paragraph. Removing them by rewriting in the author's own documented voice makes the prose more theirs, not less. But the honest part: if someone fed it wholly generated text and curated nothing, it would help them polish that text, and no tool can prevent it. What this system does instead is **keep the record**. Every suggestion requires an explicit ruling, every ruling is committed, and the analysis refuses to output a "% human" figure precisely because that number cannot be measured from prose. A system that made the dishonest version easy would not bother with any of that.

**It is not an editor - it has no editorial authority.** It judges: `critique-chapter` will tell you a chapter does not work yet, which scene breaks it, and why. What it will not do is make the call stick. The structural reason is in the first principle: the AI proposes, the author decides. That makes the system trustworthy and it also makes it an instrument you operate - and you cannot be gatekept by a tool you control. A good editor sometimes has to say "you are wrong, cut it" and be believed. p10t never will, and changing that would break the thing that makes it worth using. The honest limit that follows: a finding is only as good as the reading behind it, and the craft categories have not yet been field-tested at book length.

**It does not grade.** No score per chapter, no score per category, no average - for the same reason it refuses a "% human" figure. A grade cannot be measured from prose, a model's grade drifts between runs, and the one problem that sinks a chapter averages away against ten that are fine.

**It is not a publisher.** Publishing houses sell capital, distribution, rights and imprint. Editing is a service they bundle, not the product. p10t touches none of it.

**It is not finished, and it is not widely tested.** The revision cycle - `analyze-chapter` → `R:` → rewrite → `review-revision` - has run on a real manuscript. The generation and knowledge layers have not been exercised at book length. Detection signals are calibrated for `[pt-BR]` and `[en]` only. Expect the ceilings in `framework.md` to move. See the [Roadmap](#roadmap).

---

## Honesty as method

This system does not exist to hide AI use. It exists so that declared use is defensible.

There is a known spectrum:

| Level | Use | Reception |
| --- | --- | --- |
| 1 | AI for brainstorming | Nobody minds |
| 2 | AI for revision | Accepted |
| 3 | AI as drafter with human curation | Legitimate if declared |
| 4 | AI as drafter, passed off as solo authorship | Reputationally risky |
| 5 | AI generating whole books unsupervised | Poorly regarded |

`p10t` is built for **levels 1 to 3, with 3 as the ceiling** - and so that level 3 output is indistinguishable in quality from level 0.

Most use will sit below the ceiling, and that is the intended shape. The analysis and learning layers generate no prose at all: `analyze-chapter`, `review-revision`, `scan-recurrences` and `consolidate-style` read what you wrote and hand it back measured, which is level 2 with nothing to declare beyond having used a tool. Working out a chapter's obligations before writing it is level 1. Only the generation layer reaches level 3, and only when you ask it to.

Levels 4 and 5 are outside the design rather than guarded against. Level 5 has nowhere to put curation, and curation is the entire mechanism. Level 4 is not a technical state but a choice about what you say afterwards - and the system's answer to it is to make the honest version cheap, because by then the record of every decision already exists.

Declaring "I used AI for 40% of this project" is honest. What changes with this system is what those 40% mean: not "40% generated and shipped raw", but "40% generated in intensive collaboration, within a defined voice, reviewed item by item".

---

## Structure

> This diagram is the canonical one. `CLAUDE.md` and `.project/CLAUDE.md` point here rather than repeating it.

```text
{your-book}/
├── CLAUDE.md                    Project guide (read first)
├── manuscript/                  Your chapters in markdown
│   ├── 01.01.md                 flat layout: every chapter file here
│   ├── 01.02.md
│   └── ...                      (chapter layout nests each in 01.01/, 01.02/ — see below)
├── translations/                Optional: one folder per target-language edition
│   └── en-US/                   Contract, locked lexicon, referents, state, prose + reports
├── examples/                    Worked samples of the system's outputs
├── docs/
│   └── export.md                Dependencies and use of the exporter
├── scripts/
│   ├── scene-budget             Per-scene word counts vs. the header budgets
│   ├── validate                 Structural checks over the markdown
│   └── export                   Manuscript to .docx, .epub and .pdf
├── .claude/
│   └── skills/                  ── WHAT THE SYSTEM DOES ──
│       ├── init-project/        critique-chapter/    analyze-chapter/
│       ├── scan-recurrences/    review-revision/     define-persona/
│       ├── define-references/   build-worldbuilding/ create-character/
│       ├── outline-chapter/     draft-scene/         revise-passage/
│       ├── expand-beat/         restructure-chapter/ review-book/
│       ├── check-consistency/   check-arc/           update-preserve-list/
│       ├── consolidate-style/
│       ├── define-localization/ translate-chapter/
│       └── review-translation/
└── .project/
    ├── CLAUDE.md                Knowledge hub guide
    │
    ├── config/                  ── WHO YOU ARE ──
    │   ├── persona.md           Your voice: vocabulary, signatures, tone
    │   ├── references.md        Reference authors and works
    │   ├── style-guide.md       Hard rules for this project
    │   ├── export.yaml          Export profiles and typography
    │   └── project.yaml         Metadata (including output language)
    │
    ├── knowledge/               ── WHAT EXISTS IN THE BOOK ──
    │   ├── worldbuilding.md
    │   ├── timeline.md
    │   ├── glossary.md
    │   └── characters/          One sheet per character
    │
    ├── reports/                 ── WHAT HAS BEEN FOUND ──
    │   ├── technical/           Per-chapter analyses
    │   ├── literary/            Whole-book reports
    │   ├── preserve-list.md     Untouchable phrases
    │   ├── recurrences.md       Duplication map
    │   └── revision-log.md      Decision history
    │
    └── templates/               ── REUSABLE SKELETONS ──
        ├── framework.md         The 14 tic categories
        ├── craft.md             The 11 craft categories and the verdict rule
        ├── source.md            Where the prose lives: local files or a connected app
        ├── layout.md            How skills resolve and order chapter files
        ├── localization.md      How a target-language edition is laid out and decided
        ├── export/              Optional hand-written export templates
        ├── chapter-analysis.md
        ├── chapter-critique.md
        ├── chapter-outline.md
        ├── persona-template.md
        ├── book-review.md
        └── character.md
```

The split is deliberate: **`.claude/skills/` is what the system does** (machinery - identical across all books), **`.project/` is what the system knows** (this book's voice, world, and decisions). Behaviour in one place, state in the other.

**Portability.** Both directories copy to another book. Skills and `templates/` are generic; `config/`, `knowledge/`, and `reports/` are project-specific and get repopulated each time.

### Manuscript layout

Chapter files are arranged one of two ways, declared in `project.yaml → paths.layout`:

```text
flat                          chapter
manuscript/                   manuscript/
├── 01.01.md                  ├── 01.01/
├── 01.01_outline.md          │   ├── 01.01.md
├── 01.01_analysis.md         │   ├── 01.01_outline.md
├── 01.02.md                  │   └── 01.01_analysis.md
└── 01.02_analysis.md         └── 01.02/
                                  ├── 01.02.md
                                  └── 01.02_analysis.md
```

`flat` is right below ~15 chapters. `chapter` earns itself when each chapter carries an outline, an analysis, and a draft — a 32-chapter book is otherwise ~130 files in one directory.

Three properties make this cheap:

- **The chapter file repeats its id** (`01.01/01.01.md`, never `01.01/chapter.md`), so migration is a pure move, `git log --follow` survives, and the sort key is the same in both layouts.
- **The id carries the act**, so "review Act 2" is a string comparison in either layout. That is why there is no third, per-act layout — it would duplicate what the id already holds.
- **Layout and `paths.analyses` are independent axes.** All four combinations are legal.

It is **declared, never detected**: `manuscript/01/` is unresolvable without opening it, and a half-migrated tree reads as valid. A wrong guess does not fail — it silently returns a partial chapter list, and the sweep that follows reports "no duplication found" for chapters it never read.

Full rules — resolution, ordering, satellites, mixed-state handling, migration: **`.project/templates/layout.md`**.

### Manuscript source

By default the manuscript is the markdown files above. A book can instead live in a writing app and be **read through an MCP connector** - set `project.yaml → source.kind: mcp`. This is **experimental**: the first adapter is for proseyard, and it has not yet carried a chapter through the full cycle.

What changes, and what does not:

- **p10t never writes to the app.** It connects with read scope; analyses, critiques, plans, drafts and every `.project/` file stay local and in git.
- **The app's node id is the key**, and `02.03` is a display label derived from the outline. Reordering chapters in the app is detected and reported, never followed silently.
- **Content hashes replace `git log`** for "has this chapter changed since its critique?".
- **A snapshot replaces the pre-rewrite commit.** You snapshot the chapter in the app before rewriting; `review-revision` finds it by hash. When it cannot - you fixed a typo first, or deleted the snapshot - it uses an approximate baseline or the literal quotes, and says which.
- **No scaffolding.** An app-held body is exactly what prints, so every line counts; scene nodes are your divisions, and dramatic scenes inside them are numbered from the prose.
- **`scripts/export` refuses** - the app compiles its own manuscript.

Rules, the contract a source must satisfy, and the adapter's tool mapping: **`.project/templates/source.md`**.

**Tool independence.** Skills are plain markdown with YAML frontmatter. Claude Code discovers them natively; any other AI agent with filesystem access can read and execute them - the root `CLAUDE.md` says where they live.

---

## The 14 categories

The technical core. Each has a definition, detection signals, and default treatment in `templates/framework.md`.

| # | Category | Why it is a tic |
| --- | --- | --- |
| 1 | **Binary antithesis** (`Not X. Y.`) | Cheap parallelism that simulates depth |
| 2 | **Triads and parallel lists** | Anglophone pattern over-represented in training |
| 3 | **Philosophical hedging** (`maybe X, maybe Y`) | Model thinking aloud as performance |
| 4 | **Ironic meta-commentary** | Generating text without committing to the scene |
| 5 | **Paragraph-closing aphorism** | A pleasing move, repeated too often |
| 6 | **Serial comparisons** (`Like X. Like Y.`) | Effective once, formulaic in sequence |
| 7 | **Anglicized vocabulary** | Calques of modern English (*performance*, *interface*) |
| 8 | **Lexical repetition** | Consistency is safer than variation |
| 9 | **Symmetrical ping-pong dialogue** | Replies mirrored in identical meter |
| 10 | **Negation lists** (`No X, no Y, no Z`) | Among the most identifiable markers |
| 11 | **Em-dash overuse** | Anglophone punctuation habits |
| 12 | **Rhythmic summaries** (`I did X. I did Y.`) | Becomes a mantra when repeated |
| 13 | **Single-line chapter endings** | Tired when *every* chapter closes this way |
| 14 | **Named emotion** | Naming instead of showing solves the task too quickly |

Plus an open category (**15 - other tics**) capturing whatever is specific to each work: caps lock for emphasis, misplaced erudite references, invented proverbs, phrases recycled across chapters.

**None of this is an error.** These are legitimate figures. The problem is always density - and density only becomes visible when you count.

**The unit is occurrences per 1,000 words.** One figure, used everywhere: the per-chapter analysis, the before/after of each revision, the budget a generation pass drafts against, the trajectory in the whole-book report. Each category carries a default ceiling; your project overrides them in `style-guide.md`, and anything you have declared a personal signature has no ceiling at all. Counting rules are in `templates/framework.md` - they matter, because a density figure counted two different ways compares nothing.

---

## The 11 craft categories

The second instrument. Where the 14 categories count what generation leaves in prose, these judge whether the narrative works - whoever wrote it. Definitions, signals, protections and treatments in `.project/templates/craft.md`.

| Group | # | Category | The reader... |
| --- | --- | --- | --- |
| **Structure** | 1 | **Scene function** | ...cannot say what would be missing if the scene were cut |
| | 2 | **Pacing** | ...gets pages of transit and one sentence of the turn |
| | 3 | **Tension and the dramatic question** | ...carries no question into the next page |
| **Sense** | 4 | **Clarity and orientation** | ...loses who is speaking, where, when |
| | 5 | **Logic, motivation and agency** | ...asks "why don't they just...?" |
| **Execution** | 6 | **Exposition** | ...is told what the scene already showed |
| | 7 | **Point of view and distance** | ...is handed knowledge the POV could not have |
| | 8 | **Dialogue** | ...could swap the speakers and not notice |
| | 9 | **Concreteness** | ...meets *a tree* where the world has a species |
| | 10 | **Wear** | ...recognizes the phrase or the move before it completes |
| | 11 | **Sentence** | ...reads it twice for the wrong reason |

**Every finding carries a reader effect** from a closed list - *lost*, *disbelieves*, *impatient*, *indifferent*, *has seen it*, *distanced*, *ahead*, *told twice*. A finding with none is a preference and is dropped. It also carries a **severity** (*break*, *friction*, *note*) and a **level** - sentence, scene, chapter or book - which says where the fix lives and which skill takes it.

**The verdict is decided by rule.** *Works*: no break. *Works with reservations*: breaks, but none in the scene where the chapter turns. *Does not work yet*: a break in that scene, or no turn at all. Frictions never decide it alone.

**Your decisions win.** What `worldbuilding.md` keeps deliberately unexplained is never a clarity finding; a pace or a narrator your persona declares is never flagged for being that choice; what the genre requires is never wear.

---

## The skills

Twenty-three skills: `init-project` for bootstrap, `commit` for the history, and twenty-one across seven working layers. Each is a `SKILL.md` the agent reads and follows - no runtime, no dependencies.

**`commit`** - Writes a commit using the convention below: infers the type and scope from what changed, proposes one line, and commits only after you approve it. Warns before moving the boundary `review-revision` depends on. It is the only skill that touches git, it runs only when you ask, and no other skill may invoke it.

### Analysis layer

**`critique-chapter`** - Reads a chapter as an editor would and answers *does it work?* across the 11 craft categories. A reader's log first, written before any diagnosis; then a scene map with real word counts, the scene where the chapter turns, and every finding with its quote, reader effect, severity and level. Strengths get the same rigor - what revision must not break. Scopes: one scene (judged inside its chapter), a chapter, a `_draft.md`, a range, an Act, or the book - multi-chapter runs critique each chapter, reuse critiques the chapter has not outgrown, and add a synthesis of what only shows across chapters: pacing between chapters, repeated openings and exits, and habits (the same problem in three or more chapters). Never rewrites; routes each finding to the skill that fixes it.

**`analyze-chapter`** - Reads one chapter and produces `{chapter}_analysis.md`: all 14 categories, occurrence by occurrence, with literal quotes and suggested treatment. Cross-references the preserve list (never suggests cutting thesis phrases) and the recurrence map (flags duplications as high priority). Closes with a verdict: top priorities, untouchables, time estimate.

**`scan-recurrences`** - Sweeps the whole book for what repeats across chapters. Distinguishes **intentional recurrence** (a motif stitching the work) from **accidental duplication** (the same aphorism recycled). The test: *if the reader notices, will they think "how lovely, it came back" or "I've read this already"?*

**`review-revision`** - Closes the loop. After you revise a chapter, evaluates the result across six axes: introduced errors, rewrite quality, inverted problems (over-correcting into the opposite flaw), residual density, continuity gaps, and - when the chapter had a critique - which craft findings were resolved and how the verdict moved. Answers, explicitly, any questions you left in your annotations.

### Foundation layer

**`define-persona`** - Builds `config/persona.md`, the foundation of everything. Not a questionnaire: reads your corpus, extracts hypotheses about your voice, and interviews you to refine. The persona is extracted, not invented.

**`define-references`** - Turns "I love Murakami" into borrowing instructions a generation pass can follow: what exactly to take, what explicitly NOT to take, where it shows up. The NOT list prevents pastiche.

### Knowledge layer

**`build-worldbuilding`** - The world as a **consistency contract, not an encyclopaedia**. Every rule needs what it makes possible, what it costs, and who knows it. Includes the deliberately-unexplained list - mysteries no generation pass may accidentally solve. Modes: extract (from manuscript) or create (dialogue).

**`create-character`** - Character sheets that keep characters *writable*: voice first (verbatim sample lines), consistency rules second, the want/need/fear/lie engine third. Detects voice drift across a long manuscript. Modes: extract or create.

### Generation layer

**`outline-chapter`** - The chapter as **obligations, not summary**: debt to pay, seeds to plant, and protections - what must NOT happen. The validated outline is the contract drafting executes against.

**`draft-scene`** - The critical piece. Loads *everything* (persona, references, world, characters, preserve list, recurrence blocklist, the 14 categories as negative constraints), drafts against the contract, **self-audits against the project's own analysis before you ever see it**, and delivers with honest notes on every interpretive choice. The draft is a proposal; the metric is how much survives your curation.

**`revise-passage`** - Surgical rewriting of existing text. Diagnoses before cutting, preserves every word of yours that can stay, presents as annotated comparison. If the passage is fine, says so.

**`expand-beat`** - From a one-line beat to drafted prose. The beat is your plot decision; expansion adds texture, never events.

**`restructure-chapter`** - For chapters whose problem is scene design, not sentences. Rebuilds the chapter's obligations backwards from what is on the page, then proposes what to move, merge, compress, cut, or add - naming, for every cut, which surviving scene carries its load. Delivers a plan against the current structure, never a rewrite, and reports the blast radius: restructuring is the one operation that routinely breaks *other* chapters.

### Literary analysis layer

**`review-book`** - The whole-book report: literary, commercial, and AI-use analysis, every claim with evidence. Run at the end of each Act, not just at the end.

**`check-consistency`** - Chapters against world rules, timeline math, character invariants, and knowledge states (who knows what, when). Flags only real contradictions, with citations from both sides. Never resolves silently.

**`check-arc`** - Maps character trajectories, thematic development, and the tension curve **from beats on the page**, then compares against intent. Finds flat stretches, rushed turns, abandoned threads, unearned endings.

### Learning layer

**`update-preserve-list`** - Harvests your protection decisions from annotations into the preserve list, and retires entries whose phrases were cut. Proposes in batch; never promotes silently.

**`consolidate-style`** - Reads the accumulated decision history, finds patterns (three occurrences make a pattern; one makes an anecdote), and proposes evidence-backed persona updates. The mechanism by which the system genuinely learns your voice.

### Localization layer

Optional, and **additive**: it modifies no other skill and no existing `.project/` file. Delete `translations/` and p10t is exactly as it was. Layout, formats and rules: [`.project/templates/localization.md`](.project/templates/localization.md).

**`define-localization`** - The crossing contract for one target language, written once, before a single line is translated. Every rule in your style guide and every signature in your persona gets **one of three verdicts**: crosses intact, crosses with another tool (named), or does not cross (replacement declared). There is no fourth. The reason this exists: a *faithful* translation can break the book's own rules while being correct - a cap on how often characters are named, held in place by Portuguese's null subject, has no mechanism left in English, where every clause needs a subject. Also carries the typographic profile, the target language's own AI-tic watchlist, and this edition's AI declaration, which is **not** the source's.

**`translate-chapter`** - Transcreation under the contract: **where the source sentence and a book rule collide, the rule wins and the sentence is rebuilt**. Hard-stops on any term whose target form is still open - designations and thesis words appear in every chapter, so a hurried choice costs the whole edition. Produces two files: the prose, and a report **in your language** arguing every non-obvious choice. If you cannot judge literary prose in the target language, the report is the deliverable and the prose is the attachment.

**`review-translation`** - Blind back-translation first, before the source is loaded, so meaning drift shows up instead of being reproduced. Then contract compliance, a tic sweep against the target watchlist, locked-pair consistency, and staleness against the source commit. It hunts *additions* hardest - the characteristic failure of a generated translation is not error but helpfulness: filling an ellipsis, resolving an ambiguity the book kept open. It never clears the native-reader gate; only a human does that.

**The setting never moves.** A French edition of a book set in the United States keeps the county, the feds, the sycamore - it says *comté*, *platane d'Occident*. Translation changes the language, never the map.

---

## The workflow

```text
   ┌──────────────────────────────────────────────┐
   │                                              │
   ▼                                              │
[1] critique-chapter                              │
   │  {chapter}_critique.md - does it work?       │
   │  (scene-level problems: restructure first)   │
   ▼                                              │
[2] analyze-chapter                               │
   │  {chapter}_analysis.md - what marks remain?  │
   ▼                                              │
[3] you read and annotate R: on each item         │
   │  accepted / changed / kept / removed         │
   ▼                                              │
[4] git commit the chapter, then rewrite it       │
   │  the commit is what review-revision diffs    │
   ▼                                              │
[5] review-revision                               │
   │  evaluates, flags errors, answers questions  │
   │  writes the entry in revision-log.md         │
   ▼                                              │
[6] learnings feed back into                      │
   │  persona.md  +  preserve-list.md             │
   └──────────────────────────────────────────────┘

   End of each Act: scan-recurrences, check-consistency,
                    check-arc, critique-chapter over the Act,
                    review-book
```

**Craft before markers.** When the critique says the problem is a scene and not its sentences, restructure before you analyze - counting the tics of prose you are about to cut is wasted work. Either step can be skipped; `review-revision` works with whichever file exists.

**Commit before you rewrite.** One `git commit` between step 3 and step 4 gives `review-revision` an exact diff of what changed instead of a reconstruction from quotes. It is the cheapest habit in the system. When the book lives in an app (`source.kind: mcp`), the same habit is a snapshot of the chapter taken in the app.

**The revision log is not optional.** Step 4 always writes an entry to `reports/revision-log.md` - `consolidate-style`, `update-preserve-list`, and `define-persona`'s update mode all read it as their source. A skipped entry is a set of decisions that never reaches your persona, and the loop stops compounding without telling you.

**The `R:` annotation is the heart of the system.** It is where human curation happens and where the system learns. A real example (author writing in Portuguese):

```markdown
6. **"Depois de (muitos) anos nesse trabalho"** - The parenthetical
   "(muitos)" is a strong LLM tic. Remove the parenthesis.
   **R:** removi o (muitos)

7. **"Boa pergunta. Quase boa demais."** - Strong tic. Rewrite.
   **R:** troquei para "Excelente pergunta"

8. **"aliás, onde estão as crianças?"** - Self-interruption. Tic.
   **R:** por hora mantive, gostei. É um tique forte?
```

Item 8 produces two things: a direct answer in the next review, and - if confirmed as a signature - a permanent entry in `persona.md` that stops future analyses from flagging it.

---

## Commits

The commit is a working part of this system, not a record of it - step 4 above is what step 5 compares against. So the log deserves a vocabulary, and the one for code does not fit a novel.

```
type(scope)!: subject
```

Scope is optional - a chapter number, or a knowledge area. The `!` is optional and means **this invalidates text already written**, so that `git log --grep "!"` returns everything that requires going back. One line: no body, no footer.

| Family | Types | |
|---|---|---|
| **Manuscript** | `draft` | material that did not exist before - new prose, and generated proposals awaiting curation |
| | `revise` | changing prose that already exists, from a sentence to the order of the scenes |
| | `cut` | material removed and parked in `_drafts.md` |
| **Curation** | `annotate` | your `R:` rulings on an analysis or critique file |
| | `rule` | a world, character or timeline decision |
| | `voice` | persona, style guide, references, preserve list |
| **Machine** | `analyze` | `analyze-chapter`, `critique-chapter`, `scan-recurrences` |
| | `review` | `review-book`, `review-revision`, `check-consistency`, `check-arc`, and the revision log entry |
| **Apparatus** | `chore` | renames, lint, file moves, plumbing |
| | `docs` | README, CLAUDE.md - the project describing itself |

```
revise(02.05): tighten the arrival of the second crossing
annotate(01.03): rule on the Waiting Room findings
rule(world)!: reversal edits, crossing inserts
cut(02.05): park the Vera diagnosis
```

**Messages are in English, always** - even when the book is not. The types are the same vocabulary the skills use internally, and the log stays readable across projects. It is the one place where the project's output language does not apply.

**No skill commits on its own.** Skills may suggest a commit line in their closing output; only `commit` writes to git, and only when you ask. A commit is an assertion of authorship, and the log is the evidence base for the AI-use section of `review-book` - a history the machine writes about itself is self-reporting.

**Never stage what the message does not describe.** This is the rule that protects the workflow, and it applies to you as much as to the tool. `review-revision` compares against the commit you made before rewriting; a `git add -A` in the middle of a rewrite sweeps half the new chapter into that baseline, and the comparison then reports on the remainder as though the rest had never been done. Nothing errors - a smaller diff is a valid diff - so the report comes back thin and reads as *I did less than I thought* rather than *the tool measured the wrong thing*. Since `review-revision` writes the revision log, and the log is what `consolidate-style` and `define-persona` learn from, the mistake compounds quietly. `commit` checks for that state and warns before committing.

**Two conventions, one boundary.** A book repository is cloned from p10t, so it inherits p10t's own commits, which use Conventional Commits - p10t is software, with SemVer and a changelog. Commits before `init-project` belong to p10t; commits after it belong to the book. `docs` and `chore` mean the same thing in both, so the overlap is harmless.

There is no hook and no linter. A writing tool that rejects a commit at 2 a.m. because you typed `edit` instead of `revise` is a tool you will route around.

---

## The two files that make it work

### `reports/preserve-list.md`

Phrases that must **never** be flagged as tics, even when they structurally resemble one. These carry the book: character mottos, deliberate recurring images, pivotal lines.

Without this file, the system would suggest cutting the mantra that holds a character together, simply because it repeats. With it, the analysis arrives marked **(PRESERVE - thesis)**.

### `reports/recurrences.md`

The cross-chapter duplication map. It is the most damaging finding an analysis can produce, because it has no stylistic defence: a human author may have tics, but rarely repeats the same striking sentence three times without noticing.

Chapter-by-chapter analysis is blind to this. Only a global sweep sees it.

---

## Export

When the prose is ready, `scripts/export` turns the manuscript into the three files you actually send.

```sh
scripts/export --profile submission   # .docx + .pdf
scripts/export --profile reading      # .epub + .pdf
```

| Output | For | Requires |
|---|---|---|
| `.docx` | agents and publishers — it is what they ask for, because PDF cannot be annotated | pandoc |
| `.epub` | beta readers — it reflows, so it fits a phone | pandoc |
| `.pdf` | print, or a fixed artifact | pandoc + [typst](https://typst.app) |

pandoc is one installer on all three platforms; typst is one self-contained binary and **no LaTeX is involved**, whatever pandoc's own install page says. Without typst the other formats are still written and the PDF is skipped with a note. **Nothing else in p10t depends on this** — delete the script and every skill still works. Under an `mcp` source it refuses and points you to the app's own compile.

The `submission` profile is standard manuscript format: 12 pt, double spaced, one-inch margins, ragged right and unhyphenated, chapters on new pages, a `Surname / Title / page` running head, and a title page with the rounded word count.

**It refuses rather than cleans.** Only a title, paragraphs, and scene headers are accepted; a table, a list, a `{ }` placeholder or an HTML comment refuses that chapter by name and line, and exports the rest. Scaffolding is not dirt to be stripped — it is the signal that the chapter is still a plan, and a chapter exported down to its four surviving lines would be worse than one left out. The absence of scene headers stays a choice, and is never reported.

Dependencies, configuration, profiles, and the template escape hatch: **[`docs/export.md`](docs/export.md)**.

---

## Checks

A system made entirely of markdown has no compiler. A skill naming a template that was renamed, a frontmatter name that drifted from its directory, a skill count in the README that nobody updated - none of these fail loudly. They produce an agent that reads a file which is not there and carries on.

```sh
scripts/validate      # five structural checks, no dependencies, one second
```

| Check | Catches |
|---|---|
| frontmatter | a skill whose `name:` no longer matches its directory, or has no description |
| counts | prose saying "nineteen skills" when there are twenty-three |
| paths | a machinery path named in the docs that does not exist |
| skill-refs | a slash-command trigger, or a relationship table, naming an unimplemented skill |
| placeholders | `{blanks}` left in config after `init-project` |

Paths under `manuscript/` and `translations/` are yours and are never checked; a changelog may name paths that were correctly removed; a check that does not apply to the repository's state is **skipped with a reason**, and a skip is never a failure.

`.github/workflows/ci.yml` runs `validate` plus the test suite on Python 3.9, 3.11 and 3.13. It installs pandoc, because the exporter's end-to-end tests are guarded by `skipUnless(pandoc)` and would otherwise skip while the suite still reported OK - and it then **fails if any test skipped at all**, so coverage cannot erode quietly behind a green tick.

There is nothing to deploy - p10t is a repository you copy - so `release.yml` is the whole of delivery: on a `v*` tag it re-runs the checks and cuts a GitHub Release whose notes are the matching `CHANGELOG.md` section, refusing rather than publishing empty notes.

---

## Starting a new book

1. **Copy this repository** into the book folder.
2. **Run `init-project`** - a seven-question interview configures `project.yaml` (including your output language), resets the project-specific files, and routes you to the right starting sequence. It never resets an active project and never wipes leftover content silently.
3. **Place your manuscript** in `manuscript/`, markdown, one file per chapter (or point `init-project` at an existing folder).
4. **Run `define-persona`.** If you have earlier writing produced without AI assistance, point to it - it is the most valuable corpus available.
5. **Fill `references.md`** with the authors informing this book's voice.
6. **Run `critique-chapter`, then `analyze-chapter`,** on the first chapter and start the cycle.

> **Tip:** begin with the chapter you consider most *yours*. It establishes the baseline for what is voice and what is noise - and becomes the tonal model for the rest.

---

## Roadmap

All twenty-three skills described above are implemented. What is not yet built:

**Language coverage.** Detection signals are calibrated for `[pt-BR]` and `[en]`. Other languages inherit the definitions, ceilings, and treatments, but their signals need adapting - `[es]` and `[fr]` sections are the next addition. This is `framework.md`, which reads the *source* language; a target edition uses its own watchlist, written per language by `define-localization`.

**A field-tested localization contract.** The three verdicts, the hard stop on open terms, and the back-translation check are designed but have not yet produced a full edition. The first real translation is expected to move them - most likely by showing which typographic conversions are mechanical enough to compile into `scripts/` instead of asking a model to apply them.

**Field testing.** The revision cycle - `analyze-chapter` → `R:` → rewrite → `review-revision` - has run on a real manuscript. The generation and knowledge layers have not been exercised at book length. Expect the ceilings in `framework.md` to move once they are.

**A field-tested craft critique.** `critique-chapter` and the 11 categories in `craft.md` are designed but have not yet run on a real manuscript. The first critiques are expected to move the signals, the reader-effect list, and where the line between *break* and *friction* falls. There is no worked example in `examples/` yet, deliberately: the samples there come from real sessions, and a constructed critique presented beside them would not be.

**Craft in the generation layer.** `draft-scene`, `expand-beat`, `revise-passage` and `outline-chapter` do not yet load `craft.md`. Preventing beats fixing, so they should - after the critique has been calibrated on real chapters, not before.

**A field-tested app source.** `source.kind: mcp` and its proseyard adapter are designed against a contract both sides agreed - content hashes per scene, snapshots readable by node id - but the hash and snapshot tools are still being built on the app side, and no chapter has yet gone analysis → snapshot → rewrite → review through it. Until then, fingerprints and baselines degrade to node ids and literal quotes, and the skill reports say so.

**An `export-manuscript` skill.** `scripts/export` already does the work (see below); a skill would read its refusals aloud and offer to fix them. Deferred until the script has been used on a real submission.

---

## Project notes

**Plain markdown, git-versioned.** No proprietary format, no lock-in. The manuscript is text; the knowledge about the manuscript is text; the skills are text.

**Native discovery, still portable.** Skills live in `.claude/skills/` with YAML frontmatter - Claude Code discovers and triggers them automatically. For any other agent, they are ordinary markdown files: the root `CLAUDE.md` says where they live and how to follow them. Moving away from Claude Code would be a folder rename, not a rewrite.

**The system improves over time.** The first chapter analyzed needs heavy manual correction. The tenth needs little - because `persona.md`, `preserve-list.md`, and `recurrences.md` have accumulated real knowledge about the work and the author.
