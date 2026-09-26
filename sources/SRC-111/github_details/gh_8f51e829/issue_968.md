# [Issue #968] Implement OTEL trace format replay

source: https://github.com/vllm-project/guidellm/issues/968
state: open | updated: 2026-09-17T15:27:33Z
labels: priority-medium, internal, feature

## 正文

Support OTEL replaying OTEL trace format

References include

* https://github.com/open-telemetry/semantic-conventions-genai
* https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/otel_trace_replay.md

## 评论 (3)

### pree-dew · 2026-08-01

@dbutenhof if it's okay, can I pick this issue? I have been contributing to otel sdk, want to help.

### dbutenhof · 2026-08-03

Thanks for your interest.

To avoid massive conflicts and hopefully to better leverage common infrastructure, this is backed up behind PRs #935 (DAG builder/scheduler) and #972 (initial non-subagent WEKA). Once those are merged, extending WEKA on top of the DAG for full sub-agent scheduling will be our next priority.

Right now, the most valuable contribution might be technical review of those two PRs from the perspective of OTEL architectural requirements. (Although at this point we're hoping both are "essentially complete" and ready to merge within the next few days.)

### pree-dew · 2026-08-03

@dbutenhof Thank you for your response. I am happy to help in any way, I can look at the above PRs if that's more important as of now and if it's okay for you. 
