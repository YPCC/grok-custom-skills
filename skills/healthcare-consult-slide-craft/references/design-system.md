# Hybrid Design System

Default visual language for all deliverables. Override only when the user explicitly requests pure McKinsey, BCG, or Bain style.

## Color Palette (Strict)

| Role                        | Hex       | Usage |
|-----------------------------|-----------|-------|
| Background                  | #FFFFFF   | Always pure white |
| Primary (titles, key lines, headers) | #0A2540   | Deep navy — action titles, main structure |
| Accent 1 (highlights, key data, icons, connectors) | #00A3A1   | Teal — primary accent, callouts, icons |
| Accent 2 (secondary)        | #5B6ABF   | Soft indigo/purple — secondary elements, alternate series |
| Body text                   | #1F2A44   | Dark navy for high contrast |
| Supporting / cards / dividers | #E8ECF0 | Light gray |
| Subtle text / sources       | #5A6577   | Medium gray |
| Risk / alert (use sparingly)| #C8102E   | Strong red for RAG red or critical warnings only |

Use color purposefully. Never decorate. Highlight only the key insight on a chart.

## Typography

- **Titles / action titles**: Clean modern sans-serif, bold, consistent size across the entire deck (never vary title size).
- **Body / supporting text**: Same family, regular or medium weight.
- **Sources / footnotes**: 8–9 pt, medium gray.
- Prefer Arial, Calibri, or Helvetica-style fonts for maximum clarity and PowerPoint compatibility.
- Strict hierarchy: action title largest → subhead → body → source.
- Never use decorative, script, or overly stylized fonts.
- High contrast only.

## Layout & Spacing

- Generous intentional whitespace. Modern, not sparse or cramped.
- Consistent margins (minimum 0.5–0.6" from edges on standard 16:9).
- Precise alignment of all elements (left edges, columns, baselines).
- Grid discipline. Symmetric or balanced compositions preferred.
- One dominant visual per slide.

## Charts & Exhibits

- Single compelling exhibit preferred.
- Chart must make the action title obvious within 3 seconds.
- Clear axis labels, units, and data labels where needed.
- Use the accent teal (or controlled secondary) only to highlight the key series or callout.
- Avoid chart junk, 3D effects, heavy gridlines, or unnecessary legends.
- Common preferred types in healthcare consulting:
  - Horizontal bar for comparisons
  - Line or simple area for trends
  - Stacked bar for composition over time or categories
  - Waterfall for bridge analyses
  - Simple process / journey with thin teal connectors
  - 2×2 or matrix frameworks
  - KPI cards with large numbers + short insight

## Icons & Connectors (when used)

- Flat vector only — simple geometric shapes, consistent line weight, no gradients, shadows, or 3D.
- Thin, elegant connector arrows/lines in accent teal.
- Healthcare-appropriate but never cartoonish (patient, clinician, pathway, data flow, shield, hospital, network, etc.).

## Infographic-Specific Rules

When generating a standalone infographic (via `generate_image`):

- Pure white background
- Symmetric or strongly balanced layout
- Large bold action-style title at top
- Flat icons + short labels + minimal supporting text
- Thin teal connectors for flows or relationships
- High readability at a glance
- Executive / boardroom quality
- Iterate with `edit_image` until symmetry, spacing, text accuracy, and color fidelity are perfect

## PowerPoint Implementation Notes

When using the `pptx` skill:

- Lock the hybrid palette and font choices into the master / theme.
- Enforce identical action-title formatting on every slide.
- Place sources consistently at bottom-left or bottom-right in small gray text.
- Maintain generous margins and alignment across the deck.
- Prefer native editable charts and shapes over embedded images whenever possible.
