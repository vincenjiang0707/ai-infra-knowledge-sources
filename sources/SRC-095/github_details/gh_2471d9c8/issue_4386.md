# [Issue #4386] [Feature][history server] support endpoint `/api/v0/placement_groups/`

source: https://github.com/ray-project/kuberay/issues/4386
state: open | updated: 2026-09-22T16:58:04Z
labels: stale

## 正文

(empty)

## 评论 (5)

### Future-Outlier · 2026-01-13

Hi, @troychiu do you want to try this?

### popojk · 2026-01-17

Can I work on this one?

### Future-Outlier · 2026-01-17

> Can I work on this one?

sure! go for it

### popojk · 2026-01-21

Hi @Future-Outlier . Right now there is no event for placement groups in the [events list](https://github.com/ray-project/kuberay/blob/a9a4ab0a1cfdb32e89a3c7dda6572113dc0396d8/historyserver/pkg/eventserver/types/event.go#L6-L16). For implementing dead cluster behavior of this API, I'm wondering what is the expected behavior? Should we add placement groups event in ray so that the history server can collect them and return while under dead cluster scenario? Thanks 

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
