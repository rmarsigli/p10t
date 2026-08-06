# Export templates

This directory is the escape hatch. **It ships empty on purpose.**

`scripts/export` generates every template it needs from
`.project/config/export.yaml`, so an ordinary project never needs a file
here. Drop one in and it wins:

| File | Overrides |
|---|---|
| `submission.typ` | the generated Typst template for the `submission` profile |
| `reading.typ` | the generated Typst template for the `reading` profile |
| `epub.css` | the generated EPUB stylesheet |
| `reference.docx` | the derived Word reference document |

Precedence is: **a file here → `export.yaml` → the built-in default.**

Two notes:

- A `.typ` here is a **pandoc template**, not a plain Typst document, so it
  must contain `$body$` where the manuscript goes.
- A `reference.docx` here is *your* binary, in the one directory documented
  to hold one. p10t itself never commits a binary — it patches pandoc's
  default at run time instead.

To start from what the script would have produced rather than from nothing:

```sh
scripts/export --profile submission --dump-templates
```

That writes the generated templates into `export/`, where you can copy one
here and edit it.
