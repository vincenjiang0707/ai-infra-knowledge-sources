source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/components/planner/planner-guide
lastmod: 2026-09-23T23:30:39.914Z

# Planner Guide

The Dynamo Planner is an autoscaling controller that adjusts prefill and decode engine replica counts at runtime to meet latency SLAs. It reads traffic signals (Prometheus metrics or load predictor output) and engine performance models to decide when to scale up or down.

For a quick overview, see the [Planner overview](https://docs.nvidia.com/dynamo/v1.2.1/components/planner). For architecture internals, see [Planner Design](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/planner-design).

## Scaling Modes

The planner supports four optimization targets that determine how scaling decisions are made:

(default): Uses static thresholds on queue depth and KV cache utilization. No SLA targets or profiling needed. Works out of the box.`throughput`

: Same approach as`latency`

`throughput`

but with more aggressive thresholds — scales up earlier and tolerates less queuing. Ideal for latency-sensitive workloads.: Uses user-defined prefill queue token thresholds and decode KV utilization thresholds for reactive load-based scaling.`load`

: Uses the Rust engine performance shim with native AIC estimates when available, plus online FPM tuning or FPM regression fallback, to target specific TTFT/ITL values. Supports both throughput-based (predictive) and load-based (reactive) scaling modes. For advanced users who need precise SLA control.`sla`


**When to use which:**

- Start with
(the default) — it works immediately with no configuration.`throughput`

- Switch to
if your workload has strict latency requirements and you prefer to over-provision rather than queue.`latency`

- Use
when you want direct control through prefill queue and decode KV utilization thresholds.`load`

- Use
when you want to target specific TTFT/ITL values with native AIC estimates, optional bootstrap profiling data, or live FPM warmup.`sla`


## PlannerConfig Reference

The planner is configured via a `PlannerConfig`

JSON/YAML object. When using the profiler, this is placed under the `features.planner`

section of the DGDR spec:

For SLA-based scaling:

To evaluate Planner behavior without changing replica counts, turn on advisory mode:

Advisory mode is suggestion-only. The Planner computes recommended replica counts, logs them, exports them as diagnostics, and shows them in HTML reports. The recommendations are not applied as scaling decisions: the Planner does not execute scaling actions or change the deployment.

### Optimization Target

When `optimization_target`

is `throughput`

, `latency`

, or `load`

, load-based scaling is automatically enabled and throughput-based scaling is disabled. The `ttft_ms`

/`itl_ms`

fields are ignored.

### Scaling Mode Fields (SLA mode)

At least one scaling mode must be enabled when using `optimization_target: sla`

.

### Pre-Deployment Sweeping

SLA mode uses the Rust engine performance shim. If `aic_perf_model`

is present, the planner initializes the shim with native AIC model identity and engine limits. Unsupported native AIC configs automatically fall back to observed-FPM regression in the shim. If `aic_perf_model`

is absent, the shim starts as an FPM regression model and becomes ready after enough self-benchmark or live FPM observations.

At startup, the planner always tries to fetch self-benchmark results from the `get_perf_metrics`

Dynamo endpoint. If unavailable, it falls back to rapid-mode AIC interpolation data or profiler-generated data (npz or JSON) at `profile_results_dir`

when configured. These sources are converted to ForwardPassMetrics and used to tune or bootstrap the perf model. With `pre_deployment_sweeping_mode: none`

, the planner can still start; throughput decisions report `model_not_ready`

until native AIC is available or enough live FPMs have warmed the regression fallback.

Manual native AIC perf-model config:

### Throughput-Based Scaling Settings

### Load-Based Scaling Settings

### General Settings

### Traffic Prediction Settings

KV hit rate and speculative decode accept length are runtime engine/router signals, not traffic shape. The planner stores the latest valid observation for each signal and reuses it until a newer valid value arrives. On cold start, missing KV hit rate means no prefix-cache discount, and missing accept length means `1.0`

.

### Kalman Filter Settings

### Diagnostics Reports

The same diagnostic signals surfaced in these reports are also exported as Prometheus metrics under the `dynamo_planner_*`

prefix—for example estimated TTFT/ITL (`dynamo_planner_estimated_ttft_ms`

, `dynamo_planner_estimated_itl_ms`

), recommended replica counts (`dynamo_planner_predicted_num_prefill_replicas`

, `dynamo_planner_predicted_num_decode_replicas`

), per-engine capacity and FPM queue depths, and load/throughput scaling decision enums.

The Replica Counts plot overlays actual prefill/decode replicas with discrete recommendation markers for the Planner’s recommended prefill/decode replicas. When `advisory: true`

, these recommended counts are suggestions only; the Planner records what it would do without applying the change.

### Scheduling / plugin pipeline

The planner runs through the builtin plugin pipeline by default. The base
pipeline cadence lives under the `scheduling`

sub-tree of `PlannerConfig`

;
plugin registration, transport, and auth settings live under
`plugin_registration`

.

Existing planner fields still drive the builtin plugins:

`load_adjustment_interval_seconds`

schedules`builtin_load_propose`

, which reads FPM and worker-count observations and applies the current load-based algorithm.`throughput_adjustment_interval_seconds`

schedules`builtin_load_predict`

and`builtin_throughput_propose`

. The throughput proposer requires the prediction from the same tick, so it only fires when the predict plugin fires.- When both builtins propose targets in the same tick, load-based scaling runs after throughput-based scaling and preserves the existing behavior: throughput updates the lower-bound replicas, then load-based scaling can adjust above that floor and apply the global GPU budget clamp.
- After the plugin pipeline finishes, the planner applies the same final
`min_endpoint`

and GPU-budget safety checks to builtin and external-plugin targets before scaling the deployment.

#### DGDR example

## Integration with Profiler

When the profiler runs with planner enabled, it:

- Selects the best prefill and decode engine configurations
- Generates engine performance data (prefill TTFT vs ISL, decode ITL vs KV-cache utilization)
- Saves the
`PlannerConfig`

and performance data into separate Kubernetes ConfigMaps - Adds the planner service to the generated DGD, configured to read from those ConfigMaps

The planner receives its config via `--config /path/to/planner_config.json`

which is mounted from the `planner-config-XXXX`

ConfigMap. When thorough bootstrap data is generated, profiling data is mounted from the `planner-profile-data-XXXX`

ConfigMap.

See the [Profiler Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide) for the full profiling workflow and how to configure pre-deployment sweeping.

## Hierarchical Deployments

If you want one public endpoint for a model but multiple private DGDs optimized for different request classes, use a hierarchical deployment:

- one control DGD with
`Frontend`

,`GlobalRouter`

, and`GlobalPlanner`

- one or more prefill pool DGDs
- one or more decode pool DGDs

In the current workflow, run profiling independently for each intended pool, then compose the final control DGD plus pool DGDs manually. See the [Global Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/global-planner-guide).

## See Also

[Planner overview](https://docs.nvidia.com/dynamo/v1.2.1/components/planner)— Why LLM inference needs a different autoscaler[Planner Design](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/planner-design)— Architecture and algorithm internals[Planner Examples](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-examples)— DGDR YAML examples, sample configurations, advanced patterns[Global Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/global-planner-guide)— Multi-DGD coordination, shared GPU budgets, single-endpoint multi-pool deployments[Profiler Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide)— How profiling data is generated