source: https://docs.nvidia.com/dynamo/reference/observability/health-checks
lastmod: 2026-09-24T19:58:16.636Z

# Health Check Reference

Health endpoints, status codes, paths, and active-check configuration

Dynamo exposes two related health interfaces: HTTP status endpoints for external observers and
optional canary requests that actively exercise idle worker endpoints. For a local procedure, see
[Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability#check-deployment-health).

## Endpoint Summary

Set `DYN_SYSTEM_HEALTH_PATH`

or `DYN_SYSTEM_LIVE_PATH`

before process startup to replace the worker
or router paths. For the frontend, use `DYN_HTTP_SVC_HEALTH_PATH`

or `DYN_HTTP_SVC_LIVE_PATH`

.

## Frontend Responses

A live frontend returns `200 OK`

:

During graceful shutdown, `/live`

remains `200 OK`

while the Frontend is draining admitted requests.
After the drain finishes or times out and the service enters the stopping state, `/live`

returns
`503 Service Unavailable`

with status `shutting_down`

.

The frontend `/health`

endpoint returns `200 OK`

while ready and lists the endpoints and instances currently
visible through discovery:

An empty `endpoints`

or `instances`

array means the frontend does not currently discover workers; it
does not change the frontend response status by itself. As soon as graceful draining starts, `/health`

returns `503 Service Unavailable`

with status `not_ready`

and a `stage`

value that identifies the
current lifecycle stage. This removes the Frontend from readiness routing before admitted responses
finish.

## System-Status Responses

Workers and standalone routers expose health endpoints only when `DYN_SYSTEM_PORT`

is zero or a
positive port. A negative value disables the system-status server.

Before the component is ready, `/health`

and `/live`

return `503 Service Unavailable`

:

The worker `/live`

and `/health`

paths currently report the same system-status payload and status
code. After startup, both paths return `200 OK`

with status `ready`

:

`DYN_SYSTEM_STARTING_HEALTH_STATUS`

controls the initial status. The legacy
`DYN_SYSTEM_USE_ENDPOINT_HEALTH_STATUS`

variable is deprecated and no longer controls endpoint
selection in the current runtime.

## Active Canary Configuration

Each backend supplies a minimal inference payload. Dynamo marks the request as a health check and
uses the backend’s normal endpoint path, so the check covers request handling and engine execution
rather than only process reachability. For the lifecycle and rationale, see
[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture#active-worker-health-checks).