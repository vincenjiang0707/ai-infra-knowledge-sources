source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/kubernetes-deployment/deployment-guide/inference-gateway-gaie
lastmod: 2026-09-23T23:30:39.914Z

Inference Gateway (GAIE)


Inference Gateway (GAIE)

## Inference Gateway Setup with Dynamo

Integrate Dynamo with the Gateway API Inference Extension for intelligent KV-aware request routing at the gateway layer.

## Features

-
EPP’s default kv-routing approach is not token-aware because the prompt is not tokenized. But the Dynamo plugin uses a token-aware KV algorithm. It employs the dynamo router which implements kv routing by running your model’s tokenizer inline. The EPP plugin configuration lives in

, following the checked-in GAIE/EPP configuration layout used by this repository.`helm/dynamo-gaie/epp-config-dynamo.yaml`

-
Dynamo Integration with the Inference Gateway supports Aggregated and Disaggregated Serving. A request only exercises disaggregated routing when the EPP config defines a

`prefill`

profile and prefill workers are available. The standalonecurrently only defines a`epp-config-dynamo.yaml`

`decode`

profile, while the recipe examples use separate aggregated and disaggregated configs under`recipes/llama-3-70b/vllm/agg/gaie/`

and`recipes/llama-3-70b/vllm/disagg-single-node/gaie/`

. Unless`DYN_ENFORCE_DISAGG=true`

, deployments without a`prefill`

profile or prefill workers fall back to aggregated serving. -
GAIE integration supports Data Parallelism.

-
If you want to use LoRA deploy Dynamo without the Inference Gateway.

-
Currently, these setups are only tested with the kGateway Inference Gateway.


## Prerequisites

- Kubernetes cluster with kubectl configured
- NVIDIA GPU drivers installed on worker nodes

## Installation Steps

### 1. Install Dynamo Platform

