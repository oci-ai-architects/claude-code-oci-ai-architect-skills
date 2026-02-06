# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Overview

Claude Code skills marketplace for Oracle Cloud AI Architects. Provides production-grade skills and plugins covering agent development (ADK), multi-agent orchestration, vector search, diagram generation, and AI-powered visuals.

## Commands

### Testing

```bash
# Validate Python syntax in code examples
python tests/validate_code_examples.py

# Check skill completeness (frontmatter, required sections)
python tests/check_skill_completeness.py
```

### Setup

```bash
pip install pyyaml pytest oci
```

### Local Installation

```bash
# Install all skills to ~/.claude/skills/
./install.sh

# Install specific skill
./install.sh oracle-adk
```

## Architecture

### Skills vs Plugins

- **skills/**: Standalone skill files (SKILL.md) with knowledge and patterns
- **plugins/**: Installable Claude Code plugins with commands, each containing:
  - `.claude-plugin/plugin.json` - Plugin metadata
  - `commands/` - Slash command definitions (markdown with frontmatter)
  - `skills/` - Plugin-specific skill files

### Manifest

`manifest.yaml` is the central registry. Keep it synchronized with actual skills in `skills/`.

### Plugin Structure

```
plugins/{plugin-name}/
├── .claude-plugin/
│   └── plugin.json          # name, version, description, keywords
├── commands/
│   └── {command-name}.md    # Slash command definition
└── skills/
    └── SKILL.md             # Detailed knowledge/patterns
```

### Skill File Format

Every SKILL.md requires:

1. **YAML frontmatter**: `name`, `description`, `version`, `keywords`, `triggers`
2. **Required sections**: "Purpose", "Resources"
3. **Recommended sections**: "Best Practices", "Examples"
4. **Code examples**: At least one fenced code block

## Conventions

### Commits

Use conventional commits:

```
type(scope): description

# Types: fix, feat, docs, style, refactor, test, chore
# Examples:
fix(oracle-adk): correct import statement
feat(oci-services): add new model information
```

### Quality Gates (CI)

On PR/push to main:
- Markdown linting
- Link validation
- YAML validation (manifest.yaml)
- Python code block syntax validation
- Skill completeness check

Weekly: OCI SDK compatibility verification

## Key Files

- `manifest.yaml` - Skill registry with versions, tags, audiences
- `install.sh` - Bash installer for local skill deployment
- `tests/check_skill_completeness.py` - Validates skill structure
- `tests/validate_code_examples.py` - Validates Python syntax in markdown

## MCP Dependencies

The `oracle-infogenius` skill requires the `nanobanana` MCP server for image generation:

```bash
uvx nanobanana-mcp-server@latest
# Requires GEMINI_API_KEY environment variable
```
