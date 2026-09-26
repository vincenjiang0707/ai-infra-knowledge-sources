source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/modular-components/planner/choose-a-planner-mode
lastmod: 2026-09-23T23:30:39.914Z

# Choose a Planner Mode

The Planner has several settings that describe different decisions. Choose them in this order so that topology, scaling policy, and runtime behavior stay aligned.

## Recommended Starting Points

Use `load`

instead of `throughput`

or `latency`

only when you want to supply the prefill queue-token and decode KV-utilization thresholds yourself.

## Choose the Deployment Topology

Set `mode`

to match the worker topology that the Planner controls.

For a single DGD, use `disagg`

or `agg`

to match the deployment. Use `prefill`

and `decode`

for independently managed pools. To coordinate multiple DGDs or expose multiple pools through one endpoint, see the [Global Planner Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/planner/global-planner-guide).

## Choose the Optimization Target

Choose the target based on whether you have specific Time To First Token (TTFT) and Inter-Token Latency (ITL) requirements.

The `throughput`

, `latency`

, and `load`

targets always use load-based scaling. They disable throughput-based scaling and ignore `enable_throughput_scaling`

and `enable_load_scaling`

.

## Choose Scaling Methods for an SLA

The `sla`

target is the only target that lets you select scaling methods. Enable at least one.

For most SLA-driven production deployments, enable both methods:

Keep `throughput_adjustment_interval_seconds`

longer than `load_adjustment_interval_seconds`

when both methods are enabled. The throughput-based method sets the capacity floor, then the load-based method adjusts above it.

## Choose the Runtime Environment

Set `global_planner_namespace`

when `environment`

is `global-planner`

. See the [Global Planner Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/planner/global-planner-guide) for the control DGD, pool-local Planner, and routing requirements.

## Check Dependencies

The KV router is not required for load-based scaling. The Planner receives engine load through FPM regardless of the routing strategy. For backend-specific FPM requirements, see [Current Limitations](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/planner/overview#current-limitations). For profiler bootstrap options, see the [Profiler Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/profiler/profiler-guide).

## Validate Before Applying Changes

Set `advisory: true`

to calculate, log, and export recommendations without changing replica counts. Use advisory mode when introducing an SLA, changing targets, or validating a new workload.

Set replica floors and `max_gpu_budget`

before disabling advisory mode. See [Tune the Planner](https://docs.nvidia.com/dynamo/dev/kubernetes/auto-deployment/dynamo-planner) for the deployment workflow and the [Planner Configuration reference](https://docs.nvidia.com/dynamo/dev/reference/components/planner-configuration) for every field and validation rule.