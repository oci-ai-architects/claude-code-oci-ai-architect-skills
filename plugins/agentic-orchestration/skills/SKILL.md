---
name: Agentic Orchestration for Oracle
description: Multi-agent coordination patterns for enterprise AI systems on Oracle Cloud Infrastructure
version: 1.0.0
keywords: [oracle, oci, agents, orchestration, multi-agent, adk, enterprise, coordination]
triggers:
  - "multi-agent"
  - "agent orchestration"
  - "coordinate agents"
  - "agent workflow"
---

# Agentic Orchestration for Oracle Cloud

## When to Use This Skill

**Activate this skill when:**
- Designing multi-agent systems on OCI
- Coordinating Oracle ADK agents
- Building enterprise agent workflows
- Need patterns for agent handoffs and task decomposition

**Don't use when:**
- Building single-agent solutions (use `oracle-adk` directly)
- Need framework-agnostic specs (use `oracle-agent-spec`)
- Just need architecture diagrams (use `oracle-diagram-generator`)

---

## Purpose

Master patterns for coordinating multiple AI agents on Oracle Cloud Infrastructure, including task decomposition, handoff protocols, and enterprise-grade orchestration using Oracle ADK.

## Orchestration Fundamentals

### Agent Hierarchy Model
```
┌─────────────────────────────────────────────────────┐
│              SUPERVISOR AGENT                        │
│  (Strategic coordination, task routing, synthesis)   │
│  Model: cohere.command-a (256K context)             │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │  Specialist  │  │  Specialist  │  │ Specialist │ │
│  │   Agent A    │  │   Agent B    │  │  Agent C   │ │
│  │  (Research)  │  │  (Analysis)  │  │ (Execute)  │ │
│  └──────────────┘  └──────────────┘  └────────────┘ │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### Core Principles (Oracle Context)

1. **Single Responsibility**: Each agent has one clear domain
2. **Explicit Handoffs**: Clear protocols for transferring work
3. **Context Preservation**: State travels with the task via OCI Object Storage
4. **Graceful Degradation**: System works if agents fail
5. **Observable Execution**: OCI Monitoring + Logging integration

## Oracle ADK Orchestration Patterns

### Pattern 1: Hierarchical Orchestration
```python
from oci_adk import Agent, Orchestrator

# Supervisor coordinates specialists
supervisor = Agent(
    name="supervisor",
    model="cohere.command-a",
    system_prompt="Coordinate specialist agents to complete complex tasks",
    tools=[research_agent, analysis_agent, execution_agent]
)

# Each specialist has focused capabilities
research_agent = Agent(
    name="researcher",
    model="cohere.command-light",  # Cost-optimized
    tools=[vector_search_tool, web_search_tool]
)

analysis_agent = Agent(
    name="analyst",
    model="cohere.command-a",
    tools=[sql_tool, analytics_tool]
)

execution_agent = Agent(
    name="executor",
    model="cohere.command-a",
    tools=[api_tool, notification_tool]
)
```

### Pattern 2: Pipeline Orchestration
```python
from oci_adk import Pipeline, Stage

# Sequential processing through stages
pipeline = Pipeline([
    Stage("extract", data_extraction_agent),
    Stage("transform", transformation_agent),
    Stage("validate", validation_agent),
    Stage("load", loading_agent)
])

# Execute with automatic state passing
result = await pipeline.execute(input_data)
```

### Pattern 3: Parallel Processing
```python
import asyncio
from oci_adk import Agent

async def parallel_analysis(task):
    # Run multiple agents concurrently
    results = await asyncio.gather(
        security_agent.execute_async(task),
        performance_agent.execute_async(task),
        compliance_agent.execute_async(task)
    )

    # Synthesize results
    return synthesis_agent.combine(results)
```

## Handoff Protocol (Oracle Context)

### Explicit Handoff Structure
```python
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class TaskHandoff:
    from_agent: str
    to_agent: str
    task_id: str
    context: Dict[str, Any]
    artifacts: Dict[str, List[str]]
    oci_resources: Dict[str, str]  # OCI-specific

# Example handoff with OCI resources
handoff = TaskHandoff(
    from_agent="ArchitectAgent",
    to_agent="DeveloperAgent",
    task_id="rag-feature-123",
    context={
        "original_request": "Build RAG pipeline",
        "work_completed": ["Design complete", "API spec created"],
        "next_steps": ["Implement embedding service", "Create search API"]
    },
    artifacts={
        "files_created": ["design.md", "api-spec.yaml"],
        "decisions_made": [
            {"decision": "Use Cohere Embed-4", "rationale": "Best multilingual support"}
        ]
    },
    oci_resources={
        "compartment": "ocid1.compartment.oc1...",
        "vector_db": "ocid1.autonomousdatabase.oc1...",
        "object_bucket": "rag-artifacts-bucket"
    }
)
```

### Context Persistence with OCI
```python
import oci
from oci.object_storage import ObjectStorageClient

def save_handoff_context(handoff: TaskHandoff, bucket: str):
    """Persist handoff context to OCI Object Storage"""
    client = ObjectStorageClient(oci.config.from_file())

    client.put_object(
        namespace_name=get_namespace(),
        bucket_name=bucket,
        object_name=f"handoffs/{handoff.task_id}.json",
        put_object_body=json.dumps(asdict(handoff))
    )

def load_handoff_context(task_id: str, bucket: str) -> TaskHandoff:
    """Resume from persisted handoff"""
    client = ObjectStorageClient(oci.config.from_file())

    response = client.get_object(
        namespace_name=get_namespace(),
        bucket_name=bucket,
        object_name=f"handoffs/{task_id}.json"
    )

    return TaskHandoff(**json.loads(response.data.content))
