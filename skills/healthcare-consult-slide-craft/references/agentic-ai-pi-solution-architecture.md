# Agentic AI Solution Architecture for Principal Investigator Grant Support

Representative reference architecture for an enterprise-grade agentic AI platform that helps Principal Investigators (PIs) prepare, validate, and submit grant proposals — with special alignment to academic medical center environments such as Mayo Clinic’s OSPA (Office of Sponsored Projects Administration).

This document synthesizes a modern, production-oriented design (Cloud-native, multi-agent, human-in-the-loop) that can be used when creating strategy decks, solution proposals, or implementation roadmaps for PI-facing grant tools.

**Do not treat this as a Mayo Clinic proprietary specification.** It is a generalized, high-fidelity pattern inspired by public architectural thinking for OSPA-mediated grant submission platforms.

---

## 1. Solution Goals

- Reduce administrative burden on PIs while increasing compliance and submission quality.
- Insert an intelligent intermediate layer between the PI and institutional (OSPA) + external (NIH/NSF/etc.) requirements.
- Provide continuous readiness scoring, missing-component detection, and guided remediation.
- Maintain full auditability, security (HIPAA/HITRUST-aligned), and human oversight.
- Support both single-PI and multi-PI workflows, modular/detailed budgets, and institutional internal deadlines.

---

## 2. High-Level Solution Components

### Core Multi-Agent Pipeline (Sequential + Orchestrated)

| Agent | Primary Responsibility |
|-------|------------------------|
| **Intake Agent** | Validate uploaded files, classify package type, generate initial metadata |
| **Document Intelligence Agent** | OCR / parsing, entity extraction, citation detection, layout understanding |
| **Compliance Agent** | Evaluate against NIH / FOA / institutional (OSPA) rules, policy checks |
| **Missing Component Agent** | Detect absent required documents (biosketch, Other Support, specific sections, attachments) |
| **Readiness Agent** | Score overall readiness, perform gap analysis, risk ranking, generate recommendations |
| **Submission Agent** | Assemble final payload, generate submission package, interface with eRA / institutional portals, track status |

These agents are orchestrated by a central planner (LangGraph-style) that breaks goals into steps, routes to specialized agents, and evaluates intermediate results.

### Supporting Layers

- **Shared State & Memory** — Persistent conversation and document state (typically Redis / Memorystore).
- **MCP Tool Registry** — Catalog of tools the agents can call (document AI, vector search, SQL access, rules engine, web/API connectors, email/notification).
- **LLM & Reasoning Layer** — Planning, summarization, explanation generation, re-ranking (e.g., Gemini on Vertex AI).
- **Human-in-the-Loop** — Review, override, approve, and feedback loops (especially for OSPA reviewers and Navigators).

---

## 3. Typical User Roles & Interfaces

| Role | Primary Actions |
|------|-----------------|
| **PI / Researcher** | Upload package, ask guidance, check readiness, track submission |
| **Navigator (PI support)** | Guidance, Q&A, readiness insights |
| **OSPA Reviewer** | Review queue, findings, overrides, comments, scores |
| **Admin / Ops** | Rules, configuration, user management, monitoring |

Common front-end surfaces:
- Intake / Reviewer / Navigator / Admin web applications (Cloud Run)
- Chat / Assistant interface
- API and email channels

---

## 4. Representative Tech Stack (Cloud-Native Pattern)

**Compute & Orchestration**
- Cloud Run (stateless services for agents and portals)
- Google ADK + LangGraph (agent orchestration and stateful workflows)
- Apigee API Gateway (with Identity-Aware Proxy / institutional SSO)

**AI / ML**
- Vertex AI (Gemini models for planning & reasoning)
- Vertex AI Vector Search / embeddings
- Document AI (OCR, layout, entity extraction)
- Vertex AI Evaluation

