source: https://docs.nvidia.com/dynamo/zh-CN/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental
lastmod: 2026-09-23T23:30:39.914Z

# Deploy the DC KV Relay

Discover existing workers and publish endpoint-local KV pool facts from Kubernetes

**Experimental.** Deploy NVIDIA Dynamo’s DC KV Relay alongside existing inference workers.
The Relay uses the shared Dynamo runtime and universal publisher; it does not serve inference
requests or choose a destination data center. For the producer model, see
[DC KV Relay Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/multi-dc-kv-routing).

## Prerequisites

- A Dynamo operator installation with the
`DynamoWorkerMetadata`

CRD. - Ready inference workers using Kubernetes discovery in one Kubernetes namespace. They must advertise model cards, KV event sources, and a recoverable KV-state endpoint. Enabling a listener on Relay does not enable worker KV events.
- A container image built from a revision that includes
`dynamo.kv_dc_relay`

, its Rust bindings, and the WAN protocol. Older released images may not contain this module; use the repository’s[container build instructions](https://github.com/ai-dynamo/dynamo/blob/main/container/README.md)from the same revision. - The workers’ event-plane settings: direct ZeroMQ (ZMQ) over TCP, or NATS. Only the NATS variant requires a NATS server and its connection credentials.
- Network access to the Kubernetes API and advertised worker event/recovery endpoints. TCP recovery also needs a return path from workers to Relay’s advertised response-stream address. The NATS variant additionally requires access to the workers’ NATS server.
`kubectl`

, and`grpcurl`

on the machine used for verification.- Kubernetes support for native gRPC startup and readiness probes.

See [Using the Dynamo Frontend](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/using-the-dynamo-frontend) for worker KV-event configuration and
[Runtime Configuration](https://docs.nvidia.com/dynamo/dev/reference/components/runtime-configuration) for shared runtime settings.

## Discovery Scope

The example assumes an existing Kubernetes namespace named `dynamo`

and watches every Dynamo
namespace visible within it. Change the namespace consistently in the commands and RoleBinding
if your workers run elsewhere.

`--namespaces`

selects logical Dynamo namespaces, not Kubernetes namespaces. The current
Kubernetes backend watches only the Relay pod’s Kubernetes namespace. Workers in other
Kubernetes namespaces are invisible even with `--watch-all`

and cluster-wide RBAC.

`DYN_NAMESPACE`

names Relay’s own runtime endpoints and does not select the watched workers.
To narrow the visible logical scope, replace `--watch-all`

with `--namespaces <dynamo-namespace>`

.
Use the namespace in the workers’ advertised endpoint identities, not an assumed Kubernetes name.

Before deployment, confirm discovery resources exist:

This example uses pod-mode discovery, which joins ready EndpointSlices with worker metadata.
Worker Services must carry the discovery labels so their EndpointSlices are watched. Container-mode
discovery instead watches labeled Pods and needs Pod `get/list/watch`

permissions; do not mix
discovery modes without checking the workers’ registration mode.

## Deploy the Relay

Save the following manifest as `kv-dc-relay.yaml`

. Replace `REPLACE_WITH_RELAY_IMAGE`

with your
image and set `--dc-id`

to your stable logical data-center name. Add `imagePullSecrets`

if needed.
The manifest uses TCP requests and NATS events. For a deployment without NATS, apply the
[TCP-only settings](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/deploy-the-dc-kv-relay-experimental#tcp-only-local-planes-no-nats) below before deploying. Otherwise, replace
the sample NATS address with the workers’ address and supply any credentials through Secrets.

The manifest runs one replica with `Recreate`

updates. Restarting Relay changes its incarnation
and requires consumers to reconnect; this is not an HA deployment. CPU and memory values are
starting allocations, not sizing guarantees: pool count and expected unique blocks affect memory.

Relay needs write access to worker metadata because its runtime registers its own endpoints.
The Role is namespaced; it does not grant cross-namespace discovery.
This example assumes a trusted cluster network. The Service exposes plaintext gRPC without
authentication; `ClusterIP`

does not itself restrict which pods can connect. Use local
port-forwarding to inspect runtime diagnostic ports, which are not included in the Service.

### TCP-Only Local Planes (No NATS)

Use Kubernetes discovery, TCP requests, and direct ZMQ events for a deployment without a
messaging server. `DYN_EVENT_PLANE=zmq`

selects ZeroMQ over TCP; `tcp`

is not an event-plane value.
This is independent of the WAN Protobuf/gRPC listener on `5561`

.

In the Relay container’s `env`

list, replace the request/event-plane entries with the following
and remove `NATS_SERVER`

. Keep the other environment entries from the manifest:

The fixed response-stream port is optional; without it, the runtime allocates a free port.
Port `5562`

is used for worker responses to Relay’s runtime requests, not for WAN subscriptions.
It does not need to be added to the WAN Service: workers connect to the advertised pod address.

Workers and other local event consumers must also use `DYN_EVENT_PLANE=zmq`

. For an entirely
TCP-based request path, configure workers with `DYN_REQUEST_PLANE=tcp`

. Changing Relay alone
does not migrate worker publishers. Keep worker KV-event publication enabled, and do not
register a ZMQ broker for these scopes when using direct mode.

Relay discovers direct ZMQ publishers through Kubernetes metadata and connects to their
advertised TCP addresses. Allow those pod-to-pod connections, worker recovery requests, and
the return path to Relay’s response port. Publisher ports may be dynamically allocated;
opening only `5561`

is insufficient. On multi-interface workers, set `DYN_EVENT_PLANE_HOST`

to a reachable pod IP if automatic selection advertises the wrong address. It changes the
advertised address, not the listener’s bind address; use routable IPv4 addresses for direct ZMQ.

Discovery RBAC, the WAN Service, optional mTLS sidecar, and the gRPC checks below are unchanged.

### Apply the Manifest

## Verify Discovery and Published Metadata

Forward the listener to your machine:

In another terminal, query the protocol identity. The decimal marker below is `KVR1`

(`0x4B565231`

); it is required by every Relay request.

Expect this shape; identity values vary per deployment and restart:

Then inspect catalog and readiness. Each command opens a stream; stop it with Ctrl-C after the first update.

Check these fields in the responses:

For a ready disaggregated model, expect separate Prefill and Decode pools but one readiness
entry with both roles. LoRA readiness appears under the base entry’s `adapters`

, not as another
top-level entry. Catalog and readiness revisions are independent.

An empty catalog does not verify discovery; a passing pod probe does not prove model readiness. These checks expose metadata, not CKF contents. CKF validation requires subscribing to an advertised producer and validating its complete CBI1 snapshot and subsequent deltas.

## Expose the WAN Listener

The example Service is cluster-internal. A trusted in-cluster consumer can use
`kv-dc-relay.dynamo.svc.cluster.local:5561`

. Do not turn this plaintext Service into an
unrestricted LoadBalancer or expose the pod port to another data center directly.

For access across a trust boundary, terminate TLS in an external proxy and route only its
protected listener through your network ingress. Keep its upstream connection HTTP/2
and allow long-lived server streams. See the
[gRPC contract](https://github.com/ai-dynamo/dynamo/blob/main/lib/llm/src/kv_dc_relay/docs/grpc-contract.md)
for message sizes, reconnect behavior, and error reasons.

## Optional mTLS Sidecar

Mutual TLS (mTLS) is optional and implemented outside Relay. Relay has no built-in TLS configuration, certificate loading, or authentication. For a protected deployment:

- Change Relay’s bind address to
`127.0.0.1:5561`

. - Add a gRPC-capable sidecar that accepts authenticated TLS connections on a separate pod port
and forwards HTTP/2 to
`127.0.0.1:5561`

, without retries or buffering. - Mount the sidecar’s certificate, key, and trust bundle from Secrets; configure client authorization, certificate rotation, and expiry monitoring in the sidecar.
- Point the Service at the proxy port only; keep Relay’s port
`5561`

bound to loopback. - Replace the pod-IP gRPC probes from the example: they cannot reach a loopback-only listener. Use probes suitable for your proxy and a local Relay check; native Kubernetes gRPC probes do not authenticate through mTLS.

The sidecar’s image and configuration depend on your organization’s proxy and PKI.

For local inspection after this change, forward directly to Relay’s loopback listener:

The plaintext `grpcurl`

commands above still apply. This checks Relay through the Kubernetes
tunnel, not the externally exposed mTLS path.

## Troubleshooting

## Clean Up

Remove only the resources created by this guide; retain the existing workers and namespace:

For all CLI and tuning options, see [Multi-Datacenter KV Relay Configuration](https://docs.nvidia.com/dynamo/dev/reference/components/dc-kv-relay-configuration).