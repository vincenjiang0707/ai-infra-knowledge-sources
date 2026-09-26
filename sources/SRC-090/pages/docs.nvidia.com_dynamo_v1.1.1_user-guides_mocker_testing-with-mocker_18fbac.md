source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/mocker/testing-with-mocker
lastmod: 2026-09-24T19:58:16.636Z

# Mocker

The Mocker is a lightweight, high-fidelity simulation of an LLM inference engine, implemented entirely in Rust. It replicates the core scheduling, memory management, and timing behaviors of production engines without requiring a GPU, making it invaluable for testing Dynamo’s routing, KV cache events, disaggregated serving, and planner components.

## Overview

The mocker simulates:

**Block-based KV cache management**with LRU eviction**Engine-specific continuous batching schedulers**for vLLM and SGLang**Prefix caching**with hash-based block deduplication**Chunked prefill**for better batching efficiency**Realistic timing models**for prefill and decode phases**Disaggregated serving**(prefill/decode separation)**KV event publishing**for router integration**Data parallelism**(multiple DP ranks per engine)


Note:While the mocker uses vLLM as its primary reference implementation, these core components—block-based KV cache management, continuous batching schedulers, LRU evictors, and prefix caching—are fundamental to all modern LLM inference engines, including SGLang and TensorRT-LLM. The architectural patterns simulated here are engine-agnostic and apply broadly across the inference ecosystem.

## Quick Start

### Basic Usage

### Disaggregated Serving

### Multiple Workers in One Process

## CLI Arguments

## Environment Variables


Note:For local scale tests and router benchmarks, prefer`--num-workers`

over launching many separate mocker processes. All workers share one tokio runtime and thread pool, which is both lighter weight and closer to how the test harnesses exercise the mocker.

## Trace Replay

The mocker supports replaying Mooncake-style traces through the dedicated replay CLI, which exposes
`offline|online`

, `round_robin|kv_router`

, `arrival_speedup_ratio`

, closed-loop concurrency
admission, synthetic workload generation, and offline disaggregated prefill/decode replay directly:

The replay CLI defaults to `--replay-mode offline`

and `--router-mode round_robin`

. Aggregated
replay uses `--extra-engine-args`

. Offline disagg replay instead uses
`--prefill-engine-args`

plus `--decode-engine-args`

, together with
`--num-prefill-workers`

and `--num-decode-workers`

.

The same CLI also supports synthetic replay without a trace file:

Synthetic replay also supports workload-style generation for shared-prefix and multi-turn tests:

For trace files, replay also understands multi-turn sessions when records share `session_id`

. The
first turn uses `timestamp`

/`created_time`

; later turns can use `delay`

or `delay_ms`

:

For trace-file replay, `--trace-block-size`

controls how many tokens each `hash_id`

represents in
the dataset, while engine `block_size`

still controls the replay engine and router hashing. Public
Mooncake/toolagent traces use `--trace-block-size 512`

; engine `block_size`

can still stay at `64`

to match the live runtime configuration.

The standalone replay CLI prints an AIPerf-style summary table to stdout and writes the full replay report JSON to disk.

Timing semantics:

- trace mode honors first-turn timestamps and inter-turn delays
- concurrency mode ignores first-turn timestamps but still enforces inter-turn delays
- in concurrency mode, TTFT is measured from actual dispatch under the in-flight cap

For full usage, constraints, and benchmarking guidance, see [Mocker Trace Replay](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/mocker/mocker-offline-trace-replay).

Replay supports aggregated `vllm`

and `sglang`

engine configs. Internally replay uses canonical
`block_size`

; for `sglang`

, `sglang.page_size`

is still accepted as a compatibility alias as long
as it matches `block_size`

when both are provided.

Offline replay also supports disaggregated `kv_router`

mode. In that mode:

`--prefill-engine-args`

must describe a prefill worker`--decode-engine-args`

must describe a decode worker`--router-mode`

must be`kv_router`

- only offline replay is supported

Example:

## Performance Modeling Setup

