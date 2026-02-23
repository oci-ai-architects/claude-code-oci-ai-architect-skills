# Oracle AI Architect Toolkit
## Complete Workflow Guide: From Idea to Working Prototype

> **For:** Oracle AI Architect Team
> **Version:** 1.0 — February 2026
> **Disclaimer:** Unofficial community project. Not affiliated with or endorsed by Oracle Corporation.

---

## Table of Contents

1. [The AI-First Prompting Philosophy](#1-the-ai-first-prompting-philosophy)
2. [Setup: Oracle ADB MCP (All Tools)](#2-setup-oracle-adb-mcp)
3. [The Complete Pipeline](#3-the-complete-pipeline)
4. [Phase-by-Phase Guide with Prompts](#4-phase-by-phase-guide)
5. [Skill Integration Map](#5-skill-integration-map)
6. [Hub Portal Integration](#6-hub-portal-integration)
7. [Worked Example: End-to-End](#7-worked-example)
8. [Quick Reference Card](#8-quick-reference-card)

---

## 1. The AI-First Prompting Philosophy

> **The single biggest mistake:** Telling the AI exactly what to build before asking it what's best.

Most architects jump straight to "Build me X with Y services." This wastes the AI's most valuable capability — **its ability to reason about your problem before you've committed to a solution.**

### The Two-Prompt Pattern

Every phase in this guide follows a **two-prompt pattern:**

| Step | Prompt Type | Purpose | Example |
|------|------------|---------|---------|
| **1. ASK** | Intelligence prompt | Get the AI's analysis, options, trade-offs | "What's the best approach for...?" |
| **2. DIRECT** | Execution prompt | Build the thing, with informed decisions | "Build it using approach B because..." |

**The ASK prompt is where the magic happens.** The AI has seen thousands of architecture patterns, knows OCI service capabilities in depth, and can identify trade-offs you haven't considered. Skip it, and you're using a supercomputer as a typewriter.

### Phase-by-Phase: What to ASK Before You DIRECT

#### Phase 1: Discovery — ASK for Research Strategy

**Don't start with:** "Research document AI on OCI"

**Start with:**
```
I have a client who needs [high-level problem description].
Before I start researching:

1. What are the 3-5 most critical questions I should answer first?
2. What existing OCI solutions or blueprints might already solve this?
3. What are the non-obvious technical considerations I might miss?
4. What's the fastest path to a validated architecture — what should
   I research in parallel vs. sequentially?
5. Based on your knowledge, what's the most common mistake teams
   make when building this type of solution?

Help me build an efficient research plan before I start searching.
```

**Why this works:** The AI will identify blind spots, suggest existing solutions you didn't know about, and save hours of undirected research.

#### Phase 2: PRD — ASK for Requirements You're Missing

**Don't start with:** "Write a PRD with these requirements: [list]"

**Start with:**
```
Here's what we know about the client's needs: [paste discovery findings]

Before I write the PRD:
1. What requirements are implied but not stated? (security, compliance,
   observability, DR, data residency)
2. What questions should I go back to the client with before finalizing?
3. For requirements like [X], are there OCI-native solutions that would
   change how we frame the requirement?
4. What's the minimum viable architecture that would let us validate
   the concept in 2 weeks?
5. Where have you seen similar projects fail — what should our
   "must have" list protect against?
```

**Why this works:** The AI catches missing NFRs (non-functional requirements) that architects commonly forget until production — like data residency, audit logging, cost alerting, and graceful degradation.

#### Phase 3: User Flows — ASK for the Critical Path

**Don't start with:** "Create user flows for 4 personas"

**Start with:**
```
We're building [solution] with these personas: [list]

Before I design the flows:
1. Which persona's workflow is most critical to get right first?
   What makes their experience make-or-break for adoption?
2. Where should AI augment vs. automate? What decisions need
   a human-in-the-loop gate?
3. What error states and edge cases should the flows account for?
4. What's the simplest possible happy path that still demonstrates
   the full value proposition?
5. From a UX perspective, what's the #1 thing that would make
   an executive say "wow" in a 5-minute demo?
```

**Why this works:** The AI identifies which flow to prototype first (the one with highest demo impact), where human oversight is critical (builds trust), and what edge cases will bite you later.

#### Phase 4: Architecture — ASK for Trade-offs

**Don't start with:** "Design an OCI architecture with these services: [list]"

**Start with:**
```
Here's our PRD and key requirements: [paste or reference]

Before I commit to an architecture:
1. What are the 2-3 valid architecture approaches for this?
   Compare them on: cost, complexity, time-to-deploy, scalability.
2. Which OCI services have overlapping capabilities here?
   Help me pick the simplest option that meets requirements.
3. Are there any OCI AI Blueprints or oracle-quickstart patterns
   that already solve 80% of this? Show me before I build custom.
4. What's the biggest cost driver in this architecture?
   How would you optimize it?
5. If we had to cut the timeline in half, what would you simplify
   while keeping the core value?
```

**Why this works:** You get architecture *options* with reasoned trade-offs instead of a single design you can't evaluate. The AI often finds existing patterns that save weeks of work.

#### Phase 5: Visuals — ASK for Diagram Strategy

**Don't start with:** "Create an architecture diagram"

**Start with:**
```
I need to present this architecture to [audience: executives / technical team / both].

Before I generate diagrams:
1. What's the right set of diagrams for this audience?
   (master architecture, data flow, deployment, sequence?)
2. For each diagram, what level of detail is appropriate?
   Executives need outcomes, engineers need service names.
3. What's the one visual that would be most impactful if I
   could only show one slide?
4. How should I layer the information so it tells a story
   from problem → solution → value?
```

#### Phase 6: Engineering — ASK for Prototype Strategy

**Don't start with:** "Build an HTML prototype with [feature list]"

**Start with:**
```
We need a prototype to demonstrate [solution] to [audience].
The demo slot is [X minutes].

Before I build:
1. What's the ONE interaction that best demonstrates the AI value?
   That's what we build perfectly — everything else is secondary.
2. Should this be a clickable mockup, a simulated demo with mock data,
   or a live prototype connected to ADB? What's the right fidelity
   for this stage?
3. What mock data would make the demo feel real and domain-specific?
4. What processing states and animations would make the AI feel
   "alive" during the demo?
5. What's the simplest architecture for the prototype that we could
   later evolve into production code?
```

**Why this works:** You build the right thing at the right fidelity. A connected prototype impresses; a disconnected one with the wrong focus wastes effort.

#### Phase 7: Delivery — ASK for Presentation Strategy

**Don't start with:** "Package everything for delivery"

**Start with:**
```
I'm presenting this solution to [audience role] on [date].
The meeting is [X minutes]. They care about [business outcome].

Before I package the delivery:
1. What's the ideal narrative arc for this presentation?
   (Problem → Vision → Architecture → Demo → Next Steps?)
2. Which deliverables should I walk through vs. leave as reference?
3. What objections should I prepare for? What questions will they ask?
4. How should I frame the cost — total investment, per-unit savings,
   or ROI comparison?
5. What's the one thing that would make them approve budget in
   this meeting vs. asking for a follow-up?
```

### The Compound Effect

Each ASK prompt doesn't just improve one phase — it improves all downstream phases:

```
ASK: Research strategy     → Better discovery    → Better requirements
ASK: Missing requirements  → Better PRD          → Better architecture
ASK: Architecture options  → Better design       → Better prototype
ASK: Prototype strategy    → Better demo         → Better approval rate
```

**Teams that ask first, build second, deliver faster.** The initial 5-minute ASK prompt saves hours of rework.

### Golden Rules

1. **Always ask "what am I missing?" before finalizing** — the AI catches blind spots
2. **Request options, not answers** — "give me 3 approaches" beats "do it this way"
3. **Share context generously** — the more the AI knows about your client's constraints, the better its reasoning
4. **Challenge the AI's first answer** — "what's the downside of that approach?" often reveals the best path
5. **Use the AI's analysis to make YOUR decision** — you're the architect, it's your judgment call

---

## 2. Setup: Oracle ADB MCP

The Oracle SQLcl MCP server gives your AI coding assistant **direct access to Oracle Autonomous Database**. It works with every major AI coding tool.

### What You Get

| Capability | Tool | Description |
|------------|------|-------------|
| `run-sql` | Execute SQL | Run queries, get CSV results |
| `run-sqlcl` | Execute SQLcl | APEX exports, DBMS_CLOUD, Data Pump, Liquibase, `AI` command |
| `schema-information` | Inspect schema | Tables, columns, relationships, constraints |
| `connect` / `disconnect` | Manage connections | Switch between saved database connections |
| `list-connections` | Browse connections | See all saved SQLcl connections with details |
| `run-sql-async` | Async queries | Long-running queries without timeout |

### Prerequisites

1. **SQLcl 25.4+** installed (`sql -version` to check)
2. **Wallet downloaded** from OCI Console (Autonomous Database → DB Connection → Download Wallet)
3. **Saved connection** created in SQLcl:
   ```bash
   sql /nolog
   SQL> conn -save MyADB -savepwd agent_admin/YourPassword@adb_medium \
        -wallet /path/to/Wallet_ADB
   ```

### Configuration by Tool

All tools use the same pattern: launch `sql -mcp` as a stdio MCP server.

#### Claude Code (`.mcp.json`)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"],
      "timeout": 120
    }
  }
}
```

**WSL variant** (if SQLcl is installed in WSL):
```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "wsl.exe",
      "args": ["-d", "Ubuntu-24.04", "--", "bash", "-lc", "sql -mcp"],
      "timeout": 120
    }
  }
}
```

#### Cline (VS Code — `cline_mcp_settings.json`)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"],
      "timeout": 120,
      "disabled": false
    }
  }
}
```

Location: VS Code Settings → Cline → MCP Servers → Edit

#### OpenCode (`opencode.json` or settings)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"]
    }
  }
}
```

#### Codex (OpenAI — `codex_mcp.json`)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"]
    }
  }
}
```

