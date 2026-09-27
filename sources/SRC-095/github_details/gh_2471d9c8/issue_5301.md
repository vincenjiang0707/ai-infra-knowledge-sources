# [Issue #5301] [Bug][RayCluster][YuniKorn] Hard-gang placeholder timeout causes unbounded Pod recreation against a terminated YuniKorn application

source: https://github.com/ray-project/kuberay/issues/5301
state: open | updated: 2026-09-27T03:12:56Z
labels: 

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.

### KubeRay Component

ray-operator

### KubeRay Version

v1.5.1 (behavior also present on main @ `feeaf72f`)

### Ray Version

2.54

### Environment

- Kubernetes version: v1.36.1 (server)
- Installation method (Helm / Kustomize / YAML): YAML
- OS: Linux
- Apache YuniKorn (scheduler + k8shim) — an internal build carrying minor changes, none in the placeholder-timeout or application-state paths discussed below. The referenced behavior is upstream YuniKorn's.

### What happened + What you expected to happen

## Summary

When YuniKorn's gang `placeholderTimeoutInSeconds` expires under `gangSchedulingStyle=Hard`, the KubeRay operator and YuniKorn enter permanent disagreement. YuniKorn terminates the application and fails the Ray Pods; KubeRay treats those failed Pods as ordinary terminal Pods, deletes them, and recreates them against a YuniKorn application that no longer exists. The recreated Pods can never be scheduled, and the RayJob keeps reporting as running until `activeDeadlineSeconds`.

Net effect: an unbounded Pod-recreation loop against a dead scheduler application, with no signal on the RayJob or RayCluster that gang reservation has permanently failed.

## Reproduction

1. Run the operator with `--batch-scheduler=yunikorn`.
2. Submit a RayJob with `ray.io/gang-scheduling-enabled: "true"` requesting a gang that cannot be satisfied — e.g. a CPU head plus two workers on a GPU node type with no available capacity and no provisioner able to supply it within the timeout.
3. Set `yunikorn.apache.org/schedulingPolicyParameters: "placeholderTimeoutInSeconds=300 gangSchedulingStyle=Hard"`.

Observed timeline:

- `T+0s` — k8shim creates all three placeholders. YuniKorn binds the head placeholder to an existing CPU node; both worker placeholders stay pending because matching GPU capacity is unavailable.
- `T+300s` — YuniKorn correctly enforces the hard-gang timeout: the application transitions `Accepted -> Failing -> Failed` with `ResourceReservationTimeout`; the original head and both original worker Pods are set to `Phase: Failed`, `Reason: ResourceReservationTimeout`; the allocated placeholder is released, all asks are removed, placeholder Pods are deleted, and the application is removed from the queue.
- `T+300s` (milliseconds later) — the kuberay-operator reconciles the RayCluster, sees the head and workers missing relative to `replicas`, and creates replacements. k8shim observes these new tasks *after* the application has already been removed. They stay `Pending` forever: they carry the same `applicationId`, which now belongs to a terminal application, so no new gang can form.
- The RayJob remains in a running state until `activeDeadlineSeconds` (`rayjob_controller.go:1236`).

It is worth stating explicitly, because it is easy to misdiagnose: placeholder Pods disappearing while Ray Pods sit `Pending` does **not** mean YuniKorn retained the real Pods or admitted part of the gang. It means KubeRay recreated children to satisfy the unchanged RayCluster desired state.

## Why this is structural rather than a misconfiguration

Two controllers own Pod lifecycle with no shared state, and neither informs the other.

On the KubeRay side, `shouldDeletePod` classifies a `Failed` Pod as safely recreatable (`ray-operator/controllers/ray/raycluster_controller.go:1517`):

> If the Pod's status is `Failed` or `Succeeded`, the Pod will not restart and we can safely delete it. KubeRay will delete the Pod and create new Pods in the next reconciliation if necessary.

That is correct for a crashed Ray container, but a Pod failed by the scheduler with `ResourceReservationTimeout` carries the opposite meaning: the workload was rejected and should not be recreated as-is.

