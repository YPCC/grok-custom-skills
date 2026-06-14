# Open Knowledge Format (OKF) Specification v0.1

**Source**: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

## Purpose
OKF is a minimal, open format for representing knowledge (metadata, context, curated insights) in a way that is human-readable, agent-parseable, version-control-friendly, and portable. It uses a directory of markdown files with YAML frontmatter, requiring no schema registry, central authority, or specialized tooling.

## Key Components

### Knowledge Bundle
A self-contained, hierarchical collection of knowledge documents (concepts) distributed as a git repository, tarball, or subdirectory. It organizes concepts in any directory structure.

### Concept
A single markdown file representing a unit of knowledge (e.g., a table, API, metric, playbook, source file, module, architecture decision). Each concept has:
- **YAML frontmatter** (required: `type`; optional: `title`, `description`, `resource`, `tags`, `timestamp`, and custom fields)
- **Markdown body** (supports structured content like tables, lists, code blocks, Mermaid diagrams)

### Concept ID
The file path within the bundle, with `.md` removed (e.g., `tables/users.md` → `tables/users` or `modules/agent/llm.md` → `modules/agent/llm`).

### Frontmatter
YAML metadata block at the top of each concept file, delimited by `---`. 

Must include:
- `type` (e.g., `BigQuery Table`, `Playbook`, `Source File`, `Module`, `Repository Overview`, `Dependency`, `Architecture`)

Recommended/optional:
- `title`
- `description`
- `resource` (URL or path to original)
- `tags` (list)
- `timestamp` (ISO 8601)
- Custom: e.g. `language`, `loc`, `complexity`

### Body
Standard markdown content. Conventional headings like `# Schema`, `# Examples`, `# Citations`, `# Purpose`, `# Relationships` have implied meaning for consumers.

### Links
Markdown links connect concepts:
- Absolute (bundle-relative): `/path/to/concept.md` (preferred for portability)
- Relative: `./other.md` or `../sibling.md`

Links express relationships (e.g. imports, references, data flows, foreign keys) via prose context around the link.

### Index Files (`index.md`)
Optional files that list contents of a directory for progressive disclosure. 
- No frontmatter.
- Uses bullet lists with titles, links, and short descriptions.
- Example:
  ```markdown
  - [overview](overview.md) — High-level summary of the repository purpose and tech stack.
  - [architecture](architecture.md) — Core components and data flows.
  ```

### Log Files (`log.md`)
Optional, records update history with date-grouped entries (ISO 8601 dates). Supports actions like `Update`, `Creation`, `Deprecation`, `Generation`.

Example entry:
```markdown
## 2026-06-13
- Generation: Initial OKF bundle created from GitHub repository analysis using okf-repo-knowledge-generator skill.
- Source: https://github.com/example/repo @ abc1234
```

### Citations
External sources supporting claims, listed under `# Citations` with numbered links (URLs or bundle paths).

## Generation Guidelines for Repositories
- **Structure**: A bundle is a directory tree of `.md` files. Reserved: `index.md`, `log.md`. All other `.md` are concepts.
- **Conformance**: All concept files must have parseable frontmatter with at least `type:`.
- **Extensibility**: Add custom frontmatter keys freely; consumers tolerate unknowns.
- **Versioning**: Bundles may declare `okf_version: "0.1"` in root `index.md` frontmatter (even if spec says index has no frontmatter, some put metadata there).
- **Cross-Linking**: Build a graph of knowledge via links. Use in overview/architecture to tie everything together.
- **For Code Repos**: Typical concept types: `Repository Overview`, `Tech Stack`, `Architecture`, `Module`, `Source File`, `Configuration`, `Dependency`, `Test Suite`, `Documentation`, `Build System`.
- **Best Practices**:
  - Keep individual concepts focused (one file, one primary concern).
  - Include short, relevant code excerpts.
  - Infer and document relationships (e.g. "This module is called by [entrypoint](./entrypoint.md) and depends on [patient-event-graph](../modules/patient-event-graph.md).").
  - Use Mermaid diagrams in architecture/overview for visual relationships.
  - Timestamp generations and record source commit/SHA in log.md and frontmatter.

## Example Bundle Layout for a Repository
```
my-repo-okf/
├── index.md
├── overview.md
├── architecture.md
├── tech-stack.md
├── log.md
├── key-files/
│   ├── index.md
│   ├── readme.md
│   └── pyproject.md
├── modules/
│   ├── index.md
│   ├── core/
│   │   └── orchestrator.md
│   └── agents/
│       └── triage-agent.md
└── dependencies/
    ├── index.md
    └── langgraph.md
```

This format enables AI agents and humans to enrich, consume, and exchange structured knowledge about repositories in a standardized, git-friendly way.