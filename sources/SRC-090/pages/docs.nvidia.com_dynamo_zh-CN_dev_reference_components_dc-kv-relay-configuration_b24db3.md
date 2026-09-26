source: https://docs.nvidia.com/dynamo/zh-CN/dev/reference/components/dc-kv-relay-configuration
lastmod: 2026-09-23T23:30:39.914Z

Multi-Datacenter KV Relay Configuration


Multi-Datacenter KV Relay Configuration

**Experimental.** The DC KV Relay collects worker KV-cache events within a data center and
publishes compact cache-locality, serving-readiness, and load information for external consumers.

This reference describes `python -m dynamo.kv_dc_relay`

. For deployment, see
[Deploy the DC KV Relay](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental); for an overview and architecture,
see [DC KV Relay Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/multi-dc-kv-routing).

## CLI Arguments

The protocol and gRPC server are included in the standard build. Omitting `--bind`

disables only
the WAN listener; local discovery and pool maintenance still run. Relay has no TLS flags or
certificate configuration. Protect a listener across a trust boundary with an
[optional external sidecar](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental#optional-mtls-sidecar).

## Precedence and Scope

CLI values override the corresponding environment values. A CLI scope option replaces the whole
environment scope: `--namespaces`

, `--namespace-filter`

, and `--watch-all`

are mutually exclusive.
Likewise, a CLI prefix list replaces, rather than extends, the environment prefix list.

- Lists must contain nonempty, unique entries. Comma-separated lists trim item whitespace.
- Prefixes must match whole endpoint segments, not arbitrary string prefixes. With an explicit namespace allowlist, every prefix must belong to one of those namespaces.
`DYN_RELAY_NAMESPACES`

cannot be combined with a true`DYN_RELAY_WATCH_ALL`

.- Boolean environment values accept
`1/0`

,`true/false`

,`yes/no`

, or`on/off`

, ignoring case and surrounding whitespace. Explicit`DYN_RELAY_WATCH_ALL=false`

requires a namespace allowlist. - With neither a CLI nor an environment scope, the Relay watches all visible Dynamo namespaces.

For example, `production`

, `production.backend`

, and `production.backend.generate`

select
successively narrower endpoint scopes. `production.back`

does not match `production.backend`

.

Dynamo namespaces are logical discovery scopes, not Kubernetes namespaces. The current
Kubernetes discovery backend watches only the Relay pod’s Kubernetes namespace. Neither
`--watch-all`

nor `--namespaces`

expands that Kubernetes watch.

## Runtime Environment

Relay uses the shared `DistributedRuntime`

, created by `@dynamo_worker()`

.

For connection settings and runtime defaults, see [Runtime Configuration](https://docs.nvidia.com/dynamo/dev/reference/components/runtime-configuration).
For direct event transport and TCP response-stream addressing, see
[TCP-only deployment](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental#tcp-only-local-planes-no-nats).
For Kubernetes pod identity and RBAC, see [Deploy the DC KV Relay](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental).
Relay’s CLI does not accept the Frontend’s runtime CLI flags; configure the runtime through its
environment variables.

## Producer Tuning

These environment-only overrides also work without a WAN listener. All values must be positive
integers. Unknown `DYN_RELAY_*`

names are not consumed by the launcher; check spelling.

The capacity selected by `--expected-unique-blocks`

must fit the CBI1 maximum of `16777216`

buckets. The Rust producer rejects a larger derived CKF layout at startup.

## WAN Tuning

Every variable below requires `--bind`

or `DYN_RELAY_BIND`

, including publication-resource
overrides that are owned by the universal publisher. Setting one without a listener is a startup
error. All values must be positive integers; byte limits use bytes, not MiB.

### Transport and Projection Timing

### Universal Publication Resources

These limits belong to the publisher; the Python launcher exposes their overrides with WAN enabled.

### Stream Admission

### Validation Limits

WAN timer values cannot exceed `31536000000`

ms. Load fanout capacity cannot exceed `65536`

.
Channel and semaphore capacities must also fit their underlying Tokio limits. The message limit
must be at least `4259904`

bytes and the queue byte bound at least `4194624`

bytes, so each can
hold a maximum CBI1 frame plus its required overhead.

A complete snapshot chunk contains 4 MiB of bucket words plus framing. Configure clients and
sidecars to accept the server’s message size; tonic’s default 4 MiB receive limit is insufficient
for a maximum chunk. Resource exhaustion and snapshot progress deadlines are described in the
[gRPC contract](https://github.com/ai-dynamo/dynamo/blob/main/lib/llm/src/kv_dc_relay/docs/grpc-contract.md).

## Diagnostic Endpoints

The component registers Dynamo runtime endpoints under
`<DYN_NAMESPACE>.kv_dc_relay_<dc-hash>`

, where `dc-hash`

is the first 32 hexadecimal characters
of SHA-256 over the UTF-8 DC ID. These are not HTTP paths or WAN RPCs.

The WAN listener also exposes gRPC reflection and the standard gRPC health service for
`dynamo.kvrelay.v1.KvEventRelay`

. Transport readiness does not prove that pools have been
discovered or that a model can serve requests. Inspect catalog and serving-readiness streams
separately. Terminal host or transport failures stop the component with a nonzero exit status.