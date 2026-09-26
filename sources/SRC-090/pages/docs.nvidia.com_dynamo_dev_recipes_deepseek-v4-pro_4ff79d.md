source: https://docs.nvidia.com/dynamo/dev/recipes/deepseek-v4-pro
lastmod: 2026-09-24T19:58:16.636Z

DeepSeek-V4-Pro


DeepSeek-V4-Pro

Serve DeepSeek-V4-Pro with Dynamo and vLLM — aggregated or disaggregated, on B200 or H200, tuned for the agentic workload.

Each target below is an agentic-workload vLLM deployment of DeepSeek-V4-Pro — a MoE model (1.6T total / 49B active) with hybrid CSA + HCA attention, a Blackwell FP4 indexer cache, and mHC residual connections. B200 serves the `nvidia/DeepSeek-V4-Pro-NVFP4`

checkpoint at the full 1M context; H200 serves the public `deepseek-ai/DeepSeek-V4-Pro`

(FP8), capped at `max_model_len=86016`

by HBM. Pick your GPU and topology; every command updates to match. Text only; reasoning + tool calling supported.

Choose your deployment target

**Checkpoint**nvidia/DeepSeek-V4-Pro-NVFP4

**GPUs**8x B200, TP8 + EP

**MoE / spec**FLASHINFER_TRTLLM, MTP-2

**KV / routing**FP8 KV (block 256), KV-aware

**Context**1,048,576

**Checkpoint**nvidia/DeepSeek-V4-Pro-NVFP4 Recommended

**GPUs**16x B200 — 1P1D (TP8 + EP per worker)

**MoE / spec**FLASHINFER_TRTLLM, decode MTP-2

**Transfer**NIXL over RDMA/GDR

**Context**1,048,576

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro (FP8) Recommended on H200

**GPUs**8x H200, TP8 + EP

**MoE**MARLIN

**KV / routing**FP8 KV (block 256), KV-aware

**Context**86,016 (HBM cap)

**Checkpoint**deepseek-ai/DeepSeek-V4-Pro (FP8)

**GPUs**32x H200 — 1P3D (TP8 + EP per worker)

**MoE**MARLIN

**Transfer**NIXL over RDMA/GDR

**Context**86,016 (HBM cap)

Recommended picks differ by SKU: **B200 → Disaggregated (1P1D)** (highest tok/s/GPU); **H200 → Aggregated** (AGG beats the 1P3D disagg lane). H200 targets are a secondary/best-effort lane on the public FP8 checkpoint.

## Prerequisites

- A Kubernetes cluster with the Dynamo Platform (operator) installed.

**8x B200**(aggregated) or**16x B200**(disaggregated, 1P1D) available.- A Hugging Face token with access to
`nvidia/DeepSeek-V4-Pro-NVFP4`

.

**8x H200**(aggregated) or**32x H200**(disaggregated, 1P3D) available.- A Hugging Face token with access to
`deepseek-ai/DeepSeek-V4-Pro`

.

- The
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.3.0`

image (pinned in each`deploy.yaml`

).

Create the namespace and token secret:

Edit cluster-specific values before applying: `storageClassName`

in `model-cache/model-cache.yaml`

(a RWX class). For **disaggregated** targets, also set `VLLM_GPU_NIC_PCIE_MAPPING`

in the manifest — see [Per-rank NIC mapping](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md#per-rank-nic-mapping-b200--h200-disaggregated).

## Deploy

Create storage, download the checkpoint (~865 GB, 1.5–3 h first apply), then apply the target’s `deploy.yaml`

:

There is one download Job per checkpoint, because each checkpoint is ~865 GB and the PVC holds one, not both. B200 serves the NVFP4 checkpoint; every other variant serves the public FP8 one.

The workers mount the PVC read-only with `HF_HUB_OFFLINE=1`

, so they cannot fetch a checkpoint the Job did not download. Downloading the checkpoint for the other SKU leaves the worker unable to start.

To switch a populated PVC to the other checkpoint: stop the workers, delete the PVC, re-apply `model-cache.yaml`

, then apply the other Job. The two Jobs have distinct names, so applying the second one does not collide with the first.

First launch loads weights across 8 TP ranks and warms CUDA graphs — up to ~90 min; the startup probes allow for it.

## Smoke Test

The `model`

field must be the **served model name for your SKU** (the `--served-model-name`

in the deploy): B200 serves `nvidia/DeepSeek-V4-Pro-NVFP4`

, H200 serves `deepseek-ai/DeepSeek-V4-Pro`

.

Pro emits chain-of-thought into `message.reasoning_content`

and the answer into `message.content`

. Reasoning effort is selected via `chat_template_kwargs`

(`{"thinking":true,"reasoning_effort":"high"|"max"}`

; Think Max needs `--max-model-len >= 393216`

).

## Benchmark

The shared [ perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/perf/perf.yaml) replays the agentic MoonTrace (64K avg ISL / 400 OSL, 90% KV reuse) with AIPerf. Point

`ENDPOINT`

at `${DGD}-frontend:8000`

and apply it:## Compare All Targets

## Notes

**Recommended per SKU:**B200 ships**disaggregated 1P1D**(+6% tok/s/GPU over AGG); H200 ships**aggregated**(AGG > the 1P3D disagg lane). H200 is a secondary/best-effort lane on the public FP8 checkpoint at`max_model_len=86016`

.**Reasoning / tool parsers**are wired via`--dyn-reasoning-parser deepseek_v4`

/`--dyn-tool-call-parser deepseek_v4`

.**Disaggregated**targets require the per-rank NIC map (`VLLM_GPU_NIC_PCIE_MAPPING`

); B200 ships`rdma/shared_ib`

, H200 ships`rdma/ib`

. See the[top-level README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md#per-rank-nic-mapping-b200--h200-disaggregated).- Day-0 / GB200 (vLLM + SGLang, ComputeDomain/MNNVL) variants exist in the recipe tree but are experimental (dev images) and not shown here.

## Source

- Recipe README:
[recipes/deepseek-v4/deepseek-v4-pro/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/deepseek-v4-pro/README.md) - Top-level DeepSeek-V4 README (shared workloads, NIC mapping, limitations):
[recipes/deepseek-v4/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/README.md) - Manifests:
[vllm/](https://github.com/ai-dynamo/dynamo/tree/main/recipes/deepseek-v4/deepseek-v4-pro/vllm)and shared[perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/deepseek-v4/perf/perf.yaml)