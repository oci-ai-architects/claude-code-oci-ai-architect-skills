# Validated OCI Diagram Prompt Templates

These prompts have been tested and validated to produce high-quality Oracle-branded architecture diagrams using AI image generation (Gemini/nano-banana MCP).

---

## Template 1: Enterprise Platform (Horizontal Layout)

**Use for:** General OCI platform architectures, customer presentations

```
Professional Oracle Cloud Infrastructure (OCI) architecture diagram for an Enterprise AI Platform.

STYLE: Clean technical diagram, white background, professional enterprise style like Oracle documentation. NOT a 3D render, NOT isometric. Flat 2D technical diagram with clean lines.

LAYOUT: Horizontal layered architecture from left to right:
- Left side: Users/Internet
- Center: OCI services in logical groupings
- Right side: Data layer

COMPONENTS (use simple clean icons, NOT emojis):
1. NETWORK LAYER: Load Balancer icon, API Gateway
2. COMPUTE LAYER: Kubernetes cluster (OKE) with 3 container nodes
3. AI LAYER: "OCI Generative AI" service box, "[Model Name]" label
4. DATA LAYER: Database cylinder labeled "Autonomous Database 23ai", Object Storage bucket icon

CONNECTIONS: Clean straight arrows showing data flow between components

COLOR SCHEME - Oracle Brand:
- Primary: Oracle Red (#C74634) for main service boxes
- Secondary: Teal (#2d5967) for secondary elements
- Background: Pure white
- Text: Dark gray (#312D2A)
- Subtle light gray (#f5f4f2) for grouping containers

TEXT LABELS: Clear sans-serif font, include:
- Title: "[Your Architecture Name]"
- Service names on each component
- "VCN" label for the network boundary

NO: Dark backgrounds, neon colors, 3D effects, gradients, emojis, cartoon style
```

**Recommended settings:**
- Aspect ratio: `16:9`
- Model: `pro`
- Resolution: `high`
- Negative prompt: `dark background, neon, 3D render, isometric, cartoon, emoji, gradient, glossy, futuristic sci-fi, abstract`

---

## Template 2: RAG Platform (Vertical Layout)

**Use for:** RAG architectures, data processing pipelines, vertical flow diagrams

```
Professional Oracle Cloud Infrastructure architecture diagram, enterprise documentation style.

TITLE: "[Your Title]" in bold dark text at top

STYLE: Flat 2D technical diagram, pure white background (#FFFFFF), clean enterprise documentation style matching Oracle Architecture Center. Simple geometric icons, no 3D effects.

LAYOUT: Top-to-bottom layered architecture within a rounded rectangle boundary labeled "OCI Region - [region-name]"

LAYERS (top to bottom):
1. TOP: Cloud icon and "Users" label, arrow pointing down to Load Balancer
2. INGESTION LAYER (light gray container): "OCI Streaming" box, "OCI Functions" box - both in Oracle Red (#C74634) with white text
3. AI LAYER (light gray container): Large "OCI Generative AI" box in Oracle Red, sub-labels "[Embed Model]" and "[Chat Model]"
4. DATA LAYER (light gray container): "Autonomous Database 23ai" cylinder in Oracle Red, "Object Storage" bucket icon in Oracle Red
5. BOTTOM: "OCI Observability" box with "Logging Analytics" label

CONNECTIONS: Thin dark gray (#312D2A) arrows showing data flow between layers

BRANDING:
- All OCI service boxes: Oracle Red (#C74634) fill with white text
- Container backgrounds: Very light gray (#f5f4f2)
- All text: Dark charcoal (#312D2A)
- Border: Subtle gray stroke around region boundary

Small "ORACLE" text badge in top right corner, Oracle Red background with white text
```

**Recommended settings:**
- Aspect ratio: `3:4` (vertical)
- Model: `pro`
- Resolution: `high`
- Negative prompt: `dark background, neon, 3D, isometric, cartoon, emoji, gradient, glossy, colorful rainbow, blue theme, green theme`

---

## Template 3: Multi-Agent Orchestration

**Use for:** AI agent architectures, agentic systems, supervisor patterns

```
Professional Oracle Cloud Infrastructure multi-agent AI architecture diagram.

TITLE: "[Your Title]" in bold dark text

STYLE: Flat 2D technical diagram, pure white background, Oracle enterprise documentation style. Clean geometric shapes, no 3D.

ARCHITECTURE (hierarchical, top to bottom):

TOP SECTION - "Agent Hub":
- Large rounded rectangle labeled "OCI Generative AI Agent Hub" in Oracle Red (#C74634) with white text
- Subtitle: "[Pattern Name]"

MIDDLE SECTION - "Specialist Agents" (row of N boxes):
- Box 1: "[Agent 1 Name]" - Oracle Red
- Box 2: "[Agent 2 Name]" - Oracle Red
- Box 3: "[Agent 3 Name]" - Oracle Red
- Box 4: "[Agent 4 Name]" - Oracle Red
- All with small brain/AI icon and white text

BOTTOM LEFT - "Tools Layer":
- Rounded container with light gray background
- Contains: "[Tool 1]", "[Tool 2]", "[Tool 3]" boxes in teal (#2d5967)

BOTTOM RIGHT - "Data Layer":
- Database cylinder: "Autonomous Database 23ai" in Oracle Red
- Bucket icon: "Object Storage" in Oracle Red

CONNECTIONS:
- Arrows from Agent Hub down to each Specialist Agent
- Dashed lines from Agents to Tools
- Solid lines from Tools to Database

FOOTER: Small metrics bar showing "[Metric 1] | [Metric 2] | [Metric 3]"

ORACLE badge in top right corner
```

**Recommended settings:**
- Aspect ratio: `16:9`
- Model: `pro`
- Resolution: `high`
- Negative prompt: `dark background, neon, 3D, isometric, cartoon, emoji, gradient, glossy, futuristic, sci-fi`

---

## Color Reference

Always use these exact colors for Oracle brand consistency:

| Element | Color | Hex |
|---------|-------|-----|
| OCI Services (primary) | Oracle Red | `#C74634` |
| Tools/Secondary | OCI Teal | `#2d5967` |
| Text | Dark Charcoal | `#312D2A` |
| Borders | Gray | `#9e9892` |
| Container backgrounds | Light Gray | `#f5f4f2` |
| Canvas | White | `#FFFFFF` |

---

## Negative Prompt (Always Include)

```
dark background, neon, 3D render, isometric, cartoon, emoji, gradient, glossy, futuristic sci-fi, abstract, colorful rainbow
```

---

## Quality Checklist

Before using generated diagram:

- [ ] White/light gray background (no dark themes)
- [ ] Oracle Red (#C74634) used for all OCI services
- [ ] ORACLE badge visible
- [ ] Clear readable labels
- [ ] No emojis
- [ ] Proper icons (database cylinder, bucket, etc.)
- [ ] Clean connection lines
- [ ] Logical data flow direction

---

## MCP Tool Usage

```python
# Using nano-banana MCP
mcp__nanobanana__generate_image(
    prompt="[Use template above]",
    aspect_ratio="16:9",  # or "3:4" for vertical
    model_tier="pro",
    resolution="high",
    negative_prompt="dark background, neon, 3D, isometric, cartoon, emoji, gradient, glossy",
    output_path="/path/to/output.png"
)
```

---

*Validated: January 2026*
*These templates produce consistent Oracle-branded diagrams*
