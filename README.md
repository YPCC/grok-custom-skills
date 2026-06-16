# Grok Custom Skills Repository

This repository contains custom skills developed for Grok (by xAI) to extend its capabilities, particularly in healthcare AI, knowledge graph generation, multi-agent systems, and clinical workflows.

## Skills Included

### RDF & Knowledge Graph Skills

These skills were developed inspired by the excellent work in the [OpenLinkSoftware/ai-agent-skills](https://github.com/OpenLinkSoftware/ai-agent-skills) repository (specifically `kg-generator` and `rdf-infographic-skill`).

- **rdf-kg-generator**  
  Generates high-quality, standards-compliant RDF Knowledge Graphs (Turtle by default) from documents, clinical protocols, research articles, or URLs. Strong focus on healthcare grounding (SNOMED, RxNorm, LOINC), provenance, and PI3K pathway / biomarker workflows.

- **rdf-infographic-skill**  
  Companion skill that turns RDF KGs into interactive single-file HTML infographics with embedded Knowledge Graph Explorer, floating navigation, theme toggle, and Markdown companions. Excellent for clinical decision support visualizations and leadership reviews.

### Other Skills

- **okf-code2prompt-workflow**  
  Advanced pipeline combining `code2prompt` for high-quality codebase ingestion with Open Knowledge Format (OKF) bundle generation.

- **okf-repo-knowledge-generator**  
  Generates structured OKF knowledge bundles from repositories.

## Examples

See the `examples/` directory for real-world demonstrations:

- `examples/nccn-colon-cancer-v2.2026/` — End-to-end example using the 2026 NCCN Colon Cancer Guidelines (PI3K-aspirin recommendation, biomarker pathways, dMMR/MSI-H updates).

## Usage

See individual `skills/*/SKILL.md` files for detailed instructions and trigger phrases.

## Inspiration & Credits

The RDF-related skills (`rdf-kg-generator` and `rdf-infographic-skill`) draw significant inspiration and architectural patterns from:

- [OpenLinkSoftware/ai-agent-skills](https://github.com/OpenLinkSoftware/ai-agent-skills) — particularly the `kg-generator` and `rdf-infographic-skill` implementations.

---

Built with ❤️ for healthcare AI, clinical knowledge graphs, and responsible AI tooling.