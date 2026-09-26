# [Issue #4283] [history server][collector] Make sure collector has no go routine leak

source: https://github.com/ray-project/kuberay/issues/4283
state: open | updated: 2026-09-22T16:57:37Z
labels: stale

## 正文

As title.

## 评论 (6)

### fscnick · 2025-12-17

Hi @Future-Outlier , I'd like to help with this issue.

### fscnick · 2026-01-10

There is a potential goroutine leak in some extreme situation. 
https://github.com/ray-project/kuberay/blob/fc6f1628ea2e79abf58cbe0a40d8ead1e0b1a362/historyserver/pkg/collector/logcollector/runtime/logcollector/collector.go#L485

At the collector starts, it walk through `/tmp/ray/prev-logs/` and creates goroutines as many as `{sessionid}/{nodeid}` under `/tmp/ray/prev-logs/`. If the `/tmp/ray` is not mounted on an ephemeral storage and it accumulates lots of `{sessionid}/{nodeid}` unprocessed. It would have many goroutines to upload the logs.

However, it is not that easy to happen. Once the collector starts to process `/tmp/ray/prev-logs/` and finds `{sessionid}/{nodeid}` under `/tmp/ray/prev-logs/`, it starts to uploading and creates directory `/tmp/ray/persist-complete-logs/{sessionid}/{nodeid}` after a file finished uploading to mark as completed. 

reproduce:
- Follow [set_up_collector.md](https://github.com/ray-project/kuberay/blob/master/historyserver/docs/set_up_collector.md) and mount `/tmp/ray/` on a persistent storage, but don't setup MinIO. (simulate network issue to the storage server.)
- Run `kubectl apply -f historyserver/config/raycluster.yaml` and `kubectl delete -f historyserver/config/raycluster.yaml` many times. It will accumulate `{sessionid}/{nodeid}`  under `/tmp/ray/prev-logs/`. (simulate to do some operations to figure it out)
- Bring the MinIO back (simulate the network issue resolved) and run `kubectl apply -f historyserver/config/raycluster.yaml` again. It will create goroutines as many as `{sessionid}/{nodeid}` under `/tmp/ray/prev-logs/`. 

### Future-Outlier · 2026-01-14

nice explanation!
do you mind create a PR to create worker pool?
cc @fscnick 

### Future-Outlier · 2026-01-14

I think this is not urgent, we can deal with it in beta

### fscnick · 2026-01-14

> nice explanation! do you mind create a PR to create worker pool? cc [@fscnick](https://github.com/fscnick)

Sure, let's do it in beta.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
