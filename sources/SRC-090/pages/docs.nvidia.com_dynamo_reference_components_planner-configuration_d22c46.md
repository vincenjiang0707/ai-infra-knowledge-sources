source: https://docs.nvidia.com/dynamo/reference/components/planner-configuration
lastmod: 2026-09-24T19:58:16.636Z

Planner Configuration (PlannerConfig)


Planner Configuration (PlannerConfig)

Field reference for the PlannerConfig JSON/YAML object consumed by the Dynamo Planner service.

`PlannerConfig`

is the configuration object for the Dynamo Planner. The Planner service parses it with [Pydantic](https://docs.pydantic.dev/), so every field, type, default, and constraint on this page comes from the [ PlannerConfig model](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/planner/config/planner_config.py). For the deployment workflow and scaling-mode concepts, see the

[Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide); for the autoscaler overview, see the

[Planner overview](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/overview).

## How the config is loaded

The Planner service loads `PlannerConfig`

from a single required `--config`

argument — a path to a `.json`

, `.yaml`

, or `.yml`

file, or an inline JSON string. The service auto-detects which, loads it, and validates it against the `PlannerConfig`

model. A value that is neither a readable file nor valid JSON fails at startup. How you supply it depends on where you run the Planner.

Several Prometheus fields default from environment variables and are excluded when the config is serialized back out. Set them either in the config object or through the environment variable noted on each field. See [Environment variables](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#environment-variables).

## Core settings

Planner operating mode, matching the deployment topology.

Allowed values: disagg prefill decode aggInference backend the Planner scales.

Allowed values: vllm sglang trtllm mockerRuntime environment that determines how the Planner applies scaling actions.

Allowed values: kubernetes virtual global-plannerDynamo namespace of the deployment the Planner manages. Defaults from `DYN_NAMESPACE`

, which the operator injects as `{k8s_namespace}-{dgd_name}`

. Excluded from serialized output.

Optional model name override. Auto-detected from the deployment when unset.

Namespace where the GlobalPlanner runs. **Required** when `environment`

is `global-planner`

. See the [Global Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/global-planner-guide).

Optional directory for Planner log output.

## Optimization target

Scaling strategy. `throughput`

and `latency`

use static thresholds on queue depth and KV cache utilization — no SLA targets or profiling required. `load`

uses user-defined prefill queue-token and decode KV-utilization thresholds. `sla`

uses the Rust engine performance model to target specific `ttft_ms`

/ `itl_ms`

values.

When `optimization_target`

is `throughput`

, `latency`

, or `load`

, the Planner forces load-based scaling on and throughput-based scaling off, and it ignores `ttft_ms`

/ `itl_ms`

. The two scaling-mode flags below apply only when `optimization_target`

is `sla`

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

## Performance model and pre-deployment sweeping

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

. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#pickedparallelconfig).

Parallelism pick for the decode engine. Required for `mode`

`disagg`

, `decode`

, or `agg`

. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#pickedparallelconfig).

Optional model architecture override.

Optional weight dtype.

Optional Mixture-of-Experts dtype.

Optional activation dtype.

Optional KV cache dtype.

AIConfigurator interpolation spec. Populated by the profiler in rapid mode and written onto the Planner ConfigMap; you do not normally set this by hand. When present, the Planner runs the AIC sweep in-process at bootstrap to seed the performance model. See [AICInterpolationSpec](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#aicinterpolationspec).

## GPU budget

Maximum total GPUs the Planner may allocate across worker types.

Per-DGD GPU floor enforced by the local Planner. `-1`

disables it. When set with `max_gpu_budget`

such that `min == max`

, the Planner pins the per-DGD total and only redistributes replicas between prefill and decode.

Minimum number of engine endpoints (replicas) to maintain per worker type.

GPUs per decode engine replica. Auto-detected from the deployment when unset.

GPUs per prefill engine replica. Auto-detected from the deployment when unset.

## Throughput-based scaling

Seconds between throughput-based scaling decisions. Also accepts the alias `throughput_adjustment_interval`

.

Prometheus traffic source. `frontend`

reads `dynamo_frontend_*`

metrics from the public Frontend; `router`

reads `dynamo_component_router_*`

from a LocalRouter (use for a pool-local Planner in GlobalPlanner deployments).

## Load-based scaling

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

## Load prediction

Prediction method for request count, ISL, and OSL.

Allowed values: constant arima kalman prophetApply a log1p transform to predicted request count, ISL, and OSL.

Window size (seconds) for the Prophet predictor.

Path to a warmup trace file for bootstrapping predictions.

Kalman process noise for the level component.

Kalman process noise for the trend component.

Kalman measurement noise.

Minimum data points before Kalman predictions activate.

## Prometheus metrics

These fields default from environment variables and are excluded from serialized output. Set them in the config object or through the noted environment variable.

Prometheus endpoint the Planner queries for traffic metrics. Defaults to `PROMETHEUS_ENDPOINT`

, else `http://prometheus-kube-prometheus-prometheus.monitoring.svc.cluster.local:9090`

.

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

## Advisory mode

Suggestion-only mode. The Planner computes, logs, exports, and reports recommended replica counts without executing scaling actions or changing the deployment. Use it to evaluate a new configuration or validate SLA targets against production traffic.

## Diagnostics and reporting

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

## Scheduling and plugin pipeline

The Planner runs the builtin plugin pipeline by default. `scheduling`

controls pipeline cadence; `plugin_registration`

controls how plugins register, authenticate, and communicate. For the pipeline model, see the [Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide#scheduling--plugin-pipeline).

Plugin-pipeline scheduling. Rejects unknown fields.

Base pipeline cadence. The pipeline wakes once per interval; each plugin’s `execution_interval_seconds`

decides whether it fires. When unset, computed as the gcd of `load_adjustment_interval_seconds`

and, when throughput scaling is enabled, `throughput_adjustment_interval_seconds`

. Must be greater than 0 and evenly divide both adjustment intervals.

Outer deadline wrapping the full 4-stage pipeline. Exceeding it aborts the tick; the next tick runs from a clean state. Must be greater than 0.

Static external-plugin registrations applied at startup. Per-entry failures are logged but do not crash the Planner. See [ExternalPluginEntry](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#externalpluginentry).

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

In-process plugins loaded from Python modules at startup. See [InProcessPluginSpec](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#inprocesspluginspec).

Admin (ListPlugins) RBAC config. Parsed but currently inert — the gateway default-denies `ListPlugins`

regardless of `mode`

.

## Additional types

Nested object types referenced above, broken out to keep the field lists shallow.

### PickedParallelConfig

A parallelism pick emitted by AIConfigurator. Referenced by `aic_perf_model.prefill_pick`

/ `decode_pick`

and by `AICInterpolationSpec`

.

Tensor-parallel size.

Pipeline-parallel size.

Data-parallel (attention-DP) size.

Mixture-of-Experts tensor-parallel size.

Mixture-of-Experts expert-parallel size.

### AICInterpolationSpec

Everything the Planner needs to reproduce a rapid-mode AIC sweep. Written by the profiler onto the Planner ConfigMap; not normally hand-authored.

HuggingFace model id.

AIC system identifier.

Input sequence length for the sweep. Must be greater than 0.

Output sequence length for the sweep. Must be greater than 0.

Maximum context length swept. Must be greater than 0.

Number of prefill interpolation points. Must be greater than 0.

Number of decode interpolation points. Must be greater than 0.

Prefill parallelism pick. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#pickedparallelconfig).

Decode parallelism pick. See [PickedParallelConfig](https://docs.nvidia.com/dynamo/reference/components/planner-configuration#pickedparallelconfig).

### ExternalPluginEntry

One static external-plugin registration under `scheduling.external_plugins`

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

One in-process plugin under `plugin_registration.in_process_plugins`

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

## Environment variables

The Planner reads these environment variables. The Prometheus and namespace variables set the defaults for the config fields noted above; the rest control runtime behavior for specific environments.

## Validation rules

The Planner enforces these cross-field rules at startup and rejects a config that violates any of them:

`ttft_ms`

must be greater than 0.`report_interval_hours`

must be a positive finite number or`null`

.`fpm_sample_bucket_size`

must be a perfect square.`global_planner_namespace`

is required when`environment`

is`global-planner`

.- Under
`optimization_target: load`

, prefill modes require`prefill_scale_up_queue_tokens`

>`prefill_scale_down_queue_tokens`

, and decode modes require`decode_scale_up_kv_rate`

>`decode_scale_down_kv_rate`

. - At least one scaling mode must be enabled. Under any
`optimization_target`

other than`sla`

, the Planner forces load scaling on and throughput scaling off and ignores`ttft_ms`

/`itl_ms`

. - When
`aic_perf_model`

is set,`prefill_pick`

is required for`mode`

`disagg`

/`prefill`

and`decode_pick`

for`mode`

`disagg`

/`decode`

/`agg`

. `scheduling.scale_interval_seconds`

must evenly divide`load_adjustment_interval_seconds`

and, when throughput scaling is enabled,`throughput_adjustment_interval_seconds`

.- When both scaling modes are enabled,
`load_adjustment_interval_seconds`

must be shorter than`throughput_adjustment_interval_seconds`

.