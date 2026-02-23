# Oracle AI Architect Toolkit
## Complete Workflow Guide: From Idea to Working Prototype

> **For:** Oracle AI Architect Team
> **Version:** 2.0 — February 2026
> **Disclaimer:** Unofficial community project. Not affiliated with or endorsed by Oracle Corporation.

---

## 1. The Pipeline at a Glance

This is the complete delivery pipeline. Every client engagement follows these 8 phases.

```
 INTAKE → DISCOVER → PRD → USER FLOWS → ARCHITECT → VISUALIZE → BUILD → DELIVER
   │         │        │        │           │           │          │        │
   ▼         ▼        ▼        ▼           ▼           ▼          ▼        ▼
 Scope    Research   Reqts    Journeys   OCI Design  Diagrams   Working   Package
 Client   Industry   MoSCoW   Personas   Services    Draw.io    Proto-    Audit
 Brief    Patterns   KPIs     Screens    BOM         Mockups    type      Present
```

| # | Phase | Time | Skill | One-Liner Prompt | Output |
|---|-------|------|-------|------------------|--------|
| 0 | **Intake** | 15 min | Conversation | "Starting codename K — they need [problem]. Structure the brief." | Client brief |
| 1 | **Discover** | 30 min | `/oracle-research` | "What exists on OCI for [use case]? Check quickstart + AI Blueprints first." | Discovery notes |
| 2 | **PRD** | 30 min | Direct | "Create MoSCoW requirements. What am I missing for [domain]?" | Requirements doc |
| 3 | **User Flows** | 20 min | Direct + Draw.io MCP | "Design user flows for [3 personas]. What's the critical path?" | Journey diagrams |
| 4 | **Architect** | 45 min | `/oci-services-expert` | "Give me 2-3 architecture options. Compare cost, complexity, time." | Architecture + BOM |
| 5 | **Visualize** | 30 min | Draw.io MCP | "Generate Draw.io XML for the architecture with OCI service layers." | .drawio files |
| 6 | **Build** | 60-120 min | Direct + ADB MCP | "Build working prototype — single HTML, connected to ADB, dark theme." | Working prototype |
| 7 | **Deliver** | 20 min | `/oracle-confidentiality` | "Run pre-delivery audit. Grep for real names. Check logo compliance." | Audited package |

**Total: 4-6 hours for a complete solution design with working prototype.**

---

## 2. Skills & Activation

### How Skills Work

All skills live in `.claude/skills/` as SKILL.md files. Claude auto-loads them based on context. There is **no auto-activation system** — you trigger skills explicitly via slash commands or by describing what you need.

### Core Oracle Skills

| Skill | Trigger | What It Does | When to Use |
|-------|---------|-------------|-------------|
| **oracle-research** | `/oracle-research` or "research [topic]" | Confidentiality-aware web research with OCI pattern checks | Phase 1: Discovery |
| **oci-services-expert** | `/oci-services-expert` or "OCI architecture" | Service selection + mandatory pricing verification | Phase 4: Architecture |
| **oracle-sdd-generator** | `/oracle-sdd-generator` or "generate SDD" | Structured Solution Design Document (8 sections) | Phase 4: After architecture |
| **oracle-diagram-generator** | "create OCI diagram" or "Draw.io architecture" | Draw.io XML templates + Mermaid + Python diagrams | Phase 5: Visualize |
| **oci-drawio-icon-native** | Manual (for production diagrams) | Ensures embedded icons, no mxgraph fallback | Phase 5: Quality gate |
| **oracle-adk** | `/adk-agent` or "build an agent" | Oracle Agent Development Kit patterns | Phase 6: If building agents |
| **oracle-agent-spec** | "agent spec" or "portable agents" | Framework-agnostic agent definitions (JSON/YAML) | Phase 6: Agent design |
| **oracle-confidentiality** | `/oracle-confidentiality` or auto at delivery | Pre-delivery audit with VETO power | Phase 7: Always |
| **oracle-solution-design** | `/oracle-solution-design` | Master orchestrator (chains all above) | Full engagement |

