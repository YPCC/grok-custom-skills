# Sources & Provenance

Verified knowledge sources used to build and maintain the NIH, NSF, Mayo Clinic OSPA, and agentic-AI architecture reference material in this skill.

This file exists so that future updates can be traced back to primary sources and so that the agentic system (or human maintainers) can quickly see which external guidelines informed which skill entries.

---

## 1. Mapping: Source → Skill Reference File

| Source / Guideline Cluster | Primary Skill File(s) Informed | Key Content Contributed |
|----------------------------|--------------------------------|--------------------------|
| NIH Format Attachments & Page Limits (grants.nih.gov) | `nih-grant-formatting.md` | Font, margin, density, line-spacing, Specific Aims / Research Strategy page limits |
| NIH font density measurement practice (NIAID + institutional guidance) | `nih-grant-formatting.md` (Font Density Calculation Methods) | 15 cpi / 6 lpi calculation methods, 112-character rule of thumb, Arial vs Georgia practical fixes |
| NIH Develop Your Budget + Modular Budget instructions | `nih-compliance-budgeting.md` (Sections 4, 11, 12) | Modular vs detailed rules, $250k ceiling, $25k modules, Personnel Justification requirements |
| NIH Salary Cap notices (NOT-OD-26-034 and related) | `nih-compliance-budgeting.md` (Section 7) | Current Executive Level II cap ($228,000), application to direct & indirect salaries |
| NIH Data Management & Sharing Policy + Budgeting guidance | `nih-compliance-budgeting.md` (Section 8) | Allowable / unallowable DMS costs, required “Data Management and Sharing Justification” label |
| NIH Multiple PD/PI Policy (GPS + NIAID guidance) | `nih-compliance-budgeting.md` (Section 9) | Leadership Plan requirements, Contact PI rules, no “co-PI” terminology |
| NIH Clinical Trial Dissemination Policy + ClinicalTrials.gov requirements | `nih-compliance-budgeting.md` (Section 10) | Registration & results reporting expectations, dissemination plan requirement |
| NOT-OD-26-019 (Dec 2025) – Removal of $500k prior-approval & LOI rules | `nih-compliance-budgeting.md` (Sections 4 & 11) | Elimination of formal ≥ $500k IC contact requirement |
| NCI, NINDS, NIAID funding strategy / policy pages | `nih-compliance-budgeting.md` (Sections 11 & 12) | IC-specific administrative reductions and Type-2 renewal caps |
| NIH multi-year / forward-funding policy discussions (AAMC, CRS, NIH budget materials) | `nih-compliance-budgeting.md` (Section 12) | Interaction of modular budgets with multi-year obligations |
| eRA Commons registration, roles, and account rules (era.nih.gov + GPS) | `nih-compliance-budgeting.md` (Section 13) | PI cannot self-register, one account per career, Commons ID requirements for senior/key personnel |
| eRA / ASSIST system-enforced validations & error/warning workflow | `nih-compliance-budgeting.md` (Sections 14, 17, 18, 20, 22) | Errors vs Warnings workflow, 2-day viewing window, high-frequency error codes, budget-mismatch remediation |
| NIAID “Avoid These Electronic Submission Errors” + eRA validation lists | `nih-compliance-budgeting.md` (Sections 14, 17, 18) | Top error codes (000.8, 000.10, 026.39.2, etc.) and concrete fix steps |
| NIH Single Audit / Uniform Guidance updates (NOT-OD-25-059, 2 CFR 200) | `nih-compliance-budgeting.md` (Sections 16, 19, 21) | $1 M domestic / $750 k foreign thresholds, SF-SAC, SEFA, CAP, Prior Approval Module mandate |
| NSF PAPPG 24-1 (especially Chapter II.C.2 and Budget Justification) | `nsf-proposal-formatting.md` | Font/margin rules, 1-inch margins, Project Summary structure, 15-page Project Description, 5-page Budget Justification |
| Mayo Clinic public COI in Research Policy PDF | `mayo-ospa-guidelines.md` | Disclosure thresholds, timing, Conflict of Interest Review Board role |
| SRA International presentation materials describing Mayo OSPA workflow | `mayo-ospa-guidelines.md` | Department vs OSPA roles, MIRIS usage, internal deadline concept, proposal workflow |
| Mayo Clinic Sponsored Project Specialist job descriptions (public) | `mayo-ospa-guidelines.md` | Confirmation of budget development support, MIRIS, pre- and post-award scope |
| Representative multi-agent grant platform architecture (studied diagram) | `agentic-ai-pi-solution-architecture.md` | Six-agent pipeline, tech stack pattern, compliance workflow stages, human-in-the-loop design |

