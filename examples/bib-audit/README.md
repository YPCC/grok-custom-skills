# bib-audit example

Demonstrates the [bib-audit](../../skills/bib-audit/) skill on a small `.bib` that mixes real entries with intentional problems.

## Files

| File | Description |
|------|-------------|
| `sample_with_issues.bib` | 6 entries: 2 clean, 1 fabricated DOI, 1 DOI pointing at the wrong paper, 1 truncated-author + `and others`, 1 formatting nits |

## Run the audit

From the skill directory (or after installing the skill):

```bash
python3 skills/bib-audit/scripts/validate_refs.py \
  examples/bib-audit/sample_with_issues.bib
```

Useful flags:

```bash
# Focus on one key and print publisher BibTeX ready to paste
python3 skills/bib-audit/scripts/validate_refs.py \
  examples/bib-audit/sample_with_issues.bib \
  --key wrong_doi_points_elsewhere --show-bibtex

# Single-title identifier lookup
python3 skills/bib-audit/scripts/lookup_id.py \
  "Decoupled Weight Decay Regularization" --author Loshchilov
```

## Expected findings (illustrative)

| Key | Expected tier / verdict | Why |
|-----|-------------------------|-----|
| `adamw2019` | OK / mild CHECK | Real arXiv preprint → ICLR 2019; year/author list can legitimately differ |
| `unet2015` | OK | Real DOI, correct metadata |
| `fake_doi_2024` | **P1/P2 FABRICATED** | DOI does not resolve; title/authors invented |
| `wrong_doi_points_elsewhere` | **P2 MISMATCH** | DOI resolves to the U-Net paper, not “Attention Is All You Need” |
| `truncated_authors` | P3 | `and others` + missing co-authors (full list is longer) |
| `formatting_nits` | P4 | Double-braced ALL-CAPS title, `J.D.` initials, single-hyphen page range, DOI stored as URL |

## Design note

The skill deliberately ranks **integrity issues (P1/P2) above housekeeping (P3/P4)**. A false fabrication accusation is considered worse than a miss, so ambiguous cases are downgraded to advisory `[CHECK]`.

Original skill: [isaaccorley/skills bib-audit](https://github.com/isaaccorley/skills/tree/main/plugins/bib-audit).
