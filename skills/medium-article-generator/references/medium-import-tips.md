# Medium Import Tips

## Recommended workflow after generating the MHTML / HTML

1. Open the generated `.mhtml` (or `.html`) file in a browser that supports it
   (Chrome, Edge, and many others open MHTML natively).
2. Select the main article content.
3. Copy (Ctrl/Cmd+C).
4. In Medium’s editor, create a new story and paste.
5. Medium will convert most structure. Equation images usually appear correctly.
6. Manually fix any remaining issues:
   - Re-upload or re-position equation images if needed.
   - Adjust heading levels if Medium flattened them.
   - Check code blocks (they survive well thanks to the injected CSS).
   - Tables may need light manual cleanup in the Medium editor.

## Why standalone HTML + explicit UTF-8?

As noted by Sam Vaseghi (update 1 June 2026):

> I just added a standalone option "-s" to the pandoc command. This creates a full HTML document with an explicit UTF-8 declaration in the header. It avoids encoding problems. The articles may contain UTF-8 characters such as curly apostrophes, quotation marks, and accented letters, but the browser may interpret the HTML as an older encoding such as Windows-1252 or ISO-8859-1.

The skill always passes `-s` to Pandoc and writes UTF-8, so the charset meta tag is present.

## Why MHTML by default?

- Single self-contained file (HTML + all data-URI equation SVGs packaged together).
- Easy to archive, share, or open offline.
- Still trivial to open in a browser and copy-paste into Medium.

If you prefer plain HTML, pass `-o article.html` or `--html-only`.

## Offline mode notes

- Requires a working TeX Live installation with `latex`, `amsmath`, `standalone`, and `dvisvgm`.
- First run for a document may be slower (each unique equation is compiled once and cached by hash).
- By default SVGs are embedded as data URIs → the resulting MHTML is fully self-contained.
- Use `--no-embed` if you prefer external `.svg` files next to the HTML.

## Syntax highlighting

Pandoc’s built-in highlighters are used. Good choices for light backgrounds:

- `tango` (default) — clean, readable
- `pygments`
- `kate`
- `monochrome` (zero color)

## Tables

Standard Markdown pipe tables and grid tables are converted to clean HTML `<table>` elements with basic borders and header styling. Medium usually preserves them reasonably well on paste.
