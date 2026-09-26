source: https://github.com/vllm-project/guidellm/issues/518

**Is your feature request related to a problem? Please describe.**

GuideLLM currently writes benchmark metrics only after the run completes. During long-running benchmarks, progress metrics are available only via the interactive TTY UI, which is not usable in automated or non-TTY environments

**Describe the solution you'd like**

Add support for emitting progress metrics to a file periodically during the run (e.g., incremental JSON/JSONL output flushed at --output-sampling intervals), so progress can be monitored programmatically without requiring a TTY.

**Additional context**

This would significantly improve observability and automation for long-running benchmarks and production test pipelines.

Is your feature request related to a problem? Please describe.GuideLLM currently writes benchmark metrics only after the run completes. During long-running benchmarks, progress metrics are available only via the interactive TTY UI, which is not usable in automated or non-TTY environments

Describe the solution you'd likeAdd support for emitting progress metrics to a file periodically during the run (e.g., incremental JSON/JSONL output flushed at --output-sampling intervals), so progress can be monitored programmatically without requiring a TTY.

Additional contextThis would significantly improve observability and automation for long-running benchmarks and production test pipelines.