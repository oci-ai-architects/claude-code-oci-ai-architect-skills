# Skill Template

Use this template when creating new skills for the marketplace.

---

## Template

```markdown
---
name: [Skill Name]
description: [One-line description]
version: 1.0.0
---

# [Skill Name]

## Purpose
[2-3 sentences explaining what this skill enables and who it's for]

## Core Concepts

### [Concept 1]
[Explanation]

**Example:**
\`\`\`python
# Code example
\`\`\`

### [Concept 2]
[Explanation]

## Patterns & Best Practices

### Pattern 1: [Name]
[When to use, explanation]

**Implementation:**
\`\`\`python
# Complete, working code example
\`\`\`

### Pattern 2: [Name]
[Continuation...]

## Integration

### With OCI Services
[How this integrates with other OCI services]

### With Other Skills
[How this relates to other skills in the marketplace]

## Cost Considerations
[Pricing information, optimization tips]

## Resources

**Official Documentation:**
- [Link 1](https://...)
- [Link 2](https://...)

**Tutorials:**
- [Link](https://...)

## Decision Framework

**Use this skill when:**
- Condition 1
- Condition 2

**Consider alternatives when:**
- Condition 1
- Condition 2

---

*[One-line summary of what this skill enables]*
```

---

## Requirements Checklist

Before submitting a new skill, ensure:

### Structure
- [ ] YAML frontmatter with name, description, version
- [ ] Purpose section explaining the skill
- [ ] At least 3 major sections with content
- [ ] Resources section with official links
- [ ] Closing summary line

### Content Quality
- [ ] All code examples are syntactically valid
- [ ] Code examples are complete (can run with minimal setup)
- [ ] Cost information is current and accurate
- [ ] Links point to official Oracle documentation
- [ ] No placeholder text like "TODO" or "[...]"

### Style
- [ ] Uses ATX headers (`#`, `##`, `###`)
- [ ] Code blocks specify language (```python, ```yaml, etc.)
- [ ] Consistent formatting throughout
- [ ] No trailing whitespace
- [ ] Proper markdown escaping

### Testing
- [ ] Passes markdownlint
- [ ] Passes link checker
- [ ] Code examples parse successfully
- [ ] Skill completeness check passes

---

## Example: Minimal Valid Skill

```markdown
---
name: OCI Queue Expert
description: Build event-driven applications using OCI Queue Service
version: 1.0.0
---

# OCI Queue Expert

## Purpose
Master OCI Queue Service for building reliable, decoupled event-driven applications. This skill is for developers building microservices and event-driven architectures on Oracle Cloud.

## Core Concepts

### Queue Basics
OCI Queue provides managed message queuing with guaranteed delivery.

**Create a Queue:**
\`\`\`python
import oci

queue_client = oci.queue.QueueAdminClient(config)

queue = queue_client.create_queue(
    create_queue_details=oci.queue.models.CreateQueueDetails(
        display_name="my-queue",
        compartment_id=compartment_id,
        retention_in_seconds=172800
    )
)
\`\`\`

### Publishing Messages
\`\`\`python
queue_client.put_messages(
    queue_id=queue.data.id,
    put_messages_details=oci.queue.models.PutMessagesDetails(
        messages=[
            oci.queue.models.PutMessagesDetailsEntry(content="Hello World")
        ]
    )
)
\`\`\`

### Consuming Messages
\`\`\`python
messages = queue_client.get_messages(
    queue_id=queue.data.id,
    limit=10
)

for msg in messages.data.messages:
    print(msg.content)
    # Acknowledge after processing
    queue_client.delete_message(queue_id, msg.receipt)
\`\`\`

## Best Practices

### Dead Letter Queues
Configure DLQ for failed message handling:
\`\`\`python
queue = queue_client.create_queue(
    create_queue_details=oci.queue.models.CreateQueueDetails(
        display_name="my-queue",
        compartment_id=compartment_id,
        dead_letter_queue_delivery_count=5
    )
)
\`\`\`

## Cost Considerations
- First 1M API requests/month: Free
- Additional requests: $0.40 per 1M
- Message retention: Free up to 7 days

## Resources

**Official Documentation:**
- [OCI Queue Overview](https://docs.oracle.com/en-us/iaas/Content/queue/home.htm)
- [Queue API Reference](https://docs.oracle.com/en-us/iaas/api/#/en/queue/latest/)

---

*Build reliable event-driven applications with OCI Queue Service.*
```

---

## Skill Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Service expert | `oci-[service]-expert` | `oci-queue-expert` |
| Technology expert | `oracle-[tech]` | `oracle-adk` |
| Use case focused | `[use-case]-on-oci` | `rag-on-oci` |
| Integration | `oci-[a]-to-[b]` | `oci-fusion-to-adb` |

## File Locations

```
skills/
└── your-skill-name/
    └── SKILL.md          # Main skill file (required)
```

Keep it simple - one file per skill. If a skill needs supporting files, consider if it should be split into multiple skills instead.
