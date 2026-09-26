source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/kubernetes/dynamo-graph-deployment-request
lastmod: 2026-09-23T23:30:39.914Z

DynamoGraphDeploymentRequest (DGDR) Reference


DynamoGraphDeploymentRequest (DGDR) Reference

Field reference and lifecycle for the DynamoGraphDeploymentRequest custom resource — Dynamo’s deploy-by-intent generator.

A `DynamoGraphDeploymentRequest`

(DGDR) is Dynamo’s deploy-by-intent generator for [ DynamoGraphDeployment](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment) (DGD) resources. You describe what you want to run and your performance targets; the profiler determines a configuration and produces the DGD that serves traffic.

For the task-oriented walkthrough — authoring a request step by step — see [Auto Deploy with DGDR](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough). For ready-to-copy manifests, see [DGDR Templates](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgdr).

This page documents the `nvidia.com/v1beta1`

API — the served, storage version.

## Spec reference

Only `model`

is required; every other field has a default or is auto-detected.

Model to deploy — a HuggingFace ID (for example `Qwen/Qwen3-0.6B`

, `meta-llama/Llama-3-70b`

) or a private model name. Must be non-empty.

Container image for the profiling job (the planner image), for example `nvcr.io/nvidia/ai-dynamo/dynamo-planner:1.4.2`

. For Dynamo < 1.1.0, use `dynamo-frontend`

.

Dynamo runtime version propagated to generated DGD components when `image`

has no parseable semantic-version tag or its tag does not identify the intended runtime.

Inference backend used for profiling and deployment.

Allowed values: auto vllm sglang trtllmProfiling depth. `rapid`

performs a fast, AIC-backed sweep (~30s); `thorough`

explores more configurations on real GPUs (2–4h).

Automatically create a DGD after profiling completes. When `false`

, the generated spec is stored in `status`

for manual review instead of being applied.

### Profiler image version compatibility

When `spec.image`

is omitted, the operator defaults it on creation to
`nvcr.io/nvidia/ai-dynamo/dynamo-planner:<operatorVersion>`

. The operator
requires `operatorVersion`

to be valid semantic versioning, so the default
image has a parseable version tag.

The DGDR-level `spec.runtimeVersionOverride`

supplies a default for generated
DGD components. After the profiler materializes the DGD and applies
`spec.overrides.dgd`

, the operator copies the DGDR value only to components that
do not already have an explicit override. This behavior applies across profiler
versions. Profilers through Dynamo 1.3.0 may discard the field while parsing the
DGDR, but the operator reapplies the default from the stored DGDR.

Set `spec.runtimeVersionOverride`

when an effective generated component image
uses a non-semantic-version tag or digest, or when its tag does not identify the
intended Dynamo runtime version. The DGDR value also covers images replaced
through `spec.overrides.dgd`

when that component does not set its own
`runtimeVersionOverride`

. An explicit component-level value takes precedence.

While a DGDR has `autoApply: false`

, you may set or change
`runtimeVersionOverride`

during `Profiling`

or `Ready`

. After it reaches
`Ready`

, you may enable `autoApply`

, either separately or while changing the
override. The operator applies the current value while creating the new DGD.
These updates do not modify `status.profilingResults.selectedConfig`

or the
`nvidia.com/generated-dgd-spec`

annotation. Other spec updates remain
forbidden after profiling starts.

When the DGDR-level field is unset, each effective generated DGD component
follows the DGD component rules independently. An overridden image without a
parseable semantic-version tag requires `runtimeVersionOverride`

on that
component.

Profilers through Dynamo 1.3.0 discard the embedded DGD override’s `apiVersion`

and `kind`

, then directly merge the remaining dictionary into a generated
`v1alpha1`

DGD. Raw storage preserves the override fields but does not convert
between DGD schemas. Use a `v1alpha1`

-shaped override under `spec.services`

; a
`v1beta1`

`spec.components`

override is not translated into the generated
service.

Expected workload characteristics for SLA-based profiling.

Input Sequence Length — expected average input tokens.

Output Sequence Length — expected average output tokens.

Optional target concurrency level. Mutually exclusive with `requestRate`

. When neither field is set and the Planner is disabled, the profiler uses its default maximum-throughput selection.

Optional target request rate in requests per second. Mutually exclusive with `concurrency`

. When neither field is set and the Planner is disabled, the profiler uses its default maximum-throughput selection.

Service-level agreement targets that drive profiling optimization.

Time To First Token target, in milliseconds.

