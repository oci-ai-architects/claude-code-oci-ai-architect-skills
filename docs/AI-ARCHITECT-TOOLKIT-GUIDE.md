# Oracle AI Architect Toolkit
## From Idea to Working Prototype — Complete Workflow Guide

> **For:** Oracle AI Architect Team
> **Version:** 3.0 — February 2026
> **Central Command:** `/oci-ai-architect` — your single entry point for everything below
> **Disclaimer:** Unofficial community project. Not affiliated with or endorsed by Oracle Corporation.

---

## 1. The Pipeline at a Glance

Every client engagement follows 8 phases. `/oci-ai-architect` routes you to the right skill at each step.

```
 INTAKE → DISCOVER → PRD → USER FLOWS → ARCHITECT → VISUALIZE → BUILD → DELIVER
   │         │        │        │           │           │          │        │
   ▼         ▼        ▼        ▼           ▼           ▼          ▼        ▼
 Scope    Research   Reqts    Journeys   OCI Design  Diagrams   Working   Package
 Client   Industry   MoSCoW   Personas   Services    Draw.io    Proto-    Audit
 Brief    Patterns   KPIs     Screens    BOM         D2/Img     type      Present
```

| # | Phase | Skill | What You Get |
|---|-------|-------|-------------|
| 0 | **Intake** | `/oci-ai-architect` | Structured brief, codename assignment |
| 1 | **Discover** | `/oracle-research` | OCI capabilities, existing solutions, industry patterns |
| 2 | **PRD** | Direct | MoSCoW requirements mapped to OCI services |
| 3 | **User Flows** | Draw.io MCP / D2 | Persona journeys, screen maps, critical paths |
| 4 | **Architect** | `/oci-services-expert` + `/oracle-sdd-generator` | Architecture + BOM + SDD |
| 5 | **Visualize** | Draw.io (3 tiers) / D2 / `/oracle-infogenius` | Editable diagrams or raster visuals |
| 6 | **Build** | Direct + ADB MCP | Working prototype with live data |
| 7 | **Deliver** | `/oracle-confidentiality` | Audited, presentation-ready package |

**For a complete end-to-end engagement:** `/oracle-solution-design` chains all phases automatically with quality gates.

**Total: 4-6 hours from blank page to working prototype with live database.**

---

## 2. What You Can Build

> **If you're new to the toolkit, start here.** These aren't hypothetical — they're complete solutions Claude builds end-to-end using the skills above + ADB MCP + Draw.io MCP.

### 2.1 Enterprise RAG Platform

Vector search + keyword search + reranking over your domain data.

```
Build an enterprise RAG platform on OCI for [domain — e.g., internal policy documents].

Architecture:
- Cohere Embed 4 for multimodal embeddings (text + images)
- Oracle AI Database 26ai with VECTOR(1024, FLOAT32) columns
- Cohere Rerank 3.5 for result quality scoring
- Cohere Command A for grounded generation with citations

Build me a working prototype:
- Single index.html, dark theme (#0D1117), Oracle Red accents (#C74634)
- Chat interface with streaming responses
- Source citations with relevance scores for every answer
- Hybrid search toggle: semantic / keyword / hybrid
- Connected to ADB via ORDS REST endpoints
- 15 sample documents with realistic [domain] content
- PROTOTYPE banner visible

Then create the Draw.io architecture diagram showing the full pipeline:
Data Sources → Chunking → Embedding → Vector Store → Retrieval + Rerank → Generation
```

**What you get:** A fully functional RAG chatbot with live Oracle database, editable architecture diagram, and 15 seeded documents — in about 90 minutes.

---

### 2.2 Graph RAG with Knowledge Graphs

Combine vector similarity with Oracle's native property graph engine.

```
Build a Graph RAG system on Oracle AI Database 26ai for [domain — e.g., pharmaceutical R&D].

Database layer (create via ADB MCP):
1. Relational tables: compounds, targets, pathways, publications, researchers
2. VECTOR(1024, FLOAT32) column on publications for semantic search
3. CREATE PROPERTY GRAPH research_graph linking all entities
4. Sample data: 20 compounds, 10 targets, 15 pathways, 30 publications, 8 researchers

Hybrid retrieval (implement both):
- VECTOR_DISTANCE for semantic search across publications
- PGQL queries for graph traversal: "Which compounds target pathway X and were
  studied by researcher Y?"
- Combined: Vector search → filter by graph relationships → rerank

Prototype:
- Interactive knowledge graph visualization using vis.js (force-directed layout)
- Click any node to see connected entities and AI-generated summary
- Search bar supporting both natural language and structured graph queries
- Side panel: vector search results with relevance scores
- Dark theme, PROTOTYPE banner, mobile responsive
- Cohere Command A for generating insights from combined graph + vector context
```

**What you get:** Interactive knowledge graph explorer with dual retrieval — something most teams spend months building.

---

### 2.3 Select AI Agent (In-Database AI)

Natural language to SQL using Oracle's built-in Select AI with 26ai's new Agent capabilities.

```
Set up Select AI Agent on Oracle AI Database 26ai.

Database setup (via ADB MCP):
1. Create OCI GenAI credential: DBMS_CLOUD.CREATE_CREDENTIAL
2. Create AI profile: DBMS_CLOUD_AI.CREATE_PROFILE using Cohere Command A
   connected to OCI GenAI endpoint in eu-frankfurt-1
3. Load sample schema: 5 tables for [domain — e.g., e-commerce]
   - customers (1000 rows), orders (5000), products (200), reviews (3000), inventory (200)
4. Enable Select AI: SELECT AI SHOWSQL "What were top 10 products last quarter?"

Prototype:
- Business intelligence chat interface
- User asks questions in plain English
- Shows: generated SQL, query results as interactive Chart.js visualizations
- Toggle between chart types: bar, line, pie, table
- Query history sidebar with re-run capability
- Auto-suggest: show 5 example questions the user can click
- Connected live to ADB — real queries, real results
- Dark theme, PROTOTYPE banner
```

