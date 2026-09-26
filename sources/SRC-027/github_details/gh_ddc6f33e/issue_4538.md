# [Issue #4538] Documentation Link Check Failed - 2026-07-20

source: https://github.com/AI-Hypercomputer/maxtext/issues/4538
state: closed | updated: 2026-07-20T21:57:43Z
labels: documentation

## 正文

## Documentation Link Check Failed

The weekly documentation link checker has detected broken links.

**Workflow Run:** https://github.com/AI-Hypercomputer/maxtext/actions/runs/29733785939

### Broken Links Report

```
guides/monitoring_and_debugging/features_and_diagnostics.md:83: [broken] https://cloud.google.com/compute/docs/gpus#h100-gpus: Anchor 'h100-gpus' not found
guides/monitoring_and_debugging/use_vertex_ai_tensorboard.md:31: [redirected permanently] https://docs.cloud.google.com/vertex-ai/docs/start/cloud-environment#set_up_a_project to https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/cloud-environment
guides/data_input_pipeline/data_input_grain.md:18: [broken] https://google-grain.readthedocs.io/en/stable/grain.dataset.html#grain.MapDataset.shuffle: Anchor 'grain.MapDataset.shuffle' not found
```

Please review and fix the broken links in the documentation.


## 评论 (1)

### SurbhiJainUSC · 2026-07-20

PR to fix the issue: https://github.com/AI-Hypercomputer/maxtext/pull/4539
