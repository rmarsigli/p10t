# Revision Log

_Version 0 — no revisions recorded_

> **Write entries in the project's output language.**

Decision history across revisions. Written by the `review-revision` skill at the end of every session — **an entry is mandatory, not optional.**

This log is the primary source for `consolidate-style` (which mines it for persona patterns), `update-preserve-list` (confirmed-signature entries), and `define-persona` in update mode. It is also the evidence trail for how much of the book passed through human judgement, and the raw material for the AI-use declaration.

A session that skips its entry is a set of decisions that never reaches the persona. The learning loop stops compounding silently.

**Density unit:** occurrences per 1,000 words (see `templates/framework.md`).

---

## Entry format

```markdown
## {Chapter} — revised on {date}

**Length:** {before} → {after} words
**Density:** {before}/1k → {after}/1k (ceiling {N,N}/1k)
**Still over ceiling:** {cat. N ({N,N}/1k)} — or "none"
**Decisions:** {N} accepted, {M} rejected, {K} done differently
**Confirmed signatures:** {what the author kept as style}
**Errors corrected in review:** {N}
**Status:** {✓ approved | needs another pass}

**Notes:** {anything worth remembering about this revision}
```

---

## Worked example

```markdown
## 01.01 — revised on 23/05/2026

**Length:** 3.240 → 3.010 palavras
**Density:** 14,2/1k → 5,8/1k (teto 8,0/1k)
**Still over ceiling:** cat. 11 (travessão), 2,4/1k — teto 2,0/1k
**Decisions:** 24 aceitas, 6 rejeitadas, 11 feitas de outro jeito
**Confirmed signatures:** vocabulário elevado; "ou não" como autocorreção; "aliás" como auto-interrupção; travessão só para diálogo
**Errors corrected in review:** 4 (concordância, regência, palavra trocada, typo)
**Status:** ✓ aprovado

**Notes:** O autor melhorou a sugestão com frequência em vez de aplicá-la — a linha da cerveja e a troca por "constatação" ficaram melhores do que o proposto. Atenção ao problema invertido no diálogo: a cena do taverneiro saiu de seca demais para levemente sobrecarregada de comentário narrativo.
```

---

## Entries

_(to fill)_

---

## Aggregate summary

Updated by `review-revision` at each entry. Useful for the AI-use declaration in submission materials.

| Metric | Value |
|---|---|
| Chapters revised | 0 |
| Average density reduction | — |
| Chapters under total ceiling | 0 |
| Confirmed author signatures | 0 |
| Total decisions logged | 0 |
