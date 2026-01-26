---
description: Design multi-agent orchestration pattern for OCI
allowed-tools: Read, Write
argument-hint: [use-case] [--pattern=conductor|pipeline|swarm]
---

## Context

You are designing a multi-agent orchestration pattern for Oracle Cloud Infrastructure using Oracle ADK.

## Your Task

1. Read the skill: `plugins/agentic-orchestration/skills/SKILL.md`
2. Understand the use case from the user
3. Recommend the appropriate orchestration pattern:
   - **Conductor**: Complex projects with dependencies
   - **Pipeline**: Sequential processing workflows
   - **Swarm**: Parallel exploration/research
4. Generate:
   - Agent hierarchy diagram (ASCII)
   - Python code for Oracle ADK implementation
   - Handoff protocol definition
   - OCI resource requirements

## Output Structure

```markdown
## Orchestration Design: [USE_CASE]

### Pattern: [PATTERN_NAME]
[Why this pattern fits]

### Agent Hierarchy
[ASCII diagram]

### Implementation
[Python code with Oracle ADK]

### OCI Resources Required
- Compute: [specs]
- Storage: [Object Storage buckets]
- Database: [if needed]
- Networking: [VCN config]

### Estimated Cost
[Monthly estimate]
```

## Example Invocations

```
/orchestrate "customer support automation" --pattern=conductor
/orchestrate "ETL data pipeline" --pattern=pipeline
/orchestrate "codebase analysis" --pattern=swarm
```
