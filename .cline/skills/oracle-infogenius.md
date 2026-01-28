# Oracle InfoGenius - AI Architect Visual Generation

You generate **enterprise-grade, technically-validated Oracle Cloud architecture visuals** that meet Senior AI Architect standards.

## When to Use This Skill
- Creating OCI architecture diagrams
- Generating presentation visuals for customer engagements
- Building technical documentation with imagery
- Producing brand-compliant Oracle content

## Quality Principles

Every image must be:
- **Research-Grounded** - Validated against Oracle documentation
- **Technically Accurate** - Correct service names, capabilities
- **Brand-Compliant** - Official Oracle colors, typography
- **Zero Text Errors** - Perfect spelling, no truncation
- **Presentation-Ready** - Professional quality

## Oracle Brand Colors

| Purpose | Color | Hex |
|---------|-------|-----|
| Primary | Oracle Red | `#C74634` |
| AI/Agents | Purple | `#7B1FA2` |
| Security | Green | `#388E3C` |
| Data | Amber | `#F59E0B` |
| Integration | Cyan | `#0EA5E9` |

## Current Service Naming (January 2026)

| Service | Correct Name | NEVER Use |
|---------|--------------|-----------|
| Database | Oracle AI Database 26ai | 23ai, 23c |
| GenAI LLM | Cohere Command A (256K) | Command R, Command R+ |
| GenAI Vision | Cohere Command A Vision | Command Vision |
| Embeddings | Cohere Embed 4 | Embed v3 |
| Agents | OCI GenAI Agent Hub | just "Agent Hub" |
| Integration | Oracle Integration Cloud (OIC) | just "Integration" |
| Documents | Oracle Document Understanding | OCI Vision |

## Visual Generation Pipeline

```
RESEARCH → ARCHITECT → COMPOSE → GENERATE → VALIDATE
```

### Step 1: RESEARCH (Always)
Before any visual, validate current Oracle naming and features:
```
WebSearch("OCI {service} features capabilities 2026")
```

### Step 2: COMPOSE PROMPT

**MANDATORY Text Quality Block:**
```
TEXT QUALITY REQUIREMENTS (CRITICAL - ZERO TOLERANCE):
- All text must be perfectly spelled with zero typos
- Use complete words only - NEVER truncate
- Professional English grammar throughout
- Technical terms must match official Oracle naming exactly
```

### Step 3: GENERATE

Using image generation tools with:
- aspect_ratio: "16:9" (presentations) or "1:1" (social)
- negative_prompt: "blurry text, typos, misspellings, truncated words"
- Always enable grounding for accuracy

## Architecture Visual Types

### 1. Solution Architecture
- 3-5 layers (presentation, application, data, infrastructure)
- Service icons with labels
- Data flow arrows
- Security boundaries

### 2. Data Flow Diagram
- Source systems → Processing → Storage → Analytics
- Clear direction indicators
- Integration points highlighted

### 3. Comparison Matrix
- Side-by-side feature comparison
- Clear headers and rows
- Checkmarks and ratings

### 4. Journey/Timeline
- Sequential steps
- Milestones and phases
- Progress indicators

## Image Quality Tiers

| Tier | Cost | Resolution | Best For |
|------|------|------------|----------|
| Flash | $0.039 | 1024px | Drafts, iterations |
| Pro | $0.134 | 1K-2K | Client presentations |
| Premium | $0.24 | 4K | Print, large displays |

## Output Directory
```
/projects/deliverables/images/
```

## Trademark Policy

- **DO NOT** include official Oracle logos
- **DO** use text labels like "Oracle Cloud" or "OCI"
- **DO** use brand-inspired colors
- **DO** reference official service names accurately
