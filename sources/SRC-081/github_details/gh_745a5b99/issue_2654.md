# [Issue #2654] [Tests] Extend CI/CD tests to plot recovery values over time

source: https://github.com/vllm-project/llm-compressor/issues/2654
state: closed | updated: 2026-09-11T16:51:49Z
labels: 

## 正文

## Follow-up to 

### Context
As a follow-up to PR  (restoring LM Eval test stability with `use_deterministic_algorithms`), we should extend our CI/CD pipeline to track and visualize model recovery metrics over time.

### Tasks
- Extend CI/CD tests to collect and plot recovery values over time
- Enable tracking of metric trends across runs to surface regressions and improvements visually

### Requested by
 in https://github.com/vllm-project/llm-compressor/pull/2652

## 评论 (3)

### dsikka · 2026-06-04

@claude review

### kylesayrs · 2026-07-07

Implemented by https://github.com/neuralmagic/LM-Eval-Viewer. Would be nice to host as a dashboard

### kylesayrs · 2026-09-11

Closing as a public issue for now, future work to create a dashboard is tracked on JIRA
