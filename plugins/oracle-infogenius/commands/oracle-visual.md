---
description: Generate professional OCI architecture visuals using AI
allowed-tools: Read, ToolSearch, mcp__nanobanana__generate_image
argument-hint: [description] [--style=technical|executive|simple] [--size=1920x1080]
---

## Context

You are generating a professional visual for Oracle Cloud Infrastructure. Use the oracle-infogenius skill for brand guidelines and visual patterns.

## Your Task

1. Read the skill: `plugins/oracle-infogenius/skills/SKILL.md`
2. Understand the requested visual from the user's description
3. Construct an optimized prompt following Oracle brand guidelines:
   - Oracle Red (#C74634) for primary services
   - Clean, minimalist enterprise design
   - Clear labels and data flow arrows
4. Use the nanobanana MCP server to generate the image
5. Return the image with metadata

## Prompt Construction Template

```
Create a professional [TYPE] diagram for Oracle Cloud Infrastructure.

Subject: [USER_DESCRIPTION]

Style Requirements:
- Clean enterprise design with Oracle branding
- Primary color: Oracle Red (#C74634)
- Secondary: Dark gray (#312D2A) for text
- Background: White or light gray
- Modern, flat design with subtle shadows

Layout:
- [horizontal/vertical/radial] flow
- Clear visual hierarchy
- Service icons with labels
- Data flow arrows

Resolution: [SIZE]
Format: Professional presentation quality
```

## Example Invocations

```
/oracle-visual "RAG platform with vector search and multi-agent orchestration"
/oracle-visual "Three-tier web application" --style=executive
/oracle-visual "Data lakehouse architecture" --size=1920x1080
```
