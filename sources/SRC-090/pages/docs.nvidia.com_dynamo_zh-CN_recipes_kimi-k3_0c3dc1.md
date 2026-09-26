source: https://docs.nvidia.com/dynamo/zh-CN/recipes/kimi-k3
lastmod: 2026-09-24T19:58:16.636Z

Kimi-K3


Kimi-K3

Serve Kimi-K3 with Dynamo on H200, GB200, or GB300.

Each target below is a Dynamo + vLLM or SGLang deployment of Moonshot AI’s Kimi-K3, a multimodal MoE model serving up to 1M-token context, on H200, GB200, or GB300. Pick your framework, GPU architecture, and serving topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, BF16 KV

**GPUs**32x H200 (1 replica)

**Parallelism**TP8, PP4

**Routing**KV-aware

**Speculative decoding**None

**Status**No recipe available for this combination

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**16x GB200 (1 replica)

**Parallelism**TP16

**Routing**KV-aware

**Speculative decoding**None

**Status**No recipe available for this combination

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**16x GB300 (1 replica)

**Parallelism**DCP16 attention, TEP16 MoE

**Routing**KV-aware

**Speculative decoding**DSPARK

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**16x GB300 (1P1D)

**Parallelism**TP8 per role

**Routing**KV-aware

**Speculative decoding**DSPARK

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**24x GB300 (3 replicas)

**Parallelism**DCP8 attention, TP8/EP1 MoE

**Routing**Load-aware

**Speculative decoding**DSPARK

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**32x GB200 (2 replicas)

**Parallelism**DCP16 attention, TEP16 MoE

**Routing**Load-aware

**Speculative decoding**DSPARK

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**48x GB200 (2P1D)

**Parallelism**Prefill TEP16; decode DCP16 attention, TEP16 MoE

**Routing**Load-aware

**Speculative decoding**DSPARK

**Status**No recipe available for this combination

**Status**No recipe available for this combination

**Checkpoint**moonshotai/Kimi-K3

**Precision**MXFP4 experts, FP8 KV

**GPUs**16x GB300 (1P1D)

**Parallelism**Prefill TEP8; decode DCP8 attention, TEP8 MoE

**Routing**Load-aware

**Speculative decoding**DSPARK

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and 32 H200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

.

- A Kubernetes cluster with the Dynamo platform installed and 16 GB200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

.

- A Kubernetes cluster with the Dynamo platform installed and 16 GB300 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`Inferact/Kimi-K3-DSpark`

.

- A Kubernetes cluster with the Dynamo platform installed and 16 GB300 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`Inferact/Kimi-K3-DSpark`

.

- A Kubernetes cluster with the Dynamo platform installed and 32 GB200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`RadixArk/Kimi-K3-DSpark`

.

- A Kubernetes cluster with the Dynamo platform installed and 48 GB200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`RadixArk/Kimi-K3-DSpark`

.

- A Kubernetes cluster with the Dynamo platform installed and 24 GB300 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`RadixArk/Kimi-K3-DSpark`

.

- A Kubernetes cluster with the Dynamo platform installed and 16 GB300 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to the checkpoint
`moonshotai/Kimi-K3`

and draft model`RadixArk/Kimi-K3-DSpark`

.

Create the namespace and token secret:

The recipes require the `shared-model-cache`

PVC. Edit `storageClassName`

in `model-cache/model-cache.yaml`

to a ReadWriteMany storage class on your cluster (`kubectl get storageclass`

) before applying it. Review namespace, image tags, and resource claims in the manifests as well.

## Deploy

Create the `shared-model-cache`

PVC and download the Kimi-K3 checkpoint and both DSPARK draft models. The download can take several hours on a cold cache:

The workers mount the PVC at `/shared-model-cache`

and resolve the checkpoint and any configured DSPARK draft model from the local Hugging Face cache with `HF_HUB_OFFLINE=1`

.

Deploy the selected DynamoGraphDeployment (DGD):

The first worker launch loads weights and captures CUDA graphs, which can take tens of minutes.

## Smoke Test

Send a test request to verify the selected deployment serves traffic. The deploy command sets `DGD`

to its resource name. Forward the frontend port:

All Kimi-K3 recipes serve under the same model name, `moonshotai/Kimi-K3`

:

Kimi-K3 reasons before answering, and tool calling is supported — the deployment uses the `kimi_k3`

reasoning and tool-call parsers at the frontend.

## Benchmark

See [perf/README.md](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/perf/README.md) for the full benchmark workflow: staging the trace on the PVC, running the AIPerf trace-replay Job, running a concurrency sweep, and fetching artifacts.

### Optimization Targets

Recipes are optimized for the following agentic workload and target user interactivity:

The benchmark replays the Mooncake-format agentic trace described in [perf/README.md](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/perf/README.md).

### Performance Results

Benchmarking uses a synthetic acceptance length with the SpeedBench coding AL.

## Compare All Targets

## Limitations

- With JSON structured decoding, output for non-object top-level items can appear in
`reasoning_content`

instead of`content`

. - Requests containing
`logprobs`

or`stop_token_ids`

are not supported and may cause disaggregated recipes to crash or enter a bad state

## Source

- Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k3/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k3/model-cache/model-download.yaml) - Benchmark instructions:
[recipes/kimi-k3/perf/README.md](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/perf/README.md)

- Selected recipe:
[vLLM aggregated GB200 deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k3/vllm/agg-gb200-agentic/deploy.yaml)

- Selected recipe:
[vLLM aggregated GB300 deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k3/vllm/agg-gb300-agentic/deploy.yaml)

- Selected recipe:
[vLLM disaggregated GB300 deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k3/vllm/disagg-gb300-agentic/deploy.yaml)

- Selected recipe:
[vLLM aggregated H200 deploy.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/vllm/agg-h200-agentic/deploy.yaml)

- Selected recipe:
[SGLang aggregated GB200 deploy.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/sglang/agg-gb200-agentic/deploy.yaml)

- Selected recipe:
[SGLang disaggregated GB200 deploy.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/sglang/disagg-gb200-agentic/deploy.yaml)

- Selected recipe:
[SGLang aggregated GB300 deploy.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/sglang/agg-gb300-agentic/deploy.yaml) - Benchmark Job:
[perf.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/perf/perf.yaml)

- Selected recipe:
[SGLang disaggregated GB300 deploy.yaml](https://github.com/milesial/dynamo/blob/docs/kimi-k3-framework-selector/recipes/kimi-k3/sglang/disagg-gb300-agentic/deploy.yaml)