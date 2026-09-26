source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/quickstart
lastmod: 2026-09-24T19:58:16.636Z

# GAIE Quickstart

This quickstart deploys a Dynamo operator-managed serving graph behind Gateway API. The `Gateway`

receives requests, GAIE calls the Dynamo EPP for endpoint selection, and the selected worker’s
Frontend sidecar forwards the request in direct mode.

## What This Deploys

## Prerequisites

- Kubernetes cluster with GPU nodes.
`kubectl`

, Helm, and`jq`

.- Access to
`nvcr.io/nvidia/ai-dynamo`

images for the Dynamo release you use. - Hugging Face access to
`Qwen/Qwen3-0.6B`

. - Shared RWX storage for the recipe’s
`model-cache`

PVC.

Set the common variables:

Clone the Dynamo source tree that contains the recipe manifests used below:

## Install Dynamo Platform

Install the Dynamo platform and operator with the [Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide).
Use the same Dynamo release line for the platform chart, EPP image, and runtime images.

After installation, verify that the Helm release exists in the platform namespace:

## Create Model Credentials

Create model credentials if the model requires them. This is a Dynamo model-serving prerequisite,
not a GAIE-specific resource. The general Kubernetes quickstart explains the
[Hugging Face token secret](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart#huggingface-token-secret) pattern.

## Install Gateway API and GAIE CRDs

Install the Gateway API layer explicitly. If your platform team already installed Gateway API, GAIE,
and a compatible Gateway implementation, skip to [Create the Gateway](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/quickstart#create-the-gateway).

## Create the Gateway

Choose the Gateway implementation for this namespace.

###### agentgateway

###### Istio

Create the `AgentgatewayParameters`

resource in the model namespace. The parameters resource
excludes Istio sidecar injection from `agentgateway-proxy`

pods when the namespace has
`istio-injection=enabled`

.

Create the `Gateway`

that uses those parameters.

Wait for the gateway controller to program the gateway.

Keeping the `Gateway`

and `HTTPRoute`

in the same namespace avoids a cross-namespace
`parentRefs[].namespace`

field in the route.

## Prepare the Model Cache

The Qwen recipe mounts a shared `model-cache`

PVC. Edit
`recipes/qwen3-0.6b/model-cache/model-cache.yaml`

first and set `storageClassName`

to a RWX storage
class available in your cluster. For the general pattern, see [Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching).

## Deploy the Serving Graph

Deploy the Qwen 0.6B aggregated recipe and its route:

Wait for the operator-created resources:

## Verify End-to-End

Use one access mode to set `GATEWAY_URL`

, then send a request through the Gateway and EPP. Keep
`ROUTE_MODEL`

set to the model name from the route manifest you applied.

###### Port-forward

###### LoadBalancer or tunnel

In another terminal:

Finish by checking that the EPP path handled the request. A successful smoke test should show the EPP receiving endpoint-picker traffic and selecting a worker near the time of your request; that proves the request flowed through Gateway API and the Dynamo EPP before it reached the Frontend sidecar.

If the log output is quiet, run the chat request again while tailing the EPP logs in another terminal.

## Troubleshooting

###### agentgateway

###### Istio

If requests return HTTP 500 and the namespace has `istio-injection=enabled`

, verify the
`agentgateway-proxy`

pod does not have an `istio-proxy`

sidecar:

See [GAIE Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/reference#agentgateway-and-istio-injection) for the sidecar
injection contract.

If model pods restart while loading, inspect the pod events. When events show startup probe failures
and the model load time is expected, increase `startupProbe.failureThreshold`

on the affected DGD
component. This is general Kubernetes probe tuning, not a GAIE-specific setting.

## Clean Up

If this namespace is only for the quickstart, delete it: