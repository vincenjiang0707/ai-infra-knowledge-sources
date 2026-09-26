# [Issue #326] Feature request: Perf Analyzer reporting cpu metrics

source: https://github.com/triton-inference-server/perf_analyzer/issues/326
state: open | updated: 2025-03-17T10:33:35Z
labels: 

## 正文

Hi team, 

Thanks for the amazing work! 

Would it be possible to also report CPU metrics when running perf_analyzer? 

What is the recommended alternatives?

## 评论 (3)

### nv-hwoo · 2025-03-13

Hi @VirginieBfd are you using Triton server? I know perf_analyzer can collect [server-side metrics](https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/measurements_metrics.md#server-side-prometheus-metrics) but not sure if it supports non-Triton metric endpoints. @matthewkotila probably knows more.

### matthewkotila · 2025-03-13

There's no CPU utilization metrics/statistics reported by Perf Analyzer currently. But it is something that can be added.

But I'm not sure of when we would be able to work on this.

As far as recommended alternatives, you could run `top` in the background while Perf Analyzer is running and visually/cursorily see CPU utilization.

Sorry that there aren't any great options here.

### VirginieBfd · 2025-03-17

No problem, I understand the prioritisation aspect, will keep an eye on the release notes to see if that pops up!