On the YuniKorn plugin side there is no writeback path at all (`ray-operator/controllers/ray/batchscheduler/yunikorn/yunikorn_scheduler.go`):

- `DoBatchSchedulingOnSubmission` — no-op (line 41)
- `CleanupOnCompletion` — no-op (line 139)
- `ConfigureReconciler` — returns the builder unchanged (line 152), so **no watch is registered on any YuniKorn object**
- `AddMetadataToChildResource` — only stamps `applicationId` / `queue` labels and the task-groups annotation

So the operator has no visibility into YuniKorn application state, and the `BatchScheduler` interface has no hook a plugin could use to report "the scheduler gave up on this workload." There is no configuration that resolves this.

Two aggravating details:

- `applicationId` is derived from the parent CR and is therefore constant across reconciles, so recreated Pods deterministically rejoin the dead application ID rather than forming a fresh gang.
- YuniKorn has no requeue concept here. Hard style fails the application terminally; Soft style instead *downgrades to non-gang best-effort scheduling*, which for a multi-node Ray cluster is exactly the partial allocation that gang scheduling was meant to prevent. Neither style leaves a usable path.

## Expected behavior

When gang reservation fails terminally, the RayJob/RayCluster should reflect it rather than silently looping. Concretely, any of:

1. **Surface it.** A RayCluster condition (and a corresponding RayJob transition to `Failed`) when the batch scheduler reports terminal rejection of the gang — so `activeDeadlineSeconds` is not the only backstop.
2. **Stop recreating.** Have `shouldDeletePod` (or the reconcile path around it) not blindly recreate Pods that a batch scheduler failed with a scheduler-owned reason, at minimum when gang scheduling is enabled.
3. **Give plugins a hook.** Extend the `BatchScheduler` interface with something like `OnSchedulingFailure`, or a `ConfigureReconciler` watch on scheduler-owned objects, so the YuniKorn plugin can observe application state and write a condition. Today `ConfigureReconciler` is a no-op for this plugin, so it cannot.

For contrast, Kueue avoids this class of problem entirely by owning the *job* object — it toggles `spec.suspend` on the RayJob, so KubeRay's reconcile loop becomes the enforcement mechanism rather than an adversary. The YuniKorn integration has no equivalent lever.

Related: #5233 covers the adjacent problem of quota-blocked worker groups being indistinguishable from slow-starting ones. This issue is the terminal-failure case of the same missing signal.

### Reproduction script

Not provided — reproduction requires a cluster where a gang's GPU capacity cannot be satisfied within `placeholderTimeoutInSeconds`. The steps above are sufficient to reproduce on any cluster with YuniKorn and an unsatisfiable node selector.

### Anything else

Of the three directions above, option 3 (a plugin hook) looks like the one that would generalize to Volcano and scheduler-plugins as well, but that is a maintainer call.

Reported from an evaluation rather than a production deployment, so this is filed as a findings record — I am not planning to drive the fix myself, but happy to answer questions or supply further logs from the run.

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!


## 评论 (3)

### dundysm · 2026-09-17

taking a look; planning to stop unbounded pod recreation after yunikorn ResourceReservationTimeout (hard-gang) so the rayjob surfaces a terminal gang failure instead of looping against a dead applicationId

### dundysm · 2026-09-17

opened pr https://github.com/ray-project/kuberay/pull/5305

treats yunikorn hard-gang ResourceReservationTimeout as a terminal batch scheduler failure: stops pod delete/recreate against the dead applicationId, sets raycluster failed status/reason (and BatchSchedulingFailed condition when enabled), and fails the rayjob while initializing.

verified with unit tests (shouldDeletePod, fake-client reconcilePods/calculateStatus, and helper tests).

### fscnick · 2026-09-27

Hi @ankushbbbr , 

There has been some discussion about possible fixes for this issue. If you're encountering this with a RayJob, would `preRunningDeadlineSeconds` help as a workaround?
