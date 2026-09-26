source: https://docs.nvidia.com/dynamo/zh-CN/recipes/nemotron-3-super
lastmod: 2026-09-24T19:58:16.636Z

Nemotron-3-Super


Nemotron-3-Super

Serve NVIDIA-Nemotron-3-Super-120B-A12B with Dynamo and vLLM, tuned per GPU and workload.

Each target below is a validated aggregated vLLM deployment of Nemotron-3-Super — NVIDIA’s ~120B hybrid Mamba/Attention/MoE model (~12B active) — with MTP speculative decoding (DL=3) and KV-aware routing; the B200 agentic target measured 1388.4 system output tok/s per GPU on its trace. B200 serves the NVFP4 checkpoint, H200 the FP8 checkpoint. Pick your GPU and workload; every command on this page updates to match.

Choose your deployment target

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200 per worker, TP4 + EP (2 replicas)

**All2All**DeepEP high-throughput

**Spec decode**MTP, DL=3

**Workload**Chat 8K/1K, 70% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200 per worker, TP4 + EP (2 replicas)

**All2All**DeepEP low-latency

**Spec decode**MTP, DL=3

**Workload**Agentic 64K/400, 90% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8

**Precision**FP8 + FP8 KV cache

**GPUs**4x H200 per worker, TP4 + EP (2 replicas)

**All2All**FlashInfer NVLink one-sided

**Spec decode**MTP, DL=3

**Workload**Chat 8K/1K, 70% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8

**Precision**FP8 + FP8 KV cache

**GPUs**4x H200 per worker, TP4 + EP (2 replicas)

**All2All**DeepEP high-throughput

**Spec decode**MTP, DL=3

**Workload**Agentic 64K/400, 90% KV reuse

## Prerequisites

- A Kubernetes cluster with the Dynamo Platform installed (DGD CRDs registered with
`nvidia.com/v1beta1`

served) and**8x B200**available (two 4-GPU worker replicas). - A Hugging Face token with access to
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4`

. **Namespace labeled for KAI**— without`kai.scheduler/enabled=true`

, pods sit`SchedulingGated`

indefinitely because KAI’s`pod-grouper`

filters by namespace label.

- A Kubernetes cluster with the Dynamo Platform installed (DGD CRDs registered with
`nvidia.com/v1beta1`

served) and**8x H200**available (two 4-GPU worker replicas). - A Hugging Face token with access to
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8`

. **Namespace labeled for KAI**— without`kai.scheduler/enabled=true`

, pods sit`SchedulingGated`

indefinitely because KAI’s`pod-grouper`

filters by namespace label.

Create the namespace with the KAI label and the token secret:

Edit namespace, storage class, image tags, and other cluster-specific settings in the manifests before applying them.

## Deploy

Prepare the model cache and download the checkpoint for your SKU:

Downloading both checkpoints lands ~200 GB on the PVC — the default size in `model-cache.yaml`

— so bump `storage:`

first if you want both.

Then deploy. First-time boot per worker takes about 6–9 minutes (image pull + vLLM engine init + Inductor + CUDA graph capture up to size 512):

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

A single AIPerf trace-replay Job ([ perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/perf/perf.yaml)) covers every target — only

`ENDPOINT`

, `TRACE_FILE`

, `TARGET_MODEL`

, and `CONCURRENCY`