```

## Coordination Models

### Model 1: Conductor (Centralized)
```
┌─────────────────────────────────────────────┐
│             CONDUCTOR AGENT                  │
│  - Receives initial request                  │
│  - Decomposes into subtasks                  │
│  - Assigns to specialist agents              │
│  - Monitors via OCI Monitoring               │
│  - Synthesizes results                       │
└─────────────────────────────────────────────┘

Best for: Complex enterprise projects
Oracle Implementation: ADK Supervisor + Function Tools
```

### Model 2: Pipeline (Sequential)
```
Request → [Extract] → [Transform] → [Load] → Result
              │            │           │
         OCI Stream   OCI Function  Autonomous DB

Best for: ETL, data processing workflows
Oracle Implementation: OCI Functions + Streaming
```

### Model 3: Swarm (Distributed)
```
     ┌────────┐
     │Agent A │←──────────────────┐
     └───┬────┘                   │
         │        (Blackboard)    │
    ┌────▼────┐   ┌──────────┐   │
    │ Agent B │◄──│ Shared   │───┤
    └────┬────┘   │ State in │   │
         │        │ ADB 26ai │   │
     ┌───▼────┐   └──────────┘   │
     │Agent C │◄──────────────────┘
     └────────┘

Best for: Research, exploration, analysis
Oracle Implementation: Vector DB as shared memory
```

## Error Handling for Enterprise

### Retry with OCI Integration
```python
from oci.monitoring import MonitoringClient

async def execute_with_retry(agent, task, max_retries=3):
    monitoring = MonitoringClient(oci.config.from_file())

    for attempt in range(1, max_retries + 1):
        try:
            result = await agent.execute(task)

            # Log success metric
            post_metric(monitoring, "agent_success", 1, {
                "agent": agent.name,
                "task_id": task.id
            })

            return result

        except Exception as e:
            # Log failure metric
            post_metric(monitoring, "agent_failure", 1, {
                "agent": agent.name,
                "attempt": attempt,
                "error": str(e)
            })

            if attempt == max_retries:
                raise

            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

### Checkpoint & Resume
```python
async def execute_with_checkpoints(task, steps):
    """Resume-capable execution with OCI persistence"""

    # Check for existing checkpoint
    checkpoint = await load_checkpoint(task.id)
    start_index = checkpoint.current_step if checkpoint else 0

    for i, step in enumerate(steps[start_index:], start_index):
        try:
            await execute_step(step, task)

            # Save checkpoint after each step
            await save_checkpoint(Checkpoint(
                task_id=task.id,
                completed_steps=i + 1,
                current_step=i + 1,
                state=task.state
            ))

        except Exception as e:
            # Checkpoint is saved, can resume
            logger.error(f"Step {i} failed: {e}")
            raise
```

## Observability on OCI

### Structured Logging
```python
import logging
import oci

def setup_oci_logging(agent_name: str):
    """Configure OCI Logging Service integration"""

    handler = oci.loggingingestion.LoggingClient(
        oci.config.from_file()
    )

    logger = logging.getLogger(agent_name)
    logger.addHandler(OCILogHandler(handler, log_ocid))

    return logger

# Usage
logger = setup_oci_logging("supervisor_agent")
logger.info("Task started", extra={
    "task_id": task.id,
    "agent": "supervisor",
    "action": "TASK_START"
})
```

### Metrics Dashboard
```python
def create_agent_dashboard():
    """OCI Monitoring dashboard for agent metrics"""

    return {
        "widgets": [
            {
                "title": "Agent Success Rate",
                "query": "agent_success[1h].rate()"
            },
            {
                "title": "Average Task Duration",
                "query": "task_duration[1h].mean()"
            },
            {
                "title": "Active Agents",
                "query": "agent_active.count()"
            },
            {
                "title": "Token Usage",
                "query": "tokens_used[1h].sum()"
            }
        ]
    }
```

## Anti-Patterns to Avoid

### ❌ God Agent
One agent that does everything - no specialization.
**Fix:** Decompose into focused specialists.

### ❌ Lost Context
Handoffs that don't preserve essential information.
**Fix:** Use explicit handoff protocol with OCI persistence.

### ❌ Infinite Loops
Agents handing work back and forth forever.
**Fix:** Add loop detection and max iterations.

### ❌ Silent Failures
Agents that fail without proper error reporting.
**Fix:** Structured logging + OCI Monitoring alerts.

### ❌ Unobservable Execution
Can't see what agents are doing.
**Fix:** Decision audit trail + progress tracking.

## Quality Checklist

Before deploying orchestrated agents:

**Architecture:**
- [ ] Clear agent responsibilities defined
- [ ] Handoff protocol documented
- [ ] Error handling for all failure modes
- [ ] Loop detection implemented

**OCI Integration:**
- [ ] Checkpoints persisted to Object Storage
- [ ] Logging configured with OCI Logging
- [ ] Metrics published to OCI Monitoring
- [ ] Alerts configured for failures

**Production Readiness:**
- [ ] Load tested with realistic workloads
- [ ] Fallback agents configured
- [ ] Cost monitoring enabled
- [ ] Security review completed

## Resources

**Oracle Documentation:**
- [OCI Generative AI Agents](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/)
- [Oracle ADK](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [OCI Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/home.htm)

**Patterns:**
- [Multi-Agent Patterns](https://docs.anthropic.com/en/docs/agents-and-tools/agents)
- [Enterprise AI Architecture](https://docs.oracle.com/en/solutions/)

---

*Good orchestration is invisible - the system should feel like one coherent intelligence, not a committee of bickering agents.*
