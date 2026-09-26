source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/modular-components/router/topology-aware-kv-transfer
lastmod: 2026-09-23T23:30:39.914Z

Topology-Aware KV Transfer


Topology-Aware KV Transfer

Runtime metadata and decode routing semantics for topology-aware prefill/decode handoff

**Experimental.** Topology-aware KV transfer in NVIDIA Dynamo constrains or biases decode worker selection after a prefill worker has been selected. The router derives standard `RoutingConstraints`

from the selected prefill worker’s published topology metadata, then merges those constraints into the decode request.

Use the Kubernetes operator path when possible. For the Kubernetes configuration fields, see the
[KvTransferPolicy API](https://docs.nvidia.com/dynamo/dev/reference/api/kubernetes/full-api-reference#kvtransferpolicy).

## Runtime Contract

Workers publish topology and policy fields through `ModelRuntimeConfig`

:

Each topology entry also becomes a canonical worker taint:

For example:

This creates worker taints:

The KV-transfer policy uses only `kv_transfer_domain`

to derive the decode constraint. Other topology domains remain available as ordinary routing taints.

## Request Flow

The prefill router builds the decode constraint before dispatching prefill when the selected worker is already known. This keeps `required`

policy fail-closed: if the router cannot derive authoritative decode constraints for a required policy, it fails the request instead of dispatching prefill and then discovering that decode cannot be routed safely.

## Enforcement Modes

### Required

`required`

turns the selected prefill worker’s transfer-domain topology into a required taint.

Decode workers without that taint are ineligible. If no eligible decode worker exists, routing returns no endpoint for that request.

### Preferred

`preferred`

turns the same topology into a preferred taint.

Decode workers that satisfy existing required constraints remain eligible, but matching workers receive a routing-cost bias. When enforcement is `preferred`

, `preferredWeight`

is required, must be from `0`

to `1`

, and controls the strength of that bias. It is not a probability and does not guarantee same-domain selection.

## Worker Environment Contract

The Python backend utility reads topology from files and transfer policy from environment variables:

Each non-hidden, non-empty file under `DYN_TOPOLOGY_MOUNT_PATH`

is interpreted as one topology domain. The file name is the domain; the file content is the worker’s value for that domain.

For example:

When topology is enabled, the worker polls once per second for up to 30 seconds until the selected transfer-domain file exists and has content. If it remains missing or empty, the worker exits so the bad topology source is visible during startup.

## Backend Support

The integrated Python backends apply the topology config during worker registration:

- vLLM
- SGLang
- TensorRT-LLM
- Mocker, for simulation and tests

The topology utility writes the fields onto `ModelRuntimeConfig`

; Rust owns validation and canonical topology-taint generation.

## Interactions with Existing Routing Constraints

Topology-aware KV transfer uses the existing `RoutingConstraints`

path. It does not add a topology-specific selector. If a request already has routing constraints, the prefill router merges the generated topology constraints into the decode request:

- Required topology taints are appended to existing
`required_taints`

. - Preferred topology taints are appended to existing
`preferred_taints`

.

User-provided constraints still apply. A decode worker must satisfy all required constraints to be eligible.

## Operational Notes

- Configure this only for disaggregated prefill/decode deployments. Aggregated workers do not perform a remote prefill-to-decode KV transfer.
- Keep
`DYN_ROUTER_MODE=kv`

on the frontend so the prefill and decode routing paths use the KV router. - Make sure every prefill domain has enough decode capacity when using
`required`

; otherwise the router can legitimately fail requests in domains without decode workers. - Use
`preferred`

during incremental rollouts when same-domain transfer is a latency preference rather than a hard placement requirement. - Transport health is separate from topology selection. Topology-aware routing chooses a better peer, but RDMA, EFA, UCX, or libfabric still need to be configured correctly for NIXL KV transfer.

## Troubleshooting Signals

For the operator field definitions, see the
[KvTransferPolicy API](https://docs.nvidia.com/dynamo/dev/reference/api/kubernetes/full-api-reference#kvtransferpolicy).