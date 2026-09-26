source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/multimodal/multimodal-kv-routing
lastmod: 2026-09-23T23:30:39.914Z

# Multimodal KV Routing

## Overview

Multimodal KV routing extends Dynamo’s KV-aware router to account for image content when computing cache overlap scores. An image hash (`mm_hash`

) is computed per request — in the Rust frontend by default for vLLM backends, by vLLM’s own processor when the chat-processor variant is enabled, or by a dedicated MM router worker for TRT-LLM backends — and included in per-block routing metadata. The KV router then selects the backend worker with the highest cache overlap, including overlap on image embedding blocks.

Repeated requests containing the same image are routed to the worker that already has the corresponding KV cache blocks, maximizing prefix cache reuse.

Note: KV cache is separate from embedding cache (also called encoder cache), which reuses vision encoder outputs (image→embeddings) to avoid re-running the encoder. For encoder-side reuse see

[Embedding Cache].

## When to Use

Use multimodal KV routing when:

- You have multiple backend workers serving multimodal requests
- Your workload includes repeated images across requests (e.g., the same product photo, shared reference images)
- You want to maximize KV cache hit rates for multimodal content

Without MM-aware routing, the standard router treats image token blocks as opaque and cannot match which worker has cached a particular image’s KV blocks.

## Support Matrix

(*) The SGLang Rust-frontend path substitutes per-image `pad_value`

tokens in the routing-side view so SGLang’s RadixAttention prefix cache key (`MM_PAD_SHIFT_VALUE + mm_hash % 2^30`

) matches byte-for-byte. Requires the sglang fork with the `mm_hashes`

field on `GenerateReqInput`

