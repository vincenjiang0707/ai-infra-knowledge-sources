source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/deepseek-v4-pro-0813
lastmod: 2026-09-24T19:58:16.636Z

DeepSeek-V4-Pro-0813


DeepSeek-V4-Pro-0813

Serve DeepSeek-V4-Pro-0813 with Dynamo and vLLM on GB200 or H200, aggregated or disaggregated, with 1M context.

Each target below is a Dynamo + vLLM deployment of DeepSeek-V4-Pro-0813 — a 1.6T-parameter MoE model with MXFP4-packed routed experts and hybrid sparse attention — with KV-aware routing, FP8 KV cache and prefix caching, running aggregated or with prefill/decode disaggregation. Every target serves the model’s full 1,048,576-token context without CPU KV offload. Pick your GPU architecture and serving topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro-0813

**Precision**MXFP4 experts, FP8 KV

**GPUs**8x GB200 (2 nodes)

**Context**1,048,576 tokens

**Routing**KV-aware

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro-0813

**Precision**MXFP4 experts, FP8 KV

**GPUs**8x GB200 prefill + 8x GB200 decode (1P1D)

**Context**1,048,576 tokens

**Routing**KV-aware, NIXL KV transfer

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro-0813

**Precision**MXFP4 experts, FP8 KV

**GPUs**8x H200, one worker

**Context**1,048,576 tokens

**Routing**KV-aware

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro-0813

**Precision**MXFP4 experts, FP8 KV

**GPUs**8x H200 prefill + 8x H200 decode (1P1D)

**Context**1,048,576 tokens

**Routing**KV-aware, NIXL KV transfer

## Prerequisites

- A Dynamo Platform install on your Kubernetes cluster — see the
[Kubernetes quickstart](https://docs.nvidia.com/dynamo/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`deepseek-ai/DeepSeek-V4-Pro-0813`

. - A ReadWriteMany storage class. The checkpoint is ~832 GiB; the PVC in this recipe requests 1200 Gi.

Eight H200 GPUs on a single node.

Sixteen H200 GPUs across two nodes — one prefill worker and one decode worker, eight GPUs each.

Eight GB200 GPUs across two nodes, connected over NVLink (MNNVL) using a Kubernetes ComputeDomain.

Sixteen GB200 GPUs — eight for prefill and eight for decode, each spanning two nodes over NVLink (MNNVL) using Kubernetes ComputeDomains.

## Deploy

Create the namespace and Hugging Face secret:

Create the model cache and download the checkpoint. Edit `storageClassName`

in `model-cache.yaml`

to a ReadWriteMany class available on your cluster:

Deploy the graph:

Loading the 832 GiB checkpoint takes roughly 15–20 minutes on first start on H200.
GB200 is slower — allow several hours, which is why the GB200 manifests set
`VLLM_ENGINE_READY_TIMEOUT_S: 21600`

and the waits above use a six-hour timeout.

## Smoke Test

Port-forward the frontend and send one request:

This is a reasoning model. The chain of thought is returned in `reasoning_content`

and the answer in `content`

; a small `max_tokens`

can leave `content`

empty because the budget is consumed by reasoning.

## Benchmark

See [ perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/deepseek-v4-pro-0813/perf/README.md) for the full workflow — staging the Mooncake trace on the PVC, running the AIPerf trace-replay Job, sweeping concurrency, and fetching artifacts.

## Expected Performance

Agentic Mooncake trace, 64K median ISL / 400 median OSL, ~90% KV reuse. SLA is user output ≥ 50 tok/s.

## Compare All Targets

## Notes

**One config per topology serves both workloads.**The 64K agentic workload and 1M-context requests use the same deployment; GPU KV holds roughly 3.1M tokens, about 3x a full 1M request, so no CPU KV offload is needed. At 1M context, time-to-first-token is minutes — treat it as a batch capability, not an interactive one.**FP8 KV cache is required, not a tuning choice.**vLLM asserts`DeepseekV4 fp8_ds_mla layout only supports fp8 kv-cache`

; the routed experts ship MXFP4 in the checkpoint. Serving precision is fixed by the model.**Speculative decoding is not enabled**on the H200 targets. It measured a large regression on this checkpoint.**Different checkpoint from**See the`DeepSeek-V4-Pro`

.[DeepSeek-V4-Pro recipe](https://docs.nvidia.com/dynamo/recipes/model-recipes/deepseek-v4-pro)for that model. The two use different Hugging Face repositories and must not share a model cache.

## Source

- Recipe:
`recipes/deepseek-v4/deepseek-v4-pro-0813`

- Benchmark:
`perf/`