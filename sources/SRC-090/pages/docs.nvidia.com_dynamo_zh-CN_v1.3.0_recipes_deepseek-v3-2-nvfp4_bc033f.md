source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/recipes/deepseek-v3-2-nvfp4
lastmod: 2026-09-23T23:30:39.914Z

# DeepSeek V3.2 NVFP4

Serve nvidia/DeepSeek-V3.2-NVFP4 with Dynamo and TensorRT-LLM, disaggregated with KV routing and WideEP on GB200 NVL72.

This recipe deploys DeepSeek V3.2 NVFP4 disaggregated across 32 GB200 GPUs — 2x prefill + 2x decode workers (DEP8) with KV-aware routing and WideEP — for long-context coding traces with heavy prefix reuse (~39.2K avg ISL, 44% KV block hit rate). The aggregated round-robin configuration is the benchmark control and lives on the related Feature Benchmark page.

Deployment target

**Checkpoint**nvidia/DeepSeek-V3.2-NVFP4

**GPUs**32x GB200 across 8 nodes (NVL72, MNNVL)

**Techniques**Disagg, KV-aware routing, WideEP

**Workload**10K-request Mooncake-based coding trace, fixed schedule

**SLA**TTFT 20s / ITL 50ms

## Prerequisites

- A Kubernetes cluster with the Dynamo platform (operator) installed and
**32x GB200 across 8 nodes (NVL72, MNNVL-connected)**available. - A Hugging Face token with access to
`nvidia/DeepSeek-V3.2-NVFP4`

. - The
`nvcr.io/nvidia/ai-dynamo/tensorrtllm-runtime:1.2.1`

image (already pinned in`deploy.yaml`

).

Create the namespace and token secret:

Multinode deployments on MNNVL-connected GB200 clusters typically require a ComputeDomain in your namespace so the DRA scheduler co-locates worker pods on MNNVL-connected nodes — otherwise internode GPU peer memory access fails:

If you rename the ComputeDomain or its `resourceClaimTemplate`

(defaults: `your-compute-domain`

/ `your-compute-domain-channel`

), apply the same names in the deploy YAMLs under `extraPodSpec.resourceClaims`

and `mainContainer.resources.claims`

.

Edit cluster-specific values before applying: `storageClassName`

in `model-cache/model-cache.yaml`

(run kubectl get storageclass), your namespace (perf.yaml hardcodes `namespace: your-namespace`

), and the ComputeDomain claim names.

## Deploy

Create storage, download NVIDIA’s official NVFP4 checkpoint, copy the trace into the PVC, then deploy:

To synthesize the trace, run Dynamo’s [prefix data generator](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/benchmarks/prefix_data_generator) on the Mooncake `conversation_trace.jsonl`

:

## Smoke Test

The Dynamo operator creates the `disagg-kv-dsv32-nvfp4-frontend`

service for this deployment.

## Benchmark

The checked-in [ perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/deepseek-v32-fp4/trtllm/disagg-kv-router/perf.yaml) runs a short synthetic warmup, then replays the trace at its original timestamps. It wraps this AIPerf run:

Results land under `/model-cache/perf/<epoch>_<job-name>/`

on the `model-cache`

PVC; copy them out with `kubectl cp`

.

Because the replay is `--fixed-schedule`

, throughput is fixed by the trace — the metrics to compare are TTFT (KV-aware routing cuts prefill compute via prefix hits), ITL (disaggregation isolates decode from prefill interference), total request latency, and goodput against the TTFT 20s / ITL 50ms SLA.

## Related Feature Benchmarks

## Notes

- The aggregated round-robin configuration (
`trtllm/agg-round-robin/`

) is the benchmark control arm; it appears on the Feature Benchmark page, not as a recipe target here. - The benchmark job pins
`transformers==4.57.6`

: the trtllm-runtime base ships 4.55.0, and aiperf’s`transformers>=4.56.0`

floor would otherwise pull 5.x, which cannot load the`deepseek_v32`

tokenizer (surfaces as “Failed to load tokenizer”). - Decode workers run the WIDEEP MoE backend with
`moe_expert_parallel_size: 8`

and FP8 KV cache; prefill enables chunked prefill and KV block reuse (`tokens_per_block: 64`

, matching`--kv-block-size 64`

). - The trace tops out at 109,459 input tokens; both engine configs set
`max_seq_len: 121000`

to accommodate it.

## Source

- Source README:
[recipes/deepseek-v32-fp4/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/deepseek-v32-fp4/README.md) - Disagg + KV router + WideEP:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/deepseek-v32-fp4/trtllm/disagg-kv-router/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/deepseek-v32-fp4/trtllm/disagg-kv-router/perf.yaml) - Setup assets:
[model-cache/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/deepseek-v32-fp4/model-cache)including[compute-domain.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/deepseek-v32-fp4/model-cache/compute-domain.yaml)