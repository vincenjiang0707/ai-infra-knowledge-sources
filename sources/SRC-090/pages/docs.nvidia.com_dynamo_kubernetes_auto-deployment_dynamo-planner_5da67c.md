source: https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dynamo-planner
lastmod: 2026-09-25T12:26:00.485Z

# Tune the Planner

The [Auto Deploy with DGDR](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough) guide shows how to turn the Planner on with a few lines under `features.planner`

. This page picks up where that leaves off: which Planner knobs actually change behavior, and when to reach for each one.

The Planner exposes a long list of fields. Most workloads only need a handful. This guide covers the ones that matter — the optimization target, the two SLA scaling modes, and the guardrails that keep scaling safe — and points to the [PlannerConfig reference](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide#plannerconfig-reference) for the rest. Set every field under `spec.features.planner`

in the DGDR; DGDR passes the object through to the Planner service.

This is a how-to for tuning a Planner you have already enabled. For why LLM inference needs a purpose-built autoscaler and the prefill/decode scaling model, read the [Planner overview](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/overview) first. For the exhaustive field table, see the [Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide).

## Two levels of tuning

Planner tuning happens at two levels, and it helps to keep them separate:

**The optimization target**(`optimization_target`

) picks the overall strategy — how the Planner decides it needs to scale at all. This is the first knob everyone touches.**The SLA scaling modes**(`enable_throughput_scaling`

,`enable_load_scaling`

) tune*how*the Planner scales, but only when the target is`sla`

. They are ignored for every other target.

`optimization_target: throughput`

and `enable_throughput_scaling`

are **different knobs** despite the shared word. The first is a simple, zero-config target that scales on queue depth and KV-cache utilization. The second is a predictive scaling *mechanism* that only runs under `optimization_target: sla`

. Setting `enable_throughput_scaling`

while the target is `throughput`

does nothing. Level 1 chooses the strategy; level 2 only applies once you have chosen `sla`

.

### Choose an optimization target

`optimization_target`

is the knob to set first. It has four values, in rough order of how much setup they need:

**Reach for each when:**

— Start here. It works out of the box with no SLA targets and no profiling data, and it’s the right default when you don’t yet have latency requirements to hit.`throughput`

— Switch when your workload is latency-sensitive and you’d rather over-provision than let requests queue. It uses the same thresholds as`latency`

`throughput`

with a more aggressive trigger.— Use when you want to drive scaling directly from thresholds you set — prefill queue tokens and decode KV-cache utilization — instead of the built-in ones. Good when you understand your engine’s saturation points and want explicit control without committing to full SLA modeling.`load`

— Use when you need to hold a specific TTFT and ITL. This is the only target that models engine performance to translate “keep P95 TTFT under 500 ms” into replica counts. It’s the most powerful and the most involved — the rest of this page is mostly about tuning it.`sla`


For `throughput`

, `latency`

, and `load`

, the Planner enables load-based scaling automatically and ignores `ttft_ms`

/`itl_ms`

. Those SLA targets and the two `enable_*_scaling`

knobs below only take effect under `optimization_target: sla`

.

### Tune SLA mode: throughput vs. load scaling

Under `optimization_target: sla`

, two scaling mechanisms decide when to change replica counts. You enable them independently, and **at least one must be on.**

**Reach for each when:**

**Throughput-based scaling**gives you stable, prediction-driven capacity planning. Keep it on (the default) when traffic is reasonably predictable and you want the Planner to hold a sensible baseline rather than chase every spike.**Load-based scaling**reacts fast — it reads per-iteration engine metrics and adjusts on a short interval, so it catches bursts that prediction misses. Turn it on when traffic is spiky.**Both together**is the recommended production setup: throughput-based scaling sets the long-term floor, and load-based scaling adjusts above it in real time. When you enable both, keep`throughput_adjustment_interval_seconds`

well above`load_adjustment_interval_seconds`

so the two mechanisms don’t fight.

### Warm up the performance model

SLA mode relies on a performance model to translate latency targets into replica counts. How fast it becomes accurate depends on `pre_deployment_sweeping_mode`

:

Use `rapid`

for most cases. Reach for `thorough`

when you need measured accuracy for a production deployment or your hardware isn’t covered by AIC. With `none`

, the Planner still starts, but throughput decisions report `model_not_ready`

until enough live metrics accumulate — acceptable when load-based scaling is carrying real-time response and you’re comfortable with a slower warmup.

Reaching SLA mode through a DGDR is the fastest path because the profiler generates this bootstrap data for you. See [Auto Deploy with DGDR — Enable the Planner](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#enable-the-planner-for-runtime-autoscaling) for the profiling workflow.

### Set the guardrails

Whatever target you choose, a few knobs bound what the Planner is allowed to do. Set these before you let it scale unattended:

`min_endpoint`

and `load_scaling_down_sensitivity`

matter most because of how scale-down works: when the Planner removes a worker, it terminates it **without draining in-flight requests**, so requests mid-prefill on that worker fail. In disaggregated deployments this can also fail decode workers waiting on a KV-cache transfer from the terminated prefill worker. To reduce the blast radius, set `min_endpoint`

above your steady-state floor and lower `load_scaling_down_sensitivity`

so scale-down fires less often. See [Current Limitations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/overview#current-limitations) for the full caveat.

### Validate before you scale for real

Before letting a new configuration move GPUs, run it in **advisory mode**. The Planner observes traffic, computes recommended replica counts, logs them, and exports them as metrics — but never actually scales.

Watch the recommended counts against your actual traffic — `dynamo_planner_predicted_num_prefill_replicas`

and `dynamo_planner_predicted_num_decode_replicas`

, or the Replica Counts plot in the [diagnostics reports](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/overview#html-diagnostics-reports), which overlays recommendations on actual replicas. Use advisory mode when validating new SLA targets, evaluating a config change, or confirming how the Planner would react to production traffic. Once the recommendations look right, drop `advisory: true`

and let it scale.

## Go deeper

This page covers the knobs most workloads touch. For everything it skips: