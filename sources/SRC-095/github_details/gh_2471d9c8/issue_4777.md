# [Issue #4777] [Bug] applyServeTargetCapacity: .(float64) type assertion always panics because yaml.Unmarshal decodes integers as int64, causing cache idempotency check to never skip UpdateDeployments

source: https://github.com/ray-project/kuberay/issues/4777
state: closed | updated: 2026-09-24T02:12:23Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

In `rayservice_controller.go`, the function `applyServeTargetCapacity` reads the cached `ServeConfigV2` string, unmarshals it via `k8s.io/apimachinery/util/yaml`, and then attempts to extract the `target_capacity` field using a `.(float64)` type assertion:



```go
cachedConfig := make(map[string]interface{})
if err := yaml.Unmarshal([]byte(cachedServeConfigStr), &cachedConfig); err == nil {
    if cachedTargetCapacity, ok := cachedConfig["target_capacity"].(float64); ok {
        if cachedTargetCapacity == *goalTargetCapacity {
            return nil  // idempotency: skip update
        }
    }
}



### Reproduction script

Root cause: k8s.io/apimachinery/util/yaml (which wraps encoding/json for JSON-compatible input and gopkg.in/yaml.v2 for YAML) decodes all integer numbers as int64, not float64. Therefore, the .(float64) assertion always fails (returns ok = false), and the idempotency check is silently skipped on every Reconcile loop.
This was verified with a minimal Go program:

```
import "k8s.io/apimachinery/pkg/util/yaml"

data := []byte(`{"target_capacity": 50}`)
m := map[string]interface{}{}
yaml.Unmarshal(data, &m)
// m["target_capacity"] is int64(50), NOT float64(50.0)
_, ok := m["target_capacity"].(float64)  // ok == false, always!
```

### Anything else

Why existing tests did NOT catch this

The existing test TestReconcileServeTargetCapacity in rayservice_controller_unit_test.go only tests scenarios where the cached value differs from the goal value (e.g., cached=0, goal=30). It never tests the idempotency scenario (cached value == goal value)

1、缓存的初始值（0）与目标值（30 或 60）, 因此，即使代码中的 .(float64) 断言失败导致 if 块被跳过，代码继续往下执行更新逻辑，这与测试期望的“需要更新”的行为恰好一致。

2、而从未验证“没有发生更新”。例如 60 ->60 ； 此 Bug 导致代码每次都无脑更新. 



### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### git-jxj · 2026-09-24

PR #5262 is open and links this issue with `Fixes #4777`. It is awaiting review, so please keep this issue open while that PR is under consideration.