**What you get:** A natural language BI tool running on live Oracle database — the demo that makes executives immediately understand AI value.

---

### 2.4 Multi-Agent Orchestration Platform

Coordinated AI agents with Oracle ADK patterns.

```
Design and prototype a multi-agent system using Oracle ADK patterns for [use case —
e.g., customer support automation].

Agent architecture (conductor pattern):
- OrchestratorAgent: Routes incoming requests, manages conversation state
- DataAgent: Queries ADB via Select AI for customer/order information
- AnalysisAgent: Uses Cohere Command A Reasoning for multi-step analysis
- ActionAgent: Executes approved actions (refund, escalate, schedule callback)
- ComplianceAgent: Validates all actions against policy rules before execution

Use Llama 4 Maverick for tool-calling (MoE architecture, best for agentic workflows).

Store in ADB:
- agent_conversations: Full conversation history with timestamps
- agent_actions: Every action taken, status, approval state
- agent_metrics: Response times, resolution rates, escalation %

Prototype:
- Real-time agent activity dashboard
- Live conversation view showing which agent is active
- Action queue with approve/reject buttons
- Metrics panel: avg resolution time, first-contact resolution %, agent utilization
- WebSocket-style updates (simulated with polling for prototype)
- 10 sample conversations pre-loaded showing different routing paths
- Dark theme, PROTOTYPE banner
```

**What you get:** A live multi-agent dashboard showing AI agents collaborating in real-time — the "future of enterprise AI" demo.

---

### 2.5 Intelligent Document Processing

End-to-end document AI with OCI Document Understanding + GenAI.

```
Build an intelligent document processing platform on OCI for [document type —
e.g., insurance claims].

Pipeline:
1. Upload: Drag-drop with file validation (PDF, PNG, JPEG)
2. Extract: OCI Document Understanding API — OCR + key-value extraction
3. Classify: Cohere Command A — document type, urgency, department routing
4. Enrich: Cohere Command A Reasoning — cross-reference against policy database
5. Index: Cohere Embed 4 → VECTOR column in AI Database 26ai
6. Search: Hybrid search (vector + keyword) across all processed documents

ADB schema (create via MCP):
- documents: id, filename, doc_type, status, confidence, extracted_json,
  embedding VECTOR(1024, FLOAT32), uploaded_at, processed_at
- extraction_results: doc_id, field_name, field_value, confidence
- processing_log: doc_id, step, status, duration_ms, error_msg

Prototype:
- Drag-drop upload zone with real-time processing animation (step-by-step progress)
- Extraction preview: show detected fields with confidence % color-coding
  (green >90%, yellow 70-90%, red <70%)
- Classification result with top-3 categories and probabilities
- Document search with hybrid mode toggle
- Processing metrics dashboard: docs/hour, avg confidence, error rate
- 10 pre-loaded sample [document type]s with realistic mock data
- Dark theme, Oracle Red accents, PROTOTYPE banner
```

---

### 2.6 GenAI Chat with Multi-Source RAG

Chat pulling from multiple knowledge bases with source-aware retrieval.

```
Build a multi-source GenAI chat for [domain — e.g., IT help desk].

Knowledge sources in AI Database 26ai (create all via ADB MCP):
1. documentation — product docs, 50 chunks, VECTOR(1024, FLOAT32)
2. faqs — common questions, 30 entries, VECTOR(1024, FLOAT32)
3. policies — company policies, 20 documents, VECTOR(1024, FLOAT32)
4. tickets — resolved support tickets, 40 entries, VECTOR(1024, FLOAT32)

Retrieval strategy:
- Intent classifier (Cohere Command A): route query to 1-2 relevant collections
- Per-collection VECTOR_DISTANCE search, top-5 each
- Cross-collection Cohere Rerank 3.5 to merge and rank all results
- Cohere Command A generation with source citations:
  "[answer text] (Source: policies/acceptable-use, relevance: 0.94)"

Conversation features:
- Conversation memory: last 10 turns stored in ADB conversation_history table
- Context window management: summarize old turns when context exceeds threshold
- Source transparency: expandable citation panel showing exact text chunks used

Prototype:
- Chat interface with streaming response animation
- Source panel: color-coded by collection (docs=blue, FAQs=green, policies=orange, tickets=purple)
- Conversation sidebar with history
- "How did I answer this?" button: shows retrieval pipeline breakdown
- Analytics: queries/day, collection hit rates, avg response quality
- 140 sample entries across 4 collections
- Dark theme, PROTOTYPE banner
```

---

## 3. Central Command: `/oci-ai-architect`

Your single entry point. Use it when you don't know which skill to invoke, or to kick off any workflow.

```
/oci-ai-architect

I need to [describe what you need — e.g., "build a document processing system
for insurance claims on OCI with AI classification and searchable archive"]
```

It routes your request to the optimal skill:

| Your Need | Routed To |
|-----------|-----------|
| Complete solution design | `/oracle-solution-design` (5-phase orchestrator) |
| OCI service selection / cost | `/oci-services-expert` |
| Research OCI capabilities | `/oracle-research` |
| Generate SDD document | `/oracle-sdd-generator` |
| Build OCI agents | `/oracle-adk` |
| Architecture diagrams | Draw.io workflow (see Section 6) |
| Architecture images | `/oracle-infogenius` (requires Nano Banana MCP) |
| Pre-delivery audit | `/oracle-confidentiality` |

