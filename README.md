# Grok Custom Skills

Custom skills for [Grok](https://x.ai) (xAI) — healthcare knowledge graphs, responsible AI documentation, office productivity, security review, critical analysis, publishing workflows, bibliography integrity, and production engineering.

## Installation

Copy skills into your Grok skills directory. Grok auto-reloads when files change on disk.

**All skills (recommended):**

```bash
rsync -av --exclude='.DS_Store' skills/ ~/.grok/skills/
```

**Single skill:**

```bash
rsync -av skills/<skill-name>/ ~/.grok/skills/<skill-name>/
```

**Project-scoped skills** (share with teammates via git):

```bash
mkdir -p .grok/skills
rsync -av skills/<skill-name>/ .grok/skills/<skill-name>/
```

Invoke skills via slash command (`/<skill-name>`), the skills menu (`/skills`), or let Grok auto-invoke based on the skill description.

---

## Skills Overview

| Category | Skills |
|----------|--------|
| Healthcare & KG | `rdf-kg-generator`, `rdf-infographic-skill`, `datacard-generator`, `okf-code2prompt-workflow`, `okf-repo-knowledge-generator` |
| Diagramming | `drawio-skill` |
| Office & documents | `docx`, `xlsx`, `pptx` |
| Publishing | `medium-article-generator` |
| Security | `python-owasp-reviewer` |
| Quality, Verification & Review | `check-work`, `code-review`, `scientific-strategic-review-board`, `bib-audit` |
| Grok platform | `create-skill`, `help`, `imagine` |
| Engineering lifecycle | 24 skills in `from-github-addyosmani-agent-skills/` |

See `skills/*/SKILL.md` for full trigger phrases and invocation details.

---

## Bibliography Integrity

### bib-audit

Flag hallucinated references, authors and bib items, and correct badly formatted ones — in your own draft (before submitting) or a paper you are reviewing. Works from a `.bib` file, a PDF, or a pasted reference list.

**Key features:**
- Resolves every entry against Crossref, arXiv, DataCite, Semantic Scholar, and OpenAlex
- Detects fabricated DOIs / arXiv IDs, invented authors, title mismatches, truncated author lists, year drift
- Recovers canonical publisher BibTeX for drop-in fixes (`--show-bibtex`)
- Ranks findings P1–P4 (integrity first, formatting last)
- Mechanical style checks (single-hyphen page ranges, DOI-as-URL, double-braced titles, `J.D.` initials, literal `and others`)
- Stdlib-only Python scripts; read-only; exits non-zero for CI / pre-submission gates
- Design bias: a false fabrication accusation is worse than a miss — ambiguous cases stay advisory `[CHECK]`

**Trigger phrases (examples):**
- "audit my bibliography" / "check citations" / "verify references"
- "find hallucinated refs" / "is this DOI real?"
- "fix badly formatted bib entries"
- "extract bibliography from this PDF and audit it"
- "gate my pre-submission bibliography"

**Quick start:**
```bash
# Preferred path — structured .bib
python3 skills/bib-audit/scripts/validate_refs.py refs.bib
python3 skills/bib-audit/scripts/validate_refs.py refs.bib --key somekey --show-bibtex

# Single-title identifier lookup
python3 skills/bib-audit/scripts/lookup_id.py "Decoupled Weight Decay Regularization" --author Loshchilov
```

**Example:** `examples/bib-audit/` — sample `.bib` with intentional issues + expected findings table.

**Source:** Adapted from [isaaccorley/skills bib-audit](https://github.com/isaaccorley/skills/tree/main/plugins/bib-audit) (MIT). Formatting rules distilled from John Owens (UC Davis) *Common Errors in Bibliographies* and Henning Schulzrinne (Columbia).

---

## Publishing

### medium-article-generator

Generate Medium-ready **MHTML** (default) or HTML articles from Markdown that contains LaTeX equations. Equations are automatically rendered as crisp SVG images so they display correctly on Medium (which has no native LaTeX support).

**Key features:**
- Online path (default): Pandoc `--webtex` → CodeCogs SVG with white background
- Offline fallback: local `latex` + `dvisvgm` → self-contained data-URI SVGs
- Always produces standalone HTML with explicit UTF-8 charset (avoids encoding problems with curly quotes / accented characters)
- Syntax highlighting for fenced code blocks + clean table styling
- Packages the result as a single self-contained `.mhtml` file by default

**Examples:**
- "Convert this Markdown article with LaTeX equations into a Medium-ready MHTML"
- "Render the math in my draft for Medium"
- "Generate Medium HTML from article.md using offline rendering"

**Quick start:**
```bash
python3 skills/medium-article-generator/scripts/generate_medium_html.py article.md
# → article.mhtml (self-contained)

python3 .../generate_medium_html.py article.md --offline   # local TeX rendering
python3 .../generate_medium_html.py article.md -o article.html  # plain HTML
```

**Based on:** The Markdown–Pandoc pipeline described by Sam Vaseghi in *The Quantastic Journal* ("How to Write LaTeX Equations in Medium Articles Automatically", May/June 2026), including the standalone + UTF-8 recommendation.

---

## Scientific & Strategic Review

### scientific-strategic-review-board

Performs independent, evidence-based scientific and strategic reviews of research proposals, papers, architectures, product concepts, GitHub repositories, and strategic initiatives. Functions as a multi-perspective Review Board that challenges assumptions, evaluates scientific rigor, methodological soundness, strategic alignment, novelty, risks, and provides objective, calibrated recommendations.

**Key features:**
- Structured 13-section board output (Executive Summary, Hidden Assumptions categorized across 13 dimensions, Contrarian Review, Failure Modes, Novelty Analysis, Literature Gaps, Competing Designs, Red Team, Steelman, Evidence Scoring, Risk Matrix, Recommended Improvements, Final Verdict + Confidence Level)
- Explicit separation of facts, assumptions, speculation, and unknowns
- Multi-perspective lens (scientific/methodological, strategic/competitive, operational, ethical/regulatory)
- Feedback-ready: ideal before publishing, funding decisions, architecture reviews, or challenging research/product thinking
- High intellectual honesty with calibrated confidence scoring

**Trigger phrases (examples):**
- "scientific review of this proposal"
- "strategic critique of this architecture"
- "Act as review board for this research idea"
- "Challenge my thinking on this FHIR validator with scientific and strategic lens"
- "Devil's advocate / independent board review before publishing"
- "Validate novelty and risks of this R&D initiative"

**Best used for:** Pre-publication peer review, investment/funding decisions in science & tech, architecture reviews, research proposal validation, and improving the robustness of complex ideas.

---

## Healthcare & Knowledge Graph

### rdf-kg-generator

Generate standards-compliant RDF Knowledge Graphs (Turtle default) from documents, clinical protocols, research articles, PDFs, or URLs.

**Key features:**
- Healthcare grounding (SNOMED CT, RxNorm, LOINC priority)
- Provenance and nanopublication patterns
- Generic + Healthcare/Clinical templates with self-audit checklists
- Script-assisted validation using `rdflib`
- Designed for GraphDB, patient timelines, and clinical decision support

**Examples:**
- "Generate a knowledge graph from this NCCN guideline"
- "Create RDF-Turtle for the 2026 Colon Cancer updates with PI3K pathway"
- "Build a comorbidity KG for colorectal cancer + diabetes"

**Example output:** `examples/rdf-kg-generator/nccn-colon-cancer-v2.2026/nccn_colon_cancer_2026_updates.ttl`

---

### rdf-infographic-skill

Turn RDF Knowledge Graphs into interactive single-file HTML infographics with embedded Knowledge Graph Explorer (Cytoscape.js), floating navigation, theme toggle, resolver links, and optional Markdown companion.

**Key features:**
- RDF is always the single source of truth
- Healthcare-optimized rendering (timelines, comorbidity clusters, biomarker pathways)
- Patient journey timeline view + class filters
- Self-contained (CDN-based, no external dependencies at runtime)

**Examples:**
- "Create an interactive HTML explorer from this Turtle file"
- "Generate a visual companion for the NCCN Colon KG with timeline emphasis"

**Example output:** `examples/rdf-infographic-skill/nccn-colon-cancer-v2.2026/nccn_colon_kg_explorer_v3.html`

---

### datacard-generator

Generate comprehensive Data Cards following the Google PAIR Data Cards Playbook from a dataset folder + metadata/context YAML.

**Key features:**
- Auto-analyzes folder contents (file stats, tabular schema inference, README extraction)
- Scaffolds all 15+ core Playbook themes with tables and `[TODO]` markers
- Supports rich context YAML for motivations, provenance, sensitivity, reflections
- Healthcare focus (RxNorm provenance, FHIR, nanopublications, HIPAA considerations)

**Examples:**
- "Create a Data Card for this RxNorm monthly mapping folder"
- "Generate transparency documentation for my patient triage context graph"

**Example output:** `examples/datacard-generator/BioRED_DataCard.md` (full Data Card for the NCBI BioRED biomedical relation extraction dataset)

**Source inspiration:** [Google PAIR Data Cards Playbook](https://github.com/PAIR-code/datacardsplaybook) and [sites.research.google/datacardsplaybook](https://sites.research.google/datacardsplaybook/) — operationalized into a practical, auto-scaffolding CLI skill tailored for healthcare AI and regulated data documentation workflows.

---

### drawio-skill

Generate professional editable draw.io diagrams from natural language — architecture diagrams, ERDs, UML class/sequence diagrams, flowcharts, ML/DL model architectures, network topologies, and clinical workflows.

**Key features:**
- Produces fully editable `.drawio` XML files (open in the free draw.io desktop app or https://app.diagrams.net)
- Supports swimlanes, precise orthogonal edge routing, containers/groups, branded shapes, and a professional semantic color palette
- Includes Python helper scripts: `DrawioDiagram` XML builder, structural validator, and grid/layered layout tools
- Strong healthcare and clinical focus with examples for patient triage systems, FHIR/GraphDB architectures, clinical trial site activation, RxNorm mapping workflows, agent orchestration, and comorbidity graphs
- Iterative refinement loop with targeted XML edits based on user feedback

**Examples:**
- "Draw an architecture diagram for the patient triage system with FHIR, GraphDB, and agent orchestrator layers in swimlanes"
- "Create an ERD for the pharmacy drug database including RxNorm mappings and nanopublications"
- "UML class diagram for the clinical trial site activation workflow entities"
- "Flowchart of the IRB approval process with decision points and swimlanes for sponsor vs site"

**Helper scripts & references:** `skills/drawio-skill/scripts/` and `skills/drawio-skill/references/`

**Source inspiration:** Adapted from [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) with customization for the Grok sandbox environment, healthcare domain needs, and integration with existing skills.

---

### okf-code2prompt-workflow

Integrated pipeline combining code2prompt (codebase ingestion + filtering + token management) with OKF concept generation. Produces rich Open Knowledge Format bundles from any repository.

**Examples:**
- "Use code2prompt with OKF for this repo"
- "Generate OKF using code2prompt"

---

### okf-repo-knowledge-generator

Generate Open Knowledge Format (OKF) bundles for any repository (GitHub URL or local path). Analyzes structure, README, source files, configs, and dependencies to produce hierarchical markdown concept documents.

**Examples:**
- "Generate OKF for this repo"
- "Create knowledge bundle for github.com/org/repo"

---

## Office & Documents

| Skill | Use when |
|-------|----------|
| `docx` | Creating, reading, or editing Word documents (.docx) — reports, memos, tracked changes, comments |
| `xlsx` | Spreadsheets are the primary input or output (.xlsx, .csv, .tsv) — formulas, formatting, cleaning |
| `pptx` | Slide decks, presentations, or any .pptx file — create, edit, extract, combine |

---

## Security & Quality

| Skill | Use when |
|-------|----------|
| `python-owasp-reviewer` | OWASP Top 10 SAST on Python (FastAPI, Flask, Django); also reviews agent workflows and SKILL.md files |
| `check-work` | Verify changes with a subagent — `/check-work`, `/verify`, `/self-verify` |
| `code-review` | Strict maintainability audit — abstraction quality, giant files, spaghetti conditions |
| `bib-audit` | Bibliography integrity — hallucinated refs, fabricated DOIs, metadata mismatches, style nits |

---

## Grok Platform

| Skill | Use when |
|-------|----------|
| `create-skill` | Scaffold a new Grok skill interactively — `/create-skill` |
| `help` | Grok setup, MCP servers, authentication, skills, slash commands |
| `imagine` | Image generation/editing workflow guidance in Grok Build |

---

## Engineering Lifecycle (addyosmani/agent-skills)

24 production-grade engineering skills vendored from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) in `skills/from-github-addyosmani-agent-skills/`.

| Phase | Skills |
|-------|--------|
| Meta | `using-agent-skills` |
| Define | `interview-me`, `idea-refine`, `spec-driven-development` |
| Plan | `planning-and-task-breakdown` |
| Build | `incremental-implementation`, `test-driven-development`, `context-engineering`, `source-driven-development`, `doubt-driven-development`, `frontend-ui-engineering`, `api-and-interface-design` |
| Verify | `browser-testing-with-devtools`, `debugging-and-error-recovery` |
| Review | `code-review-and-quality`, `code-simplification`, `security-and-hardening` |
| Ship | `shipping-and-launch`, `ci-cd-and-automation`, `observability-and-instrumentation`, `performance-optimization` |
| Maintain | `documentation-and-adrs`, `git-workflow-and-versioning`, `deprecation-and-migration` |

See `skills/from-github-addyosmani-agent-skills/README.md` for provenance and update instructions.

---

## Attribution

- **RDF skills:** Adapted and extended from [OpenLinkSoftware/ai-agent-skills](https://github.com/OpenLinkSoftware/ai-agent-skills) (`kg-generator`, `rdf-infographic-skill`)
- **Data Cards:** Based on the [Google PAIR Data Cards Playbook](https://sites.research.google/datacardsplaybook/)
- **Draw.io diagrams:** Adapted from [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)
- **Engineering lifecycle:** Vendored from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **Office skills (`docx`, `xlsx`, `pptx`):** Grok built-in document skills
- **Scientific & Strategic Review Board:** New custom skill for rigorous, board-style critique of research, architecture, and strategic proposals (created via skill-creator)
- **medium-article-generator:** Inspired by Sam Vaseghi’s Markdown–Pandoc pipeline in *The Quantastic Journal* (May/June 2026)
- **bib-audit:** Adapted from [isaaccorley/skills bib-audit](https://github.com/isaaccorley/skills/tree/main/plugins/bib-audit) (MIT); style rules from John Owens (UC Davis) and Henning Schulzrinne (Columbia)
