# NIH Compliance, Budgeting, Registration & Submission Guidelines

Core reference for decks and recommendations about preparing NIH grant proposals (especially R01, R03, R21 and related activity codes). Focus is on **must-have / must-not-have** rules for proposal preparation, budgeting, investigator registration, and electronic submission.

**Always defer to the specific Notice of Funding Opportunity (NOFO).** General rules below are the baseline.

## 1. Investigator & Institutional Registration (Must-Have Before Submission)

### Institutional Level
- The applicant organization **must** be registered in **eRA Commons**.
- Registration is performed by a Signing Official (SO) who has legal authority to bind the organization.
- Organization must also have an active **UEI** (Unique Entity Identifier) from SAM.gov at the time of submission.

### Individual Level (PIs and Key Personnel)
- **Every PD/PI** must have an eRA Commons account with the **PI role** and be affiliated with the applicant organization.
- **PIs cannot create their own account.** The institutional SO or Account Administrator (AA) must create it.
- All Senior/Key Personnel and Other Significant Contributors listed on the application **must** have active eRA Commons IDs (entered in the Credential field).
- Individuals with Undergraduate, Graduate Student, or Postdoctoral roles who will participate ≥ 1 person-month must also have eRA Commons IDs (required for progress reporting).
- **ORCID iD** is required for all senior/key personnel (linked in the personal profile / Common Forms).

**Practical implication for agentic tools:** Any grant-support system should check or guide users on eRA Commons affiliation status and ORCID linkage before allowing proposal generation.

## 2. Submission Portals & Process

NIH applications are submitted electronically. Common paths:

| Method | Description | Notes |
|--------|-------------|-------|
| **ASSIST** (preferred by many) | NIH’s web-based system for preparing, validating, and submitting applications | Uses eRA Commons login. Strong pre-submission validation. Supports single- and multi-project applications. Routes through Grants.gov. |
| **Grants.gov Workspace** | Alternative preparation/submission route | Does **not** support complex multi-project applications as well as ASSIST. |
| **System-to-System** | Institution’s own solution that talks to Grants.gov | Often preferred by large universities for internal workflow integration. |

**Key process facts:**
- Final submission still goes through Grants.gov, then lands in eRA Commons for tracking and review.
- Applications must be error-free and validated by both Grants.gov **and** eRA Commons by 11:59 p.m. ET on the due date.
- Submit 24–72 hours early to allow time to correct errors and resubmit.
- ASSIST provides the best pre-submission NIH business-rule checking.

## 3. Common Activity Codes – Quick Comparison (R01 / R03 / R21)

| Feature | R01 (Research Project) | R03 (Small Grant) | R21 (Exploratory/Developmental) |
|---------|------------------------|-------------------|---------------------------------|
| Typical duration | Up to 5 years | Up to 2 years | Up to 2 years |
| Direct cost guidance | No statutory limit (must be appropriate) | ≤ $50k per year; ≤ $100k total | ≤ $275k total over 2 years; ≤ $200k in any single year |
| Research Strategy page limit | 12 pages | 6 pages | 6 pages |
| Specific Aims | 1 page | 1 page | 1 page |
| Preliminary data | Expected / strongly preferred | Not required | Not required |
| Renewable | Yes | No | No |
| Modular budget eligible | Yes (if ≤ $250k direct/year) | Yes | Yes |

## 4. Budget Rules – Modular vs Detailed (Deep Dive on Modular Limits)

### Core Modular Budget Limit
- **Hard ceiling**: ≤ **$250,000 in direct costs per budget period** (year).
- The $250,000 limit **excludes consortium (subaward) F&A / indirect costs**. Only the applicant organization’s direct costs + the direct-cost portion of any consortium count toward the cap.
- Requests are made in **modules of $25,000** (i.e., maximum of 10 modules per year).
- **No automatic future-year escalations**. Request the same number of modules each year unless the science genuinely requires variation (then justify the variation).

### When the Modular Form (PHS 398 Modular Budget) **Must** Be Used
All of the following must be true:
- Applicant is a **U.S. (domestic) organization**
- Requesting ≤ $250,000 direct costs per year (excluding consortium F&A)
- Activity code is one of the eligible mechanisms (or their cooperative-agreement equivalents):
  - R01 / U01
  - R03
  - R15
  - R21 / UH2
  - R34 / U34
- Application is new, renewal, resubmission, or revision
- The specific NOFO does **not** override and require a detailed budget