### The Full Orchestrator: `/oracle-solution-design`

For complete client engagements, this runs the full 5-phase pipeline:

```
DISCOVER → ARCHITECT → VISUALIZE → PROTOTYPE → DELIVER
   │            │            │            │           │
 [Gate 1]   [Gate 2]    [Gate 3]    [Gate 4]    [Gate 5]
   │            │            │            │           │
Parallel    system-     Draw.io/     coder       Package
research    architect   infogenius   agent       + audit
agents      agent
```

Each phase has a quality gate. No phase starts until the previous gate passes. Research agents run in parallel for speed.

---

## 4. Skills & Activation

All skills live in `.claude/skills/` as SKILL.md files. They activate via slash commands or contextual triggers.

### Core Skills

| Skill | Command | What It Does | Phase |
|-------|---------|-------------|-------|
| **Oracle Solution Design** | `/oracle-solution-design` | 5-phase orchestrator with quality gates | All |
| **Oracle Research** | `/oracle-research` | Confidentiality-aware research + OCI pattern checks | Discover |
| **OCI Services Expert** | `/oci-services-expert` | Service selection + **mandatory** pricing verification | Architect |
| **Oracle SDD Generator** | `/oracle-sdd-generator` | 8-section Solution Design Document | Architect |
| **Oracle ADK** | `/oracle-adk` | Agent Development Kit scaffolding + patterns | Build |
| **Oracle Agent Spec** | `/oracle-agent-spec` | Framework-agnostic agent definitions (JSON/YAML) | Build |
| **Oracle Confidentiality** | `/oracle-confidentiality` | Pre-delivery audit with VETO power | Deliver |
| **OCI Draw.io Icon-Native** | *(auto for production diagrams)* | Ensures embedded icons, no mxgraph fallback | Visualize |

### Optional Skills

| Skill | Command | Dependency |
|-------|---------|------------|
| **Oracle InfoGenius** | `/oracle-infogenius` | Requires Nano Banana MCP server |
| **Oracle AI Architect InfoGenius** | `/oracle-ai-architect-infogenius` | Requires Nano Banana MCP server |

### Skill Chain

```
/oci-ai-architect (entry point — routes to the right skill)
    │
    ├── /oracle-solution-design (full engagement — chains everything below)
    │       ├── Phase 1 → /oracle-research (parallel research agents)
    │       ├── Phase 2 → /oci-services-expert + /oracle-sdd-generator
    │       ├── Phase 3 → Draw.io MCP or /oracle-infogenius
    │       ├── Phase 4 → /oracle-adk (if agents) + ADB MCP (if database)
    │       └── Phase 5 → /oracle-confidentiality (ALWAYS)
    │
    ├── Individual skills (for focused work outside full engagement)
    │       ├── /oci-services-expert → "What OCI services for [X]? Cost?"
    │       ├── /oracle-research → "Research [technology] on OCI"
    │       └── /oracle-adk → "Build an agent for [use case]"
    │
    └── Diagram workflows (see Section 6)
```

---

## 5. Setup: MCP Servers

Two MCP servers are essential. One is optional. All work with **every AI coding tool**.

### 5.1 Oracle ADB MCP (SQLcl)

Direct access to Oracle Autonomous Database. This is what makes prototypes real.

**Prerequisites:**
1. SQLcl 25.4+ installed (`sql -version`)
2. Wallet downloaded from OCI Console (ADB → DB Connection → Download Wallet)
3. Saved connection: `sql /nolog` → `conn -save MyADB -savepwd user/pass@adb_medium -wallet /path/to/Wallet`

**What it gives you:**

| Tool | Capability |
|------|-----------|
| `run-sql` | Execute any SQL — DDL, DML, queries. Results as CSV |
| `run-sqlcl` | SQLcl-specific: APEX exports, DBMS_CLOUD, Data Pump, the `AI` command |
| `schema-information` | Full schema introspection: tables, columns, constraints, relationships |
| `connect` / `disconnect` | Switch between saved connections (dev, test, prod) |
| `run-sql-async` | Long-running queries without timeout |

**Example — Create a RAG schema in 30 seconds:**
```
Connect to ADB and create this schema:

CREATE TABLE knowledge_base (
    id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
    title VARCHAR2(500) NOT NULL,
    content CLOB,
    source_collection VARCHAR2(50),
    embedding VECTOR(1024, FLOAT32),
    metadata JSON,
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP
);

CREATE SEARCH INDEX kb_hybrid_idx ON knowledge_base(content)
    PARAMETERS('SYNC(ON COMMIT)');

INSERT 20 sample rows for an IT help desk knowledge base across 4 collections:
documentation, faqs, policies, tickets. Make the content realistic and varied.
Verify with: SELECT source_collection, COUNT(*) FROM knowledge_base GROUP BY source_collection;
```

### 5.2 Draw.io MCP

Create and open editable architecture diagrams.

| Tool | Input | Best For |
|------|-------|---------|
| `open_drawio_xml` | Draw.io XML | Production architectures (Tier 3 — see Section 6) |
| `open_drawio_mermaid` | Mermaid syntax | Quick flowcharts, sequence diagrams (Tier 1) |
| `open_drawio_csv` | CSV data | Org charts, structured layouts |

### 5.3 Configuration (All AI Coding Tools)

**The JSON is identical for every tool** — only the file location changes.

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

