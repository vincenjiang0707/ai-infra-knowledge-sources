source: https://docs.nvidia.com/dynamo/recipes/benchmarks
lastmod: 2026-09-24T19:58:16.636Z

# Feature Benchmarks

Feature Benchmarks evaluate Dynamo features, topologies, and feature stacks under controlled traffic. Each page states the question, compares deployable configurations, shows how to reproduce the run, and links to the [Recipe](https://docs.nvidia.com/dynamo/dev/recipes/browse) target when one deployment should be used directly.

## Features Under Test

Serving techniques and topology changes benchmarked across the comparisons below.

**KV routing**

Routes traffic to workers with reusable KV cache so TTFT, ITL, and goodput can improve on prefix-heavy workloads.

**Prefill/decode split**

Separates prompt prefill and token decode into specialized worker pools for long-context latency and throughput tests.

**WideEP**

Spreads MoE experts across a wider GPU set so expert-heavy requests get more parallel capacity.

**Embedding cache**

Reuses multimodal embeddings, especially repeated images, instead of recomputing them for every request.

**Speculative decoding**

Drafts candidate tokens and verifies them with the target model; Eagle3 is the speculative path used here.

**KV offload**

Moves colder KV blocks to a host-memory tier so longer context can fit without keeping all KV on GPU.

**Frontend decoding**

Moves decode coordination into the Dynamo frontend so routing and cache policy can act before backend execution.

**Multi-node topology**

Runs serving workers across node boundaries to compare aggregate, single-node P/D, and multi-node P/D shapes.

## Agentic coding throughput stack

How much do KV routing, speculative decoding, P/D split, and KV offload gain when composed?

**Kimi-K2.5 NVFP4**

**Traffic**

**Agentic coding trace**

**Hardware**

**24x GB200**

[Open](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/kimi-k2-5-feature-stack)

## Frontend decoding plus embedding cache

How do Dynamo frontend decoding and embedding cache change a single-GPU multimodal benchmark versus vanilla vLLM serve?

**Qwen3.6-35B-A3B FP8**

**Traffic**

**Multimodal sliding window**

**Hardware**

**1x H100 or GB200**

[Open](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/qwen3-6-35b-feature-stack)

## Multimodal embedding cache

How much does enabling the vLLM multimodal embedding cache improve repeated-image traffic on one GB200 worker?

**Qwen3-VL-30B**

**Traffic**

**80% image reuse**

**Hardware**

**1x GB200**

[Open](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/qwen3-vl-embedding-cache)

## KV-aware routing + prefill/decode split

Does disaggregated KV-aware routing reduce TTFT and ITL compared with aggregated round-robin routing?

**Qwen3-32B**

**Traffic**

**Mooncake prefix reuse**

**Hardware**

**16x H200**

[Open](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/qwen3-32b-kv-routing)