source: https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/dgdr-reference
lastmod: 2026-09-24T19:58:16.636Z

# DGDR Reference

A `DynamoGraphDeploymentRequest`

(DGDR) is Dynamo’s deploy-by-intent generator
for [ DynamoGraphDeployment](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/api-reference-k-8-s#dynamographdeployment) (DGD)
resources. You describe what you want to run and your performance targets; the
profiler determines a configuration and produces the DGD that serves traffic.

For the full deployment mental model — including DGD, DCD, DGDR, recipes,
strategy selection, model caching, planner setup, and common pitfalls — see the
[Deployment Overview](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/model-deployment-guide).

## DGDR, DGD, and Recipes

Dynamo provides two Custom Resources for deploying inference graphs:

Use DGD directly when you have a hand-crafted configuration for a specific
model/hardware combination. Most
[recipes](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/recipes) are tuned DGD
manifests. Use DGDR when you want Dynamo to generate the DGD for you.

For DGD deployment details, see [Creating Deployments](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/creating-deployments).

## Spec Reference

### Minimal Example

### Field Reference

For the complete CRD spec, see the [API Reference](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/api-reference-k-8-s).

DGDR does not currently expose a `features.kvRouter`

field. To configure
router mode or KV-aware routing details, use a direct DGD, a tuned recipe, or
`overrides.dgd`

when you still want DGDR to generate the base deployment.

### Generated DGD Overrides

Use `spec.overrides.dgd`

when the generated `DynamoGraphDeployment`

needs a
field that DGDR does not expose directly. The value is a partial
`nvidia.com/v1alpha1`

DGD object that is merged into the profiler-generated
deployment after Dynamo selects a configuration.

For example, to inject an environment variable into every generated service:

Use `spec.envs`

for variables that should apply to all generated services. To
target a single service, override that service’s `envs`

entry instead:

`overrides.profilingJob`

only customizes the profiling Job. Use
`overrides.dgd`

for settings that must appear on the deployed worker pods.

### Routing

DGDR-generated deployments include a standalone `Frontend`

service. That
frontend runs Dynamo’s embedded router and defaults to `round-robin`

routing,
which is often not optimal. Because DGDR does not yet expose a first-class
router feature, configure the generated frontend with `spec.overrides.dgd`

.

For the full router mode and environment variable reference, see
[Router Guide](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/kv-cache-aware-routing) and
[Router Configuration](https://docs.nvidia.com/dynamo/v1.2.1/components/router/configuration-and-tuning).

For example, enable KV-aware routing on the generated frontend:

Use the same `Frontend`

override for other frontend router modes, such as
`random`

, `least-loaded`

, or `device-aware-weighted`

. For normal DGDR
deployments, use `kv`

when you want prefix-cache-aware routing and
`round-robin`

or `least-loaded`

when you only want load balancing. Use
`direct`

only when an external router supplies explicit worker IDs in the
request routing hints. For detailed mode definitions, see
[Router Guide](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/kv-cache-aware-routing#routing-modes-router-mode).

KV-aware routing can use event-driven prefix-cache state or approximate
prefix matching. The frontend still runs in `kv`

mode in both cases. If you
do not configure worker KV-event publication, set
`DYN_ROUTER_USE_KV_EVENTS=false`

to use approximate KV mode:

For event-driven prefix-cache state, enable worker event publication only
where prefill happens: the single worker in aggregated serving, or prefill
workers in disaggregated serving. Decode workers are scored by load
(`dyn-decode-scorer`

), not prefix overlap (`dyn-prefill-scorer`

), so vLLM
decode workers omit both `--enable-prefix-caching`

and `--kv-events-config`

.
Service names depend on the selected backend and topology, so inspect the
generated DGD first, especially when `autoApply: false`

.

For example, a generated vLLM disaggregated deployment may contain a
`VllmPrefillWorker`

service. This override appends the vLLM KV-event publishing
arguments to that service while enabling the frontend KV router:

Worker KV-event flags are backend-specific. For cross-backend behavior, see
[Router Operations](https://docs.nvidia.com/dynamo/v1.2.1/components/router/router-operations#additional-notes).

In Kubernetes deployments the Dynamo runtime normally uses Kubernetes
discovery and the NATS event plane. Some backends, such as vLLM and SGLang,
emit raw KV events over ZMQ; the Dynamo worker consumes those backend events
and republishes router events through the Dynamo event plane. For the event
plane model, see [Event Plane](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/communication-planes/event-plane).

### EPP and Gateway Routing

EPP/Gateway routing is a different topology from the standalone frontend that DGDR generates:

In this mode the EPP owns worker selection. The worker-local frontend sidecar
must run with `--router-mode direct`

so it honors the worker IDs selected by
EPP. In the normal Gateway path, the selected endpoint and the frontend sidecar
are the same worker pod; if they differ, direct mode can still forward to the
worker ID supplied by EPP.

DGDR does not currently generate EPP components or frontend sidecars. Also,
`overrides.dgd`

only patches services that already exist in the generated DGD,
so it cannot be used to add a missing `Epp`

service to a DGDR-generated
deployment. Use a direct DGD manifest or a GAIE recipe for EPP deployments.
For manifests, `frontendSidecar`

configuration, direct routing, EPP routing
variables such as `DYN_USE_KV_EVENTS`

, and route setup, see
[Gateway API Inference Extension](https://docs.nvidia.com/dynamo/v1.2.1/integrations/kubernetes-integrations/gateway-api-inference-extension-gaie). The same guide also
documents the optional [Rust EPP](https://docs.nvidia.com/dynamo/v1.2.1/integrations/kubernetes-integrations/gateway-api-inference-extension-gaie#4b-build-rust-epp-image-optional--experimental),
which is currently experimental.

### SKU Format

When providing hardware configuration manually, use lowercase underscore format:

All supported values: `gb200_sxm`

, `b200_sxm`

, `h200_sxm`

, `h100_sxm`

,
`h100_pcie`

, `a100_sxm`

, `a100_pcie`

, `a30`

, `l40s`

, `l40`

, `l4`

,
`v100_sxm`

, `v100_pcie`

, `t4`

, `mi200`

, `mi300`

.

Not all SKUs are supported by the AIC profiler for `rapid`

mode. See
[AIC Support Matrix](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/model-deployment-guide#aic-support-matrix) for details.

**PCIe variants not yet supported by profiler.** The CRD admits PCIe SKUs
(`h100_pcie`

, `a100_pcie`

, `v100_pcie`

), but the profiler does not currently
ship training data for them. You can submit a DGDR with a PCIe value; the
operator will accept it but profiler-assisted sizing will fall back to
defaults. Profiler support for PCIe SKUs is tracked as an engineering
follow-up.

## Lifecycle

When you create a DGDR, it progresses through these phases:

### Conditions

The operator maintains these conditions on the DGDR status:

### Monitoring

### Resource Ownership

- The DGDR does
**not**set an owner reference on the DGD it creates. Deleting a DGDR does not delete the DGD — it persists independently so it can continue serving traffic. - The relationship is tracked via labels:
`dgdr.nvidia.com/name`

and`dgdr.nvidia.com/namespace`

. - Additional resources (planner ConfigMaps) are created in the same namespace
and labeled with
`dgdr.nvidia.com/name`

.

## Known Issues

Tracked as an engineering follow-up. Workaround: re-run with a narrower sweep; narrow sweeps bypass the NaN path in practice.`pareto_analysis.py`

produces NaN for some configurations.**PCIe profiler data not yet available.**See the PCIe callout under[SKU Format](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/dgdr-reference#sku-format).

## Further Reading

[Deployment Overview](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/model-deployment-guide)— DGD, DCD, DGDR, recipes, strategy selection, and common pitfalls[Profiler Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide)— Profiling algorithms, picking modes, gate checks[Profiler Examples](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-examples)— Ready-to-use YAML for SLA targets, private models, MoE, overrides[Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-guide)— Scaling modes, PlannerConfig reference[API Reference](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/api-reference-k-8-s)— Complete CRD field specifications[Creating Deployments](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/creating-deployments)— DGD spec for full manual control