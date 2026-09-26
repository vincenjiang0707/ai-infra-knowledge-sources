source: https://docs.nvidia.com/dynamo/dev/recipes/qwen3-32b-fp8
lastmod: 2026-09-24T19:58:16.636Z

Qwen3-32B FP8


Qwen3-32B FP8

Serve Qwen/Qwen3-32B-FP8 with Dynamo on TensorRT-LLM or vLLM, aggregated or disaggregated.

Each target below is a validated FP8 deployment of Qwen3-32B — from a 2-GPU TensorRT-LLM aggregate to 8-GPU disaggregated prefill/decode setups on TensorRT-LLM or vLLM — each with a checked-in AIPerf benchmark Job. The targets use different traffic shapes and GPU counts, so this page is not a backend benchmark. Pick your target; every command on this page updates to match.

Choose your deployment target

**Checkpoint**Qwen/Qwen3-32B-FP8

**GPUs**2x H100/H200/A100, single TP2 worker

**Routing**Round-robin

**Techniques**CUDA graphs, FP8 KV cache

**Workload**4K ISL / 500 OSL, concurrency 4

**Checkpoint**Qwen/Qwen3-32B-FP8

**GPUs**8x H100/H200/A100

**Topology**4x prefill (TP1) + 2x decode (TP2)

**Routing**Round-robin

**Workload**4K ISL / 500 OSL, concurrency 48

**Checkpoint**Qwen/Qwen3-32B-FP8

**GPUs**8x H100/H200/A100, single node

**Topology**2x prefill (TP2) + 1x decode (TP4)

**KV transfer**NIXL (NixlConnector)

**Workload**2K ISL / 500 OSL, concurrency 8

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**2x H100/H200/A100-class GPUs**available. - A Hugging Face token with access to
`Qwen/Qwen3-32B-FP8`

.

- A Kubernetes cluster with the Dynamo platform installed and
**8x H100/H200/A100-class GPUs**available. - A Hugging Face token with access to
`Qwen/Qwen3-32B-FP8`

.

- A Kubernetes cluster with the Dynamo platform installed and
**8x H100/H200/A100-class GPUs on a single node**— all prefill and decode workers must be co-located for NIXL KV transfer. - A Hugging Face token with access to
`Qwen/Qwen3-32B-FP8`

.

Create the namespace and token secret:

Edit namespace, storage class, image tags, node selectors, resource claims, and cluster-specific placement in the manifests before applying them.

## Deploy

Prepare the model cache and download the checkpoint:

Then deploy:

A single TP2 TensorRT-LLM worker with round-robin routing and CUDA graphs enabled:

4x prefill workers (TP1) and 2x decode workers (TP2):

2x prefill workers (TP2) and 1x decode worker (TP4) using NixlConnector KV transfer; all workers must land on one node:

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

Each target ships its own `perf.yaml`

AIPerf Job, sized at a fixed concurrency per GPU with `request-count = 10x concurrency`

. Artifacts land on the `model-cache`

PVC under `/model-cache/perf`

.

The Job wraps this AIPerf run — 4K ISL / 500 OSL at concurrency 4 (2 per GPU x 2 GPUs):

The Job wraps this AIPerf run — 4K ISL / 500 OSL at concurrency 48 (6 per GPU x 8 GPUs):

The Job wraps this AIPerf run — 2K ISL / 500 OSL at concurrency 8 (1 per GPU x 8 GPUs); note the shorter input length than the TRT-LLM targets:

## Compare All Targets

All three targets serve `Qwen/Qwen3-32B-FP8`

; they differ in runtime, GPU count, topology, and benchmark traffic:

## Notes

- This page is the FP8 alternative to the BF16
[Qwen3-32B](https://docs.nvidia.com/dynamo/dev/recipes/qwen3-32b)recipe. - The TRT-LLM and vLLM targets use different traffic shapes (4K vs 2K ISL) and different GPU counts; normalize traffic before making backend performance claims.
- The aggregated config uses CUDA graphs for optimized inference, and KV cache uses FP8 dtype for memory efficiency.
`--max-model-len 8192`

is set in`vllm/disagg/deploy.yaml`

for A100 40 GB compatibility; remove or increase it on H100/H200.- Update
`storageClassName`

in`model-cache/model-cache.yaml`

before deploying.

## Source

- Source README:
[recipes/qwen3-32b-fp8/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/README.md) - TRT-LLM aggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/trtllm/agg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/trtllm/agg/perf.yaml) - TRT-LLM disaggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/trtllm/disagg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/trtllm/disagg/perf.yaml) - vLLM disaggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/vllm/disagg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/vllm/disagg/perf.yaml) - Setup assets:
[model-cache/model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/model-cache/model-cache.yaml)and[model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-32b-fp8/model-cache/model-download.yaml)