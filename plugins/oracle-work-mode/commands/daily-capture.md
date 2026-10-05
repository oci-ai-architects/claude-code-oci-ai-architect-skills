---
description: Quick capture of what you learned, built or got stuck on in your OCI study labs
thinking: false
---

# Daily Learning Log

Log your independent OCI study work: what you learned, what you built and what blocked you.

**Do not submit confidential engagement data.** This log is for personal study on public or
synthetic material. Never record customer or client names, employer-internal information,
credentials, OCIDs or network details. If an entry contains any of these, decline to store it and
ask for a rewrite.

## Capture protocol

### Step 1: Gather information

Ask for:
1. **Lab**: which fictional lab label (or "general")?
2. **Entry type**: built / learned / blocked
3. **Description**: what happened?

### Step 2: Check the entry

Before storing, check the entry against the data rules above. Replace any identifier that slipped
in (a region-specific endpoint, an OCID, an IP range) with a placeholder such as `<your-region>` or
`<compartment-ocid>`.

### Step 3: Store the entry

Append to the daily log in this format:

```markdown
### [TIME] - [LAB] - [TYPE]
**Entry:** [description]
**Skills practised:** [relevant skills]
**Sources:** [docs or labs used, with links]
```

## Quick capture syntax

- `[LAB] built: [description]`
- `[LAB] learned: [description]`
- `[LAB] blocked: [description]`

### Examples (fictional)

```
lab-oke built: Three-node OKE cluster with a private API endpoint
lab-rag learned: Embedding chunk size changed answer quality more than the model choice
lab-agents blocked: Tool-call schema rejected by the agent runtime, reading the docs next
general learned: Finished the OCI Generative AI learning path module on prompt design
```

## Output location

Configure in your workspace:
- Daily logs: `notes/daily/YYYY-MM-DD.md`
- Lab notes: `labs/[LAB].md`

---

**Start capturing:** what would you like to log?
