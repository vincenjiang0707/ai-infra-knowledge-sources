source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/ax-k2
lastmod: 2026-09-24T19:58:16.636Z

A.X-K2


A.X-K2

Serve A.X-K2 with Dynamo and vLLM on B200, aggregated or disaggregated.

Deploy SK Telecom’s [A.X-K2](https://huggingface.co/skt/A.X-K2-NVFP4) with
NVIDIA Dynamo, NVFP4 weights, FP8 KV cache, KV-aware routing, and EAGLE3
speculative decoding. Both topologies use four B200 GPUs per worker and
support text generation, reasoning, and tool calling.

Choose your deployment target

**Checkpoint**skt/A.X-K2-NVFP4

**Hardware**8x B200, two TP4 aggregate workers

**Precision**NVFP4 weights, FP8 KV cache

**Speculation**EAGLE3, 3 tokens

**FlashInfer autotuning**Disabled

**Checkpoint**skt/A.X-K2-NVFP4

**Hardware**12x B200, two TP4 prefill workers and one TP4 decode worker

**Precision**NVFP4 weights, FP8 KV cache

**Speculation**EAGLE3, 3 tokens on both roles

**FlashInfer autotuning**Disabled on prefill and decode

## Prerequisites

- A Kubernetes cluster with the
[Dynamo platform](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)installed. - Four B200 GPUs and 400 GiB of host memory per worker: eight GPUs total for aggregated serving or twelve for disaggregated serving.
- A ReadWriteMany storage class for model weights.
- A Hugging Face token with access to
`skt/A.X-K2-NVFP4`

and`skt/A.X-K2-EAGLE3`

.

Disaggregated serving also requires InfiniBand with one `rdma/shared_ib`

device resource available per worker for NIXL/UCX KV transfer.

## Deploy

Run commands from the repository root. Set `CONTEXT`

and `NAMESPACE`

to your
cluster context and namespace, and set `HF_TOKEN`

to your Hugging Face token.
Create the namespace and token secret:

Set `storageClassName`

in
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/ax-k2/model-cache/model-cache.yaml)
to your cluster’s ReadWriteMany storage class. Create the PVC and download
both pinned checkpoints:

Both profiles and the download job mount `model-cache`

. To use an existing
populated PVC, set `claimName`

in the job and selected deployment source to
that PVC and skip creating a new claim. Regenerate the selected manifest
after editing its Kustomize source.

Deploy two aggregate workers:

The manifest is generated from
[Kustomize sources](https://github.com/ai-dynamo/dynamo/tree/main/recipes/ax-k2/vllm/agg-b200-chat/kustomize).
To change a setting, edit `kustomize/base/deploy.yaml`

and regenerate:

Deploy two prefill workers and one decode worker:

The manifest is generated from
[Kustomize sources](https://github.com/ai-dynamo/dynamo/tree/main/recipes/ax-k2/vllm/disagg-b200-chat/kustomize).
To change a setting, edit `kustomize/base/deploy.yaml`

and regenerate:

## Smoke Test

Wait for the selected deployment, then forward its frontend port:

In another terminal, verify model discovery and a completion:

Model discovery should list `skt/A.X-K2-NVFP4`

; the completion should contain
a `choices`

array. Reasoning uses the `deepseek_v3`

parser, and tool calling
uses the `hermes`

parser.

## Benchmark

The [AIPerf workflow](https://github.com/ai-dynamo/dynamo/blob/main/recipes/ax-k2/perf/README.md)
replays an 8K-input / 1K-output chat trace with 70% KV reuse against the
aggregated profile at concurrency 32. It preserves expanded configurations,
raw reports, and frontend metrics. Keep the default real EAGLE3 acceptance
configuration for accuracy evaluation.

Before starting the benchmark, follow the workflow’s
[trace-staging instructions](https://github.com/ai-dynamo/dynamo/blob/main/recipes/ax-k2/perf/README.md#stage-the-trace)
to copy the Git LFS chat trace from your checkout onto the model-cache PVC.
The job reads it through `TRACE_FILE`

and verifies its SHA-256 and request
counts before sending traffic.

The checked-in benchmark job targets the aggregate frontend. To benchmark the disaggregated profile, update its endpoint and frontend selector to this deployment before applying the job.

### Performance Results

Benchmarking uses synthetic EAGLE3 acceptance length 2.12.