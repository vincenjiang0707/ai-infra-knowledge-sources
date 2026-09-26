source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/fault-tolerance/request-rejection
lastmod: 2026-09-23T23:30:39.914Z

# Request Rejection

This document describes how Dynamo implements request rejection to prevent system overload and maintain service stability under high load conditions.

## Overview

Request rejection (also known as load shedding) is a fault tolerance mechanism that proactively rejects new requests when workers are overloaded. This prevents:

- Cascading failures from resource exhaustion
- Degraded latency for all requests
- Out-of-memory conditions on GPU workers

When all workers exceed their configured busy thresholds, new requests receive an HTTP 503 (Service Unavailable) response, signaling clients to retry later.

## Architecture

## Configuration

### Frontend Arguments

Configure busy thresholds when starting the frontend:

### Dynamic Configuration via API

Thresholds can be adjusted at runtime via the `/busy_threshold`

endpoint:

#### Set Thresholds

#### Get Current Thresholds

Response:

## Busy Detection Logic

Workers are marked as “busy” based on a dual-threshold system. A worker is considered busy when **either** threshold is exceeded.

### KV Cache Block Threshold

Monitors the percentage of KV cache blocks in use:

Example: With `active_decode_blocks_threshold=0.85`

, a worker using 87% of its KV cache blocks is marked busy.

### Prefill Token Threshold

Monitors the number of tokens currently being prefilled:

Example: With `active_prefill_tokens_threshold=10000`

, a worker prefilling 12,000 tokens is marked busy.

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

- HTTP 503 response is returned to client

- Request is rejected with

### Error Response

When requests are rejected, clients receive:

### Client Retry Strategy

Clients should implement exponential backoff when receiving 503 responses:

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

error because all workers are busy. The rejected request is surfaced to the client as an HTTP 503 response.

- Labels:

**Example metrics output:**

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

### 3. Use Both Thresholds for Disaggregated Serving

In disaggregated deployments:

- Use
`active_prefill_tokens_threshold`

for prefill workers - Use
`active_decode_blocks_threshold`

for decode workers

### 4. Coordinate with Autoscaling

If using Kubernetes HPA, ensure rejection thresholds trigger before autoscaling:

## Related Documentation

[Health Checks](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/observability-local/health-checks)- Worker health monitoring[Metrics](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/observability-local/metrics)- Available Prometheus metrics[Request Migration](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/fault-tolerance/request-migration)- Handling failed requests