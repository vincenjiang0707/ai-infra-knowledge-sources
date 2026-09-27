# [Issue #1749] Review benchmark configurations for sglang

source: https://github.com/llm-d/llm-d/issues/1749
state: open | updated: 2026-09-26T01:18:02Z
labels: lifecycle/stale

## 正文

Some of the sglang benchmarks show significant different with their vllm counter part, e.g. https://github.com/llm-d/llm-d/pull/1720. This could be due to different configurations such as kv cache capacity. This task is to review those and suggest either updating sglang recipes or the benchmark templates to better reflect sglang performance.

The task is to:
* run existing benchmark with sglang  and compare with vllm results
* if there are significant differences, investigate the cause and suggest updates



## 评论 (3)

### ahg-g · 2026-06-12

/assign @rahulgurnani 

### rahulgurnani · 2026-06-15

One observation I have is that sglang cache hit seems lower than what I see for vLLM when running these benchmarks. So for vLLM its 90+ percent and sglang its ~20%. It may be something to do with the benchmark or sglang config, still investigating this further.

Also, found a gap in inference-perf while running these benchmarks, that I have documented in https://github.com/kubernetes-sigs/inference-perf/issues/548



### github-actions[bot] · 2026-09-26

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