### When Modular Is **Not** Allowed / Detailed R&R Budget Is Required
- Direct costs > $250,000 in **any** budget period
- Foreign (non-U.S.) applicant institution (even if under $250k)
- SBIR / STTR applications
- NOFO explicitly requires a detailed budget
- - **Note on ≥ $500k**: As of Dec 3, 2025 (NOT-OD-26-019), the prior IC contact/approval requirement for ≥ $500k direct costs has been eliminated. See Section 11 for details.

### Modular Budget Justification Requirements (Still Mandatory)
Even though dollar details are not itemized, three attachments are typically required:

1. **Personnel Justification**  
   - List **every** person (not only senior/key) by name, role, and person-months (or percent effort).  
   - **Do not** include salary or fringe dollar amounts.  
   - Use the current NIH salary cap when estimating how many modules are needed.

2. **Consortium Justification** (if any subawards)  
   - Total costs (direct + F&A) for each consortium, rounded to nearest $1,000.  
   - Indicate whether each collaborating organization is foreign or domestic.  
   - List personnel roles and person-months on the consortium.

3. **Additional Narrative Justification**  
   - Required when the number of modules varies across years.  
   - Also used for Data Management & Sharing costs, equipment, tuition remission, off-site work, or any other costs that need explanation.

### Practical Notes
- A typical modular application requests the **same number of modules** every year.
- NIH may request a full detailed budget later (Just-in-Time) in exceptional cases.
- Reviewers see far less budget detail on modular applications, which often results in fewer recommended cuts than on large detailed budgets.
- New investigators are frequently advised to stay within modular limits unless the science clearly requires more.

**Agentic AI implication**: Automatically detect eligible activity codes + requested amount, force the modular form when appropriate, calculate modules in $25k increments (after subtracting consortium F&A), enforce the Personnel Justification format (no salaries), and flag any year-to-year module variation for additional justification.

## 5. Must-Have / Must-Not-Have Budget Rules (High-Level)

### Must-Have / Strongly Expected
- Costs that are **allowable, allocable, reasonable, necessary, and consistently treated**.
- Personnel effort justified with person-months.
- Equipment listed individually when using detailed budget and justified as necessary for the project.
- Data Management and Sharing costs addressed (either in budget or explicitly stated as $0 with justification).
- Compliance with the current NIH salary cap (when calculating modular modules or detailed salaries).

### Must-Not-Have / Common Unallowable or High-Risk Items
- Entertainment, lobbying, most general-purpose office equipment as direct costs.
- Voluntary committed cost sharing (unless the NOFO requires it).
- Charging administrative/clerical salaries as direct costs unless the strict 2 CFR 200.413 criteria are met and approved.
- Inflated or “padded” budgets — reviewers notice and frequently recommend cuts.
- Requesting senior personnel salary without corresponding person-months (or vice versa).

**Note on salary:** NIH has a legislatively mandated salary cap. Modular budgets should be calculated using the current cap.

## 6. Other Critical Compliance Points for Proposal Preparation

- **Page limits** are strictly enforced (Specific Aims = 1 page; Research Strategy = 12 pages for most R01s, 6 pages for R03/R21). Exceeding them can cause the application to be withdrawn.
- Font, margin, and density rules (see `nih-grant-formatting.md`) are enforced; non-compliant applications may be withdrawn before review.
- Biosketches and Current & Pending (Other) Support must use the required format (Common Forms / SciENcv for due dates on or after January 25, 2026).
- All senior/key personnel must have ORCID iDs linked.
- Clinical trial applications have additional registration and dissemination plan requirements.

## 7. Salary Cap Details (Current)

- **Legislative mandate**: Congress limits the amount of salary that can be charged to NIH grants to Executive Level II of the Federal Executive Pay Scale.
- **Current cap** (effective January 1 / 11, 2026): **$228,000**.
- Applies to **both direct salaries** (individuals working on the project) and, for awards issued on or after October 1, 2024, certain **indirect salaries**.
- Institutions may pay individuals above the cap from non-federal funds; the difference cannot be charged to the NIH award.
- Modular budgets should be calculated using the current salary cap when determining the number of modules.
- Active awards may rebudget (if funds are available and consistent with institutional base salary) to accommodate the new cap.
- Recipients must have consistent institutional policies regardless of funding source.

**Agentic AI implication**: Always surface the current Executive Level II amount and warn when requested effort would imply a salary above the cap.

## 8. Data Management and Sharing (DMS) Costs

NIH expects applicants to maximize appropriate data sharing. Reasonable, allowable costs for DMS activities may be requested.

