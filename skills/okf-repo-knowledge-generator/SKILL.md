---
name: okf-repo-knowledge-generator
description: Generate Open Knowledge Format (OKF) bundles for any given repository (GitHub URL or local directory path). Analyzes structure, README, source files, configs and dependencies to produce hierarchical markdown concept documents with YAML frontmatter. Creates portable, versionable knowledge graphs for human/agent consumption and visualization. Trigger on requests like 'generate OKF for this repo', 'create knowledge bundle for github.com/org/repo', 'document this repository in OKF format', 'build OKF concepts from local code checkout'.
---

# OKF Repository Knowledge Generator

## When to Activate
Use this skill whenever the user wants structured, machine- and human-readable knowledge extracted from a software repository in the Open Knowledge Format (OKF). It is ideal for:
- Creating version-controlled knowledge catalogs of codebases (for RAG, onboarding, audits, or agentic workflows).
- Turning GitHub repos or local projects into interconnected concept graphs.
- Producing artifacts consumable by Obsidian, MkDocs, GraphDB, or the OKF visualization tools.
- Documenting complex multi-agent systems, clinical trial tools, healthcare AI repos, or any technical project the user is working on.

Do **not** use for non-repo content (use other skills) or trivial single-file scripts.

## Power User Workflow: code2prompt Integration
For medium-to-large repositories or when you want superior token control, filtering, and structured input, use the companion skill **`okf-code2prompt-workflow`** instead of (or in addition to) this one.

It provides:
- A custom Jinja2 template (`okf-context.j2`) optimized for OKF generation.
- Recommended `code2prompt` commands with smart filtering for clinical/multi-agent/FHIR repos.
- A helper script (`scripts/split_okf_context.py`) to turn code2prompt output into initial OKF skeletons.
- Full end-to-end pipeline documentation.

**Quick start**:
1. `pipx install code2prompt`
2. Use the commands documented in the `okf-code2prompt-workflow` skill.
3. Feed the resulting context file into this skill (or let the workflow skill orchestrate everything).

This combination produces higher-quality bundles with less manual effort on larger codebases.

## Core Principles
- Strictly follow the OKF specification (see `references/OKF-SPEC.md`).
- Every concept file **must** start with valid YAML frontmatter containing at least `type:`.
- Output is a self-contained directory (bundle) that can be committed to git, zipped, or visualized.
- Prefer local filesystem analysis when a path is provided (full access to all files). Fall back to GitHub connected tools (`github___get_file_contents`) for public repos specified by URL or owner/repo.
- Be selective: Do not dump entire files. Read key files, summarize intelligently, extract representative snippets, and infer architecture/relationships.
- Build a **graph** through markdown links between concepts.
- Keep concepts focused and reasonably sized.

