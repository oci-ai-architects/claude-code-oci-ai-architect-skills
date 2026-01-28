---
description: Quick capture of daily wins, learnings, and blockers with automatic confidentiality
thinking: false
---

# Daily Capture Mode

Quickly log your Oracle consulting work with automatic confidentiality transformation.

## Capture Protocol

### Step 1: Gather Information

Provide:
1. **Project Context**: Which project codename? (or General)
2. **Entry Type**: Win / Learning / Blocker
3. **Description**: What happened?

### Step 2: Automatic Confidentiality

Before storing, I automatically transform:

| If You Say | I Transform To |
|------------|----------------|
| Customer name | Project codename |
| "$2.3M" | "multi-million dollar" |
| "47 users" | "approximately 50 users" |
| "December 15" | "mid-Q4" |
| Specific IP/endpoints | "customer infrastructure" |

### Step 3: Store Entry

I append to your daily log with this format:

```markdown
### [TIME] - [PROJECT] - [TYPE]
**Context:** [Project codename or General]
**Entry:** [Abstracted description]
**Skills Applied:** [Relevant skills]
**Business Value:** [Impact in business terms]
```

## Quick Capture Syntax

For rapid entry, use this format:
- `[CODENAME] win: [description]`
- `[CODENAME] learning: [description]`
- `[CODENAME] blocker: [description]`

### Examples

```
A win: Resolved Kubernetes networking issue
B learning: Discovered new OCI GenAI capability
C blocker: Waiting on customer access credentials
general learning: Completed OCI AI certification module
```

## Output Location

Configure in your workspace:
- Daily logs: `reports/daily/YYYY-MM-DD.md`
- Project updates: `projects/[CODENAME].md`

---

**Start capturing:** What would you like to log?
