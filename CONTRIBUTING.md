# Contributing to Claude Code Oracle Skills

Thank you for your interest in contributing! This guide will help you get started.

## Ways to Contribute

1. **Report Issues** - Found a bug or broken link? Open an issue.
2. **Suggest Improvements** - Ideas for new content? Open a discussion.
3. **Fix Errors** - Typos, outdated info? Submit a PR.
4. **Add Content** - New patterns, examples? Submit a PR.
5. **Create New Skills** - Missing a skill you need? Propose and build it.

## Quick Start

### Prerequisites

- Git
- Python 3.10+ (for running tests)
- A GitHub account

### Setup

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/claude-code-oracle-skills.git
cd claude-code-oracle-skills

# Create a branch for your changes
git checkout -b fix/your-description
```

### Make Changes

1. Edit files in `skills/` directory
2. Follow the [skill template](docs/SKILL_TEMPLATE.md) format
3. Run tests locally:

```bash
pip install pyyaml pytest
python tests/validate_code_examples.py
python tests/check_skill_completeness.py
```

### Submit

```bash
git add .
git commit -m "fix(skill-name): description of change"
git push origin fix/your-description
```

Then open a Pull Request on GitHub.

## Commit Message Format

We use conventional commits:

```
type(scope): description

[optional body]
```

**Types:**
- `fix` - Bug fixes
- `feat` - New features/content
- `docs` - Documentation only
- `style` - Formatting changes
- `refactor` - Code restructuring
- `test` - Adding tests
- `chore` - Maintenance tasks

**Examples:**
```
fix(oracle-adk): correct import statement in multi-agent example
feat(oci-services): add new AI21 model information
docs(readme): update installation instructions
```

## Pull Request Process

1. **Title** - Use conventional commit format
2. **Description** - Explain what changed and why
3. **Tests** - Ensure all CI checks pass
4. **Review** - Wait for maintainer review
5. **Merge** - Squash and merge after approval

### PR Checklist

Before submitting:

- [ ] I've read the [skill template](docs/SKILL_TEMPLATE.md)
- [ ] My code examples are syntactically valid
- [ ] I've tested changes locally
- [ ] I've updated version in manifest.yaml (if applicable)
- [ ] I've updated README.md (if adding new skill)

## Code Style

### Markdown

- Use ATX-style headers (`#` not underlines)
- One blank line between sections
- Code blocks must specify language
- No trailing whitespace

### Python Examples

- Follow PEP 8
- Include necessary imports
- Use type hints where helpful
- Keep examples focused and minimal

### YAML

- 2-space indentation
- Quote strings containing special characters
- Use lowercase keys

## Issue Guidelines

### Bug Reports

Include:
- Skill name and section
- What you expected
- What actually happened
- Steps to reproduce

### Feature Requests

Include:
- What skill/topic
- Why it's needed
- Example use cases

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn
- Keep discussions professional

## Recognition

Contributors will be:
- Listed in release notes
- Credited in the skill they contributed to
- Thanked publicly (if desired)

## Questions?

- Open a GitHub Discussion for general questions
- Tag @FrankX for urgent issues
- Check existing issues before creating new ones

---

Thank you for making these skills better for everyone!
