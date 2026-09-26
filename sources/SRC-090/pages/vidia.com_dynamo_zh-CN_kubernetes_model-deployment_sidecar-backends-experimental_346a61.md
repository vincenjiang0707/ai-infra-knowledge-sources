source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/model-deployment/sidecar-backends-experimental
lastmod: 2026-09-24T19:58:16.636Z

# Sidecar Backends

**Experimental.** Sidecar packaging, launchers, and API coverage are still
evolving. The sidecar path does not yet match every feature of the in-process
backends.

A Dynamo sidecar runs beside the inference engine process. It registers the engine with Dynamo discovery and forwards engine events into the Dynamo event plane. Today, requests also pass through the sidecar. The target design routes requests directly to the engine’s native gRPC service.

## Design Goals

- Keep the upstream engine’s native serve path and argument surface.
- Move toward public, versioned gRPC contracts with explicit backward compatibility instead of importing private engine APIs.
- Isolate Dynamo and engine dependencies in separate processes.
- Attribute failures through engine-specific and Dynamo-specific logs and health checks.
- Reuse Dynamo’s frontend, routing, planning, and disaggregated-serving orchestration.

## Architecture

* The direct request path is the target design. Today, requests pass
through the sidecar.

In the target design, the frontend and router resolve the engine endpoint through discovery, then send requests directly to the engine. The sidecar stays off the request path and uses the engine’s native gRPC service for metadata and event integration with Dynamo’s discovery and event planes.

## Target Responsibilities

## Current Readiness

Disaggregated launch paths require multiple GPUs and use NIXL for KV transfer. This table describes validated launch topologies, not feature parity with the in-process backends.

See the
[sidecar source and engine-specific READMEs](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/lib/sidecar)
for implementation details.