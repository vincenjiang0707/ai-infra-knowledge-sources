source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/reference
lastmod: 2026-09-23T23:30:39.914Z

# GAIE Reference

Use this reference after the [GAIE Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/quickstart) when you need to inspect generated
resources, tune routing behavior, or adapt the Gateway API path to a cluster policy.

This page is user-facing runtime reference. It does not cover building custom EPP images, local development loops, minikube-specific setup, or full uninstall procedures.

## Resource Contract

Operator-managed GAIE connects Gateway API resources to the Dynamo serving graph through an
operator-generated `InferencePool`

.

The Dynamo operator creates the `InferencePool`

for a `DynamoGraphDeployment`

that contains an EPP
component. The pool name is `<dgd-name>-pool`

, it lives in the DGD namespace, and its
`endpointPickerRef`

points to the generated EPP `Service`

.

The generated selector matches worker pods by Dynamo labels:

Do not hand-edit the generated `InferencePool`

unless you also keep its selector aligned with the
operator’s worker-pod labels. If the pool selector and Dynamo discovery disagree, the EPP can select
a worker that the gateway data plane refuses to forward to.

For the upstream Gateway API model, see the
[HTTP routing guide](https://gateway-api.sigs.k8s.io/guides/user-guides/http-routing/) and
[cross-namespace routing guide](https://gateway-api.sigs.k8s.io/guides/user-guides/multiple-ns/).

## Request Contract

With GAIE, worker selection happens in the EPP before the request reaches the worker sidecar. The sidecar must run in direct mode so it honors the EPP decision instead of routing again.

The EPP sends routing decisions to the selected sidecar through request headers.

For body-bearing OpenAI requests, the EPP also tokenizes the request and injects token data into the request body so the sidecar can avoid repeating the same tokenization work.

## Routing Modes

The same Dynamo router logic can run behind the Dynamo-native Frontend entry path or inside the GAIE EPP. In the Gateway API path, the EPP owns endpoint selection and the worker sidecar owns request forwarding.

In the operator-managed GAIE path, KV events reach the EPP through the Dynamo event plane using
NATS Core. vLLM can also publish KV events through ZMQ in other integration shapes; the
operator-managed `DynamoGraphDeployment`

path does not use ZMQ for the EPP.

To use KV cache aware routing:

- Enable worker prefix caching and KV event publishing for your backend.
- Keep EPP KV events enabled.
- Keep the worker KV block size aligned with the EPP block size.

Backend examples:

Set `DYN_KV_CACHE_BLOCK_SIZE`

on the EPP only when discovery does not already provide the backend’s
block size. It must match the workers’ `--block-size`

. A mismatch changes the block hashes used for
prefix overlap and produces incorrect routing scores.

To use approximate routing, disable worker KV events and set the EPP to predicted local state:

## Router Tuning

Set these values on the EPP component unless the deployment manifest says otherwise.

For the broader router configuration surface, see
[Router Configuration](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning).

## Service Mesh Integration

The EPP serves gRPC on port `9002`

. When an Istio sidecar mediates traffic from the gateway proxy to
the EPP service, configure mesh TLS explicitly so the proxy connects to the EPP’s serving mode.

Enable operator-managed Istio `DestinationRule`

generation when installing or upgrading the Dynamo
platform chart:

The platform values are:

When enabled and Istio CRDs are installed, the operator creates a `DestinationRule`

for each EPP
service:

If you install without the Dynamo operator Helm chart or leave `dynamo.serviceMesh.enabled=false`

,
create an equivalent `DestinationRule`

for each EPP service used through Istio.

## agentgateway and Istio Injection

When namespace-level Istio injection is enabled, the `agentgateway-proxy`

pod can receive an Istio
sidecar. That sidecar can intercept the ext_proc gRPC connection from agentgateway to the EPP and
cause HTTP 500 responses from the gateway.

Use a per-Gateway `AgentgatewayParameters`

resource in the same namespace as the `Gateway`

:

Reference that parameters resource from the `Gateway`

:

Verify that the proxy pod does not contain `istio-proxy`

:

Patch the default `AgentgatewayParameters`

resource in `agentgateway-system`

only as a
cluster-wide policy decision. Gateways without `spec.infrastructure.parametersRef`

inherit that
default.

## Developer References

Image build commands belong with the component source, not in this user reference. Use this source location when developing or replacing the standard EPP image: