# Oracle Solution Design Orchestrator

> **Replaces:** claude-flow swarm orchestration for solution design workflows
> **Method:** Native Claude Code Task agents with parallel dispatch + quality gates
> **Confidentiality:** Conversation-only context model. Zero persistent state.

## When to Use This Skill

Invoke when the user needs:
- A complete solution design for a customer engagement
- A Solution Design Document (SDD) for an OCI-based solution
- An architecture recommendation with BOM and visuals
- A prototype or interactive demo for a customer presentation

**Trigger:** `/oracle-solution-design` or when user says "solution design", "SDD", "architecture for [client]"

---

## The 5-Phase Workflow

```
  DISCOVER --> ARCHITECT --> VISUALIZE --> PROTOTYPE --> DELIVER
     |             |             |              |            |
  [Gate 1]     [Gate 2]     [Gate 3]       [Gate 4]    [Gate 5]
     |             |             |              |            |
  Parallel     system-       nano-banana    coder         Package
  research     architect     + infogenius   agent         + audit
  agents       agent
```

### Phase Execution Model

Each phase uses native Claude Code capabilities. No daemon, no vector DB, no external processes.

| Phase | Agent Strategy | Tools Used |
|-------|---------------|------------|
| DISCOVER | Parallel Task(researcher) x2-3 | WebSearch, WebFetch, Grep, Read |
| ARCHITECT | Task(system-architect) + Task(researcher) | Read, WebFetch, Write |
| VISUALIZE | Direct (main context) | Nano Banana MCP, Read |
| PROTOTYPE | Task(coder) or direct | Write, Edit, Bash |
| DELIVER | Direct (main context) | Write, Read, Bash |

---

## Phase 1: DISCOVER

### Objective
Gather all information needed to design the solution. Run research in parallel.

### Parallel Agent Dispatch Pattern

Launch 2-3 Task agents simultaneously:

**Agent 1 -- OCI Capabilities Research:**
```
Task(subagent_type="researcher")
"Research OCI services for [use case]. Check:
 1. OCI GenAI models available (docs.oracle.com/iaas/Content/generative-ai/)
 2. Relevant oracle-quickstart repos (github.com/oracle-quickstart)
 3. OCI AI Blueprints if GenAI workload
 Return: service list with capabilities and limitations."
```

**Agent 2 -- Industry/Domain Research:**
```
Task(subagent_type="researcher")
"Research [industry/domain] AI patterns:
 1. Common architecture patterns for [use case]
 2. Compliance/regulatory requirements
 3. Industry benchmarks and KPIs
 Return: requirements matrix and constraints."
```

**Agent 3 -- Pricing and Competitor Landscape (if needed):**
```
Task(subagent_type="researcher")
"Research current pricing for [specific OCI services]:
 1. Verify at oracle.com/cloud/price-list/
 2. Check OCI Cost Estimator for complex scenarios
 3. Note any commitment discounts or free tiers
 Return: verified pricing with sources and dates."
```

### Confidentiality Gate
Before proceeding, verify:
- No real customer names in any output
- All context uses codename only
- Research results are generic (industry patterns, not client-specific)

### Output
Mental model of the solution. No document yet. Just validated understanding.

### Quality Gate 1: Discovery Complete
- Core use cases identified (top 3)
- OCI services mapped to requirements
- Constraints documented (compliance, timeline, budget)
- Existing OCI patterns checked (oracle-quickstart, AI Blueprints)

---

## Phase 2: ARCHITECT

### Objective
Design the technical architecture with OCI service selection and cost estimation.

### Agent Strategy

**Primary: System Architect Agent**
```
Task(subagent_type="system-architect")
"Design an OCI architecture for [use case] with these requirements:
 [paste discovery results]

 Deliver:
 1. OCI service selection with rationale for each choice
 2. Architecture tiers (Basic / Advanced / Premium)
 3. Data flow: ingestion > processing > storage > retrieval > presentation
 4. Security architecture: IAM, encryption, network isolation
 5. Integration points and APIs"
```

**Support: Pricing Verification**
```
Task(subagent_type="researcher")
"Verify pricing for these OCI services: [list from architect]
 Source: oracle.com/cloud/price-list/
 Return: Monthly cost estimate by tier with line items."
```

### MANDATORY Checks Before Finalizing Architecture
1. AI Blueprints decision tree -- Does an existing blueprint cover this? (See CLAUDE.md)
2. Model selection -- Use the OCI GenAI Model Selection Matrix (See CLAUDE.md)
3. Pricing claims -- NEVER say "X times cheaper" without specific model comparison
4. Service availability -- Confirm services exist in target OCI region

### Document Generation

Generate the SDD in clients/[CODE]/ using /oracle-sdd-generator skill.

### Quality Gate 2: Architecture Validated
- Every OCI service verified against official docs
- Pricing confirmed via oracle.com/cloud/price-list/ (not from memory)
- No blanket cost comparison claims
- Existing patterns checked (oracle-quickstart, technology-engineering)
- Architecture follows OCI Well-Architected Framework principles
- Confidentiality audit passed (no client names, codename only)

---

## Phase 3: VISUALIZE

### Objective
Create architecture diagrams that are logo-free and technically accurate.

### Direct Execution (Main Context)
Visual generation stays in the main context for interactive refinement:

