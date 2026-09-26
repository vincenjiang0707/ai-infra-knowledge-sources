source: https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/vanilla-vllm-onramp
lastmod: 2026-09-25T12:26:00.485Z

# Using GAIE with vanilla vLLM

Add Dynamo’s advanced KV-aware routing to GAIE deployments that use upstream vLLM images.

This on-ramp uses the **experimental standalone mode** of the Dynamo Endpoint Picker Plugin (EPP).
This is a special operator-free integration for existing vanilla vLLM fleets, not the standard
operator-managed Gateway API path. Standalone mode is not available in a published Dynamo release
yet. Use an image built from a Dynamo revision that includes standalone EPP support.

Use this on-ramp to add Dynamo’s advanced KV-aware routing to
[Gateway API Inference Extension (GAIE)](https://github.com/kubernetes-sigs/gateway-api-inference-extension)
deployments that run stock `vllm serve`

workers. **Stock vLLM** means the upstream vLLM container
images. You do not need to replace them with Dynamo vLLM images, install the Dynamo operator, or
migrate the rest of the deployment to Dynamo. The standalone Dynamo Endpoint Picker Plugin (EPP)
adds the routing layer while your Gateway, `HTTPRoute`

, and `InferencePool`

remain standard GAIE
resources and your workers keep running the upstream vLLM images.

The EPP runs the same Dynamo worker selection service used by a full Dynamo deployment. In standalone
mode, it runs in-process without a `DynamoGraphDeployment`

(DGD) or the Dynamo distributed runtime
and event plane.

This is still the **Gateway API routing topology** described in
[KV-Aware Routing on Kubernetes](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/overview). Standalone mode changes who creates the
resources and how the EPP discovers worker state; it does not add a third request-entry topology.

## Architecture

The `InferencePool`

is the source of truth for the worker labels and HTTP port. The EPP watches that
pool and Ready pods in its namespace, subscribes directly to each worker’s KV event socket, and calls
vLLM’s `/v1/chat/completions/render`

endpoint to tokenize each routing request. The Gateway forwards
the original request to the selected pod. The render Service is not a separate renderer workload; it
is a stable Kubernetes Service address for the HTTP endpoint served by the same vLLM pods.

For the operator-managed architecture and generated-resource boundary, see
[Gateway API Routing Architecture](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/gateway-api-routing).

## Before You Begin

You need:

- A Kubernetes cluster with GPU nodes.
`kubectl`

and Helm configured for the cluster.- A Dynamo source checkout.
- A container registry that every cluster node can pull from.
- Two schedulable GPUs for the example’s two vLLM replicas. You can scale the worker Deployment to one replica for a smoke test.

The example serves the public `Qwen/Qwen3-0.6B`

model, which does not require a Hugging Face token.

## Build the EPP Image

Standalone mode is not available in a published Dynamo image yet. From the repository root, build the Rust EPP from the current source revision and push it to your container registry:

## Choose a Deployment Path

Choose the path that matches your starting point:

**Deploy from Scratch**installs the Gateway API layer and applies the complete example, including vLLM workers, the EPP, an`InferencePool`

, and an`HTTPRoute`

.**Use the Dynamo EPP in an Existing GAIE Deployment**keeps your current Gateway,`HTTPRoute`

,`InferencePool`

, and vLLM workers. Deploy a replacement EPP as shown below, or adapt the existing EPP Deployment in place with the same configuration.

Both paths use the same example names so the verification commands apply to either path:

For an existing GAIE deployment, these are example names. Replace them in the commands and YAML snippets with the names of your existing resources.

Set the shared namespace variables:

###### Deploy from Scratch

###### Use the Dynamo EPP in an Existing GAIE Deployment

### Install the Gateway API Layer

Install Gateway API, GAIE, agentgateway, and the Gateway:

The script pins the supported Gateway API, GAIE, and agentgateway versions. It creates the
`inference-gateway`

Gateway in `$AGW_NAMESPACE`

; the `http`

listener allows `HTTPRoute`

resources
from workload namespaces. The on-ramp resources remain in `$NAMESPACE`

.

Verify that the Gateway is programmed:

### Configure Model Access

The public `Qwen/Qwen3-0.6B`

model in the example does not require authentication. To substitute a
gated or private Hugging Face model, create a Secret in the workload namespace before deploying:

Add the Secret reference to the vLLM container in `agg.yaml`

:

### Deploy the On-ramp

The installation script above creates the Gateway API and GAIE layer. The example manifest then
creates the workload layer in `$NAMESPACE`

:

- Two stock vLLM workers with prefix caching, KV events, and readiness probes.
- A
`vllm-qwen-render`

Service that selects those same workers and exposes their HTTP port for`/v1/chat/completions/render`

. - Namespaced read-only RBAC for pods,
`InferencePool`

, and`EndpointSlice`

resources. - Two standalone EPP replicas and their gRPC and replica-synchronization Service.
- An
`InferencePool`

and an`HTTPRoute`

that attaches to the cross-namespace Gateway.

Apply the manifest from the repository root using the image you pushed:

The checked-in manifest is also available as
[ agg.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/deploy/inference-gateway/ext-proc/examples/onramp/agg.yaml).

## Verify the Deployment

These commands apply to both paths because they use the same example names. Wait for the vLLM workers and EPP:

Confirm that the route attached to the intended Gateway:

The output should identify `inference-gateway`

and report `Accepted=True`

and
`ResolvedRefs=True`

.

Find the Service generated for the Gateway and start a port-forward:

In another terminal, send an OpenAI-compatible request:

Inspect the EPP logs near the request:

The logs should show worker discovery and endpoint selection. If the model responds but the EPP logs
show no selection, the route is bypassing the `InferencePool`

.

## EPP Replication

Each EPP replica has an in-process selector and KV index. When `DYN_EPP_PEER_SERVICE`

is set, replicas
watch their own Service’s `EndpointSlice`

resources and discover its named TCP `replica-agg`

port.
They synchronize admission, prefill-complete, and free events so active-load accounting converges
across replicas.

Replica synchronization does not copy the full KV index to a new EPP. A new replica warms its index
from live worker events and optional replay. For consistency details, see
[Standalone Selection Service](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-selection).

For a single EPP replica, set `spec.replicas: 1`

and remove `DYN_EPP_PEER_SERVICE`

, `POD_IP`

, and the
`replica-agg`

Service port.

## Standalone EPP Configuration Reference

## Scope and Limitations

The standalone path currently targets aggregated vLLM serving with data-parallel size 1 per pod. It does not provide the DGD/operator lifecycle, Dynamo runtime discovery, disaggregated prefill/decode orchestration, request migration, topology-aware routing, or full operator-managed observability.

Use [GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo) when you want the supported
operator-managed lifecycle, Dynamo workers, or disaggregated serving. Use
[Gateway API Routing Reference](https://docs.nvidia.com/dynamo/reference/components/gateway-api-routing) for the DGD and
operator-generated resource contract; that contract does not configure standalone mode.

## Troubleshoot

Follow the full request path when debugging:

## Clean Up the From-Scratch Example

If you used the **Deploy from Scratch** path, delete the example resources:

Delete the namespace only if it contains no resources you want to keep: