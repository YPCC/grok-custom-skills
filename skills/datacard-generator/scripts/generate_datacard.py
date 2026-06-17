#!/usr/bin/env python3
"""
Data Card Generator
===================
Generates a comprehensive Data Card following the Google PAIR Data Cards Playbook
structure for a dataset located in a given folder, augmented by optional context YAML/JSON
and automatic analysis of files, schemas, and metadata.

Usage:
  python generate_datacard.py --data-folder /path/to/dataset --output DataCard.md [options]

The script is intentionally dependency-light. pandas and jinja2 improve output quality
but are not strictly required (graceful fallback to basic Markdown scaffolding).
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# --- Optional dependencies (graceful fallback) ---
try:
    import yaml
except ImportError:
    yaml = None

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    HAS_JINJA = True
except ImportError:
    HAS_JINJA = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False


def find_key_files(root: Path) -> Dict[str, Path]:
    """Locate common metadata and documentation files."""
    candidates = {
        "readme": ["README.md", "README.txt", "README", "readme.md"],
        "license": ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"],
        "citation": ["CITATION.cff", "CITATION.bib", "citation.bib"],
        "metadata": ["metadata.json", "dataset.json", "datapackage.json"],
        "changelog": ["CHANGELOG.md", "HISTORY.md", "CHANGES.md"],
        "requirements": ["requirements.txt", "pyproject.toml", "setup.py"],
        "data_dict": ["data_dictionary.csv", "data_dictionary.xlsx", "schema.json", "columns.json"],
    }
    found = {}
    for key, names in candidates.items():
        for name in names:
            p = root / name
            if p.exists():
                found[key] = p
                break
            # Also check one level deep
            for sub in root.glob(f"*/{name}"):
                found[key] = sub
                break
    return found


def scan_folder(root: Path, max_files: int = 500) -> Dict[str, Any]:
    """Recursively scan folder for file types, sizes, and basic structure."""
    stats: Dict[str, Any] = {
        "root": str(root),
        "total_files": 0,
        "total_size_bytes": 0,
        "file_types": {},
        "top_level_dirs": [],
        "sample_files": [],
        "has_tabular": False,
        "tabular_files": [],
    }
    try:
        entries = list(root.rglob("*"))
    except Exception as e:
        stats["error"] = str(e)
        return stats

    for p in entries:
        if p.is_file():
            stats["total_files"] += 1
            try:
                size = p.stat().st_size
                stats["total_size_bytes"] += size
            except Exception:
                pass
            ext = p.suffix.lower() or "no_extension"
            stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
            if len(stats["sample_files"]) < 10:
                stats["sample_files"].append(str(p.relative_to(root)))
            if ext in {".csv", ".tsv", ".parquet", ".xlsx", ".xls", ".feather"}:
                stats["has_tabular"] = True
                if len(stats["tabular_files"]) < 5:
                    stats["tabular_files"].append(str(p.relative_to(root)))
        elif p.is_dir() and p.parent == root:
            stats["top_level_dirs"].append(p.name)

    stats["total_size_gb"] = round(stats["total_size_bytes"] / (1024**3), 3)
    stats["file_type_summary"] = ", ".join(
        f"{k}: {v}" for k, v in sorted(stats["file_types"].items(), key=lambda x: -x[1])[:8]
    )
    return stats


def analyze_tabular(file_path: Path, max_rows: int = 100_000) -> Dict[str, Any]:
    """Basic schema and sample analysis for a tabular file using pandas if available."""
    if not HAS_PANDAS:
        return {"error": "pandas not available", "path": str(file_path)}

    try:
        if file_path.suffix.lower() in {".csv", ".tsv"}:
            sep = "\t" if file_path.suffix.lower() == ".tsv" else ","
            df = pd.read_csv(file_path, sep=sep, nrows=max_rows, low_memory=False)
        elif file_path.suffix.lower() in {".parquet", ".feather"}:
            df = pd.read_parquet(file_path) if file_path.suffix == ".parquet" else pd.read_feather(file_path)
            if len(df) > max_rows:
                df = df.head(max_rows)
        elif file_path.suffix.lower() in {".xlsx", ".xls"}:
            df = pd.read_excel(file_path, nrows=max_rows)
        else:
            return {"error": "unsupported format"}

        analysis = {
            "path": str(file_path),
            "rows": int(len(df)),
            "columns": int(len(df.columns)),
            "dtypes": {str(k): str(v) for k, v in df.dtypes.items()},
            "missing_pct": {str(k): round(float(v), 2) for k, v in (df.isna().mean() * 100).items()},
            "sample_head": df.head(5).to_markdown(index=False) if len(df) > 0 else "empty",
            "numeric_summary": {},
        }
        # Basic numeric stats for first few numeric cols
        num_cols = df.select_dtypes(include=["number"]).columns.tolist()[:4]
        for col in num_cols:
            analysis["numeric_summary"][col] = {
                "mean": float(df[col].mean()) if not df[col].empty else None,
                "std": float(df[col].std()) if not df[col].empty else None,
                "min": float(df[col].min()) if not df[col].empty else None,
                "max": float(df[col].max()) if not df[col].empty else None,
            }
        return analysis
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}


def read_text_file(p: Path, max_chars: int = 8000) -> str:
    """Safely read and truncate text file content."""
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [truncated]"
        return text
    except Exception as e:
        return f"[Error reading {p.name}: {e}]"


def load_context(ctx_path: Optional[Path]) -> Dict[str, Any]:
    """Load additional context from YAML or JSON file."""
    if not ctx_path or not ctx_path.exists():
        return {}
    if ctx_path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            print("[WARN] PyYAML not installed. Cannot parse YAML context. Install with: pip install pyyaml", file=sys.stderr)
            return {}
        with open(ctx_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    elif ctx_path.suffix.lower() == ".json":
        with open(ctx_path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    else:
        print(f"[WARN] Unsupported context format: {ctx_path.suffix}. Use .yaml/.yml or .json", file=sys.stderr)
        return {}


def build_context(
    data_folder: Path,
    context: Dict[str, Any],
    stats: Dict[str, Any],
    key_files: Dict[str, Path],
) -> Dict[str, Any]:
    """Merge auto-detected info with user context into a single dict for templating."""
    ctx = dict(context)  # shallow copy; deep merge could be added if needed

    # Folder-derived basics
    ctx.setdefault("data_folder", str(data_folder))
    ctx.setdefault("scan_stats", stats)
    ctx.setdefault("generated_at", datetime.now().isoformat(timespec="seconds"))

    # README / metadata extraction (simple heuristics)
    if "readme" in key_files and "description" not in ctx:
        readme_text = read_text_file(key_files["readme"], max_chars=4000)
        # Very naive extraction: first paragraph-ish
        lines = [l.strip() for l in readme_text.splitlines() if l.strip()]
        if lines:
            ctx["description"] = " ".join(lines[:8])  # crude first block
            if "short_summary" not in ctx:
                ctx["short_summary"] = ctx["description"][:600]

    if "license" in key_files and "license" not in ctx:
        ctx["license"] = read_text_file(key_files["license"], max_chars=500).splitlines()[0]

    # Tabular analysis (first tabular file found)
    if stats.get("has_tabular") and stats.get("tabular_files") and HAS_PANDAS:
        first_tab = data_folder / stats["tabular_files"][0]
        tab_analysis = analyze_tabular(first_tab)
        if "error" not in tab_analysis:
            ctx.setdefault("snapshot", {})
            ctx["snapshot"].setdefault("num_records", tab_analysis.get("rows"))
            ctx["snapshot"].setdefault("num_fields", tab_analysis.get("columns"))
            ctx["sample_table"] = tab_analysis.get("sample_head", "")
            # crude modality inference
            if "modalities" not in ctx:
                ctx["modalities"] = ["Tabular (CSV/Parquet)"]
    else:
        if "modalities" not in ctx:
            exts = list(stats.get("file_types", {}).keys())
            if any(e in {".csv", ".parquet", ".xlsx"} for e in exts):
                ctx["modalities"] = ["Tabular data files"]
            elif any(e in {".json", ".jsonl"} for e in exts):
                ctx["modalities"] = ["JSON / structured records"]
            elif any(e in {".png", ".jpg", ".jpeg", ".dcm"} for e in exts):
                ctx["modalities"] = ["Image data"]
            else:
                ctx["modalities"] = ["Mixed / file-based dataset"]

    # Snapshot size
    if "snapshot" not in ctx:
        ctx["snapshot"] = {}
    ctx["snapshot"].setdefault("total_size_gb", stats.get("total_size_gb", 0))

    # File type summary for provenance / overview
    ctx.setdefault("file_type_summary", stats.get("file_type_summary", "See scan stats"))

    # Ensure nested dicts exist so Jinja attribute access never fails
    for key in ["version_maintenance", "sensitivity", "provenance", "access", "retention",
                "extended_use", "transformations", "annotations", "validation", "sampling",
                "reflections", "intended_uses", "owners", "publishers", "funding_sources",
                "primary_contact", "glossary", "applications", "changelog", "related_artifacts"]:
        ctx.setdefault(key, {} if key not in ["owners", "publishers", "funding_sources", "glossary", "applications", "changelog", "related_artifacts"] else [])

    return ctx


def render_markdown(ctx: Dict[str, Any], template_path: Path) -> str:
    """Render the Jinja2 template with context."""
    if not HAS_JINJA:
        # Fallback: very basic scaffolding
        title = ctx.get("title", "Untitled Dataset")
        summary = ctx.get("short_summary", "No summary provided.")
        return f"""# Data Card: {title}