1. Invoke /oracle-infogenius or Nano Banana directly
2. Mandatory prompt elements:
   - "NO Oracle logos -- text labels only"
   - Oracle Red (#C74634) for accents
   - Dark background for professionalism
   - All service names must match official branding
3. Draft then Refine pattern:
   - Flash ($0.039) for initial draft
   - Review and adjust prompt
   - Pro ($0.134) for final version only after draft approved

### Recommended Visual Set

| Image | Audience | Focus |
|-------|----------|-------|
| Master Architecture | Technical + Executive | Full OCI stack, all tiers |
| User Journey | Executive | 4-5 step flow, business outcomes |
| Data Flow | Technical | Ingestion to Processing to Storage to Retrieval |
| Tier Comparison | Commercial | Side-by-side Basic/Advanced/Premium |

### Quality Gate 3: Visuals Compliant
- ZERO Oracle logos in any image
- Service names match official branding (26ai not 23ai)
- No spelling errors in diagrams
- Readable at presentation size (1920x1080 minimum)
- Architecture matches the SOLUTION-DESIGN.md

---

## Phase 4: PROTOTYPE

### Objective
Create an interactive HTML prototype the customer can experience.

### Agent Strategy

For complex prototypes:
```
Task(subagent_type="coder")
"Build an interactive HTML prototype for [solution name]:
 Requirements:
 - Single index.html with embedded CSS/JS (no build tools)
 - Simulated [core workflow] with mock data
 - Processing states (loading animations, progress bars)
 - AI insights panel with simulated responses
 - Mobile responsive
 - PROTOTYPE banner clearly visible
 - Oracle Red (#C74634) accents, dark theme
 - NO real customer data -- all mock/synthetic"
```

For simple prototypes: Build directly in main context.

### Prototype Quality Standards
- One core workflow, executed perfectly
- Every element has obvious purpose
- No placeholder content, no broken buttons
- Demo/prototype clearly labeled
- Mock data is realistic but obviously synthetic

### Quality Gate 4: Prototype Functional
- Core interaction works end-to-end
- Processing states visible (loading, progress)
- No broken buttons or dead links
- PROTOTYPE/DEMO banner displayed
- No real customer data anywhere
- Mobile responsive (at minimum, not broken on mobile)

---

## Phase 5: DELIVER

### Objective
Package everything for customer presentation.

### Output Structure
```
clients/[CODE]/
  SOLUTION-DESIGN.md           # Full SDD
  deliverables/
    images/
      architecture.png         # Master architecture (logo-free)
      user-journey.png         # Executive flow
      data-flow.png            # Technical detail
      tier-comparison.png      # Commercial comparison
    prototype/
      index.html               # Interactive demo
    docs/
      DISCOVERY.md             # Requirements captured
      BOM.md                   # Bill of Materials
  README.md                    # Project overview (codename only)
```

### Final Confidentiality Audit
Before any delivery:
- grep for real customer names in all output files -- MUST return zero
- Solution name is generic or codename-based
- No internal Oracle pricing beyond published list prices
- No competitor attacks -- only OCI capability focus
- README.md contains ONLY: status, role, codename -- no industry/scope

### Quality Gate 5: Delivery Ready
- All files in correct structure
- README complete with codename only
- Images are logo-free (visual inspection)
- Prototype loads and works standalone
- BOM pricing verified against official sources
- Would McKinsey present this to a Fortune 500 CEO? Yes/No

---

## Quick Reference: Agent Routing Matrix

| Need | Agent | Why Not Other? |
|------|-------|----------------|
| OCI service research | Task(researcher) | Web search + fetch access |
| Competitor/market research | Task(researcher) | Web search access |
| Architecture design | Task(system-architect) | Architecture patterns expertise |
| Code review of prototype | Task(reviewer) | Code quality focus |
| Build prototype | Task(coder) | Implementation focus |
| Deep codebase exploration | Task(Explore) | Fast file search |
| Multi-step planning | Task(Plan) | Architecture planning |
| Pricing verification | Task(researcher) | Needs web access |

## Anti-Patterns

| Do Not Do This | Do This Instead |
|---------------|----------------|
| Run all phases sequentially with no parallelism | Parallel research agents in Phase 1 |
| Skip pricing verification | ALWAYS verify at oracle.com/cloud/price-list/ |
| Include Oracle logos in visuals | Text labels only, Oracle Red accents |
| Persist client context to files | Conversation-only context, codename in files |
| Use claude-flow daemon for orchestration | Native Task agents -- zero infrastructure |
| Generate final visuals on first attempt | Flash draft first, Pro only after approval |
| Build complex prototype without coder agent | Delegate to Task(coder) for complex HTML/JS |
| Deliver without confidentiality audit | Always grep for real names before delivery |

---

## Integration with Other Skills

| Phase | Complementary Skill | When to Invoke |
|-------|---------------------|---------------|
| DISCOVER | /oracle-research | Deep OCI service investigation |
| ARCHITECT | /oci-services-expert | Service selection + pricing |
| ARCHITECT | /oracle-sdd-generator | Full SDD document generation |
| VISUALIZE | /oracle-infogenius | Tiered image generation |
| VISUALIZE | /oracle-ai-architect-infogenius | Full validation pipeline |
| PROTOTYPE | /oracle-adk | If agent-based prototype needed |
| DELIVER | /oracle-confidentiality | Final audit before handoff |

---

*Version: 1.0 | Created: 2026-02-09 | Replaces: claude-flow swarm orchestration*