**Data & State**
- Memorystore (Redis) — shared agent state
- AlloyDB (PostgreSQL) — relational metadata, users, rules, workflows
- BigQuery — analytics, reporting, usage metrics
- Firestore — business rules, configuration, lightweight documents
- Cloud Storage — raw documents, attachments, parsed text

**Platform & Security**
- Secret Manager, Cloud Scheduler, Pub/Sub, Workflows
- VPC, IAM, CMEK, DLP, Access Approval
- Cloud Logging / Monitoring / Trace / Audit Logs
- HIPAA / HITRUST aligned controls

**External Integrations**
- NIH eRA Commons / ASSIST APIs
- Other agency portals
- Institutional SSO / IAM, Finance / Budget systems, DMS / ECM, Data Warehouse

---

## 5. Typical End-to-End Workflow

1. **PI uploads** proposal package (or individual documents) via Intake Portal or chat.
2. **Intake Agent** validates files and creates metadata.
3. **Document Intelligence Agent** extracts text, entities, citations, and structure.
4. **Compliance Agent** checks against current NIH / FOA / OSPA rules (page limits, font/margin, salary cap, modular budget rules, Other Support completeness, COI status, etc.).
5. **Missing Component Agent** flags absent required items (Specific Aims, biosketches, Leadership Plan for multi-PI, DMS justification, etc.).
6. **Readiness Agent** produces a scored readiness report + prioritized remediation list.
7. **Human-in-the-loop** (PI, Navigator, or OSPA Reviewer) reviews findings, supplies missing information, or overrides.
8. **Submission Agent** assembles the final compliant package and either:
   - Hands it to OSPA for official institutional submission, or
   - Submits directly via eRA / Grants.gov when institutional policy allows.
9. Status, audit logs, and notifications are written back to the shared state and observability layer.

The same pipeline can be invoked iteratively (“check readiness again after I uploaded the revised Other Support”).

---

## 6. Key Design Principles for Grant-Focused Agentic Systems

- **Institutional gatekeeping first** — Always respect OSPA (or equivalent) internal deadlines and review requirements. The system should never bypass the institutional submitting office.
- **Rules as data** — NIH, NSF, FOA-specific, and institutional rules should live in a queryable rules engine / knowledge store so they can be updated without code changes.
- **Citation & reference integrity** — Integrate with a dedicated citation audit capability (see `bib-audit` skill) as part of the Compliance or Document Intelligence stage.
- **Explainability** — Every flag or score must be accompanied by a clear explanation tied to a specific rule or source.
- **Progressive disclosure of complexity** — PIs see a simple readiness score and action list; OSPA staff and admins see full rule traces and audit logs.
- **Human authority remains final** — Agents recommend; authorized humans (PI or OSPA) approve.

---

## 7. How This Reference Should Be Used in Decks & Proposals

When creating MBB-style slides or solution proposals for agentic AI grant support:

- Use the six-agent pipeline as the core “how it works” story.
- Show the separation of PI-facing experience vs OSPA / institutional control plane.
- Highlight the tech stack only at the level needed for the audience (executive vs technical).
- Always call out the mandatory human-in-the-loop and institutional submission authority.
- Map specific NIH / OSPA compliance checks (modular budget, salary cap, DMS justification, multi-PI Leadership Plan, internal deadlines, Other Support, COI) onto the Compliance and Missing Component agents.

This architecture pattern keeps the solution both ambitious and realistic for a regulated academic medical center environment.

---

## 8. Specific Compliance Workflow Steps

The Compliance Agent (working with Document Intelligence, Missing Component, and Readiness Agents) executes a structured, multi-stage compliance workflow. Below is the recommended sequence that aligns with NIH, NSF, and institutional (OSPA) requirements.

### Stage 1 – Package Intake & Structural Validation
1. Confirm all uploaded files are readable and correctly classified (PDF, DOCX, etc.).
2. Detect application type (R01, R03, R21, NSF, foundation, multi-PI, clinical trial, etc.).
3. Identify whether the submission is new, renewal, resubmission, or revision.
4. Extract key metadata: FOA/NOFO number, due date, activity code, PI names, institution.

