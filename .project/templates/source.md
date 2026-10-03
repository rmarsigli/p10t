# Manuscript source

Where the prose lives, and how every skill reaches it. This is the single resolver for the manuscript's **origin**, the way `layout.md` is for its arrangement on disk and `localization.md` is for a target edition.

Declared in `.project/config/project.yaml → source.kind`. **Never detected** — for the same reason `layout.md` gives: a wrong guess does not fail, it produces a confident analysis of a book that is not the one the author is writing.

> **Status: `local` is the default and is unchanged. `mcp` is experimental** until its first field test — the adapter below names what is confirmed and what is pending.

---

## The two kinds

| | `local` (default) | `mcp` (experimental) |
|---|---|---|
| The prose lives in | markdown files in `paths.manuscript`, versioned in git | a writing app, read through an MCP connector |
| Chapters are enumerated by | `layout.md` | the app's outline (below) |
| A chapter's key | its id — the filename stem | the app's **node id**; the `{act}.{chapter}` id is a display label |
| Text is read from | the chapter file | the connector, by scope |
| The revision baseline is | the commit made before rewriting | the **snapshot** the author takes in the app before rewriting |
| "Has this changed?" is answered by | `git log` | per-scene **content hashes** |
| The manuscript's history lives in | git | the app (snapshots); git holds `.project/` only |

Everything p10t writes — analyses, critiques, plans, drafts, reports, the revision log, persona, knowledge — stays local and in git under both kinds. **Under `mcp`, p10t never writes to the app.**

---

## The contract every source satisfies

A skill never talks to a source directly. It asks for one of these operations and this file says how the declared source answers.

| Operation | Returns |
|---|---|
| **enumerate** | The chapters in reading order, each with its key, display id, title, and scenes in order. Supports Act scoping |
| **read** | The exact text of a scene, a chapter, a range, an Act, or the book |
| **fingerprint** | For a chapter: its scenes in order, each with key and content hash — or, under `local`, the commit |
| **baseline** | The text of a chapter as it was before the author rewrote it |
| **staleness** | Whether a recorded fingerprint still matches the current text |
| **intent** *(optional)* | Synopses and declared fields (POV, characters present, location) the app holds per node |

Under `local`, every operation already has an answer elsewhere: `layout.md` enumerates, files are read, the commit is the fingerprint, `git diff` against the pre-rewrite commit is the baseline, `git log` is staleness, and `_outline.md` is intent. **Nothing in this section changes how a `local` book works.** The rest of this file is the `mcp` kind.

---

## `mcp` — the rules

### 1. Read-only, always

Connect with the app's **read** scope. If the connector exposes write tools anyway, no skill calls them — not to fix a typo, not to set a status, not to take a snapshot. The baseline snapshot in particular is **the author's act**, for the same reason no skill commits: defining the baseline is an assertion of authorship.

If the connector is not reachable, or its authorization expired, **stop and say so**. Never fall back to anything in `manuscript/`, never work from a cached copy, never continue on what was read earlier in the session.

### 2. The text is the stored body, exactly as typed

The connector returns the author's text byte for byte — no normalization, in either direction. Quotes in every report are literal from it. Never "clean" it: a `_` the author typed stays `_`, a non-breaking space stays one.

**Large documents arrive in parts.** Join the parts of one document in order before counting anything. Every part carries the hash of the **whole** document: if two parts of the same document disagree, the document changed mid-read — discard what was read and read it again.

### 3. There is no scaffolding

Under `local`, `##` scene headers, HTML comments and budget lines are drafting scaffolding, excluded from every count. **Under `mcp` none of that exists**: the body of a node is exactly what prints.

- Every line of the body is prose and **counts** — including headings, which in an app-held book are the book's own content (an in-world report's section titles, a letter's heading).
- The `##`-header convention, `scripts/scene-budget` and the scaffolding rules in `manuscript/README.md` do not apply.
- A thematic break (`***`) inside a body is the author's text: a break **within** that node, not a node boundary.
- The connector's `separator` field belongs to the compile preset — what prints between nodes. It is not a scene marker either.

