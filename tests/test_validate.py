"""Tests for scripts/validate.

A validator that only ever passes is worse than none: it converts an unread
check into a green tick. Every check here is exercised twice — once against
a repository that should pass it, once against one deliberately broken.

The script has no .py extension, so it is loaded by path.
"""
import importlib.machinery
import importlib.util
import pathlib
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "validate"

_spec = importlib.util.spec_from_loader(
    "p10t_validate",
    importlib.machinery.SourceFileLoader("p10t_validate", str(SCRIPT)),
)
validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate)


SKILL = """\
---
name: {name}
description: {description}
---

# Skill: {name}

**Triggers**
- "/{name}"
"""

PROJECT_YAML = """\
language: en
title: {title}
author: {author}
subtitle: ""
paths:
  manuscript: "manuscript/"
  naming: "{{act}}.{{n}}.md"
  layout: "flat"
"""


def build(root, skills=("alpha-one", "beta-two"), title='"{Title}"',
          author='"{Your name}"'):
    """A minimal repository shaped like p10t."""
    root = pathlib.Path(root)
    for name in skills:
        d = root / ".claude" / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(
            SKILL.format(name=name, description=f"Does {name}."), encoding="utf-8"
        )
    cfg = root / ".project" / "config"
    cfg.mkdir(parents=True)
    (cfg / "project.yaml").write_text(
        PROJECT_YAML.format(title=title, author=author), encoding="utf-8"
    )
    return root


def run(root):
    report = validate.Report()
    for _name, fn in validate.CHECKS:
        fn(pathlib.Path(root), report)
    return report


def failures(report, check):
    return [d for c, d in report.failures if c == check]


def skipped(report, check):
    return any(c == check for c, _ in report.skips)


class TestFrontmatter(unittest.TestCase):
    def test_matching_names_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(failures(run(build(tmp)), "frontmatter"), [])

    def test_name_drifted_from_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            p = root / ".claude/skills/alpha-one/SKILL.md"
            p.write_text(p.read_text().replace("name: alpha-one", "name: renamed"),
                         encoding="utf-8")
            found = failures(run(root), "frontmatter")
        self.assertEqual(len(found), 1)
        self.assertIn("alpha-one", found[0])

    def test_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / ".claude/skills/beta-two/SKILL.md").write_text(
                "# no frontmatter\n", encoding="utf-8")
            found = failures(run(root), "frontmatter")
        self.assertEqual(len(found), 1)
        self.assertIn("no YAML frontmatter", found[0])

    def test_empty_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            p = root / ".claude/skills/beta-two/SKILL.md"
            p.write_text(p.read_text().replace("description: Does beta-two.",
                                               "description:"), encoding="utf-8")
            found = failures(run(root), "frontmatter")
        self.assertEqual(len(found), 1)
        self.assertIn("description", found[0])

    def test_no_skills_is_a_skip_not_a_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = run(tmp)
        self.assertTrue(skipped(report, "frontmatter"))
        self.assertEqual(report.failures, [])


class TestCounts(unittest.TestCase):
    def test_correct_count_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text("Two skills, described below.\n",
                                            encoding="utf-8")
            self.assertEqual(failures(run(root), "counts"), [])

    def test_stale_count_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text("Nineteen skills, described below.\n",
                                            encoding="utf-8")
            found = failures(run(root), "counts")
        self.assertEqual(len(found), 1)
        self.assertIn("there are 2", found[0])

    def test_instructions_is_counted_too(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "CLAUDE.md").write_text("A set of five instructions.\n",
                                            encoding="utf-8")
            self.assertEqual(len(failures(run(root), "counts")), 1)

    def test_table_cells_are_examples_not_claims(self):
        """A table documenting this very check must not trip it."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "| Check | Catches |\n|---|---|\n"
                "| counts | prose saying \"nineteen skills\" when there are two |\n",
                encoding="utf-8")
            self.assertEqual(failures(run(root), "counts"), [])

    def test_unspelled_numbers_are_ignored(self):
        """'22 skills' is not checked; only spelled-out words are."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text("There are 19 skills here.\n",
                                            encoding="utf-8")
            report = run(root)
        self.assertEqual(failures(report, "counts"), [])
        self.assertTrue(skipped(report, "counts"))


