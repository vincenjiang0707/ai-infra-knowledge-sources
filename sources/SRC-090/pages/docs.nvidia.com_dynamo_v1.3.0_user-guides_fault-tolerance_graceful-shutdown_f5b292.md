source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/graceful-shutdown
lastmod: 2026-09-24T19:58:16.636Z

# Graceful Shutdown

Coordinates SIGTERM and SIGINT handling so endpoints drain, in-flight requests finish, and pods restart cleanly.

This document describes how Dynamo components handle shutdown signals to ensure in-flight requests complete successfully and resources are properly cleaned up.

## Overview

Graceful shutdown in Dynamo ensures that:

**Routing stops quickly**- Endpoints are unregistered from discovery first**In-flight requests can finish**- Workers keep serving during a short grace period**Endpoints drain**- After the grace period, endpoints are invalidated and optionally wait for in-flight work**Resources are cleaned up**- Engines, connections, and temporary files are released**Pods restart cleanly**- Exit codes signal Kubernetes for proper restart behavior

## Signal Handling

All Dynamo components handle Unix signals for graceful shutdown:

### Implementation

Each component registers signal handlers at startup:

The `graceful_shutdown()`

function:

- Logs the shutdown signal
- Unregisters all endpoints from discovery
- Waits for a configurable grace period (
`DYN_GRACEFUL_SHUTDOWN_GRACE_PERIOD_SECS`

, default 5s) - Calls
`runtime.shutdown()`

to invalidate endpoints and stop accepting new requests - Waits for in-flight requests (based on
`graceful_shutdown`

per endpoint) - Returns to allow cleanup to proceed

The aggregate wait in `runtime.shutdown()`

is bounded by
`DYN_RUNTIME_GRACEFUL_SHUTDOWN_TIMEOUT_SECS`

, which defaults to 900 seconds
(15 minutes). If endpoint draining exceeds this timeout, Dynamo logs the
remaining graceful endpoint count and proceeds with runtime teardown.

## Endpoint Draining

After the grace period, `runtime.shutdown()`

invalidates endpoints so no new requests are accepted. The behavior for in-flight requests depends on the `graceful_shutdown`

parameter when serving the endpoint.

### Configuration

When registering an endpoint, the `graceful_shutdown`

parameter controls draining behavior:

### Component-Specific Behavior

### Frontend HTTP Draining

During frontend HTTP shutdown, Dynamo first marks the frontend as draining. While draining:

`/health`

returns`503 Service Unavailable`

, allowing Kubernetes or ingress controllers to remove the frontend from ready endpoints.`/live`

continues to return`200 OK`

so liveness checks do not restart the frontend while admitted responses are still draining.- New OpenAI-compatible requests are rejected with
`503 Service Unavailable`

. - Requests that have already been admitted continue until their response body completes, including streaming responses.
- Accepted
`/v1/realtime`

WebSocket sessions remain tracked until the WebSocket task exits, even though the HTTP upgrade response has already completed.

The frontend waits for admitted inference requests to finish until
`DYN_HTTP_GRACEFUL_SHUTDOWN_TIMEOUT_SECS`

expires. The default timeout is 5
seconds. After the timeout, the frontend enters stopping and cancels runtime
state.

### Migration Integration

Backend workers always use `graceful_shutdown=True`

, meaning they wait for in-flight requests to complete until the engine is stopped. Request migration is configured at the **frontend** level via `--migration-limit`

:

- When migration is enabled at the frontend, disconnected streams from failed workers are automatically retried on healthy workers
- Workers don’t need to know about migration configuration - they simply complete their work or signal incomplete streams
- See
[Request Migration Architecture](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration)for details on how migration works

## Resource Cleanup

After endpoint draining, components clean up their resources in `finally`

blocks:

### vLLM Worker Cleanup

The handler’s `cleanup()`

method:

- Removes temporary directories (LoRA adapters, etc.)
- Releases engine resources

### SGLang Worker Cleanup

### TensorRT-LLM Worker Cleanup

## Error-Initiated Shutdown

Workers can initiate graceful shutdown when fatal errors occur:

### Engine Health Monitoring (vLLM)

The `VllmEngineMonitor`

continuously checks engine health:

Configuration:

`HEALTH_CHECK_INTERVAL`

: 2 seconds between checks`ENGINE_SHUTDOWN_TIMEOUT`

: 30 seconds max for engine shutdown

### Fatal Error Handling (TensorRT-LLM)

## Kubernetes Integration

### Pod Termination Flow

- Kubernetes sends
`SIGTERM`

to the pod - Dynamo initiates graceful shutdown
- Dynamo operator-created pods have
`terminationGracePeriodSeconds`

to complete (default: 60s) - If not terminated, Kubernetes sends
`SIGKILL`


### Customize the termination grace period

Set `terminationGracePeriodSeconds`

based on your workloads and utilization. For example, use 180 seconds to allow
more time for request draining:

### Health Check Integration

Kubernetes uses health endpoints to determine pod readiness:

**During shutdown**: Endpoints become unavailable**Readiness probe fails**: Traffic stops routing to the pod**Graceful draining**: Existing requests complete

## Best Practices

### 1. Set Appropriate Grace Periods

Match `terminationGracePeriodSeconds`

to your expected request completion time and utilization:

- Short requests (< 10s): 30s grace period
- Long generation (> 30s) or high utilization: 120s+ grace period

### 2. Enable Request Migration

Enable migration at the frontend to allow request recovery when workers shut down:

This allows the frontend to automatically retry disconnected streams on healthy workers.

### 3. Monitor Shutdown Metrics

Track shutdown behavior via logs:

### 4. Handle Cleanup Errors

Ensure cleanup methods handle errors gracefully:

## Related Documentation

[Request Migration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration)- How requests migrate during shutdown[Request Cancellation](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-cancellation)- Canceling in-flight requests[Health Checks](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/health-checks)- Liveness and readiness probes