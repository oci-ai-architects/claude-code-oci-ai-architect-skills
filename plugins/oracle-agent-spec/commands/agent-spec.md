---
description: Generate a framework-agnostic Oracle Agent Spec definition
allowed-tools: Read, Write
argument-hint: [agent-name] [format]
---

## Context

You are generating an Oracle Agent Spec definition that can be compiled to any framework.

Available formats:
- `yaml` - YAML specification (default)
- `json` - JSON specification

## Your Task

1. Ask what the agent should do if not clear
2. Read the oracle-agent-spec skill: `plugins/oracle-agent-spec/skills/SKILL.md`
3. Design the agent structure (nodes, tools, workflow)
4. Generate the specification in requested format
5. Explain how to compile to different frameworks

## Generated Output

A complete Agent Spec including:
- Agent metadata (name, version, description)
- Component definitions (LLMNode, AgentNode, etc.)
- Tool specifications
- Workflow orchestration
- Entry point

## Example Invocations

```
/agent-spec research-assistant yaml
/agent-spec customer-support json
```