### Optional Skills

| Skill | Trigger | What It Does | Dependency |
|-------|---------|-------------|------------|
| **oracle-infogenius** | `/oracle-infogenius` | AI-generated architecture images (PNG) via Nano Banana | Requires Nano Banana MCP |
| **oracle-ai-architect-infogenius** | `/oracle-ai-architect-infogenius` | Audience-aware visuals (research/executive/technical) | Requires Nano Banana MCP |

> **Note:** Infogenius generates beautiful raster images but requires the Nano Banana MCP server. Draw.io MCP is the primary diagram tool — it produces editable, version-controlled `.drawio` files that work everywhere.

### Skill Chaining

```
/oracle-solution-design (orchestrates everything)
├── Phase 1 → /oracle-research (parallel research agents)
├── Phase 2 → /oci-services-expert (service selection + pricing)
│           → /oracle-sdd-generator (document generation)
├── Phase 3 → Draw.io MCP (architecture diagrams)
│           → /oracle-infogenius (optional: raster images)
├── Phase 4 → /oracle-adk (if building agents)
│           → ADB MCP (database schema + data)
└── Phase 5 → /oracle-confidentiality (audit before delivery)
```

---

## 3. Setup: MCP Servers

Two MCP servers are essential. Both work with **every AI coding tool**.

### 3.1 Oracle ADB MCP (SQLcl)

Direct access to Oracle Autonomous Database from your AI assistant.

**Prerequisites:**
1. SQLcl 25.4+ installed (`sql -version`)
2. Wallet downloaded from OCI Console (ADB → DB Connection → Download Wallet)
3. Saved connection: `sql /nolog` then `conn -save MyADB -savepwd user/pass@adb_medium -wallet /path/to/Wallet`

**Capabilities:**

| Tool | What It Does |
|------|-------------|
| `run-sql` | Execute SQL queries, get CSV results |
| `run-sqlcl` | SQLcl commands (APEX, DBMS_CLOUD, Data Pump, `AI` command) |
| `schema-information` | Tables, columns, relationships, constraints |
| `connect` / `disconnect` | Switch between saved connections |
| `run-sql-async` | Long-running queries without timeout |

### 3.2 Draw.io MCP

Create and open editable architecture diagrams directly from Claude.

**Capabilities:**

| Tool | Input | Best For |
|------|-------|---------|
| `open_drawio_xml` | Draw.io XML | Production architectures from templates |
| `open_drawio_mermaid` | Mermaid syntax | Quick flowcharts, sequence diagrams |
| `open_drawio_csv` | CSV data | Org charts, structured layouts |

### 3.3 Configuration (All Tools)

