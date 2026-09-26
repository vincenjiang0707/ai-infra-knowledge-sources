# [Issue #3940] [Flaky] "Test Autoscaler E2E Part 2 (nightly operator)" is flaky

source: https://github.com/ray-project/kuberay/issues/3940
state: open | updated: 2026-09-22T16:56:21Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ci

### What happened + What you expected to happen

https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/10320/steps/canvas?jid=01989d53-2ea4-478e-887e-93e55ef29c49

```
--- RUN   TestRayClusterAutoscalerV2IdleTimeout
=== RUN   TestRayClusterAutoscalerV2IdleTimeout/Create_a_RayCluster_with_autoscaler_v2_enabled
    raycluster_autoscaler_part2_test.go:38: [2025-08-12T08:14:23Z] Created ConfigMap test-ns-rxz6g/scripts successfully
    raycluster_autoscaler_part2_test.go:71: [2025-08-12T08:14:23Z] Created RayCluster test-ns-rxz6g/ray-cluster successfully
    raycluster_autoscaler_part2_test.go:80: [2025-08-12T08:14:59Z] Found head pod test-ns-rxz6g/ray-cluster-head-77hkd
    core.go:87: [2025-08-12T08:14:59Z] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor-long-timeout --num-cpus=2]
    core.go:100: [2025-08-12T08:15:01Z] Command stdout: 
    core.go:101: [2025-08-12T08:15:01Z] Command stderr: 2025-08-12 01:14:59,797	INFO worker.py:1554 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2025-08-12 01:14:59,797	INFO worker.py:1694 -- Connecting to existing Ray cluster at address: 10.244.0.6:6379...
        2025-08-12 01:14:59,805	INFO worker.py:1879 -- Connected to Ray cluster. View the dashboard at ^[[1m^[[32m10.244.0.6:8265 ^[[39m^[[22m
    core.go:87: [2025-08-12T08:15:01Z] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor-short-timeout --num-cpus=1]
    core.go:100: [2025-08-12T08:15:02Z] Command stdout: 
    core.go:101: [2025-08-12T08:15:02Z] Command stderr: 2025-08-12 01:15:01,320	INFO worker.py:1554 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2025-08-12 01:15:01,321	INFO worker.py:1694 -- Connecting to existing Ray cluster at address: 10.244.0.6:6379...
        2025-08-12 01:15:01,329	INFO worker.py:1879 -- Connected to Ray cluster. View the dashboard at ^[[1m^[[32m10.244.0.6:8265 ^[[39m^[[22m
    core.go:87: [2025-08-12T08:15:06Z] Executing command: [python /home/ray/test_scripts/terminate_detached_actor.py actor-short-timeout]
    core.go:100: [2025-08-12T08:15:07Z] Command stdout: 
    core.go:101: [2025-08-12T08:15:07Z] Command stderr: 2025-08-12 01:15:06,849	INFO worker.py:1554 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2025-08-12 01:15:06,849	INFO worker.py:1694 -- Connecting to existing Ray cluster at address: 10.244.0.6:6379...
        2025-08-12 01:15:06,857	INFO worker.py:1879 -- Connected to Ray cluster. View the dashboard at ^[[1m^[[32m10.244.0.6:8265 ^[[39m^[[22m
    raycluster_autoscaler_part2_test.go:93: 
        Timed out after 40.000s.
        Expected
            <int32>: 2
        to equal
            <int32>: 1
    test.go:114: [2025-08-12T08:15:47Z] Retrieving Pod Container test-ns-rxz6g/ray-cluster-head-77hkd/ray-head logs
    test.go:94: [2025-08-12T08:15:47Z] Creating output directory in parent directory: /workdir/ray-operator/tmp
    test.go:105: [2025-08-12T08:15:47Z] Output directory has been created at: /workdir/ray-operator/tmp/TestRayClusterAutoscalerV2IdleTimeout_Create_a_RayCluster_with_autoscaler_v2_enabled2279968640
    test.go:114: [2025-08-12T08:15:47Z] Retrieving Pod Container test-ns-rxz6g/ray-cluster-head-77hkd/autoscaler logs
    test.go:114: [2025-08-12T08:15:47Z] Retrieving Pod Container test-ns-rxz6g/ray-cluster-long-idle-timeout-group-worker-2zt56/ray-worker logs
    test.go:114: [2025-08-12T08:15:47Z] Retrieving Pod Container test-ns-rxz6g/ray-cluster-short-idle-timeout-group-worker-vbf6q/ray-worker logs
### FAIL: TestRayClusterAutoscalerV2IdleTimeout (84.30s)
    ### FAIL: TestRayClusterAutoscalerV2IdleTimeout/Create_a_RayCluster_with_autoscaler_v2_enabled (84.30s)
```

### Reproduction script

https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/10320/steps/canvas?jid=01989d53-2ea4-478e-887e-93e55ef29c49

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (3)

### popojk · 2025-08-13

Hi @win5923 , may I work on this issue?

### win5923 · 2025-08-13

Sure, go ahead!

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
