source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/glm-5-3-flash
lastmod: 2026-09-24T19:58:16.636Z

GLM-5.3-Flash


GLM-5.3-Flash

Serve GLM-5.3-Flash with Dynamo and vLLM on GB200 or H200, aggregated or with prefill/decode disaggregation.

This recipe references an upstream third-party vLLM container image. NVIDIA does not publish or distribute this image. Users should review the upstream image’s open-source license and codec terms before use or redistribution.

Each target below is an NVIDIA Dynamo + vLLM deployment of Z.AI’s GLM-5.3-Flash, a GLA/KDA hybrid-attention model. All targets load the same FP8-quantized checkpoint with BF16 KV cache and support up to 1,048,576 tokens of context. The GB200 targets use TP4 workers over MNNVL. The H200 targets add MTP7 speculative decoding and TP8 workers. Pick your GPU architecture and serving topology.

Choose your deployment target

**Checkpoint**zai-org/GLM-5.3-Flash

**Precision**FP8-quantized checkpoint + BF16 KV cache

**GPUs**8x H200, one worker

**Parallelism**TP8

**Speculation**MTP7

**Context**Up to 1,048,576 tokens

**Checkpoint**zai-org/GLM-5.3-Flash

**Precision**FP8-quantized checkpoint + BF16 KV cache

**GPUs**8x H200 prefill + 8x H200 decode

**Parallelism**TP8 prefill / TP8 decode

**Routing**KV-aware, NIXL KV transfer

**Speculation**MTP7 on prefill and decode

**Context**Up to 1,048,576 tokens

**Checkpoint**zai-org/GLM-5.3-Flash

**Precision**FP8-quantized checkpoint + BF16 KV cache

**GPUs**4x GB200, one worker

**Parallelism**TP4 over MNNVL

**Routing**KV-aware

**Context**Up to 1,048,576 tokens

**Checkpoint**zai-org/GLM-5.3-Flash

**Precision**FP8-quantized checkpoint + BF16 KV cache

**GPUs**4x GB200 prefill + 4x GB200 decode

**Parallelism**TP4 prefill / TP4 decode over MNNVL

**Routing**KV-aware, NIXL/UCX KV transfer over TCP

**Context**Up to 1,048,576 tokens

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and GB200 GPUs available: 4x on one ARM64 node for aggregated, or 8x across two ARM64 nodes for disaggregated. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - The NVIDIA DRA driver with ComputeDomain support installed. Both GB200 targets require a ComputeDomain spanning the full NVL72 rack.
- Access to
`zai-org/GLM-5.3-Flash`

and the`vllm/vllm-openai:glm53-flash`

image. - A ReadWriteMany PVC named
`model-cache`

, populated with the checkpoint in the standard Hugging Face cache layout.

- A Kubernetes cluster with the Dynamo platform installed and H200 GPUs available: 8x on one node for aggregated, or 16x across two nodes for disaggregated. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - Eight RDMA resource claims on each GPU node for disaggregated serving. Update
`rdma/ib`

if your device plugin advertises a different resource name. - Access to
`zai-org/GLM-5.3-Flash`

and the`vllm/vllm-openai:glm53-flash`

image. - A ReadWriteMany PVC named
`model-cache`

, populated with the checkpoint in the standard Hugging Face cache layout.

Create the namespace and token secret:

Edit namespace, node selectors, tolerations, storage, image tags, and resource claims in the manifests to match your cluster.

## Deploy

All four targets read the checkpoint from the `model-cache`

PVC with `HF_HUB_OFFLINE=1`

. Create and populate the PVC with the recipe’s [storage manifest](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/model-cache/model-cache.yaml) and [model-download job](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/model-cache/model-download.yaml):

Then apply the manifest for your target.

First worker launch loads the model and captures CUDA graphs and can take tens of minutes.

## Smoke Test

Send a test request to verify the deployment serves traffic. First forward the frontend port for your target:

All targets serve under the same model name, `zai-org/GLM-5.3-Flash`

:

GLM-5.3-Flash reasons before answering. The deployments support streaming chat, completions, tool calls, one image per prompt, and schema-constrained output through the `glm45`

reasoning and `glm47`

tool-call parsers.

## Compare All Targets

All four targets serve the same FP8-quantized GLM-5.3-Flash checkpoint on vLLM with BF16 KV cache. The GB200 aggregated target and both H200 targets enable prefix caching. The H200 targets add MTP7 speculative decoding, DeepGEMM, and FLASHMLA_SPARSE attention. The GB200 targets use MNNVL for TP4 collectives.

## Related Feature Benchmarks

No controlled feature benchmark is linked to this recipe. Browse the [Feature Benchmarks](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks) for comparable KV-routing, disaggregation, and speculative-decoding studies.

## Notes

- The H200 targets enable prefix caching with a match unit of 128 and use MTP with seven speculative tokens.
- The H200 disaggregated target sets the same MTP configuration,
`VLLM_SSM_CONV_STATE_LAYOUT=DS`

, and`VLLM_KV_CACHE_LAYOUT=HND`

on prefill and decode. These values must match for the NIXL compatibility handshake and KV layout. - The GB200 targets use MNNVL for TP4 collectives. The disaggregated target excludes
`cuda_ipc`

from UCX and transfers KV data over`cuda_copy`

and TCP because the GLM image’s UCX build lacks MNNVL IPC support. - To enable MNNVL IPC for GB200 KV transfer, rebuild on the vLLM runtime base and set
`UCX_TLS=cuda_copy,cuda_ipc,tcp`

with`UCX_CUDA_IPC_ENABLE_MNNVL=y`

. - A
`sitecustomize.py`

overlay disables cuDNN to avoid a convolution crash during multimodal initialization with the GLM-specific vLLM image. `n>1`

requests are not supported by the disaggregated targets.

## Source

- Source README:
[recipes/glm-5.3-flash/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/README.md) - Aggregated GB200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/vllm/agg-gb200-agentic/deploy.yaml) - Disaggregated GB200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/vllm/disagg-gb200-agentic/deploy.yaml) - Aggregated H200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/vllm/agg-h200-agentic/deploy.yaml) - Disaggregated H200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/glm-5.3-flash/vllm/disagg-h200-agentic/deploy.yaml)