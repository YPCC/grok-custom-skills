---
name: bib-audit
description: Flag hallucinated references, authors and bib items, and correct badly formatted ones, in any paper — your own draft (run it before submitting) or one you are reviewing — from a .bib file, a PDF, or a pasted reference list. Checks every entry against Crossref (DOI), arXiv (eprint ID), and title search; detects fabricated DOIs/arXiv IDs, hallucinated titles and authors, truncated author lists, wrong years; recovers canonical publisher BibTeX. Also citation-style rules (et al., cite spacing, shortcite, reference sorting, bib title capitalization). Use to validate/audit/check references, verify citations in a submission under review, fix bib entries, hunt hallucinated or invented citations, extract a bibliography from a PDF, look up a DOI/canonical BibTeX, or gate a pre-submission bibliography.
---

# Bib Audit

Inherited and adapted from [isaaccorley/skills bib-audit](https://github.com/isaaccorley/skills/tree/main/plugins/bib-audit).

Two jobs, in priority order. First, flag hallucinated references, authors and bib items, meaning works that don't exist, identifiers that name a different paper, and authors who aren't on the paper. Second, correct badly formatted references, by resolving every field from the registrar of record instead of hand-authoring it.

The core rule is to never author bib fields, only resolve them. Every reference should trace to a DOI or arXiv ID.

Why this matters more than tidiness. The whole idea is that authors run this *before* submitting, so that reviewers never have to spend their time spot-checking a bibliography to decide whether an LLM wrote the paper. Right now checking someone's references is unpaid cleanup for a mistake you didn't make, and reviewer attention is the scarcest thing in the process, so that's a lousy way to spend it. If everyone gates their own submission on this, the doubt goes away as a category. So the tool is built author-first: it's read-only, it exits non-zero for CI, and it tells you how to *fix* each finding rather than only naming it. Using it to audit someone else's submission works and is documented below, but that's the fallback, not the goal.

That priority sets the design bias too, which is that a false accusation is worse than a miss. A missed bad reference is one entry a reviewer might still catch, while a false "fabricated" verdict on a correct entry destroys trust in the whole report, and in a review it puts an integrity allegation next to someone's name. When in doubt the tool downgrades to advisory rather than escalating.

Both situations differ only in what you do with a finding:

- **Your own paper** (draft, pre-submission, camera-ready). Fix in place. Replace fields from the canonical source, add missing identifiers, re-run until the audit is clean, then wire it into CI as a gate.
- **Someone else's paper** (peer review, reading a preprint, checking a collaborator's draft). You can't fix it, so the output is evidence. Resolve each finding to "identifier names no paper" or "identifier names a different paper" *before* saying anything, quote the specific entry, and read the review-etiquette note below, because a citation-manager glitch and deliberate fabrication look identical in the audit output.

## Quick start

All scripts live under this skill's `scripts/` directory. Run them with `python3` via the bash tool. They are stdlib-only (no extra deps) and read-only.

### .bib file (preferred, fully automatic)

```bash
python3 scripts/validate_refs.py path/to/refs.bib
python3 scripts/validate_refs.py refs.bib --key somekey2024 --show-bibtex
```

### PDF or pasted reference list

Three steps. Step 2 is a language task (you extract structured fields); never automate it with heuristics.

```bash
# 1. Extract reference-list text (plain pdftotext, NOT -layout)
pdftotext paper.pdf - | tr -d '\f' | sed -n '/^[[:space:]]*References[[:space:]]*$/,$p' > refs.txt

# 2. READ refs.txt and write refs.json yourself: one object per reference
#    Schema is documented in scripts/audit_refs.py — title required;
#    doi/arxiv ONLY if the printed reference actually contains one.
#    Extract in chunks of ~20 references. Mark kind and authors_truncated.

# 3. Resolve and rank
python3 scripts/audit_refs.py refs.json
```

Fill in `kind` and `authors_truncated` as you extract. Mark datasets, agency reports, software, standards and web pages as non-`article` (DOI registries do not index them). Mark `authors_truncated` whenever the reference printed "et al.".

Do the extraction step yourself. Turning a rendered reference list back into fields is a language task; every false "fabricated" verdict in testing traced to a title- or reference-splitting heuristic. Only fill in `doi`/`arxiv` when the reference actually prints one.

### Legacy heuristic path (CI / non-interactive only)

```bash
python3 scripts/resolve_refs.py refs.txt
```

Every finding is capped at P3 (advisory) and labelled PROVISIONAL. Prefer `audit_refs.py` for any verdict you must defend.

### Single-paper identifier lookup

```bash
python3 scripts/lookup_id.py "Decoupled Weight Decay Regularization" --author Loshchilov
python3 scripts/lookup_id.py --arxiv-id 1711.05101
```

