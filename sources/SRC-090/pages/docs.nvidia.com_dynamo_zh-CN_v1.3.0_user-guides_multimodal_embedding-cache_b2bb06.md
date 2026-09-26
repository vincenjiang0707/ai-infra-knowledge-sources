source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/multimodal/embedding-cache
lastmod: 2026-09-23T23:30:39.914Z

# Embedding Cache

Cache vision encoder embeddings to skip re-encoding repeated multimodal content

## Overview

The embedding cache is a CPU-side LRU cache that stores vision encoder outputs. When the same multimodal content, such as an image or video, appears in multiple requests, the cached embedding is reused instead of running the vision encoder again. This reduces GPU load on the encoder and lowers latency for repeated content.

This feature is also called the **encoder cache**. The embedding cache is separate from the KV cache, which reuses attention key/value state after prefill to skip prefill and go straight to decode. For KV cache reuse and routing, see [Multimodal KV Routing](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/multimodal-kv-routing).

## When to Use

Use the embedding cache when your workload includes repeated multimodal content across requests. Common scenarios:

- Product catalog queries where users ask about the same product images
- Document processing pipelines that reference shared diagrams or figures
- Chat sessions where the same image is discussed across multiple turns, like an architecture diagram in a code-gen use case.
- Video QA or benchmark workloads that repeatedly reference the same clips

If your workload consists entirely of unique multimodal content, the cache provides no benefit.

## Support Matrix

This support requires vLLM `0.17.0`

or newer.

## How It Works

In vLLM/TRT-LLM disaggregated flows, the prefill worker owns the CPU-side LRU cache. On a hit, the encode worker is skipped entirely. On a miss, the encode worker produces the embedding, transfers it via NIXL, and the prefill worker saves it to the cache.

In SGLang E/PD, the encode worker owns the cache and skips re-encoding on cache hits before forwarding the cached image or video embeddings downstream.

**Launch (vLLM):**

**Launch (TRT-LLM):**

## Configuration

Set the capacity based on your expected working set of unique multimodal content. A larger cache holds more embeddings but consumes more host memory.

### Cache-Aware Routing

For SGLang encode/prefill/decode deployments that use `--router-mode device-aware-weighted`

, set both `--multimodal-embedding-cache-capacity-gb`

and `--multimodal-embedding-cache-publisher`

on the encode worker. The publisher sends cache-key additions and removals over the configured event plane so the router can track which workers hold each requested embedding.

When one or more workers hold every distinct embedding-cache key in a request, the router bypasses the CPU-to-non-CPU ratio and selects the least-loaded full-hit worker. Partial cache hits continue through the normal weighted group selection. The publisher is disabled by default and is not needed for round-robin routing or aggregated deployments.

See the backend-specific documentation ([vLLM](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/v-llm-multimodal#embedding-cache), [TRT-LLM](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/tensor-rt-llm-multimodal#embedding-cache)) for more details.