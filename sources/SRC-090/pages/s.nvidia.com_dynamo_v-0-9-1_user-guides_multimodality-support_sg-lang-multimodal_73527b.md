source: https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support/sg-lang-multimodal
lastmod: 2026-09-24T19:58:16.636Z

# SGLang Multimodal

This document provides a comprehensive guide for multimodal inference using SGLang backend in Dynamo. SGLang multimodal supports **EPD**, **E/PD**, and **E/P/D** flows, with NIXL (RDMA) for zero-copy tensor transfer in disaggregated modes.

## Support Matrix

### Supported URL Formats

## Deployment Patterns

SGLang supports EPD, E/PD, and E/P/D patterns. See [Multimodal Architecture Patterns](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support#architecture-patterns) for detailed explanations.

### Component Flags

### SGLang-Specific Characteristics

**Vision Encoder in Python**: Encode worker loads vision model (AutoModel) and image processor (AutoImageProcessor)**Token Expansion**: Single`<|image_pad|>`

token replaced with N tokens based on embedding shape**NIXL Transfer**: Embeddings transferred from Encoder → PD Worker using NIXL**No Rust Processing**: All tokenization and image handling happens in Python

## Use the Latest Release

We recommend using the latest stable release of dynamo to avoid breaking changes:

You can find the [latest release](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## EPD Serving (Simple Aggregated)

### Components

- worker:
[DecodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/llm/decode_handler.py)handles encoding, prefilling, and decoding in a single process.

### Workflow

The `DecodeWorkerHandler`

receives multimodal requests with image URLs and passes them directly to SGLang’s engine. SGLang’s internal `mm_data_processor`

handles image fetching, loading, encoding, and token expansion.

### Launch

**Client:**

## E/PD Serving (Encode Separate)

### Components

- workers:
[MultimodalEncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/multimodal/encode_worker_handler.py)for encoding[MultimodalWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for prefilling and decoding.

- processor:
[MultimodalProcessorHandler](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/components/src/dynamo/sglang/request_handlers/multimodal/processor_handler.py)- tokenizes the prompt using the chat template
- passes the text and image url to the MultimodalEncodeWorker.


### Workflow

The `MultimodalEncodeWorker`

downloads and encodes the image and passes the embeddings to the MultimodalWorker. The work complete event is sent via NATS, while the embeddings tensor is transferred via RDMA through the NIXL interface. The `MultimodalWorker`

then prefills and decodes the prompt in the same engine, as in the [LLM aggregated serving](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang) example. Only the processor is registered to the Dynamo frontend as an available endpoint. Workers do NOT register - they are internal components and communicate via NATS.

### Launch

**Client:**

## E/P/D Serving (Full Disaggregation)

### Components

- workers:
[MultimodalEncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/multimodal/encode_worker_handler.py)for encoding[MultimodalWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for decoding[MultimodalPrefillWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/main/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for prefilling

- processor:
[MultimodalProcessorHandler](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/components/src/dynamo/sglang/request_handlers/multimodal/processor_handler.py)tokenizes the prompt and passes it to the MultimodalEncodeWorker.

### Workflow

In models like Qwen2.5-VL, embeddings are only required during the prefill stage. The image embeddings are transferred via NIXL from the Encode Worker to the Decode Worker (the entry point for disaggregation), which then coordinates with the Prefill Worker. The Prefill Worker processes the embeddings and forwards the KV cache back to the Decode Worker for token generation.

### Launch

**Client:**

## Bootstrap Coordination

SGLang disaggregation uses a bootstrap mechanism for P->D coordination:

### Request Flow (Important)

### Bootstrap Process

**Decode Worker**receives request from Encode Worker**Decode Worker**calls Prefill Worker via NATS to request bootstrap info**Prefill Worker**generates`{host, port, room}`

and returns immediately**Both workers**connect to same “room” using bootstrap coordinates**SGLang internally**transfers KV cache state via bootstrap connection (not NIXL)

### Key Difference from vLLM

- vLLM: Frontend → Prefill → Decode (Prefill is entry point)
- SGLang: Frontend → Processor → Encode →
**Decode → Prefill**(Decode is entry point)

## Inter-Component Communication

### Control Flow (NATS)

All component-to-component communication happens via NATS:

#### E/PD Mode (Encode Separate)

#### E/P/D Mode (Full Disaggregation)

### Detailed Message Flow

### Data Transfer (NIXL)

NIXL is used only for embedding transfer:

## Vision Encoding Details

### Encode Worker Components

The encode worker loads and runs the vision model in Python:

### Token Expansion Process

- Processor inserts single image token (e.g.,
`<|image_pad|>`

) - Encode worker generates embeddings:
`shape = (batch, num_patches, hidden_dim)`

- Encode worker replaces single token with
`num_patches`

tokens - Downstream worker receives expanded token sequence

Example:

## Chat Template Processing

SGLang uses its own chat template system:

Supported templates: `qwen2-vl`

, `llama-3`

, `vicuna`

, etc.

## NIXL Usage

**Key Difference:** SGLang P/D uses bootstrap mechanism, not NIXL for KV cache like vLLM.

## Known Limitations

**No Data URL support**- Only HTTP/HTTPS URLs supported;`data:image/...`

base64 URLs not supported**No pre-computed embeddings**- Cannot use`.pt`

,`.pth`

,`.bin`

embedding files; vision encoder runs for every request**No video support**- No video encoder implementation**No audio support**- No audio encoder implementation**Only Processor registers with Dynamo**- Workers are internal components, frontend routes to Processor only**Disaggregated routing**- Decode Worker is the entry point (calls Prefill), cannot route directly to Prefill workers**Limited model generalization**- Token expansion logic is model-specific; adding new models may require implementation updates

## Supported Models

SGLang multimodal **only supports image-based vision-language models**:

**Qwen2-VL**/**Qwen2.5-VL**(primary support)- Models with
`AutoImageProcessor`

and vision tower - Models compatible with SGLang’s image embedding format