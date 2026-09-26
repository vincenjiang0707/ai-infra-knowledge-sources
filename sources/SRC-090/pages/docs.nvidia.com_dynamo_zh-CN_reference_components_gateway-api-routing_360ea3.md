source: https://docs.nvidia.com/dynamo/zh-CN/reference/components/gateway-api-routing
lastmod: 2026-09-23T23:30:39.914Z

# Gateway API Routing Reference

Use this reference for a `DynamoGraphDeployment`

(DGD) that routes requests through the Gateway API
Inference Extension (GAIE) and the Dynamo Endpoint Picker Plugin (EPP). For the procedure, see
[Using GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo). For architecture, see
[Gateway API Routing Architecture](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/gateway-api-routing).

## DGD EPP Fields

The EPP is a DGD component with `type: epp`

. The Dynamo operator creates the EPP workload, Service,
configuration, and `InferencePool`

from these fields.

Set to `epp`

for the Endpoint Picker Plugin component. A DGD can contain at most one EPP component.

Number of EPP pods. Increase this value when endpoint-picker request volume requires more EPP capacity.

EPP configuration source. Set exactly one of `config`

or `configMapRef`

.

Inline endpoint-picker configuration. The operator serializes the object into a generated `ConfigMap`

.
Mutually exclusive with `configMapRef`

.

Reference to a user-managed `ConfigMap`

containing an `EndpointPickerConfig`

. Mutually exclusive with
`config`

.

Name of the Frontend container in each routable worker pod. The named container must exist in
`podTemplate.spec.containers`

and run with `--router-mode direct`

.

For the complete component schema, see the
[DynamoComponentDeployment Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment).

## EndpointPickerConfig Fields

Plugin instances available to scheduling profiles. A plugin can filter endpoints, score endpoints, choose a result, or establish aggregated and disaggregated profiles.

Local name used by `schedulingProfiles[].plugins[].pluginRef`

. Omit only for a plugin that does not
need to be referenced directly, such as `disagg-profile-handler`

.

Plugin implementation.

Common Dynamo values: disagg-profile-handler label-filter dyn-prefill-scorer dyn-decode-scorer max-score-pickerPlugin-specific configuration. The operator preserves this object without pruning unknown fields.

Ordered plugin chains for endpoint selection. Aggregated deployments use a `decode`

profile.
Disaggregated deployments use both `prefill`

and `decode`

profiles.

Worker role handled by the profile.

Dynamo values: prefill decodePlugins applied by the profile.

Name of a plugin declared in the top-level `plugins`

list.

Relative influence of the plugin in the scheduling profile. Keep required filters and the final picker enabled. Validate scorer-weight changes with production-like traffic.

## Dynamo Plugin Parameters

### Label Filter

Pod label used to identify eligible workers. For DGD v1beta1 components, use
`nvidia.com/dynamo-component-type`

.

Accepted values for the selected label. Use `prefill`

or `decode`

to separate worker roles.

Whether pods without the selected label remain eligible. Aggregated profiles can set this to `true`

when worker pods do not carry a separate decode role. Disaggregated profiles should use `false`

.

## EPP Runtime Environment

Set these values on the EPP component’s `main`

container. Shared KV router settings use the same
semantics as Frontend-hosted routing; this section identifies the settings most relevant to the
Gateway topology.

Model identifier used to load tokenizer and model configuration. Set it when discovery does not provide the model name. It must match the model served by the workers.

Backend KV cache block size. Set it when discovery does not provide the value. It must match the worker backend’s block size; a mismatch changes prefix block hashes and produces incorrect overlap scores.

Enables worker-published KV event consumption in the EPP router. When `false`

, the router relies on
predicted local state instead of precise worker cache events.

Credit applied to device-local prompt-prefix overlap. Higher values prefer workers that already hold
more of the prompt prefix. Set to `0`

to remove device-local cache overlap from endpoint scoring.

Reduces overlap credit as active prefill load rises above the least-loaded eligible worker. `0`

disables decay.

Scales prompt-side prefill load after cache-hit credits are applied.

Adds block-equivalent routing cost for each active request on a candidate worker. Tune this value only when decode step latency depends materially on active batch size.

Controls worker exploration through normalized softmax sampling. `0`

selects deterministically.

Publishes and consumes best-effort active-sequence state across EPP replicas through the Dynamo event plane.

Includes blocks used by active generation in worker load accounting.

Predicts output blocks during generation and decays them as requests make progress.

Includes active prompt-side prefill tokens in worker load accounting.

For the full shared configuration surface and tuning guidance, see
[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).

## Generated Resource Contract

For a DGD named `<dgd-name>`

, the operator generates an `InferencePool`

named `<dgd-name>-pool`

in
the DGD namespace. Its `endpointPickerRef`

points to the generated EPP Service on gRPC port `9002`

,
and its target port points to worker Frontend sidecars on port `8000`

.

Treat the generated `InferencePool`

, EPP Service, Deployment, and inline configuration `ConfigMap`

as
operator-owned resources. Make persistent changes in the DGD.

## HTTPRoute Contract

Gateway that receives model traffic. The Gateway and route can be in different namespaces only when the Gateway listener allows the route namespace.

Reference to the operator-generated `InferencePool`

.

Set to `inference.networking.k8s.io`

.

Set to `InferencePool`

.

Generated pool name, normally `<dgd-name>-pool`

.

Worker Frontend target port. The operator-generated pool uses `8000`

.

## Request Mutation Contract

The EPP returns the selected endpoint and routing metadata to the Gateway. The Gateway forwards the mutated request to the selected Frontend sidecar.

Aggregated or decode worker selected for the request.

Data-parallel rank selected for the aggregated or decode worker.

Routing topology selected for the request.

Values: aggregated disaggregatedPrefill worker selected for a disaggregated request.

Data-parallel rank selected for the prefill worker.

For supported body-bearing OpenAI requests, the EPP can inject precomputed token data into
`nvext.token_data`

so the Frontend sidecar does not repeat tokenization.

## Service Mesh Configuration

Generates service-mesh resources for EPP Services when the provider CRDs are installed.

Service-mesh provider. Only Istio is supported.

Value: istioTLS mode in generated Istio `DestinationRule`

resources.

Skips server certificate verification for the EPP’s self-signed serving certificate.

Client certificate path for `MUTUAL`

TLS mode.

Client private-key path for `MUTUAL`

TLS mode.

Certificate authority path for `MUTUAL`

TLS mode.

When service-mesh integration is enabled, the operator creates a `DestinationRule`

for each EPP
Service. If the operator does not manage the mesh integration, create an equivalent rule so the
Gateway proxy can connect to EPP gRPC port `9002`

.

## agentgateway and Istio Injection

When namespace-level Istio injection is enabled, an injected `istio-proxy`

in an agentgateway data
plane pod can intercept the EPP external-processing gRPC connection and cause HTTP 500 responses.
Use an `AgentgatewayParameters`

resource in the same namespace as the `Gateway`

:

Reference it from the Gateway:

`AgentgatewayParameters`

is a local reference and must be in the Gateway namespace. Use a
per-Gateway resource unless disabling injection is an intentional cluster-wide policy.