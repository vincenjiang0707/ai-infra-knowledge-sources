source: https://docs.nvidia.com/dynamo/dev/recipes/glm-5-2
lastmod: 2026-09-24T19:58:16.636Z

GLM-5.3/5.2


GLM-5.3/5.2

Serve GLM-5.3/5.2 with Dynamo and SGLang on B200 or H200 for long-context agentic workloads.

Each target below is a Dynamo + SGLang deployment of Z.AI’s GLM-5.3/5.2 tuned for an agentic workload (64K median ISL / 400 median OSL, 90% KV cache hit rate) with KV-aware routing and EAGLE-style MTP speculative decoding. B200 serves the NVFP4 checkpoint at up to 500K context with HiCache CPU offload; H200 serves the FP8 checkpoint at up to 250K context. Both run aggregated or with prefill/decode disaggregation. Pick your GPU architecture and serving topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**RadixArk/GLM-5.3-NVFP4 / nvidia/GLM-5.2-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200, one worker

**Parallelism**DTP4

**Routing**KV-aware

**Context**Up to 500K, HiCache CPU offload

**Checkpoint**RadixArk/GLM-5.3-NVFP4 / nvidia/GLM-5.2-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**4x B200 prefill + 8x B200 decode

**Parallelism**DEP4 prefill / DTP8 decode

**Routing**KV-aware, NIXL/UCX over IB

**Context**Up to 500K, HiCache CPU offload

**Checkpoint**zai-org/GLM-5.3 / zai-org/GLM-5.2-FP8

**Precision**FP8 + FP8 KV cache

**GPUs**8x H200, one worker

**Parallelism**TP8/EP8

**Routing**KV-aware

**Context**Up to 250K

**Checkpoint**zai-org/GLM-5.3 / zai-org/GLM-5.2-FP8

**Precision**FP8 + FP8 KV cache

**GPUs**8x H200 prefill + 8x H200 decode

**Parallelism**TP8/EP8 prefill / TP8/DP8/EP1 decode

**Routing**KV-aware, NIXL/UCX over IB

**Context**Up to 250K

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and B200 GPUs available — 4x for aggregated, 12x for disaggregated. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`RadixArk/GLM-5.3-NVFP4`

/`nvidia/GLM-5.2-NVFP4`

.

- A Kubernetes cluster with the Dynamo platform installed and H200 GPUs available — 8x for aggregated, 16x for disaggregated. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`zai-org/GLM-5.3`

/`zai-org/GLM-5.2-FP8`

.

Create the namespace and token secret:

Edit `storageClassName`

in `model-cache/model-cache.yaml`

to a ReadWriteMany storage class on your cluster (`kubectl get storageclass`

) before applying it. Review namespace, image tags, node selectors, and resource claims in the manifests as well.

## Deploy

Create the shared model cache, then download the checkpoint for your target SKU. Edit `model-cache/model-download.yaml`

(select between GLM-5.3 and GLM-5.2 checkpoints, and between FP8 and NVFP4 precisions). Uncomment the `hf download`

line for your checkpoint and remove the others:

When serving GLM-5.3, update every `model-path`

in the target DGD to `RadixArk/GLM-5.3-NVFP4`

for B200 or `zai-org/GLM-5.3`

for H200, and update every `served-model-name`

to `zai-org/GLM-5.3`

.

Then deploy the target DGD:

## Smoke Test

Send a test request to verify the deployment serves traffic. First forward the frontend port for your target:

Set `MODEL_NAME`

to the `served-model-name`

configured in the DGD: `zai-org/GLM-5.3`

for GLM-5.3 or `zai-org/GLM-5.2`

for GLM-5.2:

GLM-5.3/5.2 reasons before answering. To get the answer in the `content`

field instead of `reasoning_content`

, disable thinking:

## Benchmark

A single AIPerf trace-replay Job — `perf/perf.yaml`

— covers all four DGDs. It replays a Mooncake-format agentic trace (64K ISL / 400 OSL, 90% KV cache hit rate) at one concurrency value and writes artifacts to the shared `model-cache`

PVC. The benchmark pod is co-located with a DGD frontend through `podAffinity`

.

Edit the `env`

block in `perf/perf.yaml`

to target your deployed DGD — set `ENDPOINT`

to the matching frontend service, `SYNTHESIS_MAX_ISL`

to its context limit, and `CONCURRENCY`

to the value for that target. The `CONCURRENCY`

values below reproduce the [Expected Performance (run on GLM-5.2)](https://docs.nvidia.com/dynamo/dev/recipes/glm-5-2#expected-performance-run-on-glm-52) numbers:

Then run the Job:

For trace staging, concurrency sweeps, and fetching artifacts, see the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/perf/README.md).

## Expected Performance (run on GLM-5.2)

Measured on the 15% agentic trace subset. System throughput is per-GPU output tokens per second; user throughput is the P50 per-request output rate.

## Compare All Targets

All four targets serve GLM-5.3/5.2 on SGLang with KV-aware routing and EAGLE-style MTP speculative decoding (draft length 3, SpeedBench acceptance length 2.69), benchmarked on the same agentic trace:

## Notes

- Speculative decoding uses EAGLE-style MTP with draft length 3, measured at a SpeedBench acceptance length of 2.69.
- All four targets use KV-aware routing at the frontend. The B200 targets add HiCache CPU offload; the agentic traces are shaped to show the value of KV-aware routing and offloading.
- The disaggregated targets transfer KV over NIXL/UCX on InfiniBand.

## Limitations

- B200 targets support up to 500K context; the full 1M context length is not supported out of the box. H200 targets support up to 250K context.
- Structured decoding requires reasoning to be disabled (
`"chat_template_kwargs": {"enable_thinking": false}`

) so the output lands in the`content`

field instead of`reasoning_content`

. `n>1`

requests are not supported with the disaggregated targets.

## Source

- Source README:
[recipes/glm-5.2/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/README.md) - Benchmark README:
[recipes/glm-5.2/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/perf/README.md) - Aggregated B200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/sglang/agg-b200-agentic/deploy.yaml) - Disaggregated B200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/sglang/disagg-b200-agentic/deploy.yaml) - Aggregated H200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/sglang/agg-h200-agentic/deploy.yaml) - Disaggregated H200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/sglang/disagg-h200-agentic/deploy.yaml) - Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/model-cache/model-download.yaml) - Benchmark manifest:
[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.2/perf/perf.yaml)