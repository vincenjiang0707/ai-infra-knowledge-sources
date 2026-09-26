source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/multimodal/multimodal-kv-routing
lastmod: 2026-09-24T19:58:16.636Z

# Multimodal KV Routing

## Overview

Multimodal KV routing extends Dynamo’s KV-aware router to account for image content when computing cache overlap scores. An image hash (`mm_hash`

) is computed per request — by the frontend’s vLLM processor for vLLM backends, or by a dedicated MM router worker for TRT-LLM backends — and included in per-block routing metadata. The KV router then selects the backend worker with the highest cache overlap, including overlap on image embedding blocks.

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

## How It Works

### vLLM

- The frontend’s vLLM processor downloads images and runs
`process_inputs()`

— this invokes the HF image processor and produces expanded token IDs, mm_hashes, and processed pixel values - Per-block routing metadata (
`block_mm_infos`

) is built from the mm_features, tagging blocks that contain image tokens with their mm_hash - The KV router evaluates overlap across all backend workers, accounting for image-bearing blocks
- Pre-processed
`mm_kwargs`

(pixel values, image grid info) are transferred to the selected worker via shared memory (SHM) or NIXL RDMA, so the backend skips the HF processor entirely - The backend injects the received kwargs into its processor cache for accurate MM cache hit rate metrics

On repeated requests with the same image, the selected worker shows higher cached block counts, reducing prefill latency.

**Key advantages:**

**Model-agnostic**: Uses vLLM’s own`process_inputs()`

— supports all multimodal models that vLLM supports, with no model-specific token expansion code**No double processing**: Images are downloaded and processed once on the frontend; the backend receives pre-processed tensors via SHM or NIXL**In-process KV router**: No cross-process RPC overhead for routing decisions

### TRT-LLM

For TRT-LLM, a dedicated MM Router Worker sits between the frontend and backend workers. See the [TRT-LLM MM Router README](https://github.com/ai-dynamo/dynamo/tree/v1.1.1/examples/backends/trtllm/mm_router_worker/README.md) for setup instructions.

## Prerequisites

### Upstream vLLM Patch (vLLM backends only)

MM KV routing on vLLM depends on [vllm-project/vllm#39502](https://github.com/vllm-project/vllm/pull/39502), which exposes `InputProcessor.inject_into_mm_cache()`

as a public API for injecting pre-processed `mm_kwargs`

into the processor cache. Until that PR merges, apply the patch to your installed vLLM:

## Launching

### vLLM

Key environment variables:

### TRT-LLM

See the [TRT-LLM MM Router README](https://github.com/ai-dynamo/dynamo/tree/v1.1.1/examples/backends/trtllm/mm_router_worker/README.md) for full setup instructions and configuration options.

## Transfer Mode Details (vLLM only)

On vLLM backends, the frontend runs the HF image processor and ships the pre-processed `mm_kwargs`

to the selected backend worker so the backend can skip re-processing. The `DYNAMO_MM_TRANSFER`

environment variable controls how that payload is transferred. (TRT-LLM does not use this path — its backend workers re-run their own preprocessing, so `DYNAMO_MM_TRANSFER`

has no effect there.)

(default): POSIX shared memory via a`shm`

`/dev/shm`

segment. Intended for same-node deployments, where frontend and backend share the host filesystem. If the backend can’t access the segment (e.g., running on a different node), it falls back to re-processing the image from the URL.: NIXL RDMA transfer. Required for cross-node deployments where`nixl`

`/dev/shm`

is not shared between frontend and backend. Works across nodes over InfiniBand or TCP (whichever UCX selects).: Disables pre-processed mm_kwargs transfer entirely. The backend downloads and processes images itself from the original URLs. Useful for debugging or when transfer overhead exceeds re-processing cost.`DYNAMO_DISABLE_NIXL_MM=1`