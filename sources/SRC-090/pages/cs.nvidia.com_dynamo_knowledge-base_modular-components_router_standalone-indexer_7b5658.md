source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-indexer
lastmod: 2026-09-24T19:58:16.636Z

# Standalone KV Indexer

## Overview

The standalone KV indexer (`python -m dynamo.indexer`

) is a lightweight service that maintains a radix tree of cached blocks and exposes HTTP endpoints for querying and managing workers.

- It subscribes to ZMQ KV event streams directly from workers.
- It exposes an HTTP API for registration, inspection, and overlap queries.
- It preserves P2P recovery and gap detection/replay for the standalone ZMQ path.
- It indexes device, host-pinned, and disk tier blocks and reports per-tier matches in
`/query`

responses.

This is distinct from the [Standalone Router](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/router/README.md), which is a full routing service. The standalone indexer provides only the indexing and query layer without routing logic.

For Dynamo-native remote indexing, use `--serve-indexer`

on `dynamo.frontend`

or `dynamo.router`

and `--use-remote-indexer`

on consumers instead. That request-plane service reuses the router’s existing event ingestion and recovery machinery; it is not implemented by `dynamo.indexer`

.

The HTTP API follows the [Mooncake KV Indexer RFC](https://github.com/kvcache-ai/Mooncake/issues/1403) conventions.

`DYN_ROUTER_MIN_INITIAL_WORKERS`

is also honored here. When set to a positive integer, the
standalone indexer registers the initial `--workers`

entries, attempts `--peers`

recovery, and
then waits for that catalog count before binding its HTTP listener. Because `/register`

is
unavailable during this wait, the threshold must be met by initial workers, workers recovered
from peers, or a combination of both.

## Model and Routing Group Support

The indexer maintains one radix tree per `(model_name, routing_group)`

pair. Workers registered with different model names or routing groups are isolated into separate indexers. Queries against one pair never return scores from another.

(required on`model_name`

`/register`

and`/query`

): Identifies the model. Workers serving different models get separate radix trees.(optional, defaults to`routing_group`

`"default"`

): Identifies a statically assigned worker pool within the model. Omit it when the model does not need independently selectable pools.is per-indexer: the first`block_size`

`/register`

call for a given`(model_name, routing_group)`

sets the block size. Subsequent registrations for the same pair must use the same block size or the request will fail.

## Compatibility

The standalone indexer works with any engine that publishes KV cache events over ZMQ in the expected msgpack format. This includes bare vLLM and SGLang engines, which emit ZMQ KV events natively — no Dynamo-specific wrapper is required.

Events tagged with non-device storage tiers (host-pinned, disk, external) are routed into a lower-tier slot rather than dropped, and surface in `/query`

responses as `cpu`

/ `disk`

reach.

## Use Cases

**Debugging**: Inspect the radix tree state to verify which blocks are cached on which workers.**State verification**: Confirm that the indexer’s view of KV cache state matches the router’s internal state (used in integration tests).**Custom routing**: Build external routing logic that queries the indexer for overlap scores and makes its own worker selection decisions.**Monitoring**: Observe KV cache distribution across workers without running a full router.**Standalone microservice**: Run an indexer independently of the router/frontend when you want direct HTTP inspection and ZMQ-based ingestion.

## P2P Recovery

Multiple indexer replicas can subscribe to the same ZMQ worker endpoints for fault tolerance. When a replica starts (or restarts after a crash), it bootstraps its radix tree state from a healthy peer before processing live events.

### How It Works

- Workers are registered via
`--workers`

or`/register`

. Each ZMQ listener enters`pending`

state and begins its initial subscribe/connect attempt in the background. - A 1-second delay biases peer recovery past the slow-joiner window, so the dump covers events that may have occurred before a fresh listener can safely start draining.
- The indexer fetches a
`/dump`

from the first reachable peer in`--peers`

. - Dump events are applied to populate the radix tree.
- After recovery completes, the ready gate opens. Any listener whose initial ZMQ connect has already succeeded transitions to
`active`

and begins draining buffered events; listeners for workers that are still down remain`pending`

until they connect.

If no peers are reachable, the indexer starts with an empty state.

### Example: Two-Replica Setup

Both replicas subscribe to the same workers. Replica B recovers A’s tree state on startup, then both independently process live ZMQ events going forward.

### Consistency

The dump is a weakly consistent BFS snapshot of the radix tree — concurrent writes may race with the traversal. This is acceptable because:

**Stale blocks**(partially removed branches): live`Remove`

events will clean them up.**Missing blocks**(partially added branches): live`Stored`

events will add them.- The tree converges to the correct state after live events catch up.

### Peer Management

Peers can be registered at startup via `--peers`

or dynamically via the HTTP API. The peer list is used for recovery only — peers do not synchronize state in real time.

## Building

The service is exposed through the Python bindings package and launched with `python -m dynamo.indexer`

after building the bindings with maturin. Feature flags control which capabilities are compiled in:

### Standalone build

After installation, launch the service from `lib/bindings/python`

with
`../../../.venv/bin/python -m dynamo.indexer`

.

### Standalone build with metrics

This keeps the default `kv-indexer`

build lean while still allowing Prometheus metrics when needed.

## CLI

### Shared Startup Gate

Set `DYN_ROUTER_MIN_INITIAL_WORKERS=<n>`

to require at least `<n>`

workers before the
standalone indexer, frontend push-router path, and KV router config-ready gate all proceed.
For the standalone indexer, the gate runs before the HTTP listener is bound, so its count can
only be satisfied by initial `--workers`

and workers recovered through `--peers`

; `/register`

cannot satisfy it. Leave the variable unset or set it to `0`

to disable the startup wait.

## HTTP API

`GET /health`

— Liveness check

Returns `200 OK`

unconditionally.

`GET /metrics`

— Prometheus metrics

Returns metrics in Prometheus text exposition format. Available when the Python bindings are built with the `kv-indexer-metrics`

feature.

The core event counters aggregate process-wide across model and routing-group indexers and
across all indexer threads. A `duplicate_store`

warning is not necessarily an error:
peer recovery replay can reapply content already restored from a snapshot. Lower-tier
events and listener transport or replay failures are not represented by these core
event counters; use the standalone service metrics and logs for those paths. These
device-tier-only semantics apply to the standalone indexer. The frontend-embedded
router’s component-scoped `dynamo_component_kv_cache_events_applied`

counter includes
both device- and lower-tier events. See [KV Indexer Metrics](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#kv-indexer-metrics).

`POST /reopen_logs`

— Reopen the access log

Reopen the file configured by `--access-log`

after an external log rotation renames or
moves the active file. When access logging is disabled, the endpoint returns the same
successful no-op response.

Returns:

`POST /register`

— Register an endpoint

Register a ZMQ endpoint for an instance. Each call creates or reuses the indexer for the given `(model_name, routing_group)`

pair.
Registration is non-blocking: if the worker is not up yet, the listener is accepted in `pending`

state and transitions to `active`

once the initial ZMQ connection succeeds.

For transition compatibility, indexer HTTP inputs also accept a string `tenant_id`

, and the
CLI accepts the hidden `--tenant-id`

flag. These values are ignored. `routing_group`

always
controls worker eligibility; when it is omitted, the endpoint’s normal default or all-groups
behavior applies. Responses never include `tenant_id`

.

`POST /unregister`

— Deregister an instance

Remove an instance. Omitting `routing_group`

removes the instance from every routing group for the given model; providing it targets one routing group.

`GET /workers`

— List registered instances

Returns all registered workers, optionally filtered by model and routing group.

Returns:

Filters are independent — providing both `model_name`

and `routing_group`

returns only workers matching both. An empty array is returned (not a 404) when no workers match the filter.

`POST /query`

— Query overlap for token IDs

Given raw token IDs, compute block hashes and return per-instance overlap scores (in matched tokens):

Returns:

All counts are in **matched tokens** (block overlap count × block size).

`scores`

/`frequencies`

: legacy device-tier overlap.`scores`

is nested by`instance_id`

then`dp_rank`

. Preserved for backward compatibility — existing callers do not need to change.`instances`

: per-instance, per-tier breakdown aligned with[Mooncake RFC #1403](https://github.com/kvcache-ai/Mooncake/issues/1403). See[Per-instance tier breakdown](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-indexer#per-instance-tier-breakdown)below.

`POST /query_by_hash`

— Query overlap for pre-computed hashes

Same response format as `/query`

, including the per-instance `instances`

map. Scores are in matched tokens.

`block_hashes`

are opaque outputs of token hashing, so the indexer cannot apply or verify a salt
after they have been computed. Callers must precompute these hashes with the intended cache salt
and omit `cache_salt`

from `/query_by_hash`

. Use `/query`

when the indexer should compute salted
hashes from tokens server-side.

### Per-instance tier breakdown

Each entry in `instances`

is keyed by `instance_id`

(as a string) and reports prefix reach across the device, host-pinned, and disk storage tiers:

Tier counts are cumulative because the lower-tier walk reports each tier’s *extension* on top of the previous one. Under a natural offload pipeline (device → host → disk), this guarantees `gpu ≤ cpu ≤ disk`

for every instance — lower tiers extend the device-tier prefix rather than shrink it.

Legacy callers that only consume `scores`

keep working: those values are equal to each instance’s per-`dp_rank`

`gpu`

count.

`GET /dump`

— Dump all radix tree events

Returns the full radix tree state as a JSON object keyed by `model_name:routing_group`

:

Returns:

Each indexer is dumped concurrently. The `block_size`

field lets recovering peers create indexers with the correct block size without requiring `--block-size`

on every replica.

`POST /register_peer`

— Register a peer indexer

`POST /deregister_peer`

— Remove a peer indexer

`GET /peers`

— List registered peers

Returns:

## DP Rank Handling

When a worker registers with the standalone KV indexer (`/register`

), it provides an `instance_id`

, a ZMQ `endpoint`

, and an optional `dp_rank`

(defaults to 0). The service spawns one ZMQ listener per registration.

Each incoming `KvEventBatch`

may carry an optional `data_parallel_rank`

field. If present, it **overrides** the statically-registered `dp_rank`

for that batch. This allows a single ZMQ port to multiplex events from multiple DP ranks.

**Caveat**: the registry only tracks dp_ranks from explicit `/register`

calls. If an engine dynamically emits batches with a dp_rank that was never registered, the indexer will store those blocks correctly (under the dynamic `WorkerWithDpRank`

key), but per-dp_rank deregistration (`/unregister`

with `dp_rank`

) will not find them. Full-instance deregistration (`/unregister`

without `dp_rank`

) still cleans up all dp_ranks for a given `worker_id`

in the tree via `remove_worker`

.

## Gap Detection and Replay

ZMQ PUB/SUB is lossy — messages can be dropped under backpressure or brief disconnects. The indexer detects gaps by tracking the sequence number of each batch: if `seq > last_seq + 1`

, a gap is detected.

When a `replay_endpoint`

is provided during `/register`

, the indexer connects a DEALER socket to the engine’s ROUTER socket and requests the missing batches by sequence number. The engine streams back buffered `(seq, payload)`

pairs from its ring buffer until an empty-payload sentinel.

If no `replay_endpoint`

is configured, gaps are logged as warnings but not recovered.

Deregistration removes the listener’s sequence watermark. Re-registering the same worker and
DP rank therefore starts with a fresh watermark; it does not continue incremental replay from
the previous listener’s `last_seq`

. If the first live batch starts above sequence `0`

, a configured
`replay_endpoint`

triggers replay from sequence `0`

before that live batch is applied. This only
recovers history still retained by the engine. Without a replay endpoint, or when the requested
range is no longer retained, restart with a healthy indexer in `--peers`

to recover its startup
snapshot, or perform another full resynchronization before relying on the rebuilt worker state.

## Limitations

**Standalone mode is ZMQ only**: Workers must publish KV events via ZMQ PUB sockets.**No routing logic**: The indexer only maintains the radix tree and answers queries. It does not track active blocks, manage request lifecycle, or perform worker selection.

## Architecture

### Standalone Mode

### P2P Recovery Flow

## See Also

: Community API standardization for KV cache indexers[Mooncake KV Indexer RFC](https://github.com/kvcache-ai/Mooncake/issues/1403): Full KV router configuration and tuning[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning): Architecture and event transport modes[Router Design](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-design): Full routing service (routes requests to workers)[Standalone Router](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/router/README.md)