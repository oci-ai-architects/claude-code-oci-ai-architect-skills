# Visual Architecture Patterns Guide

> **Purpose:** Defines how architecture diagrams should be structured, validated, and generated for the OCI AI Architect skills ecosystem. Every visual must be architecturally accurate before it is aesthetically polished.

## Principles

1. **Architecture first, aesthetics second** — A wrong diagram that looks pretty is worse than a rough sketch that's correct
2. **Every label must be defensible** — If someone asks "why is X in the Y column?", you must have an answer grounded in how the system actually works
3. **Iterate cheap, finalize expensive** — Use Flash tier ($0.039) for drafts, Pro ($0.134) only after architecture review
4. **No stale data in visuals** — No hardcoded pricing, version numbers that will age, or claims that need periodic verification

## Generation Workflow

```
1. DEFINE architecture (text/ASCII first)
   ↓
2. VALIDATE against reference patterns below
   ↓
3. GENERATE at Flash tier (draft)
   ↓
4. REVIEW with user — check labels, flow, accuracy
   ↓
5. ITERATE at Flash if changes needed
   ↓
6. FINALIZE at Pro tier (approved architecture only)
```

**Cost discipline:** A single Pro image is 3.4x the cost of Flash. Never go straight to Pro without validating the architecture.

---

## Pattern: Enterprise RAG Platform

