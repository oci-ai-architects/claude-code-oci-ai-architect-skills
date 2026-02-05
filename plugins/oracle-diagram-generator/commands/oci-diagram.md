---
description: Generate a professional OCI architecture diagram
allowed-tools: Read, Write, Bash(python:*)
argument-hint: [architecture-type] [output-format]
---

## Context

You are generating an OCI architecture diagram. The user wants a professional diagram with correct Oracle styling.

Available architecture types:
- `rag` - RAG/AI platform with vector search
- `three-tier` - Classic web application
- `microservices` - OKE-based microservices
- `data-lake` - Analytics and data platform
- `multi-agent` - AI agent factory
- `hybrid` - On-prem + OCI hybrid

Available output formats:
- `drawio` - Draw.io XML file (default)
- `python` - Python diagrams library code
- `mermaid` - Mermaid.js markdown

## Your Task

1. If no architecture type specified, ask the user what they want to diagram
2. Read the oracle-diagram-generator skill for templates: `plugins/oracle-diagram-generator/skills/SKILL.md`
3. Generate the diagram in the requested format
4. Save to a file with appropriate extension (.drawio, .py, or .md)
5. Provide instructions for viewing/running the output

## Output Requirements

- Use Oracle Red (#C74634) for primary OCI services
- Include cost estimates where applicable
- Add proper labels and connections
- Follow Oracle icon naming conventions (mxgraph.oci.*)

## Example Invocations

```
/oci-diagram rag drawio
/oci-diagram three-tier python
/oci-diagram multi-agent mermaid
```
