# `.project/` — Book knowledge hub

This directory holds **what the system knows** about this book. Its counterpart, `.claude/skills/`, holds **what the system does** — the seventeen skills, which read from and write to the files here.

Portable (copy into another book and repopulate), git-versionable, plain markdown throughout.

## Language

Templates here are in **English** for LLM reliability. **All content written into these files follows `config/project.yaml → language`** — persona examples, character sheets, reports, and preserve-list entries are quotes from and about the manuscript, so they live in its language.

## Structure

```
.project/
├── CLAUDE.md            this file
│
├── config/              ── WHO YOU ARE ──
│   ├── persona.md       author voice (fill via define-persona)
│   ├── references.md    reference authors and works
│   ├── style-guide.md   hard rules for this project
│   └── project.yaml     metadata, including output language
│
├── knowledge/           ── WHAT EXISTS IN THE BOOK ──
│   ├── worldbuilding.md
│   ├── timeline.md
│   ├── glossary.md
│   └── characters/      one sheet per character
│
├── reports/             ── WHAT HAS BEEN FOUND ──
│   ├── technical/       per-chapter analyses (if centralized)
│   ├── literary/        whole-book reports
│   ├── preserve-list.md untouchable phrases
│   ├── recurrences.md   duplication map
│   └── revision-log.md  decision history
│
└── templates/           ── REUSABLE SKELETONS ──
    ├── framework.md     the 14 tic categories
    ├── chapter-analysis.md
    ├── chapter-outline.md
    ├── persona-template.md
    ├── book-review.md
    └── character.md
```

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
