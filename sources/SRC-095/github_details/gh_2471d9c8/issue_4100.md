# [Issue #4100] [Bug] Failed creating ingress due to too long label, if cluster name long

source: https://github.com/ray-project/kuberay/issues/4100
state: open | updated: 2026-09-22T16:57:05Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

Long ray cluster name leads to
```
  Warning  FailedToCreateIngress  15m (x19 over 37m)  raycluster-controller  Failed creating ingress platform-development/r0-dn1-0-dn1-0-dn0-0-raycluster-cp7d8-head-ingress, Ingress.networking.k8s.io "r0-dn1-0-dn1-
0-dn0-0-raycluster-cp7d8-head-ingress" is invalid: metadata.labels: Invalid value: "axgbwrqlmz9r9g7nbvc4-n0-0-dn1-0-dn1-0-dn0-0-raycluster-cp7d8-head": must be no more than 63 characters
```
- The ray cluster name is `axgbwrqlmz9r9g7nbvc4-n0-0-dn1-0-dn1-0-dn0-0-raycluster-cp7d8` (65 chars)

### Reproduction script

Create a ray cluster with name `axgbwrqlmz9r9g7nbvc4-n0-0-dn1-0-dn1-0-dn0-0-raycluster-cp7d8`

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### sunran1203 · 2025-09-26

K8s limits labels to 63 characters. I always encounter this problem and can only find a way to compress the value.

### Future-Outlier · 2025-09-27

I think we should fail the CR right?
what's your expected behavior?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