**Allowable costs** (must be incurred during the performance period):
- Curating data and developing supporting documentation
- Formatting data to community standards or for repository deposit
- De-identifying data
- Preparing metadata for discoverability and reuse
- Local specialized data management infrastructure (before repository deposit)
- Repository deposit / long-term preservation fees (including multiple repositories if proposed)

**Not allowable**:
- Infrastructure costs already included in institutional F&A / overhead
- Costs of routine research conduct or collecting/gaining access to data

**Budget presentation**:
- Request costs in the appropriate budget category (personnel, other direct costs, etc.).
- In the Budget Justification, include a clearly labeled section: **“Data Management and Sharing Justification”** followed by the estimated dollar amount.
- Even if DMS costs are $0, it is good practice to state that explicitly and justify why.

**Agentic AI implication**: Prompt users for DMS activities, estimate associated costs, and auto-generate the required labeled justification paragraph.

## 9. Multiple PD/PI (Multi-PI) Rules

- Allowed when scientifically justified; the decision rests with the applicant organization and the investigators.
- All designated PD/PIs share responsibility and authority for the project.
- One PD/PI must be designated as the **Contact PI** (primary communication point with NIH). The Contact PI must be affiliated with the submitting institution.
- NIH does **not** use the term “co-PI.”
- **Required attachment**: Multiple PD/PI Leadership Plan. It must address:
  - Rationale for choosing the multi-PI approach
  - Roles and responsibilities of each PD/PI
  - Governance and organizational structure
  - Communication plans
  - Process for scientific decision-making and resource allocation
  - Conflict resolution procedures
- All PD/PIs must have eRA Commons accounts with the PI role.
- Changing from single-PI to multi-PI (or vice versa) after award requires prior NIH approval.

**Agentic AI implication**: When more than one PI is detected, require and scaffold a complete Leadership Plan covering all mandated elements.

## 10. Clinical Trial–Specific Compliance

For applications that propose clinical trials (in whole or in part funded by NIH):

- **NIH Policy on Dissemination of NIH-Funded Clinical Trial Information** applies (effective for applications submitted on or after January 18, 2017).
- All NIH-funded clinical trials are expected to:
  - Register on **ClinicalTrials.gov**
  - Submit summary results information to ClinicalTrials.gov according to required timelines
- Applicants must submit a plan describing how they will meet these dissemination expectations.
- The Authorized Organization Representative’s signature certifies compliance with the dissemination plan.
- Separate from (and broader than) the FDAAA 801 / 42 CFR Part 11 “applicable clinical trial” requirements. NIH policy covers trials of any intervention type funded by NIH.
- Non-compliance can lead to funding actions by NIH in addition to any FDA civil penalties (where applicable).
- Progress reports (RPPR) include validations related to registration and results reporting.

**Agentic AI implication**: Detect clinical-trial applications early, require a dissemination plan section, and surface ClinicalTrials.gov registration and results-reporting timelines.

## Practical Implications for Agentic AI / PI Support Systems

A high-value agentic system for Principal Investigators should:
- Check eRA Commons affiliation and ORCID status early.
- Guide the user to the correct budget form (modular vs detailed) based on activity code and requested amount.
- Enforce page limits and formatting rules in real time.
- Generate compliant Personnel Justification even for modular budgets.
- Flag requests ≥ $500k direct costs (require prior NIH contact).
- Surface the current salary cap and F&A implications.
- Support export to ASSIST-compatible or Grants.gov-ready packages.
- Distinguish clearly between R01 vs R03 vs R21 constraints (duration, page limits, preliminary data expectations, renewability).

## Sources
- eRA Commons registration: grants.nih.gov and era.nih.gov
- Budget development: grants.nih.gov → Develop Your Budget
- Page limits table: grants.nih.gov → Page Limits
- Modular budget guidance: NIAID and NIH application guides
- Always cross-check the specific NOFO and the current SF424 Application Guide.

## 11. NIH R01 Budget Guidelines (Specific)

The R01 is NIH’s flagship research project grant. Budget rules combine the general modular/detailed framework with R01-specific expectations.

### Key Characteristics of R01 Budgets
- **No statutory dollar limit** on direct costs (unlike R03 or R21). The budget must be appropriate to the science.
- Typical funded R01-equivalent awards in recent years average roughly $600k–$665k total costs (direct + F&A). Many successful applications request $250k–$500k direct costs per year.
- Project period: up to 5 years.
- Modular option remains available if ≤ $250k direct costs/year (excluding consortium F&A).

### Modular vs Detailed for R01
- ≤ $250k direct/year → modular form allowed (and required for domestic institutions unless NOFO says otherwise).
- > $250k direct/year → detailed R&R Budget Form required.
- ≥ $500k direct costs in any year → traditionally required prior contact with the IC program official (check current NOFO/policy; some recent guidance has relaxed the formal pre-approval step, but consultation is still strongly advised).

