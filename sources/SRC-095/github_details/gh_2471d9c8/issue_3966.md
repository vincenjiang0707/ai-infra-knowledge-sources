# [Issue #3966] [Epic][Feature] Support History Server

source: https://github.com/ray-project/kuberay/issues/3966
state: closed | updated: 2026-09-23T07:00:10Z
labels: size:large, roadmap, 1.5.0, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

This issue aims to track multiple pull requests (PRs) related to implementing or enhancing support for a history server within the project.

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (13)

### KunWuLuan · 2025-08-18

TODO: 
- [ ] Design Doc
- [ ] Agent Implementation
- [ ] Front End Implementation
- [ ] Webserver Implementation
- [ ] Sidecar Injection By Kuberay

### liugs0213 · 2025-08-18

> TODO:
> 
> * [ ]  Design Doc[ ]  Agent Implementation[ ]  Front End Implementation[ ]  Webserver Implementation[ ]  Sidecar Injection By Kuberay

Hi, I’m also very interested in this feature.
I noticed that there is already a [KubeRay Dashboard](https://github.com/ray-project/kuberay/tree/master/dashboard).
Do you plan to reuse/extend the existing KubeRay dashboard for the history server implementation, or build a new one from scratch?

### my-vegetable-has-exploded · 2025-08-21

Here is a related issue #3884

### Myasuka · 2025-09-03

@KunWuLuan I noticed that there already have a PR focusing on log collector, in my mind, this is just part of the whole plan. Thanks for the contribution and looks forward for the update of design docs.

### KunWuLuan · 2025-12-01

https://github.com/ray-project/kuberay/pull/4241

https://github.com/ray-project/kuberay/pull/4242

https://github.com/ray-project/kuberay/pull/4187

All codes have been split into 3 PRs for reviewing. @Future-Outlier 

### Future-Outlier · 2025-12-01

Hi, @KunWuLuan thank you so much!!
plz remove Chinese comment and I'll start review today

### Future-Outlier · 2025-12-03

Hi, @chiayi
will there be a chance to see your implementation about event server with this one https://github.com/ray-project/kuberay/pull/4241 ?


### metasyn · 2025-12-08

Really looking forward to this landing. Thank you all for adding it.

### jmccarthy-lila · 2025-12-10

Thanks for working on this feature, really excited about this as well. I am able to build and launch the historyserver from the Dockerfile and instructions on #4187 on kind, but selecting a cluster via `/enter_cluster/...` fails:
`could not read HTML file`
I can see in the local minio bucket the session logs - might be just a case of routing. Any suggestions for building and utilizing?

### Future-Outlier · 2025-12-10

Hi @jmccarthy-lila,
Here is a step by step guide: https://github.com/ray-project/kuberay/pull/4187#pullrequestreview-3509505276
I think it’s ok to wait until the alpha version is released, since it’s not done yet.

### my-vegetable-has-exploded · 2025-12-10

> Thanks for working on this feature, really excited about this as well. I am able to build and launch the historyserver from the Dockerfile and instructions on [#4187](https://github.com/ray-project/kuberay/pull/4187) on kind, but selecting a cluster via `/enter_cluster/...` fails:感谢开发这个功能，我也对此感到非常兴奋。我能够按照 [#4187](https://github.com/ray-project/kuberay/pull/4187) 上的 Dockerfile 和说明在 kind 上构建并启动历史服务器，但通过 `/enter_cluster/...` 选择集群时失败了： `could not read HTML file` I can see in the local minio bucket the session logs - might be just a case of routing. Any suggestions for building and utilizing?我可以在本地 minio 存储桶中看到会话日志——可能只是路由问题。对于构建和使用有什么建议吗？

Maybe you should run `npm ci && npm build` firstly under `historyserver/dashboard/v2.51.0/client` to package the dashboard. Or just set `BUILD_RAYSERVER_DASHBOARD` to yes when build history server image.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### KunWuLuan · 2026-09-23

Closing this epic as delivered. The History Server graduated to beta in KubeRay v1.7.0, with `historyserver`/`collector` images published to quay.io. The core work landed via #4241 (collector implementation), #4821 (QPS/burst flags), #4874 (disk-first event storage), and #5156 (OSS deployment samples). Remaining follow-ups (#5086, #5202, #5204, #5207) are tracked in their own PRs. Thanks everyone for the feedback along the way.
