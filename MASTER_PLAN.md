# Oracle Claude Code Skills - Master Expansion Plan

## Vision
Create the definitive Claude Code marketplace for Oracle Cloud practitioners - from AI Architects to Cloud Engineers to Sales Engineers.

## Naming Decision
**Primary:** `claude-code-oracle-skills` (current, Claude ecosystem focus)
**GitHub Topics:** `oracle`, `oci`, `claude-code`, `ai-architect`, `enterprise-ai`

## Phase 1: Skill Expansion (Current Session)

### High-Value Skills to Add from Global Skills
| Skill | Source | Value for Oracle |
|-------|--------|------------------|
| starlight-architect | Global | Enterprise AI system design with Oracle |
| agentic-orchestration | Global | Multi-agent patterns (ADK-compatible) |
| planning-with-files | Global | Structured execution methodology |
| sparc-methodology | Global | Spec-driven development |
| mcp-architecture | Global | MCP server design for OCI |
| verification-quality | Global | Quality gates and testing |

### Oracle-Specific Skills to Create
| Skill | Purpose |
|-------|---------|
| oracle-fusion-ai | AI integration with Fusion Apps |
| oci-data-platform | Data lakehouse + AI patterns |
| oracle-apex-ai | APEX + GenAI integration |

## Phase 2: Visual Identity

### GitHub Pages
- Landing page with skill catalog
- Interactive skill selector
- Architecture diagram gallery
- Cost calculator widget

### Infographics (InfoGenius)
- Skill ecosystem map
- Decision flowchart (which skill to use)
- Architecture pattern gallery
- Cost comparison charts

## Phase 3: Local Management Structure

### Current Setup
```
/mnt/c/Users/Frank/
├── oracle-work/                    # Day job (CONFIDENTIAL)
│   ├── projects/                   # Customer projects (codenames)
│   ├── .private/                   # Real mappings (NEVER COMMIT)
│   └── claude-code-oracle-skills/  # PUBLIC marketplace
└── .claude/
    └── skills/                     # Active skills (local)
```

### Recommended Structure
```
/mnt/c/Users/Frank/
├── oracle-work/                    # Day job (CONFIDENTIAL)
│   ├── projects/                   # Customer work
│   ├── .private/                   # Mappings
│   └── research/                   # Learning/exploration
├── claude-code-oracle-skills/      # MOVE TO SEPARATE REPO
│   └── (public marketplace)
└── .claude/
    └── skills/                     # Symlink to marketplace
```

**Key Principle:** Marketplace is PUBLIC, oracle-work is PRIVATE
- Never merge confidential work into public repo
- Use symlinks for local skill activation
- Marketplace evolves from PUBLIC knowledge only

## Execution Plan

### Wave 1: Parallel Skill Creation
- [ ] Add starlight-architect (adapted for Oracle)
- [ ] Add agentic-orchestration (ADK patterns)
- [ ] Add sparc-methodology (OCI context)
- [ ] Add mcp-architecture (OCI MCP servers)

### Wave 2: Visual Assets
- [ ] GitHub Pages setup
- [ ] InfoGenius infographics
- [ ] Architecture gallery

### Wave 3: Documentation
- [ ] Skill comparison matrix
- [ ] Decision flowchart
- [ ] Video walkthroughs (future)

## Privacy Boundaries

| Content | Location | Visibility |
|---------|----------|------------|
| Marketplace skills | claude-code-oracle-skills/ | PUBLIC |
| Customer projects | oracle-work/projects/ | PRIVATE |
| Customer mappings | oracle-work/.private/ | NEVER COMMIT |
| Personal learnings | oracle-work/research/ | PRIVATE |
| Architecture patterns | Marketplace | PUBLIC (sanitized) |

## Success Metrics
- 10+ production-quality skills
- 500+ GitHub stars (6 month goal)
- Used by Oracle community
- Cited in Oracle blogs/docs