---

## 2. Bibliography – Key Primary Sources

### NIH – Formatting, Font Density & Page Limits
- https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide/format-attachments  
- https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide/page-limits  
- https://www.niaid.nih.gov/grants-contracts/guidelines-font-i-use-my-application  
- Institutional practical guidance on measuring 15 characters/inch (e.g., Northwestern FSM document-setup notes)

### NIH – Budget, Modular, Salary Cap, $500k Rule
- https://grants.nih.gov/grants-process/write-application/advice-on-application-sections/develop-your-budget  
- https://grants.nih.gov/grants/how-to-apply-application-guide/forms-i/general/g.320-phs-398-modular-budget-form.htm  
- https://www.niaid.nih.gov/grants-contracts/when-modular-budget-right  
- https://www.niaid.nih.gov/grants-contracts/create-budget  
- https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-034.html (Salary Cap FY 2026)  
- https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-019.html (Removal of $500k prior-approval & LOI requirements)  
- https://www.grants.nih.gov/policy-and-compliance/policy-topics/nih-fiscal-policies/salary-cap-summary  

### NIH – Data Management & Sharing
- https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/budgeting-for-data-management-sharing  

### NIH – Multi-PI & Clinical Trials
- https://grants.nih.gov/grants-process/plan-to-apply/consider-your-idea-resources-and-collaborators/multiple-principal-investigators  
- https://grants.nih.gov/policy-and-compliance/policy-topics/clinical-trials/reporting  

### NIH – IC Funding Policies & Multi-Year Funding
- https://www.cancer.gov/grants-training/grants-funding/funding-strategy/current-funding-policy (NCI)  
- https://www.ninds.nih.gov/funding/determining-your-funding-likelihood/ninds-funding-strategy (NINDS)  
- https://www.niaid.nih.gov/grants-contracts/calculate-your-renewal-budget-cap (NIAID renewal cap)  
- AAMC analyses of NIH multi-year / forward funding  
- Congressional Research Service summaries of NIH funding policy changes  

### eRA Commons, ASSIST Validations & Error Codes
- https://www.era.nih.gov/erahelp/commons/ (roles, account creation)  
- https://grants.nih.gov/grants/policy/nihgps/html5/section_2/2.2.1_era_commons_registration.htm  
- https://www.era.nih.gov/applicants/system/validations.htm  
- https://www.niaid.nih.gov/grants-contracts/avoid-these-electronic-applicationsubmission-errors (top error list)  
- https://www.era.nih.gov/erahelp/assist/ (ASSIST validation & submission help)  

### NIH – Single Audit & Prior Approval
- https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-059.html (Uniform Guidance implementation, audit threshold)  
- https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-026.html (eRA Prior Approval Module mandate)  
- 2 CFR 200 Subpart F (Single Audit)  

### NSF
- https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation (PAPPG 24-1, Chapter II)  
- https://www.nsf.gov/policies/pappg  

### Mayo Clinic OSPA / Institutional
- https://www.mayoclinic.org/content/dam/media/global/documents/policies/conflict-of-interest/conflict-of-interest-in-research-policy.pdf  
- SRA International presentation materials describing Mayo Clinic OSPA workflow, MIRIS, and internal process  
- Public Mayo Clinic Sponsored Project Specialist role descriptions  

### Architecture Pattern
- Representative multi-agent OSPA-aligned grant submission platform architecture (studied for agentic-AI reference; not stored as an asset)

---

## 3. How to Maintain This File

When updating any of the following skill files:

- `nih-grant-formatting.md`
- `nih-compliance-budgeting.md`
- `nsf-proposal-formatting.md`
- `mayo-ospa-guidelines.md`
- `agentic-ai-pi-solution-architecture.md`

…add or update the corresponding row in the mapping table above and append new primary URLs to the bibliography section. Prefer official `.gov` or institutional policy PDFs over secondary summaries.

This keeps the skill’s knowledge base auditable and makes it easier to refresh content when NIH, NSF, or institutional offices publish new notices.