| Tool | Config Location |
|------|----------------|
| **Claude Code** | `.mcp.json` in project root |
| **Cline** (VS Code) | VS Code Settings → Cline → MCP Servers |
| **Cursor** | `.cursor/mcp.json` |
| **Windsurf** | `.windsurf/mcp.json` |
| **OpenCode** | `opencode.json` or settings |
| **Codex** (OpenAI) | `codex_mcp.json` |
| **Gemini CLI** | `gemini_mcp_settings.json` |

**WSL variant** (if SQLcl runs inside WSL, not Windows):
```json
{
  "sqlcl": {
    "command": "wsl.exe",
    "args": ["-d", "Ubuntu-24.04", "--", "bash", "-lc", "sql -mcp"],
    "timeout": 120
  }
}
```

---

## 6. Architecture Diagrams: The Real Guide

> **Honest assessment:** Generating production-quality OCI architecture diagrams is complex. There is no magic one-liner. Here are the three approaches, ranked by reliability.

### Tier 1: Mermaid → Draw.io (Quick Drafts)

**When:** Quick flowcharts, sequence diagrams, user journeys, decision trees. NOT for detailed OCI architecture diagrams.

**How it works:** Write Mermaid syntax, open in Draw.io via MCP. Result is editable.

```
Create a Mermaid flowchart for the document processing pipeline and open it in Draw.io:

graph LR
    A[Document Upload] --> B{File Type?}
    B -->|PDF| C[OCR Engine]
    B -->|Image| D[Vision AI]
    C --> E[Extract Fields]
    D --> E
    E --> F[Classify Document]
    F --> G[Route to Department]
    G --> H[(AI Database 26ai)]
    H --> I[Search & Retrieve]
```

**Limitations:** No OCI icons. No layered architecture styling. No security/governance overlays. Good for process flows, not architecture.

**Prompt engineering tip:** Keep Mermaid diagrams to 15-20 nodes max. Beyond that, they become unreadable. For complex architectures, use Tier 2 or D2.

---

### Tier 2: Python Generators (Production Quality)

**When:** Client-facing architecture diagrams with proper OCI icons, layering, and professional polish. **This is the reliable path for production diagrams.**

**How it works:** Python scripts clone embedded OCI icon stencils from the official toolkit into new .drawio files. Icons render correctly in any environment — no library imports needed.

**Available generators (4,146 LOC across 9 tools):**

| Script | What It Builds |
|--------|---------------|
| `build_oci_coe_domain_architectures.py` | Industry-specific architectures (healthcare, automotive, db-migration, software-saas) |
| `build_ai_factory_meta_architecture.py` | 6-page AI Factory meta-architecture pack |
| `build_agentic_rag_diagram.py` | Agentic RAG architecture with icon-native stencils |
| `build_oci_coe_use_case_portfolio.py` | Multi-page use-case portfolio packs |
| `build_oci_coe_use_case_tracker.py` | CSV/markdown portfolio tracker with BOM data |

**Production workflow:**

```
Step 1 — Generate the diagram:

python3 drawio/tools/build_oci_coe_domain_architectures.py \
  --domain healthcare \
  --output drawio/domain-architectures/

Step 2 — Validate icon integrity (MANDATORY before sharing):

python3 drawio/tools/validate_drawio_icon_integrity.py \
  --file drawio/domain-architectures/OCI_AICoE_healthcare_Agentic_Architecture.drawio \
  --diagram "Healthcare Agentic Architecture"

# MUST report:
#   mxgraph_oci_refs=0         (no fallback icons)
#   VALIDATION: PASS

Step 3 — Optional: Run pack-level QA:

python3 drawio/tools/qa_oci_architecture_pack.py \
  --file drawio/OCI_AICoE_Hub_Domain_Architectures.drawio

Step 4 — Open in Draw.io for manual refinement, then share.
```

**Why this works:** The Python generators embed icon geometry as base64-encoded stencil data directly in the XML. No external library dependency. Icons render correctly whether you open the file in Draw.io desktop, web, VS Code extension, or embed in Confluence.

**Prompt to customize an existing template:**
```
Read the healthcare domain architecture template at
drawio/domain-architectures/OCI_AICoE_healthcare_Agentic_Architecture.drawio

Adapt it for a document processing use case:
- Replace Clinical Decision Support → Document Classification
- Replace Patient Data → Document Store
- Replace EHR Integration → ERP Integration
- Keep the OCI service layer structure (Security → Processing → Data → Presentation)
- Keep all embedded icon stencils intact
- Save as drawio/domain-architectures/OCI_AICoE_document_processing_Architecture.drawio

Then validate:
python3 drawio/tools/validate_drawio_icon_integrity.py --file <new_file> --diagram <name>
```

---

### Tier 3: Direct XML Generation (Advanced)

**When:** You need a completely custom architecture diagram not covered by existing templates. Requires understanding Draw.io XML structure.

**Why this is hard:**
1. **Icon embedding:** OCI icons must use `shape=stencil(...)` with base64-encoded geometry — NOT `shape=mxgraph.oci.*` (renders as red blocks without library)
2. **Z-ordering:** Edges (arrows) must be inserted before foreground elements in XML document order
3. **Clone geometry:** Icon groups have parent-child hierarchies; only the root gets absolute positioning, descendants use relative offsets
4. **Cell IDs:** Every `mxCell` needs a unique ID; parent references must be consistent

**If you must generate raw XML, use this pattern:**

