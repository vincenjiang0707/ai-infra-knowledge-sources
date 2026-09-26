# [Issue #2667] [Bug] Flaky KVCache pod-triggered reconciliation integration test

source: https://github.com/vllm-project/aibrix/issues/2667
state: closed | updated: 2026-09-05T02:10:23Z
labels: 

## 正文

## Summary

`Go Integration Tests` has a flaky KVCache controller integration spec:

`KVCache controller test / pod-triggered reconciliation / reconciles the KVCache named by the Pod's identifier label`

The failure is at `test/integration/controller/kvcache_test.go:293`.

## Evidence

Observed at least twice in recent GitHub Actions runs:

- https://github.com/vllm-project/aibrix/actions/runs/33837843112/job/100921328903
- https://github.com/vllm-project/aibrix/actions/runs/33772035855/job/100704428793

Both failures summarize the same spec:

```text
[FAIL] KVCache controller test pod-triggered reconciliation [It] reconciles the KVCache named by the Pod's identifier label
/home/runner/work/aibrix/aibrix/test/integration/controller/kvcache_test.go:293
```

In the 2026-09-04 run, the suite reported:

```text
Ran 71 of 71 Specs
70 Passed | 1 Failed
```

In the 2026-09-03 run, the suite reported:

```text
Ran 62 of 62 Specs
61 Passed | 1 Failed
```

## What appears to fail

The failing line is the `consistentlyAbsent(...)` assertion after deleting the generated StatefulSet and before creating the labeled Pod:

```go
gomega.Expect(k8sClient.Delete(ctx, sts)).To(gomega.Succeed())
consistentlyAbsent(kv.Name, &appsv1.StatefulSet{})

gomega.Expect(k8sClient.Create(ctx, makePod(ns.Name, "labeled-pod", kv.Name))).To(gomega.Succeed())

eventuallyGet(kv.Name, &appsv1.StatefulSet{})
```

The log shows:

```text
[FAILED] Failed after 0.255s.
Expected <bool>: false to be true
```

So the StatefulSet is recreated during the quiet window, before the labeled Pod is created.

## Why this looks flaky

The test assumes that deleting the StatefulSet will not trigger any self-healing reconcile because StatefulSets are not in the KVCache controller's `Owns()` list. However, the KVCache controller does own Services:

```go
Owns(&corev1.Service{})
```

The initial KVCache reconcile creates or updates owned Services. A delayed owner-triggered reconcile from those Service events can still be pending when the test deletes the StatefulSet. If that pending reconcile runs during `consistentlyAbsent(...)`, it recreates the StatefulSet and the test fails before the Pod-trigger path is exercised.

The Pod watch/mapping itself appears to be registered:

```go
Watches(&corev1.Pod{},
    handler.EnqueueRequestsFromMapFunc(kvCacheRequestsForPod),
    builder.WithPredicates(podWithLabelFilter(constants.KVCacheLabelKeyIdentifier))).
```

## Suggested direction

The test likely needs to drain or stabilize any initial/owned-resource-triggered reconciles before deleting the StatefulSet, then create the labeled Pod and assert that the StatefulSet is recreated.

Alternatively, the spec can be rewritten to verify the Pod-event mapping without relying on the absence of all other pending reconcile events in the shared envtest manager.


## 评论 (1)

### yigitcan-ozturk · 2026-09-04

I'd like to work on this. I'll focus on making the pod-triggered reconciliation integration test deterministic by isolating/draining pending owner-triggered reconciles before the StatefulSet deletion, while preserving coverage of the Pod event mapping. I'll keep the change scoped to the test unless the investigation shows a controller-side issue.
