source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-rejection
lastmod: 2026-09-24T19:58:16.636Z

# Request Rejection

Configure independent worker-load thresholds that shed traffic with HTTP 529

NVIDIA Dynamo rejects new requests when configured worker-load thresholds show that every eligible worker is overloaded.

## Overview

Request rejection (also known as load shedding) is a fault tolerance mechanism that proactively rejects new requests when workers are overloaded. This prevents:

- Cascading failures from resource exhaustion
- Degraded latency for all requests
- Out-of-memory conditions on GPU workers

When every eligible worker exceeds at least one configured busy threshold, new requests receive an HTTP 529 response, signaling clients to retry later.

## Architecture

## Configuration

### Frontend Arguments

Each busy threshold is disabled by default and becomes active when you set a numeric value. Setting one threshold does not enable either of the other checks. For decode-block rejection, start the frontend in KV router mode so the worker-load metrics path is active.

### Dynamic Configuration via API

Set thresholds for a discovered model at runtime through the `/busy_threshold`

endpoint. A numeric
value enables its corresponding rejection check. The update changes the stored threshold
configuration only; the router re-evaluates which workers are busy when the next worker load or
runtime-config update arrives, so a new threshold may take a short time to affect rejection
decisions. The endpoint does not enable `--router-mode kv`

or `--router-track-output-blocks`

; set
those options when the frontend starts if your decode-block monitoring path requires them.

#### Set Thresholds

#### Get Current Thresholds

Response:

### Migrate from `--admission-control`


The `--admission-control`

flag and the `DYN_ADMISSION_CONTROL`

environment variable no longer have
any effect. Both are still accepted so that existing launch commands keep starting, but they are
ignored with a startup warning. Configure only the rejection thresholds that you want Dynamo to
enforce:

Earlier behavior filled unspecified thresholds with preset values after any one threshold was set.
That implicit coupling has been removed: an unset threshold stays disabled. The independent
`--router-queue-threshold`

option also remains disabled until set to a numeric value.

## Busy Detection Logic

Each configured threshold is an independent busy check. A worker is considered busy when any configured check is exceeded; unset checks are skipped.

### Decode-Block Rejection Requirements

Decode-block based rejection (`active_decode_blocks_threshold`

) only works when all of these conditions are true:

- The frontend is started with
`--router-mode kv`

. - A decode-block threshold is configured (
`--active-decode-blocks-threshold`

or`/busy_threshold`

API). - The frontend
`KvWorkerMonitor`

is receiving worker load events (`ActiveLoad`

). - Workers are publishing
`active_decode_blocks`

. - Worker runtime config provides
`kv_total_blocks`

so utilization ratio can be computed. - For long-output workloads,
`--router-track-output-blocks`

is enabled so generated tokens add output blocks to the active block count.

If any prerequisite is missing, decode-block busy detection is effectively disabled for those workers. The most common production symptom is that `--active-decode-blocks-threshold`

appears to be accepted but no HTTP 529 is returned when KV fills up.

Examples of missing prerequisites:

- Frontend was launched without
`--router-mode kv`

; the NATS/event client path used for worker load metrics is not initialized, so`active_decode_blocks`

updates are not consumed and the threshold is ignored. - Frontend cannot receive events because worker-load subscription is unavailable (for example, event transport not reachable or misconfigured).
- Workers are running in a mode/path that does not publish
`active_decode_blocks`

(for example, custom integrations without worker metrics publishing). - Output-heavy traffic is served without
`--router-track-output-blocks`

; only prompt/input blocks are reflected in the router’s active block accounting, so generated output blocks can exhaust KV before triggering decode-block rejection.

### Important: Different from `router_track_active_blocks`


`active_decode_blocks_threshold`

and `router_track_active_blocks`

are related to load, but they are not the same feature:

`active_decode_blocks_threshold`

drives busy/free worker classification and request rejection (HTTP 529 when all workers are busy).`router_track_active_blocks`

controls KV router internal block bookkeeping used for routing decisions.

In disaggregated setups, prefill routing intentionally disables `router_track_active_blocks`

; this does **not** disable decode-block rejection for decode workers.

### KV Cache Block Threshold

Monitors the percentage of KV cache blocks in use:

Example: With `active_decode_blocks_threshold=0.85`

, a worker using 87% of its KV cache blocks is marked busy.

### Prefill Token Threshold

Monitors the number of tokens currently being prefilled:

Example: With `active_prefill_tokens_threshold=10000`

, a worker prefilling 12,000 tokens is marked busy.

### Prefill Token Fraction Threshold

Compares active prefill tokens with a multiple of the worker’s `max_num_batched_tokens`

value:

The absolute and fractional prefill checks use OR logic when both are configured.

### Data-Parallel Rank Aggregation

For workers with multiple data-parallel ranks (tensor parallelism), the worker is only marked busy if **ALL** ranks are busy:

This prevents false positives when only some ranks are temporarily loaded.

## Worker Load Monitoring

The `KvWorkerMonitor`

runs as a background task that:

