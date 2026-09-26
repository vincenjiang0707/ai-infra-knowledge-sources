source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/modular-components/backends/tensor-rt-llm/tensorrt-llm-multimodal
lastmod: 2026-09-23T23:30:39.914Z

TensorRT-LLM Multimodal


TensorRT-LLM Multimodal

This document provides a comprehensive guide for multimodal inference using TensorRT-LLM backend in Dynamo.

You can provide multimodal inputs in the following ways:

- By sending image URLs
- By providing paths to pre-computed embedding files


Note:You should provideeither image URLs or embedding file pathsin a single request.

## Support Matrix

### Supported URL Formats

Media URLs are validated against a default-deny policy. `https://`

and `data:`

sources
pass; plain `http://`

and hostnames that resolve to private or loopback addresses are
refused. To fetch media over the cluster’s internal network, set
`DYN_MM_ALLOW_INTERNAL=1`

on the worker that loads it.

## Deployment Patterns

TRT-LLM supports aggregated and traditional disaggregated patterns. See [Multimodal Model Serving](https://docs.nvidia.com/dynamo/multimodal/overview) for detailed explanations.

### Component Flags

## Multimodal KV Routing

TensorRT-LLM multimodal KV routing uses the Rust frontend to give the router and worker the same image identity:

- The frontend computes an
`mm_hash`

for each image. - It represents the image identity as hash-derived pad-value tokens in the routing view.
- The KV router credits that overlap in its combined prefill-and-decode cost and selects the lowest-cost eligible worker.
- The frontend forwards each hash as
`multi_modal_uuids`

. - The worker associates the UUID with the matching image-token run in its KV events.

For HTTP inputs, routing identity is based on the exact full image URL, including the query string, by default. Set `--frontend-decoding`

to hash decoded image content when different URLs can refer to identical images.

Workers must enable KV event publishing and block reuse. The provided launcher configures `--publish-kv-events`

, `enable_block_reuse: true`

, and a KV-routing frontend:

Key settings include:

The routing path supports Qwen2-VL, Qwen2.5-VL, Qwen3-VL, Kimi K2.5, and Kimi K2.6 model families. Other models fall back to text-prefix routing.

Current limitations:

- Use direct KV event publishing; consolidated multimodal KV events are not supported.
- Requests that mix image URLs and precomputed
`.safetensors`

embeddings skip multimodal-aware routing. - The worker and frontend must use matching block sizes.

For the user-facing workflow, see [Multimodal KV Routing](https://docs.nvidia.com/dynamo/multimodal/multimodal-kv-routing).

## Aggregated Serving

Quick steps to launch Llama-4 Maverick BF16 in aggregated mode:

**Client:**

## Disaggregated Serving

Example using `Qwen/Qwen2-VL-7B-Instruct`

:

For a large model like `meta-llama/Llama-4-Maverick-17B-128E-Instruct`

, a multi-node setup is required for disaggregated serving (see [Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/tensorrt-llm-multimodal#disaggregated-serving)), while aggregated serving can run on a single node. This is because the model with a disaggregated configuration is too large to fit on a single node’s GPUs. For instance, running this model in disaggregated mode requires 2 nodes with 8xH200 GPUs or 4 nodes with 4xGB200 GPUs.

## Full E/P/D Flow (Image URLs)

For high-performance multimodal inference, Dynamo supports a standalone encoder with an **Encode-Prefill-Decode (E/P/D)** flow using TRT-LLM’s `MultimodalEncoder`

. This separates the vision encoding stage from prefill and decode, enabling better GPU utilization and scalability.

### Supported Input Formats

### How It Works

In the full E/P/D flow:

**Encode Worker**: Runs TRT-LLM’s`MultimodalEncoder.generate()`

to process image URLs through the vision encoder and projector**Prefill Worker**: Receives`disaggregated_params`

containing multimodal embedding handles, processes context and generates KV cache**Decode Worker**: Performs streaming token generation using the KV cache

The encode worker uses TRT-LLM’s `MultimodalEncoder`

class (which inherits from `BaseLLM`

) and only requires the model path and batch size - no KV cache configuration is needed since it only runs the vision encoder + projector.

### How to Launch

### Example Request

### E/P/D Architecture (Image URLs)

### Key Differences from EP/D (Traditional Disaggregated)

## Pre-computed Embeddings with E/P/D Flow

For high-performance multimodal inference, Dynamo supports pre-computed embeddings with an **Encode-Prefill-Decode (E/P/D)** flow using **NIXL (RDMA)** for zero-copy tensor transfer.

### Supported File Types

`.safetensors`

- Safe tensor files ([safetensors format](https://huggingface.co/docs/safetensors))


Security Note:`.pt`

,`.pth`

, and`.bin`

files arerejectedbecause they use Python pickle deserialization, which can execute arbitrary code. Only`.safetensors`

format is accepted.

### Embedding File Formats

Embedding files must use the `.safetensors`

format. The first tensor key in the file is used as the embedding tensor.

**Saving embeddings:**

### How to Launch


Note:This script is designed for 8-node H200 with`Llama-4-Scout-17B-16E-Instruct`

model and assumes you have a model-specific`.safetensors`

embedding file ready.

### Configuration

### Example Request with Pre-computed Embeddings

### E/P/D Architecture

The E/P/D flow implements a **3-worker architecture**:

**Encode Worker**: Loads pre-computed embeddings, transfers via NIXL**Prefill Worker**: Receives embeddings, handles context processing and KV-cache generation**Decode Worker**: Performs streaming token generation

## Embedding Cache

Dynamo supports embedding cache in both aggregated and disaggregated settings for TRT-LLM:

The cache uses `MultimodalEmbeddingCacheManager`

to maintain an LRU cache of encoder embeddings on CPU. When the same image is seen again, the cached embedding is reused instead of re-encoding.

### Disaggregated Encoder (Embedding Cache in Prefill Worker)

In the disaggregated setting, the Prefill Worker (P) owns a CPU-side LRU embedding cache (`EmbeddingCacheManager`

). On each request P checks the cache first — on a hit, the Encode Worker is skipped entirely. On a miss, P routes to the Encode Worker (E), receives embeddings via NIXL, saves them to the cache, and then feeds the embeddings along with the request into the TRT-LLM Instance for prefill.

The `disagg_e_pd.sh`

script launches a separate encode worker and a PD worker. Extra arguments are forwarded to the PD worker. Enable embedding cache by passing `--multimodal-embedding-cache-capacity-gb`

:

## NIXL Usage


Note:NIXL for KV cache transfer is currently beta and only supported on AMD64 (x86_64) architecture.

## ModelInput Types and Registration

TRT-LLM workers register with Dynamo using:

## Inter-Component Communication

## Known Limitations

**No audio support**- No audio encoder implementation**Video decode requires NVDEC**- H.264/H.265 video is decoded on the GPU; the runtime image ships no software video decoder. This needs a GPU with a video decode engine and a container granted the`video`

driver capability — see[Video Decode GPU Requirements](https://docs.nvidia.com/dynamo/multimodal/video-decode-gpu-requirements).**Multimodal preprocessing/tokenization happens in Python**- Rust may forward token_ids, but multimodal requests are parsed and re-tokenized in the Python worker**Multi-node H100 limitation**- Loading`meta-llama/Llama-4-Maverick-17B-128E-Instruct`

with 8 nodes of H100 with TP=16 is not possible due to head count divisibility (`num_attention_heads: 40`

not divisible by`tp_size: 16`

)**llava-v1.6-mistral-7b-hf model crash**- Known issue with TRTLLM backend compatibility with`TensorRT LLM version: 1.2.0rc6.post1`

. To use Llava model download revision`revision='52320fb52229`

locally using HF.**Embeddings file crash**- Known issue with TRTLLM backend compatibility with`TensorRT LLM version: 1.2.0rc6.post1`

. Embedding file parsing crashes in`attach_multimodal_embeddings(`

. To be fixed in next TRTLLM upgrade.

## Supported Models

Multimodal models listed in [TensorRT-LLM supported models](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/models/supported-models.md) are supported by Dynamo.

Common examples:

**Llama 4 Vision models**(Maverick, Scout) - Recommended for large-scale deployments**LLaVA models**(e.g.,`llava-hf/llava-v1.6-mistral-7b-hf`

) - Default model for E/P/D examples**Qwen2-VL models**- Supported in traditional disaggregated mode- Other vision-language models with TRT-LLM support