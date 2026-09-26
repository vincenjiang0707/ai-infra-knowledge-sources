source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/resources/feature-matrix
lastmod: 2026-09-23T23:30:39.914Z

# Feature Matrix

This document provides a comprehensive compatibility matrix for key Dynamo features across the supported backends.

*Updated for Dynamo v1.2.0*

**Legend:**

- ✅ : Supported
- 🚧 : Work in Progress / Experimental / Limited

## Quick Comparison

## 1. vLLM Backend

vLLM offers the broadest feature coverage in Dynamo, with full support for disaggregated serving, KV-aware routing, KV block management, LoRA adapters, and multimodal inference including video and audio.

*Source: docs/backends/vllm/README.md*


Notes:

Multimodal + KV-Aware Routing: Image-aware KV routing is supported in the documented vLLM paths. The default Rust frontend path supports model families handled by`llm-multimodal`

; the Python chat-processor path delegates to vLLM’s multimodal processor. ([Source])KV-Aware LoRA Routing: vLLM supports routing requests based on LoRA adapter affinity.Audio Support: vLLM supports audio models like Qwen2-Audio (experimental). ([Source])Video Support: vLLM supports video input with frame sampling. ([Source])Speculative Decoding: Eagle3 support documented. ([Source])

## 2. SGLang Backend

SGLang is optimized for high-throughput serving with fast primitives, providing robust support for disaggregated serving, KV-aware routing, and request migration.

*Source: docs/backends/sglang/README.md*


Notes:

Multimodal + KV-Aware Routing: Not supported. ([Source])Multimodal Patterns: Supports simple AggregatedEPD,E/PD, andE/P/Dpatterns. Traditional DisaggEP/Dis not supported. ([Source])Request Cancellation: Cancellation during the remote prefill phase is not supported in disaggregated mode. ([Source])Speculative Decoding: Code hooks exist (`spec_decode_stats`

in publisher), but no examples or documentation yet.

## 3. TensorRT-LLM Backend

TensorRT-LLM delivers maximum inference performance and optimization, with full KVBM integration and robust disaggregated serving support.

*Source: docs/backends/trtllm/README.md*


Notes:

Multimodal Disaggregation: SupportsEP/D(Traditional) andE/P/D(Full Disaggregation) image flows, including image URLs and pre-computed embeddings. ([Source])Multimodal + KV-Aware Routing: Image-aware KV routing is supported through the dedicated TRT-LLM MM Router Worker. It requires KV event publishing on the TRT-LLM workers. ([Source])Request Cancellation: Due to known issues, the TensorRT-LLM engine is temporarily not notified of request cancellations, meaning allocated resources for cancelled requests are not freed.