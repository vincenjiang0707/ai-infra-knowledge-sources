# [Issue #2346] v0.8.0 Roadmap

source: https://github.com/vllm-project/aibrix/issues/2346
state: open | updated: 2026-08-21T05:27:53Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

- https://github.com/vllm-project/aibrix/issues/2290
- https://github.com/vllm-project/aibrix/issues/1966


### Use Case

share with community on the progress

### Proposed Solution

_No response_

## 评论 (1)

### googs1025 · 2026-08-02

Some feature PRs after v0.7.0 that I think can be counted for v0.8.0 roadmap progress:

- #2367 - support Kubernetes external metrics for autoscaler. This is useful foundation for metric-driven control-plane policy, and can help later warm standby / sleep mode decisions.
- #2402 - support in-place role image rollout. This improves runtime lifecycle management for RoleSet/StormService, and is related to warm runtime pool / less disruptive runtime update.
- #1846 - add Topology Policy for StormService. This gives AIBrix a native way to express co-location placement, which can help GPU pooling, P/D placement, and multi-stage serving pipeline scheduling.
- #2529 - support scheduled replica bounds for PodAutoscaler. This adds time-window based min/max replica bounds, including warm-from-zero during active windows, which helps scheduled capacity planning and warm standby workflows.
- #2570 - add request-aware auto config profile selection. This lets the gateway resolve `config-profile: auto` from request token hints and expose the selected profile for debugging, improving routing/profile automation.

