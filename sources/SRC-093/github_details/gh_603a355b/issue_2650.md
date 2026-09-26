# [Issue #2650] [Batch] Auto-generate batch job template configs

source: https://github.com/vllm-project/aibrix/issues/2650
state: open | updated: 2026-09-06T16:44:36Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

When a batch job is launched today, its deployment template and parameters (parallelism, GPU/replica counts, batch size) are chosen entirely manually, which may result in insufficient resources causing job timeouts or excessive resources leading to waste. These configs should not be determined fully by users.

An automated solution is expected which automatically determines appropriate resource quotas and parameter configurations based on current resource availability and the scale of batch jobs.

### Use Case

A user submits a batch job with a model, workload, completion window, etc. The system calls a solver to recommend the deployment config and renders the ModelDeploymentTemplate automatically — no manual parallelism or replica tuning.

### Proposed Solution

It may be a possible solution to use [aiconfigurator](https://github.com/ai-dynamo/aiconfigurator)
to recommend and auto-generate these configs at job-creation time. But the solver should be adapted to fit offline batch scenarios.

Current workflow will be kept if needed and the generated config could be added as an extra choice.

## 评论 (3)

### googs1025 · 2026-09-02

 Thanks for opening this. Before we decide how to integrate this, maybe we should clarify the scope and boundary a bit.

  I'm not sure whether batch should be tightly coupled with a specific external project or implementation. This feels more like a generic batch config recommendation capability, where Dynamo/aiconfigurator could be one possible provider.

### CarolWinddd · 2026-09-02

> Thanks for opening this. Before we decide how to integrate this, maybe we should clarify the scope and boundary a bit.
> 
> I'm not sure whether batch should be tightly coupled with a specific external project or implementation. This feels more like a generic batch config recommendation capability, where Dynamo/aiconfigurator could be one possible provider.

@googs1025 thanks for bringing up the scope concern.

There is no need to fully integrating the entire aiconfigurator project into our codebase. Instead, we will invoke the aiconfigurator API via Python interfaces to get recommended configurations, e.g.
```
from aiconfigurator.cli import cli_recommend
result = cli_recommend(**params)
```
This keeps our batch capability generic. Aiconfigurator acts as one potential provider for the config‑recommendation feature, rather than being a hard‑coupled dependency. We can still support other recommendation providers in the future if needed.

### googs1025 · 2026-09-06

 This could also be useful for the PD-aware autoscaling work in #2613.

  Although this issue is focused on batch job template/config recommendation, the underlying abstraction seems reusable: a generic recommendation provider that takes workload intent, model/runtime information, available resources, and profiling data, then returns recommended deployment parameters.

 So I think it would be helpful to keep this capability generic and provider-based, rather than coupling batch directly to a specific solver implementation. Dynamo/aiconfigurator can be one provider, but the AIBrix-side API should probably leave room for other recommenders later.

  It may also be useful to add a few examples under `samples/`

