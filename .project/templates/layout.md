# Manuscript layout

How skills **locate, enumerate, and order** chapter files. This is the single resolver: any skill that reads more than one chapter follows it rather than globbing on instinct.

Declared in `.project/config/project.yaml → paths.layout`. **Never detected** — see *Why declared* below.

---

## The chapter id

The **id** is the filename stem of the chapter file, and it is the primary key of the whole system. Its shape comes from `paths.naming`.

| `paths.naming` | id | example file |
| --- | --- | --- |
| `{act}.{chapter}.md` | `02.03` | `02.03.md` |
| `{chapter}.md` | `07` | `07.md` |
| `{act}.{chapter}i.md` (variant suffix) | `02.03i` | `02.03i.md` |

**Numbers are zero-padded.** Ordering is lexicographic, so `10` sorts before `2` when unpadded. Padding is not cosmetic — it is what makes ordering correct without parsing.

Any suffix a book adds to distinguish chapter *kinds* (interlude, appendix, fragment) is part of the id. The resolver never interprets it; it only sorts it. `02.03` < `02.03i` < `02.04` holds in string ordering, which is why suffixing works and a separate numbering sequence would not.

---

## The two layouts

### `flat`

Every chapter file sits directly in `paths.manuscript`.

```text
manuscript/
├── 01.01.md
├── 01.01_outline.md
├── 01.01_analysis.md
├── 01.02.md
└── 01.02_analysis.md
```

### `chapter`

One directory per chapter, **named exactly the chapter id**.

```text
manuscript/
├── 01.01/
│   ├── 01.01.md
│   ├── 01.01_outline.md
│   └── 01.01_analysis.md
└── 01.02/
    ├── 01.02.md
    └── 01.02_analysis.md
```

**The chapter file repeats its id in the filename** — `01.01/01.01.md`, never `01.01/chapter.md`. Three reasons, all load-bearing:

1. Grep results, editor tabs, and error messages stay unambiguous without their parent directory.
2. Migration between layouts is a pure **move**, never a rename. `git log --follow` survives it intact.
3. The sort key is identical in both layouts, so ordering code has one path, not two.

### Directory naming is not negotiable

The directory name is the **full id** — `01.01/`, not `1/`, not `ch01/`, not `Act 01/`. A bare number is ambiguous the moment a second act exists: chapter 1 of act 1 and chapter 1 of act 2 both claim `01/`.

---

## Resolution

Given `paths.manuscript`, `paths.layout`, and `paths.naming`:

**`flat`** — candidates are `*.md` directly inside `paths.manuscript`. A candidate is a **chapter** if its stem matches `paths.naming`; otherwise it is a satellite or a non-chapter file.

**`chapter`** — candidates are the immediate subdirectories of `paths.manuscript` whose name matches `paths.naming`. Inside each, the chapter file is the one whose stem equals the directory name. A directory with no such file is an **error**, not an empty chapter — report it.

Then sort ascending by id. That is the reading order, and it is the order every full-book sweep uses.

Files that match neither rule (`README.md`, notes, scratch) are **not chapters** and are excluded silently.

---

## Satellites

A **satellite** is a file belonging to one chapter: `{id}_analysis.md`, `{id}_outline.md`, `{id}_draft.md`, `{id}_restructure.md`, and any book-specific companion.

> **Rule: a file whose stem is `{id}_{anything}` is a satellite of `{id}`.**

An open rule, not a closed list — books add their own companions and the resolver must not need updating when they do.

Satellites live **beside their chapter file**: same directory in `flat`, inside the chapter directory in `chapter`. Skills that write "next to the chapter" are already correct in both layouts and need no branching.

### The one exception, and it is orthogonal

`paths.analyses` independently decides whether `_analysis.md` files sit beside the chapter or centralize in `.project/reports/technical/`. **`paths.layout` and `paths.analyses` are separate axes and every combination is legal.** A resolver that assumes analyses live next to the chapter is wrong in two of the four combinations.

---

## Scoping to an Act

`check-arc`, `check-consistency`, and `review-book` all accept "Act {N}". **Resolve it from the id prefix, in both layouts** — never from directory structure.

This is why there is no separate per-act layout: the id already carries the act, so act scoping costs one string comparison and works identically whether the book is flat or foldered. A directory layer grouping acts would duplicate information the id already holds, and duplicated information drifts.

For books with `structure.grouping: none`, act scoping does not apply; scope is whole-book or an explicit chapter list.

---

## Mixed state

A manuscript is mixed when both forms are present — a chapter file loose in `paths.manuscript` **and** chapter directories beside it. This happens during migration and when a file is added by hand.

> **Stop and report. Never resolve a mixed manuscript.**

The reason is the failure mode, not tidiness. A resolver that guesses does not raise an error — it silently returns a partial chapter list, and `scan-recurrences` then reports that nothing repeats across chapters it never read. The output looks exactly like a clean result. Every skill downstream inherits the lie.

Name the offending paths and let the author fix them.

---

## Migrating

Because the chapter filename does not change, migration is mechanical.

**`flat` → `chapter`**, per chapter id:

```sh
mkdir 01.01 && git mv 01.01*.md 01.01/
```

**`chapter` → `flat`**, per chapter directory:

```sh
git mv 01.01/*.md . && rmdir 01.01
```

Three rules:

1. **Update `paths.layout` in the same commit as the moves.** A config that disagrees with the tree is a mixed state by another name.
2. **Migrate in an isolated commit** — `chore:` only, touching nothing but moves and that one field.
3. **Never migrate mid-revision.** `review-revision` diffs a chapter against the commit made before the rewrite. A move commit landing inside that window changes the baseline, and the review then evaluates the wrong text confidently. Migrate between cycles.

---

## Why declared, never detected

Detection is tempting and wrong.

- `manuscript/01/` is unresolvable without opening it — act, chapter, or neither.
- A half-finished migration reads as a valid layout.
- A stray `_draft.md` in the manuscript root reads as a chapter.

And the cost is asymmetric. **A wrong layout guess does not fail — it produces a confident analysis of an incomplete book.** In a system whose only output is prose, there is nothing downstream to catch it. One declared field removes the entire class.

---

## Choosing

| | Best when |
| --- | --- |
| `flat` | fewer than ~15 chapters, or few satellites per chapter. Reading the book in file order needs no navigation. |
| `chapter` | many chapters, or 3+ satellites each. A 32-chapter book with an outline, an analysis, and a draft per chapter is ~130 files in one directory. |

The cost of `chapter` is human, not technical: reading straight through means walking directories. The cost of `flat` is that it degrades gradually and there is never an obvious day to switch.

**Migrate early if migrating at all** — the work is linear in the number of files, and the risk of getting it wrong is not.
