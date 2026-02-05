# Skill Management Guide

> How to organize, manage, and maintain Claude Code skills across projects

---

## The Problem: Skills Scattered Everywhere

Claude Code skills can end up in multiple locations:
- `.claude/skills/` - Project-specific skills
- `plugins/*/skills/` - Plugin-bundled skills
- `~/.claude/plugins/` - User-installed plugins
- Multiple project directories

This leads to:
- Duplicate, outdated versions
- Confusion about which is authoritative
- Difficult maintenance and updates

---

## The Solution: Single Source of Truth

### Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    SKILL RESOLUTION ORDER                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. PROJECT-SPECIFIC    .claude/skills/     (highest priority)  │
│         ↓                                                        │
│  2. PLUGIN SKILLS       plugins/*/skills/                       │
│         ↓                                                        │
│  3. USER PLUGINS        ~/.claude/plugins/                      │
│         ↓                                                        │
│  4. SHARED REPO         claude-code-oracle-skills/skills/       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Repository Roles

| Location | Purpose | Committed to Git? |
|----------|---------|-------------------|
| `claude-code-oracle-skills/` | PUBLIC: Shareable skills, examples | Yes (public repo) |
| `.claude/skills/` | LOCAL: Project-specific overrides | Yes (private repo) |
| `plugins/` | DEPRECATED: Remove, use public repo | No (delete) |
| `clients/` | PRIVATE: Client deliverables | No (gitignored) |

---

## Recommended Structure

### Public Skills Repo (`claude-code-oracle-skills/`)

```
claude-code-oracle-skills/
├── skills/                       # Standalone skills
│   ├── oracle-infogenius/        # Base infogenius
│   ├── oracle-infogenius-flash/  # Budget tier ($0.039)
│   ├── oracle-infogenius-pro/    # Professional tier ($0.134)
│   ├── oracle-infogenius-premium/# Maximum quality ($0.24)
│   ├── oci-services-expert/      # OCI architecture guidance
│   ├── oracle-adk/               # Agent Development Kit
│   ├── oracle-agent-spec/        # Open Agent Specification
│   └── README.md                 # Skill pricing & usage guide
├── plugins/                      # Full plugins with multiple skills
│   ├── oracle-ai-architect/
│   └── agentic-orchestration/
├── commands/                     # Slash commands
├── examples/                     # Example outputs (sanitized)
└── docs/                         # Documentation
    └── SKILL_MANAGEMENT.md       # This file
```

### Project-Specific Skills (`.claude/skills/`)

Only add project-specific skills here:
- Custom client skills
- Local overrides of public skills
- Skills in development (not yet public)

```
.claude/skills/
├── oracle-research/              # Research with confidentiality
└── oracle-ai-architect-infogenius/ # Enhanced local version
```

---

## Workflow: Adding a New Skill

### 1. Development Phase

Create in `.claude/skills/` first:

```bash
mkdir -p .claude/skills/my-new-skill
echo "# My New Skill..." > .claude/skills/my-new-skill/skill.md
```

### 2. Testing

Test the skill in your project before publishing.

### 3. Publishing to Public Repo

```bash
# Copy to public repo
cp -r .claude/skills/my-new-skill claude-code-oracle-skills/skills/

# Commit to public repo
cd claude-code-oracle-skills
git add skills/my-new-skill
git commit -m "Add my-new-skill"
git push
```

### 4. Cleanup

Once published, you can optionally remove from `.claude/skills/` to avoid duplication.

---

## Sync Script

Create this script to sync skills between locations:

```bash
#!/bin/bash
# sync-skills.sh - Sync skills to public repo

PUBLIC_REPO="claude-code-oracle-skills"
LOCAL_SKILLS=".claude/skills"

# Skills to sync (add more as needed)
SKILLS=(
    "oracle-infogenius-flash"
    "oracle-infogenius-pro"
    "oracle-infogenius-premium"
)

for skill in "${SKILLS[@]}"; do
    if [ -d "$LOCAL_SKILLS/$skill" ]; then
        echo "Syncing $skill..."
        cp -r "$LOCAL_SKILLS/$skill" "$PUBLIC_REPO/skills/"
    fi
done

echo "Done. Remember to commit changes in $PUBLIC_REPO"
```

---

## Cleaning Up Duplicates

### Step 1: Identify Duplicates

```bash
# List all skill directories
find . -type d -name "skills" 2>/dev/null

# Check for duplicate skill names
find . -path "*/skills/*" -name "skill.md" | sort
```

### Step 2: Consolidate

1. Choose authoritative version (usually newest/best)
2. Copy to public repo
3. Delete duplicates

### Step 3: Remove Legacy Folders

```bash
# DANGEROUS - Review carefully before running
# rm -rf plugins/  # If duplicating public repo
# rm -rf oci-mode/skills/  # If migrated
```

---

## Best Practices

### DO:
- Use public repo as single source of truth
- Document skill pricing and usage
- Test locally before publishing
- Use semantic versioning for major changes
- Keep examples sanitized (no client data)

### DON'T:
- Copy skills to multiple locations
- Commit client-specific customizations to public repo
- Leave outdated duplicates lying around
- Forget to update README when adding skills

---

## Invoking Skills

### Direct Invocation
```
/oracle-infogenius-flash Create a simple OCI architecture
/oracle-infogenius-pro Create a client-ready diagram
```

### Programmatic Selection
```yaml
# In skill.md
model_tier: "flash"  # or "pro" or "premium"
resolution: "high"   # 1024px, 2048px, or 4096px
```

---

## Troubleshooting

### "Skill not found"
1. Check if skill exists in `.claude/skills/` or installed plugins
2. Verify skill.md file is valid YAML frontmatter
3. Restart Claude Code to reload skills

### "Using outdated version"
1. Check for duplicates: `find . -name "skill.md" | xargs grep -l "skill-name"`
2. Remove duplicates, keep only authoritative version

### "Skills scattered across projects"
1. Follow consolidation steps above
2. Use public repo as single source of truth
3. Delete redundant `plugins/` and `oci-mode/skills/` folders

---

*Last Updated: January 2026*
*Part of the FrankX Oracle Work System*
