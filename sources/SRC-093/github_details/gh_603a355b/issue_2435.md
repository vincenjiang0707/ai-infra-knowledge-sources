# [Issue #2435] RayClusterFleet creates a new RayCluster before deleting the old one after a Pod failure

source: https://github.com/vllm-project/aibrix/issues/2435
state: open | updated: 2026-08-24T16:12:15Z
labels: 

## 正文

### 🐛 Describe the bug

For a running `RayClusterFleet`, when one Pod inside the managed `RayCluster` is killed (e.g. force-delete a worker Pod), AIBrix treats the RayCluster as unrecoverable and should recreate it.

**Expected recreate semantics:** delete/tear down the unhealthy old `RayCluster` first, then create a new `RayCluster`.

**Actual behavior:** AIBrix creates a **new** `RayCluster` immediately while the **old** `RayCluster` (and remaining Pods) are still present. The old cluster is cleaned up later (or may linger), so old and new RayClusters coexist for a period of time.

This can cause temporary double resource usage (e.g. GPUs) and is inconsistent with a delete-then-create recovery path.

**Related code / analysis**

1. `RayClusterReplicaSet` marks a previously provisioned but no-longer-ready RayCluster as inactive (`isClusterActive` / `filterActiveClusters` in `pkg/controller/rayclusterreplicaset/rayclusterreplicaset_utils.go`), then scales up a new RayCluster because active replicas < desired.
2. The inactive old RayCluster is not necessarily deleted as part of that scale-up path, so a new RayCluster can appear first.
3. Separately, for `strategy.type: Recreate`, `oldPodsRunning` in `pkg/controller/rayclusterfleet/recreate.go` also appears incorrect vs upstream Kubernetes Deployment Recreate (it only waits when a cluster is deleting **and** still Ready), which can similarly allow create-before-delete during rollouts. The primary scenario reported here is **Pod failure recovery** on a running Fleet, not necessarily a template rollout.

### Steps to Reproduce

1. Deploy AIBrix `0.6.0` with RayClusterFleet / distributed-inference controllers enabled, and KubeRay installed.
2. Create a `RayClusterFleet` with `spec.replicas: 1` and a RayCluster template that has multiple Pods (e.g. 1 head + N workers). Wait until the Fleet is Available and the RayCluster is Ready.
3. Force-delete one Pod belonging to that RayCluster, e.g.:

```bash
kubectl delete pod <worker-or-head-pod> --force --grace-period=0
```

4. Watch RayClusters and Pods:

```bash
kubectl get raycluster -w
kubectl get rayclusterreplicaset -w
kubectl get pods -l ray.io/is-ray-node=yes -w
```

5. Observe that a **new** RayCluster is created while the **old** RayCluster is still present.

### Expected behavior

After a Pod in the RayCluster is killed and the RayCluster becomes unhealthy:

1. AIBrix should delete / tear down the old unhealthy `RayCluster` first.
2. Only after the old RayCluster is gone (or fully terminating in a controlled delete-first sequence), create a new `RayCluster` to restore desired replicas.
3. There should be no period where a healthy-path new RayCluster is started while the old RayCluster is still fully present and consuming resources.

### Actual behavior

1. After killing one Pod, the old RayCluster becomes not Ready / inactive from AIBrix's perspective.
2. AIBrix immediately creates a **new** RayCluster to satisfy desired replicas.
3. The old RayCluster is still present at that time (delete happens later or is incomplete from the user's perspective).
4. Result: create-new-first, rather than delete-old-then-create-new.

### Environment

```text
- AIBrix version: 0.6.0
- Deployment environment: Kubernetes 1.34.1
- Cloud provider (if applicable): N/A / private cluster
- KubeRay version: v1.2.1-patch-20250726
- Workload: RayClusterFleet managing 1 RayCluster (multi-Pod head/worker)
```

### Additional context

- User expectation for failure recovery: kill one Pod → AIBrix kills the whole RayCluster → then starts a new RayCluster.
- Observed: kill one Pod → AIBrix starts a new RayCluster directly (old one still around).
- Suggested fix direction:
  - On RayCluster becoming inactive/unhealthy, explicitly delete the old RayCluster (or scale down) **before** creating a replacement.
  - Ensure recreate / recovery paths never count an inactive-but-still-existing RayCluster as “gone” for the purpose of allowing a new create.
  - Add a test that force-deletes a worker/head Pod and asserts no second RayCluster exists until the first is deleted.

## 评论 (4)

### Jeffwan · 2026-07-14

https://github.com/vllm-project/aibrix/pull/2426 already fixed this issue by @googs1025 

### zhaizhch · 2026-07-14

Thanks @Jeffwan for pointing to #2426.

I took a look at that PR — it improves RayClusterReplicaSet scale-down ordering (prefer deleting NotReady clusters first), which is helpful when multiple RayClusters already exist. However, I think the scenario I reported here is related but not fully covered by that fix.

**My scenario**

A `RayClusterFleet` is running normally with a single healthy `RayCluster` (e.g. 1 head + N workers). Then one Pod is lost due to a node/machine failure and gets deleted.

**What I observe today**

Two recovery paths run at the same time:

1. **KubeRay** tries to recover the deleted Pod inside the existing `RayCluster`.
2. **AIBrix** treats the `RayCluster` as unhealthy / inactive and **creates a new `RayCluster`** to satisfy desired replicas.

As a result, **two RayClusters can coexist temporarily** (old + new), which consumes extra quota (e.g. GPUs) that we did not intend to use.

**What I expect**

I would like a configurable recovery / restart policy on `RayClusterFleet` (or related API) so that when a single Pod failure happens, AIBrix does **not** automatically launch a replacement `RayCluster` by default.

Concretely, something like a `restartPolicy` (name TBD) that allows users to choose:

- **Do not create a new RayCluster on Pod failure** — let KubeRay handle in-place Pod recovery within the existing RayCluster, without provisioning an additional RayCluster that doubles resource usage.
- (Optionally) other modes such as delete-then-recreate the whole RayCluster, if full-cluster replacement is desired.

The main goal is to avoid silently doubling resource consumption during transient Pod/node failures.

Could you help confirm whether #2426 is intended to fully address this Pod-failure / duplicate-RayCluster case, or whether a separate policy knob is still needed? Happy to provide logs / `kubectl get raycluster -w` traces if useful.

Thanks!

### googs1025 · 2026-07-14

I think separate recovery policy still seems needed.   🤔 

### lettycat · 2026-08-24

Hi @googs1025, I’m interested in working on this issue.                                                                                                                                                                                                                                                                                                                                                                                                    I plan to first add a failing controller test that reproduces the duplicate-RayCluster behavior after a Pod failure. Before changing the API, I’d like to confirm the intended recovery policy semantics:                                                                                                                                                                                                                                                       
  - Let KubeRay recover the existing RayCluster without creating a replacement.                                                                                                                                                   
  - Optionally support delete-then-recreate as a separate policy.                                                                                                                                                                                                                                                                                                                                                                                              
Does this direction match your expectations? If so, I can propose the API shape and implementation plan before opening a PR.             
