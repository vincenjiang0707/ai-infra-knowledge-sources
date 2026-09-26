source: https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/event-plane
lastmod: 2026-09-24T19:58:16.636Z

# Event Plane

The event plane provides Dynamo with a pub/sub layer for near real-time event exchange between components. It delivers KV cache updates, worker load metrics, and sequence tracking events, enabling features like KV-aware routing and disaggregated serving.

## When Is the Event Plane Used?

Key use cases:

**KV cache events**— Workers publish cache state so the router can make cache-aware scheduling decisions.**Worker load metrics**— Workers report utilization so the router can balance load.**Sequence tracking**— Coordinates active sequences across router replicas for fault-tolerant routing.


## Choosing a Transport

The event plane supports two transports:

## Configuration

### Transport Selection

Set the `DYN_EVENT_PLANE`

environment variable to choose a transport:

Python components also accept this as a CLI flag:

### Environment Variables

When `DYN_EVENT_PLANE`

is not set, the default is **zmq**. Set `DYN_EVENT_PLANE=nats`

to opt into the NATS transport.

## NATS Transport

When using NATS (`DYN_EVENT_PLANE=nats`

):

- Requires a running NATS server. Set
`NATS_SERVER`

if it is not on`localhost:4222`

. - Events are published to NATS subjects scoped by namespace and component.
- Built-in reconnection and message buffering during brief disconnections.

Example setup:

## ZMQ Transport

When using ZMQ (`DYN_EVENT_PLANE=zmq`

):

- No external server required. Each worker binds a ZMQ PUB socket and advertises its address through the discovery system.
- Subscribers automatically discover and connect to all active publishers.
- When publishers come and go (e.g., workers scaling up/down), subscribers dynamically adjust their connections.

Example setup:

## Disabling the Event Plane

If you do not need KV-aware routing, you can disable the event plane entirely:

With `--no-router-kv-events`

:

- The router falls back to prediction-based cache-aware routing (estimates cache state from routing decisions).
- No NATS server or ZMQ sockets are needed.
- TTL-based expiration keeps predicted state from growing stale.

## Deployment Modes

### Bare Metal / Local

Both transports work out of the box:

### Kubernetes (with Dynamo Operator)

The operator can inject `DYN_EVENT_PLANE`

into pods. The same transport options apply. If using NATS, deploy a NATS server in the cluster and set `NATS_SERVER`

accordingly.

## Related Documentation

[Discovery Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/discovery-plane)— Service discovery and coordination (etcd, Kubernetes)[Distributed Runtime](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/distributed-runtime)— Runtime architecture[Request Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/request-plane)— Request transport configuration[Fault Tolerance](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance)— Failure handling