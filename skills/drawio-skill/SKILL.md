---
name: drawio-skill
description: Use for generating professional editable draw.io diagrams from natural language — architecture, ERD, UML class/sequence, flowcharts, ML models, system designs, network topologies. Trigger on any request for technical visualizations, flow diagrams, or when explaining multi-component systems. Outputs .drawio XML files for opening in draw.io app/desktop. Supports diagram-type presets, color palettes, swimlanes, precise orthogonal layouts, and iterative refinement.
---

# Draw.io Diagram Generation Skill

## Overview

Generate precise, editable `.drawio` XML files from natural language descriptions of systems, processes, data models, or architectures. The resulting files open directly in the free draw.io desktop application or https://app.diagrams.net for viewing, editing, and high-quality export (PNG/SVG/PDF/JPG with optional embedded XML for full editability).

This skill is ideal when polished vector output, swimlanes, custom geometry, precise control over layout/edges, or vendor-specific shapes are needed. It follows draw.io's mxGraphModel XML structure for maximum compatibility.

**Complements**: Use alongside Mermaid for simple git-friendly diagrams, or infographic-generator for high-level visual summaries. For hand-drawn/whiteboard feel, consider generate_image with descriptive prompts.

## Bundled Resources (read on demand)

| Resource                          | When to read / use |
|-----------------------------------|--------------------|
| `scripts/drawio_xml_builder.py`   | When generating any non-trivial diagram — provides `DrawioDiagram` class with `add_node`, `add_edge`, `add_swimlane`, automatic id management, escaping, and pretty XML output. Dramatically reduces manual XML errors. |
| `scripts/validate_drawio.py`      | After every generation or major edit — catches duplicate ids, missing geometry on edges, dangling references, etc. |
| `scripts/simple_grid_layout.py`   | For quick initial positioning of 5–20 nodes (grid or layered). Use before manual tuning. |
| `references/diagram-types.md`     | User requests a specific type (ERD, UML, Sequence, Architecture, Flowchart, ML/DL) — expanded guidance + examples. |
| `references/troubleshooting.md`   | Layout looks wrong, edges misbehave, refinement is hard, or you see validation errors. |
| `references/shapes-and-styles.md` | Need quick lookup for cylinder/swimlane/attachment points, flowAnimation, or healthcare-themed style suggestions. |

## When to Use This Skill

**Activate for**:
- Architecture / system / service diagrams with multiple components and flows
- ER diagrams, database schemas, data models
- UML class diagrams or sequence/interaction diagrams
- Flowcharts, decision trees, process flows (especially with swimlanes)
- ML/DL model architectures (Transformers, CNNs, pipelines with tensor shapes)
- Network topologies, infrastructure diagrams
- Any visualization with 4+ connected elements where clarity, alignment, and professional styling matter
- Proactively when user describes a complex system and visuals would help understanding

**Do NOT use (route elsewhere)**:
- Quick Mermaid/PlantUML diagrams-as-code for Markdown or git (output Mermaid syntax directly instead)
- Casual freehand or infinite-canvas sketches (use tldraw/excalidraw style or image gen)
- Purely textual explanations

## Workflow (Follow Strictly)

1. **Assess & Clarify (if needed, 1-3 questions max)**:
   - Diagram type/preset (ERD, UML Class, Sequence, Architecture, Flowchart, ML/DL Model, or general)
   - Key entities/components, their relationships, and any specific labels or annotations (e.g. tensor shapes, protocols)
   - Preferred layout direction (left-to-right / top-to-bottom) and any grouping (swimlanes by layer/service)
   - Output name and location (default: `/home/workdir/artifacts/<name>.drawio`)
   - Any style preference (corporate clean, or custom colors)

   Skip clarification for simple, fully-specified requests.

2. **Choose Diagram Type Preset** (guides structural conventions):
   - **ERD**: Rectangles for entities, diamonds or lines for relationships, attribute lists inside entities. Use cylinder for tables if preferred.
   - **UML Class**: Class boxes with 3 compartments (name, attributes, methods), inheritance arrows (hollow triangle), associations.
   - **Sequence**: Vertical lifelines, horizontal message arrows, activation bars, fragments (alt/opt/loop).
   - **Architecture**: Rounded rectangles or swimlanes for services/layers, arrows for API calls/data flows, icons via style keywords where known.
   - **Flowchart**: Start/end ellipses, process rectangles (rounded), decisions diamonds, data parallelograms, arrows with labels.
   - **ML/DL Model**: Layered blocks (encoder/decoder/attention), arrows with tensor annotations (e.g. `[batch, seq, dim]`), color by component type.
   - **General**: Flexible; default to clean rounded boxes + orthogonal arrows.

3. **Plan the Diagram**:
   - Identify nodes (vertices), edges, containers/groups/swimlanes.
   - Choose grid-aligned layout. Use horizontal/vertical bands for layers. Leave ~80px corridors for edge routing.
   - For >8-10 nodes: plan in tiers/rows, minimize crossings by strategic placement or explicit waypoints.
   - Group related items in swimlanes (titled containers) or invisible groups.
   - Decide colors from palette (or active preset). Use consistent fill/stroke per semantic type.

4. **Generate .drawio XML**:
   - **Preferred**: Use `scripts/drawio_xml_builder.py` (`DrawioDiagram` class). It handles ids, escaping, style strings, geometry, swimlanes, and pretty-printing automatically.
   - Fallback (simple diagrams): Start from the standard skeleton below and build manually.
   - Assign sequential integer ids starting at 2 (0 and 1 reserved).
   - Vertices: `vertex="1"`, `parent="1"` (or container id) + `<mxGeometry .../>`
   - Edges: `edge="1"`, `source=... target=...` + child `<mxGeometry relative="1" as="geometry"/>` (never self-closing). Include `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1`
   - Use `html=1;whiteSpace=wrap` in styles. Multi-line labels → `&#xa;` inside `value`.
   - Pin `exitX/exitY` + `entryX/entryY` when shapes have multiple connections.
   - Waypoints for routing: `<Array as="points">` inside geometry.
   - Apply colors from palette. For containers use `swimlane;startSize=30` or `group;pointerEvents=0;`.
   - After generation: run `python3 scripts/validate_drawio.py <file>` before showing the user.

5. **Persist the File**:
   - Write the complete XML to the target path in `/home/workdir/artifacts/` (create dir if needed via bash `mkdir -p`).
   - Use `write_file` tool or equivalent for the content. Name it descriptively, e.g. `architecture-overview.drawio` or `colorectal-triage-er.drawio`.
   - Confirm file creation and report the full path to user.

6. **Present & Iterate**:
   - Inform user the editable `.drawio` file is ready at the path. Instruct to open in draw.io desktop or web app (supports drag-drop or File > Open).
   - Describe the diagram briefly or highlight key design choices.
   - **Refinement**: On feedback ("move X left", "change color of Y to green", "add Z connecting to W", "make labels bigger", "add swimlane for backend"), perform **minimal targeted edits** to the existing XML (search/replace on specific mxCell by id or value). Re-write the file. Repeat up to 5 rounds. For major layout changes, regenerate the full diagram.
   - After 5 rounds suggest user fine-tunes manually in draw.io.

7. **Fallbacks**:
   - If diagram is very large/complex and manual placement is error-prone: generate Mermaid syntax as complementary output (user can render in many tools) or simplify scope.
   - For AI/LLM brand logos: provide style guidance or external image reference; draw.io can embed images via data URI or URL (advanced).
   - No automatic vision self-check or CLI export here — user performs final visual QA and export locally.

**Helper Scripts Tip**: After writing the `.drawio` file, always run the validator. For complex layouts, start with `simple_grid_layout.py` or `layered_layout` to get coordinates, then feed into the XML builder.

