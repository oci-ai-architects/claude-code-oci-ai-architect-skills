---
description: Start a source-backed research session on an OCI or AI topic, linked to a study lab
thinking: false
---

# Research Session

Research an OCI, cloud architecture or AI topic for independent study, using public sources.

**Do not submit confidential engagement data.** Research questions and notes must not contain
customer or client names, employer-internal material, credentials or tenancy details. Ask about
the pattern, never about a specific organisation's systems.

## Research protocol

### Step 1: Define scope

1. **Topic**: what are you researching?
2. **Purpose**: learning, a lab problem, certification or writing
3. **Lab link**: a fictional lab label, or general knowledge
4. **Depth**: quick overview, moderate or deep dive

### Step 2: Conduct research

Use WebSearch:

- Include the current year for recent information
- Cross-reference several sources
- Prefer the official OCI documentation, official blogs and reputable technical sources
- Search for generic patterns, for example "OCI OKE private endpoint networking"

### Step 3: Synthesise findings

Create a structured research note:

```markdown
# [Topic title]

**Researched:** YYYY-MM-DD
**Purpose:** [learning / lab problem / certification / writing]
**Lab link:** [lab label or general]

## Key findings

### Finding 1: [title]
[Summary]
- Source: [URL]
- Relevance: [how this applies to the lab]

## Synthesis
[Cross-cutting insights from several sources]

## Next steps
- [ ] [What to try in the lab]
```

### Step 4: Link to a lab

If the research applies to a lab, reference its label and store the note in that lab's folder.

## Quick research syntax

- `research: [topic]`: quick overview
- `deep dive: [topic]`: comprehensive research
- `[LAB] research: [topic]`: lab-linked research

### Examples (fictional)

```
research: OCI GPU shapes for LLM inference
deep dive: Service mesh options on OKE
lab-rag research: Hybrid keyword and vector search in Oracle Database
```

## Output location

Configure in your workspace:
- General: `research/topics/[topic-slug].md`
- Lab-specific: `research/labs/[LAB]/[topic-slug].md`

---

**Start researching:** what topic would you like to explore?
