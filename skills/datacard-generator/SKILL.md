---
name: datacard-generator
description: Generate comprehensive Data Cards following Google PAIR Data Cards Playbook specification from a dataset folder plus associated metadata or context YAML. Auto-analyzes files, infers schemas and stats for tabular data, scaffolds all core themes with tables and guidance, produces polished Markdown (convertible to DOCX/PDF). Use for responsible AI documentation of research, healthcare, ML or clinical datasets ahead of reviews, publications or sharing.
---

# Datacard Generator

## Overview

This skill produces transparency artifacts called Data Cards for datasets, strictly aligned with the structure, themes and people-centered principles defined in Google's Data Cards Playbook (PAIR). It reduces manual effort by auto-populating technical metadata from the folder contents while providing clear scaffolding and prompts for the narrative, motivational, risk and governance sections that require human judgment.

## When to Use

Trigger on requests such as: create data card, generate datacard for this folder, document this dataset following Google spec, produce transparency report for my [pharmacy data / renal ontology / patient triage graph / clinical trial metadata], prepare Data Card for leadership or publication.

Ideal for your workflows involving RxNorm mappings, FHIR patient event graphs, comorbidity graphs, clinical trial site data, or any ML-ready healthcare dataset where provenance, sensitivity, intended use and limitations must be explicitly documented.

## How the Generator Works

The core is a Python CLI in `scripts/generate_datacard.py`. It:

1. Recursively scans the provided `--data-folder` for files, computes aggregate stats (total size, file counts by extension, top-level structure).
2. Special-cases common data files:
   - Tabular (CSV, TSV, Parquet, Excel): uses pandas to report row count, column count, dtypes, missingness summary, sample head (first 3-5 rows preview), basic descriptive stats for numeric columns.
   - JSON/JSONL: counts records, infers top-level schema or samples keys.
   - Text/README: extracts relevant paragraphs for motivations, provenance, description.
   - Looks for standard files: README*, LICENSE*, CITATION*, metadata.json, data_dictionary.*, requirements.txt, etc.
3. Merges any `--context-file` (YAML or JSON) you provide. Recommended keys mirror section names (e.g. `motivations`, `owners`, `funding_sources`, `sensitive_attributes`, `limitations`, `access_procedures`, `version_maintenance`).
4. Renders a complete, well-structured Markdown document using the Jinja2 template in `assets/`. All 15+ Playbook themes are present as top-level sections with:
   - Auto-filled facts where detectable.
   - Tables for snapshots, distributions, metrics.
   - Clear `[TODO: ...]` or guided prompts for sections needing domain expertise or reasoning.
   - Professional formatting (YAML frontmatter, consistent headings, blockquotes for guidance, links to Playbook resources).
5. Optional `--format` support for basic HTML preview or direct DOCX via integrated tooling (falls back to Markdown + instructions for pdf/docx skill).

After generation you review, fill gaps (often by feeding the draft + your knowledge back to an LLM or editing directly), and optionally convert to final PDF/DOCX for leadership packets.

## Invocation Examples

```bash
# Basic scaffold from folder only (good starting point)
python scripts/generate_datacard.py \
  --data-folder /path/to/my_rxnorm_mapping_v2 \
  --output artifacts/RxNorm_Monthly_Update_DataCard.md \
  --title "RxNorm Ingredient Mapping & Provenance v2026-06"

# With rich context YAML (recommended for narrative quality)
python scripts/generate_datacard.py \
  --data-folder ./data/patient_triage_colorectal \
  --context-file ./context/patient_triage_context.yaml \
  --output ./deliverables/Colorectal_Triage_ContextGraph_DataCard.md \
  --format markdown
```

See `references/example_context.yaml` and `references/example_output.md` for templates and a filled healthcare example.

## Output Structure (15 Core Themes + Supporting)

The generated card follows the Playbook's recommended organization (curated from extensive co-creation across Google teams). Main sections include:

**Header & Summary**
- Dataset title, short summary (<=200 words), link to data, authors / maintainers, publication date or version.

**Authorship**
- Publishers, Dataset Owners / Custodians, Funding Sources, Contact.

**Dataset Overview**
- High-level description, modalities, size, instance counts.
- Sensitivity of Data (PII, PHI, demographics, etc.) + handling/risk mitigation.
- Dataset Version and Maintenance plan (update cadence, deprecation policy, changelog link).

**Example of Data Points**
- Concrete samples or previews (tables for tabular, descriptions or thumbnails for other modalities).
- Typical vs. edge-case / atypical examples to aid interpretation without downloading full data.

**Motivations & Intentions**
- Why the dataset was created / curated.
- Primary intended uses and user personas.
- Known or anticipated downstream applications & benchmarks.

**Access, Retention, & Wipeout**
- Access procedures, licenses, terms of use, API / download links.
- Retention periods, deletion / wipeout policies and implementation.

