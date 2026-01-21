---
description: Generate Oracle Database 23ai Vector Search implementation
allowed-tools: Read, Write
argument-hint: [use-case]
---

## Context

You are implementing Oracle Database 23ai AI Vector Search. This includes table creation, embedding storage, and similarity search queries.

## Your Task

1. Understand the use case (document search, product similarity, etc.)
2. Read the oracle-ai-architect skill: `plugins/oracle-ai-architect/skills/SKILL.md`
3. Generate:
   - Table creation DDL with vector columns
   - Python code for embedding generation (OCI GenAI)
   - SQL queries for vector similarity search
   - Hybrid search examples (vector + traditional filters)

## Output Includes

- SQL DDL for vector-enabled tables
- Python code for OCI GenAI embeddings
- Example queries (cosine, euclidean, dot product)
- Best practices for indexing

## Example Invocations

```
/vector-search "document Q&A system"
/vector-search "product recommendation engine"
/vector-search "semantic code search"
```
