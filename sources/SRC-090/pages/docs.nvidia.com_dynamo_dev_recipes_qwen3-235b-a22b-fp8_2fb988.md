source: https://docs.nvidia.com/dynamo/dev/recipes/qwen3-235b-a22b-fp8
lastmod: 2026-09-24T19:58:16.636Z

Qwen3-235B-A22B FP8


Qwen3-235B-A22B FP8

Serve Qwen/Qwen3-235B-A22B-FP8 with Dynamo and TensorRT-LLM on 16 Hopper or Blackwell GPUs.

Each target below is a validated TensorRT-LLM deployment of Qwen3-235B-A22B-FP8 — a 235B-parameter Mixture-of-Experts model with ~22B active parameters per token — on 16 GPUs with KV-aware routing, benchmarked at 4K ISL / 200 OSL. Hopper and Blackwell need different MoE backends, and you can serve aggregated or with prefill/decode disaggregation. Pick your GPU architecture and serving topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**Qwen/Qwen3-235B-A22B-FP8

**GPUs**16x B100/B200, 4 workers

**Parallelism**TP4 x EP4 per worker

**MoE backend**DEEPGEMM (required on SM100+)

**Routing**KV-aware

**Workload**4K ISL / 200 OSL, concurrency 32

**Checkpoint**Qwen/Qwen3-235B-A22B-FP8

**GPUs**16x B100/B200

**Parallelism**6x prefill (TP2) + 1x decode (TP4 x EP4)

**MoE backend**DEEPGEMM (required on SM100+)

**Routing**KV-aware

**Workload**4K ISL / 200 OSL, concurrency 32

**Checkpoint**Qwen/Qwen3-235B-A22B-FP8

**GPUs**16x H100/H200, 4 workers

**Parallelism**TP4 x EP4 per worker

**MoE backend**CUTLASS (TRT-LLM default)

**Routing**KV-aware

**Workload**4K ISL / 200 OSL, concurrency 32

**Checkpoint**Qwen/Qwen3-235B-A22B-FP8

**GPUs**16x H100/H200

**Parallelism**6x prefill (TP2) + 1x decode (TP4 x EP4)

**MoE backend**CUTLASS (TRT-LLM default)

**Routing**KV-aware

**Workload**4K ISL / 200 OSL, concurrency 32

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**16x B100/B200**available (~1.3 TB total GPU VRAM). - A Hugging Face token with access to
`Qwen/Qwen3-235B-A22B-FP8`

.

- A Kubernetes cluster with the Dynamo platform installed and
**16x H100/H200**available (~1.3 TB total GPU VRAM). - A Hugging Face token with access to
`Qwen/Qwen3-235B-A22B-FP8`

.

Create the namespace and token secret:

Edit namespace, storage class, image tags, node selectors, resource claims, and cluster-specific placement in the manifests before applying them.

## Deploy

Prepare the model cache and download the checkpoint (30-60 minutes):

Then deploy:

Choose the manifest matching your cluster interconnect:

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

Every target ships a `perf.yaml`

AIPerf Job sized at 4K ISL / 200 OSL and concurrency 32 (2 per GPU x 16 GPUs) with `--request-count 320`

, so aggregated vs disaggregated results are comparable within the same hardware architecture. Artifacts land on the `model-cache`

PVC under `/model-cache/perf`

.

The aggregated Job wraps this AIPerf run:

The disaggregated Job wraps this AIPerf run:

Apply the manifest matching your deployed target:

## Compare All Targets

All four targets serve `Qwen/Qwen3-235B-A22B-FP8`

on TensorRT-LLM (PyTorch backend) over 16 GPUs with KV-aware routing and the same 4K ISL / 200 OSL benchmark shape:

## Notes

- The Hopper/Blackwell split is required with TRT-LLM 1.3.x: the default CUTLASS MoE backend falls through to a Hopper-specific JIT path on SM100 and crashes, so Blackwell needs
`moe_config.backend: DEEPGEMM`

. DEEPGEMM in turn crashes on Hopper due to a scale-factor dtype mismatch — hence two separate variants per topology. - Chunked prefill is enabled for the aggregated targets and disabled for the disaggregated targets.
- All targets use KV-aware routing (
`--router-mode kv`

) at the frontend. - Model download may take 30-60 minutes; update
`storageClassName`

in`model-cache/model-cache.yaml`

before deploying.

## Source

- Source README:
[recipes/qwen3-235b-a22b-fp8/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/README.md) - Aggregated Blackwell:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/agg/blackwell/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/agg/blackwell/perf.yaml) - Disaggregated Blackwell:
[AWS EFA](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/blackwell/deploy-aws-p6-b200.48xlarge.yaml),[GKE RoCE](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/blackwell/deploy-gcp-roce.yaml),[Nscale InfiniBand](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/blackwell/deploy-nscale-ib.yaml), and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/blackwell/perf.yaml) - Aggregated Hopper:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/agg/hopper/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/agg/hopper/perf.yaml) - Disaggregated Hopper:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/hopper/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/trtllm/disagg/hopper/perf.yaml) - Setup assets:
[model-cache/model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/model-cache/model-cache.yaml)and[model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3-235b-a22b-fp8/model-cache/model-download.yaml)