source: https://docs.nvidia.com/dynamo/zh-CN/recipes/deepseek-v4-flash
lastmod: 2026-09-24T19:58:16.636Z

DeepSeek-V4-Flash


DeepSeek-V4-Flash

Serve DeepSeek-V4-Flash with Dynamo and vLLM — aggregated or disaggregated, on B200 or H200, tuned for the agentic workload.

Each target below is an agentic-workload vLLM deployment of DeepSeek-V4-Flash — a MoE model (284B total / 13B active) with hybrid CSA + HCA attention, FP8 KV cache, and KV-aware routing. B200 serves the `nvidia/DeepSeek-V4-Flash-NVFP4`

checkpoint; H200 serves the public `deepseek-ai/DeepSeek-V4-Flash`

. Pick your GPU and topology; every command on this page updates to match. Text only; reasoning + tool calling supported.

Choose your deployment target

**Checkpoint**nvidia/DeepSeek-V4-Flash-NVFP4

**GPUs**4x B200, TP4 + EP

**MoE / KV**FLASHINFER_TRTLLM, FP8 KV (block 256)

**Routing**KV-aware, prefix caching

**Context**1,048,576

**Checkpoint**nvidia/DeepSeek-V4-Flash-NVFP4

**GPUs**12x B200 — 2P1D (2 prefill + 1 decode, TP4 each)

**MoE / KV**FLASHINFER_TRTLLM, FP8 KV (block 256)

**Transfer**NIXL over RDMA/GDR

**Context**1,048,576

**Checkpoint**deepseek-ai/DeepSeek-V4-Flash

**GPUs**4x H200, DP4 + TP1 + EP

**MoE / spec**MARLIN (FLASHINFER_MLA attn), MTP-1

**Routing**KV-aware, prefix caching

**Context**1,048,576

**Checkpoint**deepseek-ai/DeepSeek-V4-Flash

**GPUs**28x H200 — 4P3D (DP4+TP1+EP per worker)

**MoE / spec**MARLIN, decode MTP-1

**Transfer**NIXL over RDMA/GDR

**Context**1,048,576

## Prerequisites

- A Kubernetes cluster with the Dynamo Platform (operator) installed.

**4x B200**(aggregated) or**12x B200**(disaggregated, 2P1D) available.- A Hugging Face token with access to
`nvidia/DeepSeek-V4-Flash-NVFP4`

.

**4x H200**(aggregated) or**28x H200**(disaggregated, 4P3D) available.- A Hugging Face token with access to
`deepseek-ai/DeepSeek-V4-Flash`

.

- The
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.3.0`

image (pinned in each`deploy.yaml`

).

Create the namespace and token secret:

Edit cluster-specific values before applying: `storageClassName`

in `model-cache/model-cache.yaml`

(a RWX class). For **disaggregated** targets, also set `VLLM_GPU_NIC_PCIE_MAPPING`

in the manifest to your node’s per-rank affine NICs — see [Per-rank NIC mapping](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md#per-rank-nic-mapping-b200--h200-disaggregated).

## Deploy

Create storage, download the checkpoint into the PVC, then apply the target’s `deploy.yaml`

:

There is one download Job per checkpoint, because the PVC holds one, not both. B200 serves the NVFP4 checkpoint; every other variant serves the public one.

The workers mount the PVC read-only with `HF_HUB_OFFLINE=1`

, so they cannot fetch a checkpoint the Job did not download. Downloading the checkpoint for the other SKU leaves the worker unable to start.

To switch a populated PVC to the other checkpoint: stop the workers, delete the PVC, re-apply `model-cache.yaml`

, then apply the other Job. The two Jobs have distinct names, so applying the second one does not collide with the first.

First launch loads weights and warms CUDA graphs; the startup probes allow for it.

## Smoke Test

The `model`

field must be the **served model name for your SKU** (the `--served-model-name`

in the deploy): B200 serves `nvidia/DeepSeek-V4-Flash-NVFP4`

, H200 serves `deepseek-ai/DeepSeek-V4-Flash`

.

Flash reasons by default: the chain-of-thought fills `message.reasoning_content`

and the answer fills `message.content`

. With too small a `max_tokens`

the budget is spent on reasoning before any `content`

(`content: null`

, `finish_reason: "length"`

) — expected; raise `max_tokens`

.

## Benchmark

The shared [ perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/perf/perf.yaml) replays the agentic MoonTrace (64K avg ISL / 400 OSL, 90% KV reuse) with AIPerf against the deployed frontend. Point

`ENDPOINT`

at `${DGD}-frontend:8000`

and apply it:## Compare All Targets

## Notes

**Reasoning / tool parsers**are wired via the Dynamo variants (`--dyn-reasoning-parser deepseek_v4`

,`--dyn-tool-call-parser deepseek_v4`

); the engine-native parsers do not feed the Dynamo OpenAI renderer.**Disaggregated**targets require the per-rank NIC map (`VLLM_GPU_NIC_PCIE_MAPPING`

) for GPU-Direct RDMA KV transfer; B200 ships`rdma/shared_ib`

, H200 ships`rdma/ib`

. See the[top-level recipe README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md#per-rank-nic-mapping-b200--h200-disaggregated).**AGG scales by independent single-replica DGDs**— KV-routed multi-replica AGG does not improve per-GPU throughput.- Day-0 / GB200 SGLang variants exist in the recipe tree but are experimental (dev images) and not shown here.

## Source

- Recipe README:
[recipes/deepseek-v4/deepseek-v4-flash/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/deepseek-v4-flash/README.md) - Top-level DeepSeek-V4 README (shared workloads, NIC mapping, limitations):
[recipes/deepseek-v4/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md) - Manifests:
[vllm/](https://github.com/ai-dynamo/dynamo/tree/main/recipes/deepseek-v4/deepseek-v4-flash/vllm)and shared[perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/perf/perf.yaml)