# RDF Infographic Harness Contract — Detailed Rules

This file contains the precise, enforceable rules for HTML and Markdown generation when `rdf-infographic-skill` is operating in Harness Mode. Load and follow these rules on every generation unless the user has explicitly waived a specific item.

## 1. RDF Source of Truth Principle

- Parse the complete input RDF graph before writing any HTML or Markdown.
- Every narrative element in the output (section headings, entity cards, FAQ Q&A pairs, HowTo steps, glossary terms, relationship descriptions, timeline events) MUST be backed by a corresponding RDF resource and its properties.
- If the RDF contains N instances of `schema:HowToStep` linked to a `schema:HowTo`, the HTML HowTo section MUST render exactly N steps with matching `schema:name`, `schema:text`, and `schema:position`.
- Do not author "pretty" narrative text that cannot be traced to an RDF literal or structured value.

## 2. Artifact Naming & Pairing

- All three artifacts (when generated) share the exact same stem: `{descriptive-slug}-{version}`.
  - Example: `colorectal-cancer-comorbidity-kg-1.html`
  - Example: `colorectal-cancer-comorbidity-kg-1.md`
  - Example: `colorectal-cancer-comorbidity-kg-1.ttl` (or the original RDF name)
- HTML must declare the companions via:
  ```html
  <link rel="alternate" type="text/markdown" href="...-1.md">
  <link rel="alternate" type="text/turtle" href="...-1.ttl">
  ```
- Embedded JSON-LD in the HTML `<head>` describes the artifact set and points to the RDF and MD.

## 3. Resolver-Backed Entity Links

- Default resolver: `https://linkeddata.uriburner.com/describe/?url={urlencoded_IRI}`
- Make resolver base configurable via parameter or frontmatter in the RDF if present.
- Every visible entity name, IRI, or label in HTML text, KG nodes, MD links, and attribution must be hyperlinked through the resolver (unless it is a same-page `#fragment`).
- Same-page navigation (TOC, section jumps, KG filters) stays same-tab.
- All external links (resolvers, DBpedia, SNOMED browser, RxNav, source URLs, companion files) use `target="_blank" rel="noopener noreferrer"`.

## 4. Interactive KG Explorer Requirements

- Embed a self-contained interactive graph component (vis-network via CDN or equivalent single-file-friendly library is acceptable).
- Data for the explorer must be derived directly from the parsed RDF (nodes = subjects/objects with labels and types; edges = predicates).
- Required controls (collapsible tray by default):
  - Search / filter by label or literal value
  - Class filters (checkboxes or multi-select for schema:MedicalCondition, schema:Drug, :PatientEvent, schema:ClinicalTrial, schema:HowTo, etc.)
  - Core / Full density toggle (Core = primary subject + direct neighbors + important relations)
  - Physics / layout controls (force-directed, hierarchical if timeline-like)
  - Node count + edge count badges
  - Clear / reset state button
- Interaction:
  - Drag nodes, zoom, pan
  - Click node → highlight neighbors + show resolver link or side panel with key properties
  - Double-click node or edge → open resolver in new tab
  - Hover shows truncated label + type
- Healthcare enhancements (when medical classes detected):
  - Color coding: conditions (blue/purple tones), drugs (green), events/timeline (orange/amber), trials (teal)
  - Special timeline lane or grouped view option when `PatientEvent` or `schema:MedicalEvent` sequences exist
  - Comorbidity clusters highlighted

## 5. Floating Navigation & Theme System

