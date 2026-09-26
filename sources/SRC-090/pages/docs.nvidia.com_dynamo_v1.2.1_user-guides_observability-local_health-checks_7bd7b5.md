source: https://docs.nvidia.com/dynamo/v1.2.1/user-guides/observability-local/health-checks
lastmod: 2026-09-24T19:58:16.636Z

# Health Checks

## Overview

Dynamo provides health check and liveness HTTP endpoints for each component which can be used to configure startup, liveness and readiness probes in orchestration frameworks such as Kubernetes.

## Environment Variables

## Getting Started Quickly

Enable health checks and query endpoints:

Check health status:

## Frontend Liveness Check

The frontend liveness endpoint reports a status of `live`

as long as
the service is running.

Frontend liveness doesn’t depend on worker health or liveness only on the Frontend service itself.

### Example Request

### Example Response

## Frontend Health Check

The frontend health endpoint reports a status of `healthy`

as long as
the service is running. Once workers have been registered, the
`health`

endpoint will also list registered endpoints and instances.

Frontend liveness doesn’t depend on worker health or liveness only on the Frontend service itself.

### Example Request

### Example Response

Before workers are registered:

After workers are registered:

## Worker Liveness and Health Check

Health checks for components other than the frontend are enabled
selectively based on environment variables. If a health check for a
component is enabled the starting status can be set along with the set
of endpoints that are required to be served before the component is
declared `ready`

.

Once all endpoints declared in `DYN_SYSTEM_USE_ENDPOINT_HEALTH_STATUS`

are served the component transitions to a `ready`

state until the
component is shutdown. The endpoints return HTTP status code of `HTTP/1.1 503 Service Unavailable`

when initializing and HTTP status code `HTTP/1.1 200 OK`

once ready.

Both /live and /ready return the same information

### Example Environment Setting

#### Example Request

#### Example Response

Before endpoints are being served:

After endpoints are being served:

## Canary Health Checks (Active Monitoring)

In addition to the HTTP endpoints described above, Dynamo includes a **canary health check** system that actively monitors worker endpoints.

### Overview

The canary health check system:

**Monitors endpoint health**by sending periodic test requests to worker endpoints**Only activates during idle periods**- if there’s ongoing traffic, health checks are skipped to avoid overhead**Automatically enabled in Kubernetes**deployments via the operator**Disabled by default**in local/development environments

### How It Works

**Idle Detection**: After no activity on an endpoint for a configurable wait time (default: 10 seconds), a canary health check is triggered**Health Check Request**: A lightweight test request is sent to the endpoint with a minimal payload (generates 1 token)**Activity Resets Timer**: If normal requests arrive, the canary timer resets and no health check is sent**Timeout Handling**: If a health check doesn’t respond within the timeout (default: 3 seconds), the endpoint is marked as unhealthy

### Configuration

#### In Kubernetes (Enabled by Default)

Health checks are automatically enabled by the Dynamo operator. No additional configuration is required.

#### In Local/Development Environments (Disabled by Default)

To enable health checks locally:

#### Configuration Options

### Health Check Payloads

Each backend defines its own minimal health check payload:

**vLLM**: Single token generation with minimal sampling options**TensorRT-LLM**: Single token with BOS token ID**SGLang**: Single token generation request

These payloads are designed to:

- Complete quickly (< 100ms typically)
- Minimize GPU overhead
- Verify the full inference stack is working

### Observing Health Checks

When health checks are enabled, you’ll see logs like:

If an endpoint fails:

### When to Use Canary Health Checks

**Enable in production (Kubernetes):**

- ✅ Detect unhealthy workers before they affect user traffic
- ✅ Enable faster failure detection and recovery
- ✅ Monitor worker availability continuously

**Disable in development:**

- ✅ Reduce log noise during debugging
- ✅ Avoid overhead when not needed
- ✅ Simplify local testing

### Troubleshooting

**Health checks timing out:**

- Increase
`DYN_HEALTH_CHECK_REQUEST_TIMEOUT`

- Check worker logs for errors
- Verify network connectivity

**Too many health check logs:**

- Increase
`DYN_CANARY_WAIT_TIME`

to reduce frequency - Or disable with
`DYN_HEALTH_CHECK_ENABLED=false`

in dev

**Health checks not running:**

- Verify
`DYN_HEALTH_CHECK_ENABLED=true`

is set - Check that
`DYN_SYSTEM_USE_ENDPOINT_HEALTH_STATUS`

includes the endpoint - Ensure the worker is serving the endpoint