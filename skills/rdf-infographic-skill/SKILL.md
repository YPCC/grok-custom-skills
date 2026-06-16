---
name: rdf-infographic-skill
description: Generate interactive single-file HTML infographics with embedded Knowledge Graph Explorer, floating navigation, theme toggle, resolver-backed entity links, and optional matching Markdown companions from RDF Turtle or JSON-LD. RDF is always the source of truth. Use after rdf-kg-generator or on any RDF dataset to create visual exploration artifacts, clinical timeline views, comorbidity graphs, or stakeholder presentations. Supports healthcare-specific rendering for medical entities, patient events, and trial workflows.
---

# RDF Infographic Skill (HTML + Markdown Companion Generator)

Transform validated RDF Knowledge Graphs into sophisticated, self-contained interactive HTML infographics and matching Markdown companions. This skill completes the end-to-end workflow started by `rdf-kg-generator`: RDF → visual exploration artifact.

## When to Use This Skill (Harness Mode)

Activate **RDF Infographic Harness Mode** when the user requests:
- HTML infographic or KG Explorer from RDF / Turtle / JSON-LD / SPARQL results
- Interactive visualization of a knowledge graph (especially clinical, comorbidity, trial, or patient timeline graphs)
- "Create visual companion", "HTML explorer", "interactive infographic", or "regenerate the viz from this RDF"
- Paired HTML + Markdown + RDF artifact set from a previously generated KG

In Harness Mode, **RDF is the single source of truth**. All narrative (FAQ, HowTo, glossary, entity descriptions, relations) must be derived from the parsed RDF. Do not invent content.

## Core Harness Contract (must be satisfied unless user explicitly opts out)

See the full enforceable rules in `references/harness-contract.md`. Key principles:

- **RDF is the single source of truth** — derive every FAQ, HowTo step, glossary term, entity card, timeline event, and narrative section from parsed RDF resources and properties. Counts and content must match exactly.
- **Shared artifact stem** across HTML, Markdown, and RDF outputs.
- **Resolver-backed links** (default uriburner describe pattern, configurable) with correct `target="_blank"` behavior for external links.
- **Interactive KG Explorer** with class filters, search, drag/zoom, Core/Full toggle, and healthcare color/timeline enhancements.
- **Floating nav + theme system** (draggable, persistent light/dark).
- **POSH/JSON-LD pairing** and attribution footer.
- **Zero-failure gate** — all checklist items in the reference must pass before delivery.

Load `references/harness-contract.md` on every run and follow every applicable rule.

## Workflow (execute in order)

1. **Receive input** — Either a path/string containing RDF (Turtle preferred for readability, JSON-LD also supported) or a reference to a previously generated artifact from `rdf-kg-generator`.
2. **Parse & analyze RDF** — Use rdflib (or the provided `scripts/analyze_rdf_for_viz.py`) to load the graph and extract:
   - Main subject(s) / primary entity and high-degree nodes
   - Key classes (MedicalCondition, Drug, ClinicalTrial, PatientEvent, HowTo, FAQPage, DefinedTermSet, etc.)
   - Relations, labels, provenance, and SPARQL examples
   - Healthcare signal for specialized rendering and color coding
3. **Elicit parameters** (if not already clear):
   - Output formats: HTML only (default), HTML + Markdown, or both + updated RDF
   - Theme preference or resolver base URL
   - Focus areas (e.g., "emphasize patient timeline and comorbidities", "full KG Explorer", "executive summary view")
   - Healthcare mode (auto-detected if medical classes present)
4. **Plan the artifact** — Briefly describe planned sections (narrative summary, FAQ count, HowTo steps, glossary terms, KG Explorer node/edge counts, timeline view if applicable). Get confirmation on complex clinical graphs.
5. **Generate** — 
   - Load and follow the detailed rules in `references/harness-contract.md`.
   - Build interactive single-file HTML (modern glassmorphism or clean healthcare aesthetic with blue/purple/green accents matching your infographic-generator style, responsive, accessible).
   - Embed KG Explorer using a lightweight CDN-friendly library (vis-network or equivalent). Derive node/edge data and filters directly from the parsed RDF.
   - Derive **all** narrative text, FAQ, HowTo steps, glossary, timeline events, and SPARQL examples strictly from RDF entities and properties (exact counts and content match required).
   - Add floating draggable nav, theme toggle with persistence, resolver links on every entity, and proper open-tab behavior.
   - If Markdown requested: produce parallel `.md` with identical logical structure and resolver links (see harness contract for parity rules).
6. **Validate & deliver** — Run internal checks (parse, link integrity, no missing required sections, KG data consistency). Deliver files with shared stem. Provide a short usage note (how to open the HTML, interact with the explorer, switch themes).
7. **Optional further handoff** — If user wants a polished static executive infographic (McKinsey-style), pass a structured summary of the KG entities/relations/timeline to the `infographic-generator` skill.

## Integration with Existing Skills

- **rdf-kg-generator** (primary upstream): After generating a Turtle KG, say "now create the interactive HTML infographic and Markdown companion using rdf-infographic-skill". The two skills together give a complete RDF → validated Turtle → beautiful interactive explorer workflow.
- **infographic-generator** (downstream/static polish): Use this skill for interactive exploration; use infographic-generator when you need a clean, presentation-ready static visual summary or dashboard image for leadership review. They complement each other.
- **Your GraphDB / clinical pipelines**: Generated HTML can embed live resolver links back to your GraphDB or public LOD resolvers. Markdown companions are great for documentation or Git-based workflows.

## Technical Notes & Constraints

- Single-file HTML preferred for easy sharing and offline use (embed JS/CSS via CDN where possible for the explorer).
- For very large graphs (> few hundred nodes), offer "Core view" (main entities + key relations) vs "Full view" with progressive loading or clustering.
- Healthcare rendering: Prioritize clear visual distinction for conditions vs drugs vs events vs trials. Support horizontal/vertical timeline rendering when `:PatientEvent` or `schema:MedicalEvent` sequences are present.
- No external dependencies at runtime for the final HTML (self-contained after generation).
- SPARQL examples in the RDF are rendered as expandable accordions with correctly encoded live query links when an endpoint is known.

## Limitations & Responsible Use

- The interactive explorer is for exploration and communication, not a replacement for full GraphDB workbench or dedicated KG visualization tools on very large enterprise graphs.
- Always validate clinical accuracy of the underlying RDF before using the visual artifact in decision support or external sharing.
- Theme and interaction persistence uses localStorage; provide fallback instructions.

This skill, together with `rdf-kg-generator`, gives you a powerful, repeatable pipeline for turning clinical knowledge, trial protocols, comorbidity analyses, and pharmacy data into traceable, interactive, stakeholder-ready artifacts while keeping RDF as the canonical source of truth.
