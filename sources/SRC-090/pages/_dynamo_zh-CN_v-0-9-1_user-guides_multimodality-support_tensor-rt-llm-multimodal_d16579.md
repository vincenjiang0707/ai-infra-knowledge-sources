source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/user-guides/multimodality-support/tensor-rt-llm-multimodal
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

## Deployment Patterns

TRT-LLM supports aggregated and traditional disaggregated patterns. See [Architecture Patterns](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support#architecture-patterns) for detailed explanations.

### Component Flags

## Aggregated Serving

Quick steps to launch Llama-4 Maverick BF16 in aggregated mode:

**Client:**

## Disaggregated Serving

Example using `Qwen/Qwen2-VL-7B-Instruct`

:

For a large model like `meta-llama/Llama-4-Maverick-17B-128E-Instruct`

, a multi-node setup is required for disaggregated serving (see [Multi-node Deployment](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support/tensor-rt-llm-multimodal#multi-node-deployment-slurm) below), while aggregated serving can run on a single node. This is because the model with a disaggregated configuration is too large to fit on a single node’s GPUs. For instance, running this model in disaggregated mode requires 2 nodes with 8xH200 GPUs or 4 nodes with 4xGB200 GPUs.

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

`.pt`

- PyTorch tensor files`.pth`

- PyTorch checkpoint files`.bin`

- Binary tensor files

### Embedding File Formats

TRT-LLM supports two formats for embedding files:

**1. Simple Tensor Format**

Direct tensor saved as `.pt`

file containing only the embedding tensor:

**2. Dictionary Format with Auxiliary Data**

Dictionary containing multiple keys, used by models like Llama-4 that require additional metadata:

**Simple tensors**: Loaded directly and passed to`mm_embeddings`

parameter**Dictionary format**:`mm_embeddings`

key extracted as main tensor, other keys preserved as auxiliary data

### How to Launch


Note:This script is designed for 8-node H200 with`Llama-4-Scout-17B-16E-Instruct`

model and assumes you have a model-specific embedding file ready.

### Configuration

### Example Request with Pre-computed Embeddings

### E/P/D Architecture

The E/P/D flow implements a **3-worker architecture**:

**Encode Worker**: Loads pre-computed embeddings, transfers via NIXL**Prefill Worker**: Receives embeddings, handles context processing and KV-cache generation**Decode Worker**: Performs streaming token generation

## Multi-node Deployment (Slurm)

This section demonstrates how to deploy large multimodal models that require a multi-node setup using Slurm.


Note:The scripts referenced in this section can be found in[.]`examples/basics/multinode/trtllm/`


### Environment Setup

Assuming you have allocated your nodes via `salloc`

and are inside an interactive shell:

### Multi-node Disaggregated Launch

For 4 4xGB200 nodes (2 for prefill, 2 for decode):

### Understanding the Output

`srun_disaggregated.sh`

launches three srun jobs: frontend, prefill worker, and decode worker- The OpenAI frontend will dynamically discover workers as they register:
- TRT-LLM workers output progress from each MPI rank while loading
- When ready, the frontend logs:

### Cleanup

## NIXL Usage


Note:NIXL for KV cache transfer is currently beta and only supported on AMD64 (x86_64) architecture.

## ModelInput Types and Registration

TRT-LLM workers register with Dynamo using:

## Inter-Component Communication

## Known Limitations

**No video support**- No video encoder implementation**No audio support**- No audio encoder implementation**Multimodal preprocessing/tokenization happens in Python**- Rust may forward token_ids, but multimodal requests are parsed and re-tokenized in the Python worker**Multi-node H100 limitation**- Loading`meta-llama/Llama-4-Maverick-17B-128E-Instruct`

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