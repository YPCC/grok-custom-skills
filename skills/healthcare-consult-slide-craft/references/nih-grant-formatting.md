# NIH Grant Proposal Formatting Rules

Use this reference when creating decks, slides, or recommendations related to NIH grant support, Principal Investigator productivity tools, agentic AI for proposal writing, research administration, or compliance automation.

**Always note:** The specific Notice of Funding Opportunity (NOFO) supersedes general rules. Page limits and requirements can vary by activity code and NOFO.

## Core Formatting Requirements (SF424 / Forms I era)

These rules apply to most NIH application attachments, especially those with page limits.

| Requirement              | Rule                                                                 | Notes |
|--------------------------|----------------------------------------------------------------------|-------|
| Paper size               | Standard US Letter (8.5" × 11")                                       | — |
| Margins                  | At least 0.5" on all sides (top, bottom, left, right)                 | No applicant-supplied information may appear in the margins |
| Font size                | 11 points or larger                                                  | Smaller text allowed in figures/charts/tables if legible at 100% zoom |
| Recommended fonts        | Arial, Helvetica, Palatino Linotype, Georgia                         | Arial Narrow is **not** allowed. Other fonts acceptable only if they meet density rules |
| Type density             | ≤ 15 characters per linear inch (including spaces)                   | Critical compliance check |
| Line spacing             | ≤ 6 lines per vertical inch                                          | Often achieved with “Exactly 12 pt” line spacing in Word |
| Text color               | No formal restriction                                                | Black or high-contrast strongly recommended for legibility and printing |
| Column format            | Single-column preferred                                              | Multi-column can cause electronic review issues |
| Headers / Footers        | Do not put applicant information in headers or footers               | System automatically adds page numbers, PI name, etc. |

**Compliance risk:** Applications that violate font size, density, line spacing, or margin rules may be withdrawn from consideration before review.

## Common Page Limits

| Section                          | Typical Limit                  | Applies to |
|----------------------------------|--------------------------------|------------|
| Specific Aims                    | 1 page                         | Most research applications |
| Research Strategy                | 12 pages                       | R01, many U01, R15, R18, etc. |
| Research Strategy                | 6 pages                        | R21, R03, R34, many exploratory mechanisms |
| Project Summary / Abstract       | 30 lines of text               | All |
| Project Narrative                | 3 sentences                    | Most |
| Introduction (Resubmission)      | 1 page                         | Resubmissions / revisions |
| Biographical Sketch              | 5 pages (legacy) or SciENcv    | All senior/key personnel |
| Commercialization Plan           | 12 pages                       | SBIR/STTR |

**Important:** Always check the specific NOFO and the current Page Limits table on grants.nih.gov. Limits can differ for multi-component applications, special mechanisms, or updated forms.

## Research Strategy Structure (most R01-style)

Organize under these required headings (order matters):

1. **Significance**
2. **Innovation**
3. **Approach** (includes Preliminary Studies / Progress Report when applicable)

The entire Research Strategy (including figures, tables, and preliminary data) must fit within the page limit.

## Practical Implications for Agentic AI / PI Support Tools

When recommending or designing agentic AI solutions for Principal Investigators:

- The system must enforce or strongly guide users toward these rules (font, density, margins, page limits).
- Automatic compliance checking (character density, line count, margin detection, section length) is high-value.
- Specific Aims generator and Research Strategy section writers must respect the 1-page / 12-page (or 6-page) constraints.
- Real-time feedback on remaining page budget and density is a differentiating feature.
- Output should be easily exportable to compliant PDF that passes NIH automated checks.

## Sources for Latest Rules

- Official: https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide/format-attachments
- Page Limits table: https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide/page-limits
- Always verify against the current SF424 Application Guide and the specific NOFO.

## Font Density Calculation Methods (Practical)

NIH requires:
- **Type density** ≤ 15 characters per linear inch (including spaces)
- **Line spacing** ≤ 6 lines per vertical inch

These are the two most common automated compliance failure points.

### 1. Characters-per-inch (Horizontal Density)

**Simple page-width method (most used by research offices)**  
On a standard 8.5" page with 0.5" left + 0.5" right margins, the printable width is 7.5".  
Maximum allowed characters per line (including spaces) = 15 × 7.5 = **112.5 → practically 112 characters**.

**How to measure in practice**
1. Open the final PDF (or print-ready Word document).
2. Select a full line of body text in the densest section (often Methods or a paragraph with many short words).
3. Count every character **including spaces**.
4. Divide by the measured printable width in inches, **or** simply ensure the line never exceeds ~112 characters when margins are 0.5".

**Word / Google Docs tips that commonly cause violations**
- Justified alignment can compress inter-character spacing and push density over 15 cpi.
- Arial 11 pt is the most popular font but frequently exceeds the limit when justified.
- Fixes that work in practice:
  - Switch to Georgia 11 or 11.5 pt, **or**
  - Keep Arial 11 and set Character Spacing → Expanded by 0.1–0.2 pt.

### 2. Lines-per-inch (Vertical Density)

**Calculation**
- Printable height with 0.5" top + bottom margins = 10".
- Maximum lines = 6 × 10 = **60 lines per page**.

**How to measure**
1. Count the number of lines of body text on a representative full page.
2. Divide by the printable height in inches.
3. Or set Word line spacing to “Exactly 12 pt” (which yields approximately 6 lines per inch at 11 pt font).

### 3. Automated / Tool-Assisted Checking
- Some institutional tools and commercial proposal platforms measure both horizontal character density and vertical line density on the final PDF.
- eRA / ASSIST perform automated checks; applications that fail can be withdrawn before review.
- Always verify the **final flattened PDF**, because some PDF converters shrink fonts.

### Practical Rule of Thumb for Agentic Systems
When generating or checking text:
- Target ≤ 110–112 characters per line (including spaces) for 0.5" margins.
- Prefer “Exactly 12 pt” line spacing.
- Avoid pure justified alignment with Arial 11 unless character spacing is slightly expanded.
- Flag any line that exceeds 112 characters or any page that exceeds ~60 lines of body text.
