---
description: Start confidential research session with web search, synthesis, and project linking
thinking: false
---

# Research Session Mode

Conduct research for Oracle consulting while maintaining strict confidentiality.

## Research Protocol

### Step 1: Define Scope

1. **Topic**: What are you researching?
2. **Purpose**: Learning / Problem-solving / Customer preparation / Certification
3. **Project Link**: Related to a project codename or General knowledge?
4. **Depth**: Quick overview / Moderate / Deep dive

### Step 2: Conduct Research

Using WebSearch with confidentiality:

**Search Strategy:**
- Use current year for latest information
- Focus on: Oracle, OCI, enterprise AI, cloud architecture
- Cross-reference multiple sources
- Prioritize: Oracle docs, official blogs, reputable tech sources

**Confidentiality Rules:**
- NEVER include customer names in search queries
- Search generic patterns, not specific implementations
- Example: "OCI OKE networking best practices" NOT "Customer XYZ OKE setup"

### Step 3: Synthesize Findings

I create structured research documents:

```markdown
# [Topic Title]

**Researched:** YYYY-MM-DD
**Purpose:** [Learning/Problem-solving/etc.]
**Project Link:** [Codename/General]

## Key Findings

### Finding 1: [Title]
[Summary]
- Source: [URL]
- Relevance: [How this applies]

## Synthesis
[Cross-cutting insights from multiple sources]

## Action Items
- [ ] [What to do with this knowledge]
- [ ] [How to apply to current projects]
```

### Step 4: Link to Projects

If research is relevant to a project:
1. Reference the project codename
2. Suggest how findings might help (abstractly)
3. Store in project-specific research folder

## Quick Research Syntax

- `research: [topic]` → Quick overview
- `deep dive: [topic]` → Comprehensive research
- `[CODENAME] research: [topic]` → Project-linked research

### Examples

```
research: OCI GPU shapes for LLM inference
deep dive: Kubernetes service mesh patterns for enterprise
A research: AI for network optimization use cases
```

## Output Location

Configure in your workspace:
- General: `research/topics/[topic-slug].md`
- Project-specific: `research/projects/[CODENAME]/[topic-slug].md`

---

**Start researching:** What topic would you like to explore?
