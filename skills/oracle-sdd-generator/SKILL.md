# Oracle SDD Generator

> **Purpose:** Generate structured Solution Design Documents for OCI-based customer solutions.
> **Confidentiality:** Uses codenames only. No client names, no industry details in output files.

## When to Use This Skill

Invoke when the user needs:
- A formal Solution Design Document (SDD) for a customer engagement
- A structured technical document from architecture decisions already made
- To convert conversation-based design into a deliverable document

**Trigger:** `/oracle-sdd-generator` or when user says "generate SDD", "write the solution design doc"

**Prerequisite:** Phase 2 (ARCHITECT) of /oracle-solution-design should be complete, or the user must provide equivalent context in conversation.

---

## SDD Structure

### Document Sections

Every SDD follows this structure. Sections can be expanded or condensed based on engagement complexity.

```
SOLUTION-DESIGN.md
  1. Executive Summary
  2. Business Context
  3. Requirements Summary
  4. Solution Architecture
     4.1 Architecture Overview
     4.2 OCI Service Selection
     4.3 Data Architecture
     4.4 Integration Architecture
     4.5 Security Architecture
  5. Implementation Approach
     5.1 Tier Definitions
     5.2 Phased Roadmap
     5.3 Dependencies and Assumptions
  6. Cost Estimation (BOM)
     6.1 Per-Tier Breakdown
     6.2 Pricing Sources
  7. Risk Assessment
  8. Success Criteria
  Appendix A: OCI Service Reference
  Appendix B: Glossary
```

---

## Section Guidelines

### 1. Executive Summary
- 3-5 sentences maximum
- Business outcome focus, not technical details
- Must be understandable by a non-technical executive
- Include solution tier recommendation

### 2. Business Context
- Problem statement (what pain exists today)
- Current state (what tools/processes are in use)
- Desired future state (what success looks like)
- CONFIDENTIALITY: Use generic descriptions, never name the customer

### 3. Requirements Summary
- Table format: Requirement | Priority | OCI Service | Notes
- Top 3-5 functional requirements
- Top 3-5 non-functional requirements (performance, security, compliance)

### 4. Solution Architecture

**4.1 Architecture Overview**
- High-level diagram reference (link to architecture.png)
- 3-tier description: Presentation > Application > Data
- Key design decisions with rationale

**4.2 OCI Service Selection**
Table format for every service:
| Service | Purpose | Why This Service | Alternative Considered |
Each selection MUST reference official documentation.

**4.3 Data Architecture**
- Data flow diagram reference
- Storage strategy (Object Storage, Autonomous DB, etc.)
- Vector search strategy if AI workload
- Data residency and sovereignty requirements

**4.4 Integration Architecture**
- API specifications (REST, gRPC, event-driven)
- Integration patterns (OIC, API Gateway, Functions)
- Third-party connections

**4.5 Security Architecture**
- IAM and RBAC model
- Encryption (at rest, in transit, in use)
- Network isolation (VCN, subnets, security lists)
- Compliance framework mapping (GDPR, HIPAA, etc.)

### 5. Implementation Approach

**5.1 Tier Definitions**
| Aspect | Basic | Advanced | Premium |
Each tier must be self-contained and deployable independently.

**5.2 Phased Roadmap**
- Phase 1: Foundation (weeks 1-4)
- Phase 2: Core capabilities (weeks 5-8)
- Phase 3: Advanced features (weeks 9-12)
- Phase 4: Optimization (weeks 13-16)
Timeline is indicative only. Never commit to dates without customer input.

**5.3 Dependencies and Assumptions**
- List each assumption explicitly
- Identify external dependencies (customer data, access, approvals)

### 6. Cost Estimation (BOM)

**MANDATORY RULES:**
- All prices MUST come from oracle.com/cloud/price-list/
- Include date of price verification
- Show per-month and per-year totals
- Separate compute, storage, networking, AI/ML costs
- NEVER extrapolate one service cost to "total savings"
- Include Universal Credits calculation if applicable

Format:
| Service | Shape/Config | Qty | Monthly ($) | Annual ($) | Source |

**6.2 Pricing Sources**
- Link every price to its official source
- Note any assumptions (region, commitment period)

### 7. Risk Assessment
Table format:
| Risk | Likelihood | Impact | Mitigation |
Minimum 5 risks covering: technical, schedule, resource, compliance, adoption.

### 8. Success Criteria
- Measurable KPIs tied to business outcomes
- Technical acceptance criteria
- User adoption metrics

---

## Confidentiality Rules for SDD

1. Solution name: Use codename or generic solution name (e.g., "AI Document Intelligence Platform")
2. Customer: NEVER named. Use "the organization" or "the customer"
3. Industry: Can mention industry IF provided in conversation, but keep generic
4. Data: All examples use synthetic/mock data
5. File location: clients/[CODE]/SOLUTION-DESIGN.md (gitignored via clients/.gitignore)

---

## Agent Strategy for SDD Generation

For a full SDD, dispatch these in sequence:

1. Read all Phase 1+2 outputs from conversation context
2. Task(system-architect) for architecture sections (4.1-4.5)
3. Task(researcher) for pricing verification (section 6)
4. Main context for executive summary, business context, risk assessment
5. /oracle-confidentiality for final audit

---

*Version: 1.0 | Created: 2026-02-09*
