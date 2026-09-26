source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/qwen-3-8-flash-next
lastmod: 2026-09-24T19:58:16.636Z

Qwen3.8-Flash-Next


Qwen3.8-Flash-Next

Serve Qwen3.8-Flash-Next with Dynamo and vLLM on B200, aggregated or disaggregated.

This recipe references an upstream third-party vLLM container image. NVIDIA does not publish or distribute this image. Users should review the upstream image’s open-source license and codec terms before use or redistribution.

Each target below is a Dynamo + vLLM deployment of [Qwen3.8-Flash-Next](https://huggingface.co/Inferact/Qwen3.8-Flash-Next-NVFP4) — a multimodal, ultra-sparse Mixture-of-Experts model (125B total / 6B active) with GDN+QSA hybrid attention, a 51B N-gram embedding table offloaded to host RAM, and a 262K-token context (extensible to 1M with YaRN) — with NVFP4 weights, MTP3 speculative decoding, and KV-aware routing. Pick your serving topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**Inferact/Qwen3.8-Flash-Next-NVFP4

**Precision**NVFP4 weights

**GPUs**4x B200 (1 node), 1 replica

**Parallelism**TP4 + expert parallel

**Spec decode**MTP3

**Routing**event-driven KV-aware, prefix caching

**Checkpoint**Inferact/Qwen3.8-Flash-Next-NVFP4

**Precision**NVFP4 weights

**GPUs**4x B200 prefill + 4x B200 decode (1P1D, colocated)

**Parallelism**TP4 + EP, both roles

**Spec decode**MTP3

**KV transfer**NIXL over InfiniBand RDMA (rc_x + rc + cuda_copy + cuda_ipc)

**Routing**KV-aware

## Overview

[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) is a multimodal, ultra-sparse Mixture-of-Experts model with 125B total parameters (including a 51B N-gram embedding table) and 6B active parameters per token. The architecture combines:

**GDN + QSA**: three of every four layers use Gated DeltaNet; the fourth uses Qwen Sparse Attention.**Gated Residual**: four residual branches dynamically control cross-layer reads and writes.**N-gram Embedding**: a 51B lookup memory offloaded to host RAM via`VLLM_PLE_CPU_OFFLOAD=1`

.**MTP**: built-in Multi-Token Prediction for speculative decoding (3 draft tokens).

This recipe uses the [Inferact NVFP4 quantization](https://huggingface.co/Inferact/Qwen3.8-Flash-Next-NVFP4) (~130 GB VRAM minimum) and the upstream `vllm/vllm-openai:qwen38-flash-next`

image with GDN/QSA kernels.

## Prerequisites

**Dynamo Platform installed**— see[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart).**vLLM image**:`vllm/vllm-openai:qwen38-flash-next`

— model-specific build with GDN/QSA kernels.`ai-dynamo`

is pip-installed at pod startup.**Hugging Face access**to`Inferact/Qwen3.8-Flash-Next-NVFP4`

.**Host memory**: ≥ 51 GB per worker for N-gram embedding offload.

## Quick Start

### 1. Create namespace and secret

### 2. Create storage

Edit `model-cache/model-cache.yaml`

and set `storageClassName`

to a ReadWriteMany storage class.

### 3. Download the model

### 4. Deploy

### 5. Smoke test

See the [recipe README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/qwen3.8-flash-next/README.md) for full smoke tests including tool calling and image input.