Inter-Token Latency target, in milliseconds.

End-to-end request latency target, in milliseconds. An alternative to specifying `ttft`

+ `itl`

; cannot be combined with them.

Optimization target for SLA profiling.

Allowed values: latency throughputGPU hardware for profiling and deployment.

GPU type to target (see [SKU format](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#sku-format)). When omitted, auto-detected by selecting the GPU with the highest node count, then highest VRAM. In mixed-GPU clusters, set this to choose the GPU type; discovery and `totalGpus`

are then restricted to matching nodes.

VRAM per GPU in MiB. Auto-detected from cluster GPU nodes when omitted.

GPU budget for profiling and deployment; the profiler uses it to determine parallelism and replica count. When omitted, computed by counting GPUs on discovered nodes (filtered by `gpuSku`

when set), temporarily capped at 32 to limit the profiler search space. Set explicitly to override the cap.

GPUs per node. Auto-detected when omitted.

Primary GPU-to-GPU interconnect within a node, for example `nvlink`

or `pcie`

. Capability metadata for profiling and planning only — it does not enable any interconnect. Best-effort discovery distinguishes `nvlink`

from `pcie`

when omitted. An over-optimistic value can lead the planner to overestimate intra-node bandwidth and pick overly aggressive parallelism.

Whether the cluster has RDMA-capable networking for Dynamo data movement. Capability metadata only — it does not install or configure RDMA. Best-effort discovery via node labels when omitted. A false positive can cause transports to assume RDMA is usable and fail to connect; a false negative falls back to non-RDMA transports.

Optional PVC configuration for pre-downloaded model weights. When set, weights are loaded from the PVC instead of downloading from HuggingFace.

Name of a `ReadWriteMany`

PVC containing cached model weights. The PVC must exist in the same namespace as the DGDR.

Path to the model checkpoint directory within the PVC, for example `deepseek-r1`

or `models/Llama-3.1-405B-FP8`

.

Mount path for the PVC inside the container.

Optional Dynamo platform features in the generated deployment.

A `PlannerConfig`

object passed to the Planner service. The presence of this field (non-null) enables the planner in the generated DGD. DGDR passes it through without field-level validation; the Planner service validates it at startup. See [Planner](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#planner) for the full field list.

[runtime.RawExtension](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#RawExtension)

Configures the simulated (mocker) backend for testing without GPUs.

Deploy mocker workers instead of real inference workers.

DGDR does not currently expose a `features.kvRouter`

field. To configure router mode or KV-aware routing, use a direct DGD, a tuned recipe, or `overrides.dgd`

(see [Generated DGD overrides](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#generated-dgd-overrides)).

### Overrides

Customizes the profiling job and the generated DGD.

Overrides merged into the controller-generated profiling Job spec (for example, tolerations or node selectors). Only customizes the profiling Job — not the deployed worker pods.

[batch/v1.JobSpec](https://pkg.go.dev/k8s.io/api/batch/v1#JobSpec)

A partial, versioned DGD merged into the generated deployment. Use `nvidia.com/v1beta1`

for new overrides; `nvidia.com/v1alpha1`

remains supported for compatibility. See [Generated DGD overrides](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#generated-dgd-overrides).

[runtime.RawExtension](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#RawExtension)

## Planner

`spec.features.planner`

is a `PlannerConfig`

object, passed through to the Planner service without field-level validation; the Planner validates it at startup. Setting it (non-null) enables the planner in the generated DGD. The same object is documented standalone at [Planner Configuration](https://docs.nvidia.com/dynamo/reference/components/planner-configuration); its fields are reproduced here. Nested list-and-object types are expanded under [Additional Types](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#additional-types). All fields are optional.

### Core settings

Planner operating mode, matching the deployment topology.

Allowed values: disagg prefill decode aggInference backend the Planner scales.

Allowed values: vllm sglang trtllm mockerRuntime environment that determines how the Planner applies scaling actions.

Allowed values: kubernetes virtual global-plannerDynamo namespace of the deployment the Planner manages. Defaults from `DYN_NAMESPACE`

, which the operator injects as `{k8s_namespace}-{dgd_name}`

. Excluded from serialized output.

Optional model name override. Auto-detected from the deployment when unset.

Namespace where the GlobalPlanner runs. Required when `environment`

is `global-planner`

.

Optional directory for Planner log output.

### Optimization target

Scaling strategy. `throughput`

and `latency`

use static thresholds on queue depth and KV cache utilization — no SLA targets or profiling required. `load`

uses user-defined prefill queue-token and decode KV-utilization thresholds. `sla`

uses the Rust engine performance model to target specific `ttft_ms`

/ `itl_ms`

values. Under any target other than `sla`

, the Planner forces load scaling on, throughput scaling off, and ignores `ttft_ms`

/ `itl_ms`

.

Enable predictive, traffic-based scaling. Only honored when `optimization_target`

is `sla`

.

Enable reactive, load-based scaling. Only honored when `optimization_target`

is `sla`

. At least one scaling mode must be enabled.

Time To First Token SLA target, in milliseconds. Also accepts the alias `ttft`

. Must be greater than 0. Used only under `optimization_target: sla`

.

Inter-Token Latency SLA target, in milliseconds. Also accepts the alias `itl`

. Used only under `optimization_target: sla`

.

### Performance model and pre-deployment sweeping

How to generate optional bootstrap performance data. `none`

skips bootstrap data; `rapid`

uses AIConfigurator to simulate engine performance (~30s); `thorough`

measures on real GPUs (several hours).

Directory holding profiler-generated performance data (npz or JSON), used to bootstrap or tune the performance model when the `get_perf_metrics`

endpoint is unavailable.

Native AIConfigurator forward-pass model identity for the Rust engine performance shim, enabling real-time AIC estimates with online correction. Unsupported native configs fall back to FPM regression. Does not trigger an AIC interpolation sweep.

HuggingFace model id, for example `Qwen/Qwen3-32B`

.

AIC system identifier, for example `h200_sxm`

.

Optional backend version string.

Parallelism pick for the prefill engine. Required for `mode`

`disagg`

or `prefill`

. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#pickedparallelconfig).

Parallelism pick for the decode engine. Required for `mode`

`disagg`

, `decode`

, or `agg`

. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#pickedparallelconfig).

Optional model architecture override.

Optional weight dtype.

Optional Mixture-of-Experts dtype.

Optional activation dtype.

Optional KV cache dtype.

AIConfigurator interpolation spec. Populated by the profiler in rapid mode and written onto the Planner ConfigMap; you do not normally set this by hand. When present, the Planner runs the AIC sweep in-process at bootstrap to seed the performance model. See [AICInterpolationSpec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#aicinterpolationspec).

### GPU budget

Maximum total GPUs the Planner may allocate across worker types.

Per-DGD GPU floor enforced by the local Planner. `-1`

disables it. When set with `max_gpu_budget`

such that `min == max`

, the Planner pins the per-DGD total and only redistributes replicas between prefill and decode.

Minimum number of engine endpoints (replicas) to maintain per worker type.

GPUs per decode engine replica. Auto-detected from the deployment when unset.

GPUs per prefill engine replica. Auto-detected from the deployment when unset.

### Throughput-based scaling

Seconds between throughput-based scaling decisions. Also accepts the alias `throughput_adjustment_interval`

.

Prometheus traffic source. `frontend`

reads `dynamo_frontend_*`

metrics from the public Frontend; `router`

reads `dynamo_component_router_*`

from a LocalRouter (use for a pool-local Planner in GlobalPlanner deployments).

### Load-based scaling

Seconds between FPM tuning updates and load-based scaling decisions. Even when only throughput scaling is enabled, live FPM observations feed the performance model at this interval. Also accepts the alias `load_adjustment_interval`

. Must be greater than 0 and, when both scaling modes are on, shorter than `throughput_adjustment_interval_seconds`

.

Maximum retained ForwardPassMetrics observations for online tuning and regression fallback.

Number of buckets for observation retirement. Must be a perfect square.

Scale-down sensitivity from 0 to 100 (0 = never scale down, 100 = aggressive).

Minimum observations before load-based scaling decisions begin (cold-start threshold).

Prefill queue-token count that triggers scale-up. Required (with the scale-down field) when `optimization_target`

is `load`

and `mode`

includes prefill. Must be greater than 0 and greater than `prefill_scale_down_queue_tokens`

.

Prefill queue-token count that allows scale-down. Required alongside `prefill_scale_up_queue_tokens`

.

Decode KV-utilization percentage (0–100) that triggers scale-up. Required (with the scale-down field) when `optimization_target`

is `load`

and `mode`

includes decode. Must be greater than `decode_scale_down_kv_rate`

.

Decode KV-utilization percentage (0–100) that allows scale-down. Required alongside `decode_scale_up_kv_rate`

.

Manual fallback speculative-decoding depth. A worker’s published `runtime_config.runtime_data.spec_decode.nextn`

takes precedence when present. Must be 0 or greater.

### Load prediction

Prediction method for request count, ISL, and OSL.

Allowed values: constant arima kalman prophetApply a log1p transform to predicted request count, ISL, and OSL.

Window size (seconds) for the Prophet predictor.

Path to a warmup trace file for bootstrapping predictions.

Kalman process noise for the level component.

Kalman process noise for the trend component.

Kalman measurement noise.

Minimum data points before Kalman predictions activate.

### Prometheus metrics

These fields default from environment variables and are excluded from serialized output.

Prometheus endpoint the Planner queries for traffic metrics. Defaults to `PROMETHEUS_ENDPOINT`

, else the in-cluster `kube-prometheus`

service URL.

Optional bearer token sent as `Authorization: Bearer <token>`

on every PromQL request. Read once at startup.

Path to a file containing a bearer token, re-read before every request so rotated tokens are picked up without a restart.

Verify the upstream Prometheus TLS certificate. Defaults from `PROMETHEUS_SSL_VERIFY`

(`1`

/`true`

/`yes`

enable it). Pair with a CA bundle for a private CA.

Fixed key/value pairs appended as URL query parameters on every PromQL request. Set `PROMETHEUS_EXTRA_QUERY_PARAMS`

as a URL query string, for example `namespace=my-ns&tenant=foo`

.

Path to a CA bundle for verifying the upstream Prometheus TLS certificate. When set, the bundle is used for verification regardless of `metric_pulling_prometheus_ssl_verify`

. Must point to an existing file.

Port on which the Planner exposes its own `dynamo_planner_*`

metrics. Defaults from `PLANNER_PROMETHEUS_PORT`

. `0`

disables.

### Advisory and diagnostics

Suggestion-only mode. The Planner computes, logs, exports, and reports recommended replica counts without executing scaling actions or changing the deployment. Use it to evaluate a new configuration or validate SLA targets against production traffic.

Generate an HTML diagnostics report every N hours (simulated time). Set to `null`

to disable. Must be a positive finite number or `null`

.

Directory for HTML diagnostics reports.

Fixed report filename written under `report_output_dir`

. When unset, a timestamped name is used.

Write a compressed JSONL diagnostics log (`.log.jsonl.gz`

) next to each HTML report.

Port for the live diagnostics dashboard HTTP server. `0`

disables. When enabled, visit `http://host:port/`

for a real-time Plotly report.

### Scheduling and plugin pipeline

Plugin-pipeline scheduling. Rejects unknown fields.

Base pipeline cadence. The pipeline wakes once per interval; each plugin’s `execution_interval_seconds`

decides whether it fires. When unset, computed as the gcd of `load_adjustment_interval_seconds`

and, when throughput scaling is enabled, `throughput_adjustment_interval_seconds`

. Must be greater than 0 and evenly divide both adjustment intervals.

Outer deadline wrapping the full 4-stage pipeline. Exceeding it aborts the tick; the next tick runs from a clean state. Must be greater than 0.

Static external-plugin registrations applied at startup. Per-entry failures are logged but do not crash the Planner. See [ExternalPluginEntry](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#externalpluginentry).

gRPC registration gateway for self-registering plugins. Disabled by default.

Open the gRPC gateway at `listen`

. Not needed for static `external_plugins`

.

Bind address. A `unix:`

socket path for in-Pod registration, or `host:port`

for TCP.

Permit binding a plaintext (no-TLS) gateway on a TCP listen. Fails closed by default because the gateway receives plugins’ shared-secret tokens. `unix:`

listens are always allowed.

Plugin registry configuration — auth, transport, heartbeat, and in-process plugins. Rejects unknown fields.

Registry authentication. In the Planner process, an empty `trusted_sources`

activates a legacy compatibility fallback to unauthenticated access and logs a warning. This fallback is **DEV ONLY**; do not rely on it as an intentional configuration. Select `allow_unauthenticated`

explicitly for development. Production deployments must configure `static_secret`

.

Accepted auth sources. Use `['allow_unauthenticated']`

for development, or `['static_secret']`

with `static_secrets`

for production.

Map of `secret_value`

to `subject_label`

. Populate from a mounted Kubernetes Secret rather than hard-coding in the ConfigMap.

Outbound gRPC transport settings for calling plugins.

Allow plaintext `grpc://`

plugin endpoints. Required to use any `grpc://`

endpoint; mTLS support is not yet shipped.

Per-RPC timeout applied to every plugin call. Must be greater than 0.

gRPC keepalive time, in milliseconds.

Maximum gRPC message size (10 MB).

Minimum accepted plugin protocol version.

Maximum accepted plugin protocol version.

Reserved liveness setting. Heartbeats update registry timestamps, but no monitor currently applies this timeout or evicts plugins automatically.

Reserved liveness setting. Automatic missed-heartbeat eviction is not currently wired.

In-process plugins loaded from Python modules at startup. See [InProcessPluginSpec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#inprocesspluginspec).

Admin (ListPlugins) RBAC config. Parsed but currently inert — the gateway default-denies `ListPlugins`

regardless of `mode`

.

`spec.overrides.dgd`

is not required to enable the Planner. Use `spec.features.planner`

for Planner enablement and configuration; use `spec.overrides.dgd`

to customize profiler-generated benchmark deployments and the final DGD. For the deployment workflow, scaling-mode concepts, and cross-field validation rules, see the [Planner Configuration reference](https://docs.nvidia.com/dynamo/reference/components/planner-configuration) and [Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide).

## Generated DGD overrides

`spec.overrides.dgd`

is a partial, versioned DGD. It does not define or extend
the profiler’s candidate topology. Thorough profiling merges the override into
each generated benchmark candidate before measurement and into the
interpolation deployment. Every search strategy merges it into the final
generated DGD. Use `apiVersion: nvidia.com/v1beta1`

and
`kind: DynamoGraphDeployment`

for new overrides. Components, pod-template
containers, and container environment variables merge by `name`

; atomic lists
such as graph-level `spec.env`

and container `args`

replace their generated
values.

For example, set an environment variable on one generated component:

Inspect `.status.profilingResults.selectedConfig`

with `autoApply: false`

to find component names.
Overrides can modify only components present in the generated DGD; unknown names are ignored with a
warning, and an override cannot add deployment topology. Labels and annotations merge,
`metadata.name`

selects the final DGD name, and other identity metadata is ignored. `status`

, null
values for typed fields, and field deletion are not supported.

Existing `nvidia.com/v1alpha1`

overrides remain supported. They use the older `spec.services`

shape, merge services by name, and append `extraPodSpec.mainContainer.args`

to generated worker
arguments. In `v1beta1`

, container `args`

is atomic and replaces the generated list. Use
`v1beta1`

for new overrides and provide the complete desired argument list when overriding
`args`

.

`overrides.profilingJob`

customizes only the profiling Job. Use `overrides.dgd`

for settings that
must appear on deployed components.

For worked examples, see [DGDR Templates](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgdr). For router configuration and EPP
topologies, see the [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide) and
[Gateway API Inference Extension](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo).

## SKU format

`hardware.gpuSku`

uses lowercase underscore format (`h100_sxm`

, not `H100-SXM5-80GB`

).

Not all SKUs are supported by the AIC profiler for `rapid`

mode.

**PCIe variants not yet supported by the profiler.** The CRD admits PCIe SKUs (`h100_pcie`

, `a100_pcie`

, `v100_pcie`

), but the profiler does not currently ship training data for them. You can submit a DGDR with a PCIe value; the operator accepts it but profiler-assisted sizing falls back to defaults. Profiler support for PCIe SKUs is tracked as an engineering follow-up.

## Status

The operator maintains observed state under `status`

. See [Lifecycle](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#lifecycle) for how `phase`

and `profilingPhase`

progress, and for the full condition-type list.

High-level lifecycle phase of the deployment request.

Allowed values: Pending Profiling Ready Deploying Deployed FailedCurrent sub-phase of the profiling pipeline. Only meaningful while `phase`

is `Profiling`

; cleared when profiling completes or fails.

Name of the generated or created `DynamoGraphDeployment`

.

Name of the Kubernetes Job running the profiler.

Latest observed conditions. Standard types include `Succeeded`

, `Validation`

, `Profiling`

, `SpecGenerated`

, and `DeploymentReady`

— see [Conditions](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#conditions).

[metav1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition)

Output of the profiling process, including the selected deployment configuration.

Deprecated compatibility field retained for status objects written by older releases. The current controller does not populate it.

Recommended configuration chosen by the profiler based on the SLA targets. This is the configuration used for deployment when `autoApply`

is `true`

.

[runtime.RawExtension](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#RawExtension)

State of the deployed `DynamoGraphDeployment`

. Populated once a DGD has been created (via `autoApply`

or manually).

Desired number of replicas.

Number of replicas that are available and ready.

Most recent `metadata.generation`

observed by the controller.

## Additional Types

Nested struct types referenced by the fields above, broken out here to keep the field lists shallow. Types prefixed `batch/v1.`

, `metav1.`

, or `runtime.`

are standard Kubernetes types and link to their Go package documentation instead of being expanded.

### ParetoConfig

Deprecated compatibility type for `status.profilingResults.pareto`

. Current
profiling runs do not populate this type.

Full deployment configuration for this Pareto point.

[runtime.RawExtension](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#RawExtension)

### PickedParallelConfig

A parallelism pick emitted by AIConfigurator. Referenced by `features.planner.aic_perf_model.prefill_pick`

/ `decode_pick`

and by [AICInterpolationSpec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#aicinterpolationspec).

Tensor-parallel size.

Pipeline-parallel size.

Data-parallel (attention-DP) size.

Mixture-of-Experts tensor-parallel size.

Mixture-of-Experts expert-parallel size.

### AICInterpolationSpec

Everything the Planner needs to reproduce a rapid-mode AIC sweep. Written by the profiler onto the Planner ConfigMap; not normally hand-authored. Referenced by `features.planner.aic_interpolation`

.

HuggingFace model id.

AIC system identifier.

Input sequence length for the sweep. Must be greater than 0.

Output sequence length for the sweep. Must be greater than 0.

Maximum context length swept. Must be greater than 0.

Number of prefill interpolation points. Must be greater than 0.

Number of decode interpolation points. Must be greater than 0.

Prefill parallelism pick. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#pickedparallelconfig).

Decode parallelism pick. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#pickedparallelconfig).

### ExternalPluginEntry

One static external-plugin registration under `features.planner.scheduling.external_plugins`

. Rejects unknown fields.

Unique identifier. Must not collide with a builtin plugin id.

Pipeline stage the plugin participates in.

Allowed values: predict propose reconcile constrainStage priority. Smaller number is more authoritative.

Wire endpoint. Must start with `grpc://host:port`

; `inproc://`

is rejected here.

Bearer token validated by the registry. Populate from a mounted Secret.

Plugin protocol version. Must fall within the registry’s supported range.

Plugin’s own version string, surfaced in ListPlugins.

`0.0`

runs every tick; a positive value throttles to every N seconds. Must be 0 or greater.

Behavior when throttled. `HOLD_LAST`

reuses the cached result; `ACCEPT_WHEN_IDLE`

treats the plugin as no-opinion when not due. Accepts the name (case-insensitive) or its integer value.

Capability list consumed by the type-aware merge.

Dot-paths into the pipeline context (for example `predictions`

, `observations.traffic`

) that must be set for the plugin to fire on a tick. Empty means no gating.

Aggregation window for windowed observation types in `needs`

. `0.0`

uses `scale_interval`

freshness; a positive value aggregates over the last N seconds and must be an integer multiple of `scale_interval_seconds`

.

### InProcessPluginSpec

One in-process plugin under `features.planner.plugin_registration.in_process_plugins`

. Rejects unknown fields.

Python module path containing the plugin class.

Plugin class name within `module`

.

Unique plugin identifier.

Stage priority. Smaller number is more authoritative.

`0.0`

runs every tick; a positive value throttles to every N seconds.

Behavior when throttled.

Allowed values: ACCEPT_WHEN_IDLE HOLD_LASTCapability list consumed by the type-aware merge.

Dot-paths into the pipeline context that must be set for the plugin to fire on a tick.

Aggregation window for windowed observation types in `needs`

. Must be `0.0`

or a positive integer multiple of `scale_interval_seconds`

.

Keyword arguments passed to the plugin class constructor.

## Lifecycle

When you create a DGDR, it progresses through these phases (`status.phase`

):

### Conditions

The operator maintains these conditions on `status.conditions`

:

### Monitoring

### Resource ownership

- The DGDR does
**not**set an owner reference on the DGD it creates. Deleting a DGDR does not delete the DGD — it persists independently so it can continue serving traffic. - The relationship is tracked via labels:
`dgdr.nvidia.com/name`

and`dgdr.nvidia.com/namespace`

. - Additional resources (planner ConfigMaps) are created in the same namespace and labeled with
`dgdr.nvidia.com/name`

.

## Known issues

**PCIe profiler data not yet available.**See the PCIe callout under[SKU format](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#sku-format).