#### Gemini CLI (`gemini_mcp_settings.json`)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"]
    }
  }
}
```

#### Cursor / Windsurf (`.cursor/mcp.json` or `.windsurf/mcp.json`)

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"]
    }
  }
}
```

### Verify Connection

After configuring, test with these prompts in any tool:

```
List my Oracle database connections
```

```
Connect to MyADB and show me the database version
```

```
Show me all tables in my current schema with row counts
```

### What the ADB MCP Enables

| Use Case | Example Prompt |
|----------|---------------|
| **Schema exploration** | "What tables exist? Show me the ERD relationships" |
| **Data analysis** | "Analyze the patient_core table — show distributions by diagnosis" |
| **Select AI Agent** | "Run: SELECT AI 'summarize sales trends' FROM dual" |
| **Vector search** | "Find similar documents using VECTOR_DISTANCE on my embeddings table" |
| **Performance tuning** | "Show me the top 10 slowest queries from V$SQL" |
| **Prototype data** | "Generate realistic mock data for the demo and insert 100 rows" |

---

## 3. The Complete Pipeline

```
 INTAKE → DISCOVER → PRD → USER FLOWS → ARCHITECT → VISUALIZE → ENGINEER → DELIVER
   │         │        │        │           │           │           │          │
   ▼         ▼        ▼        ▼           ▼           ▼           ▼          ▼
 Scope    Research   Reqts    Journeys   OCI Design  Diagrams   Prototype  Package
 Client   Industry   MoSCoW   Personas   Services    Mockups    HTML/Code  Audit
 Brief    Patterns   KPIs     Screens    BOM         Draw.io    Database   Present
```