The config is **identical JSON** for every tool — only the file location changes.

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"],
      "timeout": 120
    },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"]
    }
  }
}
```

| Tool | Config File Location |
|------|---------------------|
| **Claude Code** | `.mcp.json` in project root |
| **Cline** (VS Code) | VS Code Settings → Cline → MCP Servers |
| **Cursor** | `.cursor/mcp.json` |
| **Windsurf** | `.windsurf/mcp.json` |
| **OpenCode** | `opencode.json` or settings |
| **Codex** (OpenAI) | `codex_mcp.json` |
| **Gemini CLI** | `gemini_mcp_settings.json` |

**WSL variant** (if SQLcl is in WSL, not Windows PATH):
```json
{
  "sqlcl": {
    "command": "wsl.exe",
    "args": ["-d", "Ubuntu-24.04", "--", "bash", "-lc", "sql -mcp"],
    "timeout": 120
  }
}
```

### 3.4 Draw.io MCP: Known Quirks & Best Practices

| Quirk | Impact | Workaround |
|-------|--------|-----------|
| **mxgraph.oci.* fallback** | OCI icons render as red blocks if library not loaded | Use icon-native mode (embedded stencils) for production diagrams |
| **CSV import not idempotent** | Re-import may render differently | Use XML templates for reproducible output; CSV for exploration only |
| **Large multi-page files** | 40+ pages can be slow in web UI | Generate standalone .drawio per use case; aggregate into master pack separately |
| **Clone geometry** | Cloned icon groups pile up at origin if root x/y missing | Generator must write explicit x/y on clone roots; descendants stay relative |
| **Lightbox mode** | `lightbox=true` makes diagram read-only | Use for sharing/review; omit for editing |

**Best Practice:** Always validate production diagrams with:
```bash
python3 drawio/tools/validate_drawio_icon_integrity.py --file <file> --diagram <name>
# Must report: mxgraph_oci_refs=0, VALIDATION: PASS
```

### 3.5 Draw.io Template Library

We maintain **67 production .drawio files** ready to customize:

| Category | Count | Examples |
|----------|-------|---------|
| **Meta-Architectures** | 6 | AI Factory: Logical, Physical, Execution, User Flows, Governance, Portal |
| **Domain Architectures** | 4 | Healthcare, Automotive, DB Migration, Software/SaaS |
| **Use-Case Architectures** | 37+ | Clinical decision support, fraud detection, supply chain, etc. |
| **Master Portfolios** | 3 | Multi-page packs (4-page domain, 40-page use case, 6-page AI Factory) |
| **OCI Style Guide** | 2 | Official OCI Architecture Diagram Toolkit v24.2 |

**Location:** `drawio/` directory. Use these as starting templates — clone and customize rather than building from scratch.

---

## 4. Phase-by-Phase Guide

> **Prompting principle:** At each phase, **ASK the AI what's best before telling it what to build.** This surfaces blind spots, existing solutions, and trade-offs you haven't considered. Each phase below shows the ASK prompt first, then the DIRECT prompt.

### Phase 0: Intake & Scoping

**What happens:** Client makes a request. You assign a codename and capture the brief.

**Steps:**
1. Assign a codename (A-Z) — never use real client names in any file
2. Create `clients/[CODE]/README.md` with status and role only
3. Capture the brief in conversation (not in files)

**Prompt:**
```
I'm starting work on codename K. They need an AI-powered document processing
system — extract data from scanned invoices, classify documents, route to
departments, integrate with ERP.

Help me structure the initial brief and identify what we need to discover.
```

---

### Phase 1: Discover & Research

**Skill:** `/oracle-research`

**What happens:** Research OCI capabilities, industry patterns, existing solutions, and pricing. The key question: **does something already exist that solves this?**

**ASK first:**
```
Before I start researching document AI on OCI:
1. What existing OCI solutions or blueprints might already solve this?
2. What are the 3-5 most critical questions I should answer?
3. What's the most common mistake teams make building this?
4. What non-obvious technical considerations should I investigate?
```

**Then DIRECT:**
```
/oracle-research

Deep dive for intelligent document processing on OCI:
1. Check oracle-quickstart for document AI blueprints
2. OCI Document Understanding capabilities and limits
3. OCI AI Blueprints — any relevant accelerator packs?
4. Pricing: Document Understanding, GenAI models, ADB, Functions
5. Industry benchmarks for invoice extraction accuracy

Save to research/topics/ — no client references.
```

**Quality Gate 1:**
- [ ] Top 3 use cases identified
- [ ] OCI services mapped to each requirement
- [ ] Existing oracle-quickstart patterns checked
- [ ] AI Blueprints decision tree consulted
- [ ] Zero real client names in any file

---

### Phase 2: Product Requirements Document

**Skill:** Direct prompting (or `/oracle-solution-design` Phase 2)

**What happens:** Transform discovery into structured requirements with MoSCoW prioritization.

**ASK first:**
```
Here's what we found in discovery: [paste key findings]

Before I write the PRD:
1. What requirements are implied but not stated? (security, compliance,
   observability, DR, data residency)