```
Generate a Draw.io XML architecture diagram. CRITICAL RULES:

1. DO NOT use shape=mxgraph.oci.* — these require external libraries
2. Use simple labeled rectangles with professional styling instead of OCI icons
3. Use rounded=1;whiteSpace=wrap; for service boxes
4. Layer structure (top to bottom):
   - Security band: fillColor=#1a1a2e (dark), fontColor=#FFFFFF
   - Processing: fillColor=#16213e, fontColor=#FFFFFF
   - Data tier: fillColor=#0f3460, fontColor=#FFFFFF
   - Presentation: fillColor=#C74634 (Oracle Red), fontColor=#FFFFFF
5. Edges: orthogonal routing, strokeColor=#888888, endArrow=block
6. Overall: background=#0D1117 (dark), grid=0

Services to show:
[list your OCI services and data flows]

Open the result in Draw.io using open_drawio_xml.
```

**Important:** Tier 3 produces professional-looking diagrams with labeled boxes and color-coded layers. For actual OCI icons, use Tier 2 (Python generators) or manually add icons in Draw.io after opening.

---

### Alternative: D2 Language (No MCP Required)

**When:** You don't have Draw.io MCP, or you want version-controlled diagrams in text form. Better than Mermaid for architecture diagrams — supports layers, nested containers, and the TALA layout engine.

**Install:** `curl -fsSL https://d2lang.com/install.sh | sh -s --`

**Render:** `d2 architecture.d2 architecture.svg --layout=elk`

**Example — OCI RAG Architecture in D2:**

```d2
direction: down

security: Security & Governance {
  style.fill: "#1a1a2e"
  style.font-color: "#FFFFFF"

  waf: WAF
  apigw: API Gateway
  iam: IAM
  vault: Vault
  cloud-guard: Cloud Guard
}

processing: AI Processing Pipeline {
  style.fill: "#16213e"
  style.font-color: "#FFFFFF"

  ingest: Object Storage
  functions: OCI Functions
  doc-ai: Document Understanding
  genai: OCI GenAI {
    embed: Cohere Embed 4
    command: Cohere Command A
    rerank: Rerank 3.5
  }
}

data: Data Platform {
  style.fill: "#0f3460"
  style.font-color: "#FFFFFF"

  adb: AI Database 26ai {
    vectors: Vector Store
    graph: Property Graph
    relational: Relational Tables
  }
  obj: Object Storage (Raw Documents)
}

presentation: Presentation {
  style.fill: "#C74634"
  style.font-color: "#FFFFFF"

  app: Web Application
  api: REST API (ORDS)
  dash: Dashboard
}

security.apigw -> processing.functions: Incoming requests
processing.ingest -> processing.functions: New document event
processing.functions -> processing.doc-ai: Extract
processing.doc-ai -> processing.genai.embed: Embed
processing.genai.embed -> data.adb.vectors: Store
data.adb -> processing.genai.command: Retrieve + Generate
processing.genai.command -> presentation.api: Response
presentation.api -> presentation.app: Display
```

**Export options:** SVG, PNG, PDF. Embed SVGs directly in HTML portals.

**Prompt engineering for D2:**
```
Create a D2 architecture diagram for [use case] on OCI.

Requirements:
- 4 horizontal layers: Security, Processing, Data, Presentation
- Use dark fills with white text (see D2 style examples above)
- Oracle Red (#C74634) for the presentation layer
- Show data flow with labeled arrows
- Nest related services inside containers
- Save as diagrams/[name].d2

Then render:
d2 diagrams/[name].d2 diagrams/[name].svg --layout=elk
```

---

### Template Library: 89 Production .drawio Files

Don't start from scratch. We have templates for:

| Category | Count | What's Inside |
|----------|-------|--------------|
| **Meta-Architectures** | 6 | AI Factory: Logical, Physical, Execution, User Flows, Governance, Portal Map |
| **Domain Architectures** | 4 | Healthcare, Automotive, DB Migration, Software/SaaS |
| **Use-Case Architectures** | 60 | 10 per domain × 4 domains + 20 cross-domain |
| **OCI Reference Architectures** | 6 | Agentic AI, GenAI Enterprise, ERP Integration, Select AI, Multi-tenant, Integration Patterns |
| **Master Portfolios** | 3 | Multi-page packs (domain, use-case, AI Factory) |
| **OCI Style Guide** | 2 | Official OCI Architecture Diagram Toolkit v24.2 |

**Location:** `drawio/` directory with subdirectories.

**Prompt to find the right template:**
```
I need an architecture diagram for [use case] in [industry].

Check the drawio/ directory — which existing template is closest?
Show me the top 3 matches. Then clone the best one and customize
for my specific requirements:
[list your OCI services and data flows]

Validate the output with validate_drawio_icon_integrity.py.
```

---

## 7. Phase-by-Phase Deep Dive

> **Prompting principle:** At every phase, first **ASK** the AI for its reasoning, then **DIRECT** execution. 5 minutes of ASK saves hours of rework.

### Phase 0: Intake & Scoping

**Prompt:**
```
/oci-ai-architect

Starting a new engagement — codename K.

Context (conversation only, not in files):
- [Industry/domain]
- [Problem statement]
- [Scale: users, data volume, regions]
- [Timeline and budget constraints]
- [Key stakeholders and their concerns]

Structure the initial brief. What are the 5 most critical questions I should
answer before moving to discovery? What OCI capabilities are most likely relevant?
```

---

### Phase 1: Discover & Research

