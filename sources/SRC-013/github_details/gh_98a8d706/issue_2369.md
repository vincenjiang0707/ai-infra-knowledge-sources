# [Issue #2369] [Observability] Add troubleshooting guidance for precise prefix cache routing

source: https://github.com/llm-d/llm-d/issues/2369
state: open | updated: 2026-08-25T06:25:58Z
labels: 

## 正文

Part of #1982.

The precise prefix cache routing guide explains how to enable monitoring, but it does not yet explain which signals are useful for this path or how to troubleshoot common problems.

I'd like to add an observability and troubleshooting section that covers:

- the key model server and EPP prefix-cache metrics for this path;
- how to tell whether KV events are reaching the router and the prefix index is being populated;
- what to check when cache hit rate is low or cache hits do not improve TTFT;
- links to the shared metrics, PromQL, tracing, and alerting docs instead of repeating the full metric reference;
- a pointer from the precise prefix cache routing well-lit-path page to the guide section.

The change will be limited to user-facing documentation in `llm-d/llm-d`. If the work uncovers missing instrumentation, that should be tracked separately.

## 评论 (1)

### cyclinder · 2026-08-25

/assign