([sgl-project/sglang#25300](https://github.com/sgl-project/sglang/pull/25300)).

## Supported Model Families (Rust frontend path)

The Rust frontend’s MM-aware routing path supports whatever VLM families the
`llm-multimodal`

crate registers — see
[ ImageProcessorRegistry::with_defaults()](https://docs.rs/llm-multimodal/1.5.0/llm_multimodal/vision/image_processor/struct.ImageProcessorRegistry.html#method.with_defaults)
for the up-to-date list. A model the registry doesn’t recognize falls back
to text-prefix-only KV routing (request still completes; just no prefix-cache
benefit across images).

The Python chat-processor variant doesn’t share this constraint — it delegates to vLLM’s own multimodal processor and works with any VLM vLLM supports.

## How It Works

### vLLM (default — Rust frontend)

- The Rust frontend computes an
`mm_hash`

per image:`xxh3_64`

of the decoded bytes for`data:`

URIs (and for`http(s)://`

when`media_decoder`

is enabled on the model), otherwise`xxh3_64`

of the full URL string. Two callers will share an`mm_hash`

only when they send byte-identical URLs. - The image-placeholder token id is resolved by delegating to a per-model
`ModelProcessorSpec`

(one spec per supported VLM family — Qwen3-VL, Qwen2.5-VL, Qwen2-VL, LLaVA-NeXT, LLaVA-1.5, Llama-4, Kimi-K2.5). Each spec reads the appropriate`config.json`

field for its model family (`image_token_id`

,`image_token_index`

, or`media_placeholder_token_id`

) and falls back to probing the tokenizer’s vocab when only the placeholder string is registered. Models the registry doesn’t recognise fall back to text-prefix-only routing.


Note:Qwen3.5 / Qwen3.6 image token expansion is not yet supported in the Rust frontend for MM routing, so KV routing will only consider the text inputs + unexpanded image token placeholders. Support will come in a follow-up release.

- Per-image
`(W, H)`

is read from a 64KB`Range`

-bounded header fetch (or from in-memory bytes for`data:`

URIs); the image-processor registry computes the per-image expanded token count. - The single placeholder token is expanded to N copies in
`routing_token_ids`

(a router-only view); the worker still sees one placeholder per image in`token_ids`

. - Per-block MM metadata (
`block_mm_infos`

) is built from the expanded view; the KV router evaluates overlap across workers including image-bearing blocks. - The frontend forwards each image’s
`mm_hash`

(16-hex-char prefix, padded) via`extra_args["mm_hashes"]`

; the backend handler injects them as vLLM’s`multi_modal_uuids`

, so vLLM’s own KV-cache key matches the hash the router used.

### vLLM (alternative — Python chat-processor variant)

Use this variant (`--dyn-chat-processor=vllm`

) when you want the frontend to run vLLM’s HF image processor in-process and ship pre-processed `mm_kwargs`

to the selected worker via shared memory or NIXL RDMA, so the backend skips the HF processor entirely. See the [Transfer Mode Details](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/multimodal/multimodal-kv-routing#transfer-mode-details-vllm-only) section below for the `DYNAMO_MM_TRANSFER`

flags.

### TRT-LLM

For TRT-LLM, a dedicated MM Router Worker sits between the frontend and backend workers. See the [TRT-LLM MM Router README](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples/backends/trtllm/mm_router_worker/README.md) for setup instructions.

### SGLang

Unlike the vLLM path (which forwards `mm_hashes`

as `multi_modal_uuids`

for vLLM’s own KV-event publisher to consume), SGLang’s RadixAttention computes its cache key from the **token IDs** of the prompt, including the per-image `pad_value`

token that gets inserted in place of image placeholders. The router has to substitute that `pad_value`

itself in its token-id view so its overlap calculation matches what the worker will actually cache.

Two preconditions for byte-for-byte alignment between routing-side and server-side hashes:

**Dynamo Rust frontend**computes`pad_value = MM_PAD_SHIFT_VALUE + (mm_hash % 2^30)`

for each image and substitutes that value (× N expansion) in`routing_token_ids`

. Engaged automatically when the worker’s`ModelDeploymentCard`

reports`backend_framework="sglang"`

.**SGLang fork**exposes`GenerateReqInput.mm_hashes: Optional[List[str]]`

. When set,`set_pad_value()`

skips its internal`hash_feature()`

recompute and uses the caller’s hash directly, so the worker’s derived`pad_value`

matches the router’s substitution. See[upstream PR sgl-project/sglang#25300](https://github.com/sgl-project/sglang/pull/25300).

Without both pieces, the routing-side hash and the server-side hash decouple and MM-aware routing silently degrades to text-prefix-only (the request still completes; just no prefix-cache benefit across images).

## Launching

### vLLM (default — Rust frontend)

The Rust frontend computes per-image token counts and expands placeholders
in-process via the `llm-multimodal`

crate, so the router can match vLLM’s
expanded image-token count without invoking the HF image processor. Each
`mm_hash`

is then forwarded to the worker as `multi_modal_uuids`

so vLLM’s
KV events publish the same key the router computes.

Key environment variables:

To opt into frontend image decoding (so the frontend downloads + decodes once and `mm_hash`

becomes content-addressed instead of URL-addressed):

The worker then registers a `media_decoder`

on its model card; the frontend’s `MediaLoader`

runs in-process and hashes decoded RGB bytes via xxh3. Two distinct (signed) URLs of the same image bytes collide on the same routing key.

### vLLM (alternative — Python chat-processor variant)

Uses `--dyn-chat-processor=vllm`

so the frontend runs vLLM’s HF processor
in-process. Adds the `DYNAMO_MM_TRANSFER`

shm/NIXL pre-rendered `mm_kwargs`

delivery channel between frontend and worker.

### TRT-LLM

See the [TRT-LLM MM Router README](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples/backends/trtllm/mm_router_worker/README.md) for full setup instructions and configuration options.

### SGLang

The launcher sets `--kv-events-config`

on each worker plus the standard `--router-mode kv --kv-cache-block-size 16`

on the frontend so the KV router consumes block-level overlap. The SGLang pad-value protocol is engaged automatically — the worker registers `backend_framework="sglang"`

in its `ModelDeploymentCard`

and the frontend picks the matching path from there.

Key environment variables:

Both prerequisites are enabled by default in the dynamo sglang image; the list below is only for users building dynamo from source:

-
Dynamo built with

`--features mm-routing`

(Rust frontend’s image-token counter + the SGLang glue). The container build always passes this; the cargo feature is opt-in only for source builds. -
SGLang with the

`GenerateReqInput.mm_hashes`

field — added by[sgl-project/sglang#25300](https://github.com/sgl-project/sglang/pull/25300)and vendored into the dynamo sglang image via`container/deps/sglang/patches/<ver>/`

.If you’re running against your own sglang install (outside the dynamo image), apply it manually:

Without the patch, the worker’s

`_resolve_mm_hashes_supported`

probe falls through to text-prefix-only routing (no crash, but no MM-aware cache reuse either).

Verification (visible at `DYN_LOG=info,mm_routing=debug`

):

On the second identical request the same worker wins with high overlap (e.g. `137/138 blocks overlap`

on Qwen3-VL-2B with 4 images), confirming MM-aware reuse.

## Transfer Mode Details (vLLM chat-processor variant only)

Applies to the `--dyn-chat-processor=vllm`

launch (`agg_multimodal_router_chat_processor.sh`

), **not** the default Rust frontend path. In the chat-processor variant the frontend runs the HF image processor in-process and ships the pre-processed `mm_kwargs`

to the selected backend worker so the backend can skip re-processing; the `DYNAMO_MM_TRANSFER`

environment variable controls how that payload is transferred.

The default Rust frontend path doesn’t run the HF processor or pre-render `mm_kwargs`

— it forwards only `mm_hashes`

, and each worker re-processes the image itself. TRT-LLM backends similarly re-run their own preprocessing and don’t honor `DYNAMO_MM_TRANSFER`

.

(default): POSIX shared memory via a`shm`

`/dev/shm`

segment. Intended for same-node deployments, where frontend and backend share the host filesystem. If the backend can’t access the segment (e.g., running on a different node), it falls back to re-processing the image from the URL.: NIXL RDMA transfer. Required for cross-node deployments where`nixl`

`/dev/shm`

is not shared between frontend and backend. Works across nodes over InfiniBand or TCP (whichever UCX selects).: Disables pre-processed mm_kwargs transfer entirely. The backend downloads and processes images itself from the original URLs. Useful for debugging or when transfer overhead exceeds re-processing cost.`DYNAMO_DISABLE_NIXL_MM=1`