# Marketplace Maintenance Guide

Best practices for keeping the Claude Code Oracle Skills marketplace healthy and valuable.

## Update Triggers

### When to Update Skills

1. **OCI SDK Release** - Check monthly for new SDK versions
2. **New OCI Service** - When Oracle releases new AI/Cloud services
3. **API Changes** - When existing APIs are deprecated or modified
4. **Bug Reports** - When users report issues with examples
5. **Documentation Updates** - When Oracle updates official docs

### Monitoring Sources

- [OCI Release Notes](https://docs.oracle.com/en-us/iaas/releasenotes/)
- [OCI Python SDK Changelog](https://github.com/oracle/oci-python-sdk/blob/master/CHANGELOG.md)
- [Oracle ADK Updates](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [Oracle AI Blog](https://blogs.oracle.com/ai-and-datascience/)

## Update Workflow

### Quick Updates (Typos, Minor Fixes)

```bash
# 1. Edit skill file directly
vim skills/oracle-adk/SKILL.md

# 2. Commit with descriptive message
git add skills/oracle-adk/SKILL.md
git commit -m "fix(oracle-adk): correct typo in multi-agent example"

# 3. Push to trigger CI
git push origin main
```

### Major Updates (New Features, API Changes)

```bash
# 1. Create feature branch
git checkout -b update/oracle-adk-v2

# 2. Make changes
vim skills/oracle-adk/SKILL.md

# 3. Update version in manifest.yaml
sed -i 's/oracle-adk:\n    version: 1.0.0/oracle-adk:\n    version: 1.1.0/' manifest.yaml

# 4. Run local tests
python tests/validate_code_examples.py
python tests/check_skill_completeness.py

# 5. Commit and PR
git add .
git commit -m "feat(oracle-adk): add new Workflow patterns from ADK 2.0"
git push origin update/oracle-adk-v2
gh pr create --title "feat(oracle-adk): ADK 2.0 workflow patterns"
```

### Quarterly Review

Every quarter, do a full review:

1. **Check all links** - Run link checker manually
2. **Verify code examples** - Test against latest OCI SDK
3. **Update cost estimates** - Check current OCI pricing
4. **Review user feedback** - Check GitHub issues/discussions
5. **Update manifest** - Bump `last_verified` date

```bash
# Quarterly review script
./scripts/quarterly-review.sh
```

## Version Strategy

### Semantic Versioning

```
MAJOR.MINOR.PATCH

MAJOR - Breaking changes (restructured skill, removed sections)
MINOR - New content (new patterns, new examples)
PATCH - Bug fixes (typos, broken links)
```

### Version Tracking

- Each skill has its own version in `manifest.yaml`
- Overall marketplace version in root `manifest.yaml`
- Use git tags for releases: `v1.2.0`

## Quality Gates

### Automated Checks (CI/CD)

| Check | Trigger | Failure Action |
|-------|---------|----------------|
| Markdown lint | Every PR | Block merge |
| Link checking | Every PR | Block merge |
| YAML validation | Every PR | Block merge |
| Python syntax | Every PR | Block merge |
| Skill completeness | Every PR | Block merge |
| OCI compatibility | Weekly | Create issue |

### Manual Checks (Quarterly)

- [ ] Test code examples in real OCI environment
- [ ] Verify pricing information
- [ ] Review for outdated patterns
- [ ] Check competitor offerings (compare with other skill sources)
- [ ] Update screenshots/diagrams if UI changed

## Adding New Skills

### Criteria for New Skills

1. **Demand** - Users have requested this topic
2. **Scope** - Large enough to warrant a full skill
3. **Stability** - Based on stable Oracle technology
4. **Differentiation** - Not covered by existing skills

### New Skill Checklist

- [ ] Create `skills/skill-name/SKILL.md` using template
- [ ] Add entry to `manifest.yaml`
- [ ] Add tests if skill has unique requirements
- [ ] Update README.md with new skill
- [ ] Create PR with `[new-skill]` label

## Deprecation Process

### When to Deprecate

1. Oracle discontinues the service/feature
2. Better alternative exists
3. No longer maintained/used

### Deprecation Steps

1. **Mark as deprecated** in manifest.yaml:
   ```yaml
   oracle-old-skill:
     deprecated: true
     deprecation_date: 2026-06-01
     replacement: oracle-new-skill
   ```

2. **Add deprecation notice** to skill header:
   ```markdown
   > **DEPRECATED**: This skill is deprecated. Use [oracle-new-skill](../oracle-new-skill/) instead.
   ```

3. **Keep for 6 months** - Don't remove immediately
4. **Remove after notice period**

## Contribution Guidelines

### For External Contributors

1. Fork the repository
2. Create feature branch
3. Make changes following the style guide
4. Run tests locally
5. Submit PR with clear description

### Style Guide

- Use ATX-style headers (`#` not underlines)
- Code blocks must specify language
- Include cost estimates where applicable
- Reference official Oracle docs
- Keep examples concise but complete

### Review Criteria

- [ ] Follows skill template structure
- [ ] All code examples are valid
- [ ] Links point to official Oracle sources
- [ ] No sensitive data in examples
- [ ] Passes all CI checks

## Metrics to Track

### Usage Metrics (if analytics enabled)

- Download count per skill
- Geographic distribution
- Most popular skills

### Quality Metrics

- GitHub stars/forks
- Open issues count
- PR merge time
- Link rot percentage

### Update Metrics

- Days since last update (per skill)
- OCI SDK version lag
- Quarterly review completion rate

## Emergency Procedures

### Critical Bug (Security/Data Loss)

1. **Immediately** push fix to main
2. Tag emergency release: `vX.Y.Z-hotfix`
3. Notify users via GitHub release notes
4. Post-mortem within 48 hours

### Oracle API Breaking Change

1. Create issue documenting the change
2. Update affected skills within 1 week
3. Add migration notes if needed
4. Bump major version if breaking

---

**Maintainer**: FrankX
**Review Cycle**: Quarterly (Jan, Apr, Jul, Oct)
**Last Review**: 2026-01-21