### Personnel (Largest Cost Category)
- Typically ~70–80% of an R01 budget.
- PI effort: Early-stage / new investigators are often expected to commit meaningful effort (commonly ≥ 2.5–3 calendar months / ~25% on a single R01). Reviewers question both under-commitment and over-commitment.
- All senior/key personnel must show measurable person-months.
- Use current salary cap ($228,000 as of early 2026) when calculating allowable salary charges.
- Administrative/clerical salaries as direct costs only if the strict 2 CFR 200.413 criteria are met and justified.

### Equipment
- Defined as items ≥ $5,000 (or institutional capitalization threshold) with useful life > 1 year.
- Must be listed individually on detailed budgets and justified as necessary and not already available.
- General-purpose equipment is usually not allowable as a direct cost.
- On modular budgets, equipment is not itemized but must still be supportable within the requested modules.

### Travel
- Must be project-specific (presenting results, essential collaboration, data collection).
- Justify destination, number of travelers, duration, and scientific necessity.
- Foreign travel requires extra justification.
- Typical R01 travel budgets are modest ($5k–$15k/year); larger amounts attract scrutiny.

### Other Common R01 Budget Elements
- Supplies, animal costs, patient-care costs, consultants, consortium/subawards, publication costs, Data Management & Sharing costs.
- Graduate student tuition remission is often excluded from the F&A base.
- F&A (indirect) costs are calculated on the institution’s negotiated rate applied to the appropriate base (usually Modified Total Direct Costs).

### Renewal (Type 2) Budget Caps – Important Nuances
- **IC-specific**: Many Institutes apply their own renewal (Type 2) budget caps. 
  - **NIAID example**: Caps renewals at 20% above the direct costs of the last competing segment (after subtracting supplements, equipment, alterations/renovations, and subaward F&A). Formula: (prior final-year direct costs – adjustments) × 1.20.
  - Other ICs (NCI, etc.) publish annual funding policy statements with their own Type-2 caps and across-the-board reductions for new awards.
- Submitting a “new” (Type 1) application instead of a renewal to avoid a cap is possible but generally has a lower success rate.
- Always check the target IC’s current funding policy page before finalizing a renewal budget.

### Reviewer & Program Officer Expectations
- Budget must match the proposed scope and aims.
- Inflated budgets are frequently cut; under-budgeted applications raise feasibility concerns.
- New investigators are often advised to stay modular unless the science clearly demands more.
- Justifications must be specific — vague statements (“travel to conferences,” “personnel as needed”) are red flags.

**Agentic AI implication for R01 support**:  
- Auto-detect whether modular or detailed is required.  
- Surface current salary cap and typical effort expectations for the PI career stage.  
- Flag requests approaching or exceeding $500k direct costs.  
- Scaffold strong, specific justifications for personnel, equipment, and travel.  
- For renewals, prompt for previous award amounts to calculate IC-specific caps.

## 12. Modular Budgets, Multi-Year Funding & IC-Specific Reductions

### Multi-Year (Forward) Funding Policy and Modular Budgets

**What changed**  
Starting in FY 2025 and accelerating in FY 2026, NIH significantly increased the use of **multi-year funding** (also called forward funding). Instead of obligating only Year 1 and committing out-years, NIH fully funds the entire project period upfront from the current fiscal year’s appropriation.

**Interaction with modular budgets**  
- Modular applications are fully compatible with multi-year funding.  
- When an R01 (or other modular-eligible mechanism) is selected for multi-year funding, the entire multi-year modular total is obligated at once.  
- Because a 4- or 5-year modular R01 consumes 4–5× the Year-1 dollars of a traditionally funded award, each multi-year modular award reduces the number of new awards NIH can make in that fiscal year.  
- In FY 2026, a notable share of multi-year RPG awards have been R21s, but R01s are also increasingly included.  
- Congress limited FY 2026 multi-year funding volume to FY 2025 levels, creating ongoing uncertainty about the pace of the shift.

**Practical impact for applicants**  
- Success rates have declined in part because fewer awards can be made when large multi-year obligations are used.  
- Modular budgets remain advantageous for many applicants (simpler preparation, often fewer reviewer cuts), but the overall funding environment is tighter.  
- Institutions must plan cash-flow and laboratory continuity carefully when receiving large multi-year modular awards.

### IC-Specific Funding Reductions (Examples)

