"""Orchestration and reporting.

Exit codes: 0 complete, 1 nothing produced, 2 partial.
"""
import argparse
import sys
from pathlib import Path

from .chapters import find_chapters, LayoutError
from .config import load_config, ConfigError, format_number
from .engines import EngineError, find_tool, install_hint, run_pandoc
from .parse import parse_chapter
from .render import output_name, render_document
from .templates import (derive_reference_docx, epub_css, resolve_override,
                        typst_template)

MAX_REFUSALS_SHOWN = 6


def _report_chapter(parsed, language, out):
    if parsed.accepted:
        breaks = parsed.scene_breaks
        suffix = ", %d scene breaks" % breaks if breaks else ""
        out("  %-8s ok    %9s words%s"
            % (parsed.chapter_id, format_number(parsed.words, language),
               suffix))
        return

    out("  %-8s REFUSED" % parsed.chapter_id)
    for refusal in parsed.refusals[:MAX_REFUSALS_SHOWN]:
        out("           line %4d  %-14s %s"
            % (refusal.line, refusal.kind, refusal.text[:44]))
    remaining = len(parsed.refusals) - MAX_REFUSALS_SHOWN
    if remaining > 0:
        out("           ... %d more scaffolding lines" % remaining)
    out("")
    out("           This chapter is not written yet. Move the plan to")
    out("           %s_plot.md and leave the prose behind." % parsed.chapter_id)
    out("")


def _write_templates(cfg, profile, out_dir):
    typst_name = "%s.typ" % profile.name
    typst_path = out_dir / typst_name
    override = resolve_override(cfg.root, typst_name)
    typst_path.write_text(
        override.read_text(encoding="utf-8") if override
        else typst_template(cfg, profile), encoding="utf-8")

    css_path = out_dir / "epub.css"
    css_override = resolve_override(cfg.root, "epub.css")
    css_path.write_text(
        css_override.read_text(encoding="utf-8") if css_override
        else epub_css(profile), encoding="utf-8")
    return typst_path, css_path


def _metadata_args(cfg):
    return ["--metadata", "title=%s" % cfg.metadata.title,
            "--metadata", "author=%s" % cfg.metadata.author,
            "--metadata", "lang=%s" % cfg.metadata.language]


def _export_format(cfg, profile, chapters, fmt, context, out, warned):
    out_dir, pandoc, typst, typst_path, css_path = context
    render_fmt = "typst" if fmt == "pdf" else fmt

    source = out_dir / ("_%s.%s.md" % (profile.name, fmt))
    source.write_text(render_document(cfg, profile, chapters, render_fmt),
                      encoding="utf-8")

    extra = _metadata_args(cfg)
    if fmt == "docx":
        reference = resolve_override(cfg.root, "reference.docx")
        if reference is None:
            reference = derive_reference_docx(
                profile, pandoc, out_dir / ("_reference.%s.docx" % profile.name))
        extra += ["--reference-doc", str(reference)]
    elif fmt == "epub":
        extra += ["--css", str(css_path), "--split-level=1"]
    elif fmt == "pdf":
        if typst is None:
            out("")
            out("  skipped pdf (%s): typst is not installed." % profile.name)
            if "typst" not in warned:
                out(install_hint("typst"))
                warned.add("typst")
            return None
        extra += ["--pdf-engine=typst", "--template", str(typst_path)]

    target = out_dir / output_name(cfg, profile, fmt)
    run_pandoc(pandoc, source, target, extra)
    return target


def build_parser():
    parser = argparse.ArgumentParser(
        prog="export",
        description="Export the manuscript to .docx, .epub and .pdf.")
    parser.add_argument("--profile", default="all",
                        choices=["submission", "reading", "all"],
                        help="which profile to build (default: all)")
    parser.add_argument("--root", default=".",
                        help="project root (default: the current directory)")
    parser.add_argument("--out", default=None,
                        help="output directory (default: <root>/export)")
    parser.add_argument("--dump-templates", action="store_true",
                        help="write the generated templates and stop")
    parser.add_argument("--quiet", action="store_true",
                        help="print nothing but errors")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    out = (lambda *_: None) if args.quiet else (lambda text="": print(text))

    root = Path(args.root).resolve()
    try:
        cfg = load_config(root)
    except ConfigError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    out_dir = Path(args.out).resolve() if args.out else root / "export"
    out_dir.mkdir(parents=True, exist_ok=True)

    names = ["submission", "reading"] if args.profile == "all" \
        else [args.profile]

    if args.dump_templates:
        for name in names:
            _write_templates(cfg, cfg.profiles[name], out_dir)
        out("templates written to %s" % out_dir)
        return 0

    try:
        found = find_chapters(cfg.manuscript, cfg.layout, cfg.naming)
    except LayoutError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    if not found:
        print("error: no chapter found in %s\n"
              "Check paths.manuscript, paths.layout and paths.naming in "
              ".project/config/project.yaml." % cfg.manuscript,
              file=sys.stderr)
        return 1

    parsed = [parse_chapter(chapter) for chapter in found]
    for chapter in parsed:
        _report_chapter(chapter, cfg.metadata.language, out)

    accepted = [chapter for chapter in parsed if chapter.accepted]
    if not accepted:
        print("\nerror: no chapter was accepted, so nothing was written.",
              file=sys.stderr)
        return 1

    pandoc = find_tool("pandoc")
    if pandoc is None:
        print("\nerror: pandoc is not installed and nothing can be written.\n%s"
              % install_hint("pandoc"), file=sys.stderr)
        return 1
    typst = find_tool("typst")

    partial = len(accepted) < len(parsed)
    warned = set()
    for name in names:
        profile = cfg.profiles[name]
        typst_path, css_path = _write_templates(cfg, profile, out_dir)
        context = (out_dir, pandoc, typst, typst_path, css_path)
        for fmt in profile.formats:
            try:
                produced = _export_format(cfg, profile, accepted, fmt, context,
                                          out, warned)
            except EngineError as exc:
                print("\nerror: %s failed for the %s profile:\n%s"
                      % (fmt, name, exc), file=sys.stderr)
                return 1
            if produced is None:
                partial = True
            else:
                out("  wrote %s" % produced.name)

    out("")
    out("  %d of %d chapters exported -> %s"
        % (len(accepted), len(parsed), out_dir))
    return 2 if partial else 0
