# Oracle Work Mode Plugin

A comprehensive plugin for Oracle consulting work with built-in confidentiality protocols.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/oracle-work` | Activate Oracle work context with confidentiality mode |
| `/daily-capture` | Quick capture wins, learnings, blockers |
| `/research [topic]` | Start confidential research session |

### Agents

| Agent | Purpose |
|-------|---------|
| `oracle-cloud-coach` | OCI architecture guidance and technical coaching |
| `research-analyst` | Web research with automatic confidentiality |
| `confidentiality-guardian` | Review content before external sharing |

## Installation

```bash
# Via plugin marketplace
/plugin install oracle-work-mode

# Or manually
git clone https://github.com/frankxai/claude-code-oracle-skills.git
cp -r claude-code-oracle-skills/plugins/oracle-work-mode ~/.claude/plugins/
```

## Setup

### 1. Define Your Codenames

Create a codename mapping in your workspace (keep private, don't commit):

```markdown
<!-- .private/codename-registry.md -->
| Codename | Real Customer | Industry |
|----------|---------------|----------|
| A | [Customer 1] | Telecom |
| B | [Customer 2] | Finance |
| C | [Customer 3] | Healthcare |
```

### 2. Create Directory Structure

```
your-workspace/
├── projects/
│   ├── A.md
│   ├── B.md
│   └── C.md
├── reports/
│   ├── daily/
│   └── weekly/
├── research/
│   ├── topics/
│   └── projects/
└── .private/           ← Never commit
    └── codename-registry.md
```

### 3. Add to .gitignore

```
.private/
```

## Usage

### Start Work Session
```
/oracle-work
```

### Log Daily Activity
```
/daily-capture
A win: Resolved customer's OKE networking issue
```

### Research a Topic
```
/research OCI GPU shapes for LLM inference
```

### Review Before Sharing
```
Ask: "Review this weekly report before I send it"
→ confidentiality-guardian agent scans for sensitive info
```

## Confidentiality Protocol

This plugin automatically:
- Uses codenames instead of customer names
- Abstracts specific numbers to ranges
- Replaces dates with quarters
- Blocks output of: pricing, security configs, internal roadmaps

### Transformation Examples

| You Say | Plugin Transforms To |
|---------|---------------------|
| "Acme Corp" | Project codename or "the customer" |
| "$2.3M contract" | "multi-million dollar engagement" |
| "47 users" | "approximately 50 users" |
| "December 15 go-live" | "mid-Q4 launch" |

## Best Practices

1. **Always use codenames** in conversation
2. **Run confidentiality-guardian** before sharing any content externally
3. **Store sensitive mappings** only in `.private/` (not committed)
4. **Use daily-capture** to build evidence of value delivered

## License

MIT - Part of the Claude Code Oracle Skills collection.
