# [Issue #197] Add new benchmark mode to search for peak goodput under an SLO

source: https://github.com/vllm-project/guidellm/issues/197
state: closed | updated: 2026-09-18T11:39:07Z
labels: internal

## 正文

Often when we benchmark a new model or hardware, the goal is to determine the max RPS or tokens per second that the server can sustain under a certain SLO. We should add a new feature similar to the "sweep" but instead of doing linearly spaced constant RPS runs, it should do something like a binary search to try to find the peak load which the server can handle while meeting a defined latency SLO. 

We would need to support some config options for the SLO, to support p99 or p95 ITL and TTFT. 

I have a rough PoC of this in progress on this branch: https://github.com/dagrayvid/guidellm/tree/goodput, but wanted to open this issue to discuss the idea further and track progress.

## 评论 (1)

### QHarshil · 2026-09-04

I have this implemented and tested, opened as two PRs: #1085 adds the goodput metric, #1086 adds the search on top of it.

The starting point was the SLO guide in this repo, which lists targets like "TTFT ≤ 200ms for 99% of requests" but has no tooling to measure against them. Objectives are per-request thresholds named after `benchmark_serving` so they carry over. `tpot_ms` maps to inter-token latency rather than time per output token, and it is close to but not identical with vLLM's `tpot`, which measures to request completion.

The search varies concurrency rather than request rate, as your PoC branch also did. Every concurrency level settles into a steady state, whereas a rate above capacity grows a backlog and the measurements then describe the backlog.

Pass/fail uses attainment rather than the goodput rate. Attainment is a ratio, so it does not vary with measurement window length. The throughput-phase rate in #93 does: it is low by ramp/window, which I measured separately at 26% for a 30s run and under 1% at 300s.

I validated by predicting the knee analytically from the mock server's service-time distribution and then running the search:

| objective | predicted | found |
| --- | --- | --- |
| `e2el_ms=1200` | 19 | 19 |
| `e2el_ms=1500` | 26 | 26 |
| `e2el_ms=2000` | 38 | 38 |

Past the knee, throughput stays flat while goodput falls. At `e2el_ms=1500`, concurrency 16 gives 24.6 req/s throughput and 24.6 goodput; concurrency 32 gives 24.3 and 19.3. At `e2el_ms=2000`, concurrency 64 posts the highest throughput of any level tested, with goodput of 1.4.

Each probe carries a Wilson score interval on its attainment. When the interval straddles the target, the probe was too short to decide and the search says so rather than returning a number that looks precise.

One known limitation, noted on #1086: the final probe and the stop reason are not written to the report, because `BenchmarkConfig` snapshots profile state before each run and a probe is only recorded once the next strategy is requested. Per-probe numbers are in the benchmark metrics and the console table, and the search logs its verdict. Putting the machine-readable result in the report needs a schema field, which I left out.