### Pipeline at a Glance

| # | Phase | Time | Primary Skill | Output |
|---|-------|------|---------------|--------|
| 0 | **Intake** | 15 min | Manual / conversation | Client brief, codename assigned |
| 1 | **Discover** | 30 min | `/oracle-research` | Discovery notes, industry context |
| 2 | **PRD** | 30 min | `/oracle-solution-design` | Requirements document (MoSCoW) |
| 3 | **User Flows** | 20 min | Direct prompting | Persona maps, journey diagrams |
| 4 | **Architect** | 45 min | `/oci-services-expert` | Architecture, BOM, SDD |
| 5 | **Visualize** | 30 min | `/oracle-infogenius` | Architecture diagrams (logo-free) |
| 6 | **Engineer** | 60-120 min | `/oracle-solution-design` | Working HTML prototype |
| 7 | **Deliver** | 20 min | `/oracle-confidentiality` | Audited package, presentation |

**Total: 4-6 hours for a complete solution design with working prototype.**

---

## 4. Phase-by-Phase Guide

### Phase 0: Intake & Scoping

**What happens:** Client makes a request or you identify an opportunity. You create a codename and capture the initial brief.

**Steps:**
1. Assign a codename (A-Z) — never use real client names in any file
2. Create `clients/[CODE]/README.md` with status and your role only
3. Capture the brief in conversation (not in files)

**Example prompt:**
```
I'm starting work on a new engagement. Codename: K.
They need an AI-powered document processing system that can:
- Extract data from scanned invoices
- Classify documents by type
- Route to appropriate department
- Integrate with their existing ERP

Help me structure the initial brief and identify what we need to discover.
```

**Output:** Structured brief with open questions for discovery phase.

---

### Phase 1: Discover & Research

**Primary skill:** `/oracle-research`

**What happens:** Parallel research into OCI capabilities, industry patterns, existing solutions, and pricing. This is where you validate that you're not reinventing the wheel.

**Step 1 — Check existing solutions FIRST:**

```
/oracle-research

Research what already exists on OCI for intelligent document processing:
1. Check oracle-quickstart for any document AI blueprints
2. Check OCI Document Understanding service capabilities
3. Look at OCI AI Blueprints for relevant accelerator packs
4. What industry patterns exist for invoice processing on Oracle?

Save findings to research/topics/ (no client references).
```

**Step 2 — Industry & competitor research:**

```
Research enterprise document processing AI platforms in 2026:
- What are the key capabilities expected?
- What compliance requirements apply (GDPR, SOC2)?
- What are typical accuracy benchmarks for invoice extraction?
- What OCI services map to each capability?
```

**Step 3 — Pricing research:**

```
/oci-services-expert

I need verified pricing for these OCI services for a document processing solution:
- OCI Document Understanding (per page)
- OCI GenAI - Cohere Command A (for classification)
- OCI Object Storage (for document storage)
- Oracle AI Database 26ai (Autonomous, for metadata + vector search)
- OCI Functions (for processing pipeline)

Verify all prices against oracle.com/cloud/price-list/ with dates.
```

**Quality Gate 1 checklist:**
- [ ] Top 3 use cases identified
- [ ] OCI services mapped to each requirement
- [ ] Existing oracle-quickstart patterns checked
- [ ] AI Blueprints decision tree consulted
- [ ] Pricing verified with sources
- [ ] Zero real client names in any file

---

### Phase 2: Product Requirements Document

**Primary skill:** `/oracle-solution-design` (Phase 2: ARCHITECT)

**What happens:** Transform discovery findings into structured requirements with MoSCoW prioritization.

**Example prompt:**
```
Based on our discovery for codename K, create a PRD with:

## Requirements (MoSCoW)

MUST HAVE:
- Invoice data extraction (vendor, amount, date, line items)
- Document classification (invoice, PO, receipt, contract)
- Searchable document archive with metadata

SHOULD HAVE:
- Automated routing to department based on classification
- Duplicate detection
- Approval workflow integration

COULD HAVE:
- Natural language querying ("show me all invoices over $10K from Q1")
- Anomaly detection (unusual amounts, vendors)

WON'T HAVE (this phase):
- ERP write-back integration
- Multi-language support

For each requirement, map the OCI service and estimate effort.
Format as a table: Requirement | Priority | OCI Service | Effort | Notes
```

**Output:** Structured PRD with service mappings.

---

### Phase 3: User Flows & Journeys

**What happens:** Map the user personas and their journeys through the solution. This drives the prototype design.

**Example prompt:**
```
Create user flow diagrams for our document processing solution.

Personas:
1. **AP Clerk** — Uploads/scans invoices daily, needs fast processing
2. **Finance Manager** — Reviews flagged items, approves exceptions
3. **Auditor** — Searches historical documents, runs compliance checks

For each persona, create:
1. A step-by-step user journey (5-7 steps)
2. Key screens they interact with
3. Decision points and branching logic
4. AI touchpoints (where the system adds intelligence)

Format as Mermaid flowcharts I can embed in documentation.
```

