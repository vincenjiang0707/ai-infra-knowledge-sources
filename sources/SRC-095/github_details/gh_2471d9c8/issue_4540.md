# [Issue #4540] [feature] [operator] Pods will be deleted in batches repeatedly and frequently after configuration with numOfHosts

source: https://github.com/ray-project/kuberay/issues/4540
state: open | updated: 2026-09-22T16:58:39Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

The current logic of numOftons is that pods under the same EP group will be deleted and created atomically. But we found a situation where when creating a rayjob, if pods failed to create due to resourcequota and other reasons, it would batch delete all pods in an EP group because it detected that the expected number of pods was not equal to the actual number of pods created, and requeue for the next reconciliation.

We want to not detect the relationship between the expected number of pods and the actual number of pods when **creating a rayjob**, so that frequent batch deletions of pods will not be triggered. Only after rayjob runs, check whether any pods in the EP group have been deleted. The advantage of this is that the stage of creating rayjob is more stable, and there will be no multiple batch pod deletion requests, which will increase the load on apiserver

### Reproduction script

Set a smaller resourcequota to make pod creation fail

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (6)

### dushulin · 2026-02-26

cc @EthanGuoliang 

### dushulin · 2026-02-26

PTAL, Thanks, we can discuss this case @Future-Outlier 

### Future-Outlier · 2026-02-28

let's sync offline

### Future-Outlier · 2026-03-14

Hi, @dushulin 
do you mind provide a reproduction script?

### dushulin · 2026-03-14

信件已收到      【自动回复】

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
