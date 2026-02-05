---
description: Create or scaffold an Oracle ADK agent application
allowed-tools: Read, Write, Bash(pip:*), Bash(python:*)
argument-hint: [agent-name] [pattern]
---

## Context

You are scaffolding an Oracle ADK agent application. Reference the oracle-adk skill for patterns.

Available patterns:
- `basic` - Single agent with tools (default)
- `multi-agent` - Supervisor + specialist agents
- `workflow` - Deterministic sequential workflow
- `pipeline` - ETL-style data pipeline

## Your Task

1. Ask for agent name if not provided
2. Ask for pattern if not provided
3. Read the oracle-adk skill: `plugins/oracle-adk/skills/SKILL.md`
4. Generate the agent code following the selected pattern
5. Create requirements.txt with dependencies
6. Provide setup instructions

## Generated Files

```
{agent-name}/
├── agent.py           # Main agent code
├── tools.py           # Function tools
├── config.py          # OCI configuration
├── requirements.txt   # Dependencies
└── README.md          # Usage instructions
```

## Example Invocations

```
/adk-agent customer-support basic
/adk-agent sales-assistant multi-agent
/adk-agent etl-processor pipeline
```