**For visual journey maps:**
```
/oracle-infogenius

Create a user journey diagram showing:
- 3 personas (AP Clerk, Finance Manager, Auditor)
- Their workflow from document upload to final action
- AI decision points highlighted in Oracle Red (#C74634)
- Dark background, professional style, NO Oracle logos
- Show the OCI services powering each step as subtle labels
```

---

### Phase 4: Technical Architecture

**Primary skill:** `/oci-services-expert` + `/oracle-sdd-generator`

**What happens:** Design the full OCI architecture with service selection, security, networking, and cost estimation.

**Step 1 — Architecture design:**

```
/oci-services-expert

Design a 3-tier OCI architecture for intelligent document processing:

REQUIREMENTS:
- Process 10,000 documents/day
- 99.9% availability
- GDPR compliant (EU region)
- Sub-5-second classification
- Searchable archive with vector similarity

CONSTRAINTS:
- Must use EU Frankfurt region
- Budget: target under $5K/month for production
- Integration: REST API for ERP connectivity

Include:
1. Architecture overview (compute, storage, AI, networking, security)
2. OCI service selection with rationale for EACH service
3. Data flow: upload → classify → extract → store → search
4. Security architecture (IAM, encryption, network isolation)
5. Cost estimate (BOM) with verified pricing
```

**Step 2 — Generate the SDD:**

```
/oracle-sdd-generator

Generate a complete Solution Design Document for the document processing
architecture we just designed. Include all 8 sections:
1. Executive Summary
2. Business Context
3. Requirements Summary
4. Solution Architecture (with all sub-sections)
5. Implementation Approach (3 tiers + phased roadmap)
6. Cost Estimation (BOM with verified prices)
7. Risk Assessment (minimum 5 risks)
8. Success Criteria (KPIs)
```

**Quality Gate 2 checklist:**
- [ ] Every OCI service verified against official docs
- [ ] Pricing sourced from oracle.com/cloud/price-list/ with date
- [ ] No blanket "X times cheaper" claims
- [ ] AI Blueprints decision tree consulted
- [ ] Model selection justified per use case
- [ ] Security architecture complete (IAM, encryption, network)

---

### Phase 5: Architecture Visuals & Mockups

**Primary skill:** `/oracle-infogenius` or `/oracle-diagram-generator`

**What happens:** Create professional, logo-free architecture diagrams and UI mockups.

**Step 1 — Master architecture diagram:**

```
/oracle-infogenius

Create a master architecture diagram for an intelligent document processing
platform on OCI:

LAYERS (top to bottom):
1. SECURITY & GOVERNANCE: WAF, API Gateway, IAM, Cloud Guard, Data Safe
2. INGESTION: Object Storage upload → OCI Events → Functions (preprocessing)
3. AI PROCESSING: Document Understanding (OCR/extraction) → GenAI (classification) → Functions (routing)
4. DATA PLATFORM: Oracle AI Database 26ai (metadata + vectors) → Object Storage (documents)
5. PRESENTATION: API Gateway → Web Application (search, dashboard, reports)
6. OBSERVABILITY: Logging, Monitoring, APM

STYLE:
- Dark background, Oracle Red (#C74634) accents
- NO Oracle logos — text labels only
- Clean, professional, McKinsey-grade
- Show data flow arrows between layers
- Include service names as labels
```

**Step 2 — Data flow diagram:**

```
/oracle-infogenius

Create a data flow diagram showing:
Document Upload → Object Storage → Event Trigger → Function (validate) →
Document Understanding (OCR + extract) → GenAI Cohere Command A (classify) →
Oracle AI Database 26ai (store metadata + embeddings) → API (search/query)

Show each step as a node with the OCI service name.
Dark theme, horizontal flow, Oracle Red highlights.
NO Oracle logos.
```

**Step 3 — Draw.io for editable diagrams:**

```
/oracle-diagram-generator

Generate a Draw.io XML file for the document processing architecture.
Use the OCI icon shapes where available.
Include: VCN boundary, subnet layout, all services with correct icons.
Output as XML I can import into draw.io.
```

**Quality Gate 3 checklist:**
- [ ] ZERO Oracle logos in any image
- [ ] Service names match official branding (AI Database 26ai)
- [ ] No spelling errors
- [ ] Readable at 1920x1080
- [ ] Architecture matches the SDD
- [ ] Brand colors applied correctly

---

### Phase 6: Engineering & Prototype

**Primary skill:** `/oracle-solution-design` (Phase 4: PROTOTYPE)

**What happens:** Build a working interactive prototype that demonstrates the core workflow with realistic mock data.

**Step 1 — Define prototype scope:**

```
Build an interactive HTML prototype for the document processing solution.

CORE WORKFLOW TO DEMONSTRATE:
1. Document upload (drag-and-drop zone)
2. AI processing animation (show Document Understanding + GenAI classification)
3. Extracted data display (vendor, amount, date, line items in structured view)
4. Classification result with confidence score
5. Document search with AI-powered natural language query

REQUIREMENTS:
- Single index.html with embedded CSS/JS (no build tools)
- Dark theme with Oracle Red (#C74634) accents
- Realistic mock data (5-10 sample invoices)
- Processing state animations (loading spinners, progress bars)
- "PROTOTYPE" banner clearly visible
- Mobile responsive
- Professional enough for executive demo

DO NOT:
- Use real customer data
- Include non-functional buttons (label "Coming Soon" if needed)
- Include Oracle logos
```

