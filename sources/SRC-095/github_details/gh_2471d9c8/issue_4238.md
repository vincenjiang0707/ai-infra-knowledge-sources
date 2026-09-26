# [Issue #4238] [Feature] Why doesn’t serveConfigV2 support file inputs

source: https://github.com/ray-project/kuberay/issues/4238
state: open | updated: 2026-09-22T16:57:27Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Could someone explain the design decision behind this limitation? thanks

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (5)

### Future-Outlier · 2025-11-29

1. what do you mean file inputs? can you give an example?


### Ethan-rookie · 2025-12-01

 `spec:
       serveConfigV2: application.yaml`
like this

### win5923 · 2025-12-07

RayService’s `serveConfigV2` currently only accepts inline YAML strings, for the following reasons:

- In the CRD, serveConfigV2 is defined as a string, which means it is designed to contain the full YAML content directly.
https://github.com/ray-project/kuberay/blob/aa8d8301ce0526f07d03691a3edd64b7d7c07bd1/ray-operator/apis/ray/v1/rayservice_types.go#L105-L109

- The controller simply treats this string as YAML and unmarshals it.

https://github.com/ray-project/kuberay/blob/aa8d8301ce0526f07d03691a3edd64b7d7c07bd1/ray-operator/controllers/ray/rayservice_controller.go#L1233-L1240


To support file-based inputs, maybe we can add a `serveConfigV2From` field to load the YAML from a referenced ConfigMap.

### Future-Outlier · 2025-12-08

this is worth discussing, will put it in my topic to committers next time we have meeting, thank you @win5923 

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
