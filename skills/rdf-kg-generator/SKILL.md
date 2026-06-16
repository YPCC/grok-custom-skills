---
name: rdf-kg-generator
description: Generate standards-compliant RDF Knowledge Graphs (Turtle default, JSON-LD supported) from file-scheme or https URLs, documents, clinical protocols, research articles or pasted text. Uses curated templates for general and healthcare/clinical content with schema.org, SNOMED, RxNorm, LOINC alignment, IRI rules, provenance options and validation. Trigger on requests to generate knowledge graph, RDF from URL or document, JSON-LD extraction, semantic structuring of medical/clinical content, build patient timeline KG or ontology population.
---

# RDF Knowledge Graph Generator

Generate high-quality, loadable RDF Knowledge Graphs (primarily Turtle for readability and GraphDB compatibility; JSON-LD available) from web pages, local files, clinical trial documents, research articles, or arbitrary text. Emphasizes correct IRI usage, medical entity grounding, minimal hallucinated relations, and syntactic/semantic validity.

## When to Use This Skill

- "Generate a knowledge graph from [URL or document]"
- "Create RDF-Turtle for this clinical protocol / research article / patient case"
- "Build JSON-LD representation of [medical content]"
- "Convert this URL to structured semantic data / RDF"
- "Generate KG for colorectal cancer triage guidelines with comorbidities"
- "Extract entities and relations as RDF from [PDF/text]"
- "Create nanopublication-style assertions or provenance-rich KG from [source]"

Use for both one-off generation and as part of larger pipelines (e.g. before loading to GraphDB, feeding patient event timelines, or powering CDSS reasoning).

## Core Principles

- **RDF is the source of truth.** Never invent relations or entities not grounded in source. Prefer explicit schema.org + domain vocabulary over free-form.
- **IRI quality first.** Follow priority rules for every entity type. Use owl:sameAs to link local document IRIs to authoritative ones. Never use schema:sameAs.
- **Healthcare grounding.** For conditions use SNOMED CT IRIs when confident; for drugs RxNorm/RxCUI; labs LOINC; procedures CPT/ICD. Fall back to DBpedia/Wikidata or schema:Medical* types + local hash IRIs. Always include rdfs:label and schema:description or skos:definition.
- **Provenance & nanopublications.** When user requests or source supports, include prov:wasDerivedFrom, np: (nanopublication) patterns, or custom assertion metadata with release/version info (aligns with your RxNorm mapping and monthly update workflows).
- **Validation mandatory.** Output must parse cleanly with rdflib (or equivalent). No unbalanced syntax, no dangling prefixes, consistent base URI usage.
- **Modality choice for efficiency.** LLM-Direct for small/simple sources (<15-20 entities). Script-Assisted (JSON entity extraction → rdflib Graph construction) for complex documents, many entities, tables, or when strict validation needed.
- **Companion artifacts optional.** After RDF, if user also wants visual summary, infographic, timeline viz or HTML explorer, hand off to infographic-generator skill (or create companion using it). RDF remains canonical.

## IRI Alignment Rules (apply at generation time)

