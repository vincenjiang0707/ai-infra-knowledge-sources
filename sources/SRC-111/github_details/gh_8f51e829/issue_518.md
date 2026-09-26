# [Issue #518] Get progress metrics in a file during run, not after the result is completed

source: https://github.com/vllm-project/guidellm/issues/518
state: open | updated: 2026-09-08T06:32:48Z
labels: needs followup

## 正文

**Is your feature request related to a problem? Please describe.**
GuideLLM currently writes benchmark metrics only after the run completes. During long-running benchmarks, progress metrics are available only via the interactive TTY UI, which is not usable in automated or non-TTY environments

**Describe the solution you'd like**
Add support for emitting progress metrics to a file periodically during the run (e.g., incremental JSON/JSONL output flushed at --output-sampling intervals), so progress can be monitored programmatically without requiring a TTY.

**Additional context**
This would significantly improve observability and automation for long-running benchmarks and production test pipelines.


## 评论 (4)

### rishabh-nuta · 2025-12-15

@sjmonson @markurtz can you please help us here, or maybe guide us for some patchwork

### sjmonson · 2025-12-15

The live metrics output to the console contains only a few counters and averages. If that is all you want then it should not be too hard to generate some periodic log messages. We are looking to improve logging especially in non-interactive ttys Generating the full metrics report without affecting benchmark performance could be a challenge so I would focus on the former first. 

### sjmonson · 2025-12-16

To answer your second question a little better. The main benchmarking loop is [here](https://github.com/vllm-project/guidellm/blob/7666c658460bc34abe3cc821d3ca072cfd39074a/src/guidellm/benchmark/benchmarker.py#L133). You can look at the accumulator and the methods that take it as an argument for logging status.

### QHarshil · 2026-09-08

Does #1070 cover the non-interactive tty case here? It adds periodic benchmark logging, which looks like the periodic log messages you suggested.

If a machine-readable file is still wanted on top of that, I would add it as an `--output kind=jsonl` writing one record per interval, so it goes through the existing output registry rather than new CLI flags. Happy to build it once #1070 lands, since it would otherwise conflict in `progress.py`.
