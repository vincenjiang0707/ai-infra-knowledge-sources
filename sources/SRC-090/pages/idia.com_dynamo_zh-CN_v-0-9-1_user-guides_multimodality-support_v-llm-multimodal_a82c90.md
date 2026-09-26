source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/user-guides/multimodality-support/v-llm-multimodal
lastmod: 2026-09-23T23:30:39.914Z

# vLLM Multimodal

This document provides a comprehensive guide for multimodal inference using vLLM backend in Dynamo.

**Security Requirement**: All multimodal workers require the `--enable-multimodal`

flag to be explicitly set at startup. This is a security feature to prevent unintended processing of multimodal data from untrusted sources. Workers will fail at startup if multimodal flags (e.g., `--multimodal-worker`

, `--multimodal-processor`

) are used without `--enable-multimodal`

.
This flag is analogous to `--enable-mm-embeds`

in vllm serve but also extends it to all multimodal content (url, embeddings, b64).

## Support Matrix

### Supported URL Formats

## Deployment Patterns

vLLM supports all multimodal deployment patterns. See [Architecture Patterns](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support#architecture-patterns) for detailed explanations.

### Component Flags

## Use the Latest Release

We recommend using the latest stable release of dynamo to avoid breaking changes:

You can find the [latest release](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## Image Serving

### E/PD Serving (Encode Separate)

**Components:**

- workers:
[EncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/vllm/multimodal_handlers/encode_worker_handler.py)for encoding and[MultimodalPDWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/components/src/dynamo/vllm/multimodal_handlers/worker_handler.py)for prefilling and decoding. - processor: Tokenizes the prompt and passes it to the EncodeWorkerHandler.
- frontend: HTTP endpoint to handle incoming requests.

**Workflow:**

The EncodeWorkerHandler encodes the image and passes the embeddings to the MultimodalPDWorkerHandler via NATS and RDMA. The work complete event is sent via NATS, while the embeddings tensor is transferred via RDMA through the NIXL interface.


Note:Aggregated serving supports LLaVA 1.5 7B and Qwen2.5-VL-7B-Instruct. Disaggregated serving is currently only confirmed for LLaVA.

**Launch:**

**Client:**

### E/P/D Serving (Full Disaggregation)

**Components:**

- workers:
[EncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/vllm/multimodal_handlers/encode_worker_handler.py)for encoding,[MultimodalDecodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/components/src/dynamo/vllm/multimodal_handlers/worker_handler.py)for decoding, and[MultimodalPDWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/components/src/dynamo/vllm/multimodal_handlers/worker_handler.py)for prefilling. - processor: Tokenizes the prompt and passes it to the EncodeWorkerHandler.
- frontend: HTTP endpoint to handle incoming requests.

**Workflow:**

For the LLaVA model, embeddings are only required during the prefill stage. The EncodeWorkerHandler is connected directly to the prefill worker, encoding the image and passing embeddings via NATS and RDMA. The prefill worker performs the prefilling step and forwards the KV cache to the decode worker.

**Launch:**

## ECConnector Serving

ECConnector is vLLM’s native connector for transferring multimodal embeddings via an Embedding Cache. The encoder worker acts as a **producer** (writes embeddings), while the PD worker acts as a **consumer** (reads embeddings).

**Workflow:**

**Launch:**

**Client:** Same as [E/PD Serving](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support/v-llm-multimodal#epd-serving-encode-separate)

## Llama 4 Serving

The Llama 4 model family is natively multimodal. Unlike LLaVA, they do not directly consume image embeddings as input (see the [vLLM support matrix](https://docs.vllm.ai/en/latest/models/supported_models.html#text-generation_1)). Therefore, the encoder worker is not used and encoding is done alongside prefill.

Example model: `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`

on H100x8.

### Llama 4 Aggregated Serving

**Workflow:**

**Launch:**

**Client:**

### Llama 4 Disaggregated Serving

**Workflow:**

**Launch:**

## Video Serving

### Video Aggregated Serving

**Components:**

- workers:
[VideoEncodeWorker](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/examples/multimodal/components/video_encode_worker.py)for decoding video into frames, and[VllmPDWorker](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/examples/multimodal/components/worker.py)for prefilling and decoding. - processor: Tokenizes the prompt and passes it to the VideoEncodeWorker.
- frontend: HTTP endpoint to handle incoming requests.

**Workflow:**

The VideoEncodeWorker decodes the video into frames. Unlike the image pipeline which generates embeddings, this pipeline passes raw frames directly to the VllmPDWorker via NATS and RDMA.

**Launch:**

**Client:**

### Video Disaggregated Serving

**Workflow:**

For the LLaVA-NeXT-Video-7B model, frames are only required during the prefill stage. The VideoEncodeWorker is connected directly to the prefill worker, decoding the video into frames and passing them via RDMA.

**Launch:**

## Audio Serving

### Audio Aggregated Serving

**Components:**

- workers:
[AudioEncodeWorker](https://github.com/ai-dynamo/dynamo/blob/59d32d259df3669bd7f120175452591482dca5eb/examples/multimodal/components/audio_encode_worker.py)for decoding audio into embeddings, and[VllmPDWorker](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/examples/multimodal/components/worker.py)for prefilling and decoding. - processor: Tokenizes the prompt and passes it to the AudioEncodeWorker.
- frontend: HTTP endpoint to handle incoming requests.

**Workflow:**

**Launch:**

**Client:**

### Audio Disaggregated Serving

**Workflow:**

For the Qwen2-Audio model, audio embeddings are only required during the prefill stage. The AudioEncodeWorker is connected directly to the prefill worker.

**Launch:**

## NIXL Usage

## ModelInput Types and Registration

Dynamo’s Rust SDK supports two input types that determine how the HTTP frontend preprocesses requests:

**Registration Pattern:**

## Known Limitations

**Disaggregated flows require Python Processor**- All multimodal disaggregation requires the Python Processor component (`ModelInput.Text`

).

## Supported Models

The following models have been tested with Dynamo’s vLLM multimodal backend:

**Qwen2.5-VL**-`Qwen/Qwen2.5-VL-7B-Instruct`

**Qwen3-VL**-`Qwen/Qwen3-VL-30B-A3B-Instruct-FP8`

**LLaVA 1.5**-`llava-hf/llava-1.5-7b-hf`

**Llama 4 Maverick**-`meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`

**LLaVA Next Video**-`llava-hf/LLaVA-NeXT-Video-7B-hf`

**Qwen2-Audio**-`Qwen/Qwen2-Audio-7B-Instruct`


For a complete list of multimodal models supported by vLLM, see [vLLM Supported Multimodal Models](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models). Models listed there should work with Simple Aggregated Mode but may not be explicitly tested.