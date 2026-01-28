# Oracle InfoGenius Pro

> **Professional Visual Generation** - $0.134/image
> Uses Gemini 3 Pro Image for high-quality architecture visuals

---

## When to Use

- Client presentations
- Executive meetings
- Technical documentation
- Architecture reviews
- Final deliverables (digital)

## Model Configuration

```yaml
model_tier: "pro"
model: "gemini-3-pro-image-preview"
resolution: "high"  # 1K-2K (up to 2048px)
thinking_level: "high"
enable_grounding: true
cost_per_image: "$0.134"
```

## Capabilities

- High-quality output
- Excellent text rendering
- Complex multi-layer architectures
- Up to 2048px resolution
- Web search grounding for accuracy
- Extended thinking for better prompt understanding
- Accurate layout following

## Best For

- Oracle Cloud architecture diagrams
- Enterprise system blueprints
- Executive presentation slides
- Technical deep-dive visuals
- Multi-component flows

## Usage

When generating images, ALWAYS use these parameters:

```
model_tier: "pro"
resolution: "high"
thinking_level: "high"
enable_grounding: true
```

## Prompt Guidelines for Pro

Pro model understands complex prompts:
- Can handle 6-layer enterprise architectures
- Supports detailed component descriptions
- Follows Oracle brand color specifications
- Renders multiple text labels accurately

## Example Invocation

```
/oracle-infogenius-pro Create a 6-layer enterprise architecture for AI-powered patent analysis with OCI services
```

---

*Part of the Oracle AI Architect InfoGenius System*
*Pro Tier: Quality & Detail Optimized*