2. What questions should I go back to the client with?
3. What's the minimum viable scope we could demo in 2-4 weeks?
```

**Then DIRECT:**
```
Create a PRD for codename K with MoSCoW prioritization:

MUST: Invoice extraction, document classification, searchable archive
SHOULD: Automated routing, duplicate detection, approval workflow
COULD: Natural language querying, anomaly detection
WON'T (this phase): ERP write-back, multi-language

For each requirement, map: OCI Service | Effort | Priority | Notes
```

---

### Phase 3: User Flows & Journeys

**Skill:** Direct prompting + Draw.io MCP for diagrams

**What happens:** Map personas, their journeys, and the screens they interact with.

**ASK first:**
```
We're building a document processing platform for 3 personas:
AP Clerk, Finance Manager, Auditor.

Before I design flows:
1. Which persona's workflow is most critical to demo first?
2. Where should AI augment vs. automate? Where's the human-in-the-loop?
3. What's the simplest happy path that shows the full value?
```

**Then DIRECT:**
```
Create user flows for each persona as Mermaid flowcharts.
Show: steps, decision points, AI touchpoints, and screens.

Then open them in Draw.io so I can edit:
```

The AI can then use the Draw.io MCP to open the Mermaid directly:
```
Tool: open_drawio_mermaid
Content: <the generated Mermaid code>
```

---

### Phase 4: Technical Architecture

**Skill:** `/oci-services-expert` + `/oracle-sdd-generator`

**What happens:** Design the OCI architecture with service selection, security, and cost estimation.

**ASK first — this is the most important ASK in the entire pipeline:**
```
Based on our PRD, I need an OCI architecture.

Before you design it:
1. What are 2-3 valid architecture approaches? Compare on:
   cost, complexity, time-to-deploy, scalability.
2. Which OCI services overlap here? What's the simplest option?
3. Are there AI Blueprints or quickstart patterns that solve 80% of this?
4. What's the biggest cost driver? How would you optimize it?
5. If we cut the timeline in half, what would you simplify?
```

**Then DIRECT:**
```
/oci-services-expert

Design the OCI architecture for document processing:
- 10K documents/day, 99.9% availability
- EU Frankfurt region (GDPR), budget <$5K/month
- Include: service selection with rationale, data flow, security, BOM
- Verify all prices against oracle.com/cloud/price-list/
```

**Then generate the SDD:**
```
/oracle-sdd-generator

Generate the complete Solution Design Document with all 8 sections.
Include 3 tiers (Basic/Advanced/Premium) and phased roadmap.
```

**Quality Gate 2:**
- [ ] Every service verified against official docs
- [ ] Pricing sourced with date from oracle.com/cloud/price-list/
- [ ] No blanket "X times cheaper" claims
- [ ] AI Blueprints decision tree documented
- [ ] Security architecture complete

---

### Phase 5: Visualize (Architecture Diagrams)

**Skill:** Draw.io MCP (primary) + `/oracle-infogenius` (optional, for raster images)

**What happens:** Create professional, editable architecture diagrams.

**ASK first:**
```
I need to present this architecture to [executives / technical team / both].
1. What's the right set of diagrams for this audience?
2. What level of detail per diagram?
3. Which single visual would be most impactful?
```

**Option A — Generate Draw.io from XML template (recommended):**
```
Generate a Draw.io XML architecture diagram for the document processing platform.

Layers (top to bottom):
1. SECURITY: WAF, API Gateway, IAM, Cloud Guard
2. INGESTION: Object Storage → Events → Functions
3. AI PROCESSING: Document Understanding → GenAI → Functions (routing)
4. DATA: Oracle AI Database 26ai (metadata + vectors) + Object Storage
5. PRESENTATION: API Gateway → Web App

