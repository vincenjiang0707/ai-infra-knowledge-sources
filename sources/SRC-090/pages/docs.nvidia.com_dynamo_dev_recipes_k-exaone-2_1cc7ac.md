source: https://docs.nvidia.com/dynamo/dev/recipes/k-exaone-2
lastmod: 2026-09-24T19:58:16.636Z

K-EXAONE 2.0


K-EXAONE 2.0

Serve LG AI Research’s K-EXAONE 2.0 750B-A37B in NVFP4 with Dynamo and vLLM on B200.

This recipe serves `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4`

— a 764.5B-parameter MoE with ~37B active per token, 256 experts at top-8 routing, and hybrid attention (20 full-attention plus 58 sliding-attention layers) — on B200 with vLLM. Multi-Token Prediction is enabled, and the MoE kernel is pinned to FLASHINFER_CUTLASS for correctness. Pick aggregated or disaggregated; every command on this page updates to match.

Choose your deployment target

**Checkpoint**LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4

**Precision**NVFP4 W4A4 + FP8 KV cache

**GPUs**4x B200

**Parallelism**TP4

**Spec decoding**MTP, draft length 2

**Workload**8K ISL / 1K OSL chat trace, designed for ~70% prefix reuse (~8.8% achieved here)

**Checkpoint**LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4

**Precision**NVFP4 W4A4 + FP8 KV cache

**GPUs**8x B200, 4 prefill + 4 decode

**Parallelism**TP4 prefill, TP4 decode

**KV transfer**NIXL over UCX, InfiniBand RDMA

**Workload**8K ISL / 1K OSL chat trace, ~70% prefix reuse

## Prerequisites

- A Kubernetes cluster with the Dynamo Operator.
- A
`ReadWriteMany`

storage class with at least 700 GB free — the checkpoint is ~530 GB on disk. - A Hugging Face token with access to
`LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4`

.

**4x B200**on a single node.

**8x B200**, ideally on a single node. Prefill and decode are co-located by a*preferred*pod affinity so the KV hop stays on one fabric where capacity allows; a required affinity deadlocks the operator’s gang scheduling. KV moves over IB RDMA, so a split placement still works, just slower.- An
**RDMA device plugin**exposing InfiniBand HCAs as a Kubernetes extended resource. The manifest requests`rdma/shared_ib`

; the name is cluster-specific — see[Notes](https://docs.nvidia.com/dynamo/dev/recipes/k-exaone-2#notes).

## Deploy

Create the namespace, token secret, and storage:

First start takes **40–120 minutes**: 53 shards load, then autotune, then CUDA-graph capture. Silence is not a hang — watch the worker log for shard progress.

## Smoke Test

This is a reasoning model. Use temperature 0.6 rather than greedy decoding, give it a generous token budget, and read `.content // .reasoning_content`

— reasoning consumes the budget before the final answer, so a short cap prints `null`

on a perfectly healthy deployment.

## Benchmark

Trace replay with AIPerf against the Mooncake 8K/1K/70%-reuse chat trace. See [ perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/k-exaone-2.0/perf/README.md) for staging the trace, running a concurrency sweep, and fetching artifacts.

## Expected Performance

Mooncake chat trace replay, 1,805 requests, at the highest concurrency meeting a joint gate of E2E ≥ 50 tok/s/user **and** TTFT p50 < 5 s, where `E2E = OSL / (TTFT_p50 + OSL × ITL)`

.

Measured KV reuse on this workload is 8.8%. That is not a misconfiguration — the trace’s working set is roughly 42x oversubscribed against TP4’s KV capacity, so blocks are evicted before they can be reused.

Mooncake chat trace replay, 1,805 requests. Concurrency 14 is this target’s operating point — the highest concurrency meeting both legs of the gate.

This is level with the aggregated target’s 87 tok/s/GPU under the same gate, so disaggregation is an SLA and scaling choice for this model rather than a throughput win or loss. It buys per-token latency (ITL 15.98 ms against the aggregated recipe’s 19.15 ms) and lets prefill and decode scale independently, for twice the GPUs. Lowering concurrency trades throughput for interactivity — at C=7 the same deployment gives 55 tok/s/GPU but E2E 70.6 tok/s/user and TTFT p50 1,018 ms.

38 of the trace’s 1,805 requests are rejected in every run, at every concurrency: the trace is multi-turn and its accumulated prompts reach 614,440 tokens against this checkpoint’s 262,144-token ceiling, so they return HTTP 400 and are excluded from the metrics.

## Compare All Targets

## Notes

-
**The MoE backend pin is a correctness requirement.**vLLM’s`auto`

selection picks FLASHINFER_TRTLLM, which silently corrupts long-form output on this checkpoint — fluent, plausible, wrong, with no error. Both manifests pin`--kernel-config '{"moe_backend":"FLASHINFER_CUTLASS"}'`

; the pinned kernel is slower and that cost is inside the figures above. -
**Use the**Plain`--dyn-*`

parser flags.`--reasoning-parser`

and`--tool-call-parser`

configure the engine only and never reach the Dynamo frontend, so tool calling silently does nothing. -
**TP4 is both the floor and the optimum.**~530 GB of weights does not fit TP2 on 180 GB B200s, and TP8 — despite 5.7x the KV capacity — is slower per GPU, because this model is communication-bound rather than KV-capacity-bound. -
**Disaggregated: prefill and decode must agree**on speculative decoding and block size. A mismatch changes KV block geometry and produces silent garbage rather than an error.`--max-num-seqs`

is the deliberate exception: 32 on prefill, 256 on decode. -
**The RDMA extended-resource name is cluster-specific.**The manifest requests`rdma/shared_ib`

; other clusters expose`rdma/ib`

or`rdma/rdma_shared_device_a`

. Prefer a shared flavour — with an exclusive-mode resource, two co-located workers each claiming HCAs can deadlock NCCL bootstrap. Verify the transport engaged before trusting any measurement:Divide

`_sum`

by`_count`

: a ~1 GB KV transfer should take milliseconds, not seconds. -
**Context length is 262,144**, the model’s native maximum. The checkpoint uses unscaled rope, so longer contexts would require a rope-scaling override with unvalidated accuracy.