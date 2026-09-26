source: https://docs.nvidia.com/dynamo/dev/recipes/qwen-3-8-2-4t-a95b-fp8
lastmod: 2026-09-24T19:58:16.636Z

Qwen3.8-2.4T-A95B


Qwen3.8-2.4T-A95B

Serve Qwen3.8-2.4T-A95B with Dynamo and vLLM or SGLang on GB300 or GB200, aggregated or disaggregated.

Each target below is a Dynamo + vLLM or SGLang deployment of [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8) — a hybrid gated-delta-net + MoE model with 512 experts and a 262k-token context — with KV-aware routing and FP8 weights/KV cache. Tensor parallelism runs over MNNVL through Kubernetes ComputeDomains. Pick your GPU architecture, serving topology, and inference engine; every command on this page updates to match.

Choose your deployment target

**Checkpoint**Qwen/Qwen3.8-2.4T-A95B-FP8

**Precision**FP8 weights, FP8 KV

**GPUs**16x GB300 (4 nodes), 1 replica

**Parallelism**TP16 over MNNVL

**Routing**event-driven KV-aware, prefix caching

**Checkpoint**Qwen/Qwen3.8-2.4T-A95B-FP8

**Precision**FP8 weights, FP8 KV

**GPUs**16x GB300 prefill (4 nodes) + 16x GB300 decode (4 nodes)

**Parallelism**TP16 / TP16 over MNNVL

**KV transfer**NIXL over cuda_ipc + MNNVL

**Routing**KV-aware, load-balanced prefill; NIXL KV transfer

**Checkpoint**Qwen/Qwen3.8-2.4T-A95B-FP8

**Precision**FP8 weights, FP8 KV

**GPUs**16x GB200 (4 nodes), 1 replica

**Parallelism**TP16 over MNNVL

**MoE backend**flashinfer_trtllm

**Routing**KV-aware (ZMQ events)

**Checkpoint**Qwen/Qwen3.8-2.4T-A95B-FP8

**Precision**FP8 weights, FP8 KV

**GPUs**16x GB200 (4 nodes), 1 replica

**Parallelism**TP16 over MNNVL

**MoE backend**flashinfer_trtllm; trtllm_mha attention

**Routing**KV-aware (ZMQ events)

**Checkpoint**Qwen/Qwen3.8-2.4T-A95B-FP8

**Precision**FP8 weights, FP8 KV

**GPUs**16x GB200 × 2 prefill + 16x GB200 decode (2P1D, 12 nodes)

**Parallelism**TP16 / TP16 over MNNVL

**MoE backend**flashinfer_trtllm; trtllm_mha attention

**Routing**KV-aware, load-balanced across prefill replicas; NIXL KV transfer over cuda_ipc + MNNVL

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and GB300 GPUs available — 16x (4 nodes). See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to
`Qwen/Qwen3.8-2.4T-A95B-FP8`

.

- A Kubernetes cluster with the Dynamo platform installed and GB200 GPUs available — 16x (4 nodes) for aggregated; 48x (12 nodes, 2×4 prefill + 4 decode) for 2P1D disaggregated. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed (required for multi-node NVLink).
- A Hugging Face token with access to
`Qwen/Qwen3.8-2.4T-A95B-FP8`

. - The
`model-cache`

PVC, populated by the model-download Job (see step 3 below).

Create the namespace:

Create the Hugging Face token secret:

Edit `storageClassName`

in `model-cache/model-cache.yaml`

to a ReadWriteMany storage class on your
cluster (`kubectl get storageclass`

) before applying it. Review namespace, image tag, node selectors,
and resource claims in the manifests as well.

## Deploy

Stage the weights into the cache, then deploy:

Stage the weights into the model-cache PVC, then deploy:

Then deploy the target DGD:

First worker launch loads ~2.4 TB of FP8 weights across the TP ranks and warms CUDA graphs. Allow up to 4 hours; the multinode pod set reports ready only once all nodes have joined the TP group.

## Smoke Test

Forward the frontend port:

Send a test request:

Qwen3.8-2.4T-A95B reasons before answering; chain-of-thought lands in `choices[0].message.reasoning_content`

and the answer in `choices[0].message.content`

. The deployment wires the `qwen3`

reasoning parser and `qwen3_coder`

tool-call parser at the frontend.

## Benchmark

Standard chat workload: 8k total context / 1k output, 70% KV cache reuse.

## Compare All Targets

Aggregated targets support both vLLM and SGLang. Disaggregated targets are SGLang only. GB300 disagg is 1P1D; GB200 disagg is 2P1D.

## Notes

**Event-driven KV-aware routing.**Both workers publish KV events (`--kv-events-config`

over ZMQ), and the frontend enables`--router-kv-events`

; otherwise the disaggregated route cannot be verified.is required for the shipped fixed shapes.`--no-async-scheduling`

**MNNVL all-reduce.**`VLLM_ALLREDUCE_USE_FLASHINFER=1`

with`VLLM_FLASHINFER_ALLREDUCE_BACKEND=mnnvl`

. Keep`VLLM_USE_NCCL_SYMM_MEM=0`

alongside it.**GB300 P-to-D fabric.**The disaggregated workers select the DRA-injected RoCE HCA and use`UCX_TLS=rc_x,rc,cuda_copy,cuda_ipc`

with Ethernet GIDs. This is RC/GDR for NIXL payloads; MNNVL remains the TP all-reduce fabric.

## Source

- Source README:
[recipes/qwen3.8-2.4t-a95b-fp8/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/README.md) - GB300 aggregated chat (vLLM):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/vllm/agg-gb300-chat/deploy.yaml) - GB300 aggregated agentic (vLLM):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/vllm/agg-gb300-agentic/deploy.yaml) - GB200 aggregated chat (vLLM):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/vllm/agg-gb200-chat/deploy.yaml) - GB200 aggregated agentic (vLLM):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/vllm/agg-gb200-agentic/deploy.yaml) - GB300 aggregated chat (SGLang):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/sglang/agg-gb300-chat/deploy.yaml) - GB300 disaggregated chat (SGLang):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/sglang/disagg-gb300-chat/deploy.yaml) - GB200 aggregated chat (SGLang):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/sglang/agg-gb200-chat/deploy.yaml) - GB200 disaggregated chat (SGLang):
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/sglang/disagg-gb200-chat/deploy.yaml) - Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-2.4t-a95b-fp8/model-cache/model-download.yaml)