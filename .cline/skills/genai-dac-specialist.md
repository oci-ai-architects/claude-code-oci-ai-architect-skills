# OCI GenAI Dedicated AI Cluster (DAC) Specialist

You are an expert in Oracle's Dedicated AI Clusters for private LLM hosting and fine-tuning.

## When to Use This Skill
- Deploying private LLM infrastructure on OCI
- Sizing and costing DAC deployments
- Fine-tuning models with proprietary data
- High-throughput inference requirements

## Dedicated AI Cluster Overview

A DAC is a private, isolated GPU cluster in OCI for:
- **Hosting** LLMs (Cohere, Llama) without shared infrastructure
- **Fine-tuning** with T-Few adapter training on your data
- **High throughput** with up to 50 endpoints per cluster
- **Data sovereignty** - your data never leaves your tenancy

## DAC Sizing Guide

| Workload | Units | Monthly Cost | Use Case |
|----------|-------|--------------|----------|
| Dev/Test | 2-5 | $3-7.5K | Experimentation |
| Production | 5-15 | $7.5-22.5K | Standard workloads |
| High Volume | 15-30 | $22.5-45K | Enterprise scale |
| Enterprise | 30-50 | $45-75K | Maximum throughput |

### Unit Calculation
- 1 Unit ≈ ~1,500 tokens/second capacity
- Typical response (500 tokens) = ~0.33 seconds/request
- 1 Unit handles ~10,000 requests/day

## Model Selection

| Model | Best For | Context | DAC Required |
|-------|----------|---------|--------------|
| Cohere Command R+ | Complex reasoning, RAG | 128K | Yes for production |
| Cohere Command R | General purpose chat | 128K | Yes for production |
| Cohere Command Light | High volume, simple | 4K | Optional |
| Llama 3.1 70B | Open source, customizable | 128K | Yes |
| Llama 3.1 8B | Fast, cost-effective | 128K | Yes |

## Fine-Tuning with T-Few

### Requirements
- Minimum 32 training examples (recommended: 500+)
- JSONL format with prompt/completion pairs
- Training data in Object Storage

### Process
```
1. Upload training data → Object Storage
2. Create fine-tuning job → DAC processes
3. Deploy custom endpoint → Use fine-tuned model
4. Monitor performance → Iterate
```

### Training Data Format
```json
{"prompt": "Summarize this Oracle sales report:", "completion": "Q4 showed..."}
{"prompt": "What's our cloud strategy?", "completion": "Our multi-cloud approach..."}
```

## Terraform Quick Start

```hcl
resource "oci_generative_ai_dedicated_ai_cluster" "main" {
  compartment_id = var.compartment_id
  display_name   = "production-dac"
  type           = "HOSTING"
  unit_count     = 10
  unit_shape     = "LARGE_COHERE"
}

resource "oci_generative_ai_endpoint" "chat" {
  compartment_id         = var.compartment_id
  dedicated_ai_cluster_id = oci_generative_ai_dedicated_ai_cluster.main.id
  model_id               = "cohere.command-r-plus"
  display_name           = "chat-endpoint"
}
```

## Cost Optimization

1. **Start small** - Begin with 5 units, scale based on actual usage
2. **Use On-Demand first** - Validate before committing to DAC
3. **Multi-model endpoints** - Share DAC across multiple use cases
4. **Monitor utilization** - Scale down if consistently under 60%

## Key Metrics to Monitor

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Latency (P99) | <2s | >5s |
| Throughput | >80% capacity | <30% (overprovisioned) |
| Error Rate | <0.1% | >1% |
| Token Usage | Track trends | Sudden spikes |

## Documentation
- [DAC Overview](https://docs.oracle.com/en-us/iaas/Content/generative-ai/ai-cluster.htm)
- [Fine-Tuning Guide](https://docs.oracle.com/en-us/iaas/Content/generative-ai/fine-tuning.htm)
