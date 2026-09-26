# [Issue #2389] [Observability] Measure observability (tracing) performance overhead across llm-d projects

source: https://github.com/llm-d/llm-d/issues/2389
state: open | updated: 2026-09-10T19:15:26Z
labels: 

## 正文

## Background

We've added OpenTelemetry tracing instrumentation across several llm-d projects. Before we expand tracing coverage further, we want to understand its actual performance cost (latency, CPU, memory) under load, so the SIG can make informed decisions about default sampling rates and where tracing should be on by default.

## Goal

For each project below, run a tracing-on vs tracing-off (and where applicable, different sampling ratios) load test comparison, and publish the results.

`llm-d-router` already has a reusable perf-testing pipeline (`test/perf/`, using `inference-perf` + pprof profiling) and a config-driven tracing toggle (`epp.flags.tracing`, `router.tracing.sampling.samplerArg`), which can serve as the template/reference methodology for the other projects.

## Suggested methodology (per project)

- Baseline run with tracing disabled
- Run(s) with tracing enabled at a few sampling rates (e.g. 1%, 10%, 100%)
- Compare: p50/p95/p99 latency, throughput, CPU/memory utilization
- Where possible, capture a CPU profile with tracing enabled to see time spent in the tracing/exporter path
- Publish a short report (methodology + results + recommendation)

## Checklist

- [x] `llm-d-router` — tracking issue: https://github.com/llm-d/llm-d-router/issues/2665
- [ ] `llm-d-batch-gateway` — tracking issue: TBD
- [ ] `llm-d-inference-payload-processor` — tracking issue: TBD
- [ ] `llm-d-kv-cache` — tracking issue: TBD
- [ ] `llm-d-workload-variant-autoscaler` — tracking issue: TBD

/cc @ahg-g @chcost @robertgshaw2-redhat 

## 评论 (1)

### gyliu513 · 2026-09-03

Great progress by @albertoperdomo2 @rameshdoddaiah , check https://llm-d.slack.com/archives/C09305NHZ45/p1788395256787249

[aiperf-trace-cost-report.html](https://github.com/user-attachments/files/31792849/aiperf-trace-cost-report.html)
