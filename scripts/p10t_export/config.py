"""Loads project.yaml and export.yaml into typed configuration.

Metadata always comes from project.yaml and is never duplicated in
export.yaml. Profile values fall back to built-in defaults, so a project
with no export.yaml still exports.
"""
from dataclasses import dataclass, field
from pathlib import Path

from .yamlish import parse, YamlishError


class ConfigError(Exception):
    pass


DEFAULT_PROFILES = {
    "submission": {
        "formats": ["docx", "pdf"],
        "font": "Courier New",
        "size": "12pt",
        "leading": "double",
        "indent": "1.27cm",
        "margins": "2.54cm",
        "scene_break": "#",
        "title_case": "upper",
        "chapter_starts": "new_page",
        "running_head": "{author_last} / {title} / {page}",
        "title_page": ["contact", "wordcount", "title", "byline",
                       "audience", "genre"],
    },
    "reading": {
        "formats": ["epub", "pdf"],
        "font": "EB Garamond",
        "size": "11pt",
        "leading": "1.3",
        "indent": "1em",
        "margins": "2.2cm",
        "scene_break": "* * *",
        "title_case": "none",
        "chapter_starts": "new_page",
        "running_head": "{title}",
        "title_page": ["title", "byline"],
    },
}

LABELS = {
    "en": {"wordcount": "Word count", "byline": "by",
           "novel_by": "a novel by", "the_end": "THE END"},
    "pt-BR": {"wordcount": "Contagem de palavras", "byline": "por",
              "novel_by": "um romance de", "the_end": "FIM"},
}


@dataclass
class Metadata:
    title: str
    author: str
    language: str
    audience: str = ""
    genre: str = ""

    @property
    def author_last(self):
        parts = self.author.split()
        return parts[-1] if parts else self.author


@dataclass
class Contact:
    name: str = ""
    address: list = field(default_factory=list)
    phone: str = ""
    email: str = ""

    @property
    def is_empty(self):
        return not (self.name or self.address or self.phone or self.email)


@dataclass
class Profile:
    name: str
    formats: list
    font: str
    size: str
    leading: str
    indent: str
    margins: str
    scene_break: str
    title_case: str
    chapter_starts: str
    running_head: str
    title_page: list


@dataclass
class ExportConfig:
    metadata: Metadata
    contact: Contact
    labels: dict
    profiles: dict
    manuscript: Path
    layout: str
    naming: str
    root: Path


def default_labels(language):
    return dict(LABELS.get(language, LABELS["en"]))


def format_number(n, language):
    grouped = "{:,}".format(int(n))
    return grouped.replace(",", ".") if language == "pt-BR" else grouped


def _read(path):
    if not path.exists():
        return {}
    try:
        return parse(path.read_text(encoding="utf-8")) or {}
    except YamlishError as exc:
        raise ConfigError("%s: %s" % (path, exc))


def _unfilled(value):
    """A template placeholder such as "{Title}" is not a real value."""
    return not value or str(value).startswith("{")


def load_config(project_root):
    root = Path(project_root)
    config_dir = root / ".project" / "config"
    project = _read(config_dir / "project.yaml")
    export = _read(config_dir / "export.yaml")

    title = project.get("title") or ""
    author = project.get("author") or ""
    if _unfilled(title):
        raise ConfigError(
            "project.yaml has no title. The title page would lie, so nothing "
            "was written. Run init-project, or set title: in "
            ".project/config/project.yaml.")
    if _unfilled(author):
        raise ConfigError(
            "project.yaml has no author. The title page would lie, so nothing "
            "was written. Set author: in .project/config/project.yaml.")

    language = project.get("language") or "en"
    genre = project.get("genre") or {}
    paths = project.get("paths") or {}

    metadata = Metadata(
        title=title,
        author=author,
        language=language,
        audience=genre.get("audience") or "",
        genre=genre.get("primary") or "",
    )

    raw_contact = export.get("contact") or {}
    contact = Contact(
        name=raw_contact.get("name") or "",
        address=list(raw_contact.get("address") or []),
        phone=raw_contact.get("phone") or "",
        email=raw_contact.get("email") or "",
    )

    labels = default_labels(language)
    labels.update({k: v for k, v in (export.get("labels") or {}).items() if v})

    profiles = {}
    configured = export.get("profiles") or {}
    for name, defaults in DEFAULT_PROFILES.items():
        merged = dict(defaults)
        merged.update({k: v for k, v in (configured.get(name) or {}).items()
                       if v not in (None, "")})
        profiles[name] = Profile(name=name, **merged)

    return ExportConfig(
        metadata=metadata,
        contact=contact,
        labels=labels,
        profiles=profiles,
        manuscript=root / (paths.get("manuscript") or "manuscript/"),
        layout=paths.get("layout") or "flat",
        naming=paths.get("naming") or "{act}.{chapter}.md",
        root=root,
    )