- Subscribes to KV cache metrics events from workers
- Maintains load state for each worker instance
- Recalculates busy instances when metrics change
- Updates the router with the current busy list

### Metrics Collected

Workers publish these metrics for monitoring:

## Rejection Behavior

### Request Flow

- Request arrives at frontend
- Push router checks if busy threshold is configured
- If configured, router retrieves list of free (non-busy) instances
- If no free instances exist (but instances are registered):
- Request is rejected with
`PipelineError::ServiceOverloaded`

- HTTP 529 response is returned to client

- Request is rejected with

### Error Response

When requests are rejected, clients receive:

#### Configuring the rejection status code

The status code returned for overload rejections is configurable via the
`DYN_HTTP_OVERLOAD_STATUS_CODE`

environment variable on the frontend. It
defaults to `529`

(“Site is overloaded”). Operators whose proxies or clients
only understand `503`

Service Unavailable retry semantics can set
`DYN_HTTP_OVERLOAD_STATUS_CODE=503`

. Any valid HTTP status code is accepted; an
unparseable or out-of-range value falls back to `529`

.

### Client Retry Strategy

Clients should implement exponential backoff when receiving 529 responses:

## Monitoring

### Prometheus Metrics

Track rejection behavior with these metrics:

`dynamo_frontend_model_rejection_total`

: Counter tracking the total number of requests rejected due to resource exhaustion- Labels:
`model`

: The model name being served`endpoint`

: The API endpoint that received the request (e.g.,`chat_completions`

,`completions`

,`embeddings`

)

- This metric is incremented when the router returns a
`ResourceExhausted`

error because all workers are busy. The rejected request is surfaced to the client as an HTTP 529 response.

- Labels:

**Example metrics output:**

For decode-block rejection debugging, also inspect:

**Endpoint:** Available on the frontend HTTP service at `/metrics`

.

## Tuning Thresholds

### Conservative Settings (Latency-Focused)

For applications prioritizing low latency:

- Rejects earlier, before workers become fully loaded
- Maintains lower queue depths
- Better tail latencies

### Aggressive Settings (Throughput-Focused)

For applications prioritizing throughput:

- Allows higher worker utilization
- May increase latency variability
- Better overall throughput

### Disabled (No Rejection)

To disable request rejection entirely:

Without thresholds configured, all requests are accepted regardless of worker load.

## Best Practices

### 1. Start Conservative, Then Tune

Begin with conservative thresholds and increase based on observed behavior:

### 2. Monitor Before Enabling

Observe worker load patterns before setting thresholds:

### 3. Use Workload-Specific Thresholds

In disaggregated deployments:

- Use
`active_prefill_tokens_threshold`

for prefill workers - Use
`active_prefill_tokens_threshold_frac`

instead when the limit should scale with`max_num_batched_tokens`

- Use
`active_decode_blocks_threshold`

for decode workers

### 4. Coordinate with Autoscaling

If using Kubernetes HPA, ensure rejection thresholds trigger before autoscaling:

## Troubleshooting

### Decode-block rejection not triggering

- Confirm threshold is actually set:

- Confirm the frontend was started with
`--router-mode kv`

. - For long-output workloads, confirm the frontend was started with
`--router-track-output-blocks`

. - Verify frontend is receiving worker load updates:

- Check frontend logs for worker-monitor subscription issues (for example, warnings that KV metrics subscriber is unavailable).
- Verify worker
`kv_total_blocks`

is present (runtime config / worker metrics), for example:

- Verify event transport configuration between frontend and workers (
`--event-plane`

, NATS/ZMQ connectivity).

### Common confusion: `router_track_active_blocks`


If `active_decode_blocks_threshold`

is configured but you suspect `router_track_active_blocks`

is the blocker, treat that as a separate routing knob. Busy rejection depends on worker load events and threshold configuration, not on the router’s internal active-block tracking flag.

## Worker-Side Request Admission

In addition to the frontend’s metric-driven busy detection above, a worker can enforce a hard concurrency cap directly at its request-plane ingress. This is disabled by default — when neither knob is set, the worker behaves exactly as before (a large pool plus a large overflow queue, no rejection).

### Knobs

When `--engine-request-limit`

is set, the worker accepts a request directly into
the engine while a slot is free; once all `N`

engine slots are busy, further
requests go into the small overflow queue of size `Q`

; when the engine **and**
the queue are both full the worker rejects the request with
`Server overloaded: worker at capacity`

. The frontend maps this rejection to
`ResourceExhausted`

→ **HTTP 529**, and temporarily marks the worker overloaded
so it is skipped on the next routing decision (cleared automatically on the next
metric recompute). The effective hard cap is **N + Q** in-flight requests per
worker. The overflow channel is sized to `Q-1`

because the single dispatcher
holds one request in transit between the queue and the engine; this makes the
cap exact for **Q ≥ 2** (at `Q = 1`

the channel floors at 1, so the queued
peak is 2 — hence the `Q ≥ 2`

requirement).

### Metrics

## Related Documentation

[Health Checks](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/health-checks)- Worker health monitoring[Metrics](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics)- Available Prometheus metrics[Request Migration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration)- Handling failed requests