**Step 2 — Add database connectivity (optional, with ADB MCP):**

```
Connect to ADB and create the schema for our document processing prototype:

CREATE TABLE doc_metadata (
  doc_id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
  filename VARCHAR2(500),
  doc_type VARCHAR2(50),
  classification_confidence NUMBER,
  vendor_name VARCHAR2(200),
  invoice_amount NUMBER,
  invoice_date DATE,
  extracted_data JSON,
  embedding VECTOR(1024, FLOAT32),
  uploaded_at TIMESTAMP DEFAULT SYSTIMESTAMP
);

Then insert 10 realistic sample rows for the prototype demo.
```

**Step 3 — Connect prototype to live data (advanced):**

```
Update the prototype to fetch data from our ADB via a REST API.
Use ORDS (Oracle REST Data Services) endpoints:
- GET /documents — list all processed documents
- GET /documents/:id — document detail with extracted data
- POST /documents/search — vector similarity search

Show me how to enable ORDS for the doc_metadata table.
```

**Quality Gate 4 checklist:**
- [ ] Core workflow works end-to-end
- [ ] Processing states visible (loading, progress)
- [ ] No broken buttons or dead links
- [ ] PROTOTYPE/DEMO banner displayed
- [ ] No real customer data
- [ ] Responsive layout works on mobile

---

### Phase 7: Delivery & Audit

**Primary skill:** `/oracle-confidentiality`

**What happens:** Package everything, run confidentiality audit, prepare for client presentation.

**Step 1 — Package deliverables:**

```
Package the complete solution for codename K:

Expected structure:
clients/K/
  README.md                    # Status + role only (codename, no industry)
  deliverables/
    docs/
      SOLUTION-DESIGN.md       # Full SDD
      DISCOVERY.md             # Requirements captured
      BOM.md                   # Bill of Materials
    images/
      architecture-master.png  # Full architecture (logo-free)
      data-flow.png            # Processing pipeline
      user-journey.png         # Persona flows
    prototype/
      index.html               # Interactive demo

Verify all files are in place and the prototype loads standalone.
```

**Step 2 — Confidentiality audit:**

```
/oracle-confidentiality

Run a full pre-delivery audit on clients/K/:
1. Grep all files for real customer names, industry terms, geographic identifiers
2. Verify README.md contains ONLY status + role + codename
3. Check .gitignore blocks deliverables from git
4. Verify all images are logo-free
5. Confirm no internal pricing beyond published list prices
6. Run the McKinsey test: Would a top firm present this?

Report: PASS/FAIL for each check.
```

**Quality Gate 5 checklist:**
- [ ] All files in correct structure
- [ ] README contains codename only
- [ ] Images are logo-free (visual inspection)
- [ ] Prototype loads standalone
- [ ] BOM pricing verified with sources and dates
- [ ] Confidentiality audit PASSED
- [ ] McKinsey test: YES

---

## 5. Skill Integration Map

### How Skills Chain Together

```
                              ┌─────────────────────────────────┐
                              │      /oracle-solution-design     │
                              │      (Master Orchestrator)       │
                              └──────────────┬──────────────────┘
                                             │
          ┌──────────────┬──────────────┬────┴────┬──────────────┐
          ▼              ▼              ▼         ▼              ▼
    ┌──────────┐  ┌──────────┐  ┌──────────┐ ┌────────┐  ┌──────────┐
    │ DISCOVER │  │ ARCHITECT│  │ VISUALIZE│ │ENGINEER│  │ DELIVER  │
    │          │  │          │  │          │ │        │  │          │
    │/research │  │/oci-svc  │  │/infogeni │ │ coder  │  │/confiden │
    │          │  │/sdd-gen  │  │/diagram  │ │ agent  │  │ -tiality │
    └──────────┘  └──────────┘  └──────────┘ └────────┘  └──────────┘
         │              │              │          │              │
    ┌────┴────┐    ┌────┴────┐   ┌────┴──┐  ┌───┴───┐    ┌────┴────┐
    │Research │    │Pricing  │   │Nano   │  │ADB    │    │Grep     │
    │agents   │    │verify   │   │Banana │  │MCP    │    │audit    │
    │(x3)     │    │agent    │   │MCP    │  │       │    │         │
    └─────────┘    └─────────┘   └───────┘  └───────┘    └─────────┘
```

### When to Use Each Skill

| I need to... | Use this skill | Example trigger |
|--------------|---------------|-----------------|
| Design a complete solution end-to-end | `/oracle-solution-design` | "Design an AI solution for codename K" |
| Research OCI capabilities or industry patterns | `/oracle-research` | "What exists for document AI on OCI?" |
| Get OCI architecture guidance with pricing | `/oci-services-expert` | "Which OCI services for invoice processing?" |
| Generate a Solution Design Document | `/oracle-sdd-generator` | "Create the SDD for our architecture" |
| Create architecture diagrams | `/oracle-infogenius` | "Create master architecture diagram" |
| Create editable Draw.io diagrams | `/oracle-diagram-generator` | "Generate Draw.io XML for the architecture" |
| Build an agent system on OCI | `/oracle-adk` | "Build a document routing agent with ADK" |
| Design framework-agnostic agents | `/oracle-agent-spec` | "Define the agent spec in YAML" |
| Audit before client delivery | `/oracle-confidentiality` | "Run pre-delivery audit on clients/K/" |
| Query the live database | ADB MCP (direct) | "Show me the schema" / "Run this query" |

### Decision Tree