[See Quickstart Guide](https://docs.nvidia.com/dynamo/v1.1.1/getting-started/kubernetes-deployment) to install Dynamo Kubernetes Platform.
If you are installing from the source tree rather than a release chart, follow [Path B: Custom Build from Source](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#path-b-custom-build-from-source) and run `helm dep build ./platform/`

before `helm install`

so the vendored subcharts match the local chart contents.

### 2. Deploy Inference Gateway

First, deploy an inference gateway service. In this example, we’ll install `kgateway`

based gateway implementation.

**Note**: The manifest at `config/manifests/gateway/kgateway/gateway.yaml`

uses `gatewayClassName: agentgateway`

, but kGateway’s helm chart creates a GatewayClass named `kgateway`

. The patch command in the script fixes this mismatch.

#### f. Verify the Gateway is running

### 3. Setup secrets

Do not forget docker registry secret if needed.

Do not forget to include the HuggingFace token.

### 4. Build EPP image (Optional)

You can either use the provided Dynamo FrontEnd image for the EPP image or you need to build your own Dynamo EPP custom image following the steps below.

#### All-in-one Targets

### 5. Deploy

We recommend deploying Inference Gateway’s Endpoint Picker as a Dynamo operator’s managed component. Alternatively, you could deploy it as a standalone pod. Note that when deploying Dynamo with the Inference Gateway Extension each worker must have the FrontEnd as a sidecar.

#### 5.a. Deploy as a DGD component (recommended)

We provide an example for the Qwen vLLM below. You have to deploy the Dynamo Graph and the HttpRoute service. For the HttpRoute service make sure to specify the namespace where your gateway (i.e. kGateway was deployed) as shown below.

Examples for other models can be found in the recipes folder.

We provide examples for llama-3-70b vLLM under the `recipes/llama-3-70b/vllm/agg/gaie/`

for aggregated and `recipes/llama-3-70b/vllm/disagg-single-node/gaie/`

for disaggregated serving.
Note for the aggregated serving you need to disable DYN_ENFORCE_DISAGG in epp config.

Use the proper folder in commands below.

- When using GAIE the FrontEnd does not choose the workers. The routing is determined in the EPP.
- The FrontEnd must run with
`--router-mode direct`

so that it respects the EPP’s routing decisions passed via request headers. - Use the
`frontendSidecar`

field on a worker service to have the operator automatically inject a fully configured frontend sidecar container with all required Dynamo env vars, probes, and ports:

- The pre-selected worker (decode and prefill in case of the disaggregated serving) are passed in the request headers.
- The
`--router-mode direct`

flag ensures the routing respects this selection.

**Startup Probe Timeout:** The EPP has a default startup probe timeout of 30 minutes (10s × 180 failures).
If your model takes longer to load, increase the `failureThreshold`

in the EPP’s `startupProbe`

. For example,
to allow 60 minutes for startup:

**Gateway Namespace**
Note that this assumes your gateway is installed into `NAMESPACE=my-model`

(examples’ default)
If you installed it into a different namespace, you need to adjust the HttpRoute entry in `http-route.yaml`

.

#### 5.b. Deploy as a standalone pod

We do not recommend this method but there are hints on how to do this here.

##### 5.b.1 Deploy Your Model

##### 5.b.2 Install Dynamo GIE helm chart

Create a model configuration file similar to the vllm_agg_qwen.yaml for your model.

By default, the Kubernetes discovery mechanism is used. If you prefer etcd, please use the `--set epp.dynamo.useEtcd=true`

flag below.

Key configurations include:

- An InferenceModel resource for the Qwen model
- A service for the inference gateway
- Required RBAC roles and bindings
- RBAC permissions
- dynamoGraphDeploymentName - the name of the Dynamo Graph where your model is deployed.

**Configuration**
You can configure the plugin by setting environment variables in the EPP component of your DGD in case of the operator-managed installation or in your [values.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/deploy/inference-gateway/standalone/helm/dynamo-gaie/values.yaml).

Common Vars for Routing Configuration:

**Enabling KV-Aware Routing (most precise)**

KV-aware routing uses live KV cache block events from workers so the EPP can route requests to the worker with the best prefix cache overlap. To enable it (default):

**Workers — enable prefix caching and KV event publishing.**Each worker must publish KV cache events to event plane (NATS/ZMQ) so the EPP’s router can track per-worker cache state.**vLLM:**Pass`--enable-prefix-caching`

and`--kv-events-config '{"enable_kv_cache_events":true}'`

.**SGLang:**Pass`--kv-events-config`

with the appropriate endpoint.**TRT-LLM:**Pass`--publish-events-and-metrics`

.

**EPP — leave**The EPP subscribes to worker KV events via event plane (NATS/ZMQ) and uses them for prefix-overlap scoring.`DYN_USE_KV_EVENTS`

at its default (`true`

).**Block size — must be consistent.**The`--block-size`

on all workers must match`DYN_KV_CACHE_BLOCK_SIZE`

on the EPP (default: 128). Mismatched block sizes cause incorrect block hash computation.

**Disabling KV-Aware Routing**

To disable the EPP from listening for KV events (e.g., when prefix caching is off on workers, or for simpler load-balanced routing):

**EPP:**Set`DYN_USE_KV_EVENTS=false`

. The router falls back to approximate mode (routing decisions are tracked locally with TTL decay instead of live KV events from workers).**Workers:**Pass`--no-enable-prefix-caching`

to disable prefix caching entirely. Without prefix caching, no KV events are generated regardless of other flags.**Optionally**set`DYN_OVERLAP_SCORE_WEIGHT=0`

on the EPP to skip prefix-overlap scoring altogether, making the router select workers based on load only.

- Set
`DYN_BUSY_THRESHOLD`

to configure the upper bound on how “full” a worker can be (often derived from kv_active_blocks or other load metrics) before the router skips it. If the selected worker exceeds this value, routing falls back to the next best candidate. By default the value is negative meaning this is not enabled. - Set
`DYN_ENFORCE_DISAGG=true`

(default:`false`

) to control per-request behavior when prefill workers are unavailable:Requests fail with an error if prefill workers are not available. Use this when disaggregated serving is required and aggregated fallback is not acceptable.`true`

(recommended for disaggregated serving):Requests gracefully fall back to aggregated mode (skip prefill, route directly to decode) when prefill workers are not available. When prefill workers appear later, subsequent requests automatically use disaggregated routing.`false`

(default):

- Set
`DYN_OVERLAP_SCORE_WEIGHT`

to weigh how heavily the score uses token overlap (predicted KV cache hits) versus other factors (load, historical hit rate). Higher weight biases toward reusing workers with similar cached prefixes. (default: 1) - Set
`DYN_ROUTER_TEMPERATURE`

to soften or sharpen the selection curve when combining scores. Low temperature makes the router pick the top candidate deterministically; higher temperature lets lower-scoring workers through more often (exploration). `DYN_ROUTER_TEMPERATURE`

— Temperature for worker sampling via softmax (default: 0.0)`DYN_ROUTER_REPLICA_SYNC`

— Enable replica synchronization (default: false)`DYN_ROUTER_TRACK_ACTIVE_BLOCKS`

— Track active blocks (default: true)`DYN_ROUTER_TRACK_OUTPUT_BLOCKS`

— Track output blocks during generation (default: false)- See the
[KV cache routing design](https://docs.nvidia.com/dynamo/v1.1.1/design-docs/component-design/router-design)for details.

Stand-Alone installation only:

- Overwrite the
`DYN_NAMESPACE`

env var if needed to match your model’s dynamo namespace.

**Service Mesh Integration (Istio)**

When running under a service mesh such as Istio, the mesh sidecar proxy may conflict with the EPP’s own TLS serving, causing connection failures (double-TLS). To avoid this, the mesh must be told how to connect to the EPP service via an Istio `DestinationRule`

.

The Dynamo operator can generate this DestinationRule automatically. Enable it by setting the `dynamo.serviceMesh`

parameters when installing or upgrading the Dynamo platform Helm chart:

Or equivalently in a custom values file:

**Helm Parameters**

The Istio CRDs (`networking.istio.io`

) must be installed on the cluster before enabling this feature. The operator detects Istio availability at startup — if the CRDs are not present, DestinationRule reconciliation is skipped even when `serviceMesh.enabled`

is `true`

.

When enabled, the operator produces a `DestinationRule`

for each EPP service equivalent to:

If you are **not** using the Dynamo operator’s Helm chart, you must create this `DestinationRule`

manually for each EPP service. Without it, Istio’s default mTLS policy will conflict with the EPP’s gRPC TLS endpoint.

### 6. Verify Installation

Check that all resources are properly deployed:

Sample output:

### 7. Usage

The Inference Gateway provides HTTP endpoints for model inference.

#### 1: Populate gateway URL for your k8s cluster

a. To test the integration in minikube, proceed as below:
Use minikube tunnel to expose the gateway to the host. This requires `sudo`

access to the host machine. Alternatively, you can use port-forward to expose the gateway to the host as shown in alternative (b).

b. To test on a cluster use commands below:

use port-forward to expose the gateway to the host

#### 2: Check models deployed to inference gateway

a. Query models:

Sample output:

b. Send inference request to gateway:

or

Sample inference output:

* If you have more than one HttpRoute running on the cluster*
Add the host to your HttpRoute.yaml and add the header

`curl -H "Host: llama3-70b-agg.example.com" ...`

or `curl -H "Host: llama3-70b-disagg.example.com" http://localhost:8000/v1/models`

### 8. Deleting the installation

If you need to uninstall run:

## Gateway API Inference Extension Integration

This section documents the updated plugin implementation for Gateway API Inference Extension **v1.5.0-rc.2**.

### Router bookkeeping operations

EPP performs Dynamo router book keeping operations so the FrontEnd’s Router does not have to sync its state.

### Header Routing Hints

Since v1.5.0-rc.1, the EPP uses **headers and body mutations** for communicating routing decisions.
The plugins set HTTP headers for worker targeting and inject pre-computed token IDs
into the request body (`nvext.token_data`

) so the frontend sidecar can skip redundant tokenization.