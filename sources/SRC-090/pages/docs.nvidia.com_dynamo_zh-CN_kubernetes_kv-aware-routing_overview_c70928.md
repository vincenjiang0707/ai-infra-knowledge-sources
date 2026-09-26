source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/kv-aware-routing/overview
lastmod: 2026-09-24T19:58:16.636Z

KV-Aware Routing on Kubernetes


KV-Aware Routing on Kubernetes

Choose where Dynamo makes cache-aware worker-selection decisions in a Kubernetes deployment.

Dynamo supports two KV-aware request-routing topologies on Kubernetes. They use the same routing concepts but place worker selection in different components. Choose based on how your platform accepts and governs traffic, not because one topology uses a different KV-routing algorithm.

## Recommendation

Use **Dynamo Frontend routing** unless your platform already needs Kubernetes Gateway API. It has
fewer components, requires no Gateway API installation, and works with a standard
`DynamoGraphDeployment`

.

Use **Gateway API routing** when the Gateway must own the external request path—for example, when a
platform team standardizes ingress, authentication, rate limiting, traffic policy, or gateway-level
telemetry through Gateway API.

The Frontend and GAIE topologies are alternatives for a request path. Do not configure the Frontend to select a worker after the EPP has already selected one.

## Dynamo Frontend Routing

The Dynamo Frontend receives the client request, tokenizes it, scores eligible workers, and forwards the request to the selected worker. Router flags and environment variables belong on the Frontend component.

Choose this topology when:

- Each deployment can expose its own Frontend Service.
- You do not need Gateway API policy in the request path.
- You want the fewest routing components to install and operate.
- Dynamo should own both HTTP request handling and worker selection.

This topology works out of the box with the normal Dynamo platform; no Gateway API components are
required. Use [the Dynamo Frontend](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-the-dynamo-frontend) to enable KV-aware worker
selection in a DGD.

## GAIE Routing

Gateway API routing separates traffic entry from worker selection. A Kubernetes `Gateway`

receives
the request and asks the Dynamo Endpoint Picker Plugin (EPP) to select an endpoint before forwarding
the request to a worker pod.

Choose this topology when:

- Your organization already uses Gateway API as the standard ingress layer.
- Authentication, authorization, rate limiting, traffic policy, or telemetry belongs at the Gateway.
- Multiple model routes should share a platform-managed address and listener.
- A platform team manages the Gateway while an application team manages the DGD and
`HTTPRoute`

.

Gateway API routing requires a separate installation. See
[Install Gateway API Inference Extension](https://docs.nvidia.com/dynamo/kubernetes/installation/gateway-api-inference-extension), then
[GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo) or [GAIE with vanilla vLLM](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/vanilla-vllm-onramp).

## What Is the Dynamo EPP?

The Dynamo **Endpoint Picker Plugin (EPP)** is a service that implements the GAIE endpoint-selection
protocol. The Gateway calls it before forwarding an inference request. The EPP tokenizes the request,
reads Dynamo worker and KV cache state, scores eligible endpoints, and returns the selected worker to
the Gateway.

The EPP is not a public inference endpoint and does not run the model. The Dynamo operator deploys it
when a DGD contains a component with `type: epp`

. In this topology, worker Frontend sidecars run with
`--router-mode direct`

because the EPP has already made the routing decision.

For the full request and state flow, see
[Gateway API Routing Architecture](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/gateway-api-routing).

## Shared Routing Behavior

Both topologies can use worker-published KV cache events to account for prefix overlap and active load. Both can also operate with predicted state when precise KV events are unavailable. The selection algorithm and tuning concepts are shared; only the component hosting them changes.

For the cost model, see [Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts). For shared tuning
guidance, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).