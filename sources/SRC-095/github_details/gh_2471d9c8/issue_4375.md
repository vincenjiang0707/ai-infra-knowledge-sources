# [Issue #4375] [Feature][history server] Job Endpoint and Event Processing for Job

source: https://github.com/ray-project/kuberay/issues/4375
state: open | updated: 2026-09-22T16:57:56Z
labels: stale

## 正文

(empty)

## 评论 (4)

### Future-Outlier · 2026-01-13

will assign to @chiayi 

### chiayi · 2026-02-06

Reiterating followup from https://github.com/ray-project/kuberay/pull/4422#pullrequestreview-3709195613 
follow-up:

1. /api/jobs/{job_id}/logs endpoint for dead clusters
2. E2E tests for /api/jobs/ endpoint
3. after ray side support more fields in job's event, update endpoints for dead cluster.

### chiayi · 2026-02-24

Update https://github.com/ray-project/kuberay/issues/4375#issuecomment-3857266420: 
1. Is currently not in scope for alpha. 

Will work on adding e2e test for /api/jobs/ endpoint

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
