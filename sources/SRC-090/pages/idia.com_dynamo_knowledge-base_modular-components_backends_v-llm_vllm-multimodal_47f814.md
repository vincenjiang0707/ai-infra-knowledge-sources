source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/vllm-multimodal
lastmod: 2026-09-24T19:58:16.636Z

# vLLM Multimodal

This page describes multimodal inference with the Dynamo vLLM backend.

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

**Video input is limited to H.264 and H.265.** The runtime images ship no software
video decoder, so these codecs are decoded on the GPU by NVDEC and no other codec
(VP8, VP9, AV1) has a decoder available. NVDEC decode requires a GPU with a video
decode engine and a container granted the `video`

driver capability — see
[Video Decode GPU Requirements](https://docs.nvidia.com/dynamo/multimodal/video-decode-gpu-requirements).
`http`

, `https`

, `file://`

and `data:`

sources are all hardware-decoded; `file://`

additionally requires `DYN_MM_LOCAL_PATH`

to permit local reads.

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

The main multimodal vLLM launchers in this repo are:

### Custom Vision Encoders

The aggregated vLLM worker can load an author-provided vision tower in
process, batch images across concurrent requests, and splice the resulting
embeddings into the language-model prompt. See [Custom Vision
Encoders](https://docs.nvidia.com/dynamo/advanced-customizations/custom-vision-encoders) for the backend contract, launch instructions,
batch sizing guidance, and current limitations.

## Multimodal KV Routing

vLLM supports two multimodal KV-routing paths. Both give the router and vLLM the same image identity so requests can be placed on workers that already cache the image’s KV blocks.

### Choose a Routing Path

Start with the default path when the model is in Dynamo’s Rust registry. It avoids running the full Hugging Face processor in the frontend and does not require a processed-input transfer channel.

Use the Python chat processor when the Rust registry does not recognize the model, when processor behavior must exactly match vLLM, or when moving preprocessing off workers is worth the added frontend CPU, memory, and transfer cost. Use shared memory for same-node deployments and NIXL for cross-node deployments.

### Default Rust Frontend

The default path keeps multimodal processing on the worker:

- The frontend computes an
`mm_hash`

for each image. - A model-specific processor specification resolves the image placeholder and calculates its expanded token count.
- The frontend expands the placeholder in a routing-only token view and builds per-block multimodal metadata.
- The KV router credits that overlap in its combined prefill-and-decode cost and selects the lowest-cost eligible worker.
- The frontend forwards
`mm_hashes`

, which the worker passes to vLLM as`multi_modal_uuids`

.

By default, the frontend hashes the exact full URI: the complete `data:`

URI string or the HTTP URL including its query string. Set `--frontend-decoding`

on the worker to register frontend media decoding and use decoded image content as the hash input. Content-addressed hashing lets different URLs for identical image bytes share a routing key.

Launch the default path:

Key settings:

### Python Chat Processor

Use the Python path when the model is supported by vLLM but not by the Rust model registry, or when the frontend should preprocess images:

This launcher sets `--dyn-chat-processor vllm`

. The frontend runs vLLM’s Hugging Face processor, extracts hashes and expanded multimodal inputs, builds routing metadata, and transfers processed `mm_kwargs`

to the selected worker. This path supports any VLM handled by vLLM’s multimodal processor.

`DYNAMO_MM_TRANSFER`

selects the transfer mechanism:

`shm`

(default) uses shared memory for same-node frontend and worker deployments.`nixl`

uses NIXL for cross-node transfer.`DYNAMO_DISABLE_NIXL_MM=1`

disables processed-input transfer and makes the worker process the original media.

If a client supplies opaque multimodal UUIDs, Dynamo cannot derive a matching content hash. Those requests use text-prefix routing.

For the user-facing workflow, see [Multimodal KV Routing](https://docs.nvidia.com/dynamo/multimodal/multimodal-kv-routing).

## Image/Video Serving

Dynamo supports multimodal image and video requests for Vision Language Models (VLMs). `Qwen/Qwen3-VL-2B-Instruct`

is a good example because the same model can handle both `image_url`

and `video_url`

requests through the standard OpenAI chat endpoint.

### Aggregated Serving

Use the single-worker aggregated launcher for the simplest image/video setup:

**Image request:**

**Video request:**

### Reuse vLLM multimodal processor cache entries

vLLM can cache processed multimodal inputs under a client-provided opaque UUID. Dynamo currently exposes this behavior for images only. The extension is specific to vLLM; it is not part of the OpenAI Chat Completions API and is not supported by Dynamo’s other backends. Dynamo rejects UUIDs on audio or video, and its SGLang and TensorRT-LLM backends reject image UUIDs rather than silently ignoring unsupported cache semantics.

To enable the cache, pass a nonzero `--mm-processor-cache-gb`

value to the vLLM
worker.

For an aggregated worker, enable Dynamo’s CPU embedding cache alongside the vLLM processor cache:

The caches store different data. The vLLM processor cache retains the processed media metadata required to resolve a UUID-only request. Dynamo’s embedding cache retains encoder output and can restore it after eviction from vLLM’s GPU encoder cache. Keep both caches enabled; the embedding cache alone cannot reconstruct a UUID-only input. Both caches are local to one vLLM engine, so the fill and reuse requests must reach the same aggregated worker.

Populate an entry by adding `uuid`

beside the media field:

Reuse that entry in a later request by setting the media field to `null`

and
sending the same top-level UUID:

UUIDs are opaque nonempty strings and must use the top-level field shown above. A UUID-only request fails on a cache miss because it contains no media payload to process. Dynamo also rejects a media content part that has neither a URL nor a UUID.

When KV-aware routing is enabled, requests with client UUIDs use text-prefix routing. Dynamo cannot convert an opaque client key into its content-derived multimodal routing hash without risking different cache identities at the router and worker.

### P/D Serving

Use the P/D launcher to separate prefill and decode without deploying a dedicated multimodal encoder:

For Qwen-VL images, prefill sends grid and embedding-shape metadata so decode can construct schema-valid placeholder embeddings and initialize mRoPE. Other model families use the expanded prompt token IDs produced during prefill.

The P/D handoff does not carry video embeddings. Video and audio inputs are loaded again on the decode worker. This preserves current behavior but adds media download and processing work. Mixed image-and-video P/D requests retain the same model-specific limitations as the aggregated vLLM path.

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

`dynamo.vllm`

automatically configures
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

request format shown in [Aggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/vllm-multimodal#aggregated-serving).

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