**Medical/Clinical Concepts (Condition, Drug, Observation, Procedure):**
1. SNOMED CT (http://snomed.info/id/[code]) or BioPortal-hosted if confident match exists.
2. RxNorm for medications (https://rxnav.nlm.nih.gov/ or appropriate RxCUI IRI).
3. LOINC for labs/measurements.
4. ICD-10/ICD-O or UMLS CUI as secondary.
5. DBpedia/Wikidata medical entity if no domain code confident.
6. Document-local hash IRI (e.g. {page_url}#condition-diabetes-type2) as primary subject, link via owl:sameAs to authoritative.

**SoftwareApplication / Tool / Platform (e.g. GraphDB, Epic, LangGraph, Virtuoso):**
1. DBpedia or Wikidata IRI if confident.
2. Official homepage URL + #this.
3. Add owl:sameAs for alternatives.

**Country / Location:**
1. DBpedia country IRI primary.
2. Wikidata fallback.
3. Local hash only if unknown.

**DefinedTerm / Glossary / Ontology Term:**
1. Standards-body or canonical IRI (W3C, schema.org, SNOMED, etc.) as primary when exists.
2. DBpedia/Wikidata via owl:sameAs.
3. Document-local hash IRI (most common); link authoritative with owl:sameAs.

Always declare used prefixes (schema, snomed, rxnorm, prov, np, etc.). Use @base or base URI derived from source URL or stable slug.

## Workflow (follow every time)

1. **Identify source** — extract URL (file: or http/https) or use pasted document text. If URL, fetch content using available tools (browse_page preferred for structured extraction, or note JS-heavy pages may need additional handling).
2. **Elicit parameters** (unless user specified):
   - Output format: (1) RDF-Turtle only (default, recommended for healthcare/GraphDB), (2) JSON-LD only, (3) Both.
   - Generation modality: (1) LLM-Direct, (2) Script-Assisted (recommended for >20 entities or complex tables), (3) Agent's choice based on content analysis.
   - Domain template: Generic, Business/Market Analysis, or Healthcare/Clinical (use for medical, oncology, comorbidity, trial protocols, pharmacy data).
3. **Analyze & plan** — for complex requests, output a short table of planned top-level entities, key relations, chosen IRIs for main subjects, and any compliance gates. Get user confirmation before full generation on high-stakes clinical content.
4. **Select & apply template** — Choose Generic, Business/Market, or Healthcare/Clinical based on content. Load and strictly follow the detailed prompt, modeling patterns, IRI rules, and self-audit checklist from the corresponding file in `references/` (e.g. `references/healthcare-template.md` for clinical/medical sources, `references/generic-template.md` otherwise). Populate all placeholders and ground entities exactly as specified.
5. **Validate output** — parse with Python + rdflib (install if needed via internal pip). Fix any syntax errors, missing labels, or inconsistent IRIs. Run basic SHACL-like checks mentally or via simple script (no blank nodes for named entities, all subjects have rdf:type where appropriate).
6. **Deliver** — present RDF in fenced code block with language tag (turtle or json). Suggest filename e.g. {slug}-kg-1.ttl. If both formats requested, provide toggle or separate blocks.
7. **Optional handoff** — 
   - For interactive HTML infographic + embedded KG Explorer + matching Markdown companion from the RDF: invoke the companion `rdf-infographic-skill`. Pass the validated Turtle/JSON-LD plus focus (e.g. "emphasize patient timeline, comorbidities, and full KG Explorer").
   - For polished static McKinsey-style executive infographic or dashboard visual: invoke `infographic-generator` with a structured summary of key entities/relations/timeline.
   - Use both sequentially when you want an interactive explorer first and a clean static summary for leadership review.

## Template Guidance

Detailed prompt templates, modeling patterns, IRI priority rules, placeholder substitution, media/FAQ/HowTo handling, and mandatory post-generation self-audit checklists live in the `references/` directory:

- `references/generic-template.md` — For general articles, docs, web content (JSON-LD default). Covers schema.org best practices, person/org/country/DefinedTerm alignment, FAQPage, HowTo, media objects.
- `references/healthcare-template.md` — **Primary template for your work**. Turtle default. Strong emphasis on SNOMED CT / RxNorm / LOINC grounding, comorbidities, patient event timelines, clinical trial modeling (eligibility, endpoints, sponsors, activation timelines), provenance/nanopub-style assertions, and GraphDB-friendly output. Includes clinical self-audit gates.

**Selection rule:** Healthcare/Clinical for any medical, oncology, comorbidity, trial protocol, pharmacy, or clinical content. Generic otherwise. Business/Market only for pure strategy/industry analysis. When in doubt, default to Generic + confirm with user, or load both references and blend.

Load the chosen reference file(s) and follow every rule in the prompt and checklist before producing output.

## Modality Details & Agent's Choice Heuristic

- **LLM-Direct:** Write full Turtle/JSON-LD end-to-end. Best for short articles, <15-20 clear entities, quick iterations, or when user wants fast prose-style RDF.
- **Script-Assisted:** First output structured JSON entity/relation map (with chosen IRIs and types). Then use Python + rdflib to construct Graph deterministically, serialize, and validate. LLM then only generates any companion HTML/MD or summary from the validated RDF. Best for long documents, tables, many entities, comments, SPARQL examples, or strict compliance needs. Reduces hallucinated triples.
- **Agent's Choice (default):** Analyze source length, entity density, presence of tables/lists, medical coding density, SPARQL/query examples. If complex or >20 entities or healthcare protocol → Script-Assisted. Else LLM-Direct. Always state chosen mode and rationale briefly.

For Script-Assisted mode, use the provided `scripts/validate_rdf.py` (install rdflib via internal pip if missing: `pip install rdflib`). It parses the generated RDF and reports triple count + basic structure.

## Post-Generation Validation Checklist (run mentally or via script)

Use the comprehensive self-audit checklist inside the loaded `references/*.md` template (Generic or Healthcare). It covers syntax (rdflib parse), entity typing/labels, IRI grounding (medical codes + owl:sameAs), provenance, no hallucinated triples, media/FAQ/HowTo modeling, prefix consistency, Turtle cleanliness, and clinical-specific gates (comorbidities, RxNorm grounding, timeline traceability, "clinician-reviewable" standard).

High-level summary of gates that must pass:
- Parses cleanly + all primary subjects have rdf:type + rdfs:label.
- Correct IRI priority + owl:sameAs (no schema:sameAs, no file: IRIs for external entities).
- Medical content: SNOMED/RxNorm/LOINC grounding where applicable; comorbidities and timelines modeled explicitly.
- Provenance on derived assertions; no invented clinical facts.
- Every triple traceable to source; suitable for GraphDB import and your SHACL/nanopub pipelines.

Run `scripts/validate_rdf.py` in Script-Assisted mode for automated syntax + triple count. For clinical KGs, always apply the extra "Would a domain expert accept this as accurate and useful?" gate before delivery.

## Integration with Existing Skills & Tools

- **infographic-generator:** After producing RDF KG (especially healthcare), call this skill to create McKinsey-style visual summary, entity-relation diagram, or patient timeline infographic. Pass key entities/relations or a textual description derived from the KG.
- **okf-repo-knowledge-generator or okf-code2prompt-workflow:** Use when source is a GitHub repo or codebase to first extract knowledge then feed to rdf-kg-generator for RDF version.
- **Your GraphDB / FHIR RDF pipelines:** Generated Turtle is designed to be directly importable. For nanopublication-style monthly updates (e.g. RxNorm mapping), follow your existing TriG + prov + np: patterns.
- **Multi-agent orchestration (LangGraph):** This skill can be a specialist node in larger agent graphs for clinical trial site activation, patient triage CDSS, or document-to-KG pipelines.

## Output & Saving

- Default filename pattern: `{source-slug}-kg-{version}.ttl` (or .jsonld)
- Save to working directory or artifacts/ as appropriate.
- When both formats requested, provide Turtle as primary + JSON-LD as alternative (or use rdflib to convert).
- Always include a short human-readable summary of what the KG contains (top classes, key relations, entity counts) before or after the code block.

## Limitations & Responsible Use

- This skill produces RDF representations grounded in source; it does not replace expert curation, SHACL validation against your full ontologies, or live clinical validation.
- For high-stakes clinical decision support or regulatory submissions, always have human review + full provenance audit.
- LLM may still hallucinate subtle relations on very long or ambiguous sources — prefer Script-Assisted + plan approval for such cases.
- No direct browser automation or authenticated fetch beyond available tools; for protected content, user must provide text or handle auth first.

This skill encodes the procedural knowledge for consistent, high-fidelity RDF KG generation tailored to your healthcare AI and clinical data workflows.
