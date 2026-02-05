---
name: Oracle InfoGenius
description: AI Architect-grade visual generation for OCI with research grounding and brand compliance
version: 1.0.0
keywords: [oracle, oci, visuals, images, infographics, ai-architect, gemini, brand]
triggers:
  - "create infographic"
  - "generate visual"
  - "oracle diagram image"
  - "architecture visual"
mcp_required: [nanobanana]
---

# Oracle InfoGenius

## When to Use This Skill

**Activate this skill when:**
- Creating professional OCI architecture visuals for presentations
- Generating infographics for customer proposals
- Building visual documentation with Oracle branding
- Need research-grounded visuals (not generic stock images)

**Use `/oracle-visual` command to generate an image.**

**Don't use when:**
- Need editable diagrams (use `oracle-diagram-generator` for Draw.io/Mermaid)
- Creating simple flowcharts (use Mermaid directly)
- Internal working documents (text is faster)

---

## Purpose

Generate AI Architect-grade visuals for Oracle Cloud Infrastructure that are:
1. **Research-grounded** - Based on actual OCI architecture patterns
2. **Brand-compliant** - Uses Oracle visual identity
3. **Professional** - Suitable for customer presentations
4. **Accurate** - Reflects real service relationships

## Oracle Visual Identity

### Brand Colors
```
Primary:
- Oracle Red: #C74634 (primary accent)
- Oracle Black: #312D2A (text, headers)
- White: #FFFFFF (backgrounds)

Secondary:
- Light Gray: #F5F5F5 (backgrounds)
- Medium Gray: #747775 (secondary text)
- Blue Accent: #1A73E8 (links, highlights)
```

### Typography
- **Headings:** Oracle Sans, Poppins fallback
- **Body:** Inter, system sans-serif fallback
- **Code:** JetBrains Mono, Consolas fallback

### Visual Style
- Clean, minimalist layouts
- Generous whitespace
- Flat design with subtle shadows
- Icon-based service representation
- Clear visual hierarchy

## Generation Patterns

### Pattern 1: Architecture Overview
```
Prompt Template:
"Create a professional architecture diagram showing [DESCRIPTION].
Style: Clean enterprise design with Oracle branding.
Colors: Oracle Red (#C74634) for primary services, gray for supporting.
Layout: [horizontal/vertical/radial] flow.
Include: Service labels, data flow arrows, cost annotations.
Resolution: 1920x1080 for presentations."
```

### Pattern 2: Comparison Infographic
```
Prompt Template:
"Create a comparison infographic showing [OPTION A] vs [OPTION B].
Style: Split layout with Oracle branding.
Include: Key metrics, pros/cons, cost comparison.
Format: Side-by-side columns with icons.
Target: Executive audience."
```

### Pattern 3: Process Flow
```
Prompt Template:
"Create a process flow diagram showing [PROCESS].
Style: Step-by-step numbered flow.
Colors: Oracle Red for active steps, gray for completed.
Include: Decision points, parallel paths, outcomes.
Format: Horizontal timeline or vertical steps."
```

### Pattern 4: Data Architecture
```
Prompt Template:
"Create a data architecture diagram showing [DATA FLOW].
Style: Lakehouse/medallion architecture.
Layers: Bronze → Silver → Gold with clear labels.
Include: Data sources, transformations, consumers.
OCI Services: Show specific service icons."
```

## OCI Service Icons

### Compute
- VM instances: Server/computer icon
- OKE: Kubernetes wheel
- Functions: Lambda symbol / function icon
- Container Instances: Container box

### Database
- Autonomous Database: Database cylinder with sparkle
- MySQL HeatWave: Dolphin + flame
- NoSQL: Document stack

### AI/ML
- Generative AI: Brain/neural network
- Data Science: Flask/beaker
- AI Services: Eye/speech/document icons

### Storage
- Object Storage: Bucket icon
- Block Volume: Disk stack
- File Storage: Folder

### Networking
- VCN: Cloud outline
- Load Balancer: Balance scale
- API Gateway: Gateway arch

## Command Usage

### Basic Generation
```bash
/oracle-visual "RAG platform architecture with OCI services"
```

### With Specifications
```bash
/oracle-visual "Multi-agent factory" --style=technical --size=1920x1080
```

### For Presentations
```bash
/oracle-visual "Three-tier web app" --format=presentation --audience=executive
```

## Best Practices

### Research First
1. Understand the actual architecture before visualizing
2. Verify service names and relationships
3. Check current OCI pricing for cost annotations
4. Use official Oracle terminology

### Visual Hierarchy
1. Most important element largest/centered
2. Data flows left-to-right or top-to-bottom
3. Group related services visually
4. Use color to indicate categories

### Accessibility
1. Sufficient contrast (WCAG AA minimum)
2. Don't rely solely on color for meaning
3. Include text labels for all icons
4. Alt text for screen readers

## Integration with MCP

### Nano Banana Server
This skill requires the Nano Banana MCP server for image generation:

```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "uvx",
      "args": ["nanobanana-mcp-server@latest"],
      "env": {
        "GEMINI_API_KEY": "${GEMINI_API_KEY}"
      }
    }
  }
}
```

### Generation Flow
1. Skill constructs optimized prompt
2. Calls nanobanana `generate_image` tool
3. Returns image with metadata
4. Optionally saves to file

## Quality Checklist

Before finalizing visuals:

**Accuracy:**
- [ ] Service names match official OCI terminology
- [ ] Connections reflect actual data/network flows
- [ ] Cost estimates from current pricing page
- [ ] Architecture matches documented pattern

**Visual Quality:**
- [ ] Oracle brand colors applied correctly
- [ ] Text is readable at presentation size
- [ ] Icons are consistent style
- [ ] Layout is balanced and clean

**Professional Standards:**
- [ ] No placeholder text visible
- [ ] All labels complete and accurate
- [ ] Appropriate for target audience
- [ ] Suitable for customer presentations

**Accessibility:**
- [ ] Color contrast meets WCAG AA
- [ ] Icons have text labels
- [ ] Not dependent on color alone

## Resources

**Oracle Brand:**
- [OCI Graphics Library](https://docs.oracle.com/en-us/iaas/Content/General/Reference/graphicsfordiagrams.htm)
- [Oracle Brand Guidelines](https://www.oracle.com/corporate/pressroom/brand/)

**MCP Integration:**
- [Nano Banana MCP](https://github.com/anthropics/nano-banana)
- [MCP Server Setup](https://modelcontextprotocol.io/)

---

*Generate professional, research-grounded visuals that represent Oracle Cloud Infrastructure accurately and beautifully.*
