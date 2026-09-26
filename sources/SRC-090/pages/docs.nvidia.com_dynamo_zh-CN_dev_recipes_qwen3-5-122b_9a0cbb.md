source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/qwen3-5-122b
lastmod: 2026-09-24T19:58:16.636Z

Qwen3.5-122B-A10B


Qwen3.5-122B-A10B

Serve Qwen3.5-122B-A10B with Dynamo and vLLM on B200 or H200 for long-context agentic workloads.

All four targets below are Dynamo + vLLM deployments of Alibaba’s Qwen3.5-122B-A10B — a 122B total / 10B active hybrid MoE combining Gated DeltaNet linear attention with full attention every fourth layer — tuned for an agentic workload (64K median ISL / 400 median OSL, 90% KV cache hit) with KV-aware routing. B200 runs the NVFP4 checkpoint at TP1; H200 runs FP8, where the weights leave less room for paged KV, so the aggregated profile shards to TP2 and adds MTP speculative decoding. Aggregated is the recommended path on both SKUs. Pick your target; every command on this page updates to match.

Choose your deployment target

**Checkpoint**Qwen/Qwen3.5-122B-A10B-FP8

**Precision**FP8 weights, BF16 KV

**GPUs**2x H200 per replica,

`replicas: 2`

(4x)**Parallelism**TP2

**Spec decode**MTP, 3 tokens

**Routing**KV-aware

**Checkpoint**Qwen/Qwen3.5-122B-A10B-FP8

**Precision**FP8 + FP8 KV

**GPUs**1x H200 prefill + 2x H200 decode

**Parallelism**TP1 per worker

**Spec decode**None — see Limitations

**Routing**KV-aware, NIXL/UCX over IB

**Checkpoint**nvidia/Qwen3.5-122B-A10B-NVFP4

**Precision**NVFP4 + FP8 KV

**GPUs**1x B200 per replica,

`replicas: 2`

(2x)**Parallelism**TP1

**Spec decode**None

**Routing**KV-aware

**Checkpoint**nvidia/Qwen3.5-122B-A10B-NVFP4

**Precision**NVFP4 + FP8 KV

**GPUs**1x B200 prefill + 2x B200 decode

**Parallelism**TP1 per worker

**Spec decode**None

**Routing**KV-aware, NIXL/UCX over IB

## Prerequisites

- Dynamo Platform installed on the target cluster with DGD CRDs served.
- A Hugging Face token stored as
`hf-token-secret`

. The checkpoint is public and Apache-2.0. - A
`model-cache`

PVC (ReadWriteMany), populated with the manifests in`model-cache/`

.

- GPU-local RDMA NICs exposed to pods (an
`rdma/ib`

device plugin) for NIXL KV transfer.

## Deploy

Create the cache and download the checkpoint. Set `storageClassName`

in `model-cache.yaml`

to a ReadWriteMany class first.

Deploy `replicas: 2`

or more so the KV-aware router has replicas to route shared prefixes across. Each replica is TP2, so a full 8x H200 node runs `replicas: 4`

.

Deploy `replicas: 2`

or more so the KV-aware router has replicas to route shared prefixes across. Each replica is TP1, so a full 8x B200 node runs `replicas: 8`

.

First cold starts take 30-45 minutes while the runtime loads the weights and captures CUDA graphs; a measured cold load spent 28.5 minutes on weights alone before graph capture began.

## Smoke Test

Both SKUs serve the model as `Qwen/Qwen3.5-122B-A10B`

regardless of the underlying checkpoint.

## Benchmark

The benchmark replays a Mooncake-format agentic trace through AIPerf.

See [nvfp4/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.5-122b/nvfp4/perf/README.md) for the full workflow.

Edit `ENDPOINT`

and `CONCURRENCY`

in the Job to select a target — aggregated at c64, disaggregated at c18. See [fp8/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.5-122b/fp8/perf/README.md) for the full workflow.

AIPerf builds its replay schedule from a `timestamp`

field. The shipped trace rows have none, and without one AIPerf replays a small default instead of the whole file, so add one before staging the trace on the PVC:

Confirm a run replayed the whole file: `Request Count`

in `profile_export_aiperf.csv`

should be about 3,411, plus roughly 130 rows that exceed the 262,144-token context and return errors.

## Expected Performance

Measured on the 3,541-request agentic Mooncake trace, block size 512, closed-loop. SLA: P50 TTFT under 5 s and P50 output at or above 50 tok/s/user. Each target is reported at its highest SLA-passing concurrency.

## Compare All Targets

Aggregated leads on both SKUs at the same SLA: 1173.2 against 916.6 output tok/s per GPU on B200, 720.3 against 256.5 on H200. **Aggregated is the recommended profile; the disaggregated targets are a functional reference rather than a throughput recommendation.** At 90% KV-cache hit the dedicated prefill worker has little to do yet emits no output tokens, and both disaggregated targets pay ~7% for `--no-async-scheduling`

on vLLM < 0.26.0. MTP runs on H200 aggregated only — H200 disaggregated gives it up, and neither B200 profile runs it. Choose disaggregation to scale prefill and decode independently, or for a workload with a lower cache-hit rate.

## Notes

- Worker
`--block-size`

must match the frontend`--kv-cache-block-size`

. If they diverge, prefix hashing does not line up and KV-aware routing silently degrades toward round-robin. - The H200 aggregated target runs
`--kv-cache-dtype auto`

; the disaggregated targets and both B200 targets use`fp8`

. FP8 KV costs compute and only pays back when the cache is the binding constraint, which it is not at TP2.

- Ship the
`speculative-config`

ConfigMap key; benchmark with`speculative-config-synthetic`

, which forces the acceptance length of 2.937 measured against real text. Real MTP reports about 3.2 on this trace because the Mooncake rows synthesise prompts from`hash_ids`

, which the draft predicts more easily than real text.

## Limitations

- Prefill and decode must use the same tensor-parallel size when disaggregated — asymmetric sharding fails the NIXL transfer with a block-size mismatch.
- MTP is not supported with disaggregation on this architecture. NIXL’s Mamba conv-state transfer needs
`VLLM_SSM_CONV_STATE_LAYOUT=DS`

, which conflicts with the`mamba_cache_mode='align'`

that MTP plus prefix caching forces ([vllm#38898](https://github.com/vllm-project/vllm/issues/38898)).

- Disaggregated decode requires
`--no-async-scheduling`

on vLLM earlier than 0.26.0. Without it the KV-block zeroing kernel races the NIXL RDMA write and silently erases transferred KV. The flag costs about 7% throughput and can be dropped on a runtime shipping vLLM 0.26.0 or later.