By default, the mocker uses hardcoded polynomial formulas to estimate prefill and decode timing. For more realistic simulations, pass `--planner-profile-data`

with either:

- a mocker-format
`.npz`

file, or - a profiler output directory

The mocker automatically accepts profiler-style results directories and converts them internally.

It also accepts older raw-data directories containing:

`prefill_raw_data.json`

`decode_raw_data.json`


### AIC Performance Model

To use the AIC SDK for latency prediction:

The AIC model automatically uses `--model-path`

and `--engine-type`

to select the appropriate performance data. Available systems include `h200_sxm`

, `h100_sxm`

, etc. (see AIC SDK documentation for the full list).

Important notes:

- AIC is opt-in. If you do not pass
`--aic-perf-model`

,`python -m dynamo.mocker`

does not use AIC. `python -m dynamo.replay`

has two separate AIC surfaces:- engine timing AIC through
`--extra-engine-args`

/ staged engine JSON - router-side prefill-load AIC through top-level
`--aic-*`

flags plus`router_prefill_load_model="aic"`

in`--router-config`


- engine timing AIC through
- The Python AIC session bridge is now shared with the live KV router path via the internal
`dynamo._internal.aic`

module. Mocker CLI behavior is unchanged; this just removes duplicate AIC session code. `aiconfigurator`

must be able to load the requested performance database for the selected`system/backend/version`

. If the SDK is installed but the backing systems data is missing or unreadable, mocker now fails fast at startup with a clear error instead of failing later on first request.- In development environments, this may require pointing Python at a source checkout of
`aiconfigurator`

with real Git LFS payloads materialized in its`systems/`

directory.

This mocker AIC path is separate from the router-side prefill-load estimator. Live router,
frontend, and replay all use `router_prefill_load_model="aic"`

plus top-level `--aic-*`

flags for
oldest-prefill prompt-load decay. Replay still uses engine-args AIC separately when you want the
mocked worker timing model itself to come from AIC.

For aggregated replay, engine timing AIC still comes from `--extra-engine-args`

:

For offline disagg replay, pass the staged engine configs instead:

The `aic_backend`

field enables the AIC perf model and should match `engine_type`

(`"vllm"`

or `"sglang"`

). The `aic_model_path`

field is the equivalent of `--model-path`

in `dynamo.mocker`

.

Replay router-side AIC prompt-load modeling is configured separately with top-level flags:

For offline disagg replay, the same top-level `--aic-*`

flags drive the prefill-stage router only;
the decode-stage router keeps prompt tracking disabled.

Example `--reasoning`

configuration:

The profile results directory should contain:

`selected_prefill_interpolation/raw_data.npz`

`selected_decode_interpolation/raw_data.npz`


To generate profile data for your own model and hardware, run the profiler and then point `--planner-profile-data`

at the resulting output directory.

## Event Transport and Router Testing

The default event path uses the local indexer / event-plane subscriber flow. The older durable KV-events mode is still available through `--durable-kv-events`

, but it is deprecated and should not be the preferred setup for new tests.

For router and indexer experiments that need native wire-format event forwarding, the mocker also supports a ZMQ path:

`--event-plane zmq`

`--zmq-kv-events-ports`

for per-worker PUB base ports`--zmq-replay-ports`

for optional replay/gap-recovery ROUTER base ports

When set, each worker binds on its base port plus `dp_rank`

, so the number of comma-separated base ports must match `--num-workers`

.

## Disaggregation Port Layout

`--bootstrap-ports`

takes a comma-separated list of base ports, one per worker. In multi-worker mode, the number of listed ports must exactly match `--num-workers`

.

Prefill workers listen on these ports and publish the bootstrap endpoint through discovery. Decode workers use the matching ports to rendezvous before decode begins.

## Kubernetes Deployment

The mocker can be deployed through example `DynamoGraphDeployment`

manifests for both aggregated and disaggregated setups:

## Architecture

