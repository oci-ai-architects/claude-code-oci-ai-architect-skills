# Claude Code Oracle Skills

[![Version](https://img.shields.io/badge/version-2.0.0-blue)]()
[![Plugins](https://img.shields.io/badge/plugins-5-green)]()
[![Commands](https://img.shields.io/badge/commands-5-orange)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

Production-grade Claude Code plugins for Oracle Cloud AI Architects and Cloud Engineers.

## Quick Install

```bash
# Add marketplace
/plugin marketplace add frankxai/claude-code-oracle-skills

# Install all plugins
/plugin install oracle-adk oracle-agent-spec oci-services-expert oracle-ai-architect oracle-diagram-generator
```

## Available Plugins

| Plugin | Description | Commands | Difficulty |
|--------|-------------|----------|------------|
| **[oracle-adk](plugins/oracle-adk/)** | Build production agents with Oracle ADK | `/adk-agent` | Intermediate |
| **[oracle-agent-spec](plugins/oracle-agent-spec/)** | Framework-agnostic agent specifications | `/agent-spec` | Intermediate |
| **[oci-services-expert](plugins/oci-services-expert/)** | OCI services and architecture patterns | `/oci-cost` | Beginner |
| **[oracle-ai-architect](plugins/oracle-ai-architect/)** | Vector Search, Select AI, NVIDIA NIM | `/vector-search` | Advanced |
| **[oracle-diagram-generator](plugins/oracle-diagram-generator/)** | Professional OCI architecture diagrams | `/oci-diagram` | Beginner |

## Slash Commands

```bash
# Generate OCI architecture diagram
/oci-diagram rag drawio
/oci-diagram three-tier python
/oci-diagram multi-agent mermaid

# Scaffold an Oracle ADK agent
/adk-agent customer-support multi-agent
/adk-agent etl-processor pipeline

# Generate Agent Spec definition
/agent-spec research-assistant yaml

# Estimate OCI costs
/oci-cost "RAG platform with vector search"

# Implement vector search
/vector-search "document Q&A system"
```

## Who Is This For?

### AI Architects
All 5 plugins provide comprehensive coverage for building enterprise AI solutions on Oracle Cloud.

### Solution Architects
- **oci-services-expert** - OCI service selection and architecture patterns
- **oracle-diagram-generator** - Create professional diagrams for proposals

### Cloud Engineers / DevOps
- **oci-services-expert** - Infrastructure patterns, security, cost optimization
- **oracle-ai-architect** - Deployment patterns (Terraform, monitoring)

### Agent Developers
- **oracle-adk** - Code-first agent development on OCI
- **oracle-agent-spec** - Framework-agnostic agent design

### Sales Engineers / Pre-sales
- **oracle-diagram-generator** - Quickly generate customer-ready diagrams
- **oci-services-expert** - Cost estimates and service recommendations

## Plugin Structure

Each plugin follows the standard Claude Code plugin structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata
├── commands/
│   └── command.md       # Slash command definitions
├── skills/
│   └── SKILL.md         # Skill reference material
└── README.md
```

## Quality Standards

Every skill includes:
- **When to Use** - Clear activation triggers at the top
- **Code Examples** - Production-ready, tested patterns
- **Quality Checklist** - Verification points before deployment
- **Decision Framework** - When to use vs. alternatives
- **Official Resources** - Links to Oracle documentation

## Verification Status

| Plugin | Version | OCI SDK | Last Verified | Status |
|--------|---------|---------|---------------|--------|
| oracle-adk | 1.0.0 | 2.130.0 | 2026-01-21 | Active |
| oracle-agent-spec | 1.0.0 | 2.130.0 | 2026-01-21 | Active |
| oci-services-expert | 1.0.0 | 2.130.0 | 2026-01-21 | Active |
| oracle-ai-architect | 1.0.0 | 2.130.0 | 2026-01-21 | Active |
| oracle-diagram-generator | 1.0.0 | 2.130.0 | 2026-01-21 | Active |

## Related Resources

- [Oracle Agent Development Kit](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [Oracle Agent Spec](https://github.com/oracle/agent-spec)
- [OCI Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [OCI Architecture Center](https://docs.oracle.com/en/solutions/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE)

---

**Maintained by FrankX** | Oracle AI Architect
*Building the future of enterprise AI on Oracle Cloud*
