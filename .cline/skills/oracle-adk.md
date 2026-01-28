# Oracle Agent Development Kit (ADK)

You are an expert in Oracle's Agent Development Kit for building production-grade AI agents on OCI.

## When to Use This Skill
- Building multi-agent systems on OCI
- Implementing tool-calling patterns
- Creating RAG-enabled agents
- Enterprise agent orchestration

## Oracle ADK Core Concepts

### Agent Architecture
```
┌─────────────────────────────────────┐
│           Agent Endpoint            │
├─────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐          │
│  │  Agent  │  │ Tools   │          │
│  │  Logic  │◄─┤ Registry│          │
│  └────┬────┘  └─────────┘          │
│       │                             │
│  ┌────▼────┐  ┌─────────┐          │
│  │Knowledge│  │ Session │          │
│  │  Bases  │  │ Memory  │          │
│  └─────────┘  └─────────┘          │
└─────────────────────────────────────┘
```

### Agent Types
1. **Simple Agent** - Single-turn Q&A with tools
2. **RAG Agent** - Knowledge base retrieval + generation
3. **Multi-Agent** - Orchestrated agent workflows
4. **Streaming Agent** - Real-time response streaming

### Tool Categories
| Category | Examples |
|----------|----------|
| **Knowledge** | Vector search, document retrieval |
| **Data** | Database queries, API calls |
| **Compute** | Code execution, calculations |
| **Integration** | External APIs, webhooks |

## SDK Quick Reference

### Python Agent Creation
```python
from oci.generative_ai_agent_runtime import GenerativeAiAgentRuntimeClient
from oci.generative_ai_agent_runtime.models import ChatDetails

client = GenerativeAiAgentRuntimeClient(config)

response = client.chat(
    agent_endpoint_id="ocid1.genaiagentendpoint.oc1...",
    chat_details=ChatDetails(
        user_message="What are our Q4 sales figures?",
        session_id=session_id
    )
)
```

### Creating Knowledge Base
```python
from oci.generative_ai_agent import GenerativeAiAgentClient

agent_client = GenerativeAiAgentClient(config)

knowledge_base = agent_client.create_knowledge_base(
    create_knowledge_base_details=CreateKnowledgeBaseDetails(
        compartment_id=compartment_id,
        display_name="Sales KB",
        description="Q4 sales documents"
    )
)
```

## Multi-Agent Patterns

### Sequential Pattern
```
Agent A → Agent B → Agent C → Result
```
Use for: Workflows where each step depends on previous

### Parallel Pattern
```
         ┌─ Agent A ─┐
Request ─┼─ Agent B ─┼─ Synthesizer → Result
         └─ Agent C ─┘
```
Use for: Independent analyses that get combined

### Hierarchical Pattern
```
      Orchestrator
         │
    ┌────┼────┐
    ▼    ▼    ▼
   A1   A2   A3  (Specialists)
```
Use for: Complex tasks with specialized sub-agents

## Enterprise Considerations
- **Security**: Agent isolation, credential management
- **Observability**: Tracing, logging, metrics
- **Governance**: Audit trails, approval workflows
- **Scaling**: Auto-scaling endpoints, load balancing

## Key Documentation
- [Oracle ADK Docs](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [GenAI Agents Overview](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
