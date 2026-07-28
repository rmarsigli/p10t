# Changelog

All notable changes to p10t are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/); versioning follows [SemVer](https://semver.org/).

## [Unreleased]

### Planned
- Field-testing the full cycle on a real manuscript
- `[en]` and `[es]` detection-signal sections in `framework.md`
- Per-skill worked examples in `examples/`

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
