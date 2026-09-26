source: https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/discovery-plane
lastmod: 2026-09-24T19:58:16.636Z

# Discovery Plane

Dynamo’s service discovery layer lets components find each other at runtime. Workers register their endpoints when they start, and frontends discover them automatically. The discovery backend adapts to the deployment environment.


## Discovery Backends


Note:The runtime always defaults to etcd. Kubernetes discovery must be explicitly enabled — the Dynamo operator handles this automatically.

## Kubernetes Discovery

When running on Kubernetes with the Dynamo operator, service discovery uses native Kubernetes resources instead of etcd.

### How It Works

- Workers register their endpoints by creating
**DynamoWorkerMetadata**custom resources. **EndpointSlices**signal pod readiness to the system.- Components watch for CRD changes to discover available workers.

### Benefits

- No external etcd cluster required.
- Native integration with Kubernetes pod lifecycle.
- Automatic cleanup when pods terminate.
- Works with standard Kubernetes RBAC.

### Environment Variables (Injected by Operator)

## etcd Discovery (Default)

When `DYN_DISCOVERY_BACKEND`

is not set (or set to `etcd`

), etcd is used for service discovery.

### Connection Configuration

Example:

### Service Registration

Workers register their endpoints in etcd with a key hierarchy:

For example:

Frontends and routers discover available workers by watching the relevant prefix and receiving real-time updates when workers join or leave.

### Lease-Based Cleanup

Each runtime maintains a lease with etcd (default TTL: 10 seconds). If a worker crashes or loses connectivity:


- Keep-alive heartbeats stop.
- The lease expires after the TTL.
- All registered endpoints are automatically deleted.
- Clients receive removal events and reroute traffic to healthy workers.

This ensures stale endpoints are cleaned up without manual intervention.

## KV Store

Dynamo provides a KV store abstraction for storing metadata (endpoint instances, model deployment cards, event channels). Multiple backends are supported:

## Operational Guidance

### Use Kubernetes Discovery on K8s

The Dynamo operator automatically sets `DYN_DISCOVERY_BACKEND=kubernetes`

for pods. No additional setup required.

### Deploy an etcd Cluster for Bare Metal

For bare-metal production deployments, deploy a 3-node etcd cluster for high availability.

### Tune Lease TTLs

Balance between failure detection speed and overhead:

**Short TTL (5s)**— Faster failure detection, more keep-alive traffic.**Long TTL (30s)**— Less overhead, slower detection.

The default (10s) is a reasonable starting point for most deployments.

## Related Documentation

[Event Plane](https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/event-plane)— Pub/sub for KV cache events and worker metrics[Distributed Runtime](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/distributed-runtime)— Runtime architecture[Request Plane](https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/request-plane)— Request transport configuration[Fault Tolerance](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/overview)— Failure handling