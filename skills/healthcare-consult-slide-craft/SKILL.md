---
name: healthcare-consult-slide-craft
description: Create healthcare consulting presentations, full editable PowerPoint decks, single slides, one-pagers, and professional infographics in a clean MBB hybrid style (McKinsey + BCG + Bain principles). Enforces action titles, Pyramid Principle, SCR storyline, one-message-per-slide, MECE structure, and strict visual discipline. Use for strategy decks, clinical/operational presentations, digital health pitches, market assessments, board materials, grant strategy, research administration, agentic AI solutions for investigators, or any healthcare consulting deliverable. Triggers include healthcare consulting deck, MBB style slides, McKinsey healthcare presentation, BCG healthcare, Bain style, consulting infographic, action title slides, strategy deck healthcare, ghost deck, grant proposal AI, principal investigator tools.
---

# Healthcare Consult Slide Craft

Create high-quality healthcare consulting slides and decks that follow top-tier MBB (McKinsey, BCG, Bain) standards in a clean hybrid style. Every deliverable is an argument, not decoration.

Default to the hybrid style defined in `references/design-system.md`. Switch to pure McKinsey, BCG, or Bain style only when the user explicitly requests it (see `references/firm-variants.md`).

## Modes of Operation

Determine the mode from context. If ambiguous, ask once.

1. **Draft** — Create a new deck, slide, one-pager, or infographic from scratch.
2. **Critique** — Evaluate an existing deck or slide against MBB hybrid standards.
3. **Update** — Improve an existing deck or slide with targeted changes.

## Non-Negotiable Principles

Apply these to every mode and every deliverable:

- **Action titles, not topic titles.** Every slide title is a complete sentence stating the takeaway (maximum 15 words / two lines). The sequence of titles alone must tell the full argument.
- **Pyramid Principle.** Lead with the answer/recommendation. Support with MECE arguments. Evidence sits at the bottom.
- **SCR narrative.** Situation → Complication → Resolution for the overall storyline (and for executive summaries).
- **One message per slide.** Every visual, number, and text block exists only to prove the action title. If it does not, remove or move it.
- **So-what test.** The implication must be explicit. Never leave the audience asking “so what?”
- **Exhibit-driven.** Prefer a single clear chart, framework, table, or process visual over bullet-heavy slides. Bullets are a last resort (maximum 3–5 short points).
- **Ghost deck first.** Always write the full sequence of action titles and get approval before designing slide bodies or generating visuals.
- **Source everything.** Every data point carries a source citation (bottom of slide, 8–9 pt).
- **MECE structure.** Arguments, sections, and frameworks must be mutually exclusive and collectively exhaustive.

## Hybrid Design System (Default)

Enforce the rules in `references/design-system.md`. Key constraints:

- Pure white background
- One consistent hybrid color palette (deep navy primary + teal accent + controlled secondary)
- Clean modern sans-serif typography with strict hierarchy and consistent sizing
- Generous whitespace, precise alignment, minimal clutter
- Flat vector icons and thin elegant connectors when used
- Charts and exhibits that make the action title obvious at a glance

## Workflow — Draft Mode

1. **Clarify the brief**  
   Audience, decision the deck must drive, constraints (length, time, template), available data, and healthcare context (provider, payer, life sciences, digital health, etc.).

2. **Build the ghost deck**  
   Write only the sequence of action titles (plus a one-line note of the intended exhibit type). Structure typically:
   - Title / cover
   - Executive summary (SCR, bold-claim + evidence format)
   - Situation (1–2 slides)
   - Complication (2–4 slides)
   - Resolution / recommendations (MECE pillars)
   - Roadmap / next steps / ask
   - Appendix (supporting detail only)

   Present the ghost deck to the user for approval before any design work.

3. **Route the output**  
   - Multi-slide deck or one-pager → use the `pptx` skill and force every rule in this skill into the slides. Output must be a native editable `.pptx`.
   - Single-slide visual or standalone infographic → use `generate_image` (and `edit_image` for refinement) with a precise prompt that follows the hybrid design system. Absorb and elevate the professional healthcare consulting aesthetic previously handled by the older infographic skill.

4. **Pressure-test before delivery**  
   - Titles alone tell a coherent SCR story.
   - Every slide passes the one-message and so-what tests.
   - Sources are present.
   - Visuals are clean, aligned, and on-brand.
   - No anti-patterns (see `references/anti-patterns.md`).

## Workflow — Critique Mode

Evaluate against the checklist in `references/critique-checklist.md`.  
Structure feedback in three tiers:

1. Structural / narrative issues
2. Slide-level issues (rewrite weak titles explicitly)
3. Polish and visual discipline

Be direct, specific, and constructive. Always show before/after title rewrites.

## Workflow — Update Mode

Run an internal critique, prioritize the highest-impact changes (title rewrites, executive summary, SCR ordering, exhibit upgrades, cutting redundancy), propose a short prioritized list, then execute the approved changes.

## Healthcare Consulting Flavor

When the topic is clinical, operational, digital health, market access, value-based care, patient journey, provider strategy, payer, or life sciences, lean into domain-appropriate frameworks (patient journey maps, care pathway, TAM/SAM/SOM for health markets, RAG status for implementations, etc.) while still obeying pure MBB structure and visual rules. Keep language precise and executive-ready.

## Quality Gate (Final Check)

Before delivering any work:

- [ ] Ghost deck / action titles approved and coherent when read alone
- [ ] Every title is an action title (complete sentence, ≤15 words)
- [ ] One clear message per slide
- [ ] SCR arc is visible
- [ ] MECE structure holds
- [ ] Sources present on data slides
- [ ] Hybrid design system followed (or pure firm style if requested)
- [ ] Output is native editable `.pptx` for decks, or high-quality generated image for pure visuals
- [ ] No anti-patterns remain

## References

Load only when needed:

- `references/design-system.md` — exact hybrid palette, fonts, margins, chart rules
- `references/firm-variants.md` — when and how to switch from hybrid to pure McKinsey / BCG / Bain
- `references/slide-patterns.md` — executive summary, recommendation, data, roadmap, market sizing, status, clinical frameworks
- `references/critique-checklist.md` — full evaluation dimensions
- `references/anti-patterns.md` — common failures to flag and fix
- `references/examples.md` — worked examples including agentic AI for principal investigator grant proposals
- `references/nih-grant-formatting.md` — current NIH proposal formatting rules (fonts, margins, density, page limits) for grant-related decks and recommendations
 - `references/nih-compliance-budgeting.md` — NIH registration (eRA Commons), submission portals (ASSIST/Grants.gov), R01/R03/R21 differences, modular vs detailed budget rules, must-have / must-not-have compliance
- `references/nsf-proposal-formatting.md` — current NSF PAPPG formatting rules (fonts, 1-inch margins, Project Summary structure, 15-page Project Description, etc.)
 - `references/mayo-ospa-guidelines.md` — Mayo Clinic OSPA intermediate office processes, internal deadlines, MIRIS budget workflow, COI, Other Support, and compliance gatekeeping
 - `references/sources-and-provenance.md` — Master mapping of external sources to skill files + full bibliography of verified links used to build NIH, NSF, and Mayo OSPA guidance
 - `references/agentic-ai-pi-solution-architecture.md` — Representative multi-agent architecture, components, tech stack, and workflows for an enterprise PI grant-support platform (OSPA-aligned)
