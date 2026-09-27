# [Issue #2821] [Bug] KPA/APA cooldown windows are inverted, scale-down cooldown never holds replicas

source: https://github.com/vllm-project/aibrix/issues/2821
state: closed | updated: 2026-09-26T13:21:20Z
labels: kind/bug, area/orchestration

## 正文

### 🐛 Describe the bug

For KPA and APA, the scale-up and scale-down cooldown windows pick the wrong end of the recommendation history, so neither window actually holds anything back.

`stabilizeRecommendation` in `pkg/controller/podautoscaler/podautoscaler_controller.go` (L1302-L1386 on main, 5706c115) does this:

```go
if recommendation > current {
    windowDuration = scaleUpWindow
    selectMax = true   // scale up: MAX over the window
} else if recommendation < current {
    windowDuration = scaleDownWindow
    selectMax = false  // scale down: MIN over the window
}
```

The current recommendation is always part of the window. So on a scale-down the min over the window is at most the new, lower recommendation, and on a scale-up the max is at least the new, higher one. The result is that the stabilized value is always at least as aggressive as the raw recommendation. The default 5 minute `scale-down-cooldown-window` has no effect: a single low sample shrinks the workload right away.

Kubernetes HPA does the opposite (`stabilizeRecommendationWithBehaviors` in `k8s.io/kubernetes/pkg/controller/podautoscaler/horizontal.go`): scale-down uses the MAX recommendation over the scale-down window, scale-up uses the MIN over the scale-up window, and the result is `current` clamped between the two. The function comment here says "similar to K8s HPA behavior", the same annotations are passed straight through as `stabilizationWindowSeconds` for the HPA strategy in `hpa_resources.go`, and the docs describe the scale-down window as a cooldown, so HPA semantics are clearly what is intended.

### Steps to Reproduce

1. Create a KPA or APA PodAutoscaler with the default windows (scale-up 0s, scale-down 5m).
2. Run steady at 10 replicas (recommendation 10).
3. Metrics dip for one reconcile, so the algorithm recommends 2.
4. The controller scales to 2 immediately, then back up to 10 on the next reconcile once the dip is gone.

Unit-level repro: call `stabilizeRecommendation` with current=10 and recommendations 10 at t=0, then 2 at t=30s. It returns 2.

### Expected behavior

With a 5 minute scale-down window, the recommendation at t=30s should stay at 10, because 10 is still the highest recommendation inside the window. Replicas should only drop once every recommendation in the last 5 minutes is lower, and then only to the highest of them. Likewise, a non-zero scale-up window should hold off a brief spike instead of reacting to it.

### Environment

- AIBrix version: main (5706c115)
- Deployment environment: Kubernetes
- Found by reading the code and confirmed with a unit test

### Area

Orchestration (controllers, CRDs)


## 评论 (1)

### github-actions[bot] · 2026-09-26

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

