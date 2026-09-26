# [Issue #4027] [Bug] RayJob Controller query JobInfo before Job is submitted

source: https://github.com/ray-project/kuberay/issues/4027
state: open | updated: 2026-09-22T16:56:43Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

Before the submitter pod is ready and submits the job, ‎`GetJobInfo` is executed, which triggers an error.
Error is shown as below.
https://github.com/ray-project/kuberay/blob/4845306afb04f75baa21da23f5b017b1ae4f08f7/ray-operator/controllers/ray/rayjob_controller.go#L269

```json
{"level":"error",
"ts":"2025-09-01T16:12:43.670Z",
"logger":"controllers.RayJob",
"msg":"Failed to get job info",
"RayJob":{"name":"rayjob-sample","namespace":"default"},
"reconcileID":"5ab79647-a618-4dfd-94ae-e3e35a55348e",
"JobId":"rayjob-sample-rvk9q",
"error":"Job rayjob-sample-rvk9q does not exist on the cluster",
"stacktrace":"github.com/ray-project/kuberay/ray-operator/controllers/ray.(*RayJobReconciler).Reconcile\n\t/home/owenowenisme/kuberay/ray-operator/controllers/ray/rayjob_controller.go:280\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller[...]).Reconcile\n\t/home/owenowenisme/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.21.0/pkg/internal/controller/controller.go:119\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller[...]).reconcileHandler\n\t/home/owenowenisme/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.21.0/pkg/internal/controller/controller.go:340\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller[...]).processNextWorkItem\n\t/home/owenowenisme/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.21.0/pkg/internal/controller/controller.go:300\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller[...]).Start.func2.1\n\t/home/owenowenisme/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.21.0/pkg/internal/controller/controller.go:202"}
```

### Reproduction script

Simply deploy `ray-operator/config/samples/ray-job.sample.yaml` and observe the log from operator.

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (4)

### Future-Outlier · 2025-09-01

What do you think the expected behavior should be?

### Future-Outlier · 2025-09-01

In my opinion, I think `"error":"Job rayjob-sample-rvk9q does not exist on the cluster"` make sense to me.

### Future-Outlier · 2025-09-13

We can change some log level to debug

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
