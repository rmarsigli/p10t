"""Paths to the synthetic books the tests run against.

They live in the repository so the suite passes anywhere — a developer's
machine, a fresh clone, a CI runner — instead of skipping when someone
else's manuscript is not present.

`book` is the chapter layout, `flat` is the flat layout. Both are English,
like the rest of the repository, and both carry satellites (`_analysis`,
`_outline`) and non-chapter files (`README`, `_drafts`) that resolution must
ignore. Language-specific behaviour — labels, thousands separators — is
covered by unit tests that pass a language code, not by translated fixtures.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "fixtures"

BOOK = ROOT / "book"
BOOK_MANUSCRIPT = BOOK / "manuscript"

FLAT = ROOT / "flat"
FLAT_MANUSCRIPT = FLAT / "manuscript"

NAMING = "{act}.{n}.md"