```
Client request arrives
    │
    ├── Need full solution design?
    │   └── YES → /oracle-solution-design (orchestrates everything)
    │
    ├── Need OCI service advice?
    │   └── YES → /oci-services-expert (pricing + architecture)
    │
    ├── Need research first?
    │   └── YES → /oracle-research (check oracle-quickstart FIRST)
    │
    ├── Need a diagram?
    │   ├── Image (PNG) → /oracle-infogenius (Nano Banana)
    │   └── Editable (XML) → /oracle-diagram-generator (Draw.io)
    │
    ├── Need database work?
    │   └── YES → ADB MCP (schema, queries, ORDS setup)
    │
    ├── Building agents?
    │   ├── On OCI specifically → /oracle-adk
    │   └── Framework-agnostic → /oracle-agent-spec
    │
    └── Ready to deliver?
        └── /oracle-confidentiality (ALWAYS before sharing)
```

---

## 6. Hub Portal Integration

### The AI CoE Hub

We maintain an **AI Center of Excellence Hub** with 11 industry portals and 86 solution pages. This is your starting point for any client engagement.

```
AI CoE Hub (index.html)
    │
    ├── Healthcare Portal (10 use cases)
    ├── Financial Services Portal (10 use cases)
    ├── Telecommunications Portal (10 use cases)
    ├── Automotive Portal (10 use cases)
    ├── Retail & Consumer Portal (10 use cases)
    ├── Energy & Utilities Portal (10 use cases)
    ├── Public Sector Portal (10 use cases)
    ├── AEC & Consulting Portal
    ├── AI CoE Patterns (cross-cutting)
    └── Database Migration Portal (6 agents)
```

### How to Use the Hub in Client Engagements

#### Step 1: Start from the industry portal

Before designing anything custom, check if the hub already has a relevant solution page.

```
I'm working on codename K — they need document AI capabilities.
Check our AI CoE Hub portals for relevant pre-built solution pages.
Which industry portal and use cases are closest to what they need?
```

#### Step 2: Use solution pages as architecture templates

Each of the 86 solution pages includes:
- Problem statement (3 challenges)
- Stakeholder personas (3-4 roles)
- Discovery questions (tabbed)
- Solution architecture (layered with OCI services)
- Model selection guide
- 4-phase implementation roadmap
- Industry success patterns

**These are ready-made templates** — adapt them rather than starting from scratch.

#### Step 3: Clone and customize for the client

```
Take the Healthcare portal's "Medical Document Intelligence" solution page
(healthcare/05-medical-document-intelligence.html) as a starting template.

Adapt it for codename K's specific requirements:
- Change the use case focus from medical to [their domain]
- Update the OCI services to match our architecture
- Replace the mock data with domain-relevant examples
- Keep the Oracle Redwood design system and styling
- Add our custom prototype as an embedded demo
```

#### Step 4: Link everything into a client portal

```
Create a client-specific portal page for codename K that links:
1. Executive overview (from our SDD executive summary)
2. Architecture diagram (from Phase 5 visuals)
3. Interactive prototype (from Phase 6)
4. Implementation roadmap (from the SDD)
5. Cost estimate summary (from the BOM)

Use the same Oracle Redwood design system as the hub portals.
Single self-contained HTML file, dark theme, professional.
```

### Portal Architecture Pattern

Every portal follows this proven structure:

```
Portal Page (industry.html)
├── Hero Section (stats, CTA)
├── Executive Brief (3 callout cards)
├── Stakeholder Profiles (4 personas with pain/gain)
├── Industry Verticals (4 sub-segments)
├── Use Case Grid (10 cards with priority badges)
├── Interactive Assessment Tool
├── Methodology (Discover → Design → Build → Scale)
├── Cross-Portal Links (3 related industries)
└── Footer + CTA
```

### Generator Scripts (for scale)

If you need to generate many solution pages quickly:

```bash
# Generate solution pages for a new industry
python projects/hub/generate-pages.py

# Generate a new portal hub page
python projects/hub/generate-portals.py

# Enhance all pages with animations
python projects/hub/enhance-solutions.py
```

---

## 7. Worked Example: End-to-End

### Scenario: "Build an AI-powered patent analysis platform"

Here's every prompt in sequence for a complete engagement:

---

#### 0. Intake

```
I'm starting a new engagement. Codename: P.
They want an AI platform that can:
- Analyze patent documents (text + chemical structures)
- Find prior art automatically
- Generate freedom-to-operate reports
- Support multiple technical domains (chemistry, electronics, biotech)

Set up the client folder and help me plan the discovery phase.
```

---

#### 1. Discover — ASK First

```
I need to build an AI-powered patent analysis platform on OCI.
Before I start researching:

1. What are the hardest technical challenges in patent AI?
   (OCR quality? Claim parsing? Chemical structure recognition?)
2. Does oracle-quickstart or OCI AI Blueprints already have something
   for document-heavy analysis? What should I check first?
3. What's the typical architecture pattern for hybrid search
   (semantic + keyword + structural) on Oracle?
4. What OCI GenAI models would you recommend evaluating for
   patent text analysis, and why each one?
5. What's the biggest risk in this type of project that I should
   validate early?
```

Then, based on the AI's analysis, DIRECT the research:

```
/oracle-research

Deep dive research for a patent AI platform on OCI:
1. Check oracle-quickstart for document analysis blueprints
2. Research: What AI models are best for patent text analysis?
3. Research: Chemical structure recognition — what OCI services apply?
4. Research: Prior art search — vector similarity vs keyword vs graph?
5. Check OCI AI Blueprints for any relevant accelerator packs
6. Verify pricing for: OCI GenAI, Document Understanding, AI Database 26ai

Save to research/topics/patent-ai-platform-capabilities-2026.md
```

