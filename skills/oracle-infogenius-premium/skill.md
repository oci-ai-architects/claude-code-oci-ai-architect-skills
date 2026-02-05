# Oracle InfoGenius Premium

> **Maximum Quality Visual Generation** - $0.24/image
> Uses Gemini 3 Pro Image at 4K for print-ready architecture visuals

---

## When to Use

- Large format printing (posters, banners)
- High-resolution displays
- Marketing materials
- Conference booth graphics
- Publication-quality diagrams
- Zoom-in detail requirements

## Model Configuration

```yaml
model_tier: "pro"
model: "gemini-3-pro-image-preview"
resolution: "4k"  # Up to 4096px
thinking_level: "high"
enable_grounding: true
cost_per_image: "$0.24"
```

## Capabilities

- Maximum 4K resolution (4096x4096)
- Sharpest text rendering
- Finest detail preservation
- Print-ready quality
- Web search grounding
- Extended thinking
- Perfect for large displays

## Best For

- Conference presentations (large screens)
- Printed posters and banners
- Marketing collateral
- Publication in reports/whitepapers
- High-DPI displays
- Zoom-in demonstrations

## Usage

When generating images, ALWAYS use these parameters:

```
model_tier: "pro"
resolution: "4k"
thinking_level: "high"
enable_grounding: true
```

## Prompt Guidelines for Premium

Same as Pro, but optimize for detail:
- Include fine-grained visual elements
- Specify small text that needs to be readable
- Add subtle gradients and shadows
- Request crisp icon details

## Example Invocation

```
/oracle-infogenius-premium Create a print-ready 4K enterprise architecture poster for Oracle AI platform
```

## Cost Consideration

At $0.24/image, use Premium only when:
- Output will be printed or displayed large
- Maximum quality is required
- Budget allows for premium pricing

For digital-only use, Pro tier ($0.134) is usually sufficient.

---

*Part of the Oracle AI Architect InfoGenius System*
*Premium Tier: Maximum Quality for Print & Large Display*
