# Oracle InfoGenius Skills

> AI Architect-grade visual generation for Oracle Cloud Infrastructure

## Overview

The Oracle InfoGenius skill family provides tiered image generation for Oracle architecture diagrams, using Google's Gemini image generation models via the Nano Banana MCP server.

## Skill Tiers

| Skill | Model | Resolution | Cost/Image | Best For |
|-------|-------|------------|------------|----------|
| `/oracle-infogenius-flash` | Gemini 2.5 Flash | 1024px | **$0.039** | Drafts, iterations, volume |
| `/oracle-infogenius-pro` | Gemini 3 Pro | 1K-2K | **$0.134** | Client presentations |
| `/oracle-infogenius-premium` | Gemini 3 Pro | 4K | **$0.24** | Print, large displays |

## Quick Selection Guide

```
┌─────────────────────────────────────────────────────────────────┐
│  CHOOSING THE RIGHT TIER                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  "I need quick drafts or many images"                          │
│       → /oracle-infogenius-flash ($0.039/image)                │
│                                                                 │
│  "I need client-ready presentation visuals"                    │
│       → /oracle-infogenius-pro ($0.134/image)                  │
│                                                                 │
│  "I need print-quality or 4K resolution"                       │
│       → /oracle-infogenius-premium ($0.24/image)               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Pricing Details

### Gemini 2.5 Flash Image (Flash Tier)
- **Model ID:** `gemini-2.5-flash-image`
- **Input:** $0.30 per 1M tokens (text/image)
- **Output:** $0.039 per image
- **Max Resolution:** 1024px
- **Speed:** Fast (~5-10 seconds)
- **Best For:** Rapid iteration, drafts, high volume

### Gemini 3 Pro Image (Pro & Premium Tiers)
- **Model ID:** `gemini-3-pro-image-preview`
- **Input:** $2.00 per 1M tokens
- **Output:**
  - 1K/2K images (up to 2048px): **$0.134/image**
  - 4K images (up to 4096px): **$0.24/image**
- **Features:** Extended thinking, web grounding
- **Best For:** Client presentations, final deliverables

## Usage Examples

### Flash Tier (Budget-Friendly)
```bash
/oracle-infogenius-flash Create a simple 3-tier OCI architecture
```
Parameters used:
```yaml
model_tier: "flash"
resolution: "high"  # Max 1024px
```

### Pro Tier (Recommended Default)
```bash
/oracle-infogenius-pro Create a 6-layer enterprise architecture for AI platform
```
Parameters used:
```yaml
model_tier: "pro"
resolution: "high"  # 1K-2K
thinking_level: "high"
enable_grounding: true
```

### Premium Tier (Maximum Quality)
```bash
/oracle-infogenius-premium Create a print-ready 4K conference poster
```
Parameters used:
```yaml
model_tier: "pro"
resolution: "4k"  # Up to 4096px
thinking_level: "high"
enable_grounding: true
```

## Quality Comparison

| Aspect | Flash | Pro | Premium |
|--------|-------|-----|---------|
| Text Rendering | Good | Excellent | Excellent |
| Complex Layouts | Acceptable | Good | Excellent |
| Detail Level | Medium | High | Maximum |
| Color Accuracy | Good | Excellent | Excellent |
| Print Quality | No | Yes (digital) | Yes (large format) |

## Cost Scenarios

| Scenario | Flash | Pro | Premium |
|----------|-------|-----|---------|
| 10 draft iterations | $0.39 | $1.34 | $2.40 |
| 5 client slides | $0.20 | $0.67 | $1.20 |
| 1 conference poster | $0.04 | $0.13 | $0.24 |
| Full deck (20 images) | $0.78 | $2.68 | $4.80 |

## Technical Notes

### Nano Banana MCP Server
These skills use the Nano Banana MCP server which wraps Google's Gemini image generation API:
- Supports aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4, etc.
- Supports negative prompts for exclusions
- Automatic file saving with thumbnails
- Grounding via Google Search (Pro only)

### No Free Tier for Image Generation
**Important:** Neither Flash nor Pro has a free tier for image generation. All usage incurs costs as documented above.

### Preview Model Notice
Gemini 3 Pro Image is currently in preview (`gemini-3-pro-image-preview`). Pricing and capabilities may change when it reaches GA.

## File Locations

```
.claude/skills/
├── README.md                          # This file
├── oracle-infogenius/                 # Main skill (Pro default)
│   └── skill.md
├── oracle-infogenius-flash/           # Budget tier
│   └── skill.md
├── oracle-infogenius-pro/             # Professional tier
│   └── skill.md
├── oracle-infogenius-premium/         # Maximum quality tier
│   └── skill.md
└── oracle-ai-architect-infogenius/    # Full architect workflow
    └── skill.md
```

## Related Skills

- `/oracle-ai-architect-infogenius` - Full architecture workflow with research validation
- `/oracle-work` - Oracle day job context activation

---

*Last Updated: January 2026*
*Part of the FrankX Oracle Work System*
