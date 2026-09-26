source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/overview
lastmod: 2026-09-24T19:58:16.636Z

Gateway API Inference Extension (GAIE)


Gateway API Inference Extension (GAIE)

Dynamo supports two request routing topologies on Kubernetes:

**Dynamo-native Frontend routing.**The Dynamo Frontend receives HTTP requests and the integrated Dynamo Router selects workers.**Gateway API routing with GAIE.**A Kubernetes`Gateway`

receives HTTP requests, the[Gateway API Inference Extension (GAIE)](https://github.com/kubernetes-sigs/gateway-api-inference-extension)calls the Dynamo Endpoint Picker Plugin (EPP) for endpoint selection, and the selected worker’s Frontend sidecar forwards the request in direct mode.

This guide covers the Gateway API path for `DynamoGraphDeployment`

resources managed by the Dynamo
operator. Use it when your Kubernetes platform wants Gateway API to own traffic entry, policy, and
observability while Dynamo owns the serving graph, discovery, event plane, and routing logic inside
the EPP.

## Components

The operator-managed GAIE path combines user-created Gateway API objects with resources created
from the `DynamoGraphDeployment`

.

## Request Flow

Gateway API owns the external request path. Dynamo still owns the serving graph: the operator
creates the EPP Service, worker pods, Frontend sidecars, and `InferencePool`

that binds the route to
the EPP. The EPP receives Dynamo routing state from the runtime event plane and returns the selected
worker ID to the gateway. The gateway forwards the request to the selected worker’s Frontend sidecar,
which runs in direct routing mode.

In this operator-managed path, the EPP consumes live routing state through the Dynamo event plane using NATS Core. Direct vLLM ZMQ KV-event subscriptions are used by other integration shapes, but not by this quickstart path.

## Shared Prerequisites

- A Kubernetes cluster with GPU nodes. For the baseline Gateway API environment, start with the
upstream
[Gateway API getting started guide](https://gateway-api.sigs.k8s.io/guides/getting-started/introduction/)and the upstream[GAIE introduction](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/site-src/index.md). `kubectl`

,[Helm](https://helm.sh/docs/intro/install/), and[jq](https://jqlang.org/download/)configured for the cluster.- Gateway API and GAIE CRDs installed. The quickstart installs them explicitly from pinned upstream release manifests.
- A Gateway API implementation that supports GAIE
`InferencePool`

resources and`endpointPickerRef`

calls. - Dynamo platform installed with the operator. See the
[Kubernetes Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart)and[Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide). - Model credentials and storage needed by the selected model. Hugging Face token secrets are a
Dynamo model-serving prerequisite, not a GAIE-specific resource; see the
[Hugging Face token secret](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart#huggingface-token-secret)setup.

## Gateway Implementation

GAIE requires a Gateway API implementation that can call an Endpoint Picker Plugin before forwarding
the request to a backend. Dynamo is independent of the Gateway implementation: pick the gateway that
matches your platform, then point its `HTTPRoute`

and generated `InferencePool`

at the Dynamo EPP.

The quickstart shows two verified paths: agentgateway and Istio. Other Gateway API
implementations might work when they support the same GAIE `InferencePool`

and `endpointPickerRef`

EPP path; check the upstream
[GAIE gateway implementation list](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/site-src/implementations/gateways.md)
and your controller’s documentation before choosing another implementation.

Istio uses Envoy in its data plane. agentgateway is a Rust-based AI gateway. The requirement for this guide is not Envoy specifically; it is support for Gateway API plus the GAIE EndpointPicker flow.

###### agentgateway

###### Istio

Use agentgateway for a small Gateway API footprint or when the cluster does not already
standardize on a service mesh. Install the agentgateway chart with
`inferenceExtension.enabled=true`

; the GatewayClass is `agentgateway`

.

The quickstart walks through the two verified implementation paths shown in this table:

## Gateway API Concepts

`HTTPRoute.spec.parentRefs`

attaches a route to a `Gateway`

. If the `HTTPRoute`

and `Gateway`

live
in different namespaces, set `parentRefs[].namespace`

to the Gateway namespace. `rules[].backendRefs`

points at the `InferencePool`

; the pool points at the EPP service through `endpointPickerRef`

.

For the upstream API model, see the
[Gateway API HTTP routing guide](https://gateway-api.sigs.k8s.io/guides/user-guides/http-routing/) and the
[cross-namespace routing guide](https://gateway-api.sigs.k8s.io/guides/user-guides/multiple-ns/).

## Configure DynamoGraphDeployments for GAIE

In GAIE mode, the EPP chooses workers. The worker Frontend sidecar must run in direct routing mode so it honors the EPP selection instead of choosing a worker again.

The EPP component is part of the `DynamoGraphDeployment`

. The operator creates the EPP Service and
the matching `InferencePool`

, so users apply the DGD and the route instead of hand-crafting the pool.

### EPP Component Configuration

Start from the recipe EPP component and update the `DynamoGraphDeployment`

for your cluster. Change
deployment-level settings such as replicas and resources to fit gateway traffic volume. Change
routing plugin settings only when you want different endpoint-selection behavior, then validate the
result with production-like traffic.

For upstream Endpoint Picker Plugin (EPP) semantics, see the GAIE
[Implementer’s Guide](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/main/site-src/guides/implementers.md)
and the
[Endpoint Picker Protocol specification](https://github.com/kubernetes-sigs/gateway-api-inference-extension/tree/main/docs/proposals/004-endpoint-picker-protocol).
For label-based endpoint selection, see the upstream
[InferencePool configuration guide](https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/#how-to-configure-an-inferencepool).
The `label-filter`

plugin shown here is Dynamo-specific; the component role label comes from the
Dynamo [ComponentType](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s#componenttype) field.

The operator reconciles the EPP `Deployment`

, EPP `Service`

, and generated `InferencePool`

from the
DGD. Tune the DGD first; patch generated resources only for short-lived debugging.

The `DYN_*`

environment values are runtime contracts between the EPP router logic and the workers.
Update them when the worker backend changes; do not use them to tune scoring.

See the complete EPP examples in the source tree:
`recipes/qwen3-0.6b/vllm/agg/gaie/deploy.yaml`

for the Qwen 0.6B aggregated recipe manifest and
`examples/backends/vllm/deploy/gaie/disagg.yaml`

for the Qwen 0.6B disaggregated example manifest.

## Routing Behavior

GAIE does not require one scoring strategy. Choose the routing behavior based on the routing state available to the EPP.

With operator-managed GAIE, NATS Core backs live routing-state delivery. After a restart, the EPP rebuilds prefix state from worker-local indexers and then consumes subsequent updates through the Dynamo event plane.

## Compatibility and Defaults

The quickstart pins the Gateway API layer so manual setup is repeatable. Keep the Dynamo platform, EPP, and runtime images on the same Dynamo release line.

## Troubleshooting Signals

## Next Step

Run the [GAIE Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/quickstart) to deploy a `DynamoGraphDeployment`

, expose it through
Gateway API, and verify an end-to-end request through the Dynamo EPP.

Use [GAIE Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/reference) for resource contracts, routing knobs, and service mesh
settings.