### Optional environment variables

Read from the environment only (never CLI flags):

- `BIB_AUDIT_MAILTO=you@example.org` — joins Crossref's polite pool.
- `S2_API_KEY=…` — authenticates Semantic Scholar (recommended; request at https://www.semanticscholar.org/product/api).

## Getting references out of a PDF

`pdftotext` (poppler) is the reliable path and is available in this environment.

Use plain `pdftotext`, **not** `-layout`. On two-column papers (most CVPR/ICCV/NeurIPS) `-layout` splices left and right columns so no reference survives intact. Plain mode follows the content stream.

If arXiv LaTeX source is available, parse the `.bbl` instead of the PDF. It has one `\bibitem` per reference, in order, none of the de-hyphenation or form-feed problems.

Papers under review often carry margin line numbers. `resolve_refs.py` detects and strips them (`strip_line_numbers`).

PDF text extraction hard-wraps mid-token. A DOI can arrive split across lines; naively rejoining with a space truncates it and produces a false fabrication verdict. Spot-check parses:

```bash
python3 -c "
import sys; sys.path.insert(0, 'scripts')
from refparse import split_references, printed_doi, printed_arxiv
for i, r in enumerate(split_references(open('refs.txt').read()), 1):
    print(i, printed_doi(r), printed_arxiv(r), r[:90])
"
```

Strip form feeds (`tr -d '\f'`). Count references before trusting any verdict (compare against highest marker number for numbered lists, or against `\bibitem` count from LaTeX).

## Verdicts and what to do with each

| Verdict | Meaning | Action |
|---|---|---|
| `[OK]` | Matches authoritative metadata | Nothing |
| `[FABRICATED]` | The entry's own DOI/arXiv ID names no paper, or names a work whose title is clearly not the one cited | Fix the **identifier**, never the title |
| `[MISMATCH]` | DOI/arXiv pins the work and the bib disagrees | Replace fields with `--show-bibtex` output |
| `[NOT FOUND]` (PDF path) | No Crossref/arXiv/OpenAlex match | Check extraction, then suspect invented paper |
| `[SUSPECT]` (legacy only) | Same evidence as FABRICATED but via heuristic parse | Re-run through `audit_refs.py` |
| `[CHECK]` | Fuzzy title-search bound something that differs, or preprint-vs-published drift | Verify by hand; best fix is adding a doi/eprint |
| `[UNRESOLVED]` | No DOI/arXiv ID and no close title match | Add an identifier |
| `[LOOKUP FAILED]` | Rate limit or API outage | Not a finding — re-run those entries |
| `[UNVERIFIABLE]` | Grey literature or anonymized for blind review | Expected; never a fabrication signal |

## Priority order for fixing

Scripts print the per-reference log first, then a ranked findings section (`scripts/triage.py`). Fix top-down.

| Tier | What it means | Why it ranks here |
|---|---|---|
| **P1** | The cited work isn't found anywhere | The sentence citing it has no support |
| **P2** | Fabricated identifier, or an invented author | Points at the wrong paper, or credits someone for work they didn't do |
| **P3** | Wrong metadata on a real, correctly-identified work | Truncated author lists, preprint-vs-published year drift |
| **P4** | Formatting and style | Mechanical; batch-fixable last |

P4 findings are checked by `scripts/bibstyle.py` on the `.bib` path: single-hyphen page ranges, DOIs stored as URLs, double-braced titles, `J.D.` initials, literal `and others`, etc.

### The "and others" tell

`author = {Smith, J. and others}` is valid BibTeX and renders as "et al.", so it never looks broken in the PDF. It is reported at P3 because a real reference-manager export writes every author. Recurrence across multiple entries is a generation-artifact signal.

## Fabricated identifiers and authors (hunt these first)

Four shapes, worst first:

1. Identifier resolves but to a different paper → `[MISMATCH]` with title diff. Fix the identifier, never the title.
2. Identifier does not resolve at all (dead DOI or non-existent arXiv ID) → `[FABRICATED]`.
3. Real paper, invented authors → extra surname the registrar does not have.
4. The paper does not exist → title search misses across Crossref *and* OpenAlex *and* arXiv.

An entry with no `doi`/`eprint` is unfalsifiable; resolve it before trusting it.

### Reporting this in a review

The audit finds *wrong metadata*. It cannot tell you *why*. Before writing anything:

- Anonymized references ("Anonymous. Title. Under review.") are unresolvable by design; scripts detect them and report `[CHECK]`, never `[FABRICATED]`.
- Re-verify every serious finding yourself in a browser.
- Report the observation, not the motive: "Ref [14]'s DOI resolves to a different paper" is useful; "the authors fabricated citations" is the editor's call.
- Count before you generalize. One bad DOI in forty is noise; a cluster is a pattern.
- Keep formatting nits separate from identifiers that name no paper.

## Workflow: fixing your own bibliography

1. Run the audit. Triage by verdict, `[FABRICATED]` first.
2. For each `[MISMATCH]`: re-run with `--key <key> --show-bibtex` to get the publisher's own BibTeX ready to paste.
3. For `[UNRESOLVED]`/`[CHECK]` real papers: find the identifier with `lookup_id.py`, add it, re-run.
4. Re-run until 0 mismatches. Rebuild the paper to confirm.

## Workflow: auditing a paper you did not write

1. Extract the reference list, verify the parse (count matches, no truncated DOIs).
2. Run the appropriate script. Read `[FABRICATED]` and `[NOT FOUND]` first.
3. Hand-verify every serious finding in a browser.
4. Write it up per the review-etiquette rules above.
5. Optional: `--emit-bibtex` recovers a real `.bib` from PDF references.

For API endpoints, curl one-liners, source ranking and per-source caveats, read [references/metadata-apis.md](references/metadata-apis.md).

## Non-obvious gotchas

- arXiv DOIs (`10.48550/arXiv.*`) 404 on Crossref; route to the arXiv API (scripts do this).
- Preprint ≠ published. arXiv year is usually v1 year; author lists can differ. Never hard-fail these.
- Title-search false binds are common on Crossref. Search hits are advisory only — pin with an identifier.
- LaTeX accents must be decoded before author comparison (`H{\"a}nsch` → `Hänsch`).
- Online-first vs print year: both can be correct; scripts accept any deposited date.
- Google Scholar BibTeX is discovery, not canonical. Prefer Crossref content negotiation > DBLP for CS/ML > arXiv export.
- ICLR/OpenReview papers have no page numbers; delete fake `pages = {1--N}`.
- Semantic Scholar is for existence/citation graphs only, never for metadata comparison (it abbreviates names and lowercases titles).
- Prefer `id_list` over `search_query` for the arXiv API.

## Citation and reference style

Distilled from John Owens (UC Davis) and Henning Schulzrinne (Columbia), plus Chicago 7.56.

- Never cite as a noun. "A similar strategy is discussed by AuthorOne et al. [15]", not "described in [15]".
- "et al." takes a period after "al" only and is never italicized. One author = A, two = A and B, three+ = A et al.
- `text~\cite{key}` with a non-breaking `~`. Multiple works in one `\cite{a,b}` ordered so numbers ascend.
- `\shortcite` when the author is already named in the sentence.
- Sort the reference list alphabetically by first author's last name (cited-order only for surveys).
- Brace only the specific words that must keep caps (`{L}oop`, `{GPU}`); never double-brace the whole title.
- ACM/IEEE Digital Library BibTeX ships systematic errors (venue capitalization, mangled booktitles, spelled-out months). Clean them.
- Citation placement: right after the author name. "et al." makes the subject plural.

## Bib entry hygiene

Sourced from John Owens's "Common Errors in Bibliographies" (https://www.ece.ucdavis.edu/~jowens/biberrors.html).

- Author names exactly as printed, diacritics and all. Initials space-separated: `J. D. Owens`, never `J.D.`.
- Titles as printed; brace only must-capitalize words. Never double-brace the whole title.
- Months as BibTeX macros: `month = mar`, `month = jun # "\slash " # jul`.
- Pages always with en-dash: `35--49`. Electronic proceedings use `12:1--12:10`. Every entry starting at page 1 means the pages are fake — omit them.
- Record a DOI (number only, never the URL) in every entry that has one. Do not duplicate it in `url`.
- URLs in `\url{}`.

## Scripts reference

| Script | Purpose |
|---|---|
| `validate_refs.py` | Audit a structured `.bib` file (preferred path) |
| `audit_refs.py` | Audit a hand-extracted `refs.json` from PDF/text |
| `resolve_refs.py` | Legacy heuristic path for non-interactive / CI |
| `lookup_id.py` | Find DOI or arXiv ID for a single title |
| `bibmeta.py` | Shared API resolution helpers |
| `refparse.py` | Split and clean extracted reference text |
| `bibstyle.py` | Mechanical P4 formatting checks |
| `triage.py` | Rank findings into P1–P4 tiers |

All scripts are offline-testable (see `tests/`) and dependency-free.

## Credits

Formatting and style rules distilled from John Owens (UC Davis) Common Errors in Bibliographies and Henning Schulzrinne (Columbia) writing-style guide. Original skill by isaaccorley. MIT licensed.
