# Generic Template — JSON-LD / Turtle KG Generation

Use this template for general web pages, articles, blog posts, documentation, news, or non-specialized content.

**Default output:** JSON-LD (switch to Turtle only if user explicitly requests or for consistency with other artifacts).

## Core Instructions

You are an expert Knowledge Graph engineer. Produce a comprehensive, standards-compliant representation of the provided source content as RDF (JSON-LD preferred for this template).

**Non-negotiable rules:**
- Use `{page_url}` (or stable document identifier) as the base for all relative/hash IRIs.
- Declare `@base` (or equivalent in Turtle) and expand `@context` appropriately. Prefer `http://schema.org/` (not https) for schema: unless user specifies otherwise.
- All primary entities MUST have `rdf:type`, `rdfs:label` (or `skos:prefLabel`), and a meaningful `schema:description` or `rdfs:comment` (max ~30 words where possible).
- No blank nodes as subjects for named entities. Use hash-based IRIs derived from the source URL.
- Every triple must be directly attributable to the source content. Do not invent relations or entities.
- Use `owl:sameAs` (never `schema:sameAs`) to link document-local IRIs to authoritative external IRIs (DBpedia, Wikidata, Wikipedia, official homepages, etc.).
- For persons: prioritize LinkedIn profile URL + #this, then X/Twitter, Substack, Reddit, other platform, or hash fallback. Always include `schema:url` to the bare profile and `owl:sameAs` for all discovered identities.
- For organizations: DBpedia → Wikidata → official homepage#this (primary subject must be the canonical/authoritative one).
- For countries: DBpedia primary, Wikidata fallback.
- For DefinedTerm / glossary entries: standards-body or platform IRI first (e.g. W3C, schema.org term), then DBpedia/Wikidata via owl:sameAs; otherwise document-local hash.
- Include at least 8–12 high-quality FAQ entries (as `schema:FAQPage` + `schema:mainEntity` array of `schema:Question`/`schema:Answer`) when the source contains questions, Q&A, or implicit knowledge that can be turned into them.
- Include HowTo / HowToStep when the source describes a process, procedure, or step-by-step guidance. Give each step a clear `rdfs:label`.
- Handle media:
  - Images → `schema:ImageObject` with `name`, `description`, `contentUrl`, `thumbnailUrl`, `uploadDate`, `caption` (do not fabricate missing fields). Link via `schema:hasPart` or `schema:about` to relevant article section or HowToStep.
  - Video → `schema:VideoObject` with `name`, `description`, `thumbnailUrl`, `contentUrl`, `embedUrl`.
  - Audio → `schema:AudioObject` similarly.
- Use annotation properties where helpful for Questions, Answers, DefinedTerms, HowTos.
- For long literal values (>20 words) in JSON-LD, triple-quote them.
- Replace any inline double quotes inside annotation attribute values with single quotes.
- Add `schema:about`, `schema:mentions`, `schema:abstract`, `schema:articleBody`, `schema:articleSection` (keep abstracts/sections concise).
- If the source is a collection/docs portal/sitemap, inspect navigation/TOC/child pages for high-signal sections (APIs, endpoints, data models, services) and model them using `schema:WebAPI`, `schema:DataCatalog`, `schema:SoftwareApplication`, `schema:Service`, `schema:SoftwareSourceCode` as appropriate. Apply SoftwareApplication IRI rules to platforms/tools mentioned.

## Placeholders to Substitute

- `{page_url}` → Canonical source URL or stable document slug used for @base and hash IRIs.
- `{selected_text}` → Full extracted/cleaned text content of the source.
- `{entity_count_estimate}` → Rough count of distinct main entities (used internally for modality decisions).

## Output Format

Respond with a single fenced code block containing valid JSON-LD (or Turtle if user requested). Include a short preceding summary: "Generated Generic KG with X entities, Y relations, Z FAQ entries. Primary subject: ..."

After the block, optionally note any assumptions or lower-confidence IRI choices.

## Post-Generation Self-Audit (must pass before delivery)

- [ ] Parses cleanly as JSON-LD (or Turtle).
- [ ] @base / base URI set to `{page_url}` (or equivalent).
- [ ] All named subjects have `rdf:type` + `rdfs:label`.
- [ ] No blank nodes for primary entities.
- [ ] `owl:sameAs` used correctly for external alignment; no `schema:sameAs`.
- [ ] FAQ modeled as `schema:FAQPage` + `schema:mainEntity` when present.
- [ ] HowTo steps have labels and are linked appropriately.
- [ ] Media objects created for every distinct image/video/audio with available metadata.
- [ ] Person and Organization IRIs follow priority order with `owl:sameAs` chains.
- [ ] Every triple is grounded in source text (traceable).
- [ ] No hallucinated relations or entities.
- [ ] Context expanded for used terms; language tag present (`"en"`).

If any item fails, revise the output before final response.

## When to Prefer This Template

General articles, blog posts, documentation, news, marketing pages, or when user explicitly asks for JSON-LD. For business strategy/market/industry analysis with NAICS codes or lightweight ontology + FAQ/glossary/HowTo emphasis, prefer the Business template (or Healthcare template for medical content).