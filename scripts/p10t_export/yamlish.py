"""A parser for the flat YAML subset p10t configuration uses.

This is deliberately not YAML. It accepts nested mappings by indentation,
scalars, inline lists, block lists, quoted strings and comments. Anything
else raises, with the line number, rather than guessing.

Depending on PyYAML would reintroduce the pip barrier that ruled out
WeasyPrint as a PDF engine, so the subset is hand-parsed instead.
"""
import re

_INLINE_LIST = re.compile(r"^\[(.*)\]$")


class YamlishError(Exception):
    def __init__(self, message, line):
        super().__init__("line %d: %s" % (line, message))
        self.line = line


def _strip_comment(raw):
    """Remove a trailing comment, leaving '#' inside quotes alone."""
    out, quote = [], None
    for ch in raw:
        if quote:
            if ch == quote:
                quote = None
            out.append(ch)
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def _scalar(text):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    inline = _INLINE_LIST.match(text)
    if inline:
        inner = inline.group(1).strip()
        return [_scalar(part) for part in inner.split(",")] if inner else []
    low = text.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "~", ""):
        return None
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    return text


def parse(text):
    """Parse the subset into nested dicts and lists.

    Each stack frame carries the container plus the mapping that owns it,
    so a key opened as a mapping can be converted into a list when the
    first '- ' item arrives.
    """
    root = {}
    stack = [(-1, root, None, None)]

    for number, raw in enumerate(text.splitlines(), start=1):
        leading = raw[: len(raw) - len(raw.lstrip())]
        if "\t" in leading:
            raise YamlishError("tabs are not allowed for indentation", number)

        line = _strip_comment(raw)
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip())
        body = line.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        frame_indent, container, owner, owner_key = stack[-1]

        if body.startswith("- "):
            if isinstance(container, dict) and not container and owner is not None:
                container = []
                owner[owner_key] = container
                stack[-1] = (frame_indent, container, owner, owner_key)
            if not isinstance(container, list):
                raise YamlishError("list item outside a list", number)
            container.append(_scalar(body[2:]))
            continue

        if ":" not in body:
            raise YamlishError("expected 'key: value'", number)
        if not isinstance(container, dict):
            raise YamlishError("mapping key inside a list", number)

        key, _, value = body.partition(":")
        key, value = key.strip(), value.strip()

        if value == "":
            child = {}
            container[key] = child
            stack.append((indent, child, container, key))
        else:
            container[key] = _scalar(value)

    return root