**Prompt:**
```
/oracle-research

Deep research for [use case] on OCI. Before you start:

1. What existing oracle-quickstart repos solve this? Check:
   - github.com/oracle-quickstart (Terraform modules)
   - github.com/oracle-quickstart/oci-ai-blueprints (GenAI on OKE)
   - github.com/oracle-devrel/technology-engineering (Solution patterns)
   - github.com/oracle-samples (Code samples)

2. Which OCI AI Blueprints are relevant? Decision tree:
   - Standard LLM inference? → vLLM Blueprint
   - Need full GenAI stack? → Llama Stack Blueprint
   - Fine-tuning? → LoRA Fine-Tuning Blueprint
   - Route optimization? → cuOPT Accelerator Pack
   - Enterprise reasoning? → AI-Q Accelerator Pack

3. OCI GenAI model selection for this workload:
   - What type of reasoning: simple extraction, complex multi-step, or agentic?
   - Multimodal needed? → Cohere Command A Vision or Llama 3.2 90B Vision
   - EU data residency? → Cohere series (EU deployable)
   - Budget-sensitive? → Gemini 2.5 Flash-Lite or Grok 3 Mini Fast

4. What are the 3 biggest technical risks for this type of project?
5. What compliance requirements apply to this domain?

Save findings to research/topics/[topic].md — no client references.
```

**Quality Gate 1:**
- [ ] Existing solutions checked (oracle-quickstart, AI Blueprints)
- [ ] Top 3 use cases identified with OCI service mapping
- [ ] Model selection justified with rationale
- [ ] Technical risks documented
- [ ] Zero client names in any file

---

### Phase 2: Product Requirements Document

**Prompt:**
```
Based on discovery findings, create a PRD for codename K.

MoSCoW prioritization:
MUST: [list critical requirements — these define MVP]
SHOULD: [list important but not blocking requirements]
COULD: [list nice-to-have features]
WON'T (this phase): [list explicitly deferred scope]

For each MUST requirement, map:
| Requirement | OCI Service | Effort (days) | Risk | Dependencies |

Non-functional requirements (check each):
- [ ] Security: encryption at rest/transit, IAM policies, network isolation
- [ ] Compliance: GDPR, industry-specific regulations, data residency
- [ ] Observability: logging, monitoring, alerting, tracing
- [ ] DR/HA: RTO/RPO targets, backup strategy, failover
- [ ] Performance: latency SLAs, throughput requirements, scaling triggers
- [ ] Cost: monthly budget, cost optimization levers, scaling cost model

What requirements am I missing for [domain]? What should I go back to the
client to clarify?
```

---

### Phase 3: User Flows & Journeys

**Prompt:**
```
Design user flows for [3-4 personas]:
1. [Persona 1 — primary user, e.g., "Data Analyst"]
2. [Persona 2 — decision maker, e.g., "VP Operations"]
3. [Persona 3 — administrator, e.g., "IT Admin"]

For each persona, create a Mermaid journey diagram showing:
- Entry point and trigger
- Each step with AI touchpoints highlighted
- Decision points and branches
- Success criteria / exit conditions
- Error/exception paths

Which persona's workflow is most critical to prototype first?
Where should AI augment (suggest) vs. automate (execute)?
What's the simplest happy path that demonstrates full value?

Open the most critical flow in Draw.io for refinement.
```

---

### Phase 4: Technical Architecture

**Prompt (this is the most important prompt in the entire pipeline):**
```
/oci-services-expert

Design the OCI architecture for [use case].

Requirements:
- [Scale: X users, Y documents/day, Z queries/hour]
- [Region: eu-frankfurt-1 (GDPR)]
- [Budget: <$X/month]
- [Availability: 99.X%]

Before designing, answer:
1. What are 2-3 valid architecture approaches? Compare on:
   cost | complexity | time-to-deploy | scalability | team skill required
2. Which approach has the fastest time-to-value?
3. Are there AI Blueprints that solve 80% of this? (CHECK FIRST)
4. What's the single biggest cost driver, and how would you optimize it?

For the recommended approach, deliver:
- Service selection with rationale for each choice
- Data flow diagram (ingestion → processing → storage → retrieval → presentation)
- Security architecture (IAM policies, encryption, network, audit)
- Bill of Materials with line items:
  | Service | SKU | Quantity | Unit Price | Monthly Cost | Source |
  Price source: oracle.com/cloud/price-list/ with verification date

Then generate the SDD:
/oracle-sdd-generator
Full 8-section Solution Design Document with 3 tiers (Basic/Advanced/Premium).
```

**Quality Gate 2:**
- [ ] Every service verified against official docs
- [ ] Pricing from oracle.com/cloud/price-list/ with date
- [ ] No blanket "X times cheaper" claims — specific model comparisons only
- [ ] AI Blueprints decision tree documented
- [ ] Security architecture complete
- [ ] BOM totals per tier

---

### Phase 5: Visualize

Choose your approach based on the situation:

| Situation | Use | Prompt |
|-----------|-----|--------|
| Quick internal review | D2 or Mermaid → Draw.io | "Create D2/Mermaid diagram of the architecture" |
| Client presentation (with OCI icons) | Python generators (Tier 2) | "Generate using build_oci_coe_domain_architectures.py" |
| Custom architecture (no template fits) | Draw.io XML (Tier 3) | "Generate Draw.io XML with colored layers, no mxgraph.oci.*" |
| Executive one-pager visual | `/oracle-infogenius` (needs Nano Banana) | "Architecture visual, dark theme, Oracle Red, NO logos" |
| Client wants to see the full template library | Clone from `drawio/` | "Find the closest template and customize" |

**Prompt for D2 (recommended for quick professional diagrams):**
```
Create a D2 architecture diagram for our [use case] architecture.

4 layers (top to bottom):
1. Security & Governance — dark navy (#1a1a2e)
   [list security services]
2. AI Processing Pipeline — medium navy (#16213e)
   [list processing services and flow]
3. Data Platform — deep blue (#0f3460)
   [list data services]
4. Presentation — Oracle Red (#C74634)
   [list presentation services]

Show data flow arrows between layers with labels.
Nest related services inside containers.
Save as diagrams/[name].d2 and render to SVG.
```

