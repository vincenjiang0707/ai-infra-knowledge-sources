source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/components/planner
lastmod: 2026-09-23T23:30:39.914Z

# Planner

## Why LLM Inference Needs a Different Autoscaler

Scaling a traditional web service is straightforward: watch CPU or request rate, add replicas when load is high, remove them when it’s low. Tools like HPA and KEDA work well for this because the relationship between load and latency is roughly linear — twice the requests means roughly twice the CPU, so a simple threshold policy keeps response times stable.

LLM inference breaks these assumptions:

**Latency depends on request content, not just request count.**A single request with a 32K-token prompt consumes orders of magnitude more compute than a short one. Two requests per second can mean completely different GPU loads depending on input/output sequence lengths.**Prefill and decode have different scaling characteristics.**In disaggregated serving, prefill is compute-bound (scales with input length) while decode is memory-bound (scales with concurrent sequences and KV cache usage). A single replica count doesn’t capture both.**The metrics that matter aren’t standard.**The SLAs users care about — Time to First Token (TTFT) and Inter-Token Latency (ITL) — don’t map cleanly to CPU utilization or request throughput. HPA can’t target “keep P95 TTFT under 500ms” because that requires understanding the relationship between sequence lengths, GPU memory pressure, and latency.**Scaling decisions are expensive.**Spinning up a GPU worker takes minutes, not seconds. Overscaling wastes GPU-hours at cloud prices; underscaling violates SLAs. The autoscaler needs to predict demand, not just react to it.

The Dynamo **Planner** is an autoscaler purpose-built for these constraints. It understands engine profiling data, tracks per-worker GPU utilization, predicts traffic patterns, and makes scaling decisions that directly target TTFT and ITL SLAs — not proxy metrics.

## Getting Started: Optimization Targets

The planner offers three `optimization_target`

settings that control how scaling decisions are made:

**We recommend starting with the default throughput target** — it works out of the box with zero configuration. Switch to

`latency`

if your workload is latency-sensitive, or to `sla`

when you need precise SLA targeting with native AIC or FPM-based performance modeling.

New to the Planner?Start with the[Planner Guide]for a complete workflow including profiling and deployment.


Need multi-DGD coordination?See the[Global Planner Guide]for shared-policy coordination across multiple DGDs and single-endpoint multi-pool deployments.

## Scaling Modes

The Planner supports two scaling modes that can run independently or together:

**Throughput-based scaling**: Uses the engine perf shim and traffic prediction to compute the replica count needed to meet TTFT and ITL targets. The shim can use native AIC estimates, self-benchmark/profiler FPM bootstrap data, and live FPM tuning. Adjusts on a longer interval (default 180s). This is the primary mode for production deployments.**Load-based scaling**: Uses ForwardPassMetrics (FPM) from the Dynamo event plane and queries the same perf shim for short-term TTFT/ITL estimates. No pre-deployment data or KV Router required. Adjusts on a short interval (default 5s) to respond quickly to bursts.

When both modes are enabled, throughput-based scaling provides a capacity floor (long-term planning) while load-based scaling handles real-time adjustments above that floor.

## Feature Matrix

## When to Use Which Mode

**Throughput-based scaling**should be enabled for SLA mode when you want stable, prediction-based capacity planning. Native AIC or bootstrap FPMs make it ready sooner; otherwise it warms from live FPMs.**Load-based scaling**should be enabled when traffic is bursty or hard to predict. It reacts quickly to real-time load changes without requiring pre-deployment data.**Both modes together**: For the best of both worlds, enable both. Throughput-based scaling provides a lower bound (long-term capacity), while load-based scaling handles bursts above that floor. When both are enabled, use a longer`throughput_adjustment_interval_seconds`

than`load_adjustment_interval_seconds`

.

## Quick Start

### Prerequisites

- Dynamo platform installed on Kubernetes (
[Installation Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/installation-guide)) - kube-prometheus-stack installed (
[Metrics Setup](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics))

