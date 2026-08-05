# p10t

**A local hub for AI-assisted writing, with human curation at its core.**

`p10t` is short for **palimpsest** - the scraped and rewritten manuscript, where the older text still shows through beneath the new. That is exactly what this system does: you write over the machine layer until only your voice remains.

> **Note on the system language.** All instructions, skills, and templates are written in English - this is the language LLMs handle most reliably, and it keeps the project portable. **Your manuscript and all generated output stay in your language.** Set it in `.project/config/project.yaml`.

---

## The problem

Writing fiction with LLM assistance produces a peculiar result: the structure is yours, the concept is yours, the dramatic decisions are yours - but **the sentences belong to the machine**. And machine sentences have a signature.

It is not a signature of poor quality. It is a signature of *uniformity*: binary antithesis, triads, philosophical hedging, an aphorism closing every paragraph, em-dashes everywhere, emotion named instead of shown. In isolation, each is a legitimate figure of speech. Accumulated across an entire book, they become a mechanical meter that critical readers detect even without being able to name it.

The result is prose that reads as competent and impersonal at the same time. Good enough not to be rejected, generic enough not to be remembered.

**p10t exists to solve this.**

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
├── examples/                    Worked samples of the system's outputs
├── scripts/
│   └── scene-budget             Per-scene word counts vs. the header budgets
├── .claude/
│   └── skills/                  ── WHAT THE SYSTEM DOES ──
│       ├── init-project/        analyze-chapter/     scan-recurrences/
│       ├── review-revision/     define-persona/      define-references/
│       ├── build-worldbuilding/ create-character/    outline-chapter/
│       ├── draft-scene/         revise-passage/      expand-beat/
│       ├── restructure-chapter/ review-book/         check-consistency/
│       ├── check-arc/           update-preserve-list/
│       └── consolidate-style/
└── .project/
    ├── CLAUDE.md                Knowledge hub guide
    │
    ├── config/                  ── WHO YOU ARE ──
    │   ├── persona.md           Your voice: vocabulary, signatures, tone
    │   ├── references.md        Reference authors and works
    │   ├── style-guide.md       Hard rules for this project
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
        ├── layout.md            How skills resolve and order chapter files
        ├── chapter-analysis.md
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

## The skills

Nineteen skills: `init-project` for bootstrap, `commit` for the history, and seventeen across six working layers. Each is a `SKILL.md` the agent reads and follows - no runtime, no dependencies.

**`commit`** - Writes a commit using the convention below: infers the type and scope from what changed, proposes one line, and commits only after you approve it. Warns before moving the boundary `review-revision` depends on. It is the only skill that touches git, it runs only when you ask, and no other skill may invoke it.

### Analysis layer

**`analyze-chapter`** - Reads one chapter and produces `{chapter}_analysis.md`: all 14 categories, occurrence by occurrence, with literal quotes and suggested treatment. Cross-references the preserve list (never suggests cutting thesis phrases) and the recurrence map (flags duplications as high priority). Closes with a verdict: top priorities, untouchables, time estimate.

**`scan-recurrences`** - Sweeps the whole book for what repeats across chapters. Distinguishes **intentional recurrence** (a motif stitching the work) from **accidental duplication** (the same aphorism recycled). The test: *if the reader notices, will they think "how lovely, it came back" or "I've read this already"?*

**`review-revision`** - Closes the loop. After you revise a chapter, evaluates the result across five axes: introduced errors, rewrite quality, inverted problems (over-correcting into the opposite flaw), residual density, continuity gaps. Answers, explicitly, any questions you left in your annotations.

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

---

## The workflow

```text
   ┌──────────────────────────────────────────────┐
   │                                              │
   ▼                                              │
[1] analyze-chapter                               │
   │  produces {chapter}_analysis.md              │
   ▼                                              │
[2] you read and annotate R: on each item         │
   │  accepted / changed / kept / removed         │
   ▼                                              │
[3] git commit the chapter, then rewrite it       │
   │  the commit is what review-revision diffs    │
   ▼                                              │
[4] review-revision                               │
   │  evaluates, flags errors, answers questions  │
   │  writes the entry in revision-log.md         │
   ▼                                              │
[5] learnings feed back into                      │
   │  persona.md  +  preserve-list.md             │
   └──────────────────────────────────────────────┘

   End of each Act: scan-recurrences, check-consistency,
                    check-arc, review-book
```

**Commit before you rewrite.** One `git commit` between step 2 and step 3 gives `review-revision` an exact diff of what changed instead of a reconstruction from quotes. It is the cheapest habit in the system.

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

The commit is a working part of this system, not a record of it - step 3 above is what step 4 compares against. So the log deserves a vocabulary, and the one for code does not fit a novel.

```
type(scope)!: subject
```

Scope is optional - a chapter number, or a knowledge area. The `!` is optional and means **this invalidates text already written**, so that `git log --grep "!"` returns everything that requires going back. One line: no body, no footer.

| Family | Types | |
|---|---|---|
| **Manuscript** | `draft` | material that did not exist before - new prose, and generated proposals awaiting curation |
| | `revise` | changing prose that already exists, from a sentence to the order of the scenes |
| | `cut` | material removed and parked in `_drafts.md` |
| **Curation** | `annotate` | your `R:` rulings on an analysis file |
| | `rule` | a world, character or timeline decision |
| | `voice` | persona, style guide, references, preserve list |
| **Machine** | `analyze` | `analyze-chapter`, `scan-recurrences` |
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

## Starting a new book

1. **Copy this repository** into the book folder.
2. **Run `init-project`** - a seven-question interview configures `project.yaml` (including your output language), resets the project-specific files, and routes you to the right starting sequence. It never resets an active project and never wipes leftover content silently.
3. **Place your manuscript** in `manuscript/`, markdown, one file per chapter (or point `init-project` at an existing folder).
4. **Run `define-persona`.** If you have earlier writing produced without AI assistance, point to it - it is the most valuable corpus available.
5. **Fill `references.md`** with the authors informing this book's voice.
6. **Run `analyze-chapter`** on the first chapter and start the cycle.

> **Tip:** begin with the chapter you consider most *yours*. It establishes the baseline for what is voice and what is noise - and becomes the tonal model for the rest.

---

## Roadmap

All nineteen skills described above are implemented. What is not yet built:

**Language coverage.** Detection signals are calibrated for `[pt-BR]` and `[en]`. Other languages inherit the definitions, ceilings, and treatments, but their signals need adapting - `[es]` and `[fr]` sections are the next addition.

**Field testing.** The revision cycle - `analyze-chapter` → `R:` → rewrite → `review-revision` - has run on a real manuscript. The generation and knowledge layers have not been exercised at book length. Expect the ceilings in `framework.md` to move once they are.

**A validation script.** Frontmatter names against directory names, unfilled `{placeholders}` after init, dangling cross-references between skills. Cheap insurance for a system made entirely of markdown.

**Export.** Manuscript to submission format. Deliberately last: nothing about it is interesting until the prose is done.

---

## Project notes

**Plain markdown, git-versioned.** No proprietary format, no lock-in. The manuscript is text; the knowledge about the manuscript is text; the skills are text.

**Native discovery, still portable.** Skills live in `.claude/skills/` with YAML frontmatter - Claude Code discovers and triggers them automatically. For any other agent, they are ordinary markdown files: the root `CLAUDE.md` says where they live and how to follow them. Moving away from Claude Code would be a folder rename, not a rewrite.

**The system improves over time.** The first chapter analyzed needs heavy manual correction. The tenth needs little - because `persona.md`, `preserve-list.md`, and `recurrences.md` have accumulated real knowledge about the work and the author.
