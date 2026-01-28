# RAG Expert for OCI

You are an expert in Retrieval-Augmented Generation patterns on Oracle Cloud Infrastructure.

## When to Use This Skill
- Building RAG systems on OCI
- Selecting embedding models and vector stores
- Optimizing retrieval quality
- Enterprise RAG architecture

## OCI RAG Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     OCI RAG Pipeline                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────────┐    ┌─────────────────┐   │
│  │Documents │───▶│ Chunking +   │───▶│ Vector Store    │   │
│  │          │    │ Embedding    │    │ (OCI Search /   │   │
│  └──────────┘    │ (Cohere)     │    │  OpenSearch)    │   │
│                  └──────────────┘    └────────┬────────┘   │
│                                               │             │
│  ┌──────────┐    ┌──────────────┐    ┌───────▼─────────┐   │
│  │  Query   │───▶│  Query       │───▶│  Vector Search  │   │
│  │          │    │  Embedding   │    │  + Reranking    │   │
│  └──────────┘    └──────────────┘    └────────┬────────┘   │
│                                               │             │
│                  ┌──────────────┐    ┌───────▼─────────┐   │
│                  │   Response   │◀───│  LLM Generation │   │
│                  │              │    │  (Cohere/Llama) │   │
│                  └──────────────┘    └─────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## OCI Components for RAG

| Component | OCI Service | Alternatives |
|-----------|-------------|--------------|
| **Embeddings** | Cohere Embed 4 | Sentence Transformers |
| **Vector Store** | OCI Search, OpenSearch | 23ai Vector DB |
| **LLM** | GenAI (Cohere, Llama) | DAC-hosted models |
| **Document Processing** | Document Understanding | Custom parsers |
| **Orchestration** | GenAI Agents | Oracle ADK |

## Chunking Strategies

### Fixed Size
```python
chunk_size = 512
chunk_overlap = 50
```
- Simple, predictable
- May break semantic boundaries

### Semantic Chunking
```python
# Based on sentence/paragraph boundaries
# Preserves meaning
# Variable chunk sizes
```

### Hierarchical (Recommended for Enterprise)
```
Document → Sections → Paragraphs → Sentences
           ↓
        Summaries at each level
```

## Embedding Models on OCI

| Model | Dimensions | Best For |
|-------|------------|----------|
| Cohere Embed v3 | 1024 | General purpose |
| Cohere Embed 4 | 1024 | Latest, highest quality |
| multilingual-e5 | 768 | Multi-language |

### Usage
```python
from oci.generative_ai_inference import GenerativeAiInferenceClient
from oci.generative_ai_inference.models import EmbedTextDetails

client = GenerativeAiInferenceClient(config)
response = client.embed_text(
    EmbedTextDetails(
        inputs=["Your text here"],
        serving_mode=OnDemandServingMode(model_id="cohere.embed-english-v3.0"),
        compartment_id=compartment_id
    )
)
embeddings = response.data.embeddings
```

## Vector Store Options

### OCI Search (Managed)
- Fully managed, no infrastructure
- Integrated with GenAI Agents
- Good for: Quick start, managed solution

### OpenSearch on OCI
- More control, familiar interface
- k-NN plugin for vector search
- Good for: Existing OpenSearch expertise

### Oracle 23ai Vector DB
- Native vector support in Oracle DB
- Combine with relational data
- Good for: Existing Oracle customers

## Retrieval Optimization

### 1. Hybrid Search
```python
# Combine vector similarity + keyword search
results = hybrid_search(
    query=user_query,
    vector_weight=0.7,
    keyword_weight=0.3
)
```

### 2. Reranking
```python
# Use Cohere Rerank for better relevance
from cohere import Client
co = Client(api_key)
reranked = co.rerank(
    query=user_query,
    documents=initial_results,
    top_n=5
)
```

### 3. Query Expansion
```python
# Generate multiple query variations
variations = llm.expand_query(user_query)
# Search with all variations
# Deduplicate and merge results
```

## RAG Quality Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Retrieval Recall | >90% | Ground truth comparison |
| Answer Relevance | >4.5/5 | LLM-as-judge |
| Faithfulness | >95% | Citation verification |
| Latency (P95) | <3s | End-to-end timing |

## Enterprise Considerations

1. **Data Security**: Encryption at rest/transit, access controls
2. **Scalability**: Sharding, caching, async processing
3. **Observability**: Trace retrieval → generation → response
4. **Governance**: Audit trails, PII handling, compliance