### Default Mode (zero config)

The planner works out of the box with no configuration needed. By default, `optimization_target`

is set to `throughput`

, which uses static thresholds on queue depth and KV cache utilization — no SLAs or profiling required:

For latency-sensitive workloads:

### SLA-Based Scaling (advanced)

For precise SLA targeting with native AIC estimates, optional bootstrap profiling data, or live FPM warmup, set `optimization_target: sla`

:

The fastest path to SLA-based scaling is through a DynamoGraphDeploymentRequest,
which automatically profiles your model. See [Planner Examples](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-examples)
for copyable DGDR manifests.

See [Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-guide) for the full workflow.

## Current Limitations

### Load-based scaling

Load-based scaling has the following known limitations. Throughput-based scaling is not affected by any of these.

**Requires ForwardPassMetrics (FPM).** Load-based scaling uses per-engine per-iteration metrics delivered via the Dynamo event plane (ForwardPassMetrics). The KV Router is **not** required for load-based scaling. FPM availability by backend:

**vLLM**— supported. Automatically enabled when the engine uses`InstrumentedScheduler`

and`DYN_FORWARDPASS_METRIC_PORT`

is set.**TensorRT-LLM**— supported for non-attention-DP workers (`attention_dp_size == 1`

); gated off when`attention_dp_size > 1`

