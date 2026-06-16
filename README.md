# Grok Custom Skills

Custom skills for Grok (xAI) focused on healthcare, knowledge graphs, and clinical workflows.

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

### Other Skills

- **okf-code2prompt-workflow** — Codebase ingestion + Open Knowledge Format bundles
- **okf-repo-knowledge-generator** — Repository to structured OKF knowledge bundles

See individual `skills/*/SKILL.md` for full details and trigger phrases.

---

**Attribution:** The two RDF skills above were developed by adapting and extending patterns from the excellent [OpenLinkSoftware/ai-agent-skills](https://github.com/OpenLinkSoftware/ai-agent-skills) repository.