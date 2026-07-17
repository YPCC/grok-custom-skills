---
name: medium-article-generator
description: Generate Medium-ready MHTML (or HTML) articles from Markdown containing LaTeX equations. Uses Pandoc with SVG webtex (CodeCogs) by default and supports full offline local rendering via latex+dvisvgm as fallback. Always produces standalone HTML with explicit UTF-8 charset. Includes syntax highlighting for code and clean table output. Trigger on requests to create Medium articles, convert Markdown to Medium HTML/MHTML, render LaTeX equations for Medium, or produce publish-ready science/math posts.
---

# Medium Article Generator

Convert a Markdown article that contains LaTeX math into a clean, Medium-ready **MHTML** (default) or HTML file. Equations become properly rendered SVG images so they display correctly in Medium (which has no native LaTeX support).

## When to use

- User wants a Medium-ready version of a Markdown article that contains math.
- User asks to “render LaTeX for Medium”, “Markdown to Medium with equations”, “generate Medium HTML/MHTML”, or similar.
- User needs both online (fast) and offline (local TeX) paths.

## Quick start

```bash
# Preferred (online SVG → self-contained MHTML)
python3 scripts/generate_medium_html.py article.md

# Offline local rendering (no internet)
python3 scripts/generate_medium_html.py article.md --offline

# Explicit plain HTML instead of MHTML
python3 scripts/generate_medium_html.py article.md -o article.html

# Convenience wrapper
scripts/md2medium article.md --offline
```

## Core options

| Flag | Meaning |
|------|---------|
| `-o FILE` | Output path. Extension decides format: `.mhtml`/`.mht` → MHTML (default), `.html` → plain HTML |
| `--offline` | Force local rendering with `latex` + `dvisvgm` → SVG |
| `--png` | Use PNG instead of SVG in online mode |
| `--highlight-style STYLE` | Pandoc highlighter (default: `tango`). Others: `pygments`, `kate`, `espresso`, `zenburn`, `monochrome` |
| `--no-embed` | Offline only: keep external SVG files instead of data-URI embedding |
| `--bg COLOR` | Background for online CodeCogs images (default: `white`) |
| `--html-only` | Force plain HTML even if the extension suggests MHTML |

## How it works

### Standalone + UTF-8 (always)

The skill always invokes Pandoc with `-s` (standalone). This produces a full HTML document that includes an explicit `<meta charset="utf-8" />` declaration.  

As noted by Sam Vaseghi (Quantastic Journal update, 1 June 2026):

> This creates a full HTML document with an explicit UTF-8 declaration in the header. It avoids encoding problems. The articles may contain UTF-8 characters such as curly apostrophes, quotation marks, and accented letters, but the browser may interpret the HTML as an older encoding such as Windows-1252 or ISO-8859-1.

### Online mode (default)
Uses Pandoc’s `--webtex` pointing at the CodeCogs SVG endpoint with white background (exactly the method from the original article).

### Offline mode (`--offline`)
1. Pandoc produces HTML containing the original TeX inside MathJax-style spans.
2. Each unique equation is rendered locally (`standalone` + `amsmath` → `latex` → `dvisvgm`).
3. Math spans are replaced by `<img>` tags (data-URI by default).
4. MathJax script is stripped; light CSS for code blocks and tables is injected.

### MHTML packaging
After the HTML is ready, it is wrapped into a single-file MHTML (MIME HTML) archive. Because equations are embedded as data-URIs, the resulting `.mhtml` is completely self-contained and can be opened directly in Chrome, Edge, etc.

## Input requirements

- Markdown with standard Pandoc math: `$inline$` and `$$display$$`.
- Optional YAML front-matter (title, author, tags) is preserved.
- Fenced code blocks receive syntax highlighting.
- Pipe tables and grid tables become clean HTML tables.

## After generation

See `references/medium-import-tips.md` for the recommended copy-paste workflow into Medium’s editor.

## Dependencies

- Always: `pandoc`
- Offline mode: TeX Live (`latex`, `amsmath`, `standalone`) + `dvisvgm`
- Python standard library only (no extra packages required for MHTML)

## Agent instructions

When the skill is active:

1. Confirm the input Markdown file path with the user if not already given.
2. Prefer SVG + online mode → MHTML unless the user explicitly requests offline, PNG, or plain HTML.
3. Run the generator script from the skill directory.
4. After success, tell the user the output path and briefly remind them of the Medium paste workflow (open MHTML in browser → select → copy → paste into Medium).
5. If offline rendering fails for a particular equation, the original math span is left in place so the document remains usable.
6. Do not invent extra features beyond what the script supports; extend the script if new capabilities are needed.
