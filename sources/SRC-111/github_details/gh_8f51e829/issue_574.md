# [Issue #574] Alerting on internal scheduling problems

source: https://github.com/vllm-project/guidellm/issues/574
state: open | updated: 2026-09-04T08:08:34Z
labels: 

## 正文

**Is your feature request related to a problem? Please describe.**

Load generation performance issues alerts/detection

Simple analysis on internal counters to detect & alert on problems.

For example, detecting when request scheduling is significantly delayed.

## 评论 (1)

### therealruthvik · 2026-09-04

Hi @dbutenhof — quick question on this one.

Looked through the scheduler code a bit and noticed there's already decent data tracked, like `ttft_violations_counter` in `scheduler/constraints/saturation.py` and delay metrics (`request_dispatch_delay`, `resolve_start_delay_avg`) in the benchmark schemas.

Curious what you had in mind for "alerting" here — a log warning when something crosses a threshold mid-run, a metric exposed for something like Prometheus to scrape, or something else entirely?
