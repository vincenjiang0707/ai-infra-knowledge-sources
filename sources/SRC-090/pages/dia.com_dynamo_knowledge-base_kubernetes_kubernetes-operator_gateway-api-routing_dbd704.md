source: https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/gateway-api-routing
lastmod: 2026-09-24T19:58:16.636Z

# Gateway API Routing Architecture

How Gateway API, the Dynamo Endpoint Picker Plugin, and worker Frontend sidecars divide request-routing responsibilities.

Gateway API routing moves worker selection out of the public-facing Dynamo Frontend and into a Dynamo Endpoint Picker Plugin (EPP). Kubernetes Gateway API owns traffic entry and route matching; Dynamo continues to own the serving graph, worker discovery, KV cache state, and endpoint scoring.

For the task-oriented setup, see [Using GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo).

## Component Responsibilities

The operator generates the EPP Deployment and Service and the `InferencePool`

from the
`DynamoGraphDeployment`

. Users create the `Gateway`

, `HTTPRoute`

, and DGD.

## Request Flow

The Frontend sidecar runs with `--router-mode direct`

. Running it in `kv`

mode would introduce a
second worker-selection decision after the EPP has already selected an endpoint.

## Routing-State Flow

In the operator-managed topology, the EPP receives worker state through the Dynamo event plane using NATS Core. A direct vLLM ZMQ subscription is a different integration shape and is not part of this request path.

The EPP can route with two levels of state:

**KV cache aware:**worker-published events identify cached prompt blocks and active sequences.**Approximate:**tokenized requests and local lifecycle bookkeeping predict state when worker KV events are unavailable or disabled.

Both modes also account for endpoint readiness and load. KV events improve the accuracy of prefix locality decisions; they do not replace health and eligibility filters.

## Operator Reconciliation Boundary

A DGD with an EPP component causes the operator to reconcile:

- An EPP configuration
`ConfigMap`

when inline configuration is used. - An EPP Deployment and Service.
- An
`InferencePool`

that selects Dynamo worker pods and points its`endpointPickerRef`

to the EPP Service on gRPC port`9002`

. - Frontend sidecar defaults and worker labels used by the Gateway and EPP.

Generated resources are implementation details of the DGD. Persistent changes belong in the DGD,
not in manual patches to the generated `InferencePool`

, Service, or Deployment.

## Gateway Independence

Dynamo does not require a specific data-plane implementation. The Gateway implementation must:

- Support Gateway API and GAIE
`InferencePool`

resources. - Call the
`endpointPickerRef`

before forwarding a request. - Forward the request to the endpoint selected by the EPP.
- Preserve the routing metadata and body mutation returned by the EPP.

agentgateway and Istio are the documented integrations. Other implementations can work when they honor the same GAIE endpoint-picker contract.

## Failure Boundaries

The topology introduces distinct readiness boundaries:

- A Gateway can be programmed while the
`HTTPRoute`

is unresolved. - An
`HTTPRoute`

can be accepted while its generated`InferencePool`

has no ready endpoints. - The EPP can be running but not ready while it waits for eligible workers.
- Workers can be ready for inference but unroutable when their labels do not match EPP filters or the
`InferencePool`

selector. - Service-mesh policy can allow client-to-Gateway traffic while blocking Gateway-to-EPP gRPC traffic.

Troubleshooting should follow the request path in that order rather than treating Gateway API routing as one process.

For field and environment-variable contracts, see the
[Gateway API Routing Reference](https://docs.nvidia.com/dynamo/reference/components/gateway-api-routing).