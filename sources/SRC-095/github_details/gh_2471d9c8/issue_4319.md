# [Issue #4319] Security Patch Release Request: Update Go to 1.25.5+ (Fix for GO-2025-4175)

source: https://github.com/ray-project/kuberay/issues/4319
state: open | updated: 2026-09-22T16:57:42Z
labels: stale

## 正文

Hi KubeRay Team,

I’d like to request a new patch release to address **[GO-2025-4175](https://pkg.go.dev/vuln/GO-2025-4175)** (wildcard SAN constraint bypass in `crypto/x509`).

I confirmed that the current image `quay.io/kuberay/operator:v1.5.1` is built with **Go 1.24.10**, which is vulnerable.

I noticed that `main` is already on Go 1.25. To resolve this, could your team please cut a new release built with **Go 1.25.5** (or later)?

Additionally, could you clarify the project's stable release cadence? I've noticed the schedule has been inconsistent with multi-month gaps between releases, and understanding the expected frequency would help us plan our security upgrades better.

Thanks

## 评论 (2)

### win5923 · 2025-12-30

Hi @LatencyTDH,
as discussed in https://github.com/ray-project/kuberay/issues/3834 and https://github.com/kubernetes-sigs/kueue/pull/5722, we intentionally avoid using patch versions, as doing so would introduce unnecessary version constraints for the broader ecosystem.

If needed, you can build a Docker image with a patch version from our release branch on your side. Apologies for any inconvenience.


> Additionally, could you clarify the project's stable release cadence? I've noticed the schedule has been inconsistent with multi-month gaps between releases, and understanding the expected frequency would help us plan our security upgrades better.

We typically cut a new release every 3–4 months.


### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