Institutes apply their own administrative reductions and Type-2 caps after peer review. These are independent of the modular vs detailed choice but interact with it.

**NCI (illustrative recent policy)**  
- Modular R01/U01 new applications:  
  - ≤ $175k direct costs → generally ~6.5% reduction from IRG recommended level  
  - > $175k direct costs → generally ~8.5% reduction  
- Non-modular (categorical) new R01s → generally ~17% reduction  
- Competing renewals (Type 2) → funded at NCI’s Type-2 cap with no additional policy reduction  

**NINDS (illustrative)**  
- Modular R01 → 0% administrative cut  
- Non-modular R01 → 20.5% administrative cut  
- R03, R21, R15, R34 → 0%  

**NIAID**  
- Applies a 20% renewal (Type 2) cap calculated on prior competing-segment direct costs (after adjustments).  
- Has at times applied additional across-the-board reductions to competing awards.

**General pattern**  
- Modular applications frequently receive milder (or zero) administrative cuts compared with large non-modular budgets at several ICs.  
- New (Type 1) applications are cut more aggressively than renewals at many ICs.  
- Always check the target IC’s current “Funding Policy” or “Funding Strategy” page, as these numbers change with the fiscal-year budget outlook.

**Agentic AI implication**  
- When generating R01 budget advice, surface both the modular/detailed decision and the likelihood of IC-specific post-review reductions.  
- For multi-year funding scenarios, note that a modular award may lock in the full multi-year total at once, affecting institutional planning.  
- Prompt users to consult the specific IC’s latest funding policy statement before finalizing requested modules or detailed budgets.

## 13. eRA Commons System Rules (Key Operational Requirements)

 eRA Commons is the mandatory system for NIH account management, application tracking, and (via ASSIST) many submissions. The following rules are frequently relevant to PI support tools and OSPA-mediated workflows.

### Account Creation & Roles
- **PIs cannot self-register.** Only institutional officials with SO, AA, AO, or BO roles can create accounts.
- Every PD/PI must have an eRA Commons account with the **PI role** and be affiliated with the applicant organization.
- A scientific user (PI, trainee, etc.) should have **only one** eRA Commons account for their entire career. Duplicate accounts must be consolidated via the eRA Service Desk.
- All Senior/Key Personnel and Other Significant Contributors listed on an application **must** have active eRA Commons usernames (entered in the Credential field).
- ORCID iD linkage is required for senior/key personnel (Common Forms era).

### Submission & Validation Rules (ASSIST / eRA)
- Applications must be **error-free** before they can move to “Ready for Submission.”
- **Errors** block submission; **Warnings** do not, but should still be reviewed.
- Common high-frequency validation errors (recent data):
  - PDF attachment problems (encryption, password protection, missing metadata, non-flattened fillable forms, file > 6 MB, wrong page size).
  - All attachments must be PDF.
  - Missing or invalid Commons ID in the Credential / Applicant Identifier field.
  - Budget total mismatches.
  - Missing required attachments (e.g., DMS Plan when flagged as required).
- After submission there is a **2-business-day application viewing window** in which the applicant can reject the assembled application if problems are found.
- Final submission still routes through Grants.gov; status is tracked in eRA Commons.

### Practical Implications for Agentic / OSPA Tools
- Always verify that every named senior/key person has a valid, affiliated Commons ID before package finalization.
- Pre-flight PDF checks (flattened, unencrypted, ≤ 6 MB, correct page size, no live hyperlinks in restricted sections) prevent the most common rejection reasons.
- Surface the institutional internal deadline and the need for OSPA (or equivalent) to perform the official submission.
- After submission, remind users of the 2-day viewing window.

## 14. eRA / ASSIST Validation Workflow (Errors & Warnings “Comments”)

When an application is validated in ASSIST (or after Grants.gov routes it to eRA), the system produces a structured list of **Errors** and **Warnings**. These function as the system’s “comments” on the package.

### Workflow Steps
1. User (or OSPA) runs **Validate Application** (or validation is triggered automatically on status change).
2. ASSIST / eRA checks the package against hundreds of system-enforced business rules (a subset of all Application Guide + NOFO rules).
3. Results appear on the **Application Errors and Warnings Results** page:
   - **Errors** (blocking) — must be fixed before the application can be marked “Ready for Submission” or accepted.
   - **Warnings** (non-blocking) — do not stop submission, but should be reviewed; many are still serious compliance issues.
4. Applicant corrects the problems, re-validates, and repeats until zero Errors remain.
5. After successful submission there is a **2-business-day application viewing window** during which the assembled application can still be rejected if problems are spotted.

