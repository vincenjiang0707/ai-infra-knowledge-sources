source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/v-llm-multimodal
lastmod: 2026-09-24T19:58:16.636Z

# vLLM Multimodal

This document provides a comprehensive guide for multimodal inference using the vLLM backend in Dynamo.

**Security Requirement**: All multimodal workers require the
`--enable-multimodal`

flag to be explicitly set at startup. This prevents
unintended processing of multimodal data from untrusted sources. Media requests
are rejected when the flag is absent, and workers configured with a multimodal
role fail at startup. This flag is analogous to `--enable-mm-embeds`

in vLLM
serve but also extends it to all multimodal content (URL, embeddings, and
base64 data).

## Support Matrix

### Supported URL Formats

## Deployment Patterns

The main multimodal vLLM launchers in this repo are:

### Custom Vision Encoders

The legacy aggregated vLLM worker can load an author-provided vision tower in
process, batch images across concurrent requests, and splice the resulting
embeddings into the language-model prompt. See [Custom Vision
Encoders](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/custom-vision-encoders) for the backend contract, launch instructions,
batch sizing guidance, and current limitations.

## Image/Video Serving

Dynamo supports multimodal image and video requests for Vision Language Models (VLMs). `Qwen/Qwen3-VL-2B-Instruct`

is a good example because the same model can handle both `image_url`

and `video_url`

requests through the standard OpenAI chat endpoint.

### Aggregated Serving

Use the single-worker aggregated launcher for the simplest image/video setup:

**Image request:**

**Video request:**

### P/D Serving

Use the P/D launcher to separate prefill and decode without deploying a dedicated multimodal encoder:

For Qwen-VL images, prefill sends grid and embedding-shape metadata so decode can construct schema-valid placeholder embeddings and initialize mRoPE. Other model families use the expanded prompt token IDs produced during prefill.

The P/D handoff does not carry video embeddings. Video and audio inputs are loaded again on the decode worker. This preserves current behavior but adds media download and processing work. Mixed image-and-video P/D requests retain the same model-specific limitations as the legacy vLLM path.

### Unified vLLM Backend

Pass `--unified`

to the aggregated or P/D launchers to run
`python -m dynamo.vllm.unified_main`

. The unified path supports HTTP URLs,
data URLs, frontend-decoded images, `mm_processor_kwargs`

, frontend-provided
multimodal hashes, and Kimi-style `vision_chunk`

inputs.

The Python vLLM frontend can pre-render multimodal processor inputs and send them to an aggregated unified worker. Shared memory is the same-node default; NIXL supports the transfer channel used by cross-node deployments:

The frontend includes the original media references when transfer preparation is unavailable or partial. Fully transferred requests omit those references to avoid duplicating large inline data URIs in the backend payload. A receiver-side failure after a full transfer does not currently have a raw-media fallback.

P/D prefill deliberately uses the original media because it still needs raw-media-derived metadata for the decode handoff.

The unified vLLM entry point does not provide a separate Encode worker and
rejects both `--disaggregation-mode encode`

and `--route-to-encoder`

. Use the
legacy E/PD or E/P/D launchers when a dedicated encoder is required.

### E/PD Serving (Encode + PD)

Use `disagg_multimodal_e_pd.sh`

when you want a separate encode worker and a combined prefill/decode worker. This path is primarily useful for image-centric workloads and embedding-cache experiments.

When a separate encode worker is deployed with the current vLLM path, only `image_url`

inputs are routed to it. `video_url`

inputs are still processed on the combined PD worker.

### E/P/D Serving (Full Disaggregation)

Use `disagg_multimodal_epd.sh`

when you want separate encode, prefill, and decode workers for multimodal workloads.

In the current vLLM implementation, the separate encode worker is only used for `image_url`

inputs. `video_url`

inputs are still processed on the prefill worker, not on the encode worker.

## Audio Serving

Dynamo supports `audio_url`

requests for audio-capable models. Audio is loaded by the backend worker via vLLM’s `AudioMediaIO`

at native sample rate — vLLM’s model-specific processor handles resampling and feature extraction internally. Omni models can handle `image_url`

, `video_url`

, and `audio_url`

in the same request.

### Aggregated Serving

Use the same aggregated multimodal launcher with an audio-capable model:

**Audio request:**

## Embedding Cache

Dynamo supports embedding cache in both aggregated and disaggregated settings:

### Aggregated Worker

A single vLLM instance caches encoded embeddings on CPU so repeated images skip encoding entirely. Supported natively with vLLM 0.17+.

**Launch with Dynamo:**

Both `dynamo.vllm`

and `dynamo.vllm.unified_main`

automatically configure
`ec_both`

mode with `DynamoMultimodalEmbeddingCacheConnector`

when capacity is
greater than zero. A capacity of zero disables the CPU cache. Frontend-provided
multimodal hashes are reused as cache identities so routing and embedding-cache
lookups agree.

**Launch with vllm serve (standalone, no Dynamo):**

The `multimodal_embedding_cache_capacity_gb`

parameter controls the CPU-side LRU cache size in GB (0 = disabled). Requires vLLM 0.17+.

### Disaggregated Encoder (Embedding Cache in Prefill Worker)

In the disaggregated setting, the Prefill Worker (P) owns a CPU-side LRU embedding cache (`EmbeddingCacheManager`

). On each request P checks the cache first — on a hit, the Encode Worker is skipped entirely. On a miss, P routes to the Encode Worker (E), receives embeddings via NIXL, saves them to the cache, and then feeds the embeddings along with the request into the vLLM Instance for prefill.

**Launch:**

**Client:** Use the same `image_url`

request format shown in [Aggregated Serving](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/multimodal/v-llm-multimodal#aggregated-serving).

## LoRA Adapters on Multimodal Workers

Multimodal workers support dynamic loading and unloading of LoRA adapters at runtime via the management API. This enables serving fine-tuned multimodal models alongside the base model.

### Loading a LoRA Adapter

Load an adapter on a running multimodal worker via the `load_lora`

endpoint:

### Sending Requests with a LoRA

Set the `model`

field in the request to the LoRA adapter name:

Requests without a LoRA name (or with the base model name) will use the base model.

### Unloading a LoRA Adapter

### Listing Loaded Adapters

### Disaggregated Mode

In disaggregated (prefill/decode) deployments, the **same LoRA adapter must be loaded on both the prefill and decode workers**. The LoRA identity (`model`

field) is automatically propagated from the prefill worker to the decode worker in the forwarded request.

If a LoRA is loaded on the prefill worker but not on the decode worker, the decode worker will fall back to the base model for that request.

## Supported Models

For a list of multimodal models supported by vLLM, see [vLLM Supported Multimodal Models](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models). Models listed there should generally work with aggregated serving, though they may not all be explicitly tested in this repo.