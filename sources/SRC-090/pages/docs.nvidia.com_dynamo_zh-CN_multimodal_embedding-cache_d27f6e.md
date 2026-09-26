source: https://docs.nvidia.com/dynamo/zh-CN/multimodal/embedding-cache
lastmod: 2026-09-24T19:58:16.636Z

# Embedding Cache

Cache vision encoder embeddings to skip re-encoding repeated multimodal content

## Overview

The embedding cache (or encoder cache) is a CPU-side LRU cache that stores vision encoder outputs. When the same multimodal content, such as an image or video, appears in multiple requests, the cached embedding is reused instead of running the vision encoder again. This reduces GPU load on the encoder and lowers latency for repeated content.

Embedding cache is separate from the KV cache, which reuses attention key/value state after prefill to skip prefill and go straight to decode. For KV cache reuse and routing, see [Multimodal KV Routing](https://docs.nvidia.com/dynamo/multimodal/multimodal-kv-routing).

## When to Use

Use the embedding cache when your workload includes repeated multimodal content across requests. Common scenarios:

- Product catalog queries or multi-turn chat where users ask about the same image(s).
- Document processing pipelines that reference shared diagrams or figures
- Video QA or benchmark workloads that repeatedly reference the same clips

If your workload consists entirely of unique multimodal content, the cache provides no benefit.

## Configuration

###### vLLM

###### TensorRT-LLM

###### SGLang

Launch a disaggregated multimodal deployment with the embedding cache enabled:

Set `--multimodal-embedding-cache-capacity-gb`

based on your expected working set of unique multimodal content. A larger cache holds more embeddings but consumes more host memory.

See the backend-specific documentation ([vLLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/vllm-multimodal#embedding-cache), [TRT-LLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/tensorrt-llm-multimodal#embedding-cache)) for more details.

## How It Works

In vLLM/TRT-LLM disaggregated flows, the prefill worker owns the CPU-side LRU cache. On a hit, the encode worker is skipped entirely. On a miss, the encode worker produces the embedding, transfers it via NIXL, and the prefill worker saves it to the cache.

In SGLang E/PD, the encode worker owns the cache and skips re-encoding on cache hits before forwarding the cached image or video embeddings downstream.

## Support Matrix

This support requires vLLM `0.17.0`

or newer.