**Important design note for agentic systems**: Pre-flight the same checks that eRA will run (especially PDF integrity, Commons IDs, and budget totals) so the PI/OSPA never discovers blocking errors at the last minute.

### Most Frequent Validation Failures (recent data)
- PDF issues (encryption, password protection, missing metadata, non-flattened forms, file > 6 MB) — by far the largest category.
- Attachment not in PDF format.
- Budget section total mismatches (see examples below).
- Missing or inactive Commons ID in the Credential field.
- Missing required attachments (e.g., DMS Plan when the opportunity flags it as required).

## 15. Specific Budget Mismatch Examples (Common eRA Errors)

These are real, high-frequency validation failures:

| Rule / Error Pattern | What It Means | Typical Cause |
|----------------------|---------------|---------------|
| **026.39.2** | Totals (Section B, row K, column 1) ≠ Total (Section A, row 1, column g) | Personnel or other category totals on the detailed budget form do not add up to the summary total. |
| **026.67.1 / 026.30.1 / 026.46.2** | Order or text of Grant Program / Function / Activity in Sections B/C/E does not match Budget Summary Section A | Copy-paste or re-ordering errors between budget forms; activity titles must be identical and in the same order. |
| Modular vs Detailed mismatch | System expects one form type but receives the other | Requesting > $250k direct costs while still using the modular form, or vice-versa. |
| Consortium F&A handling | Consortium indirects incorrectly included in (or excluded from) the modular $250k ceiling calculation | Applicant counted subaward F&A against the modular limit (they are excluded). |
| Salary-cap line items | Requested salary exceeds current Executive Level II cap without proper institutional base-salary documentation | Detailed budget shows a salary above $228,000 (2026 cap) for effort charged to the grant. |

**Agentic implication**: A Compliance or Readiness Agent should recompute all budget category totals and cross-check them against the summary lines before the package ever reaches ASSIST validation.

## 16. NIH Audit Integration Requirements (Single Audit)

NIH recipients are subject to the Single Audit requirements under 2 CFR 200 Subpart F (Uniform Guidance).

### Current Thresholds (as of FY 2025–2026 updates)
- **Domestic non-profit / higher-education / state & local government recipients**: Single Audit (or program-specific audit) required when **federal expenditures ≥ $1,000,000** in the recipient’s fiscal year (threshold raised from the previous $750,000).
- **Foreign recipients**: Still required at the **$750,000** threshold (NIH-specific retention of the lower threshold).
- For-profit and certain other entities follow the rules in 45 CFR 75.501.

### Key Points for Grant Support Systems
- The audit is an **institutional** post-award obligation, not a proposal-stage validation.
- However, proposal and award systems should surface the existence of the requirement so that PIs and research administrators understand ongoing compliance obligations.
- NIH now requires (effective recent notices) that **all prior-approval requests** be submitted through the eRA Commons Prior Approval Module (initiated by the Signing Official).
- Subaward agreements must include certification language that information submitted by subrecipients is complete and accurate (2 CFR 200.415 updates).

**Agentic / OSPA implication**: The platform should not attempt to perform the Single Audit itself, but it can:
- Flag when an institution is approaching the expenditure threshold.
- Ensure prior-approval actions route through the correct eRA module.
- Maintain clean audit trails of all automated findings and human overrides (useful for both internal compliance and external audit readiness).

## 17. Common eRA Validation Error Codes – Quick Reference Table

| Error / Rule Code | Category | Severity | What It Means | Typical Fix |
|-------------------|----------|----------|---------------|-------------|
| **000.8** | Attachment | Error | Attachment is not in PDF format | Convert every attachment to flattened PDF |
| **000.10** | Attachment | Error | PDF is encrypted, password-protected, has missing metadata, is secured, or is corrupt | Re-export as flattened, unprotected PDF; remove security settings |
| **000.6** | Schema / Form | Error | XML/schema mismatch (often budget form version or unexpected element) | Ensure correct forms package version for the NOFO; re-build budget forms |
| **005.48.11** | Commons ID | Warning | Person listed lacks an active Commons ID in the Credential field | Obtain / activate Commons ID and enter it correctly |
| **025.6.1 / 025.6.2** | Commons ID | Error | Applicant Identifier missing or not a valid Commons account | Enter the PD/PI’s valid Commons username |
| **026.39.2** | Budget Total | Error | Section B totals (row K) do not equal Section A summary total | Re-add all category totals; correct arithmetic or missing line items |
| **026.30.1 / 026.46.2 / 026.67.1** | Budget Activity | Error | Grant Program / Function / Activity text or order in Sections B/C/E does not match Section A | Make activity titles identical and in the same sequence across all budget sections |
| **010.17** | DMS Plan | Error / Warning | DMS Plan attachment required by the opportunity but missing | Attach a compliant Data Management and Sharing Plan |
| File size / page size | Attachment | Error | PDF > 6 MB or not 8.5" × 11" | Compress or split files; enforce US Letter page size |
| Hyperlinks / bookmarks | Attachment | Error | Live hyperlinks or bookmarks present in restricted attachments | Remove live links; use plain-text URLs only where allowed |

