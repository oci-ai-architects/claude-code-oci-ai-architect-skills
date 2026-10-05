# oracle-work-mode

An independent OCI learning and research workflow for Claude Code: study sessions, a daily
learning log, source-backed research and a privacy check before you publish.

Independent community project. Not affiliated with, endorsed by, or sponsored by Oracle
Corporation. Oracle and OCI are trademarks or registered trademarks of Oracle Corporation. Other
names are marks of their respective owners.

> The plugin id `oracle-work-mode` is kept for compatibility with existing installs. A rename is
> tracked separately.

## Do not submit confidential engagement data

This plugin is for personal study on public or synthetic material. Do not paste or type customer
or client names, employer-internal documents, contract or pricing terms, unreleased product
information, credentials, OCIDs, IP ranges or any other non-public material into a session. Use the
official OCI documentation, your own sandbox tenancy or synthetic data. The commands and agents
are instructed to stop and ask for a public substitute when they see such material.

## Features

### Commands

Claude Code discovers these from the plugin's `commands/` directory.

| Command | Description |
|---------|-------------|
| `/oracle-work` | Start a study session with the data rules and agents loaded |
| `/daily-capture` | Log what you built, learned or got stuck on |
| `/research [topic]` | Start a source-backed research session |

### Agents

Claude Code discovers these from the plugin's `agents/` directory.

| Agent | Purpose |
|-------|---------|
| `oracle-cloud-coach` | OCI architecture coaching for study labs |
| `research-analyst` | Source-backed web research and synthesis |
| `confidentiality-guardian` | Privacy check before a post, talk or repo goes public |

## Installation

This plugin is not listed in the repository's `.claude-plugin/marketplace.json` yet, so `/plugin install`
will not find it. Load it from a local clone instead:

```bash
claude --plugin-dir ./plugins/oracle-work-mode
```

## Setup

### 1. Name your labs

Give each study project a short fictional label and keep the list in `notes/labs.md`:

```markdown
| Label | What it is (fictional) | Status |
|-------|------------------------|--------|
| lab-rag | RAG over the public OCI docs, in a personal free-tier tenancy | Active |
| lab-agents | A toy travel-booking agent with synthetic data | Active |
| lab-oke | A three-node OKE cluster for practice | Planning |
```

### 2. Create a directory structure

```
your-workspace/
├── labs/
│   ├── lab-rag.md
│   ├── lab-agents.md
│   └── lab-oke.md
├── notes/
│   ├── labs.md
│   └── daily/
└── research/
    ├── topics/
    └── labs/
```

## Usage

### Start a study session
```
/oracle-work
```

### Log the day
```
/daily-capture
lab-oke built: Three-node OKE cluster with a private API endpoint
```

### Research a topic
```
/research OCI GPU shapes for LLM inference
```

### Check before publishing
```
Ask: "Review this lab-rag write-up before I publish it"
→ the confidentiality-guardian agent checks for identifiers, secrets and non-public information
```

## License

MIT. See the repository [LICENSE](../../LICENSE).
