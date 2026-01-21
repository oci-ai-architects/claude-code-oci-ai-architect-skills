# Claude Code Oracle Skills

Production-grade Claude Code skills for Oracle Cloud AI Architects and Cloud Engineers.

## Quick Install

```bash
# Install all skills
curl -sSL https://raw.githubusercontent.com/FrankX/claude-code-oracle-skills/main/install.sh | bash

# Or install individual skills
curl -sSL https://raw.githubusercontent.com/FrankX/claude-code-oracle-skills/main/install.sh | bash -s -- oracle-adk
```

## Manual Installation

Copy skills to your Claude Code skills directory:

```bash
# Clone the repo
git clone https://github.com/FrankX/claude-code-oracle-skills.git
cd claude-code-oracle-skills

# Copy all skills
cp -r skills/* ~/.claude/skills/

# Or copy specific skills
cp -r skills/oracle-adk ~/.claude/skills/
```

## Available Skills

| Skill | Description | Audience | Difficulty |
|-------|-------------|----------|------------|
| **[oracle-adk](skills/oracle-adk/)** | Build production agentic applications on OCI using Oracle Agent Development Kit | AI Architects, Agent Developers | Intermediate |
| **[oracle-agent-spec](skills/oracle-agent-spec/)** | Design framework-agnostic AI agents using Oracle's Open Agent Specification | AI Architects, Enterprise Architects | Intermediate |
| **[oci-services-expert](skills/oci-services-expert/)** | Expert guidance on OCI services, architecture patterns, and cost optimization | Solution Architects, Cloud Engineers | Beginner |
| **[oracle-ai-architect](skills/oracle-ai-architect/)** | Deep technical implementations: Vector Search, Select AI, NVIDIA NIM | AI Architects, Data Engineers | Advanced |
| **[oracle-diagram-generator](skills/oracle-diagram-generator/)** | Generate professional OCI architecture diagrams (Draw.io, Python, Mermaid) | Solution Architects, Sales Engineers | Beginner |

## Who Is This For?

### AI Architects
All 5 skills provide comprehensive coverage for building enterprise AI solutions on Oracle Cloud.

### Solution Architects
- **oci-services-expert** - OCI service selection and architecture patterns
- **oracle-diagram-generator** - Create professional diagrams for proposals and presentations

### Cloud Engineers / DevOps
- **oci-services-expert** - Infrastructure patterns, security, cost optimization
- **oracle-ai-architect** - Deployment patterns (Terraform, monitoring)

### Agent Developers
- **oracle-adk** - Code-first agent development on OCI
- **oracle-agent-spec** - Framework-agnostic agent design

### Sales Engineers / Pre-sales
- **oracle-diagram-generator** - Quickly generate customer-ready architecture diagrams
- **oci-services-expert** - Cost estimates and service recommendations

## Usage Examples

### Build a Multi-Agent System
```
You: I need to build a customer support agent with Oracle ADK

Claude: (Uses oracle-adk skill to provide code patterns, best practices, and OCI integration)
```

### Design Portable Agents
```
You: Design an agent that can run on both Oracle ADK and LangGraph

Claude: (Uses oracle-agent-spec skill to create framework-agnostic YAML specification)
```

### Generate Architecture Diagrams
```
You: Create an architecture diagram for an enterprise RAG platform on OCI

Claude: (Uses oracle-diagram-generator to produce Draw.io XML or Python diagrams code)
```

### Optimize OCI Costs
```
You: Review this architecture for cost optimization opportunities

Claude: (Uses oci-services-expert to identify savings from right-sizing, reserved capacity, etc.)
```

## Keeping Skills Updated

### Automatic Updates (Recommended)

Add to your crontab or scheduled task:

```bash
# Weekly update (Sundays at midnight)
0 0 * * 0 cd ~/.claude/skills-repos/claude-code-oracle-skills && git pull && cp -r skills/* ~/.claude/skills/
```

### Manual Updates

```bash
cd ~/.claude/skills-repos/claude-code-oracle-skills
git pull
cp -r skills/* ~/.claude/skills/
```

### Version Tracking

Check `manifest.yaml` for:
- `last_verified` - When examples were last tested
- `oci_sdk_version` - Compatible OCI SDK version
- `tested_models` - Verified OCI GenAI models

## Contributing

### Adding New Skills

1. Create skill directory: `skills/your-skill-name/`
2. Add `SKILL.md` following the template in `docs/SKILL_TEMPLATE.md`
3. Update `manifest.yaml` with skill metadata
4. Add tests in `tests/test_your_skill.py`
5. Submit PR

### Updating Existing Skills

1. Update the skill's `SKILL.md`
2. Bump version in `manifest.yaml`
3. Update `last_verified` date
4. Run tests: `pytest tests/`
5. Submit PR

### Quality Standards

All skills must:
- [ ] Have working code examples
- [ ] Include cost estimates where applicable
- [ ] Reference official Oracle documentation
- [ ] Pass linting (`markdownlint`)
- [ ] Pass link checking
- [ ] Be tested with current OCI SDK

## Verification Status

| Skill | Last Verified | OCI SDK | Status |
|-------|---------------|---------|--------|
| oracle-adk | 2026-01-21 | 2.130.0 | Active |
| oracle-agent-spec | 2026-01-21 | 2.130.0 | Active |
| oci-services-expert | 2026-01-21 | 2.130.0 | Active |
| oracle-ai-architect | 2026-01-21 | 2.130.0 | Active |
| oracle-diagram-generator | 2026-01-21 | 2.130.0 | Active |

## Related Resources

- [Oracle Agent Development Kit Docs](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [Oracle Agent Spec GitHub](https://github.com/oracle/agent-spec)
- [OCI Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [OCI Architecture Center](https://docs.oracle.com/en/solutions/)

## License

MIT License - see [LICENSE](LICENSE)

---

**Maintained by FrankX** | Oracle AI Architect
*Building the future of enterprise AI on Oracle Cloud*
