# Best Practices for Claude Code Skills

> Guidelines for creating, maintaining, and distributing Claude Code skills safely

---

## 1. Intellectual Property (IP)

### Trademark Usage

| DO | DON'T |
|----|-------|
| Use product names descriptively ("works with OCI") | Imply official endorsement |
| Reference official documentation | Use official logos |
| Use "unofficial" and "community" labels | Claim affiliation |
| Link to official sources | Copy proprietary content |

### Naming Conventions

```
✅ GOOD                          ❌ BAD
oci-architect-patterns          oracle-official-skills
cloud-ai-toolkit                 oracle-certified-toolkit
enterprise-cloud-skills          oracle-approved-patterns
```

### Required Disclaimers

Every skill referencing a company's products should include:

```markdown
> **Disclaimer:** This is an unofficial community project.
> Not affiliated with, endorsed by, or sponsored by [Company].
> [Product names] are trademarks of [Company].
```

### License Selection

| License | When to Use |
|---------|-------------|
| **MIT** | Default for open skills |
| **Apache 2.0** | If including patent grants |
| **CC BY-SA** | Documentation-only projects |

---

## 2. Confidentiality

### What NEVER to Commit

```gitignore
# Absolute NO - Always gitignore
.env                    # Environment variables
*.pem, *.key           # Certificates/keys
credentials.json       # Service accounts
.private/              # Private data folder
*-confidential-*       # Confidential files
clients/*/deliverables/* # Client work
```

### Customer Data Handling

| Data Type | Safe Approach |
|-----------|---------------|
| Customer names | Use codenames (K, V, E) |
| Contract values | Never include |
| Architecture details | Sanitize/generalize |
| Internal URLs | Remove or mock |
| Pricing | Use public pricing only |

### Example Sanitization

```markdown
❌ BEFORE (Confidential):
"Acme Corp's RAG platform handles 10M queries at $0.02/query"

✅ AFTER (Sanitized):
"Enterprise RAG platform handles high-volume queries cost-effectively"
```

---

## 3. Marketplace Best Practices

### Repository Structure

```
your-skills-repo/
├── README.md              # Overview, install, quick start
├── LICENSE                # MIT recommended
├── CONTRIBUTING.md        # How to contribute
├── SECURITY.md            # Security policy
├── CODE_OF_CONDUCT.md     # Community guidelines
├── .gitignore             # Comprehensive ignore list
├── manifest.yaml          # Plugin metadata
├── skills/                # Individual skills
│   └── skill-name/
│       └── skill.md
├── plugins/               # Full plugins
├── commands/              # Slash commands
├── examples/              # Sanitized examples
├── docs/                  # Documentation
│   ├── BEST_PRACTICES.md  # This file
│   └── SKILL_TEMPLATE.md  # Template for new skills
├── tests/                 # Validation scripts
└── .github/
    ├── ISSUE_TEMPLATE/    # Bug/feature templates
    └── PULL_REQUEST_TEMPLATE.md
```

### README Essentials

Every marketplace repo should have:

1. **Clear disclaimer** - Unofficial, not endorsed
2. **Quick install** - One-command installation
3. **What's included** - Table of skills/plugins
4. **Examples** - Visual or code examples
5. **Who it's for** - Target audience
6. **Prerequisites** - Dependencies
7. **License** - Clear licensing

### Version Management

```yaml
# manifest.yaml
name: your-skills
version: 1.2.3  # Semantic versioning
min_claude_code_version: "1.0.0"
```

Use semantic versioning:
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

---

## 4. Skill Quality Standards

### Required Sections

Every skill.md should include:

```markdown
---
name: "Skill Name"
description: "One-line description"
triggers:
  - "keyword1"
  - "keyword2"
---

# Skill Name

> Brief description

## When to Use
- Trigger conditions

## Usage
- How to invoke

## Examples
- Working examples

## Related Skills
- Cross-references
```

### Quality Checklist

```
PRE-PUBLISH CHECKLIST
═══════════════════════════════════════════════════
□ Disclaimer present
□ No official logos
□ No customer data
□ No credentials/secrets
□ Code examples are valid
□ Links work
□ Tested locally
□ Version bumped
□ README updated
═══════════════════════════════════════════════════
```

---

## 5. Generated Content Guidelines

### Image Generation

When using AI image generation (Nano Banana, etc.):

```
DO:
- Use text labels instead of logos
- Use brand-inspired colors (not exact)
- Add "NO LOGOS" to prompts
- Review before sharing

DON'T:
- Include official logos
- Use exact brand colors as "official"
- Generate misleading content
- Skip review step
```

### Prompt Template

```
IMPORTANT: Do NOT include any logos or trademark symbols.
Use text labels only. This is an unofficial community diagram.
```

---

## 6. Community Management

### Issue Triage

| Label | When to Use |
|-------|-------------|
| `bug` | Something broken |
| `enhancement` | New feature request |
| `documentation` | Docs improvement |
| `good-first-issue` | Easy for newcomers |
| `help-wanted` | Need contributors |

### Response Times

- **Security issues**: Within 24 hours
- **Bugs**: Within 1 week
- **Features**: When capacity allows
- **Questions**: Point to docs first

### Recognition

- Credit contributors in release notes
- Add to CONTRIBUTORS.md (if many contributors)
- Thank publicly in PR merges

---

## 7. Maintenance Checklist

### Monthly

- [ ] Review and merge PRs
- [ ] Update dependencies (if any)
- [ ] Check for broken links
- [ ] Review security alerts

### Quarterly

- [ ] Update pricing/service info
- [ ] Review and update examples
- [ ] Check competitor/similar projects
- [ ] Update documentation

### Annually

- [ ] Major version review
- [ ] License review
- [ ] IP/trademark compliance check
- [ ] Archive outdated skills

---

## 8. Distribution Channels

### GitHub Marketplace (Primary)

```bash
# Users install via
/plugin marketplace add username/repo-name
```

### Direct Installation

```bash
# Clone and link
git clone https://github.com/username/repo.git
# Follow repo-specific instructions
```

### Documentation Site

Consider GitHub Pages for:
- Interactive skill catalog
- Visual galleries
- Searchable documentation

---

## Summary: The 10 Commandments

1. **Always disclaim** - "Unofficial, not affiliated"
2. **Never use logos** - Text labels only
3. **Protect secrets** - Comprehensive .gitignore
4. **Sanitize examples** - No customer data
5. **Version properly** - Semantic versioning
6. **Document thoroughly** - README, CONTRIBUTING, etc.
7. **Test locally** - Before publishing
8. **Respond promptly** - Security issues especially
9. **Credit contributors** - Build community
10. **Maintain regularly** - Keep content fresh

---

*Last updated: January 2026*
*Part of the Claude Code Oracle Skills project*
