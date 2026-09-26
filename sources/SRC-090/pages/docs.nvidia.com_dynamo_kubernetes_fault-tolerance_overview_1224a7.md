source: https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/overview
lastmod: 2026-09-25T12:26:00.485Z

# Fault Tolerance Overview

Choose request-level and worker-level recovery behaviors for production Dynamo deployments.

Dynamo fault tolerance has two layers:

**Request fault tolerance**protects the client-visible request path. Use these guides when you need to recover in-flight requests, reject new work under overload, or stop wasted work after client disconnects.**Worker fault tolerance**protects serving capacity as workers drain, fail, or recover. Use these guides when you need Kubernetes pods to shut down cleanly, recover engines locally, or understand how Dynamo discovers and routes around worker loss.

Most production deployments need both. Request fault tolerance keeps individual generations from failing unnecessarily, while worker fault tolerance keeps the worker pool stable as Kubernetes reschedules pods or hardware faults occur.

## Request Fault Tolerance

These behaviors operate at the request boundary: an incoming request, an in-flight generation, or a client connection.

— Recovers an in-flight generation when a worker fails mid-request by moving the request to another healthy worker.[Request Migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration)**Off by default**— enable it when you want best-effort continuity for long-running generations.— Rejects new requests with HTTP 529 when every worker is too busy, so clients can retry instead of adding queueing delay for everyone.[Request Rejection](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-rejection)**Off by default**— enable it when you want explicit overload behavior.— Stops frontend and runtime work when the client disconnects. This is a built-in runtime behavior and does not require workload configuration.[Request Cancellation](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture)

## Worker Fault Tolerance

These behaviors operate at the worker and engine lifecycle boundary: planned shutdown, pod failure, engine failure, and service discovery.

— Lets a worker finish the requests it is already handling before Kubernetes terminates the pod.[Graceful Shutdown](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/graceful-shutdown)**On by default**— tune the grace period to match your rollout and scale-down behavior.— Runs an active/passive engine pair on the same node so a shadow engine can take over locally after an engine failure. It does not preserve in-flight requests or KV cache state.[Shadow Engine Failover](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/shadow-engine-failover)— Documents the liveness, readiness, and engine-monitoring endpoints used to detect unhealthy workers.[Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks)— Explains the service discovery and lease mechanisms Dynamo uses to detect worker loss and route new traffic to healthy capacity.[Distributed Runtime](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/distributed-runtime)

## Testing and References

Use these Knowledge Base pages when you want the deeper implementation model or validation details:

[Fault Tolerance Testing](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/fault-tolerance-testing)— the framework for validating these behaviors (cancellation, migration, etcd HA failover, hardware fault injection).[Request Migration Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-migration-architecture)— pipeline position, token-state tracking, and worker-failure scenarios.

## Configuration Reference

Every flag and environment variable for configurable fault tolerance behavior is cataloged in the Reference tab:

[Frontend Configuration](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration)— migration limits, independent busy thresholds, overload status, and the threshold API.[Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration)— local worker inhibition and worker-side engine and queue limits.[Observability Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables)— health-check and system-port variables.