# [Issue #5023] [Bug] Wrong default value for cmd flags

source: https://github.com/ray-project/kuberay/issues/5023
state: closed | updated: 2026-09-22T22:40:33Z
labels: bug, good-first-issue, cli

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

kubectl-plugin

### What happened + What you expected to happen

Related to: https://github.com/ray-project/kuberay/issues/3801

1. Should be ""
https://github.com/ray-project/kuberay/blob/94d37f2eb8cb742327db50898c37229b10afeaae/kubectl-plugin/pkg/cmd/log/log.go?plain=1#L151

2. Can directly use `util.RayVersion`
https://github.com/ray-project/kuberay/blob/94d37f2eb8cb742327db50898c37229b10afeaae/kubectl-plugin/pkg/cmd/create/create_workergroup.go?plain=1#L95
https://github.com/ray-project/kuberay/blob/94d37f2eb8cb742327db50898c37229b10afeaae/kubectl-plugin/pkg/cmd/job/job_submit.go?plain=1#L172


For 2., an improvement can be update the image if user specify ray version that's different from default (now there can be some mismatch). Like what we did in `create_cluster.go`

https://github.com/ray-project/kuberay/blob/94d37f2eb8cb742327db50898c37229b10afeaae/kubectl-plugin/pkg/cmd/create/create_cluster.go?plain=1#L167-L170


### Reproduction script

N/A

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (2)

### HsiaoHungKai · 2026-07-22

Can I take this one?

### machichima · 2026-07-22

Yes! Please go ahead @HsiaoHungKai . Thank you!
