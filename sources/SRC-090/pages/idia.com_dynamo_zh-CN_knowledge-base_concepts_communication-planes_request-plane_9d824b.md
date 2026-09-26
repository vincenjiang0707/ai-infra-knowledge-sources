source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/concepts/communication-planes/request-plane
lastmod: 2026-09-24T19:58:16.636Z

# Request Plane

## Overview

Dynamo supports two transport mechanisms for its request plane (the communication layer between services):

**TCP**(default): Direct TCP connection for optimal performance**NATS**: Message broker-based request plane

This guide explains how to configure and use request plane in your Dynamo deployment.

## What is a Request Plane?

The request plane is the transport layer that handles communication between Dynamo services (e.g., frontend to backend, worker to worker). Different request planes offer different trade-offs:

## Request Plane vs KV Event Plane

Dynamo has **two independent communication planes**:

**Request plane**(): how`DYN_REQUEST_PLANE`

**RPC requests**flow between components (frontend → router → worker), via`tcp`

, or`nats`

.**KV event plane**(): how`DYN_EVENT_PLANE`

**KV cache events**(and optional router replica sync) are distributed for KV-aware routing, via`nats`

or`zmq`

.

**Note:** If you are using `tcp`

request plane with KV events enabled on the router (the default router-side setting), the configured event plane is initialized independently. NATS-based event transport uses `NATS_SERVER`

(default `nats://localhost:4222`

), while ZMQ avoids external NATS infrastructure. SGLang requires explicit `--kv-events-config`

and TRT-LLM requires `--publish-events-and-metrics`

to publish events. For vLLM, KV events are currently auto-configured when prefix caching is active (deprecated — use `--kv-events-config`

explicitly to prepare for a future release where all backends will default to off). To disable the router’s KV event listener, use `--no-router-kv-events`

on the frontend.

Because they are independent, you can mix them.

For example, a deployment with TCP request plane can use different KV event planes:

**NATS Core KV events (local indexer)**: requests use TCP, KV events use NATS Core pub/sub and persistence lives on workers.**ZMQ KV events (local indexer)**: requests use TCP, KV events use direct ZMQ pub/sub, and persistence lives on workers.**No KV events**: requests use TCP and KV routing predicts cache state from routing decisions.

## Payload Codec Negotiation

`DYN_REQUEST_PLANE_CODEC`

sets the payload codec preference advertised by every request-plane
endpoint served by the process. Supported values are `json`

and `msgpack`

; the default is `msgpack`

.
The value is process-wide and cached on its first codec lookup. Restart the process after changing it.

For each request, the client discovers the destination endpoint and uses its advertised codec. If a legacy destination does not advertise a codec, the client uses JSON. The setting on the sending process does not control its outbound requests. Each request and its responses use the same selected codec.

## Configuration

### Environment Variable

Set the request plane mode using the `DYN_REQUEST_PLANE`

environment variable:

Where `<mode>`

is one of:

`tcp`

(default)`nats`


The value is case-insensitive.

### Default Behavior

If `DYN_REQUEST_PLANE`

is not set or contains an invalid value, Dynamo defaults to `tcp`

.

## Usage Examples

### Using TCP (Default)

TCP is the default request plane and provides direct, low-latency communication between services.

**Configuration:**

**Note:** By default, TCP uses an OS-assigned free port (port 0). This is ideal for environments where multiple services may run on the same machine or when you want to avoid port conflicts. If you need a specific port (e.g., for firewall rules), set `DYN_TCP_RPC_PORT`

explicitly.

**When to use TCP:**

- Simple deployments with direct service-to-service communication (e.g. frontend to backend)
- Minimal infrastructure requirements (NATS is initialized when the router listens for KV events; disable with
`--no-router-kv-events`

) - Low-latency requirements

**TCP Configuration Options:**

Additional TCP-specific environment variables:

`DYN_TCP_RPC_HOST`

: Server host address (default: auto-detected)`DYN_TCP_RPC_PORT`

: Server port. If not set, the OS assigns a free port automatically (recommended for most deployments). Set explicitly only if you need a specific port for firewall rules.`DYN_TCP_MAX_MESSAGE_SIZE`

: Maximum message size for TCP client (default: 32MB)`DYN_TCP_SHRINK_MESSAGE_SIZE`

: Threshold for shrinking the zero-copy decoder buffer back to initial size after processing large messages (default: 8MB, max: DYN_TCP_MAX_MESSAGE_SIZE)`DYN_TCP_REQUEST_TIMEOUT`

