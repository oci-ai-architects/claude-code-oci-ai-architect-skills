# Oracle InfoGenius Flash

> **Cost-Optimized Visual Generation** - $0.039/image
> Uses Gemini 2.5 Flash Image for fast, affordable architecture visuals

---

## When to Use

- Draft iterations and exploration
- Internal team reviews
- High-volume generation (10+ images)
- Quick prototypes
- Budget-conscious projects

## Model Configuration

```yaml
model_tier: "flash"
model: "gemini-2.5-flash-image"
resolution: "high"  # Max 1024px
cost_per_image: "$0.039"
```

## Capabilities

- Fast generation (~5-10 seconds)
- Good text rendering
- Simple to moderate complexity diagrams
- 1024px maximum resolution
- No grounding (web search)
- No extended thinking

## Limitations

- Lower detail than Pro
- Text may be smaller
- Complex layouts may simplify
- Not ideal for final client deliverables

## Usage

When generating images, ALWAYS use these parameters:

```
model_tier: "flash"
resolution: "high"
```

## Prompt Guidelines for Flash

Since Flash has less reasoning capability, prompts should be:
- More explicit and structured
- Simpler layouts (avoid 6+ layer architectures)
- Fewer text elements
- Clear color specifications

## Example Invocation

```
/oracle-infogenius-flash Create a simple 3-tier architecture diagram showing Users → Application → Database
```

---

*Part of the Oracle AI Architect InfoGenius System*
*Flash Tier: Speed & Cost Optimized*