---

#### 2. PRD — ASK for Gaps

```
Here are my discovery findings for codename P: [paste key findings]

Before I write the PRD:
1. What non-functional requirements am I likely missing for a
   patent platform? (IP security? Data isolation between clients?
   Audit trails for legal defensibility?)
2. For the chemical structure search requirement — is this a MUST
   or a SHOULD? What's the complexity vs. value trade-off?
3. What would a Phase 1 MVP look like that we could demo in 4 weeks?
4. What compliance frameworks apply to patent data processing?
```

Then DIRECT the PRD creation:

```
Create a PRD for codename P's patent analysis platform:

MUST HAVE:
- Patent document ingestion (PDF, XML/WIPO ST.36)
- Full-text extraction with structure preservation
- Prior art search (semantic + keyword hybrid)
- Chemical substructure search (Markush recognition)

SHOULD HAVE:
- Freedom-to-operate analysis with AI-generated reports
- Multi-domain classification (chemistry, electronics, biotech)
- Patent family tracking and citation analysis

COULD HAVE:
- Natural language patent querying
- Automated patent landscape mapping
- Competitive intelligence dashboards

Map each requirement to OCI services with MoSCoW priority.
```

---

#### 3. User Flows

```
Design user flows for 4 personas:

1. Patent Analyst — Searches prior art, reviews AI findings
2. Patent Attorney — Generates FTO reports, reviews legal risk
3. R&D Scientist — Searches for related patents in their domain
4. IP Executive — Views portfolio dashboards, strategic insights

Create Mermaid flowcharts showing each persona's primary workflow.
Include AI decision points and human review gates.
```

---

#### 4. Architect — ASK for Options

```
Based on our PRD, I need an OCI architecture for patent analysis.

Before you design it, help me think through:
1. What are the 2-3 valid architecture approaches? Compare:
   - Serverless (Functions + GenAI API) vs. Container-based (OKE + vLLM)
   - OCI GenAI managed models vs. Dedicated AI Cluster (fine-tuned)
   - Single ADB vs. Separate search + storage
2. For hybrid search (text + vector + graph), what's the simplest
   way to do this on Oracle AI Database 26ai?
3. What's the biggest cost driver? If budget is $5K/month, what
   gets squeezed first?
4. EU data residency is required — which models and services are
   available in Frankfurt? Any gotchas?
```

Then DIRECT the architecture:

```
/oci-services-expert

Design the OCI architecture for a patent analysis platform:

Scale: 100,000 patents/month ingestion, 500 concurrent users
Requirements:
- Hybrid search (vector + keyword + graph)
- Chemical structure processing
- Multi-model AI pipeline (extraction → classification → analysis → generation)
- EU data residency required

Must include:
1. Full service selection with rationale
2. Data architecture (Oracle AI Database 26ai with vector + graph)
3. AI pipeline (which GenAI models for each stage)
4. Security (GDPR, data isolation, encryption)
5. BOM with verified OCI pricing
```

Then:

```
/oracle-sdd-generator

Generate the complete SDD from our architecture.
Include 3 tiers: Essential / Professional / Enterprise.
```

---

#### 5. Visualize

```
/oracle-infogenius

Create master architecture diagram:
- 5 layers: Security, Ingestion, AI Processing, Data Platform, Presentation
- Show the multi-model pipeline: Document Understanding → Cohere Command A (classification)
  → Cohere Embed 4 (embeddings) → Oracle AI Database 26ai (hybrid search + graph)
- Dark background, Oracle Red accents, NO logos
- Professional, executive-ready quality
```

---

#### 6. Engineer — ASK for Demo Strategy

```
We have a 15-minute demo slot with the client's CTO and Head of IP.
They want to see the patent analysis platform in action.

Before I build the prototype:
1. What's the ONE interaction that would be most impressive?
   Prior art search? AI-generated FTO report? Classification?
2. What mock data would feel authentic to a patent professional?
   (Real-looking patent numbers, realistic chemical names, etc.)
3. Should I connect to our ADB for live queries, or is simulated
   data better for a controlled demo?
4. What processing animations would make the AI feel intelligent
   rather than just fast?
5. What's the "wow moment" — the thing they'll remember after
   the meeting?
```

Then DIRECT the build:

```
Build an interactive prototype for the patent analysis platform:

Single index.html, dark theme, Oracle Redwood design system.

SCREENS:
1. Search interface — query bar with mode toggle (semantic/keyword/structure)
2. Results grid — patent cards with relevance scores, domain tags, dates
3. Patent detail — extracted text, chemical structures, AI analysis panel
4. FTO Report generator — AI-generated freedom-to-operate summary

INTERACTIONS:
- Type a search query → show loading animation → display 8 mock results
- Click a result → slide in detail panel with extracted data
- Click "Generate FTO Report" → show AI processing animation → display report

Include 8 realistic mock patents with chemistry/biotech examples.
PROTOTYPE banner visible. No Oracle logos.
```

---

#### 7. Deliver

```
/oracle-confidentiality

Run pre-delivery audit on all codename P deliverables.
Check for: real names, industry-specific leaks, pricing compliance,
logo violations, broken links, README compliance.
```

---

## 8. Quick Reference Card

### Slash Commands

