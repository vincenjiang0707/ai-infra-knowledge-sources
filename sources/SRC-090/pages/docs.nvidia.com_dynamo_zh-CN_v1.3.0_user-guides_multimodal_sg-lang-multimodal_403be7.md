source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/multimodal/sg-lang-multimodal
lastmod: 2026-09-23T23:30:39.914Z

# SGLang Multimodal

This document provides a comprehensive guide for multimodal inference using SGLang backend in Dynamo. SGLang multimodal supports native **EPD** and **EP/D** flows where the SGLang engine performs media encoding, plus explicit encode-worker **E/PD** and **E/P/D** flows with NIXL (RDMA) for zero-copy tensor transfer.

## Support Matrix


MM-aware KV routingis available for SGLang via the Rust frontend — it substitutes per-image`pad_value`

tokens in the routing-side view so SGLang’s RadixAttention prefix-cache key matches the router’s overlap calculation. The frontend auto-detects the backend from the worker’s`ModelDeploymentCard`

(the SGLang worker advertises`backend_framework="sglang"`

), so no deployer-side flag is required. See[Multimodal KV Routing → SGLang section]. That path is orthogonal to the encode-worker / EPD topologies documented below; it’s a frontend routing concern that works with the aggregated SGLang worker layout in`examples/backends/sglang/launch/agg_multimodal_router.sh`

.

### Supported URL Formats

## Deployment Patterns

SGLang supports EPD, EP/D, E/PD, and E/P/D patterns. See [Multimodal Model Serving](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal) for detailed explanations.

### Component Flags

`--dedicated-mm-encoder`

is intentionally explicit. Do not infer the internal E/PD or E/P/D worker path from `--enable-multimodal --disaggregation-mode prefill/decode`

. Native EP/D or P/D uses those same two disaggregation modes, but it stays on the normal SGLang handlers: prefill processes raw image/video inputs to build vision context, while decode reprocesses the same raw media metadata so token layout matches the transferred KV cache. If the dedicated encoder flag is removed or made implicit, native disaggregated deployments can register only internal topology workers and lose the public OpenAI chat/completions surface.

In SGLang E/P/D, keep this flag on both the decode and prefill workers. This differs from vLLM: SGLang’s encode worker delegates generation to `backend.generate`

, which is the decode worker, and that decode worker forwards the precomputed multimodal payload to prefill. With this flag, the internal workers consume transferred embeddings instead of raw image/video URLs, avoiding the duplicate raw-media preprocessing used by native EP/D or P/D.

### SGLang-Specific Characteristics

**Vision Encoder in Python**: Encode worker uses SGLang’s MMEncoder for model-agnostic vision encoding**Token Expansion**: Single`<|image_pad|>`

token replaced with N tokens based on embedding shape**NIXL Transfer**: Embeddings transferred from Encoder → PD Worker using NIXL**No Rust Processing**: All tokenization and image handling happens in Python

## Use the Latest Release

We recommend using the latest stable release of dynamo to avoid breaking changes:

