---
description: Generate AI Architect-grade Oracle Cloud architecture visuals
allowed-tools: Read, Write, WebSearch, WebFetch
argument-hint: [topic] [--style executive|technical|futuristic|isometric]
---

## Oracle InfoGenius - AI Architect Visual Generation

You are generating a professional Oracle Cloud architecture visual. Apply the AI Architect thinking framework:

1. **Research** - Validate all OCI services against current documentation
2. **Architect** - Determine audience, select style, design layers
3. **Compose** - Build prompt with Oracle brand standards
4. **Generate** - Call Nano Banana MCP with optimal settings
5. **Validate** - Check quality against rubric (target >85%)

### Available Styles

| Style | Use Case |
|-------|----------|
| `executive` | Customer presentations, proposals, C-Suite |
| `technical` | Architecture reviews, design docs, engineers |
| `futuristic` | Innovation demos, tech showcases |
| `isometric` | Solution overviews, marketing, sales |

### Your Task

1. Read the skill: `skills/oracle-infogenius/SKILL.md`
2. Research current OCI service capabilities
3. Select appropriate style (default: executive)
4. Generate image with Nano Banana MCP
5. Save to `projects/deliverables/images/`

### Oracle Brand Requirements

- **Primary**: Oracle Red `#C74634`
- **Text**: Oracle Black `#312D2A`
- **AI Layer**: Purple `#7B1FA2`
- **Security**: Green `#388E3C`
- **Data**: Orange `#F57C00`

### Example

```
/oracle-infogenius "Marketing Automation Multi-Agent Platform" --style executive
```