- Floating, draggable, resizable, collapsible navigation panel (default state: compact header bar with logo + controls).
- Contents: Table of contents (derived from RDF sections), theme toggle, KG Explorer quick actions, download buttons for companions, resolver preference.
- Theme:
  - Light / Dark toggle with system `prefers-color-scheme` respect
  - Persist choice in localStorage with fallback
  - CSS variables for easy theming (healthcare palette: primary blue #0A66C2, accent purple #6B46C1, success green #059669)
- Accessibility: proper ARIA labels, keyboard navigation for key controls, sufficient color contrast.

## 6. Narrative Sections Derived from RDF

When the corresponding RDF structures exist, the HTML and MD **must** include:

- **Header / Hero**: Primary subject label + description + type badges (with resolver links)
- **Key Entities / Cards**: Grid or list of important `schema:MedicalCondition`, `schema:Drug`, `schema:ClinicalTrial`, organizations, people (with proper IRI priority already applied in the RDF)
- **FAQ Section**: If `schema:FAQPage` + `schema:mainEntity` Question/Answer pairs exist → render as accessible accordion or cards. Each Q/A must reference its RDF subject.
- **HowTo / Procedure Section**: If `schema:HowTo` exists → render steps in order using `schema:position`, `schema:name`, `schema:text`. Each step must have an absolute IRI (use a named prefix anchored to source URL, e.g. `post:`).
- **Glossary / Defined Terms**: If `schema:DefinedTermSet` + `schema:hasDefinedTerm` exists → render as definition list or cards. Each term links back to its `schema:inDefinedTermSet` and carries `owl:sameAs` to DBpedia/Wikidata/SNOMED when present in RDF.
- **Timeline / Event Flow** (healthcare priority): When `PatientEvent` or `schema:MedicalEvent` resources with dates exist → render as horizontal/vertical timeline with provenance indicators.
- **SPARQL / Query Examples**: If `schema:SoftwareSourceCode` with `schema:programmingLanguage "SPARQL"` exists → render as expandable accordions with fenced `sparql` blocks + live query link (URL-encoded against known endpoint) + resolver link to the query resource.
- **KG Explorer**: Always present (unless user explicitly requests "narrative only").
- **Attribution Footer**: Source RDF location or original URL, generation timestamp + skills used, resolver pattern in use, links to generation environment entities (with correct IRI denotation), companion file links.

## 7. Markdown Companion Parity

The generated `.md` must:
- Use the same logical structure and heading hierarchy as the HTML narrative.
- Preserve all resolver-backed links (use markdown link syntax with the full resolver URL).
- Render FAQ as blockquote or definition style, HowTo as numbered list with sub-details, glossary as definition list.
- Include SPARQL examples as fenced ```sparql blocks with the same live links.
- Contain a "Companion Files" or "Related Artifacts" section at the top or bottom pointing to the HTML and original RDF.
- Be suitable for GitHub/GitLab rendering and easy copy into documentation or reports.

## 8. Zero-Failure Delivery Checklist (run before output)

- [ ] RDF parses successfully (rdflib or equivalent)
- [ ] All required narrative sections that exist in RDF are present in HTML/MD with correct counts
- [ ] Every visible entity link uses the configured resolver (or explicit same-page fragment)
- [ ] KG Explorer data is consistent with RDF (no orphan nodes, correct edge counts)
- [ ] HTML is valid single-file (no broken CDN links for critical JS/CSS)
- [ ] Theme toggle and nav persistence work in a fresh browser profile
- [ ] Markdown renders cleanly in standard viewers and preserves links
- [ ] Shared stem naming is consistent across all delivered files
- [ ] For healthcare graphs: medical entities have appropriate visual distinction and grounding badges
- [ ] Attribution footer is complete and contains correct hyperlinks

Only deliver after every item on this checklist passes. If repairing an existing artifact, retrofit missing contract items rather than creating a disconnected patch.

## 9. Configuration & Extensibility

- Resolver base URL can be passed as a parameter or read from RDF metadata (`:preferredResolver` or similar).
- Healthcare color palette and timeline rendering can be extended via additional CSS variables or RDF-driven configuration.
- For extremely large graphs, the skill may offer a "summary + core explorer" mode + link to full GraphDB visualization.

Follow these rules strictly. They ensure consistent, high-quality, RDF-grounded artifacts that integrate cleanly with `rdf-kg-generator` and your broader clinical knowledge graph ecosystem.