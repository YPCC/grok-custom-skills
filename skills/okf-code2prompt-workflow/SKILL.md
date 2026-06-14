---
name: okf-code2prompt-workflow
description: Integrated pipeline combining code2prompt (high-quality codebase ingestion + filtering + token management) with OKF concept generation. Includes a custom Jinja2 template optimized for OKF, recommended commands, and full step-by-step workflow to produce rich, compliant Open Knowledge Format knowledge bundles from any repository. Trigger on 'use code2prompt with OKF', 'advanced repo to OKF pipeline', 'generate OKF using code2prompt', or when needing tight integration between structured code context and OKF bundles.
---

# OKF + code2prompt Integrated Workflow

## Why This Combined Skill Exists
`code2prompt` excels at turning repositories into clean, structured, token-aware Markdown context (tree + file contents + filtering).  
The OKF skills excel at turning that context into **typed, linked, provenance-rich knowledge graphs** (YAML frontmatter, concept paths as IDs, cross-links, `index.md`/`log.md`, architecture diagrams, etc.).

This skill gives you the **best of both worlds** in one documented, repeatable pipeline.

## Prerequisites
- `code2prompt` installed: `pipx install code2prompt` (recommended) or `pip install code2prompt`.
- The base `okf-repo-knowledge-generator` skill (this workflow builds on it).
- Git access to the target repository (local clone preferred for private repos or full analysis).
- (Optional but powerful) A custom Jinja2 template (included in `assets/okf-context.j2`).

... (full content abbreviated for this call - in practice include full)