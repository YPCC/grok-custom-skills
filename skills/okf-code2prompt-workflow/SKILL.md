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

## Custom Jinja2 Template (Included)
Location: `assets/okf-context.j2`

This template is specifically designed to produce output that is easy for the OKF skill to consume:
- Clean project header with token estimate.
- Hierarchical source tree (ready for `index.md` generation).
- Per-file sections with **suggested OKF `type`** and `tags` hints.
- Code blocks with language info.
- Explicit "Notes for OKF Skill" section to guide enrichment.

**Recommended invocation** (copy-paste and adapt):

```bash
code2prompt \
  --path /path/to/your-repo \
  --template /home/workdir/.grok/skills/okf-code2prompt-workflow/assets/okf-context.j2 \
  --output /tmp/repo_okf_context.md \
  --filter "*.py,*.md,pyproject.toml,setup.py,*.yaml,*.yml,Dockerfile*,Makefile,.github/workflows/*" \
  --exclude "tests/*,test_*,node_modules/*,.git/*,.venv/*,venv/*,dist/*,build/*,__pycache__/*,*.pyc,*.egg-info" \
  --line-number \
  --tokens
```

**Key flags explained**:
- `--template`: Uses our OKF-optimized template.
- `--filter`: Only include high-value files for knowledge generation.
- `--exclude`: Aggressively remove noise (tests, build artifacts, venvs). Adjust per language/ecosystem.
- `--line-number`: Makes code references precise (great for OKF `resource` links with line numbers).
- `--tokens`: Shows context size upfront.

You can also run without the custom template first (default template is already very good) and let this skill post-process.

## Full Combined Workflow (Step by Step)

### Phase 1: High-Quality Context Generation (code2prompt)
1. Clone or navigate to the target repository.
2. Run the `code2prompt` command above (or a simpler version without custom template).
3. Review `/tmp/repo_okf_context.md`:
   - Check token count.
   - Verify important files are included and noise is excluded.
   - If needed, adjust `--filter`/`--exclude` and re-run (very fast).

**Alternative (no custom template)**:
```bash
code2prompt --path . --output /tmp/repo_context.md --tokens --line-number \
  --filter "*.py,*.md,pyproject.toml,Dockerfile*" \
  --exclude "tests/*,.venv/*,dist/*,build/*"
```

### Phase 2: OKF Bundle Generation (using okf-repo-knowledge-generator)
Feed the context file into the base OKF skill with instructions like:

> "Using the okf-repo-knowledge-generator skill, create a full OKF knowledge bundle from the code2prompt output at /tmp/repo_okf_context.md. 
> Source repository: https://github.com/org/repo
> Focus areas: multi-agent architecture, FHIR integration, core orchestration logic.
> Output to: /home/workdir/artifacts/my-repo-okf-knowledge/"

The OKF skill will:
- Parse the tree → generate `index.md` files.
- Turn high-signal files into proper OKF concepts with YAML frontmatter (`type: Source File / Module / Configuration`, etc.).
- Enrich with summaries, key interfaces, code examples, and inferred relationships.
- Create `overview.md`, `architecture.md` (with Mermaid), `tech-stack.md`, `log.md`.
- Build a connected knowledge graph via internal links.
- Add provenance (source commit/SHA, generation timestamp, tool chain).

### Phase 3: Validation & Enrichment (Optional but Recommended)
- Open the generated bundle and spot-check 2–3 concepts.
- Ask for targeted refinements: "Improve the architecture concept with more detail on LangGraph flows" or "Add web enrichment for official docs mentioned in README".
- Run the OKF visualize approach (from the original knowledge-catalog repo) on the final bundle for an interactive graph view.
- Commit the bundle to git (excellent for versioning knowledge alongside code).

## Advanced Patterns

### Pattern A: Iterative / Focused Generation
For very large repos:
1. First pass: Broad but shallow with code2prompt (high-level tree + key manifests + READMEs).
2. Identify core modules from the tree.
3. Second pass: Targeted `code2prompt` on specific subdirectories + deep OKF enrichment.
4. Merge concepts into one bundle.

### Pattern B: Custom Filtering per Domain
Healthcare / Clinical / Multi-agent repos (your common use case):
```bash
--filter "*.py,*.md,pyproject.toml,*.yaml,fhir*,agent*,orchestrat*" \
--exclude "tests/*,frontend/*,docs/_build/*"
```

### Pattern C: Post-processing Script (Future)
A small helper in `scripts/` could:
- Split the single `repo_okf_context.md` into initial OKF skeleton files.
- Pre-create directories matching the tree.
- Inject basic frontmatter.
This would make the pipeline even more automated (can be added on request).

## When to Use This Workflow vs Base OKF Skill
- **Use this combined workflow** when: repo is medium-large, you want excellent token control + clean input, or you frequently analyze multiple repos.
- **Use base `okf-repo-knowledge-generator` directly** when: repo is small, you already have a clean context, or you prefer fully manual/selective file reading.

## Output
You will receive a complete, OKF-compliant knowledge bundle directory ready for:
- Human browsing (Obsidian, VS Code, MkDocs).
- Agent consumption (RAG, Graph RAG, tool use).
- Visualization (Cytoscape HTML via original OKF tools).
- Version control and collaboration.

## References
- Base skill: `okf-repo-knowledge-generator`
- Original OKF spec & tools: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
- code2prompt: https://github.com/raphaelmansuy/code2prompt
- Custom template: `assets/okf-context.j2` (included in this skill)

This pipeline turns raw repositories into production-grade, queryable knowledge assets with minimal manual effort while preserving full control and OKF compliance.