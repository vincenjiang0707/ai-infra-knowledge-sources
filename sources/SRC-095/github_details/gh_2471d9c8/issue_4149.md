# [Issue #4149] Autoscaler and ArgoCD Clash

source: https://github.com/ray-project/kuberay/issues/4149
state: open | updated: 2026-09-22T16:57:16Z
labels: stale

## 正文

See documentation proposal here: https://github.com/ray-project/kuberay/pull/4148

I have tested this multiple times on my environment with the `ignoreDifferences` with up to 200 workers. Including this field was the difference maker in getting the autoscaler to perform as intended (where one can request via the python (`sdk ray.autoscaler.sdk import request_resources`) and set the number of workers. 

Without this inclusion when deploying via ArgoCD, I was observing unexpected behaviour which I raised here: https://github.com/ray-project/ray/issues/55736



## 评论 (2)

### Future-Outlier · 2026-03-20

cc @win5923 to help take a look

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
