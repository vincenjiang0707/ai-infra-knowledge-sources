# [Issue #4069] [Feature] Make RayJob dashboard polling interval configurable

source: https://github.com/ray-project/kuberay/issues/4069
state: open | updated: 2026-09-22T16:56:59Z
labels: enhancement, 1.5.0, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently, the KubeRay operator queries the Ray dashboard for every RayJob reconciliation to update its status. This feature proposes introducing a configuration option to allow users to control this polling frequency. Instead of querying on every reconciliation loop, users could define a specific interval (e.g., every 10 seconds).

### Use case

When many RayJobs are submitted to a single RayCluster, the current behavior can generate a high volume of status query requests. This places a significant load on the Ray head pod, potentially leading to performance bottlenecks and increased resource consumption.

### Related issues

https://github.com/ray-project/kuberay/issues/3907

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (3)

### Future-Outlier · 2025-09-11

To implement this feature, we need a way to pass the polling interval to the controller from the RayJob resource.
During reconciliation, the controller can then use this value.

Based on my understanding, there are two potential approaches:
1.  Modify the RayJob API: We could add a new field to the RayJob specification. However, this is generally not recommended as it involves API changes, which can be risky.
2.  Use an annotation: We could use an annotation on the RayJob resource to specify the polling interval.

### Future-Outlier · 2025-09-15

We will wait for the background go routine PR merged, then verifiy with users if this is needed.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