Use Oracle Red (#C74634) for accents, dark background.
Show data flow arrows. Label all OCI services.
```

The AI generates Draw.io XML and opens it via `open_drawio_xml`.

**Option B — Generate from Mermaid (quick):**
```
Create a Mermaid flowchart of the data processing pipeline:
Upload → Validate → OCR/Extract → Classify → Store → Index → Search

Then open in Draw.io for editing.
```

**Option C — Customize existing template:**
```
Take the healthcare domain architecture template from
drawio/domain-architectures/OCI_AICoE_healthcare_Agentic_Architecture.drawio
and adapt it for our document processing use case.
Replace the healthcare-specific services with document AI services.
```

**Option D — Generate raster image (optional, requires Nano Banana MCP):**
```
/oracle-infogenius

Create master architecture diagram. Dark background, Oracle Red accents,
NO Oracle logos. Professional, executive-ready quality.
```

**Quality Gate 3:**
- [ ] ZERO Oracle logos
- [ ] Service names match official branding (AI Database 26ai)
- [ ] Architecture matches the SDD
- [ ] For Draw.io: validate with `validate_drawio_icon_integrity.py`

---

### Phase 6: Build (Working Prototype)

**Skill:** Direct prompting + ADB MCP + Draw.io MCP

**What happens:** Build a working interactive prototype. This is beyond architecture — you're writing real code with real data.

**ASK first:**
```
We need a prototype for a 15-minute demo with the CTO.

Before I build:
1. What's the ONE interaction that best demonstrates the AI value?
2. Should I connect to ADB for live data, or use embedded mock data?
3. What processing animations make AI feel "alive" in a demo?
4. What mock data would feel authentic for this domain?
5. What's the "wow moment" they'll remember?
```

**Then DIRECT the prototype:**
```
Build a working prototype for the document processing platform.

TECH STACK:
- Single index.html with embedded CSS/JS (no build tools needed)
- Connected to Oracle ADB via ORDS REST endpoints
- Dark theme, Oracle Red (#C74634) accents

SCREENS:
1. Upload zone (drag-and-drop) with processing animation
2. Extracted data view (vendor, amount, date, line items)
3. Classification result with confidence score
4. Search interface with AI-powered natural language query

REQUIREMENTS:
- PROTOTYPE banner visible
- Realistic mock data (10 sample invoices)
- Processing state animations (loading, progress bars)
- Mobile responsive
- NO Oracle logos, NO real customer data
```

**To set up the database layer:**
```
Connect to ADB and create the schema:

CREATE TABLE doc_metadata (
  doc_id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
  filename VARCHAR2(500),
  doc_type VARCHAR2(50),
  confidence NUMBER,
  vendor_name VARCHAR2(200),
  invoice_amount NUMBER,
  invoice_date DATE,
  extracted_data JSON,
  embedding VECTOR(1024, FLOAT32),
  uploaded_at TIMESTAMP DEFAULT SYSTIMESTAMP
);

Insert 10 realistic sample rows for the demo.
```

**To enable REST API for the prototype:**
```
Enable ORDS on the doc_metadata table so the prototype can fetch live data.
Show me the curl commands to test each endpoint.
```

**Quality Gate 4:**
- [ ] Core workflow works end-to-end
- [ ] Processing states visible
- [ ] No dead links or broken buttons
- [ ] PROTOTYPE banner displayed
- [ ] No real customer data

---

### Phase 7: Deliver & Audit

**Skill:** `/oracle-confidentiality`

**What happens:** Package everything, run audit, prepare for presentation.

**ASK first:**
```
I'm presenting to [audience] on [date]. Meeting is [X minutes].
1. What's the ideal narrative arc?
2. What objections should I prepare for?
3. How should I frame the cost?
4. What would make them approve budget in this meeting?
```

**Then DIRECT the packaging:**
```
Package deliverables for codename K:

clients/K/
  README.md                    # Status + role only
  deliverables/
    docs/SOLUTION-DESIGN.md    # Full SDD
    docs/BOM.md                # Bill of Materials
    images/architecture.png    # Master diagram
    images/data-flow.png       # Pipeline
    diagrams/architecture.drawio # Editable
    prototype/index.html       # Working demo
```

**Then audit:**
```
/oracle-confidentiality

Full pre-delivery audit on clients/K/:
- Grep for real customer names → must return zero
- Verify README has codename only
- Check images are logo-free
- Confirm BOM uses published pricing with sources
- Run McKinsey test
```

**Quality Gate 5:**
- [ ] Confidentiality audit PASSED
- [ ] All files in correct structure
- [ ] Prototype loads standalone
- [ ] BOM pricing verified with sources
- [ ] Would McKinsey present this? YES

---

## 5. Skill Integration Map

### Decision Tree

```
Client request arrives
    │
    ├── Need full end-to-end design?
    │   └── /oracle-solution-design (orchestrates everything)
    │
    ├── Need OCI service advice + pricing?
    │   └── /oci-services-expert
    │
    ├── Need research first?
    │   └── /oracle-research (check oracle-quickstart FIRST)
    │
    ├── Need a diagram?
    │   ├── Editable (.drawio) → Draw.io MCP + oracle-diagram-generator
    │   ├── Raster image (PNG) → /oracle-infogenius (needs Nano Banana MCP)
    │   └── Quick flowchart → Draw.io MCP with Mermaid input
    │
    ├── Need database work?
    │   └── ADB MCP (schema, queries, ORDS, Select AI)
    │
    ├── Building agents?
    │   ├── On OCI → /oracle-adk
    │   └── Framework-agnostic → /oracle-agent-spec
    │
    └── Ready to deliver?
        └── /oracle-confidentiality (ALWAYS before sharing)
```

---

## 6. Hub Portal Integration

### The AI CoE Hub

We maintain an **AI Center of Excellence Hub** with 11 industry portals and 86 solution pages. Use these as **starting templates** for client work.

```
AI CoE Hub (projects/hub/index.html)
    │
    ├── Healthcare (10 use cases)      ├── Energy & Utilities (10)
    ├── Financial Services (10)        ├── Public Sector (10)
    ├── Telecommunications (10)        ├── AEC & Consulting
    ├── Automotive (10)                ├── AI CoE Patterns
    ├── Retail & Consumer (10)         └── Database Migration (6 agents)
```

### Using Hub Portals in Client Engagements

**Step 1 — Find the closest template:**
```
Check the AI CoE Hub — which portal and use case page is closest
to what codename K needs? Show me the top 3 matches.
```

**Step 2 — Clone and customize:**
```
Take healthcare/05-medical-document-intelligence.html as a template.
Adapt it for codename K's document processing requirements:
- Update OCI services to match our architecture
- Replace mock data with domain-relevant examples
- Keep the Oracle Redwood design system
```

**Step 3 — Link into a client portal:**
```
Create a client portal page for codename K that links:
1. Executive overview → from SDD
2. Architecture diagram → from Phase 5
3. Interactive prototype → from Phase 6
4. Roadmap → from SDD
5. Cost summary → from BOM
```

### Generator Scripts (for scale)

```bash
python projects/hub/generate-pages.py      # Bulk solution pages
python projects/hub/generate-portals.py     # Portal hub pages
python projects/hub/enhance-solutions.py    # Add animations + styling
```

---

## 7. Worked Example: End-to-End

### Scenario: "Build an AI-powered patent analysis platform"

Every prompt below follows the ASK → DIRECT pattern.

---

**0. Intake:**
```
Starting codename P — patent analysis platform. Needs: document analysis
(text + chemical structures), prior art search, FTO reports, multi-domain.
Structure the brief and identify what to discover.
```

**1. Discover — ASK:**
```
Before I research patent AI on OCI:
1. What's hardest — OCR, claim parsing, or chemical structure recognition?
2. Does oracle-quickstart have document analysis blueprints?
3. What architecture pattern works for hybrid search (text + vector + graph)?
4. Biggest risk in this type of project?
```

**1. Discover — DIRECT:**
```
/oracle-research
Research patent AI platform on OCI. Check: quickstart, AI Blueprints,
Document Understanding, GenAI models for patent text. Verify pricing.
```

**2. PRD — ASK:**
```
What non-functional requirements am I missing for patent data?
(IP security? Data isolation? Audit trails for legal defensibility?)
```

**2. PRD — DIRECT:**
```
Create PRD: MUST: extraction, classification, prior art search.
SHOULD: FTO reports, multi-domain classification. COULD: NL querying.
Map each to OCI services.
```

**3. User Flows:**
```
Design flows for: Patent Analyst, Patent Attorney, R&D Scientist, IP Executive.
Which persona's workflow should I prototype first for maximum demo impact?
Then create Mermaid flowcharts and open in Draw.io.
```

**4. Architect — ASK:**
```
Give me 2-3 architecture options. Compare: serverless vs OKE,
managed GenAI vs dedicated cluster, single ADB vs separate search layer.
```

**4. Architect — DIRECT:**
```
/oci-services-expert
Design OCI architecture: 100K patents/month, 500 users,
hybrid search (vector + keyword + graph), EU data residency, BOM with pricing.

Then: /oracle-sdd-generator — full SDD with 3 tiers.
```

**5. Visualize:**
```
Generate Draw.io XML: 5 layers (Security, Ingestion, AI Pipeline,
Data Platform, Presentation). Show multi-model pipeline:
Document Understanding → Cohere Command A → Embed 4 → AI Database 26ai.
```

**6. Build — ASK:**
```
15-minute demo with Head of IP. What's the one interaction
that would be most impressive? Prior art search? AI-generated FTO?
What mock data feels authentic to a patent professional?
```

**6. Build — DIRECT:**
```
Build working prototype: search interface with mode toggle
(semantic/keyword/structure), results grid with relevance scores,
patent detail panel, FTO report generator.
Connect to ADB. 8 mock patents. Dark theme. PROTOTYPE banner.
```

**7. Deliver:**
```
/oracle-confidentiality
Full audit on clients/P/. Grep for real names. Check logos. Verify BOM.
```

---

## 8. Quick Reference Card

### Core Commands

| Command | Phase | What It Does |
|---------|-------|-------------|
| `/oracle-solution-design` | All | Master orchestrator (chains all skills) |
| `/oracle-research` | Discover | Confidentiality-aware research |
| `/oci-services-expert` | Architect | OCI service selection + pricing |
| `/oracle-sdd-generator` | Architect | Generate Solution Design Document |
| `/oracle-confidentiality` | Deliver | Pre-delivery audit (VETO power) |
| `/oracle-adk` | Build | Oracle Agent Development Kit |
| `/oracle-agent-spec` | Build | Framework-agnostic agent definitions |
| `/oracle-infogenius` | Visualize | *Optional:* AI-generated images (needs Nano Banana) |

### MCP Servers

| Server | Purpose | Key Tools |
|--------|---------|-----------|
| **SQLcl** | Oracle ADB access | `run-sql`, `schema-information`, `connect` |
| **Draw.io** | Editable diagrams | `open_drawio_xml`, `open_drawio_mermaid`, `open_drawio_csv` |
| **Nano Banana** | Image generation *(optional)* | `generate_image` |
| **Playwright** | Browser testing *(optional)* | Validate prototypes |

### Mandatory Checks (Every Engagement)

| Check | When | How |
|-------|------|-----|
| Existing solutions | Before designing | Check oracle-quickstart, AI Blueprints |
| Pricing verification | Before any cost claim | oracle.com/cloud/price-list/ with date |
| Model selection | Architecture phase | OCI GenAI Model Selection Matrix |
| Logo compliance | Every visual | NO Oracle logos — text labels only |
| Confidentiality | Before delivery | `/oracle-confidentiality` audit |
| Draw.io validation | Production diagrams | `validate_drawio_icon_integrity.py` |

### Quality Gates

| Gate | Phase | Key Criteria |
|------|-------|-------------|
| G1 | Discover | 3+ use cases, services mapped, patterns checked |
| G2 | Architect | Pricing verified, no blanket claims, security complete |
| G3 | Visualize | Zero logos, correct branding, matches SDD |
| G4 | Build | Core workflow works, no dead links, PROTOTYPE label |
| G5 | Deliver | Confidentiality PASS, McKinsey test YES |

### OCI Model Selection

| Use Case | Best Model | Why |
|----------|-----------|-----|
| Complex reasoning | Cohere Command A Reasoning | 256K context, multi-step |
| Multimodal (images+text) | Cohere Command A Vision | Charts, documents |
| Agentic workflows | Llama 4 Maverick | Tool-calling, MoE |
| Coding | Grok Code Fast 1 | Code-optimized |
| RAG / Retrieval | Cohere Command R | RAG-optimized, 128K |
| Embeddings | Cohere Embed 4 | Text + image |
| Speed / Budget | Gemini 2.5 Flash-Lite | High-volume, low-cost |
| EU data residency | Cohere Command A series | EU deployable |
| Fine-tuning | Llama 3.3 70B (LoRA) | Dedicated AI Clusters |

### Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| Jump straight to "build me X" | ASK: "What are 2-3 approaches? Compare trade-offs" |
| "OCI is 80x cheaper" | Cite specific model comparison with source and date |
| Include Oracle logos in diagrams | Text labels only, Oracle Red (#C74634) accents |
| Build from scratch without checking | Check oracle-quickstart and AI Blueprints FIRST |
| Use mxgraph.oci.* in production Draw.io | Use icon-native mode, validate with Python script |
| Store client names in files | Codenames only, conversation-only context |
| Skip the ASK prompt | 5 minutes of ASK saves hours of rework |

---

## Appendix A: File Structure

```
oracle-work/
├── .claude/skills/                         # All skills
│   ├── oracle-solution-design/             # Master orchestrator
│   ├── oracle-sdd-generator/               # SDD generation
│   ├── oracle-confidentiality/             # Pre-delivery audit
│   ├── oracle-research/                    # Research protocols
│   │   └── references/                     # Pricing, patterns, lessons
│   ├── oracle-diagram-generator/           # Draw.io + Python + Mermaid
│   ├── oci-drawio-icon-native/             # Icon-native validation
│   ├── oci-services-expert/                # OCI architecture
│   ├── oracle-adk/                         # Agent Development Kit
│   ├── oracle-agent-spec/                  # Open Agent Specification
│   └── oracle-infogenius/                  # Image generation (optional)
├── drawio/                                 # 67 .drawio templates
│   ├── meta-architectures/                 # 6 AI Factory architecture pages
│   ├── domain-architectures/               # 4 industry-specific architectures
│   ├── use-case-architectures/             # 37+ use-case diagrams
│   ├── tools/                              # Python validation + generation scripts
│   └── OCI Style Guide for Drawio/        # Official OCI diagram toolkit
├── clients/[CODE]/                         # Client work by codename
├── projects/hub/portals/                   # 11 industry portals, 86 pages
├── research/topics/                        # Research docs (never codename-linked)
└── docs/
    └── AI-ARCHITECT-TOOLKIT-GUIDE.md       # This guide
```

## Appendix B: MCP Configuration Template

Complete `.mcp.json` — copy to your project root:

```json
{
  "mcpServers": {
    "sqlcl": {
      "command": "sql",
      "args": ["-mcp"],
      "description": "Oracle ADB access (SQL, ORDS, Select AI, APEX)",
      "timeout": 120
    },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"],
      "description": "Create and edit Draw.io diagrams from XML, CSV, or Mermaid"
    }
  }
}
```

Add Nano Banana (oracle-infogenius images) and Playwright (browser testing) as needed.

---

*Version 2.0 — February 2026*
*For questions or contributions: Open an issue or PR on the repo.*
