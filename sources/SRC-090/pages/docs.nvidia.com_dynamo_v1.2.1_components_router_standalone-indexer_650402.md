source: https://docs.nvidia.com/dynamo/v1.2.1/components/router/standalone-indexer
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

This is distinct from the [Standalone Router](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/components/src/dynamo/router/README.md), which is a full routing service. The standalone indexer provides only the indexing and query layer without routing logic.

For Dynamo-native remote indexing, use `--serve-indexer`

on `dynamo.frontend`

or `dynamo.router`

and `--use-remote-indexer`

on consumers instead. That request-plane service reuses the router’s existing event ingestion and recovery machinery; it is not implemented by `dynamo.indexer`

.

The HTTP API follows the [Mooncake KV Indexer RFC](https://github.com/kvcache-ai/Mooncake/issues/1403) conventions.

`DYN_ROUTER_MIN_INITIAL_WORKERS`

is also honored here. When set to a positive integer, the
standalone indexer waits for that many workers to register before opening its startup-ready
gate, matching the frontend/router startup behavior.

## Multi-Model and Multi-Tenant Support

The indexer maintains one radix tree per `(model_name, tenant_id)`

pair. Workers registered with different model names or tenant IDs are isolated into separate indexers — queries against one model/tenant never return scores from another.

(required on`model_name`

`/register`

and`/query`

): Identifies the model. Workers serving different models get separate radix trees.(optional, defaults to`tenant_id`

`"default"`

): Enables multi-tenant isolation within the same model. Omit for single-tenant deployments.is per-indexer: the first`block_size`

`/register`

call for a given`(model_name, tenant_id)`

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

After installation, launch the service with `python -m dynamo.indexer`

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
Leave it unset or set it to `0`

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

`POST /register`

— Register an endpoint

Register a ZMQ endpoint for an instance. Each call creates or reuses the indexer for the given `(model_name, tenant_id)`

pair.
Registration is non-blocking: if the worker is not up yet, the listener is accepted in `pending`

state and transitions to `active`

once the initial ZMQ connection succeeds.

`POST /unregister`

— Deregister an instance

Remove an instance. Omitting `tenant_id`

removes the instance from **all** tenants for the given model; providing it targets only that tenant’s indexer.

`GET /workers`

— List registered instances

Returns all registered workers, optionally filtered by model and/or tenant.

Returns:

Filters are independent — providing both `model_name`

and `tenant_id`

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

: per-instance, per-tier breakdown aligned with[Mooncake RFC #1403](https://github.com/kvcache-ai/Mooncake/issues/1403). See[Per-instance tier breakdown](https://docs.nvidia.com/dynamo/v1.2.1/components/router/standalone-indexer#per-instance-tier-breakdown)below.

`POST /query_by_hash`

— Query overlap for pre-computed hashes

Same response format as `/query`

, including the per-instance `instances`

map. Scores are in matched tokens.

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

Returns the full radix tree state as a JSON object keyed by `model_name:tenant_id`

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

The sequence counter (`last_seq`

) persists across unregister/register cycles, so re-registering a worker after a gap will trigger replay on the first batch received by the new listener.

## Limitations

**Standalone mode is ZMQ only**: Workers must publish KV events via ZMQ PUB sockets.**No routing logic**: The indexer only maintains the radix tree and answers queries. It does not track active blocks, manage request lifecycle, or perform worker selection.

## Architecture

### Standalone Mode

### P2P Recovery Flow

## See Also

: Community API standardization for KV cache indexers[Mooncake KV Indexer RFC](https://github.com/kvcache-ai/Mooncake/issues/1403): Full KV router configuration and tuning[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.2.1/components/router/configuration-and-tuning): Architecture and event transport modes[Router Design](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/router-design): Full routing service (routes requests to workers)[Standalone Router](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/components/src/dynamo/router/README.md)