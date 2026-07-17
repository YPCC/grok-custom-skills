#!/usr/bin/env python3
"""
Medium-ready article generator from Markdown with LaTeX math.

Primary output: MHTML (.mhtml) — single-file archive with embedded resources.
Also supports plain HTML.

- Online (default): SVG via CodeCogs webtex (high quality).
- Offline fallback: local latex + dvisvgm → SVG (data-URI embedded).
- Always uses Pandoc -s (standalone) for a full HTML document with explicit UTF-8
  charset declaration (avoids encoding problems with curly quotes, accents, etc.).
- Syntax highlighting for code blocks + clean table styling.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import re
import shutil
import subprocess
import sys
from email.generator import BytesGenerator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Local math renderer (latex + dvisvgm → SVG)
# ---------------------------------------------------------------------------

LOCAL_PREAMBLE = r"""
\documentclass[preview,border=1pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts,mathtools}
\usepackage{xcolor}
\begin{document}
"""

def _hash_math(tex: str, display: bool) -> str:
    key = ("D" if display else "I") + tex
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def render_math_local(tex: str, display: bool, out_dir: Path) -> Optional[Path]:
    """Render a single math fragment to SVG using latex + dvisvgm.
    Returns path to the SVG file or None on failure.
    """
    h = _hash_math(tex, display)
    svg_path = out_dir / f"eq_{h}.svg"
    if svg_path.exists():
        return svg_path

    work = out_dir / f"tmp_{h}"
    work.mkdir(exist_ok=True)
    tex_file = work / "eq.tex"

    body = f"\\[{tex}\\]" if display else f"${tex}$"
    content = LOCAL_PREAMBLE + body + "\n\\end{document}\n"
    tex_file.write_text(content, encoding="utf-8")

    try:
        subprocess.run(
            ["latex", "-interaction=nonstopmode", "-halt-on-error", "eq.tex"],
            cwd=work,
            capture_output=True,
            check=True,
            timeout=30,
        )
        subprocess.run(
            [
                "dvisvgm",
                "--no-fonts",
                "--exact",
                "--optimize",
                "--output=eq.svg",
                "eq.dvi",
            ],
            cwd=work,
            capture_output=True,
            check=True,
            timeout=30,
        )
        shutil.move(str(work / "eq.svg"), str(svg_path))
        return svg_path
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        if work.exists():
            shutil.rmtree(work, ignore_errors=True)
        return None
    finally:
        if work.exists():
            shutil.rmtree(work, ignore_errors=True)


def svg_to_data_uri(svg_path: Path) -> str:
    data = svg_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


# ---------------------------------------------------------------------------
# Pandoc helpers
# ---------------------------------------------------------------------------

def run_pandoc(
    md_path: Path,
    html_path: Path,
    *,
    webtex_url: Optional[str] = None,
    highlight_style: str = "tango",
    standalone: bool = True,
    extra_args: list[str] | None = None,
) -> None:
    """Always prefer standalone (-s) so the result is a full HTML document
    with an explicit UTF-8 charset declaration in the header. This avoids
    encoding problems with curly apostrophes, quotation marks, and accented
    letters (as noted in the Quantastic Journal update of 1 June 2026).
    """
    cmd = [
        "pandoc",
        str(md_path),
        "-f", "markdown+yaml_metadata_block+tex_math_dollars+pipe_tables+grid_tables+table_captions+fenced_code_attributes+fenced_divs",
        "-t", "html5",
        "--highlight-style", highlight_style,
        "-o", str(html_path),
    ]
    if standalone:
        cmd.append("-s")
    if webtex_url:
        cmd.append(f"--webtex={webtex_url}")
    if extra_args:
        cmd.extend(extra_args)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc failed:\n{result.stderr}")


# ---------------------------------------------------------------------------
# CSS injected into every document
# ---------------------------------------------------------------------------

MEDIUM_CSS = """
<style>
/* Medium-friendly extras + UTF-8 safe rendering */
pre, code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
pre { background: #f6f8fa; padding: 1em; border-radius: 6px; overflow-x: auto; }
table { border-collapse: collapse; margin: 1.2em 0; width: 100%; }
th, td { border: 1px solid #d0d7de; padding: 0.5em 0.8em; text-align: left; }
th { background: #f6f8fa; font-weight: 600; }
img.math-inline { vertical-align: middle; }
.math-display { text-align: center; margin: 1.5em 0; }
img { max-width: 100%; height: auto; vertical-align: middle; }
</style>
"""


def inject_css(html: str) -> str:
    if "</head>" in html:
        return html.replace("</head>", MEDIUM_CSS + "\n</head>")
    return MEDIUM_CSS + html


# ---------------------------------------------------------------------------
# Offline mode
# ---------------------------------------------------------------------------

MATH_INLINE_RE = re.compile(
    r'<span class="math inline">\\\((.+?)\\\)</span>',
    re.DOTALL,
)
MATH_DISPLAY_RE = re.compile(
    r'<span class="math display">\\\[(.+?)\\\]</span>',
    re.DOTALL,
)


def convert_offline(
    md_path: Path,
    html_path: Path,
    *,
    highlight_style: str = "tango",
    embed: bool = True,
) -> None:
    """Full offline conversion: produce HTML with local SVG images for every math."""
    img_dir = html_path.parent / (html_path.stem + "_eqs")
    img_dir.mkdir(exist_ok=True)

    tmp_html = html_path.with_suffix(".tmp.html")
    run_pandoc(
        md_path,
        tmp_html,
        webtex_url=None,
        highlight_style=highlight_style,
        standalone=True,
        extra_args=["--mathjax"],
    )

    html = tmp_html.read_text(encoding="utf-8")

    def repl_inline(m: re.Match) -> str:
        tex = m.group(1).strip()
        tex = (
            tex.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
        )
        svg = render_math_local(tex, display=False, out_dir=img_dir)
        if svg is None:
            return m.group(0)
        if embed:
            src = svg_to_data_uri(svg)
        else:
            src = svg.name
        return (
            f'<img class="math-inline" src="{src}" '
            f'alt="{tex}" style="vertical-align: middle; height: 1.1em;" />'
        )

    def repl_display(m: re.Match) -> str:
        tex = m.group(1).strip()
        tex = (
            tex.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
        )
        svg = render_math_local(tex, display=True, out_dir=img_dir)
        if svg is None:
            return m.group(0)
        if embed:
            src = svg_to_data_uri(svg)
        else:
            src = svg.name
        return (
            f'<div class="math-display" style="text-align:center; margin: 1.2em 0;">'
            f'<img src="{src}" alt="{tex}" style="max-width:100%; height:auto;" />'
            f"</div>"
        )

    html = MATH_INLINE_RE.sub(repl_inline, html)
    html = MATH_DISPLAY_RE.sub(repl_display, html)

    # Strip MathJax script (no longer needed)
    html = re.sub(
        r'<script[^>]*src="[^"]*[Mm]ath[Jj]ax[^"]*"[^>]*>\s*</script>',
        "",
        html,
        flags=re.IGNORECASE,
    )

    html = inject_css(html)
    html_path.write_text(html, encoding="utf-8")
    tmp_html.unlink(missing_ok=True)

    if embed:
        shutil.rmtree(img_dir, ignore_errors=True)
    else:
        print(f"Equation images written to: {img_dir}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Online (webtex) mode
# ---------------------------------------------------------------------------

def convert_online(
    md_path: Path,
    html_path: Path,
    *,
    svg: bool = True,
    highlight_style: str = "tango",
    bg: str = "white",
) -> None:
    if svg:
        url = f"https://latex.codecogs.com/svg.latex?\\bg{{{bg}}}%20"
    else:
        url = f"https://latex.codecogs.com/png.latex?\\bg{{{bg}}}%20"

    run_pandoc(
        md_path,
        html_path,
        webtex_url=url,
        highlight_style=highlight_style,
        standalone=True,
    )

    html = html_path.read_text(encoding="utf-8")
    html = inject_css(html)
    html_path.write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# MHTML packaging
# ---------------------------------------------------------------------------

def html_to_mhtml(html_content: str, title: str = "Medium Article") -> bytes:
    """Wrap a complete HTML document (preferably with data-URI images)
    into a single MHTML (MIME HTML) archive.
    """
    # Root multipart/related
    msg = MIMEMultipart("related")
    msg["Subject"] = title
    msg["MIME-Version"] = "1.0"
    # Some browsers look for this
    msg.preamble = "This is a multi-part message in MIME format."

    # The main HTML part
    html_part = MIMEText(html_content, "html", "utf-8")
    html_part.add_header("Content-Location", "index.html")
    # Let the email library choose a suitable Content-Transfer-Encoding
    # (usually base64 for content that contains data-URIs).
    msg.attach(html_part)

    # Serialize
    buf = BytesIO()
    gen = BytesGenerator(buf, mangle_from_=False)
    gen.flatten(msg)
    return buf.getvalue()


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip() or "Medium Article"
    return "Medium Article"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Medium-ready MHTML (or HTML) from Markdown with LaTeX equations (SVG preferred)."
    )
    parser.add_argument("input", type=Path, help="Input Markdown file (.md)")
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output file. Extension decides format: .mhtml/.mht → MHTML (default), .html → plain HTML.",
    )
    parser.add_argument(
        "--offline", action="store_true",
        help="Force offline local rendering (latex + dvisvgm). Default is online SVG via CodeCogs.",
    )
    parser.add_argument(
        "--png", action="store_true",
        help="Use PNG instead of SVG for online mode (ignored in offline mode).",
    )
    parser.add_argument(
        "--highlight-style", default="tango",
        help="Pandoc syntax highlight style (default: tango). Try: pygments, espresso, zenburn, kate, monochrome",
    )
    parser.add_argument(
        "--no-embed", action="store_true",
        help="In offline mode, keep external SVG files instead of data-URI embedding.",
    )
    parser.add_argument(
        "--bg", default="white",
        help="Background color for online CodeCogs images (default: white).",
    )
    parser.add_argument(
        "--html-only", action="store_true",
        help="Force plain HTML output even if the extension suggests MHTML.",
    )

    args = parser.parse_args()

    md_path = args.input.resolve()
    if not md_path.is_file():
        print(f"Error: input file not found: {md_path}", file=sys.stderr)
        return 1

    # Decide output path and format
    if args.output is None:
        out_path = md_path.with_suffix(".mhtml")
    else:
        out_path = args.output.resolve()

    want_mhtml = (out_path.suffix.lower() in {".mhtml", ".mht"}) and not args.html_only

    # Intermediate HTML always written first (may be temporary)
    if want_mhtml:
        html_path = out_path.with_suffix(".tmp.html")
    else:
        html_path = out_path

    print(f"Input : {md_path}", file=sys.stderr)
    print(f"Output: {out_path} ({'MHTML' if want_mhtml else 'HTML'})", file=sys.stderr)

    try:
        if args.offline:
            print("Mode  : offline (local latex + dvisvgm → SVG)", file=sys.stderr)
            convert_offline(
                md_path,
                html_path,
                highlight_style=args.highlight_style,
                embed=not args.no_embed,
            )
        else:
            fmt = "PNG" if args.png else "SVG"
            print(f"Mode  : online CodeCogs ({fmt})", file=sys.stderr)
            convert_online(
                md_path,
                html_path,
                svg=not args.png,
                highlight_style=args.highlight_style,
                bg=args.bg,
            )

        if want_mhtml:
            html_content = html_path.read_text(encoding="utf-8")
            title = extract_title(html_content)
            mhtml_bytes = html_to_mhtml(html_content, title=title)
            out_path.write_bytes(mhtml_bytes)
            html_path.unlink(missing_ok=True)
            print(f"Wrote self-contained MHTML archive: {out_path}", file=sys.stderr)
        else:
            print(f"Wrote HTML: {out_path}", file=sys.stderr)

        print("Done.", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