change in its env block (`TARGET_MODEL`

is the NVFP4 id for B200, FP8 for H200). First stage the bundled traces from [onto the](https://github.com/ai-dynamo/dynamo/tree/main/recipes/nemotron-3-super/perf/traces)

`recipes/nemotron-3-super/perf/traces/`

`model-cache`

PVC:Set `ENDPOINT`

to `nemotron-3-super-b200-chat-frontend:8000`

(the Job default) with the NVFP4 `TARGET_MODEL`

and the chat trace, then apply. The Job wraps this AIPerf Mooncake trace replay:

Set `ENDPOINT`

to `nemotron-3-super-b200-agentic-frontend:8000`

with the NVFP4 `TARGET_MODEL`

and the agentic trace, then apply. The Job wraps this AIPerf Mooncake trace replay:

Set `ENDPOINT`

to `nemotron-3-super-h200-chat-frontend:8000`

with the FP8 `TARGET_MODEL`

and the chat trace, then apply. The Job wraps this AIPerf Mooncake trace replay:

Set `ENDPOINT`

to `nemotron-3-super-h200-agentic-frontend:8000`

with the FP8 `TARGET_MODEL`

and the agentic trace, then apply. The Job wraps this AIPerf Mooncake trace replay:

Artifacts land on the PVC under `/model-cache/perf/<epoch>_nemotron-3-super-bench/`

. 15% and 30% trace subsets are provided for shorter runs. For concurrency sweeps, delete the worker pods between runs so residual KV/prefix-cache state does not skew results (Dynamo workers are PodClique pods — `kubectl rollout restart deployment`

is a silent no-op) — see the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/perf/README.md) for the full workflow, artifact layout, and tunable environment variables.

## Expected Performance

Each target is tuned for its workload shape:

Measured results below replay the **15% trace subsets** (`*_short_15perc.jsonl`

) with two worker replicas per deployment; your selected target’s row is highlighted:

## Compare All Targets

All four targets run aggregated vLLM 0.21.0 (runtime image `vllm-runtime:1.3.0-nemotron-super-dev.1`

) with two TP4 + EP worker replicas, MTP speculative decoding (DL=3), and KV-aware routing. They differ in checkpoint, kernel backends, and the trace they are benchmarked against:

## Notes

- This is a Day-0 recipe on a dedicated dev runtime image (
`vllm-runtime:1.3.0-nemotron-super-dev.1`

); it is functional and benchmarked but not yet promoted to a release runtime image. - The namespace must carry the
`kai.scheduler/enabled=true`

label before deploying; without it, pods stay`SchedulingGated`

indefinitely. - B200 chat and agentic ship with MTP spec dec ON by default (DL=3,
`moe_backend=triton`

, stripped`compilation-config`

,`MAX_NUM_BATCHED_TOKENS=65536`

). To turn MTP off, remove the`- --speculative-config=$(SPECULATIVE_CONFIG)`

line from worker args; with the freed memory headroom you can bump`MAX_NUM_BATCHED_TOKENS`

to`"131072"`

and switch`COMPILATION_CONFIG`

to the`compilation-config-fused`

ConfigMap key for better throughput. - For a fixed-AL synthetic MTP run on H200, point the
`SPECULATIVE_CONFIG`

env at the`speculative-config-synthetic`

ConfigMap key before deploying. - Known issue: some 400 HTTP errors raised by the workers on invalid inputs surface as 500 through the Dynamo frontend (the proxy does not always preserve the worker’s original status code).
- Reasoning is controlled per request via
`chat_template_kwargs`

(`enable_thinking: true|false`

); tool calling and function calling with JSON arguments are supported. - Both DGDs of a given SKU serve the same
`--served-model-name`

, so either trace can be replayed against either DGD by swapping`TRACE_FILE`

.

## Source

- Source README:
[recipes/nemotron-3-super/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/README.md) - Benchmark workflow:
[recipes/nemotron-3-super/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/perf/README.md)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/perf/perf.yaml) - B200 chat:
[vllm/agg-b200-chat/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/vllm/agg-b200-chat/deploy.yaml) - B200 agentic:
[vllm/agg-b200-agentic/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/vllm/agg-b200-agentic/deploy.yaml) - H200 chat:
[vllm/agg-h200-chat/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/vllm/agg-h200-chat/deploy.yaml) - H200 agentic:
[vllm/agg-h200-agentic/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3-super/vllm/agg-h200-agentic/deploy.yaml) - Model cache setup:
[model-cache/](https://github.com/ai-dynamo/dynamo/tree/main/recipes/nemotron-3-super/model-cache)(`model-cache.yaml`

,`model-download.yaml`

,`model-download-fp8.yaml`

)