### Stage 2 – Formatting & Page-Limit Checks (NIH / NSF)
5. Verify font type and size (NIH: Arial/Georgia/Helvetica/Palatino ≥ 11 pt; NSF: ≤ 15 characters/inch, ≤ 6 lines/inch).
6. Check margins (NIH ≥ 0.5"; NSF = 1" all sides).
7. Measure line spacing and density (NIH: ≥ 3 lines/vertical inch recommended).
8. Enforce page limits:
   - Specific Aims = 1 page
   - Research Strategy = 12 pages (most R01s) or 6 pages (R03/R21)
   - NSF Project Description ≤ 15 pages
   - NSF Budget Justification ≤ 5 pages
9. Flag any hyperlinks or forbidden formatting in restricted sections.

### Stage 3 – Budget Compliance
10. Determine modular vs detailed budget requirement:
    - Modular if ≤ $250k direct costs/year (excluding consortium F&A) and eligible activity code.
    - Detailed otherwise.
11. Validate module count is in $25k increments and ≤ 10 modules/year.
12. Apply current NIH salary cap ($228,000 as of early 2026) when estimating personnel costs.
13. Check for required justifications:
    - Personnel Justification (name, role, person-months — no salary dollars on modular).
    - Consortium Justification (if applicable).
    - Data Management & Sharing Justification (explicitly labeled, even if $0).
14. Flag requests ≥ $500k direct costs (note: formal prior IC approval no longer required after Dec 2025, but heightened scrutiny still expected).
15. Surface any IC-specific renewal caps or administrative reduction policies.

### Stage 4 – Required Documents & Content Completeness
16. Verify presence of:
    - Specific Aims
    - Research Strategy / Project Description
    - Bibliography
    - Biosketches (Common Forms / SciENcv for NIH due dates on/after Jan 25, 2026)
    - Other Support / Current & Pending Support
    - Facilities & Other Resources
    - Equipment (if applicable)
    - Multi-PI Leadership Plan (when more than one PD/PI)
    - Clinical trial dissemination plan (when applicable)
    - Data Management & Sharing Plan
17. Cross-check that all senior/key personnel have eRA Commons IDs and ORCID iDs (NIH).
18. Run citation integrity check (delegate to `bib-audit` capability) on the reference list.

### Stage 5 – Institutional (OSPA) Gatekeeping
19. Confirm the package respects the institution’s internal deadline (earlier than sponsor deadline).
20. Verify COI disclosures are current for all listed personnel.
21. Ensure budget has been (or is ready to be) reviewed in the institutional system (e.g., MIRIS at Mayo).
22. Confirm the package is prepared for official submission by the institutional office (OSPA), not direct PI submission (unless policy explicitly allows).
23. Surface any cost-sharing or F&A waiver requests that require departmental/OSPA approval.

### Stage 6 – Readiness Scoring & Human Handoff
24. Produce a structured readiness score with severity-ranked findings.
25. Generate a prioritized remediation list mapped to specific rules and sources.
26. Route high-severity or judgmental items to human-in-the-loop (PI → Navigator → OSPA Reviewer).
27. Log every automated finding and human override for auditability.
28. Only after institutional approval does the Submission Agent assemble the final payload for eRA Commons / Grants.gov / other portals.

### Design Notes for Implementation
- Rules should be stored as data (Firestore / rules engine) so NIH notices, IC policies, and institutional SOPs can be updated without code changes.
- Every flag must cite the specific rule source (e.g., “NIH GPS Section…”, “NOT-OD-26-019”, “Mayo COI Policy”, “OSPA internal deadline”).
- The workflow is iterative: after the PI uploads a corrected document, Stages 2–6 can be re-run selectively.
- Citation checking is delegated to the dedicated `bib-audit` skill rather than re-implemented.