**Provenance**
- Upstream sources and collection methods (API, scraping, manual curation, sensor, EHR export, etc.).
- Collection criteria / inclusion-exclusion logic.
- Relationship between this dataset and raw source(s); any transformations at ingest.

**Human and Other Sensitive Attributes**
- Presence and handling of sensitive fields (race, gender, age, geography, health status, etc.).
- Demographic distributions if relevant and disclosable.
- Privacy, consent, de-identification, re-identification risk notes (especially important for healthcare).

**Extended Use**
- Potential beneficial uses beyond primary intent.
- Known or foreseeable misuse risks + recommended safeguards / monitoring.
- Fairness, bias, or performance considerations across subgroups.

**Transformations**
- Cleaning, normalization, feature engineering, augmentation steps applied.
- Tools, code versions, deterministic vs. stochastic processes.
- Any lossy steps or assumptions made.

**Annotations & Labeling**
- If labels or annotations exist: who labeled (experts, crowd, model-assisted), guidelines used, inter-annotator agreement, quality assurance process.
- For derived labels (e.g. from RxNorm mapping rules): rule sources, validation against gold standards.

**Validation Types**
- Internal validation (schema checks, unit tests, SHACL shapes, Great Expectations, etc.).
- External or expert validation performed.
- Metrics and acceptance criteria used.

**Sampling Methods**
- How instances/records were selected (random, stratified, time-based, convenience, active learning, etc.).
- Any weighting, filtering or subsampling applied and rationale.

**Known Applications & Benchmarks**
- Published models, papers, or systems that have used this dataset.
- Performance numbers, evaluation protocols, leaderboards if applicable.
- Links to model cards or related transparency artifacts.

**Terms of Art / Glossary**
- Domain-specific terminology, abbreviations, ontology codes (SNOMED, LOINC, RxCUI, ICD, ATC, etc.) with definitions or links.
- Especially valuable for healthcare / clinical datasets.

**Reflections on Data**
- Known limitations, gaps, biases, or quality issues.
- Lessons learned during creation / maintenance.
- Future plans, roadmap, or deprecation timeline.
- Any open questions or areas where community feedback is sought.

Additional supporting elements: changelog / version history table, citation instructions, related artifacts (data dictionaries, codebooks, ontology files), acknowledgments, and a "How to Cite This Data Card" block.

## Healthcare / Regulated Data Guidance (Your Context)

When the folder contains clinical, pharmacy, patient-level or trial data:
- Explicitly address HIPAA / GDPR / IRB considerations in Sensitivity and Access sections.
- Reference FHIR resources, RxNorm/RxCUI provenance, nanopublication assertions, SHACL validation where applicable (as you do in your pharmacy DB and KG work).
- Note any linkage to external terminologies (BioPortal, SNOMED CT, etc.) and versioning of those.
- For derived datasets (e.g. monthly RxNorm updates, comorbidity groupings): document the derivation logic, source release dates (RxNorm monthly), and how changes are tracked (nanopublications, prov:wasDerivedFrom).

## Limitations of Auto-Generation & Human Responsibility

- Technical stats and file-derived facts are reliable.
- Narrative sections (motivations, reflections, risk analysis, intended use nuances) are scaffolded with prompts or partial text from your context YAML. These almost always require your expertise or targeted LLM reasoning to complete accurately and responsibly.
- Never fabricate numbers, sources, or claims. When in doubt use "Not documented", "Unknown at time of creation", or "See linked README / code".
- The original Data Cards Playbook repository is archived (read-only since Aug 2025). This skill preserves the core enduring structure for ongoing use in your organization.

## Next Steps After Generation

1. Open the .md in your editor or previewer.
2. Search for `[TODO]` and `[FILL` markers and address them.
3. Validate factual claims against source materials.
4. Run the card by a colleague or stakeholder for the "Inspect" and "Audit" phases of the Playbook.
5. Convert to DOCX/PDF (use pdf skill or pandoc) and include in leadership briefs, IRB packages, or dataset release notes.
6. Consider publishing the Data Card alongside the dataset (GitHub, Hugging Face dataset card, internal portal) and linking it from your knowledge graph or nanopublications.

## References & Further Reading

- Playbook site: https://sites.research.google/datacardsplaybook/
- GitHub (archived): https://github.com/PAIR-code/datacardsplaybook
- Foundational paper: "Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI" (FAccT 2022)
- Related: Datasheets for Datasets (Gebru et al.), Model Cards (Mitchell et al.), Healthsheets
- Your org context: Use alongside infographic-generator for visual summaries, rdf-kg-generator for semantic representation of the Data Card itself, and docx/pdf skills for final packaging.

Load `references/datacard-specification.md` for expanded guidance per section, example questions from the original template, and healthcare-specific prompts.