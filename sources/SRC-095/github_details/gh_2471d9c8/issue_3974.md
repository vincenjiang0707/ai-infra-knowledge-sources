# [Issue #3974] [Feature] mTLS Support via Cert Manager

source: https://github.com/ray-project/kuberay/issues/3974
state: open | updated: 2026-09-22T16:56:33Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently Kuberay only supports mTLS via Istio. [Cert Manager](https://cert-manager.io/docs/) is the industry standard for managing TLS certs in K8s. This feature request captures the integration of cert manager to enable mTLS as an alternative to Istio.

_Cert Manager is a graduated CNCF project so helps with open sourcification of Kuberay Operator🎉_

### Use case

I am deploying Kuberay Operator on a cluster that already has cert-manager installed for other Operators. I would like to make use of cert manager to enable mTLS for Kuberay Operator also. 

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (8)

### alimaazamat · 2025-09-19

@kryanbeane I'd love to work on this issue feel free to assign to me!

### kryanbeane · 2025-09-19

Hey @alimaazamat! Thank you but my team will soon be making a PR ready for review! Would you be interested in reviewing it once it's up?


### andrewsykim · 2025-09-19

Supportative of this change, but I would like to see what the user flow and API changes looks like with cert-manager. If possible could you share that before the PR? cc @rueian @Future-Outlier 

### kryanbeane · 2025-09-23

Hey @andrewsykim sorry I didn't see this! We have a draft PR [here](https://github.com/ray-project/kuberay/pull/3952) but we are still working on it. Happy to get a feedback. There will be no API changes, it'll be behind a feature flag that's disabled by default

### marosset · 2026-01-17

@kryanbeane is this still being worked on?
I'd be happy to help pick up some of this work

### andrewsykim · 2026-01-17

@kryanbeane @laurafitzgerald are you still planning on working on this for v1.6?

### testinfected · 2026-02-26

@kryanbeane @laurafitzgerald from an platform operator pov providing oss ray to its users, that would be awesome!

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
