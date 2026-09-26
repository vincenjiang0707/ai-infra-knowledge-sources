source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/modular-components/router/offloading-support-matrix
lastmod: 2026-09-23T23:30:39.914Z

# Offloading Support Matrix

Per-framework support and setup for KV routing with tiered KV cache offloading

Use this matrix to see which KV offloading tiers the Dynamo KV router can use for each framework.

## Support Matrix

Legend: ✅ tier-aware routing · ⚠️ available but not fully validated · 🟡 router-visible, tier-agnostic · 🚧 Dynamo integration in progress · ❌ not yet supported · — does not exist for this framework.

### Status Definitions

**Router-visible (tier-aware).**The worker publishes KV cache events annotated with the storage tier (`medium`

). The router tracks per-tier residency and credits lower-tier prefix hits when selecting workers, weighted by`--router-host-cache-hit-weight`

and`--router-disk-cache-hit-weight`

.**Router-visible (tier-agnostic).**The router keeps blocks indexed across engine-managed tiers but cannot distinguish which tier currently holds them, so per-tier weights do not apply.

Offloading support changes quickly. Version gates are summarized in the matrix and expanded in the per-framework sections below.

## Common Frontend Setup

Every combination starts the frontend the same way:

### Verify Router Visibility

After sending requests, confirm that the router is applying KV events:

A rising `event_type="stored",status="ok"`

counter confirms event ingestion,
but not which tiers are visible. For tier-aware backends, run the frontend with
`DYN_LOG=debug`

and look for `Queried lower-tier indexer`

messages such as
`storage_tier=HostPinned`

. TensorRT-LLM uses a merged GPU + RAM view, so it has
no separate CPU-tier signal. The router does not currently compare a worker’s
offloading configuration with the tiers it observes.

## vLLM

Start each vLLM worker with native CPU offloading and router-usable KV events:

- Versions: vLLM v0.24.0 or later. Earlier versions publish placeholder CPU events that the router silently drops — offloading still works engine-side, but the router only sees the GPU tier.
- Disk and multi-tier offloading (
`TieringOffloadingSpec`

): vLLM main emits FS and OBJ events; Dynamo tier mapping is in progress. - Shared pools: vLLM main emits optional locality metadata; Dynamo shared-pool indexing is in progress.

See [Native KV Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/native-kv-offloading) for the full support matrix (including disaggregated and tensor-parallel status), setup commands, verification, and troubleshooting.

## SGLang

Start each SGLang worker with HiCache and KV event publishing:

- For the Mooncake shared pool: add
`--hicache-storage-backend mooncake`

(plus its extra config) on the workers and`--shared-cache-type hicache --shared-cache-multiplier 0.5`

on the frontend. - Versions: SGLang 0.5.11 or later emits host-tier (
`CPU_PINNED`

) events; earlier versions offload engine-side but the router only sees the GPU tier. With Mooncake, use SGLang 0.5.13 or later to avoid a bundled-Mooncake crash.

See [Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache) for full setup, scoring, verification, and troubleshooting.

## TensorRT-LLM

Start each TensorRT-LLM worker with native host offloading and KV event publishing:

- Versions:
`--publish-kv-events`

requires Dynamo 1.3.0 or later and the PyTorch backend. Earlier releases use the deprecated`--publish-events-and-metrics`

alias. - TensorRT-LLM events do not identify GPU versus host RAM. The router keeps a block indexed while it remains in either tier and removes it after it leaves the lowest tier.
- Native host offloading therefore extends router-visible reuse, but host-tier weights do not apply.

See the [TensorRT-LLM backend docs](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/overview) for worker setup.

## Router Flags for Lower Tiers

### How the router actually computes

The Rust worker selector (`lib/kv-router/src/scheduling/selector.rs`

) scores each candidate worker with:

Before applying the device term, the router computes
`effective_device_credit = overlap_score_credit / (1 + overlap_score_credit_decay * normalized_excess_prefill)`

.
The host, disk, and shared-cache credits do not decay.

The router picks the worker with the **minimum** logit.

### Router Flags

These flags only affect routing. Values range from 0 to 1: 0 ignores lower-tier KV cache hits, while 1 treats them like GPU cache hits.

See [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning) for the cache-hit weight semantics, [Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache#configuration) for the shared-cache flags, and [Router Operations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-operations) for enabling event publishing per backend.

## See Also

[Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide)— routing modes, deployment modes, and event transport[Native KV Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/native-kv-offloading)— vLLM detail page[Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache)— SGLang detail page[KV Cache Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading)— vLLM offloading backend catalog (native, KVBM, LMCache, FlexKV)[Feature Matrix](https://docs.nvidia.com/dynamo/reference/general/compatibility.mdx)— per-backend feature support across Dynamo