class TestPaths(unittest.TestCase):
    def test_existing_path_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "See `.project/config/project.yaml` for metadata.\n",
                encoding="utf-8")
            self.assertEqual(failures(run(root), "paths"), [])

    def test_dangling_path_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "See `.project/templates/gone.md` for the rules.\n",
                encoding="utf-8")
            found = failures(run(root), "paths")
        self.assertEqual(len(found), 1)
        self.assertIn("gone.md", found[0])

    def test_markdown_links_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "[the rules](.project/templates/gone.md)\n", encoding="utf-8")
            self.assertEqual(len(failures(run(root), "paths")), 1)

    def test_placeholder_paths_are_not_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "Writes `.project/reports/{chapter}_analysis.md` per chapter.\n",
                encoding="utf-8")
            self.assertEqual(failures(run(root), "paths"), [])

    def test_author_content_is_not_checked(self):
        """manuscript/ and translations/ are created at run time."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "README.md").write_text(
                "Chapters live in `manuscript/01.01.md`, "
                "editions in `translations/en-US/`.\n", encoding="utf-8")
            self.assertEqual(failures(run(root), "paths"), [])

    def test_changelog_may_name_removed_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            (root / "CHANGELOG.md").write_text(
                "- Skills moved from `.project/skills/` to `.claude/skills/`.\n",
                encoding="utf-8")
            self.assertEqual(failures(run(root), "paths"), [])


class TestSkillRefs(unittest.TestCase):
    def test_implemented_skill_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(failures(run(build(tmp)), "skill-refs"), [])

    def test_slash_reference_to_missing_skill_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            p = root / ".claude/skills/alpha-one/SKILL.md"
            p.write_text(p.read_text().replace('"/alpha-one"', '"/gamma-three"'),
                         encoding="utf-8")
            found = failures(run(root), "skill-refs")
        self.assertEqual(len(found), 1)
        self.assertIn("gamma-three", found[0])

    def test_relationship_table_row_is_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            p = root / ".claude/skills/alpha-one/SKILL.md"
            p.write_text(
                p.read_text()
                + "\n## Relationship to other skills\n\n"
                  "| Skill | How |\n|---|---|\n"
                  "| `beta-two` | fine |\n| `delta-four` | missing |\n",
                encoding="utf-8")
            found = failures(run(root), "skill-refs")
        self.assertEqual(len(found), 1)
        self.assertIn("delta-four", found[0])

    def test_kebab_words_outside_that_table_are_not_skill_refs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp)
            p = root / ".claude/skills/alpha-one/SKILL.md"
            p.write_text(p.read_text() + "\nWritten in `pt-BR`, set in `en-US`.\n",
                         encoding="utf-8")
            self.assertEqual(failures(run(root), "skill-refs"), [])


class TestPlaceholders(unittest.TestCase):
    def test_uninitialized_template_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = run(build(tmp))
        self.assertTrue(skipped(report, "placeholders"))
        self.assertEqual(failures(report, "placeholders"), [])

    def test_initialized_project_with_leftover_placeholder_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp, title='"Real Book"', author='"Ana Vilalba"')
            p = root / ".project/config/project.yaml"
            p.write_text(p.read_text().replace('subtitle: ""',
                                               'subtitle: "{Subtitle}"'),
                         encoding="utf-8")
            found = failures(run(root), "placeholders")
        self.assertEqual(len(found), 1)
        self.assertIn("{Subtitle}", found[0])

    def test_initialized_and_filled_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp, title='"Real Book"', author='"Ana Vilalba"')
            self.assertEqual(failures(run(root), "placeholders"), [])

    def test_fenced_entry_formats_are_not_blanks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp, title='"Real Book"', author='"Ana Vilalba"')
            (root / ".project/config/style-guide.md").write_text(
                "# Style\n\n```markdown\n- **cat. {N}:** {N,N}/1k. {Reason.}\n```\n",
                encoding="utf-8")
            self.assertEqual(failures(run(root), "placeholders"), [])

    def test_unfenced_blank_in_style_guide_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = build(tmp, title='"Real Book"', author='"Ana Vilalba"')
            (root / ".project/config/style-guide.md").write_text(
                "# Style\n\n## Quality target\n\n{How you define done.}\n",
                encoding="utf-8")
            found = failures(run(root), "placeholders")
        self.assertEqual(len(found), 1)


class TestRealRepository(unittest.TestCase):
    def test_this_repository_validates(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        report = run(root)
        self.assertEqual(report.failures, [], f"validate failed: {report.failures}")


if __name__ == "__main__":
    unittest.main()