**Quality Gate 3:**
- [ ] ZERO Oracle logos (text labels only)
- [ ] Service names match official branding (AI Database 26ai, not 23ai)
- [ ] Architecture matches the SDD
- [ ] For .drawio: `validate_drawio_icon_integrity.py` → PASS
- [ ] Readable at presentation size

---

### Phase 6: Build (Working Prototype)

**Prompt:**
```
Build a working prototype for [solution name].

Tech stack:
- Single index.html with embedded CSS/JS (no build tools, no npm)
- Connected to Oracle ADB via ORDS REST endpoints (or mock data fallback)
- Dark theme (#0D1117 background), Oracle Red (#C74634) accents
- Mobile responsive (CSS grid/flexbox)

Core interaction (the "wow moment"):
[Describe the ONE interaction that best demonstrates AI value —
e.g., "user asks a question in natural language, sees the SQL generated,
results rendered as interactive chart, with source citations"]

Screens:
1. [Primary screen — the core workflow]
2. [Secondary screen — supporting view]
3. [Dashboard — metrics and activity]

Data:
- Create the ADB schema via MCP (tables, constraints, indexes)
- Insert [N] realistic sample records for [domain]
- Enable ORDS REST endpoints on key tables
- Verify with: SELECT COUNT(*) FROM [table];

Polish:
- Loading animations on AI-powered interactions
- Smooth transitions between screens
- PROTOTYPE banner always visible
- Every button either works or says "Coming in Phase 2"
- NO Oracle logos anywhere
```

**ADB setup prompt (run before building the prototype):**
```
Connect to ADB and set up the prototype database:

1. Create tables:
[your DDL — include VECTOR columns where needed]

2. Create indexes:
CREATE VECTOR INDEX [name] ON [table](embedding)
    ORGANIZATION NEIGHBOR PARTITIONS
    DISTANCE COSINE;

3. Insert sample data:
[N] rows of realistic [domain] data with proper relationships
between tables. Include diverse examples that demonstrate
different AI classification/search outcomes.

4. Enable ORDS:
BEGIN
    ORDS.ENABLE_SCHEMA(p_enabled => TRUE);
    ORDS.ENABLE_OBJECT(p_object => '[TABLE_NAME]');
END;

5. Verify:
- SELECT table_name, num_rows FROM user_tables;
- Test ORDS endpoint: show me the curl command
```

**Quality Gate 4:**
- [ ] Core workflow works end-to-end
- [ ] Processing states visible (loading, progress, complete)
- [ ] No dead links or broken buttons
- [ ] PROTOTYPE banner displayed
- [ ] No real customer data
- [ ] Schema created and verified in ADB

---

### Phase 7: Deliver & Audit

**Prompt:**
```
/oracle-confidentiality

Package and audit deliverables for codename K:

Expected structure:
clients/K/
  README.md                      # Status + role ONLY (no industry/scope)
  deliverables/
    docs/SOLUTION-DESIGN.md      # Full SDD (from Phase 4)
    docs/BOM.md                  # Bill of Materials with pricing sources
    images/architecture.svg      # Architecture diagram (from Phase 5)
    diagrams/architecture.drawio # Editable Draw.io file
    diagrams/architecture.d2     # D2 source (if used)
    prototype/index.html         # Working demo (from Phase 6)

Audit checklist:
1. grep -r for real customer names → MUST return zero
2. README.md contains codename only — no industry, scope, or employee count
3. All images are logo-free
4. BOM pricing cites oracle.com/cloud/price-list/ with verification date
5. Prototype loads standalone (no external dependencies)
6. No competitor attacks — OCI capabilities focus only
7. McKinsey test: Would you present this to a Fortune 500 CEO?
```

**Quality Gate 5:**
- [ ] Confidentiality audit: PASS
- [ ] All files in correct structure
- [ ] Prototype loads standalone
- [ ] BOM pricing verified
- [ ] McKinsey test: YES

---

## 8. OCI Model Selection Matrix

Use this when choosing models for architecture designs.

| Use Case | Primary Model | Alternative | Why |
|----------|---------------|-------------|-----|
| Complex reasoning | Cohere Command A Reasoning | Gemini 2.5 Pro | 256K context, multi-step logic |
| Multimodal (images+text) | Cohere Command A Vision | Llama 3.2 90B Vision | Charts, diagrams, documents |
| Agentic workflows | Llama 4 Maverick | Grok 4.1 Fast | Tool-calling, MoE architecture |
| Coding | Grok Code Fast 1 | Llama 4 Maverick | Code-optimized |
| RAG / Retrieval | Cohere Command R (08-2024) | Cohere Command A | RAG-optimized, 128K context |
| Embeddings (multimodal) | Cohere Embed 4 | Embed Multilingual 3 | Text + image embeddings |
| Reranking | Cohere Rerank 3.5 | — | Relevance scoring |
| Speed / Budget | Gemini 2.5 Flash-Lite | Grok 3 Mini Fast | High-volume, low-cost |
| EU data residency | Cohere Command A series | — | EU region deployable |
| Long context (2M+) | Grok 4.1 Fast | Gemini 2.5 Pro | Massive document processing |
| Fine-tuning | Llama 3.3 70B (LoRA) | Cohere (T-few) | Dedicated AI Clusters |

**Decision flow:**
1. Data residency required? → Cohere (EU deployable)
2. Fine-tuning needed? → Llama (LoRA) or Cohere (T-few)
3. Multimodal? → Cohere Vision, Llama Vision, or Gemini
4. Agentic/tool-calling? → Llama 4 Maverick or Grok 4.1 Fast
5. Budget-constrained? → Flash-Lite or Mini Fast variants
6. Coding focus? → Grok Code Fast 1

