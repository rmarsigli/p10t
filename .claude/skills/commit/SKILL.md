---
name: commit
description: Writes a git commit for a book repository using p10t's commit convention — infers the type and scope from what actually changed, proposes a single line, and commits only after the author approves. Warns before moving the revision boundary that review-revision depends on. Use when the author asks to commit, says "commit this", or runs /commit. Never invoked by another skill.
---

# Skill: commit

**What it does.** Reads the working tree, infers a commit type and optional scope from what changed, proposes **one line**, and commits after the author approves it.

**Triggers**
- "commit"
- "/commit"
- "commit this", "commit the chapter"
- Equivalent phrasing in the project's output language

**Input.** Optional: what the author wants recorded, in their own words.

**Output.** One commit, after explicit approval.

> **Commit messages are written in English, always** — even when the book's output language is not. The types are the same vocabulary the skills use internally, and the log stays readable across projects. This is the one place in p10t where the output language does not apply.

---

## Core principle

> **No skill commits on its own. This one only runs when the author asks for it.**

A commit in a book repository is an assertion of authorship, and the log is the evidence base for `book-review.md` §3.5, which classifies each layer of the book as authorial, assisted, or generated-and-curated. If the machine writes its own history, that evidence becomes self-reporting.

> **The second principle is narrower and does more work: stage only what the message describes.**
>
> That one binds the author too, and it is the rule that actually protects the workflow. See **The revision boundary** below.

---

## The convention

```
type(scope)!: subject
```

- `type` — from the closed list below
- `(scope)` — optional; a chapter number, or a knowledge area (`world`, `timeline`, `characters`)
- `!` — optional; marks a change that **invalidates text already written**
- `subject` — English, imperative, lowercase after the colon, no full stop

**One line. No body, no footer.**

### Types

**Manuscript** — material enters, changes, or leaves.

| Type | Use |
|---|---|
| `draft` | material that did not exist before: new prose in the manuscript, and generated proposals awaiting curation (`_draft`, `_outline`, `_restructure`) |
| `revise` | changing prose that already exists — from a single sentence to reordering the scenes of a chapter |
| `cut` | material removed and parked in `_drafts.md` |

**Curation** — the author decides, and the decision becomes binding.

| Type | Use |
|---|---|
| `annotate` | the author's `R:` rulings on an analysis file |
| `rule` | a world, character or timeline decision |
| `voice` | `persona.md`, `style-guide.md`, `references.md`, `preserve-list.md` |

**Machine** — skill output, not yet ruled on.

| Type | Use |
|---|---|
| `analyze` | `analyze-chapter`, `scan-recurrences` |
| `review` | `review-book`, `review-revision`, `check-consistency`, `check-arc` — including the `revision-log.md` entry |

**Apparatus.**

| Type | Use |
|---|---|
| `chore` | renames, lint, file moves, repository plumbing |
| `docs` | README, CLAUDE.md — the project describing itself |

### The `!` marker

In Conventional Commits, `!` means breaking change. Here it means **this invalidates text already written**.

```
rule(world)!: reversal edits, crossing inserts
```

A world rule that contradicts six finished chapters is not a `rule`; it is a `rule!`. `git log --grep "!"` then returns everything that requires going back.

Propose `!` whenever a curation commit contradicts material already on the page, and say which chapters are affected. The author decides.

---

## Protocol

### Step 1 — Read the tree

`git status`, then the diff. Do not stage anything yet.

### Step 2 — Check the revision boundary

**Before anything else.** See the section below. If the boundary is at risk, say so now, not after committing.

### Step 3 — Infer type and scope

From what changed, and from what the session was doing:

| What changed | Type |
|---|---|
| a manuscript file that had no prose before | `draft` |
| a manuscript file that already had prose | `revise` |
| a `_draft`, `_outline` or `_restructure` file | `draft` |
| `_drafts.md` grew and a chapter shrank | `cut` |
| `R:` annotations added to an `_analysis.md` | `annotate` |
| `worldbuilding.md`, `timeline.md`, `glossary.md`, `characters/` | `rule` |
| `persona.md`, `style-guide.md`, `references.md`, `preserve-list.md` | `voice` |
| a new `_analysis.md`, or `recurrences.md` | `analyze` |
| `reports/literary/`, `revision-log.md`, consistency or arc reports | `review` |
| renames, lint, file moves | `chore` |
| README, CLAUDE.md | `docs` |

Scope comes from the chapter number in the path, when there is one. **Never invent a scope**; leave it out when it is not obvious.

### Step 4 — Propose one line, and wait

Show the proposed message and the files it covers. The author can correct the type, the scope or the wording. **Do not commit before they say so.**

### Step 5 — Split before flattening

When the tree mixes unrelated work — a revised chapter and a world rule, say — **propose two commits, not one vague message.** Show both lines and which files go in each.

The author may decline and ask for a single commit. That is their call; take it and move on.

### Step 6 — Stage narrowly, then commit

Stage only the files the approved message covers. Never `git add -A` when the tree contains work the message does not describe.

---

## The revision boundary

`review-revision` compares a rewritten chapter against **the commit the author made before rewriting it**. That commit is a boundary, and this skill is the only thing in p10t that can move it.

**What moves it is staging, not committing.** A commit that carries only a report leaves the chapter's bytes untouched, so the comparison still lands where it should. What breaks the boundary is a commit that sweeps in a half-finished rewrite — `git add -A` while the author is mid-chapter. The baseline then contains part of the revision, and everything before that point becomes invisible to the review.

The related fragility: `git diff HEAD~1` assumes the previous commit is the baseline. That assumption holds today because nothing else commits. It stops holding the moment anything commits twice between the baseline and the review — which is the second reason no other skill may reach this one.

**Before committing, check for this state:**

- a manuscript file has changed since its last commit, **and**
- a matching `_analysis.md` exists carrying `R:` annotations

That means the author is mid-revision. Committing now changes what `review-revision` will diff against — and the failure is silent, because the comparison still runs and still produces a confident-looking evaluation of the wrong thing.

**Say so before committing:**

> Chapter 02.05 has changed since its last commit and `02.05_analysis.md` carries R: annotations — you are mid-revision. Committing now becomes the new baseline, so `review-revision` will diff against this instead of the pre-rewrite version. Commit anyway?

Then do what the author says. The point is that they know, not that they are stopped.

---

## What to avoid

**Committing without approval.** Even when the message is obvious. Even when the author committed six identical ones already.

**Being invoked by another skill.** Other skills may *suggest* a commit line in their closing output. Suggesting is free; committing is not. If this skill is ever reached from inside another skill's protocol, stop and hand back to the author.

**`git add -A` reflexes.** Stage what the message describes and nothing else.

**Bodies and footers.** One line. If the change needs a paragraph to explain, it needs two commits.

**Inventing scope.** No scope is better than a wrong one.

**Translating the message.** The convention is English regardless of the book's language.

**Rewriting history.** No amend, no rebase, no force, unless the author asks in those words.

---

## Two conventions, one boundary

A book repository is created by cloning p10t, so it inherits p10t's own commits — which use Conventional Commits (`feat`, `fix`, `docs`, `chore`), because p10t is software with SemVer and a changelog.

**Commits before `init-project` belong to p10t. Commits after it belong to the book.** `docs` and `chore` exist in both vocabularies and mean the same thing in both, so the overlap is harmless.

If this skill is somehow run inside the p10t repository itself, use Conventional Commits there, not this convention.

---

## Relationship to other skills

| Skill | Relationship |
|---|---|
| `review-revision` | depends on the boundary this skill can move — see above |
| every other skill | may suggest a commit line; none may invoke this one |