## Standard .drawio XML Skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- All user content starts here with id="2" and up -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Critical Rules**:
- Never omit id="0" and id="1".
- User mxCell ids start at 2, increment by 1, unique.
- All shapes have `parent="1"` unless inside a container (then parent's id).
- Edges **must** have child `<mxGeometry relative="1" as="geometry" />` — self-closing mxCell for edges is invalid.
- Use `html=1` everywhere for text.
- Grid snap: prefer x/y/width/height multiples of 10.

## Shape Examples (Vertices)

**Rounded rectangle (service/module)**:
```xml
<mxCell id="2" value="User Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>
```

**Ellipse / start-end**:
```xml
<mxCell id="3" value="Start" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="50" y="200" width="80" height="40" as="geometry" />
</mxCell>
```

**Diamond / decision**:
```xml
<mxCell id="4" value="Valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
  <mxGeometry x="300" y="180" width="120" height="80" as="geometry" />
</mxCell>
```

**Cylinder / database**:
```xml
<mxCell id="5" value="Patient DB" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
  <mxGeometry x="500" y="100" width="120" height="80" as="geometry" />
</mxCell>
```

**Swimlane container** (titled group):
```xml
<mxCell id="svc" value="Frontend Layer" style="swimlane;startSize=30;fillColor=#e1d5e7;strokeColor=#9673a6;html=1;" vertex="1" parent="1">
  <mxGeometry x="80" y="80" width="400" height="220" as="geometry" />
</mxCell>
<!-- Child inside (coords relative to swimlane) -->
<mxCell id="api" value="API Gateway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="svc">
  <mxGeometry x="20" y="50" width="140" height="50" as="geometry" />
</mxCell>
```

## Edge / Connector Examples

**Basic directed orthogonal arrow** (always include these style flags for clean routing):
```xml
<mxCell id="10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Labeled arrow with explicit attachment points** (prevents stacking on busy shapes):
```xml
<mxCell id="11" value="HTTPS / REST" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="4">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**Arrow with waypoints** (route around obstacles):
```xml
<mxCell id="12" value="Data Flow" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="3" target="5">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="420" y="150" />
      <mxPoint x="480" y="150" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Edge style tips**:
- Add `flowAnimation=1;` for animated data-flow dots (great in SVG/PDF exports and desktop).
- Distribute multiple connections on one side of a shape using different exitX/entryX fractions (e.g. 0.25, 0.5, 0.75).
- Keep final straight segment to target ≥20px to avoid arrowhead clipping on bends.
- For long edge labels: add `labelBackgroundColor=#ffffff;fontSize=11` and use geometry offsets if needed.

## Professional Color Palette (Default)

Use consistently for semantic meaning. No active preset overrides this.

| Semantic       | fillColor   | strokeColor | fontColor | Example Use              |
|----------------|-------------|-------------|-----------|--------------------------|
| Primary Blue   | #dae8fc    | #6c8ebf    | #333333  | Services, clients, APIs  |
| Green          | #d5e8d4    | #82b366    | #333333  | Success, DBs, healthy    |
| Yellow         | #fff2cc    | #d6b656    | #333333  | Decisions, queues        |
| Orange         | #ffe6cc    | #d79b00    | #333333  | Gateways, warnings       |
| Red/Pink       | #f8cecc    | #b85450    | #333333  | Errors, alerts, critical |
| Grey/Neutral   | #f5f5f5    | #666666    | #333333  | External, notes          |
| Purple         | #e1d5e7    | #9673a6    | #333333  | Security, auth, layers   |

Add `fontSize=11` or `12` for readability; `bold=1` for titles.

## Layout & Spacing Guidelines

- **Simple** (≤5 nodes): 200px horizontal, 150px vertical gaps.
- **Medium** (6-10): 280px / 200px.
- **Complex** (>10): 350px / 250px.
- Snap all coordinates to multiples of 10.
- Place "hub" nodes centrally; satellites around.
- Use swimlanes for logical layers (Frontend / Backend / Data).
- For tree structures: align children under parents (same center x).
- Always leave routing corridors empty between bands.
- Test mentally: trace every edge path; if it crosses a shape, add waypoint or move node.

## Iteration & Editing Rules

When user requests changes:
- **Minor** (color, label text, single node move/resize, add/remove one edge): Edit the specific `<mxCell>` in place via targeted string replace or XML parsing. Preserve all other layout work.
- **Structural / layout overhaul**: Regenerate the full diagram with updated plan.
- Keep the same output filename across iterations (overwrite).
- After edits, re-write the file and confirm with user.
- Safety: After 5+ rounds, recommend opening the file in draw.io for pixel-perfect manual tweaks (it has excellent grid, alignment, and library tools).

## Additional Capabilities & Future Extensions

- **Codebase visualization**: For Python projects, Python AST/import parsing can be added via scripts/ to extract graphs (then manual or simple layout). Currently describe structure in text and map to diagram.
- **Shape search**: For AWS/Azure/GCP/Cisco/K8s/UML icons, user can browse draw.io's built-in libraries (Huge library of 10k+ shapes). Provide style strings like `shape=mxgraph.aws4.lambda;` when known; otherwise use descriptive labels + color.
- **Presets**: Basic support via style adjustments (corporate = clean fills + thin strokes; handdrawn = add `sketch=1;`). Advanced user presets can be added later in references/.
- **Exports**: User performs in draw.io (recommend double-ext `.drawio.png` for embedded editable XML). For automated, user can run drawio CLI locally.

## Example Trigger Phrases

"Draw an architecture diagram for the patient triage system with FHIR, GraphDB, and agent orchestrator layers in swimlanes."
"Create an ERD for the pharmacy drug database including RxNorm mappings and nanopublications."
"UML class diagram for the clinical trial site activation workflow entities."
"Flowchart of the IRB approval process with decision points and swimlanes for sponsor vs site."
"Visualize the Transformer encoder-decoder with attention layers and tensor shape annotations."

This skill ensures consistent, high-quality, editable technical diagrams that integrate well with healthcare AI, knowledge graph, and clinical workflow documentation needs.

## References & Helpers

Additional detailed examples, troubleshooting, or scripts (e.g. XML builder helpers, shape constants) can be added to `references/` and `scripts/` as the skill evolves. Core knowledge is self-contained above for immediate use.