**Note**: Exact rule numbers can evolve; always treat the human-readable message as authoritative. The codes above are the high-frequency ones observed in recent eRA data.

## 18. How to Fix the Most Common Budget Mismatch Errors

### Error 026.39.2 – Section Totals Do Not Match
**Root cause**: Arithmetic error or omitted line item when rolling detailed categories up to the summary.
**Fix steps**:
1. Open the detailed budget form(s).
2. Manually sum every category in Section B (or the equivalent detailed section).
3. Compare with the value shown in Section A / Budget Summary total.
4. Correct the differing line(s) and re-validate.
5. In modular applications, confirm that consortium F&A was **excluded** from the direct-cost modules.

### Activity Title / Order Mismatches (026.30.1, 026.46.2, 026.67.1)
**Root cause**: Copy-paste drift or re-ordering of “Grant Program, Function or Activity” rows.
**Fix steps**:
1. Copy the exact activity title string from Section A.
2. Paste it into the corresponding rows of Sections B, C, and E (or equivalent).
3. Ensure the **order** of activities is identical across sections.
4. Re-validate.

### Modular vs Detailed Form Mismatch
**Fix**: 
- If direct costs (excluding consortium F&A) ≤ $250k per year **and** the activity code is modular-eligible → use PHS 398 Modular Budget form only.
- If any year exceeds $250k → switch to the detailed R&R Budget form and supply full justifications.

### Salary-Cap Related Mismatches
**Fix**:
- Cap any individual’s requested salary at the current Executive Level II amount ($228,000 as of early 2026) for the effort charged to the grant.
- Institutional base salary may be higher; the difference cannot be charged to the NIH award.
- On modular budgets, use the capped amount when calculating how many modules are needed.

**Agentic recommendation**: Recompute all totals programmatically and surface a side-by-side “calculated vs entered” comparison before the package reaches ASSIST.

## 19. Single Audit – Reporting Forms & Practical Requirements (Enriched)

### When the Single Audit Is Triggered
| Recipient Type | Expenditure Threshold (recipient’s fiscal year) | Audit Type |
|----------------|--------------------------------------------------|------------|
| Domestic non-profit, higher-education, state/local government | ≥ **$1,000,000** in federal awards | Single Audit (2 CFR 200 Subpart F) or program-specific audit (with prior approval) |
| Foreign recipients | ≥ **$750,000** | Single Audit or program-specific audit (NIH retains lower threshold) |
| For-profit entities | Follow 45 CFR 75.501 | Financial-related audit or other acceptable options |

### Key Reporting / Submission Artifacts
- **Data Collection Form (SF-SAC)** – submitted to the Federal Audit Clearinghouse (FAC).
- **Single Audit Report package** – financial statements, Schedule of Expenditures of Federal Awards (SEFA), auditor’s opinions, internal-control findings, and corrective-action plan.
- **Management decision letters** – issued by NIH (or pass-through entity) on audit findings.
- **Corrective Action Plan (CAP)** – required when findings exist; tracked until resolved.

### Integration Points Relevant to Grant Systems
- Prior-approval actions (carryover, change of PI, no-cost extension, DMS changes, etc.) must be submitted via the **eRA Commons Prior Approval Module** (SO-initiated).
- Subaward agreements must contain the certification language required by 2 CFR 200.415 (information submitted by subrecipients is complete and accurate).
- Institutions should retain documentation that supports the SEFA (which awards, CFDA/Assistance Listing numbers, expenditures) — clean proposal and award data from systems such as MIRIS / eRA help produce a defensible SEFA.
- Agentic platforms should maintain immutable audit logs of every automated compliance finding and every human override; these logs become useful evidence during both internal reviews and external Single Audits.

### What the Platform Should **Not** Try to Do
- Perform the Single Audit itself.
- Replace the institutional auditor or the Federal Audit Clearinghouse submission.
- Automatically “clear” audit findings.

Its value is in **preventing** findings (through strong pre-award and post-award controls) and in supplying clean, auditable data trails.

## 20. ASSIST Validation Workflow – Detailed Steps

