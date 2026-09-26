source: https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo
lastmod: 2026-09-25T12:26:00.485Z

# Using GAIE with Dynamo

This how-to places a Kubernetes Gateway in front of an existing `DynamoGraphDeployment`

(DGD). The
Gateway API Inference Extension (GAIE) calls the Dynamo Endpoint Picker Plugin (EPP), and the Gateway
forwards each request to the worker selected by the EPP.

Use this topology when Gateway API should own traffic entry, policy, and gateway-level observability.
For direct-to-Frontend routing, use [the Dynamo Frontend](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-the-dynamo-frontend).

## Before You Begin

You need:

- A working DGD whose workers can serve requests.
- The Dynamo operator installed.
- Gateway API, GAIE, and a compatible Gateway implementation installed. See
[Install Gateway API Inference Extension](https://docs.nvidia.com/dynamo/kubernetes/installation/gateway-api-inference-extension). - A
`Gateway`

named`inference-gateway`

in the DGD namespace.

This page modifies an existing DGD named `qwen`

that serves `Qwen/Qwen3-0.6B`

. Keep your existing
model credentials, storage, worker images, and backend settings when adapting the example.

### Set the deployment variables

Set the namespace, resource names, model, and local filenames used throughout the procedure:

Copy your working DGD manifest to `$DGD_MANIFEST`

, then make the changes in the next three steps.

### Add the EPP component

Add one component with `type: epp`

to `qwen-gateway.yaml`

. The EPP configuration below selects
aggregated or decode workers and scores them with the Dynamo decode scorer.

If your deployment uses another Dynamo version, model, secret name, or backend block size, update those values in the manifest. Keep the platform, EPP, Frontend sidecars, and workers on the same Dynamo release line. The EPP block size must match the backend block size.

For a disaggregated graph, add separate prefill and decode filters, scorers, and scheduling profiles.
Start from the repository’s
[disaggregated GAIE example](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/vllm/deploy/gaie/disagg.yaml)
instead of extending the aggregated profile by hand.

### Put worker sidecars in direct mode

The EPP selects the worker before the request reaches its pod. In each routable worker component, add a Frontend sidecar and run it in direct mode so it forwards the request without making another worker selection.

Keep the existing worker container in the component. If your worker uses another runtime image or credential source, apply the equivalent values to the sidecar.

### Publish KV cache events

To route from actual cache contents, enable prefix caching and KV event publication in each routable
worker. For the vLLM worker in `qwen-gateway.yaml`

, include settings equivalent to:

The operator-managed EPP receives these events through the Dynamo event plane. Do not configure a direct EPP-to-vLLM ZMQ subscription for this topology.

### Apply the updated DGD

Apply `qwen-gateway.yaml`

, wait for the DGD, and inspect the generated `qwen-pool`

`InferencePool`

:

The operator also creates the EPP Deployment and Service.

## Troubleshoot the Route

If the request does not reach a worker, set the resource variables and inspect the request path in order:

- If the DGD is rejected because the
`InferencePool`

API is unavailable, install GAIE before applying a DGD with an EPP component. - If the Gateway returns HTTP 500 in an Istio-injected namespace, verify that the Gateway proxy does
not have an
`istio-proxy`

sidecar. See[agentgateway and Istio injection](https://docs.nvidia.com/dynamo/reference/components/gateway-api-routing#agentgateway-and-istio-injection). - If routing ignores expected prefix overlap, verify that workers publish KV events and that
`DYN_KV_CACHE_BLOCK_SIZE`

matches the backend block size.

For resource fields, runtime settings, request headers, and service-mesh behavior, see the
[Gateway API Routing Reference](https://docs.nvidia.com/dynamo/reference/components/gateway-api-routing).