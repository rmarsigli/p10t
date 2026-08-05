# Changelog

All notable changes to p10t are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/); versioning follows [SemVer](https://semver.org/).

## [Unreleased]

### Added

- **A declared manuscript layout, and `templates/layout.md` as the single resolver for it.** Chapter files can now be arranged `flat` (`manuscript/01.01.md`) or `chapter` (`manuscript/01.01/01.01.md`), set in `project.yaml → paths.layout`. The audit that prompted this found the skills already almost layout-agnostic — not one hardcoded glob in the set, every path reference either a name pattern (`{chapter}_analysis.md`), a relative position ("next to the chapter"), or the existing `paths.analyses` field. What was missing was never decoupling; it was that **no skill knew how to enumerate chapters**, so enumeration and reading order lived in the agent's instinct rather than on the page. `layout.md` now fixes resolution, ordering, satellite ownership, act scoping, mixed-state handling, and migration in one file that four skills cite by name — the same pattern `framework.md` already uses for density.
- **The chapter file repeats its id inside its own directory** — `01.01/01.01.md`, never `01.01/chapter.md`. This buys three properties: migration between layouts is a pure move so `git log --follow` survives it, grep output and editor tabs stay unambiguous without their parent directory, and the sort key is identical in both layouts so ordering has one code path. Directory names are the full id for the same reason a bare number fails: chapter 1 of act 1 and chapter 1 of act 2 would both claim `01/`.
- **No per-act layout, deliberately.** The chapter id already carries the act, so "review Act 2" resolves as a string comparison in either layout. A directory layer grouping acts would duplicate information the id holds, and duplicated information drifts. Documented as a decision rather than an omission.
- **Layout is declared, never detected.** `manuscript/01/` is unresolvable without opening it, a half-finished migration reads as a valid layout, and a stray `_draft.md` in the manuscript root reads as a chapter. The cost is asymmetric: a wrong guess does not raise an error, it silently returns a partial chapter list, and `scan-recurrences` then reports that nothing repeats across chapters it never read — output indistinguishable from a clean result, inherited by every skill downstream. Mixed manuscripts are refused with the offending paths named, not resolved on a best guess.
- **`paths.layout` and `paths.analyses` are independent axes**, and all four combinations are legal. `analyze-chapter` now states that "next to the chapter" resolves through the layout, since a resolver assuming analyses sit beside the chapter is wrong in half the combinations. `outline-chapter` creates the chapter directory when it does not exist yet.
- **`init-project` asks for the layout** as part of Q5, defaults to `flat` with the reason stated, recommends `chapter` when the planned count is large and per-chapter satellites are expected, and now instructs zero-padding in `paths.naming` — ordering is lexicographic, so unpadded ids sort `10` before `2`. When an existing manuscript is present it reports a layout mismatch and **never moves the author's files**.
- **Migration is documented as commit hygiene, not just commands.** The moves and the `paths.layout` change belong in one isolated `chore:` commit, and never mid-revision: `review-revision` diffs a chapter against the commit that preceded the rewrite, and a move landing inside that window silently rebaselines it.

### Fixed

- **The README's canonical directory tree showed `manuscript/Act 01/`**, a third arrangement matching neither `paths.naming` nor anything the skills resolve. It was the only place in the system describing manuscript organization, and it described one that did not exist.

### Added

- **A commit convention for book repositories, and the `commit` skill that writes it.** The commit is a working part of this system — `review-revision` diffs a rewritten chapter against the commit that preceded it — but until now the only vocabulary available was the one p10t itself uses, which describes software. Book repositories now use `type(scope)!: subject`: one line, English, ten types across four families (Manuscript: `draft`, `revise`, `cut` · Curation: `annotate`, `rule`, `voice` · Machine: `analyze`, `review` · Apparatus: `chore`, `docs`). Scope is optional. `!` marks a change that **invalidates text already written**, so `git log --grep "!"` returns everything that requires going back. Documented in the README's new **Commits** section, which is the canonical version; `CLAUDE.md` links to it.
- **`commit` is the only skill that touches git, and it runs only when the author asks.** No other skill may invoke it; skills may *suggest* a commit line in their closing output. A commit is an assertion of authorship, and the log is the evidence base for `book-review.md` §3.5 — a history the machine writes about itself is self-reporting rather than evidence.
- **The rule that protects the workflow is narrow staging, and it binds the author too.** `review-revision` compares a rewritten chapter against the commit that preceded it. A broad `git add -A` in the middle of a rewrite folds half the revision into that baseline, and the comparison then reports on the remainder as though the rest had never been done — without erroring, because a smaller diff is still a valid diff. The report reads as *less was done than expected*, and since `review-revision` writes `revision-log.md`, which `consolidate-style`, `define-persona` and `update-preserve-list` read as their source, an applied suggestion recorded as refused can be promoted into `persona.md` as a style signature. `commit` detects the state (a manuscript file changed since its last commit, with an `R:`-annotated `_analysis.md` alongside it), warns before committing, proposes splitting a mixed tree into separate commits rather than flattening it, and stages only what the approved message covers.
- **Commit messages are in English regardless of the project's output language** — the type names are the same vocabulary the skills use internally, and the log stays readable across projects. It is the one documented exception to the output-language rule.

### Planned
- `[es]` and `[fr]` detection-signal sections in `framework.md`
- Field-testing the generation and knowledge layers at book length (the revision cycle has been tested; see 0.3.0)
- A validation script: frontmatter names vs. directory names, unfilled `{placeholders}`, dangling cross-references
- An export skill: manuscript to submission format
- Per-skill worked examples in `examples/`

## [0.3.0] — 2026-07-28

End-to-end audit of the project. Two functional defects fixed, one skill added, documentation reconciled with what the system actually does.

### Changed

- **Density is now defined.** The system's central metric had been used in three incompatible scales — qualitative labels, whole-chapter percentages, and per-category percentages — with no definition of what the percentage measured. It is now **occurrences per 1,000 words**, with explicit counting rules in `framework.md`: what counts as one occurrence, one category per instance, PRESERVE and persona signatures excluded from the count, RECURRENCE included. Categories 8, 9, and 13 carry their own units (per-word per-1k, exchanges per chapter, % of chapters) rather than being forced into a figure that would mean nothing. Propagated to `analyze-chapter`, `review-revision`, `draft-scene`, `consolidate-style`, `review-book`, all affected templates, `project.yaml`, and `style-guide.md`.
- **Default ceilings per category**, marked calibratable, with an explicit precedence chain: `persona.md` signature (no ceiling) > `style-guide.md` project override > framework default. Total chapter ceiling of 8,0/1k in `project.yaml`.
- **`book-review.md` §3.5 no longer asks for "% human / % AI" per layer.** Those percentages are not measurable from prose, and the skill contradicted itself by banning false precision one step earlier. Replaced with a classification — authorial / assisted / generated-and-curated — where every row carries citable evidence and a layer with no record says `no record`. Rationale: this section can end up backing a public declaration of AI use, where an invented figure is a reputational liability for the author, not a reporting flaw. New §3.6 charts the revision trajectory, which is counted rather than asserted.
- **The `revision-log.md` entry is now mandatory** in `review-revision`, not optional. `consolidate-style`, `update-preserve-list`, and `define-persona`'s update mode all read it as their primary source — an optional entry meant the learning layer could stop compounding silently.
- **`framework.md` gained `[en]` detection signals** for every applicable category, making the "generic" claim true for English rather than aspirational. Category 7 was reframed as *anglicized vocabulary / LLM literary register*: in English there is no calque, so the equivalent marker is the over-used literary register, and the phrasings table (`a testament to`, `a quiet kind of`, `something shifted`) is the stronger signal. Category 11 now states its counting rule per language, since English marks dialogue with quotation marks and has no national dash convention to lean on.
- **Single source of truth for two conventions that had two.** Analysis file location is `project.yaml → paths.analyses` (`analyze-chapter` had pointed at the root `CLAUDE.md`). The directory tree lives only in the README; `CLAUDE.md` and `.project/CLAUDE.md` link to it — they had drifted already, disagreeing on the skill count.
- **The revision workflow now says to commit before rewriting.** `review-revision` offered `git diff` as its comparison method while nothing established the commit boundary it needs.
- `init-project` flags degraded framework coverage when the output language is neither `pt-BR` nor `en`, and offers to remove the template's own artifacts (`examples/`, `manuscript/README.md`, `CHANGELOG.md`) from a new book.
- `README.md`: corrected the skill count (said sixteen across five layers; it was seventeen across six), added `examples/` to the tree, documented the density unit, and **replaced the Roadmap section**, which listed fourteen already-implemented skills as future work and contradicted the section immediately above it.
- `examples/`: density figures relabelled as illustrative. That session predated the per-1k unit and the chapter has not been re-counted — the quotes, annotations, and outcome are real, the numbers show shape only.
- `.gitignore`: removed two no-op negation patterns (nothing above ignored the paths they exempted), leaving a note for whoever adds a broader rule later.

### Added

- **`restructure-chapter`** — the eighteenth skill, closing the gap between structural diagnosis and action. `check-arc` and `review-book` found scene-level faults but could not act on them; `revise-passage` explicitly refused them ("if more than ~60% needs replacing, the problem is upstream"); `outline-chapter` only builds chapters that do not yet exist. The path ended at "have a conversation". This skill rebuilds a chapter's obligations backwards from the page, then proposes move / merge / compress / cut / new per scene — naming, for every cut, which surviving scene inherits its load-bearing content, and reporting the blast radius on downstream chapters. Delivers a plan; never rewrites the manuscript.
- `style-guide.md`: a **Density ceilings** section for project overrides, and a **Language adaptation** note for manuscripts outside the calibrated languages.

### Fixed

- The `(roadmap)` markers left in `config/persona.md`, `knowledge/characters/_README.md`, `reports/preserve-list.md`, `reports/revision-log.md`, `reports/literary/.gitkeep`, and `templates/book-review.md`, all describing shipped skills as unbuilt.
- The unfilled `{user}` placeholder in the root `CLAUDE.md` repository URL.
- The contradiction between this file and `examples/README.md` over whether the system had been field-tested. It has, **partially**: the revision cycle ran on a real manuscript; the generation and knowledge layers have not been exercised at book length. Both files now say so.

## [0.2.0] — 2026-05-23

### Changed
- **Skills moved from `.project/skills/` to `.claude/skills/`** with YAML frontmatter (`name` + `description`), enabling native Claude Code auto-discovery. Rationale: the "agnostic path" bought folder-name neutrality, not functionality — skills are plain markdown readable from any path, and other agent ecosystems would need a convention instruction regardless. The split is now conceptual, not defensive: `.claude/skills/` holds what the system *does* (generic machinery), `.project/` holds what the system *knows* (book-specific state).
- Root `CLAUDE.md` simplified: full skill trigger table, no manual-read convention needed under Claude Code (kept as fallback for other agents).
- `.project/CLAUDE.md` and `README.md` updated to the two-root layout.
- `.gitignore`: added `.claude/settings.local.json`.

### Added
- `chapter-outline.md` listed in documented templates.

## [0.1.0] — 2026-05-23

First complete scaffold. The full 16-skill roadmap implemented as markdown skills, plus templates, knowledge structure, and documentation.

### Added

**Core documentation**
- `README.md` — philosophy, structure, the 14 categories, workflow, roadmap
- `CLAUDE.md` (root template) + `.project/CLAUDE.md` — hub convention, no auto-discovery
- `LICENSE` (MIT), `.gitignore`

**Framework**
- `templates/framework.md` — 14 categories of AI markers with definitions, detection signals (`[pt-BR]`), and default treatments; category 15 open; verdict priority order; 10-pass revision sequence

**Analysis layer**
- `analyze-chapter` — per-chapter 14-category analysis with preserve-list/recurrence/persona cross-referencing
- `scan-recurrences` — cross-chapter duplication sweep; intentional-vs-accidental classification; incremental mode
- `review-revision` — five-axis evaluation of author revisions; the learning loop's data source

**Foundation layer**
- `define-persona` — voice extraction (bootstrap/update modes); persona as extracted, not invented
- `define-references` — borrowing instructions with mandatory exclusion lines

**Knowledge layer**
- `build-worldbuilding` — world as consistency contract; rules with costs; deliberately-unexplained list; extract/create modes
- `create-character` — voice-first sheets; SHOWN/INFERRED split; voice-drift detection; extract/create modes

**Generation layer**
- `outline-chapter` — chapters as obligations (debt/planting/protection); scene contracts
- `draft-scene` — full-context generation with self-audit against the project's own analysis; mandatory delivery notes; survival-rate metric
- `revise-passage` — surgical revision; diagnosis before cutting; comparison-format delivery
- `expand-beat` — texture without plot; author's fragments are load-bearing

**Literary analysis layer**
- `review-book` — whole-book literary/commercial/AI-use report; evidence-per-claim discipline
- `check-consistency` — four sweeps (rules, time, character, knowledge states); never resolves silently
- `check-arc` — beat maps from the page before intent; flat stretches, rushed turns, abandoned threads

**Learning layer**
- `update-preserve-list` — batch harvesting of protection decisions; list verification against manuscript
- `consolidate-style` — pattern threshold (3+ occurrences); evidence-backed persona diffs

**Infrastructure**
- `init-project` — seven-question bootstrap; existing-manuscript vs. blank-page routing
- Templates: `chapter-analysis`, `chapter-outline`, `persona-template`, `character`, `book-review`
- Knowledge skeletons: `worldbuilding`, `timeline`, `glossary`, `characters/`
- Report skeletons: `preserve-list`, `recurrences`, `revision-log`

### Design decisions of record
- System language English; output language per-project (`project.yaml → language`)
- Skills in `.project/skills/` with convention-based invocation — tool-agnostic, no auto-discovery
- Persona overrides framework; preserve list overrides tic suggestions; author overrides everything
- Generated drafts never touch manuscript files directly
