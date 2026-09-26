source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/recipes/qwen3-32b
lastmod: 2026-09-23T23:30:39.914Z

Qwen3-32B


Qwen3-32B

Serve Qwen3-32B with Dynamo and vLLM — disaggregated serving with KV-aware routing for multi-turn conversational traffic.

This recipe deploys `Qwen/Qwen3-32B`

on 16x H200 with prefill/decode disaggregation and KV-aware routing — the winning configuration from the [KV routing A/B benchmark](https://docs.nvidia.com/dynamo/v1.3.0/benchmarks/qwen3-32b-kv-routing), validated against a real Mooncake conversation trace (12,031 requests, 12K average input length, 36.64% cache efficiency). It fits multi-turn conversational workloads where requests share long prefixes that KV-aware routing can exploit.

Deployment target

**Checkpoint**Qwen/Qwen3-32B

**Precision**BF16

**GPUs**16x H200, 2 nodes: 6x TP2 prefill + 2x TP2 decode

**Techniques**Disaggregated P/D + KV-aware routing

**Workload**Multi-turn conversation with prefix reuse (Mooncake trace, 12K avg ISL / 343 avg OSL)

**SLA**Goodput at TTFT 2s / ITL 25ms

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**16x H200 across 2 nodes**available. - A Hugging Face token with access to
`Qwen/Qwen3-32B`

.

Create the namespace and token secret:

Edit namespace, storage class, image tags, node selectors, resource claims, Hugging Face secrets, and cluster-specific placement before applying these manifests.

## Deploy

Prepare the model cache and download the checkpoint (`cache.yaml`

creates the `model-cache`

, `compilation-cache`

, and `perf-cache`

PVCs):

Then deploy:

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

The checked-in `perf.yaml`

downloads the Mooncake conversation trace (FAST25; 12,031 requests over ~59 minutes) and replays it on a fixed schedule, so throughput is set by the trace and latency is what you measure. It wraps this AIPerf run:

Results land on the `perf-cache`

PVC under `/perf-cache/artifacts/`

.

## Related Feature Benchmarks

[Qwen3-32B KV routing A/B](https://docs.nvidia.com/dynamo/v1.3.0/benchmarks/qwen3-32b-kv-routing)— the evidence behind this recipe: this configuration vs. aggregated round-robin on the same trace.

## Notes

- The aggregated round-robin manifest is a benchmark control and lives on the related Feature Benchmarks page, not in this recipe.
- For 80 GB GPUs (H100), use the
[Qwen3-32B FP8 recipe](https://docs.nvidia.com/dynamo/v1.3.0/recipes/qwen3-32b-fp8)— BF16 weights are ~64 GB and leave little KV headroom.

## Source

- Source README:
[recipes/qwen3-32b/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/qwen3-32b/README.md) - Deploy and benchmark:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/qwen3-32b/vllm/disagg-kv-router/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/qwen3-32b/vllm/disagg-kv-router/perf.yaml) - Setup assets:
[model-cache/cache.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/qwen3-32b/model-cache/cache.yaml)and[model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/qwen3-32b/model-cache/model-download.yaml)