| Command | Phase | What It Does |
|---------|-------|-------------|
| `/oracle-solution-design` | All | Master orchestrator (5-phase pipeline) |
| `/oracle-research` | Discover | Confidentiality-aware research |
| `/oci-services-expert` | Architect | OCI service selection + pricing |
| `/oracle-sdd-generator` | Architect | Generate Solution Design Document |
| `/oracle-infogenius` | Visualize | Generate architecture images |
| `/oracle-diagram-generator` | Visualize | Generate Draw.io XML diagrams |
| `/oracle-adk` | Engineer | Build agents on OCI with ADK |
| `/oracle-agent-spec` | Engineer | Framework-agnostic agent definitions |
| `/oracle-confidentiality` | Deliver | Pre-delivery audit (VETO power) |

### MCP Servers

| Server | Purpose | Key Commands |
|--------|---------|-------------|
| **SQLcl** | Oracle ADB access | `run-sql`, `schema-information`, `connect` |
| **Nano Banana** | Image generation | `generate_image` |
| **Draw.io** | Editable diagrams | `open_drawio_xml`, `open_drawio_mermaid` |
| **Playwright** | Browser testing | Validate prototypes |

### Mandatory Checks (Every Engagement)

| Check | When | How |
|-------|------|-----|
| Existing solutions | Before designing | Check oracle-quickstart, AI Blueprints |
| Pricing verification | Before any cost claim | oracle.com/cloud/price-list/ with date |
| Model selection | Architecture phase | OCI GenAI Model Selection Matrix |
| Logo compliance | Every visual | NO Oracle logos — text labels only |
| Confidentiality | Before delivery | `/oracle-confidentiality` audit |

### Quality Gates Summary

| Gate | Phase | Key Criteria |
|------|-------|-------------|
| G1 | Discover | 3+ use cases, services mapped, patterns checked |
| G2 | Architect | Pricing verified, no blanket claims, WAF principles |
| G3 | Visualize | Zero logos, correct branding, matches SDD |
| G4 | Engineer | Core workflow works, no dead links, PROTOTYPE label |
| G5 | Deliver | Confidentiality PASS, McKinsey test YES |

### Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| "OCI is 80x cheaper" | Cite specific model comparison with source |
| Hallucinate pricing | Verify at oracle.com/cloud/price-list/ |
| Include Oracle logos in diagrams | Text labels only, Oracle Red accents |
| Build from scratch without checking | Check oracle-quickstart FIRST |
| Use non-functional prototype buttons | Either make it work OR label "Coming Soon" |
| Store client names in files | Codenames only, conversation-only context |
| Skip confidentiality audit | ALWAYS run `/oracle-confidentiality` before delivery |

### OCI Model Selection Quick Reference

| Use Case | Best Model | Why |
|----------|-----------|-----|
| Complex reasoning | Cohere Command A Reasoning | Multi-step, 256K context |
| Multimodal (images+text) | Cohere Command A Vision | Charts, documents |
| Agentic workflows | Llama 4 Maverick | Tool-calling, MoE |
| Coding | Grok Code Fast 1 | Code-optimized |
| RAG / Retrieval | Cohere Command R | RAG-optimized, 128K |
| Embeddings | Cohere Embed 4 | Text + image |
| Speed / Budget | Gemini 2.5 Flash-Lite | High-volume, low-cost |
| EU data residency | Cohere Command A series | EU deployable |
| Long context (2M) | Grok 4.1 Fast | Massive documents |
| Fine-tuning | Llama 3.3 70B (LoRA) | Dedicated AI Clusters |

---

## Appendix A: File Structure

```
oracle-work/
├── .claude/
│   └── skills/                         # All skills live here
│       ├── oracle-solution-design/     # Master orchestrator
│       ├── oracle-sdd-generator/       # SDD generation
│       ├── oracle-confidentiality/     # Pre-delivery audit
│       ├── oracle-research/            # Research protocols
│       │   └── references/             # Pricing, patterns, lessons learned
│       ├── oracle-diagram-generator/   # Draw.io + Python diagrams
│       ├── oci-services-expert/        # OCI architecture guidance
│       ├── oracle-adk/                 # Agent Development Kit
│       └── oracle-agent-spec/          # Open Agent Specification
├── clients/
│   └── [CODE]/                         # One folder per client codename
│       ├── README.md                   # Status + role ONLY
│       └── deliverables/               # (gitignored) SDD, images, prototype
├── projects/
│   └── hub/
│       ├── index.html                  # AI CoE Hub landing page
│       ├── portals/                    # 11 industry portals
│       │   ├── healthcare.html         # + healthcare/ (10 use cases)
│       │   ├── financial-services.html # + financial-services/ (10 use cases)
│       │   ├── automotive.html         # + automotive/ (10 use cases)
│       │   └── ...                     # 8 more portals
│       ├── generate-pages.py           # Bulk solution page generator
│       └── generate-portals.py         # Portal page generator
├── research/
│   └── topics/                         # Research docs (never codename-linked)
├── templates/                          # Reusable templates
│   ├── DAILY-CAPTURE.md
│   ├── WEEKLY-REPORT.md
│   └── WORKSHOP-TEMPLATE.md
└── docs/
    └── AI-ARCHITECT-TOOLKIT-GUIDE.md   # This guide
```

## Appendix B: MCP Configuration Template

Copy this complete `.mcp.json` for all your tools:

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"],
      "description": "Oracle ADB access via SQLcl (schema, SQL, ORDS, Select AI)",
      "timeout": 120
    },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"],
      "description": "Create and open draw.io diagrams from XML, CSV, or Mermaid"
    }
  }
}
```

Add Nano Banana (image generation) and Playwright (browser testing) as needed for your workflow.

---

*Last updated: 2026-02-23*
*For questions or contributions: Open an issue or PR on the repo.*
