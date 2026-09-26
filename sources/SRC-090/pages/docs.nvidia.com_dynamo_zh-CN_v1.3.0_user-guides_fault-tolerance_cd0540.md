source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/fault-tolerance
lastmod: 2026-09-23T23:30:39.914Z

# Fault Tolerance

Dynamo provides comprehensive fault tolerance mechanisms to ensure reliable LLM inference in production deployments. This section covers the various strategies and features that enable Dynamo to handle failures gracefully and maintain service availability.

## Overview

Fault tolerance in Dynamo operates at multiple levels:

## Key Features

### Request Migration

When a worker fails during request processing, Dynamo can migrate in-progress requests to healthy workers. The migration system:

- Preserves partial generation state (accumulated tokens)
- Transparently continues generation on a new worker
- Maintains seamless token flow to clients

See [Request Migration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration) for details.

### Request Cancellation

Dynamo supports canceling in-flight requests to free computational resources:

- Graceful stop signals for clean termination
- Kill signals for immediate termination
- Hierarchical cancellation propagation through request chains

See [Request Cancellation](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-cancellation) for details.

### Graceful Shutdown

Workers handle shutdown signals (SIGTERM/SIGINT) gracefully:

- Immediately stop accepting new requests
- Optionally drain in-flight requests before terminating
- Clean up resources (engines, connections, temp files)

See [Graceful Shutdown](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/graceful-shutdown) for details.

### Request Rejection (Load Shedding)

When workers are overloaded, Dynamo rejects new requests to prevent cascading failures:

- Configurable busy thresholds based on KV cache utilization
- Real-time worker load monitoring
- HTTP 503 responses with retry guidance

See [Request Rejection](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-rejection) for details.

### Health Checks

Dynamo provides multiple health check mechanisms:

**HTTP Endpoints**:`/health`

and`/live`

endpoints for orchestration**Canary Health Checks**: Active monitoring via periodic test requests**Engine Monitoring**: Automatic shutdown on engine failure detection

See [Health Checks](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/health-checks) for details.

### Shadow Engine Failover

For Kubernetes deployments, [Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/shadow-engine-failover) can help with same-node recovery from unknown backend engine or software-process failures. It uses GPU Memory Service to keep model weights resident while a standby or replacement engine attaches. It does not preserve in-flight requests or KV cache state, and it does not cover GPU or node loss.

## Configuration Quick Reference

## Failure Scenarios and Recovery

### Worker Pod Restart

- Worker receives SIGTERM from Kubernetes
- Endpoints are immediately invalidated (no new requests)
- In-flight requests complete or migrate (based on configuration)
- Resources are cleaned up
- Pod restarts with fresh state

### Worker Crash (Unexpected)

- etcd lease expires (TTL-based detection)
- Client discovers endpoint removal via etcd watch
- New requests route to remaining healthy workers
- In-flight requests on crashed worker are migrated (if enabled)

### Network Partition

- Worker loses connectivity to etcd/NATS
- Lease keep-alive fails, lease eventually expires
- Worker is removed from service discovery
- Traffic reroutes to reachable workers

### GPU Failure

- Engine health check detects GPU error (XID, OOM, etc.)
- Worker initiates graceful shutdown
- Runtime is shut down, engine cleaned up
- Process exits with code 1 for pod restart

## Testing Fault Tolerance

Dynamo includes a comprehensive testing framework for validating fault tolerance:

- Request cancellation tests
- Migration tests with worker failures
- etcd HA failover tests
- Hardware fault injection (GPU XID, network partitions)

See [Fault Tolerance Testing](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/testing) for details.

## Related Documentation

[Observability](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local)- Metrics and monitoring[Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/shadow-engine-failover)- Same-node active/passive engine failover for Kubernetes deployments[Distributed Runtime](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/distributed-runtime)- Service discovery architecture[Event Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/event-plane)- Pub/sub for KV cache events and worker metrics[Discovery Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/discovery-plane)- Service discovery and coordination