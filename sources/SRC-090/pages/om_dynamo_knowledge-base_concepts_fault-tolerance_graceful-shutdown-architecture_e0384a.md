source: https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/graceful-shutdown-architecture
lastmod: 2026-09-24T19:58:16.636Z

# Graceful Shutdown Architecture

This document describes the internals of how Dynamo components handle shutdown signals to ensure in-flight requests complete successfully and resources are properly cleaned up.

This is an architecture reference. For how to tune graceful shutdown for a deployment — grace periods, drain windows, and enabling migration — see the [Graceful Shutdown](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/graceful-shutdown) use-case guide.

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

The Frontend uses a separate HTTP drain state before it cancels the distributed runtime:

- Mark the server as draining.
- Return
`503 Service Unavailable`

from`/health`

and reject new OpenAI-compatible requests with 503. - Keep
`/live`

at`200 OK`

so liveness probes do not restart the process while requests drain. - Wait for admitted response bodies, including streaming responses, to complete.
- Continue tracking accepted
`/v1/realtime`

WebSocket sessions until their tasks exit, even though the HTTP upgrade response has completed. - After
`DYN_HTTP_GRACEFUL_SHUTDOWN_TIMEOUT_SECS`

expires (default`5`

seconds), enter the stopping state and cancel runtime state.

This separates readiness from liveness: traffic is removed promptly without turning an intentional drain into a restart loop.

### Migration Integration

Backend workers always use `graceful_shutdown=True`

, meaning they wait for in-flight requests to complete until the engine is stopped. Request migration is configured at the **frontend** level via `--migration-limit`

:

- When migration is enabled at the frontend, disconnected streams from failed workers are automatically retried on healthy workers
- Workers don’t need to know about migration configuration - they simply complete their work or signal incomplete streams
- See
[Request Migration Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-migration-architecture)for details on how migration works

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


### Health Check Integration

Kubernetes uses health endpoints to determine pod readiness:

**During shutdown**: Endpoints become unavailable**Readiness probe fails**: Traffic stops routing to the pod**Graceful draining**: Existing requests complete

## Related Documentation

[Graceful Shutdown](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/graceful-shutdown)- How to tune grace periods and drain windows (use-case guide)[Request Migration Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-migration-architecture)- How requests migrate during shutdown[Request Cancellation Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture)- Canceling in-flight requests[Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks)- Liveness and readiness endpoints