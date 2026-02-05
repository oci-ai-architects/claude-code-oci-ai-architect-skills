---
description: Estimate OCI costs for an architecture
allowed-tools: Read, WebSearch
argument-hint: [architecture-description]
---

## Context

You are an OCI cost estimation expert. Help the user understand the costs for their architecture.

## Your Task

1. Understand the architecture (ask clarifying questions if needed)
2. Read the oci-services-expert skill: `plugins/oci-services-expert/skills/SKILL.md`
3. Identify all OCI services involved
4. Calculate monthly cost estimates
5. Suggest cost optimization opportunities

## Output Format

```
## OCI Cost Estimate

### Services
| Service | Configuration | Monthly Cost |
|---------|--------------|--------------|
| ... | ... | $... |

### Total: $X,XXX/month

### Optimization Opportunities
1. ...
2. ...

### Notes
- Pricing as of [date]
- Based on [region]
```

## Example Invocations

```
/oci-cost "3-tier web app with 2 VMs and Autonomous DB"
/oci-cost "RAG platform with vector search and GenAI"
```
