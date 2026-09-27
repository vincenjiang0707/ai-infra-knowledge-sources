# [Issue #2288] Autoscaler-driven elastic expert/data parallelism for MoE

source: https://github.com/vllm-project/aibrix/issues/2288
state: open | updated: 2026-09-27T04:32:21Z
labels: area/autoscaling, kind/feature, area/distributed

## 正文

### Feature Description and Motivation

For large MoE models we only scale whole replicas, which is coarse and expensive. vLLM has elastic EP (`enable_elastic_ep`, `/is_scaling_elastic_ep`, the DP coordinator request-wave protocol in `vllm/v1/engine/coordinator.py`) to add/remove DP/EP ranks at runtime. The autoscaler doesn't drive it. Scaling EP width by load would right-size MoE serving without full-replica steps.

### Use Case

DeepSeek / Qwen-MoE style deployments where per-replica cost is high and traffic varies; scale expert parallelism up and down instead of adding or removing entire replicas.

### Proposed Solution

Let PodAutoscaler target EP/DP width for elastic-EP-enabled deployments and drive scaling via the engine's elastic-EP endpoints + the DP coordinator wave protocol. Start observe-only (read `/is_scaling_elastic_ep` and wave state) before acting on it.


## 评论 (1)

### bolubo · 2026-09-27

Opening a design thread for this: https://github.com/vllm-project/aibrix/issues/2825. It proposes the act-side semantics on top of the observe-only step in #2812 (three-state alignment, transaction discipline within reconcile, and the failure rules we think should be agreed before acting). Feedback welcome.