### Single-Project Applications
1. Optional but strongly recommended: run **Validate Application** from the Actions panel at any time while editing.
2. Correct all **Errors** (Warnings are non-blocking but should still be reviewed).
3. When ready, the Signing Official (AOR) sets status to **Ready for Submission** and submits.
4. Application routes through Grants.gov → eRA; status becomes **Submitted**.
5. 2-business-day application viewing window opens; applicant can reject if problems are found in the assembled image.

### Multi-Project Applications (more structured status machine)
| Status | Meaning | Who / What Sets It |
|--------|---------|---------------------|
| Work in Progress | Editing allowed | Default / manual |
| All Components Final | Every component is Final (or Abandoned) | Manual – prerequisite for full validation |
| All Components Validated | Validate Application ran with zero Errors | System-generated |
| Ready for Submission | Internal reviews complete; ready for AOR | Manual (usually SO / AOR) |
| Submitted | Successfully sent to Grants.gov | System-generated |
| Submission Errors | Post-submission or validation failures | System-generated |
| Abandoned | Component or application no longer being worked | Manual |

**Key multi-project rules**
- Validate Application can be run only when status is **All Components Final**.
- Only a Signing Official of the applicant lead organization can perform the final Submit.
- Components in Abandoned status are skipped by validation.
- Access control is granular: Entire Application Editor vs Component Editor (Budget / Non-Budget).

**Agentic implication**: Mirror this status machine in the Readiness / Submission agents so the platform can tell a PI or OSPA specialist exactly which gate is still open.

## 21. Single Audit Thresholds – Expanded Detail

| Recipient Category | Federal Expenditure Threshold (recipient’s fiscal year) | Audit Required | Where Reports Go |
|--------------------|----------------------------------------------------------|----------------|------------------|
| Domestic non-profit, higher-education, state & local government | ≥ **$1,000,000** | Single Audit (2 CFR 200 Subpart F) or program-specific audit (with prior written approval) | Federal Audit Clearinghouse (FAC) |
| Foreign recipients | ≥ **$750,000** (NIH retains the lower threshold) | Single Audit or program-specific audit | NIH Audit Resolution / as directed |
| For-profit entities | Per 45 CFR 75.501 | Financial-related audit or other acceptable options | As specified |

**Important timing note**: The $1 M threshold for domestic entities became effective for fiscal years beginning on or after October 1, 2024 (OMB 2024 Uniform Guidance revision). NIH has incorporated this into the Grants Policy Statement while retaining the $750 k floor for foreign recipients.

**Related recent requirements**
- All prior-approval requests must be submitted through the **eRA Commons Prior Approval Module** (SO-initiated).
- Subaward agreements must include the 2 CFR 200.415 certification language.
- Clean SEFA production depends on accurate award and expenditure data from institutional systems (MIRIS, etc.).

## 22. Additional Specific Error-Code Examples (Expanded)

| Code | Message Pattern (paraphrased) | Why It Happens | Concrete Fix |
|------|-------------------------------|----------------|--------------|
| 000.8 | All attachments must be in PDF format | DOCX, DOC, or other format uploaded | Convert every file to PDF |
| 000.10 | PDF has metadata missing / encrypted / password-protected / secured / PDF error | Security settings left on, or corrupt export | Re-export as flattened, unprotected PDF; remove passwords and certificates |
| 026.39.2 | Section B total (row K) ≠ Section A summary total | Arithmetic error or omitted line | Re-sum every category; correct the differing line |
| 026.30.1 / 026.46.2 / 026.67.1 | Activity title or order in Sections B/C/E does not match Section A | Copy-paste drift or re-ordering | Copy exact title string and sequence from Section A into the other sections |
| 005.48.11 | Person lacks active Commons ID in Credential field | Missing or inactive Commons username | Obtain/activate ID and enter it |
| 025.6.1 / 025.6.2 | Applicant Identifier missing or invalid | Blank or wrong Commons username for PD/PI | Enter the correct, active Commons ID |
| 010.17 | DMS Plan required but missing | Opportunity flagged DMS as required | Attach compliant Data Management and Sharing Plan |
| File-size / page-size errors | Attachment > 6 MB or not 8.5" × 11" | Large image-heavy PDFs or wrong paper size | Compress or split; enforce US Letter |
| Hyperlink / bookmark errors | Live hyperlinks or bookmarks present | Word/PDF retained active links | Remove live links; use plain-text URLs only where permitted |

These examples should be used by a Compliance or Readiness Agent to give precise, actionable feedback rather than generic “budget error” messages.
