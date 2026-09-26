# [Issue #1983] [Observability][Feature]: Consolidate observability assets for llm-d

source: https://github.com/llm-d/llm-d/issues/1983
state: open | updated: 2026-09-13T02:34:30Z
labels: enhancement

## 正文

### Feature Area

Optimized baseline

### Problem Statement

Here are some tasks we need follow up for each repo in llm-d org.

* **Move component user-facing assets into `llm-d/llm-d`.** Migrate user-deployable scrape manifests, `PrometheusRule` alerts, and dashboards currently in component `deploy/` folders (e.g. [llm-d-router#1668](https://github.com/llm-d/llm-d-router/pull/1668)) into llm-d recipes; leave only definitional/dev-CI artifacts behind.
* **Render metric references on llm-d.ai.** Ensure each component's metric reference is present under `docs/operations/observability/` and kept in sync with the component's `docs/metrics.md` (per [llm-d-router#1636](https://github.com/llm-d/llm-d-router/pull/1636#issuecomment-4696434898)).

Check https://github.com/llm-d/llm-d/blob/main/proposals/observability-integration.md for more detail.

Please feel free to open sub issues for separate repos and link it back to this parent issue.

One example issue: https://github.com/llm-d/llm-d-router/issues/1855

### Proposed Solution

see above

### Alternatives Considered

_No response_

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

_No response_

## 评论 (2)

### gyliu513 · 2026-07-01

## Sub tasks
- [x] Router https://github.com/llm-d/llm-d-router/issues/1855
- [ ] WVA https://github.com/llm-d/llm-d-workload-variant-autoscaler/issues/1466
- [ ] kv cache https://github.com/llm-d/llm-d-kv-cache/issues/708
- [ ] batch gateway https://github.com/llm-d/llm-d-batch-gateway/issues/619
- [ ] IPP Grafana dashboard
- [ ] TBA

### sudoalok · 2026-08-13

/assign