pending per-rank FPM emission.**SGLang**— pipeline wired in Dynamo, but the upstream SGLang FPM module is not included in the current 1.2.0 SGLang runtime image. See the[SGLang FPM section](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/observability#forward-pass-metrics-fpm)for the runtime-image prerequisite.

### General

**In-flight requests during scale-down.** When the Planner scales down a worker, the worker is terminated without waiting for in-flight requests to complete. Requests that were mid-prefill on the terminated worker will fail. In disaggregated deployments, this can also affect decode workers that were waiting on KV cache transfers from the terminated prefill worker. **Workaround:** Set `min_endpoint`

to a value that avoids scaling below your steady-state traffic floor, and use a lower `load_scaling_down_sensitivity`

value to reduce the frequency of scale-down events.

## Documentation

## Configuration Reference

### Key PlannerConfig Fields

The planner process is launched with `--config /path/to/planner_config.json`

.
DGDR planner features and generated ConfigMaps are materialized into these
`PlannerConfig`

fields.

### Environment Variables

## Monitoring

### Grafana Dashboard

Deploy the planner dashboard:

The dashboard shows:

- Worker counts and GPU usage over time
- Observed TTFT, ITL, request rate, sequence lengths
- Predicted load and recommended replica counts
- Engine perf model status

### Prometheus Metrics

When `PLANNER_PROMETHEUS_PORT`

is set, the planner serves its own metrics endpoint. Exported series use the `dynamo_planner_*`

naming convention (underscores and standard unit suffixes), replacing older `planner:*`

-style names.

**Throughput-based scaling** pulls traffic metrics from the cluster-wide Prometheus server:

- Request count and duration
- TTFT and ITL distributions
- Input/output sequence lengths

Planner can read these traffic signals from either the public `Frontend`

or a pool-local `LocalRouter`

. Use `throughput_metrics_source: "frontend"`

for a single-DGD deployment. Use `throughput_metrics_source: "router"`

for GlobalPlanner / multi-pool deployments so each pool Planner reads its own router traffic instead of the shared public endpoint.

The throughput planner uses request count, ISL, OSL, and optional KV hit rate as the core traffic forecast inputs. TTFT, ITL, and request duration are also scraped and exported as observed diagnostics.

**Load-based scaling** uses ForwardPassMetrics (FPM) from the Dynamo event plane:

- Per-iteration wall time, scheduled prefill/decode tokens, and queued request status
- Delivered via
`FpmEventSubscriber`

with automatic engine discovery and lifecycle tracking - No router
`/metrics`

scraping required

FPM observes engine-side scheduled and queued work. It does not include requests still queued in the `LocalRouter`

before engine assignment.

Core gauges on the planner port include replica counts (`dynamo_planner_num_prefill_replicas`

, `dynamo_planner_num_decode_replicas`

), observed traffic (`dynamo_planner_observed_*`

), replica recommendations (`dynamo_planner_predicted_num_prefill_replicas`

, `dynamo_planner_predicted_num_decode_replicas`

), and cumulative `dynamo_planner_gpu_hours`

.

Throughput prediction gauges `dynamo_planner_predicted_requests_per_second`

, `dynamo_planner_predicted_input_sequence_tokens`

, and `dynamo_planner_predicted_output_sequence_tokens`

are wired from throughput-scaling traffic prediction and exposed alongside observed sequence-length metrics.

### Advisory mode

Set `advisory: true`

to run the local Planner in suggestion-only mode. This is recommended when you are evaluating a new Planner configuration, validating SLA targets, or reviewing how the Planner would react to production traffic before allowing it to scale workers.

In advisory mode, the Planner still observes traffic and FPM data, computes recommended prefill and decode replica counts, logs recommendation summaries, exports predicted replica metrics, and includes recommendations in diagnostics reports. The recommendations are not applied as scaling decisions: the Planner does not execute scaling actions, send replica changes to Kubernetes or GlobalPlanner, or mutate the deployment.

#### Diagnostics metrics

Additional series support dashboards and offline analysis:

**Perf-model latency estimates:**`dynamo_planner_estimated_ttft_ms`

and`dynamo_planner_estimated_itl_ms`

reflect the maximum estimated TTFT and ITL from the engine perf model across engines.**Engine capacity:**`dynamo_planner_engine_prefill_requests_per_second`

and`dynamo_planner_engine_decode_requests_per_second`

report single-engine prefill and decode capacity under the configured SLA.**Scaling decision reasons:**`dynamo_planner_load_scaling_decision`

and`dynamo_planner_throughput_scaling_decision`

are Enum gauges whose state labels encode why each mode chose to scale, hold, or skip (for example`scale_up`

,`no_fpm_data`

,`set_lower_bound`

).**Per-engine FPM queue depths:**`dynamo_planner_engine_queued_prefill_tokens`

,`dynamo_planner_engine_queued_decode_kv_tokens`

, and`dynamo_planner_engine_inflight_decode_kv_tokens`

are labeled with`worker_id`

and`dp_rank`

for each engine.

### HTML diagnostics reports

The planner can emit periodic, self-contained HTML diagnostics files with interactive Plotly charts.

Configure this in `PlannerConfig`

(or the equivalent YAML / constructor wiring your deployment uses):

`report_interval_hours`

: interval in**simulated**time between reports (default`24.0`

hours); set to`None`

to disable.`report_output_dir`

: directory where HTML files are written (default`./planner_reports`

).`live_dashboard_port`

: port for a real-time HTTP dashboard (default`8080`

). Set to`0`

to disable. An aiohttp server starts on the given port and serves the current accumulated snapshot data as an interactive Plotly report at`http://<host>:<port>/`

. Unlike periodic reports, the live dashboard does**not**clear snapshots — it always shows all data accumulated since the last periodic report (or since startup if periodic reports are disabled).

Reports aggregate per-tick snapshots and use `TickInput.now_s`

for timestamps, so they behave the same in live runs (wall clock) and in **replay** with a simulated clock. Typical charts cover worker counts, recommended replica counts, observed versus estimated latencies versus SLA targets, request rate, engine capacity, scaling decision timelines, and input/output sequence lengths. In the Replica Counts plot, actual replicas are shown as lines and the Planner’s recommended prefill and decode replica counts are shown as discrete markers at the ticks where recommendations were produced. This is especially useful with `advisory: true`

because those recommendations are suggestions only.