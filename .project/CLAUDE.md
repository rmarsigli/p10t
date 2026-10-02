# `.project/` — Book knowledge hub

This directory holds **what the system knows** about this book. Its counterpart, `.claude/skills/`, holds **what the system does** — the twenty-three skills, which read from and write to the files here.

Portable (copy into another book and repopulate), git-versionable, plain markdown throughout.

## Language

Templates here are in **English** for LLM reliability. **All content written into these files follows `config/project.yaml → language`** — persona examples, character sheets, reports, and preserve-list entries are quotes from and about the manuscript, so they live in its language.

## Structure

Four directories, each with one job:

| Directory | Holds | Filled by |
|---|---|---|
| `config/` | ── **WHO YOU ARE** ── voice, references, hard rules, metadata | `define-persona`, `define-references`, by hand |
| `knowledge/` | ── **WHAT EXISTS IN THE BOOK** ── world, timeline, glossary, characters | `build-worldbuilding`, `create-character`, by hand |
| `reports/` | ── **WHAT HAS BEEN FOUND** ── analyses, critiques, preserve list, recurrence map, decision history | `analyze-chapter`, `critique-chapter`, `scan-recurrences`, `review-revision`, `review-book` |
| `templates/` | ── **REUSABLE SKELETONS** ── the 14 marker categories, the 11 craft categories, the layout and localization resolvers, output shapes | never — these are the machinery |

The canonical file-by-file tree lives in the p10t [README](https://github.com/rmarsigli/p10t#structure), kept in one place so it cannot drift out of sync with this file.

## Density

Occurrences per 1,000 words, one decimal. Counting rules and default ceilings: `templates/framework.md`. Project overrides: `config/style-guide.md`. Chapter total: `config/project.yaml`.

## Craft

Judged, never scored. Categories, reader effects, severities, and the verdict rule: `templates/craft.md`. Output shape: `templates/chapter-critique.md`.

## Manuscript layout

`config/project.yaml → paths.layout` declares how chapter files are arranged — `flat` or one directory per chapter. **`templates/layout.md` is the single resolver**: any skill that reads more than one chapter follows it rather than globbing the manuscript directory. It also fixes the ordering rule, which timeline checks and cross-chapter sweeps depend on.

## Target-language editions

Optional. When a book has one, it lives in `translations/{bcp47}/` — outside `.project/`, one self-contained folder per language, mirroring `paths.layout` for its own manuscript. **`templates/localization.md` is the single resolver**, the same way `layout.md` is for chapters.

Nothing here is modified by a translation run. The localization skills read `config/` and `knowledge/`, and report findings about them — an uncatalogued referent, a term that drifted, culture of the prose language leaking into a setting that is not its own. **The author rules; the skills do not edit.**

## Generic vs. project-specific

| Location | Reusable across books? |
|---|---|
| `.claude/skills/` | Yes — copy as is |
| `.project/templates/` | Yes — copy as is |
| `.project/config/` | No — repopulate per book |
| `.project/knowledge/` | No — repopulate per book |
| `.project/reports/` | No — generated during work |

## The two files that make the system work

**`reports/preserve-list.md`** — phrases that must never be flagged as tics. Without it, analysis would suggest cutting the mantra that holds a character together.

**`reports/recurrences.md`** — the cross-chapter duplication map. Chapter-by-chapter analysis is blind to repetition across chapters; this is the only defence.