### 4. Identity: the node id is the key

The app's node id is the primary key. The `{act}.{chapter}` id is a **display label**, derived from the outline:

- **Act** — the position of the enclosing part among the outline's parts, zero-padded as `paths.naming` requires. An outline with no parts has no act: the label is `{chapter}` alone, and `structure.grouping` should say `none`.
- **Chapter** — the chapter's position inside its part (or in the book, when there are no parts), zero-padded.
- **Scenes** — the chapter's child nodes, in order. A chapter node whose own body has text and no children is a single-scene chapter.

**Scenes in the app are the author's divisions, not necessarily dramatic scenes.** One node can hold two dramatic scenes separated by `***`. Skills that map scenes (`critique-chapter`, `restructure-chapter`) keep the node as the unit of identity and number the dramatic scenes inside it: `c01.s04 · 1`, `c01.s04 · 2`, using the node's label as the app shows it.

**Every record stores both.** An analysis, a critique, a translation row records the node id next to the display label. When a skill resolves a chapter and the node id it recorded now sits at a different display label — the author reordered chapters — it **stops and reports** the old and new labels, and proposes renaming the satellites in one isolated `chore:` commit. It never re-points a record silently. A recorded node id the outline no longer has is reported the same way: the chapter was deleted or emptied out of the preset.

### 5. Satellites still live "next to the chapter"

`manuscript/` keeps its job as the home of satellites — `_outline`, `_draft`, `_restructure`, and analyses when `paths.analyses` points there — arranged by `paths.layout` exactly as before. It just never holds the chapter file itself.

> **Two sources is a mixed state.** If `source.kind` is `mcp` and any file in `manuscript/` matches `paths.naming` as a chapter, stop and name the files — the same rule `layout.md` applies to a half-migrated tree, for the same reason.

Drafts produced by `draft-scene` and `expand-beat` remain local `_draft.md` files: they are proposals, not the book. The author carries what survives curation into the app by hand.

### 6. Fingerprint

Every analysis, critique and translation made under `mcp` records the chapter's **source fingerprint** in its header:

```markdown
**Source:** {server} · project {projectId} · read {date}

| Scene | Node | Content hash |
|---|---|---|
| {label} | {nodeId} | {contentHash} |
```

Where one cell must hold it — the `status.md` column of a translation — use the **short form**: each scene's hash truncated to its first 12 hex characters, joined by `+` in reading order.

A multi-chapter run also records the outline's book `version` at the start of the run. If it differs at the end, or a paginated read's cursor is refused because the book changed, the run read an inconsistent book: say so, and re-read the chapters that changed rather than reporting on a mixture.

### 7. Staleness

A record is **current** when the chapter's scenes, in order, still carry the hashes it recorded. Compare against the outline — no text needs to be read. A hash that changed, a scene added, removed or reordered: stale. This replaces every `git log` staleness check under `mcp`.

### 8. Baseline — three levels, decided per scene

`review-revision` needs the chapter as it was before the rewrite. For each scene in the recorded fingerprint, in order:

1. **Exact** — a snapshot of that node whose content hash equals the recorded hash. Its text is the baseline, byte for byte.
2. **Approximate** — no hash matches (the author fixed a typo between the analysis and the snapshot). Take the **earliest snapshot of that node created after the record's date**, and check it against the record's literal quotes: count how many quotes it still contains. Use it, and say in the report that this scene's baseline is approximate and how many quotes it carries.
3. **Quotes only** — no snapshot after the record. Fall back to the literal quotes, exactly as `review-revision` does today for a `local` chapter that was never committed.

The report states which level each scene got. **A missing snapshot is a normal state, not an error**: the author may have deleted it, and emptying the app's trash removes a node's snapshots with it.

Snapshots are looked up by the **recorded node ids**, never by walking the chapter as it is now: a scene the author moved out of the chapter after the analysis is exactly the scene whose baseline matters most.

