# [Issue #4832] [Feature] History server list resource by namespace

source: https://github.com/ray-project/kuberay/issues/4832
state: open | updated: 2026-09-23T04:43:05Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Hi team, when history server tries to load living or dead clusters, it always get entries for all namespaces.
- list RayCluster under all namespaces: https://github.com/ray-project/kuberay/blob/b110189e7b656d8c5ae6ca709befa3818bc865a6/historyserver/pkg/historyserver/clientmanager.go#L24-L38


### Use case

In the production environment, different teams are deploying in different namespaces (and we use k8s namespace for access control); I'm wondering if we could add support for listing resource only in the requested namespace?

Configuration-wise, users have to configure both Role/RoleBinding (which is namespace-scoped), AND ClusterRole/ClusterRoleBinding (which is cluster-scoped).

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (6)

### ManishSharma1609 · 2026-05-13

Hi @dentiny , are you already working on a PR for this? If not, I'd love to pick it up!

### dentiny · 2026-05-13

>  are you already working on a PR for this? If not, I'd love to pick it up!

No, feel free to. Just a reminder, I'm not part of the working group and I don't have approval or merge permission.

### ManishSharma1609 · 2026-05-13

Thanks, Happy to work on this if maintainers are okay with it.


### andrewsykim · 2026-05-13

I think @chiayi is already working on this in another PR 

### andrewsykim · 2026-05-13

For historical clusters, it will depend on https://github.com/ray-project/kuberay/issues/4774#issuecomment-4441508974

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
