# [Issue #4068] CVE-2025-4802 & CVE-2025-47907 in Kuberay 1.4.2 from quay

source: https://github.com/ray-project/kuberay/issues/4068
state: open | updated: 2026-09-22T16:56:56Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

Others

### What happened + What you expected to happen

We recently upgraded to 1.4.2 version of the operator and our automated image scanning workflows have been failing for this image due to two high-risk CVEs in dependencies of the kuberay image from quay.  I've not had time to look into the codebase to see what a fix would entail as I'm not familiar with the kuberay codebase but I wanted to share this so that the developers are aware as I didn't see any other open or related issues.  Thanks for Kuberay and the Ray ecosystem y'all rock!

```
quay.io/kuberay/operator:v1.4.2 (debian 12.11)
==============================================
Total: 1 (HIGH: 1, CRITICAL: 0)

┌─────────┬───────────────┬──────────┬────────┬───────────────────┬─────────────────┬───────────────────────────────────────────────────────────┐
│ Library │ Vulnerability │ Severity │ Status │ Installed Version │  Fixed Version  │                           Title                           │
├─────────┼───────────────┼──────────┼────────┼───────────────────┼─────────────────┼───────────────────────────────────────────────────────────┤
│ libc6   │ CVE-2025-4802 │ HIGH     │ fixed  │ 2.36-9+deb12u10   │ 2.36-9+deb12u11 │ glibc: static setuid binary dlopen may incorrectly search │
│         │               │          │        │                   │                 │ LD_LIBRARY_PATH                                           │
│         │               │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2025-4802                 │
└─────────┴───────────────┴──────────┴────────┴───────────────────┴─────────────────┴───────────────────────────────────────────────────────────┘

manager (gobinary)
==================
Total: 1 (HIGH: 1, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                   Title                    │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼────────────────────────────────────────────┤
│ stdlib  │ CVE-2025-47907 │ HIGH     │ fixed  │ 1.24.4            │ 1.23.12, 1.24.6 │ database/sql: Postgres Scan Race Condition │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2025-47907 │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴────────────────────────────────────────────┘
```

### Reproduction script

image scanner workflows

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