: Request timeout for TCP client (default: 10 seconds)`DYN_TCP_POOL_SIZE`

: Connection pool size for TCP client (default: 50)`DYN_TCP_CONNECT_TIMEOUT`

: Connect timeout for TCP client (default: 3 seconds)`DYN_TCP_CHANNEL_BUFFER`

: Request channel buffer size for TCP client (default: 100)

### Using NATS

NATS provides a brokered request plane and can also carry KV events and router replica synchronization over NATS Core.

**Prerequisites:**

- NATS server must be running and accessible
- Configure NATS connection via standard Dynamo NATS environment variables

**When to use NATS:**

- Production deployments with service discovery
- Event-backed KV-aware routing when using NATS as the event transport. Note: ZMQ event transport and approximate mode (
`--no-router-kv-events`

) both provide KV routing without NATS, with approximate mode using predicted cache state. - Environments where brokered request routing is preferred

Limitations:

- NATS does not support payloads beyond 16MB (use TCP for larger payloads)

## Complete Example

Here’s a complete example showing how to launch a Dynamo deployment with different request planes:

See [ examples/backends/vllm/launch/agg_request_planes.sh](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/backends/vllm/launch/agg_request_planes.sh) for a complete working example that demonstrates launching Dynamo with TCP or NATS request planes.

## Real-World Example

The Dynamo repository includes a complete example demonstrating both request planes:

**Location:** `examples/backends/vllm/launch/agg_request_planes.sh`


## Architecture Details

### Network Manager

The request plane implementation is centralized in the Network Manager (`lib/runtime/src/pipeline/network/manager.rs`

), which:

- Reads the
`DYN_REQUEST_PLANE`

environment variable at startup - Creates the appropriate server and client implementations
- Provides a transport-agnostic interface to the rest of the codebase
- Manages all network configuration and lifecycle

### Transport Abstraction

All request plane implementations conform to common trait interfaces:

`RequestPlaneServer`

: Server-side interface for receiving requests`RequestPlaneClient`

: Client-side interface for sending requests

This abstraction means your application code doesn’t need to change when switching request planes.

### Configuration Loading

Request plane configuration is loaded from environment variables at startup and cached globally. The configuration hierarchy is:

**Mode Selection**:`DYN_REQUEST_PLANE`

(defaults to`tcp`

)**Transport-Specific Config**: Mode-specific environment variables (e.g.,`DYN_TCP_*`

)

## Migration Guide

### From NATS to TCP

- Stop your Dynamo services
- Set environment variable
`DYN_REQUEST_PLANE=tcp`

- Optionally configure TCP-specific settings (e.g.,
`DYN_TCP_RPC_HOST`

). Note:`DYN_TCP_RPC_PORT`

is optional; if not set, an OS-assigned free port is used automatically. - Restart your services

### Testing the Migration

After switching request planes, verify your deployment:

## Troubleshooting

### Issue: Services Can’t Communicate

**Symptoms:** Requests timeout or fail to reach the backend

**Solutions:**

- Verify all services use the same
`DYN_REQUEST_PLANE`

setting - Check that server ports are not blocked by k8s network policies or firewalls
- For TCP: Ensure host/port configurations are correct and accessible
- For NATS: Verify NATS server is running and accessible

### Issue: “Invalid request plane mode” Error

**Symptoms:** Service fails to start with configuration error

**Solutions:**

- Check
`DYN_REQUEST_PLANE`

spelling (valid values:`nats`

,`tcp`

) - Value is case-insensitive but must be one of the two options
- If not set, defaults to
`tcp`


### Issue: Port Conflicts

**Symptoms:** Server fails to start due to “address already in use”

**Solutions:**

- TCP: By default, TCP uses an OS-assigned free port, so port conflicts should be rare. If you explicitly set
`DYN_TCP_RPC_PORT`

to a specific port and get conflicts, either change the port or remove the setting to use automatic port assignment.

## Performance Considerations

### Latency

**TCP**: Lowest latency due to direct connections and binary serialization**NATS**: Additional broker-hop latency

### Resource Usage

**TCP**: Minimal request-plane infrastructure. KV events use the configured event plane; NATS is needed only when`DYN_EVENT_PLANE=nats`

, and router-side event consumption can be disabled with`--no-router-kv-events`

.**NATS**: Requires running NATS server (additional memory/CPU)