**The ritual that makes level 1 the common case:** after reading the analysis and critique, and before rewriting, the author takes a snapshot of the chapter in the app. It replaces "commit the chapter before rewriting". The `.project/` files — the `R:` annotations above all — are still committed as before.

### 9. Intent

Synopses (chapter and scene) and declared fields (POV, characters present, location) are **intent**, with the same standing as an `_outline.md`: read **after** the first reading pass, compared against the page, never used to read it. A declared POV is the claim cat. 7 of `craft.md` tests the page against. A synopsis describing a scene the page does not deliver is a finding about the page or about the synopsis — present both readings; the author rules.

### 10. What does not apply

| Under `local` | Under `mcp` |
|---|---|
| `scripts/export` | Refuses, and says to compile in the app — the app's compile presets are the export |
| `scripts/scene-budget` | The app counts words per node |
| "Commit the chapter before rewriting" | "Snapshot the chapter in the app before rewriting" |
| Manuscript commit types (`draft`, `revise`, `cut`) | Do not apply to the manuscript — its history is the app's. They still apply to `_draft` and other local satellites |
| `git log` as evidence of who wrote what | Snapshots and `revision-log.md`. If the app records snapshots taken automatically before machine edits, those are direct evidence for `review-book`'s AI-use section — cite them |

### 11. Knowledge stays in `.project/`

Character and location sheets the app holds are **seeds** for `create-character` and `build-worldbuilding` in extract mode — useful, and never the source of truth. `.project/knowledge/` wins. Nothing is synchronized in either direction: two sources of truth for the same character drift, and the drift is silent.

---

## Adapter — proseyard

The first `mcp` source. Tools are named by their base name; the prefix depends on what the author called the connection in their client (`source.server`), so skills match the base name and never hardcode a prefix.

| Operation | Tool | Status |
|---|---|---|
| choose the project | `list_projects`, `get_project_overview` | available |
| enumerate | `get_manuscript_outline` (preset from `source.preset_id`, or the app's default) — parts, chapters, scenes, labels, word counts, synopses, declared fields, book `version` | available |
| read | `read_manuscript` with `scopeKind` `node` · `chapter` · `chapters` · `part` · `book`, paginated by cursor | available |
| fingerprint · staleness | `contentHash` on each outline node and each `read_manuscript` item, every part carrying the whole document's hash | **pending** |
| baseline | `list_snapshots` by a list of node ids (with creation date, title, kind, word count, `contentHash`); `read_snapshot`, paginated, every part carrying the whole snapshot's hash | **pending** |
| intent | synopses and reference fields from `get_manuscript_outline`; `read_document` for one node's notes | available |
| search | `search_text` | available |
| knowledge seeds | `list_entities`, `get_entity` | available |

**Confirmed behaviour:** `text` is the stored body exactly as typed; annotations live outside it; a read-scope connection only exposes read tools; the outline's `version` is a hash over preset, node ids, content versions, section types, parents and separators — statuses, synopses and labels do not move it.

**Pending, to be confirmed against the app's final summary:** the exact names and parameters of the snapshot tools, the `contentHash` formula (expected: sha256 of the UTF-8 body as returned), `read_snapshot` pagination, `separator` always present as `null` when empty, and the server-side "snapshot this chapter" action. Until `contentHash` and the snapshot tools exist, rules 6–8 cannot run: a skill reading an `mcp` source records the node ids and the book `version`, says plainly that staleness and baseline are unavailable, and `review-revision` uses the quotes-only level.

---

## Why declared, and why read-only

Detection would have to guess whether a connected app or the files on disk are the book — and an author with both is exactly the author halfway through moving. A wrong guess produces a confident report on the wrong text, and nothing downstream catches it.

Read-only for the reason the whole system rests on: the AI proposes, the author decides. A tool that can edit the manuscript eventually does, and a manuscript edited by its own reviewer is no longer evidence of anything.