### Reference Sources
- [Oracle RAG Reference Architecture](https://docs.oracle.com/en/solutions/implement-rag-oci/index.html)
- [OCI GenAI Agents RAG Service](https://blogs.oracle.com/ai-and-datascience/oci-generative-ai-agents-rag-service)
- [oracle-devrel/oci-rag-vectordb](https://github.com/oracle-devrel/oci-rag-vectordb)

### Correct Pipeline Stages

A RAG system has **two distinct flows**: ingestion (batch/offline) and query (real-time). A single left-to-right diagram should accurately represent the query-time flow, with ingestion shown as a secondary path or separate diagram.

**Query-time flow (primary):**

```
USER QUERY → EMBED → RETRIEVE → RERANK → GENERATE → RESPONSE
```

**Ingestion flow (secondary):**

```
DATA SOURCES → PROCESS → CHUNK → EMBED → INDEX (Vector Store)
```

### Stage Definitions

| Stage | What Happens | OCI Service | NOT This |
|-------|-------------|-------------|----------|
| **Data Sources** | Raw data origins | OCI Object Storage, DB, APIs, SaaS | Don't list non-OCI services as primary (no "S3", no "SharePoint") |
| **Processing** | Extract, clean, chunk documents | OCI Document Understanding, OCI Functions | Not "Ingestion" (too vague) |
| **Embedding** | Convert text/images to vectors | OCI Generative AI + Cohere Embed 4 | Embedding is a specific step, not a service category |
| **Vector Store** | Store and index vectors | Oracle AI Database 26ai + AI Vector Search | Not "Storage" (too generic). DB is THE differentiator |
| **Retrieval** | Semantic search + reranking | AI Vector Search (query) + Cohere Rerank 3.5 | Reranking is retrieval, NOT orchestration |
| **Generation** | LLM synthesizes answer from context | Cohere Command A / Command A Reasoning | Generation is NOT orchestration — it's the answer step |
| **Applications** | End-user interfaces | Chat UIs, enterprise portals, Slack/Teams bots | Not "API Gateway" (that's infrastructure, not an app) |

### Common Mistakes

| Mistake | Why It's Wrong | Correct |
|---------|---------------|---------|
| Putting Rerank under "Orchestration" | Reranking scores retrieval relevance — it's search, not orchestration | Put under "Retrieval" |
| Putting Command A under "Orchestration" | The LLM generates the answer — that's "Generation" | Separate "Generation" stage |
| "Orchestration" as a catch-all | Orchestration means coordinating multi-step agent workflows (GenAI Agents). Don't use it for single-pass RAG | Only use for agentic patterns |
| API Gateway in "Application" | API Gateway is networking/infrastructure | Show actual user-facing apps |
| Hardcoded pricing in visuals | Goes stale. $0.19/OCPU was Jan 2025, may change | Never include prices in diagrams |

---

## Pattern: Multi-Agent Orchestration

### Correct Stages

```
TRIGGER → ROUTER → SPECIALIST AGENTS → TOOLS/ACTIONS → SYNTHESIS → OUTPUT
```

| Stage | What Happens | OCI Service |
|-------|-------------|-------------|
| **Trigger** | User request or event | API Gateway, OCI Events, Chat interface |
| **Router** | Classifies intent, selects agent | OCI GenAI Agents (Select AI Agent) |
| **Agents** | Specialized task execution | ADK agents, MCP-connected tools |
| **Tools** | External actions (DB query, API call, code exec) | OCI Functions, Database, REST APIs |
| **Synthesis** | Combine agent outputs | Cohere Command A (summarization) |
| **Output** | Formatted response to user | Application layer |

---

## Pattern: Data Pipeline / Lakehouse

### Correct Stages

```
SOURCES → INGEST → TRANSFORM → STORE → ANALYZE → SERVE
```

| Stage | OCI Service |
|-------|-------------|
| **Sources** | Object Storage, Streaming (Kafka), GoldenGate |
| **Ingest** | OCI Data Integration, OCI Functions |
| **Transform** | OCI Data Flow (Spark), OCI Data Science |
| **Store** | Oracle AI Database 26ai, Autonomous Data Warehouse |
| **Analyze** | OCI GenAI, Oracle Analytics Cloud |
| **Serve** | API Gateway, OCI Functions, Applications |

---

## Visual Standards

### Dark Theme (Default)

| Element | Color | Hex |
|---------|-------|-----|
| Canvas background | Dark navy | `#0D1117` |
| Component cards | Slate | `#1E293B` |
| Section headers | Oracle Red on dark | `#C74634` on `#1E293B` |
| Primary text | White | `#FFFFFF` |
| Secondary text | Light gray | `#94A3B8` |
| Arrows/connectors | Light gray or white | `#CBD5E1` |
| Accent (DB/Vector) | Amber/gold | `#F59E0B` |

### Layout Rules

1. **Flow direction:** Left-to-right for pipelines, top-to-bottom for stacks
2. **Max columns:** 7 (beyond this, text becomes unreadable at README width)
3. **Column headers:** ALL CAPS, red background, short labels (1-2 words)
4. **Component boxes:** Rounded corners, subtle border, icon + label
5. **Arrows:** Simple, unidirectional, no curved spaghetti
6. **Whitespace:** Generous — cramped diagrams look amateur

### Text Rules

1. **Service names:** Must match Oracle documentation exactly
2. **No pricing:** Never hardcode costs into visuals
3. **No version numbers that age:** Use "Oracle AI Database 26ai" (the brand name includes the version). Don't add extra version qualifiers
4. **Labels must be justified:** Every box label should answer "what role does this play in the architecture?"

### Trademark Compliance

- NO official Oracle logos
- NO Oracle "O" symbol
- YES to text labels ("Oracle Cloud", "OCI")
- YES to brand-inspired colors (#C74634)
- YES to official service names

---

## Validation Checklist

Before any visual is committed to the public repo:

```
ARCHITECTURE ACCURACY
[ ] Every stage label correctly describes what happens at that stage
[ ] Services are placed in the right stage (not catch-all buckets)
[ ] Data flow direction makes technical sense
[ ] No services listed that don't exist on OCI
[ ] Service names match current Oracle documentation

VISUAL QUALITY
[ ] Text is readable at 80% width in a GitHub README
[ ] No spelling errors
[ ] Dark background with Oracle Red accents
[ ] Clean layout with adequate whitespace
[ ] No glow effects, 3D, or clip-art aesthetics

COMPLIANCE
[ ] No Oracle logos
[ ] No hardcoded pricing
[ ] No competitor service names as primary data sources
[ ] Disclaimer present in repo (DISCLAIMER.md)

PROCESS
[ ] Architecture validated in text/ASCII before image generation
[ ] Draft generated at Flash tier first
[ ] User approved architecture before Pro generation
```

---

## Version History

| Date | Change |
|------|--------|
| 2026-02-05 | Initial version — RAG, Multi-Agent, Data Pipeline patterns |

---

*Maintained by the OCI AI Architects community*
