# [Issue #4382] [Feature][history server] support endpoint `/api/grafana_health`

source: https://github.com/ray-project/kuberay/issues/4382
state: open | updated: 2026-09-22T16:58:00Z
labels: stale

## 正文

(empty)

## 评论 (9)

### Future-Outlier · 2026-01-13

Hi, @fscnick  do you want to try this?

### Future-Outlier · 2026-01-14

cc @fscnick 

### fscnick · 2026-01-14

Yes, I'd like to help.

### KunWuLuan · 2026-01-14

We add a sidecar to provide grafana. The grafana will use Aliyun Arms Prometheus as the datasource. The datasource can be configured to use any metrics service, either from Cloud Provider or Self Built.

### KunWuLuan · 2026-01-14

We are glad to share the configuration if needed.

### Future-Outlier · 2026-01-14

Hi, @KunWuLuan yes plz share the configuration without any confidential information

### Future-Outlier · 2026-01-15

Hi, @fscnick 
you can support live cluster first, for dead cluster, we can do it later

### fscnick · 2026-01-15

> Hi, [@fscnick](https://github.com/fscnick) you can support live cluster first, for dead cluster, we can do it later

Got it.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
