# [Issue #1568] Questions about Llama benchmarks

source: https://github.com/mlcommons/inference/issues/1568
state: closed | updated: 2026-05-09T00:41:07Z
labels: Stale

## 正文

Really exciting to see progress on LLM benchmarking in the `loadgen` codebase. I do wonder that:

a) Is `First Token latency` going to be the only metric? Sometimes we might also need per-token latency, or other metrics.
b) The "significant overhead" mentioned in https://github.com/mlcommons/inference/blob/master/language/llama2-70b/SUT.py#L333 , is it because adding `FirstTokenStreamer` to `generate` slows it down significantly?
c) Is there an expected release date on mlperf-loadgen 4.0?

Thanks for the great work :)

## 评论 (3)

### mrmhodak · 2024-01-23

@pgmpablo157321 to answer

### attafosu · 2024-01-23

@ljk3210 For the Server scenario the **first-token-latency** is one of the constraints that have to be met. The other constraint is the **time-per-output-token**. Their statistics during the run will also be reported, but the actual metric of interest here is the **target qps** which determines the frequency at which queries are dispatched to the client system.

Regarding b), yes, the overhead is a perceived one, since the implementation is not optimized. The tokens streamer runs in a live thread.

@pgmpablo157321 Can comment on the release date for the loadgen 4.0

### github-actions[bot] · 2026-05-09

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
