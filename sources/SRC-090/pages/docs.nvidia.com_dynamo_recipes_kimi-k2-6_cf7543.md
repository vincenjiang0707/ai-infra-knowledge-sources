source: https://docs.nvidia.com/dynamo/recipes/kimi-k2-6
lastmod: 2026-09-24T19:58:16.636Z

Kimi-K2.6


Kimi-K2.6

Serve moonshotai/Kimi-K2.6 with Dynamo and vLLM, tuned per GPU and workload.

Each target below is a validated aggregated vLLM deployment of Kimi-K2.6 — text + image input, reasoning, and tool calling — with KV-aware routing, Eagle3 MLA speculative decoding, and LMCache CPU KV-cache offload, benchmarked to roughly 50 output tok/s per user on its trace. Pick your GPU and workload; every command on this page updates to match.

Choose your deployment target

**Checkpoint**nvidia/Kimi-K2.6-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200 per worker, TP4

**MoE backend**FlashInfer-TRTLLM

**Attention**TokenSpeed MLA

**Workload**Chat, 70% KV reuse

**Checkpoint**nvidia/Kimi-K2.6-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200 per worker, TP4

**MoE backend**FlashInfer-TRTLLM

**Attention**TokenSpeed MLA

**Workload**Agentic, 64K-median ISL, 90% KV reuse

**Checkpoint**moonshotai/Kimi-K2.6 (native INT4)

**Precision**INT4

**GPUs**8x H200 per worker, TP8

**MoE backend**Marlin

**Attention**FlashAttention MLA

**Workload**Chat, 70% KV reuse

**Checkpoint**moonshotai/Kimi-K2.6 (native INT4)

**Precision**INT4

**GPUs**8x H200 per worker, TP8

**MoE backend**Marlin

**Attention**FlashAttention MLA

**Workload**Agentic, 64K-median ISL, 90% KV reuse

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**4x B200 per worker replica**available (results below were measured at 4 replicas). - A Hugging Face token with access to
`nvidia/Kimi-K2.6-NVFP4`

and`lightseekorg/kimi-k2.6-eagle3-mla`

.

- A Kubernetes cluster with the Dynamo platform installed and
**8x H200 per worker replica**available (results below were measured at 4 replicas). - A Hugging Face token with access to
`moonshotai/Kimi-K2.6`

and`lightseekorg/kimi-k2.6-eagle3-mla`

.

Create the namespace and token secret:

Edit namespace, storage class, image tags, node selectors, resource claims, and cluster-specific placement in the manifests before applying them.

## Deploy

Prepare the model cache and download the checkpoint and Eagle3 head:

Then deploy:

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

A single AIPerf trace-replay Job ([ perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/perf/perf.yaml)) covers every target — only

`ENDPOINT`

and `TRACE_FILE`

change. Before running it: point the worker’s `SPECULATIVE_CONFIG`

at the `speculative-config-synthetic`

ConfigMap key (synthetic Eagle3 acceptance, AL=2.49), set worker `replicas`

to your target, and stage the traces from [onto the](https://github.com/ai-dynamo/dynamo/tree/main/recipes/kimi-k2.6/perf/traces)

`recipes/kimi-k2.6/perf/traces/`

`model-cache`

PVC:Set `ENDPOINT`

to `kimi-k26-agg-b200-chat-frontend:8000`

and `TRACE_FILE`

to the chat trace, then apply. The Job wraps this AIPerf run:

Set `ENDPOINT`

to `kimi-k26-agg-b200-agentic-frontend:8000`

and `TRACE_FILE`

to the agentic trace, then apply. The Job wraps this AIPerf run:

Set `ENDPOINT`

to `kimi-k26-agg-h200-chat-frontend:8000`

and `TRACE_FILE`

to the chat trace, then apply. The Job wraps this AIPerf run:

Set `ENDPOINT`

to `kimi-k26-agg-h200-agentic-frontend:8000`

and `TRACE_FILE`

to the agentic trace, then apply. The Job wraps this AIPerf run:

15% and 30% trace subsets are provided for shorter runs. To sweep concurrencies, delete the DGD worker pods between runs so residual KV-cache and prefix-cache state does not skew results — see the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/perf/README.md) for the full workflow, artifact layout, and tunable environment variables.

## Expected Performance

Each target is tuned for its workload shape at a 50 tok/s/user interactivity target:

Measured results below were collected by replaying the **15% trace subsets** (`*_short_15perc.jsonl`

) with 4 worker replicas per deployment; your selected target’s row is highlighted:

## Compare All Targets

All four targets serve `moonshotai/Kimi-K2.6`

on aggregated vLLM 0.21.0 with KV-aware routing, Eagle3 MLA speculative decoding (3 draft tokens), and LMCache CPU KV-cache offload. They differ in checkpoint, parallelism, kernel backends, and the trace they are benchmarked against:

## Notes

- Dynamo’s KV cache router does not support all LMCache KV events, so routing can be sub-optimal.
- Some 400 HTTP errors raised by workers on invalid inputs can surface as 500 errors through the frontend.
- B200 targets run
`nvidia/Kimi-K2.6-NVFP4`

with FP8 KV cache; H200 targets run the native INT4`moonshotai/Kimi-K2.6`

checkpoint. Both serve under the name`moonshotai/Kimi-K2.6`

. - The chat- and agentic-tuned deployments for a given SKU share the same engine configuration; they are separate targets because each is benchmarked and sized against its own trace, and either trace can be replayed against either DGD.
- For benchmarking, swap
`SPECULATIVE_CONFIG`

to the`speculative-config-synthetic`

key so Eagle3 acceptance is synthetic and deterministic (AL=2.49); production deployments use the standard`speculative-config`

key.

## Source

- Source README:
[recipes/kimi-k2.6/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/README.md) - Benchmark README:
[recipes/kimi-k2.6/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/perf/README.md)and[recipes/kimi-k2.6/perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/perf/perf.yaml) - B200 chat:
[recipes/kimi-k2.6/vllm/agg-b200-chat/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/vllm/agg-b200-chat/deploy.yaml) - H200 chat:
[recipes/kimi-k2.6/vllm/agg-h200-chat/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/vllm/agg-h200-chat/deploy.yaml) - B200 agentic:
[recipes/kimi-k2.6/vllm/agg-b200-agentic/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/vllm/agg-b200-agentic/deploy.yaml) - H200 agentic:
[recipes/kimi-k2.6/vllm/agg-h200-agentic/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/vllm/agg-h200-agentic/deploy.yaml) - Setup assets:
[recipes/kimi-k2.6/model-cache/model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/model-cache/model-cache.yaml)and[recipes/kimi-k2.6/model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/model-cache/model-download.yaml)