---

## 9. Hub Portal Integration

### The AI CoE Hub

We maintain an **AI Center of Excellence Hub** with 11 industry portals and 86+ solution pages. Use these as starting templates.

```
AI CoE Hub (projects/hub/index.html)
    ├── Healthcare (10 use cases)      ├── Energy & Utilities (10)
    ├── Financial Services (10)        ├── Public Sector (10)
    ├── Telecommunications (10)        ├── AEC & Consulting
    ├── Automotive (10)                ├── AI CoE Patterns
    ├── Retail & Consumer (10)         └── Database Migration (6 agents)
    └── Chemical/IP (Patent AI)
```

**Using hub portals for client work:**
```
Check the AI CoE Hub — which portal and use case is closest to
codename K's requirements? Show me the top 3 matches.

Then clone the best match and create a custom portal page that links:
1. Executive overview (from SDD)
2. Architecture diagram (from Phase 5)
3. Interactive prototype (from Phase 6)
4. Roadmap (from SDD phased approach)
5. Cost summary (from BOM)

Keep the Oracle Redwood design system styling.
```

---

## 10. Quick Reference

### Commands at a Glance

| Command | When |
|---------|------|
| `/oci-ai-architect` | **Start here** — routes to the right skill |
| `/oracle-solution-design` | Full 5-phase engagement with quality gates |
| `/oracle-research` | Research OCI capabilities for a use case |
| `/oci-services-expert` | OCI service selection + pricing verification |
| `/oracle-sdd-generator` | Generate Solution Design Document |
| `/oracle-adk` | Build agents with Oracle ADK |
| `/oracle-confidentiality` | Pre-delivery audit (VETO power) |
| `/oracle-infogenius` | AI-generated architecture images *(optional — needs Nano Banana)* |

### MCP Servers

| Server | Purpose | Key Tools |
|--------|---------|-----------|
| **SQLcl (ADB)** | Oracle database access | `run-sql`, `schema-information`, `connect` |
| **Draw.io** | Editable diagrams | `open_drawio_xml`, `open_drawio_mermaid` |
| **Nano Banana** | Image generation *(optional)* | `generate_image` |
| **Playwright** | Browser testing *(optional)* | Validate prototypes |

### Mandatory Checks (Every Engagement)

| Check | When | How |
|-------|------|-----|
| Existing solutions | Before designing | oracle-quickstart, AI Blueprints |
| Pricing verification | Before any cost claim | oracle.com/cloud/price-list/ with date |
| Model selection | Architecture phase | OCI GenAI Model Selection Matrix (Section 8) |
| Logo compliance | Every visual | NO Oracle logos — text labels only |
| Confidentiality | Before delivery | `/oracle-confidentiality` audit |
| Draw.io validation | Production diagrams | `validate_drawio_icon_integrity.py` |

### Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| Jump straight to "build me X" | ASK first: "What are 2-3 approaches? Compare trade-offs" |
| "OCI is 80x cheaper" | Cite specific model comparison with source and date |
| Include Oracle logos in diagrams | Text labels only, Oracle Red (#C74634) accents |
| Build from scratch without checking | Check oracle-quickstart and AI Blueprints FIRST |
| Use `mxgraph.oci.*` in Draw.io | Tier 2 Python generators, or Tier 3 with `shape=stencil()` |
| Store client names in files | Codenames only, context in conversation |
| Generate production diagrams from Mermaid | Mermaid for drafts, Tier 2/D2 for production |
| Skip the ASK prompt | 5 minutes of ASK saves hours of rework |
| Assume you know OCI pricing | VERIFY at oracle.com/cloud/price-list/ — models change monthly |

---

## Appendix A: File Structure

```
oracle-work/
├── .claude/
│   ├── commands/
│   │   └── oci-ai-architect.md          # Central orchestrator command
│   └── skills/
│       ├── oracle-solution-design/      # 5-phase workflow orchestrator
│       ├── oracle-sdd-generator/        # SDD document generation
│       ├── oracle-confidentiality/      # Pre-delivery audit
│       ├── oracle-research/             # Research protocols + references
│       ├── oracle-diagram-generator/    # Diagram generation patterns
│       ├── oci-drawio-icon-native/      # Icon-native validation
│       ├── oci-services-expert/         # OCI architecture + pricing
│       ├── oracle-adk/                  # Agent Development Kit
│       ├── oracle-agent-spec/           # Open Agent Specification
│       └── oracle-infogenius/           # Image generation (optional)
├── drawio/                              # 89 .drawio templates
│   ├── meta-architectures/             # 6 AI Factory pages
│   ├── domain-architectures/           # 4 industry architectures
│   ├── usecase-architectures/          # 60 use-case diagrams
│   ├── oci ai architectures/          # 6 OCI reference architectures
│   ├── tools/                          # 9 Python tools (4,146 LOC)
│   └── OCI Style Guide for Drawio/   # Official toolkit v24.2
├── clients/[CODE]/                     # Client work by codename
├── projects/hub/portals/              # 11 industry portals, 86+ pages
├── research/topics/                   # Research docs (never codename-linked)
└── docs/
    └── AI-ARCHITECT-TOOLKIT-GUIDE.md  # This guide
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

Add Nano Banana (for `/oracle-infogenius` images) and Playwright (for browser testing) as needed.

---

*Version 3.0 — February 2026*
*Central command: `/oci-ai-architect`*
*For questions or contributions: Open an issue or PR on the repo.*
