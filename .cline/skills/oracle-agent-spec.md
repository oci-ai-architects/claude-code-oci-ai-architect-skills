# Oracle Open Agent Specification

You are an expert in Oracle's Open Agent Specification for portable, framework-agnostic AI agent definitions.

## When to Use This Skill
- Defining agents that work across multiple platforms
- Creating portable agent specifications
- Implementing "The Frank Method" agent blueprints
- Enterprise agent standardization

## Oracle Agent Spec Overview

The Open Agent Specification is a **framework-agnostic** standard for defining AI agents. Agents defined in this format can be deployed on:
- Oracle ADK
- LangChain
- AutoGen
- Custom frameworks

## Core Components

### Agent Definition Structure
```yaml
name: "Marketing Agent"
version: "1.0.0"
description: "Strategic brand management and campaign optimization"

llm_config:
  model_id: "llama-3.1-70b"
  temperature: 0.7
  max_tokens: 2048

system_prompt: |
  You are an expert Marketing AI agent specializing in...

tools:
  - name: analyze_campaign
    description: Analyze marketing campaign metrics
    inputs:
      - campaign_id: string
      - date_range: string
    outputs:
      - roi: number
      - recommendations: list

inputs:
  - user_name: string
  - department: string
  - access_level: string
```

## The AGENT Blueprint Framework

Every agent follows the **AGENT** acronym:

### A - Architecture (System Prompt)
```markdown
## Primary Function
[One-sentence mission statement]

## Core Competencies
[3-5 key capability areas]

## Communication Style
[How this agent speaks and thinks]

## Typical Outputs
[What this agent produces]
```

### G - Governance (Decision Authority)

| Level | Scope | Example |
|-------|-------|---------|
| **Full Authority** | Routine, reversible | Approve invoice <$1K |
| **Collaborative** | Cross-domain, medium risk | Budget >$10K |
| **Advisory Only** | High risk, irreversible | Policy changes |

### E - Execution (Tools)

Tools follow single-purpose design:
```python
ServerTool(
    name="analyze_campaign_performance",
    description="Analyze marketing campaign metrics",
    inputs=[
        StringProperty(title="campaign_id"),
        StringProperty(title="date_range"),
    ],
    outputs=[
        NumberProperty(title="roi"),
        ListProperty(title="recommendations")
    ]
)
```

### N - Network (Multi-Agent Orchestration)

**Pattern 1: Sequential**
```
Strategist → Creator → Engineer → Guardian → Deploy
```

**Pattern 2: Parallel**
```
Request → [Agent A | Agent B | Agent C] → Synthesis
```

**Pattern 3: Hierarchical**
```
Orchestrator → [Specialist A | Specialist B | Specialist C]
```

### T - Transformation (KPIs)

Every agent tracks:
- Efficiency: Time saved, error reduction
- Quality: Accuracy, satisfaction
- Business: Revenue, cost savings

## Python SDK Usage

```python
from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer

agent = Agent(
    name="Finance Agent",
    llm_config=VllmConfig(
        name="finance-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"
    ),
    system_prompt="...",
    tools=[...],
)

# Export to JSON/YAML
serializer = AgentSpecSerializer()
agent_json = serializer.to_json(agent)
agent_yaml = serializer.to_yaml(agent)
```

## Enterprise Agents Catalog

| Agent | ROI | Annual Savings |
|-------|-----|----------------|
| Finance | 60% efficiency | $180K |
| HR | 50% efficiency | $150K |
| Customer Support | 70% efficiency | $280K |
| Marketing | 85% efficiency | $340K |
| Sales | 55% efficiency | $220K |

## Resources
- [Oracle Agent Spec GitHub](https://github.com/oracle/agent-spec)
- [pyagentspec Documentation](https://pypi.org/project/pyagentspec/)
