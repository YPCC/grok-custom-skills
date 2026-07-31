# bib-audit

Bibliography integrity skill for Grok — flags hallucinated references, fabricated DOIs/arXiv IDs, metadata mismatches, and formatting issues.

Adapted from [isaaccorley/skills bib-audit](https://github.com/isaaccorley/skills/tree/main/plugins/bib-audit) (MIT).

## Quick install

```bash
rsync -av skills/bib-audit/ ~/.grok/skills/bib-audit/
cd ~/.grok/skills/bib-audit
bash scripts/fetch_upstream_scripts.sh   # pulls the full Python audit suite
```

Or from this repo root:

```bash
cd skills/bib-audit && bash scripts/fetch_upstream_scripts.sh
```

## Run

```bash
python3 scripts/validate_refs.py path/to/refs.bib
python3 scripts/validate_refs.py refs.bib --key somekey --show-bibtex
python3 scripts/lookup_id.py "Paper Title" --author Surname
```

See [SKILL.md](SKILL.md) for the full workflow (PDF extraction, verdicts, review etiquette, style rules).

## Example

See [examples/bib-audit/](../../examples/bib-audit/) for a sample `.bib` with intentional issues and expected findings.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Offline, stdlib-only, no network required for the unit tests.