You can find the [latest release](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## EPD Serving (Simple Aggregated)

### Components

- worker:
[DecodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/llm/decode_handler.py)handles encoding, prefilling, and decoding in a single process.

### Workflow

The `DecodeWorkerHandler`

receives multimodal requests with image/video URLs and passes them directly to SGLang’s engine. SGLang’s internal `mm_data_processor`

handles image/video fetching, loading, encoding, and token expansion.

### Launch

**Client:**

Video requests use the same aggregated path:

## EP/D or P/D Serving (No Separate Encode Worker)

### Components

- workers:
[PrefillWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/llm/prefill_handler.py)receives raw multimodal metadata and lets SGLang perform media loading, encoding, token expansion, and KV production during prefill.[DecodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/llm/decode_handler.py)receives matching multimodal metadata so token layout stays aligned with the transferred KV cache.


### Workflow

The Rust frontend tokenizes the request and forwards image/video URLs as `multi_modal_data`

. There is no encode worker. The prefill worker passes those URLs to SGLang’s normal multimodal engine path, so the vision context is produced inside the prefill worker. The decode worker also passes the same URLs to SGLang so the tokenizer manager can reproduce the multimodal token layout while consuming KV cache from prefill.

This native EP/D or P/D path intentionally trades simplicity for duplicated raw-media preprocessing: both prefill and decode call SGLang with `image_data`

/`video_data`

, so SGLang’s multimodal processor may fetch/load/preprocess the same media twice. Use the E/PD or E/P/D encode-worker topology when the deployment must preprocess media once and forward precomputed embeddings.

### Launch

Native P/D and EP/D use the same launchers. The topology is selected by the model: text-only models run P/D, while VLMs run native EP/D where the prefill worker performs the media encode step. Neither path has a separate encode worker.

These launchers pass `--enable-multimodal`

to the prefill and decode workers but deliberately do not pass `--dedicated-mm-encoder`

.

## E/PD Serving (Encode Separate)

### Components

- workers:
[MultimodalEncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/multimodal/encode_worker_handler.py)for image encoding and embeddings generation[MultimodalWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for prefilling and decoding.


### Workflow

The Rust frontend tokenizes the request and extracts image URLs into `multi_modal_data`

. The `MultimodalEncodeWorker`

receives the pre-tokenized request, downloads and encodes the image, and passes the embeddings to the MultimodalWorker. The work complete event is sent via NATS, while the embeddings tensor is transferred via RDMA through the NIXL interface. The `MultimodalWorker`

then prefills and decodes the prompt in the same engine, as in the [LLM aggregated serving](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang) example. Only the encode worker is registered to the Dynamo frontend as an available endpoint. The PD worker does NOT register - it is an internal component and communicates via NATS.

### Launch

**Client:**

## E/P/D Serving (Full Disaggregation)

### Components

- workers:
[MultimodalEncodeWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/multimodal/encode_worker_handler.py)for image encoding and embeddings generation[MultimodalWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for decoding[MultimodalPrefillWorkerHandler](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/sglang/request_handlers/multimodal/worker_handler.py)for prefilling


### Workflow

In models like Qwen2.5-VL, embeddings are only required during the prefill stage. The Rust frontend tokenizes and extracts image URLs. The `MultimodalEncodeWorker`

receives the pre-tokenized request, encodes images, and transfers embeddings via NIXL to the Decode Worker (the entry point for disaggregation), which then coordinates with the Prefill Worker. The Prefill Worker processes the embeddings and forwards the KV cache back to the Decode Worker for token generation.

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

The encode worker uses SGLang’s `MMEncoder`

for model-agnostic vision encoding. `MMEncoder`

handles vision model loading, image preprocessing, and feature extraction internally:

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

**Key Difference:** SGLang native EP/D or P/D uses bootstrap mechanism, not NIXL for KV cache like vLLM.

## Environment Variables

`SGLANG_ENCODER_MM_LOAD_WORKERS`


Controls how many threads the encoder uses to fetch and load images concurrently. When a request contains multiple images (URLs, file paths, or base64 data), each image is loaded in a separate thread. Default is 4. Increase if image loading (network fetch or disk I/O) is the bottleneck rather than GPU compute. Has no effect if the vision encoder itself is the bottleneck, since encoding is sequential on GPU after all images are loaded.

Only applies to the EPD encode worker (which uses [SGLang’s MMEncoder](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/disaggregation/encode_server.py) internally).

## Profiling

Dynamo’s SGLang multimodal workers include NVTX markers for `nsys`

profiling. They are disabled by default (zero overhead) and enabled by setting `DYN_NVTX=1`

.

Key NVTX ranges emitted:

## Known Limitations

**No Data URL support**- Only HTTP/HTTPS URLs supported;`data:image/...`

base64 URLs not supported**No pre-computed embeddings**- Cannot use`.pt`

,`.pth`

,`.bin`

embedding files; vision encoder runs for every request**No audio support**- No audio encoder implementation**Only Processor registers with Dynamo**- Workers are internal components, frontend routes to Processor only**Disaggregated routing**- Decode Worker is the entry point (calls Prefill), cannot route directly to Prefill workers**Limited model generalization**- Token expansion logic is model-specific; adding new models may require implementation updates

## Supported Models

SGLang multimodal **only supports image-based vision-language models**:

**Qwen2-VL**/**Qwen2.5-VL**-`Qwen/Qwen2.5-VL-7B-Instruct`

**Qwen3-VL**-`Qwen/Qwen3-VL-30B-A3B-Instruct`

- Models supported by SGLang’s MMEncoder