**WARNING**: Jinja2 not installed. Install with `pip install jinja2 pyyaml pandas` for full templated output.

## Summary
{summary}

## Dataset Overview (auto-detected)
- Folder: {ctx.get('data_folder')}
- Files: {ctx.get('scan_stats', {}).get('total_files', 'N/A')}
- Size: {ctx.get('snapshot', {}).get('total_size_gb', 'N/A')} GB
- File types: {ctx.get('file_type_summary', 'N/A')}

See full template at assets/datacard_template.md.j2 and re-run with dependencies installed.
"""
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(template_path.name)
    return template.render(**ctx)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Data Card following Google PAIR Data Cards Playbook from a dataset folder + optional context.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--data-folder", "-d", type=Path, required=True, help="Path to the root folder containing the dataset files and metadata.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Output path for the generated Data Card (e.g. DataCard.md or .html).")
    parser.add_argument("--context-file", "-c", type=Path, default=None, help="Optional YAML or JSON file with additional known information (owners, motivations, sensitivity, etc.). See references/example_context.yaml.")
    parser.add_argument("--title", "-t", type=str, default=None, help="Override dataset title.")
    parser.add_argument("--format", "-f", choices=["markdown", "md", "html"], default="markdown", help="Output format (markdown recommended; html is basic preview).")
    parser.add_argument("--max-tabular-rows", type=int, default=100_000, help="Max rows to read for pandas analysis of tabular files.")
    args = parser.parse_args()

    data_folder = args.data_folder.resolve()
    if not data_folder.exists() or not data_folder.is_dir():
        print(f"[ERROR] data-folder does not exist or is not a directory: {data_folder}", file=sys.stderr)
        sys.exit(1)

    print(f"[INFO] Scanning {data_folder} ...")
    stats = scan_folder(data_folder)
    key_files = find_key_files(data_folder)
    print(f"[INFO] Found {stats['total_files']} files, {stats['total_size_gb']} GB. Key files: {list(key_files.keys())}")

    context = load_context(args.context_file)
    if args.title:
        context["title"] = args.title

    full_ctx = build_context(data_folder, context, stats, key_files)

    template_path = Path(__file__).parent.parent / "assets" / "datacard_template.md.j2"
    if not template_path.exists():
        print(f"[ERROR] Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    print("[INFO] Rendering Data Card ...")
    md_content = render_markdown(full_ctx, template_path)

    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if args.format in {"html"}:
        # Very basic HTML wrapper (for preview only)
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{full_ctx.get('title', 'Data Card')}</title>
<style>body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; line-height: 1.6; }} table {{ border-collapse: collapse; }} th, td {{ border: 1px solid #ccc; padding: 0.4rem 0.6rem; }} pre {{ background: #f8f8f8; padding: 1rem; overflow-x: auto; }}</style>
</head><body>
{md_content.replace('```', '<pre>').replace('```', '</pre>')}  <!-- crude -->
</body></html>"""
        output_path = output_path.with_suffix(".html")
        output_path.write_text(html, encoding="utf-8")
        print(f"[OK] Wrote HTML preview to {output_path}")
    else:
        output_path.write_text(md_content, encoding="utf-8")
        print(f"[OK] Wrote Markdown Data Card to {output_path}")

    print("\n[Next steps]")
    print("1. Review the generated file and address all [TODO] markers.")
    print("2. Provide or refine a context YAML for richer narrative sections (motivations, reflections, sensitivity, etc.).")
    print("3. Convert to DOCX/PDF using your preferred tooling or the pdf/docx skills for leadership review.")
    print("4. Load references/datacard-specification.md for detailed guidance per section.")


if __name__ == "__main__":
    main()