The mocker is organized into several cooperating components that mirror the internal architecture of production LLM inference engines. The scheduler (vLLM-style and SGLang-style variants) and KV block manager live inside the engine core. Multi-engine behavior — KV transfer/offloading simulation, KV router simulation, planner simulation — is added by the replay harness on top of multiple engine cores; see [Mocker Trace Replay](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/mocker/mocker-offline-trace-replay) for the component-level diagram and for offline replay internals under [ lib/mocker/src/replay/offline/](https://docs.nvidia.com/dynamo/v1.1.1/lib/mocker/src/replay/offline/README.md).

### Scheduler

The mocker now has two scheduler shapes rather than one generic queue model:

**vLLM mocker**uses an upstream-style`waiting + running`

scheduler. Each request tracks computed tokens, the scheduler spends one token budget across the running set first, and decode pressure triggers inline preemption of running requests.**SGLang mocker**uses a cache-aware waiting/running scheduler around a radix-style prefix cache. It batches prefill work with decode-state awareness and handles pressure primarily through decode retraction while preserving cached prefixes.

Both schedulers simulate continuous batching, prefix reuse, chunked prefill, memory pressure, and decode token emission while publishing metrics about current resource utilization.

When resources become constrained, the mocker simulates the engine’s real recovery path:

- vLLM-style decode preemption and recompute
- SGLang-style decode retraction plus prefix-preserving cache updates

### KV Block Manager

The mocker’s KV block manager is now built on [ kvbm-logical::BlockManager<G1>](https://docs.nvidia.com/dynamo/v1.1.1/lib/kvbm-logical), the same logical block manager the real Dynamo runtime uses. The mocker wraps it in

[and translates its own](https://github.com/ai-dynamo/dynamo/blob/36b4208e5e88fa4de75844039b6da06625ae5146/lib/mocker/src/kv_manager/kvbm_backend.rs)

`lib/mocker/src/kv_manager/kvbm_backend.rs`

`MoveBlock`

protocol onto kvbm-logical’s RAII lifecycle (`allocate → stage → register → drop`

).Blocks still conceptually live in one of two pools:

**Active**— blocks currently held by at least one sequence. Partial (still-filling) blocks are held as`MutableBlock<G1>`

; full blocks are held as`ImmutableBlock<G1>`

clones (the clone vec length is the mocker’s refcount, one per`Use`

).**Inactive**— blocks no longer referenced by any sequence but kept for prefix-cache reuse. Handled entirely by kvbm-logical’s inactive pool; the mocker never tracks them manually.

The lifecycle is RAII: dropping the last `ImmutableBlock`

clone transitions the block from active to inactive (kvbm-logical’s `reset`

pool), with no explicit `deref`

/`evict`

bookkeeping on the mocker side. When a sequence completes or is preempted, the mocker simply drops its handles; kvbm-logical recovers the capacity.

Three `Use`

outcomes are tracked for KV-event emission: `ActiveHit`

(bump refcount on an already-pinned block), `InactiveHit`

(reactivate via `match_blocks(plh)`

), and `NewStore`

(fresh allocation). Only `NewStore`

emits a `Stored`

KV event — the router radix tree already knows about the other two and only forgets on explicit `Removed`

.

### Eviction Backends

The kvbm-logical inactive pool selects eviction victims via one of three backends, exposed as `MockerEvictionBackend`

in [ lib/mocker/src/common/protocols.rs](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/lib/mocker/src/common/protocols.rs):

(default) — parent-chain aware: evicts leaf blocks first, preserving shared prefix chains. Subsumes the preemption-priority behavior the old hand-rolled`Lineage`

`LRUEvictor::push_front`

used to provide.— plain recency-based LRU.`Lru`

— 4-tier frequency-aware LRU built on a TinyLFU tracker.`MultiLru`


All three give the same “suffix blocks evicted before shared prefixes” outcome that the old evictor was designed to produce; `Lineage`

does it structurally (via the block parent chain) rather than via monotonic counters.

### Sequence Tracking

Each active request is tracked as a sequence, managing its token blocks and generation state. As tokens are generated, the sequence tracks which blocks are partial (`MutableBlock<G1>`

, still being filled) versus full (`ImmutableBlock<G1>`

, complete and hashable for prefix caching). When a partial block fills up, it gets “promoted” to a full block with a content-based `SequenceHash`

(or collapses onto an existing registered handle if the PLH is already present), enabling future cache hits from requests with matching prefixes.

### Performance Model

The mocker supports three timing prediction modes:

**Polynomial Model (Default):** Uses hardcoded polynomial formulas that approximate typical GPU behavior. Prefill time scales quadratically with token count, while decode time depends on the total active KV cache size.

**Interpolated Model:** Loads actual profiling data from an NPZ file containing measured prefill and decode latencies. The mocker interpolates between data points to predict timing for any input size. This enables high-fidelity simulation matching a specific hardware configuration.

**AIC Model ( --aic-perf-model):** Uses the NVIDIA AI Configurator (AIC) SDK for latency prediction. AIC provides calibrated performance models for specific GPU/model/engine combinations, predicting prefill and decode latency as a function of batch size, sequence length, and prefix cache hits. The model path is automatically derived from

`--model-path`

, and the engine type from `--engine-type`

. This mode is opt-in and requires both the `aiconfigurator`

SDK and loadable systems/perf data for the requested tuple.### Bootstrap Rendezvous (Disaggregated Serving)

For disaggregated prefill/decode deployments, prefill and decode workers coordinate via a simple TCP-based rendezvous protocol. The decode worker connects to the prefill worker’s bootstrap port and waits until the prefill phase completes and KV cache is ready. Either side can arrive first—the rendezvous completes when both are ready.

### KV Transfer Latency Simulation

The mocker simulates KV cache transfer time between prefill and decode workers. Before the prefill worker emits its first (and only) token, it sleeps for a duration based on:

**kv_bytes_per_token**(auto-computed from model config):`num_layers * 2 * num_kv_heads * head_dim * dtype_bytes`

. The`dtype_bytes`

is determined by`--kv-cache-dtype`

: when set to`auto`

(default), it uses the model’s`dtype`

from config; when explicitly set (e.g.,`fp8`

), it uses the specified dtype instead. It can also be overridden directly with`--kv-bytes-per-token`

.**kv_transfer_bandwidth**(default: 64.0 GB/s, inter-node InfiniBand)**Transfer time**:`num_input_tokens * kv_bytes_per_token / bandwidth`


This delay is injected after the scheduler’s prefill compute simulation completes, modeling the sequential flow: prefill computation → KV transfer → decode begins. Set `--kv-transfer-bandwidth 0`

to disable.

## Integration with Dynamo

### KV Event Publishing

When prefix caching is enabled, the mocker publishes KV cache events to the distributed runtime. These events notify the system when blocks are stored (new content cached) or removed (evicted). This enables the KV-aware router to make intelligent routing decisions based on which workers have which prefixes cached.

### Metrics Publishing

Each scheduler publishes metrics about its current state, including the number of active decode blocks per DP rank. The router uses these metrics for load-aware routing decisions.

## Testing Scenarios

The mocker is particularly useful for:

**Router Testing**- Validate KV-aware routing without GPUs**Planner Testing**- Test SLA-based planners with realistic timing**Fault Tolerance**- Test request migration, graceful shutdown**Disaggregation**- Test P/D separation and KV transfer coordination**Performance Modeling**- Prototype scheduling policies**CI/CD**- Fast integration tests without hardware dependencies

## Comparison with Real Engines

## Next Steps

## Feature Gaps (WIP)

For the broader mocker enhancement roadmap, see

[#6383].

The following features are not yet supported by the mocker:

**Multi-tier memory**- No support for offloading KV cache to CPU/disk or onboarding back to GPU; potential future integration with KVBM**Multimodal support**- Currently only simulates text token processing; no vision encoder or cross-attention simulation**Native Rust reference counting**- Work in progress to use native Rc/Arc for block reference counting, enabling natural RAII patterns for simpler tracking