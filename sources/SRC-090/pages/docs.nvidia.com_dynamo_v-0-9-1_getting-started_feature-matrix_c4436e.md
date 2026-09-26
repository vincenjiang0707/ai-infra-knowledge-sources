source: https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/feature-matrix
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Feature Compatibility Matrices

This document provides a comprehensive compatibility matrix for key Dynamo features across the supported backends.

*Updated for Dynamo v0.9.1*

**Legend:**

- ✅ : Supported
- 🚧 : Work in Progress / Experimental / Limited

## Quick Comparison

## 1. vLLM Backend

vLLM offers the broadest feature coverage in Dynamo, with full support for disaggregated serving, KV-aware routing, KV block management, LoRA adapters, and multimodal inference including video and audio.

*Source: docs/backends/vllm/README.md*


Notes:

Multimodal + KV-Aware Routing: The KV router uses token-based hashing and does not yet support image/video hashes, so it falls back to random/round-robin routing. ([Source])KV-Aware LoRA Routing: vLLM supports routing requests based on LoRA adapter affinity.Audio Support: vLLM supports audio models like Qwen2-Audio (experimental). ([Source])Video Support: vLLM supports video input with frame sampling. ([Source])Speculative Decoding: Eagle3 support documented. ([Source])

## 2. SGLang Backend

SGLang is optimized for high-throughput serving with fast primitives, providing robust support for disaggregated serving, KV-aware routing, and request migration.

*Source: docs/backends/sglang/README.md*


Notes:

Multimodal + KV-Aware Routing: Not supported. ([Source])Multimodal Patterns: SupportsE/PDandE/P/Donly (requires separate vision encoder). Doesnotsupport simple Aggregated (EPD) or Traditional Disagg (EP/D). ([Source])Request Cancellation: Cancellation during the remote prefill phase is not supported in disaggregated mode. ([Source])Speculative Decoding: Code hooks exist (`spec_decode_stats`

in publisher), but no examples or documentation yet.

## 3. TensorRT-LLM Backend

TensorRT-LLM delivers maximum inference performance and optimization, with full KVBM integration and robust disaggregated serving support.

*Source: docs/backends/trtllm/README.md*


Notes:

Multimodal Disaggregation: Fully supportsEP/D(Traditional) pattern.E/P/D(Full Disaggregation) is WIP and currently supports pre-computed embeddings only. ([Source])Multimodal + KV-Aware Routing: Not supported. The KV router currently tracks token-based blocks only. ([Source])Request Migration: Supported onDecode/Aggregatedworkers only.Prefillworkers do not support migration. ([Source])Speculative Decoding: Llama 4 + Eagle support documented. ([Source])Request Cancellation: Due to known issues, the TensorRT-LLM engine is temporarily not notified of request cancellations, meaning allocated resources for cancelled requests are not freed.