source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference
lastmod: 2026-09-23T23:30:39.914Z

# DGDR Reference

Field reference for DynamoGraphDeploymentRequest, the deploy-by-intent generator that profiles and produces a DGD.

A `DynamoGraphDeploymentRequest`

(DGDR) is Dynamo’s deploy-by-intent generator
for [ DynamoGraphDeployment](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s#dynamographdeployment) (DGD)
resources. You describe what you want to run and your performance targets; the
profiler determines a configuration and produces the DGD that serves traffic.

For the full deployment mental model — including DGD, DCD, DGDR, recipes,
strategy selection, model caching, planner setup, and common pitfalls — see the
[Deployment Overview](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide).

## DGDR, DGD, and Recipes

Dynamo provides two Custom Resources for deploying inference graphs:

Use DGD directly when you have a hand-crafted configuration for a specific
model/hardware combination. Most
[recipes](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes) are tuned DGD
manifests. Use DGDR when you want Dynamo to generate the DGD for you.

For DGD deployment details, see [Creating Deployments](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/creating-deployments).

## Spec Reference

### Minimal Example

### Field Reference

For the complete CRD spec, see the [API Reference](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s).

### Planner

DGDR supports Planner through `spec.features.planner`

. Set this field to a
PlannerConfig object to have DGDR pass that configuration to the profiler and
generate Planner support in the final DGD. DGDR passes this PlannerConfig
through without field-level validation; the Planner service validates it when it
starts.

When Planner is enabled, the generated output may include a `Planner`

service in
the DGD plus supporting Planner configuration resources, such as a
`planner-config-*`

ConfigMap. Depending on profiling mode and Planner settings,
DGDR may also generate profiling-data resources for Planner bootstrap data.

Minimal Planner-enabled DGDR:

To evaluate Planner recommendations without applying scaling changes, enable
advisory mode in the same `features.planner`

object:

For Planner behavior, scaling modes, and the full PlannerConfig field reference,
see the [Planner overview](https://docs.nvidia.com/dynamo/v1.3.0/components/planner) and
[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide).
For additional generated-deployment examples, see
[DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples).

`spec.overrides.dgd`

is not required to enable Planner. Use
`spec.features.planner`

for Planner enablement and configuration. Use
`spec.overrides.dgd`

only when you need to customize the generated DGD after
DGDR has assembled it.

DGDR does not currently expose a `features.kvRouter`

field. To configure
router mode or KV-aware routing details, use a direct DGD, a tuned recipe, or
`overrides.dgd`

when you still want DGDR to generate the base deployment.

### Generated DGD Overrides

Use `spec.overrides.dgd`

when the generated `DynamoGraphDeployment`

needs a
field that DGDR does not expose directly. Provide a partial, versioned DGD with
`kind: DynamoGraphDeployment`

and either `apiVersion: nvidia.com/v1beta1`

or
`apiVersion: nvidia.com/v1alpha1`

. Use `v1beta1`

for new DGDRs.

The override is applied to each complete DGD that the profiler materializes:

- The profiler generates a complete DGD blueprint.
- If the blueprint and override use different API versions, Dynamo converts the complete blueprint to the override’s version.
- Dynamo merges the override according to that version’s structural schema.
- Dynamo converts the complete merged result back to the blueprint’s version.
- The DGDR controller records
`.status.profilingResults.selectedConfig`

as a`nvidia.com/v1beta1`

DGD and creates a`v1beta1`

DGD when`autoApply`

is enabled.

Dynamo never converts the partial override by itself. This avoids filling omitted fields with conversion defaults before the merge.

For example, this `v1beta1`

override sets a graph-level environment variable
that is prepended to every generated component. The `spec.env`

list is atomic,
so include any generated graph-level entries that must be retained:

Use `spec.env`

for variables that apply to all generated components. To target
one component, identify it by `name`

. Nested map lists, including `containers`

and `env`

, also merge by `name`

:

Inspect `.status.profilingResults.selectedConfig`

with `autoApply: false`

when
you need the generated component names.

Merge behavior depends on the override’s declared API version:

Both versions follow these rules:

- When overriding topology entries, an override can update only services or components present in the generated blueprint. Dynamo ignores unknown names and reports a warning; an override cannot add deployment topology.
`metadata.labels`

and`metadata.annotations`

merge into the generated DGD.`metadata.name`

selects the final DGD name. Other identity and runtime metadata, such as`namespace`

and`finalizers`

, is ignored.`status`

overrides and`null`

values for typed fields are rejected. Field deletion is not supported.

`v1alpha1`

overrides remain supported for compatibility with existing
configurations. Kubernetes DGDR resources must include both `apiVersion`

and
`kind`

in `overrides.dgd`

. When you run the profiler directly, an older
override that omits both is treated as `v1alpha1`

and produces a compatibility
warning; an override that supplies only one is rejected.

The operator injects the override helper into Kubernetes profiling jobs. For
direct profiler runs, install the matching helper as described in
[Local Runs with DGD Overrides](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide#local-runs-with-dgd-overrides).

`overrides.profilingJob`

only customizes the profiling Job. Use
`overrides.dgd`

for settings that must appear on the deployed worker pods.

### Routing

DGDR-generated deployments include a standalone `Frontend`

component. That
frontend runs Dynamo’s embedded router and defaults to `round-robin`

routing,
which is often not optimal. Because DGDR does not yet expose a first-class
router feature, configure the generated frontend with `spec.overrides.dgd`

.

For the full router mode and environment variable reference, see
[Router Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing) and
[Router Configuration](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning).

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
[Router Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing#routing-modes-router-mode).

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
Component names depend on the selected backend and topology, so inspect the
generated DGD first, especially when `autoApply: false`

.

For example, a generated vLLM disaggregated deployment may contain a
`VllmPrefillWorker`

component. This override appends the vLLM KV-event
publishing arguments to that component while enabling the frontend KV router:

This example deliberately uses the `v1alpha1`

compatibility shape because
worker `args`

append in that version. In a `v1beta1`

override, container
`args`

is atomic and replaces the generated argument list. To use `v1beta1`

,
inspect the generated DGD and supply the complete desired argument list.

Worker KV-event flags are backend-specific. For cross-backend behavior, see
[Router Operations](https://docs.nvidia.com/dynamo/v1.3.0/components/router/router-operations#additional-notes).

In Kubernetes deployments the Dynamo runtime normally uses Kubernetes
discovery and the NATS event plane. Some backends, such as vLLM and SGLang,
emit raw KV events over ZMQ; the Dynamo worker consumes those backend events
and republishes router events through the Dynamo event plane. For the event
plane model, see [Event Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/event-plane).

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

only patches services or components that already exist in the
generated DGD, so it cannot add a missing `Epp`

component to a DGDR-generated
deployment. Use a direct DGD manifest or a GAIE recipe for EPP deployments.
For manifests, `frontendSidecar`

configuration, direct routing, EPP routing
variables such as `DYN_USE_KV_EVENTS`

, and route setup, see
[Gateway API Inference Extension](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/request-routing/gateway-api-inference-extension/overview).

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
[AIC Support Matrix](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide#aic-support-matrix) for details.

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

produces NaN for some configurations.**PCIe profiler data not yet available.**See the PCIe callout under[SKU Format](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference#sku-format).

## Further Reading

[Deployment Overview](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide)— DGD, DCD, DGDR, recipes, strategy selection, and common pitfalls[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide)— Profiling algorithms, picking modes, gate checks[Profiler Examples](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-examples)— Ready-to-use YAML for SLA targets, private models, MoE, overrides[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide)— Scaling modes, PlannerConfig reference[API Reference](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s)— Complete CRD field specifications[Creating Deployments](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/creating-deployments)— DGD spec for full manual control