## Input Handling
Accept one of:
- Local directory path (e.g. `/home/workdir/my-repo` or `.` after user clones).
- GitHub URL (https://github.com/owner/repo or tree/main/path).
- Explicit `owner` + `repo` + optional `ref` (branch/tag/sha).

If GitHub and private, user must have access via connected account or provide local clone. For very large repos, ask user to specify focus areas (e.g. "only the okf/ and src/enrichment_agent directories") or `--max-depth 2`.

Always confirm output location (default: `/home/workdir/artifacts/<sanitized-repo-name>-okf-knowledge/`). 

## Step-by-Step Generation Process

### 1. Discovery & Metadata Collection
- Verify input path exists or resolve GitHub coordinates.
- Capture source metadata: repo URL, current commit/SHA (use `git rev-parse HEAD` locally or GitHub tools), timestamp.
- Read primary README (try README.md, README.rst, README.txt). Produce a concise project summary (purpose, who it's for, core value prop, quick start).
- Detect tech stack:
  - Scan for manifest files: `pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `requirements*.txt`, `Pipfile`, `Dockerfile*`, `docker-compose*.yml`, `Makefile`, `.github/workflows/*`.
  - Note primary languages by extension counts or shebangs (limit scan with `find` excluding `node_modules`, `.git`, `dist`, `build`, `__pycache__`, `.venv`, `venv`).
- Capture high-level tree (2-3 levels): `find . -maxdepth 3 -type f -o -type d | grep -vE '(\.git|node_modules|__pycache__|\.venv|dist|build|target)' | head -60`

### 2. Define Concept Inventory
Based on discovery, decide on concepts to create. Typical set for most repos:

**Root level concepts (in bundle root):**
- `overview.md` — Executive summary + tech radar + Mermaid architecture diagram.
- `tech-stack.md` — Detailed languages, frameworks, major libraries with versions/purposes.
- `architecture.md` — Components, data/control flow, entrypoints, key design decisions. Include Mermaid flowchart or C4-style if complex.
- `log.md` — Generation audit trail (always create).

**Grouped concepts:**
- `key-files/` — Important non-code or config files (README variants, manifests, Dockerfiles, CI configs, entrypoint scripts). One .md per file or logical group.
- `modules/` or `src/` — Mirror logical code organization. Create subdirs for packages/namespaces. One concept per significant module/file (e.g. `modules/agents/triage.md`, `modules/orchestrator.md`).
- `dependencies/` — One concept per major external dependency or group (with why it's used, version constraints, alternatives considered).
- `docs/` or `documentation/` — If extensive docs/ folder exists, summarize or create concepts for key guides.
- `tests/` — Testing strategy, frameworks, coverage approach (if relevant and not too voluminous).
- `contributing.md`, `license.md`, `changelog.md` (or recent changes) — Summarize or excerpt.

Adapt names and structure to the specific repo (e.g. for the knowledge-catalog okf, have concepts for `enrichment_agent`, `SPEC.md`, `bundles/`, `samples/`). 

Prioritize files that reveal architecture: main entrypoints, core agents/orchestrators, data models, config loaders, API routers.

### 3. Analyze & Summarize Key Artifacts
For each selected file/concept:
- Fetch content (read_file with limit if huge, or github___get_file_contents with path; for dirs use path to list).
- Ask: What is the primary responsibility? What are the 3-5 most important functions/classes/configs it exposes? Who calls it or what does it call? Any notable patterns (LangGraph, FastAPI, GraphDB, etc.)?
- Extract 5-15 line representative code example (never full file unless tiny).
- Note imports/dependencies for relationship mapping.
- Record resource link back to original (GitHub blob URL with line numbers if possible, or relative local path + commit).

Use simple static analysis where helpful:
- `grep -r "from .* import\|import " --include="*.py" src/ | head -30` (or equivalent for other languages) to understand coupling.
- But do not over-index; focus on high-signal files.

### 4. Write the OKF Files
Use `bash mkdir -p $output_dir/key-files $output_dir/modules/...` etc.

For **every** `.md` concept file:

```yaml
---
type: "Repository Overview" | "Tech Stack" | "Architecture" | "Module" | "Source File" | "Dependency" | "Configuration" | "Documentation" | "Test Strategy" | ...
title: "Human readable title matching filename intent"
description: "One crisp sentence describing what this concept captures."
resource: "https://github.com/owner/repo/blob/<sha>/path/to/original.py#L10-L25"   # or local equivalent
tags: [python, langgraph, healthcare-ai, multi-agent, repository-analysis, ...]
timestamp: "2026-06-13T18:37:00Z"
okf_version: "0.1"
# any repo-specific: language: python, primary: true, loc_estimate: 312
---
```

**Body guidelines** (use these headings where natural):
- `# <Title>`
- Short prose intro.
- `## Purpose` or `## Responsibility`
- `## Key Interfaces / Exports / Config`
- `## Implementation Notes` or `## Code Example` (fenced block)
- `## Relationships` — prose + markdown links e.g. "Called by the [orchestrator](./orchestrator.md) and depends on [patient-event-graph](../modules/patient-event-graph.md)."
- `## Citations` — numbered list of sources (the repo itself is primary).
- End with any generation notes if non-obvious.

For `index.md` files (no frontmatter):
- Pure bullet list:
  ```markdown
  - [overview](overview.md) — Project purpose, tech stack summary and high-level architecture diagram.
  - [modules/orchestrator](modules/orchestrator.md) — Central LangGraph supervisor coordinating specialist agents.
  ```

Create `log.md` at root with:
```markdown
# Generation Log

## 2026-06-13T18:37:00Z
- Action: Initial generation
- Tool: okf-repo-knowledge-generator skill (Grok)
- Source: https://github.com/owner/repo @ <short-sha>
- Focus: full repo (or "limited to src/ and okf/")
- Concepts created: 12
- Notes: ...
```

### 5. Cross-Linking & Graph Construction
- In `overview.md` and `architecture.md` provide the "big picture" with links to all major concepts.
- Every module/file concept should link to its callers, callees, and related config/docs.
- Use **bundle-absolute links** starting with `/` for robustness (e.g. `/modules/foo.md`).
- Add Mermaid diagrams in overview/architecture for visual navigation (nodes = concepts, edges = relationships). Example:
  ```mermaid
  graph TD
      Overview --> Architecture
      Architecture --> Orchestrator
      Orchestrator --> TriageAgent
  ```

### 6. Validation & Polish
- After writing all files, run a quick check:
  - `find $output_dir -name "*.md" -exec grep -L "^---" {} \;` should return nothing (or only index.md / log.md).
  - All concepts have `type:` in frontmatter.
- Read back 1-2 key files to verify quality and links resolve logically.
- If issues found (missing type, broken description, poor linking), fix immediately with edit_file or rewrite.
- Optionally generate a root `README.md` in the bundle: "This is an OKF knowledge bundle generated for <repo>. See SPEC.md reference and original enrichment_agent for visualization tools."

### 7. Delivery
- Report the full path to the generated bundle.
- Offer next actions:
  - "Would you like me to generate the interactive viz.html using the OKF visualize approach?" (note: requires setting up the enrichment_agent env or we can create a lightweight alternative).
  - "Focus refinement on the architecture concept?"
  - "Zip the bundle?"
  - "Add web enrichment pass for official documentation pages?"
  - "Create a follow-up skill invocation for a different focus area or another repo."

## OKF Compliance Checklist (Enforce on Every Run)
- [ ] All concept .md files have opening `---` ... `type: ...` frontmatter.
- [ ] No frontmatter on `index.md` or `log.md`.
- [ ] Links use relative or `/bundle-root-relative` paths.
- [ ] Timestamps and source resources recorded.
- [ ] Content is accurate to the repo (no hallucinated APIs or files).
- [ ] Bundle is self-describing and standalone.

## Advanced / Future Extensions (Document if Used)
- Web enrichment pass: Accept seed URLs from README or user, use `browse_page` tool to pull official docs and enrich existing concepts or mint new `references/` concepts (similar to original enrichment_agent web pass).
- Deeper static analysis: Integrate tree-sitter or simple AST for function-level concepts (future script).
- Provenance/nanopublications: Add custom frontmatter or companion Turtle files if user requests semantic layer output.
- Multi-repo bundles: Merge knowledge from related repos (e.g. your clinical trial + this one).

## References & Further Reading
- `references/OKF-SPEC.md` — Full Open Knowledge Format specification and examples.
- Original OKF + enrichment_agent implementation: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf (browse the samples/ and bundles/ for inspiration on output quality and structure).
- Visualization: After generation, the bundle can be fed to the `enrichment_agent visualize` command from the OKF project for interactive Cytoscape HTML graph (nodes colored by type, clickable details, search, backlinks).

This skill turns any repository into a first-class, queryable, linkable knowledge asset following open standards.