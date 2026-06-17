# Grok Custom Skills

Custom skills for Grok (xAI) focused on healthcare, knowledge graphs, clinical workflows, and responsible AI documentation.

## Skills

### rdf-kg-generator
**Generate standards-compliant RDF Knowledge Graphs** (Turtle default) from documents, clinical protocols, research articles, PDFs, or URLs.

**Key features (adapted from OpenLinkSoftware/ai-agent-skills):**
- Strong healthcare grounding (SNOMED CT, RxNorm, LOINC priority)
- Provenance & nanopublication patterns
- Two templates: Generic + Healthcare/Clinical (with self-audit checklists)
- Script-assisted validation mode using `rdflib`
- Designed for GraphDB, patient timelines, and clinical decision support

**Usage examples:**
- "Generate a knowledge graph from this NCCN guideline"
- "Create RDF-Turtle for the 2026 Colon Cancer updates with PI3K pathway"
- "Build a comorbidity KG for colorectal cancer + diabetes"

**Example output:** `examples/rdf-kg-generator/nccn-colon-cancer-v2.2026/nccn_colon_cancer_2026_updates.ttl`

**Source inspiration:** [OpenLinkSoftware/ai-agent-skills/kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator) — we adopted the core architecture and extended it with healthcare-specific IRI rules, PI3K/RxNorm focus, and tighter integration with our clinical pipelines.

---

### rdf-infographic-skill
**Turn RDF Knowledge Graphs into interactive single-file HTML infographics** with embedded Knowledge Graph Explorer (Cytoscape.js), floating navigation, theme toggle, resolver links, and optional Markdown companion.

**Key features (adapted from OpenLinkSoftware/ai-agent-skills):**
- RDF is always the single source of truth
- Healthcare-optimized rendering (timelines, comorbidity clusters, biomarker pathways)
- Patient journey timeline view + class filters
- One-click prompt generation for static McKinsey-style infographics
- Self-contained (CDN-based, no external dependencies at runtime)

**Usage examples:**
- "Create an interactive HTML explorer from this Turtle file"
- "Generate a visual companion for the NCCN Colon KG with timeline emphasis"
- "Build a stakeholder-ready infographic from the RDF"

**Example output:** `examples/rdf-infographic-skill/nccn-colon-cancer-v2.2026/nccn_colon_kg_explorer_v3.html`

**Source inspiration:** [OpenLinkSoftware/ai-agent-skills/rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) — we enhanced it with Cytoscape.js, stronger timeline/patient-journey emphasis, and direct handoff to our `infographic-generator` skill.

---

### datacard-generator
**Generate comprehensive Data Cards** following the Google PAIR Data Cards Playbook specification from a dataset folder + associated metadata/context YAML.

**Key features:**
- Auto-analyzes folder contents (file stats, tabular schema inference via pandas, README extraction)
- Scaffolds all 15+ core Playbook themes with tables, guidance prompts, and `[TODO]` markers
- Supports rich context YAML for motivations, provenance, sensitivity, reflections, etc.
- Produces clean, versionable Markdown (with YAML frontmatter) ready for PDF/DOCX conversion or leadership review
- Strong healthcare focus (RxNorm provenance, FHIR, nanopublications, HIPAA considerations, comorbidity graphs)
- Includes detailed specification reference and healthcare example (BioRED)

**Usage examples:**
- "Create a Data Card for this RxNorm monthly mapping folder"
- "Generate transparency documentation for my patient triage context graph using the Google spec"
- "Document this clinical trial metadata dataset for leadership review"

**Example output:** `examples/datacard-generator/BioRED_DataCard.md` (full Data Card for the NCBI BioRED biomedical relation extraction dataset)

**Source inspiration:** Google PAIR Data Cards Playbook (https://github.com/PAIR-code/datacardsplaybook and https://sites.research.google/datacardsplaybook/) — we operationalized the archived template into a practical, auto-scaffolding CLI skill tailored for healthcare AI and regulated data documentation workflows.

---

### Other Skills

- **okf-code2prompt-workflow** — Codebase ingestion + Open Knowledge Format bundles
- **okf-repo-knowledge-generator** — Repository to structured OKF knowledge bundles

See individual `skills/*/SKILL.md` for full details, trigger phrases, and invocation instructions.

---

**Attribution:** The RDF skills were developed by adapting and extending patterns from [OpenLinkSoftware/ai-agent-skills](https://github.com/OpenLinkSoftware/ai-agent-skills). The `datacard-generator` skill brings the Google PAIR Data Cards Playbook into the same ecosystem for responsible AI documentation.