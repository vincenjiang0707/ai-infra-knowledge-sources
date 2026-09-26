# [Issue #4387] [Feature][history server] support endpoint `/api/v0/logs/file`

source: https://github.com/ray-project/kuberay/issues/4387
state: open | updated: 2026-09-22T16:58:06Z
labels: stale

## 正文

(empty)

## 评论 (4)

### Future-Outlier · 2026-01-13

Hi, @machichima do you want to work on this?

### machichima · 2026-01-26

TODOs:

1. Use for loop in e2e test to cover all different cases (usage of different parameters). Like following

```go
var logFileTestCases = []struct {
    name           string
    buildURL       func(baseURL, nodeID string) string
    expectedStatus int
    checkBody      bool
}{
    // normal request
    {"lines=100", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out&lines=100", u, n) }, 200, true},
    {"lines=0 (default 1000)", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out", u, n) }, 200, true},
    {"lines=-1 (all)", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out&lines=-1", u, n) }, 200, true},
    {"lines=MAX (10000)", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out&lines=10000", u, n) }, 200, true},
    {"lines>MAX (capped)", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out&lines=99999", u, n) }, 200, true},
    
    // missing parameter
    {"missing node_id", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?filename=raylet.out", u) }, 400, false},
    {"missing filename", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s", u, n) }, 400, false},
    {"missing both", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file", u) }, 400, false},
    
    // invalid parameter
    {"invalid lines (string)", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=raylet.out&lines=abc", u, n) }, 400, false},
    {"file not found", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=nonexistent.log", u, n) }, 404, false},
    
    // Path traversal attack
    {"traversal ../etc/passwd", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=../etc/passwd", u, n) }, 400, false},
    {"traversal ..", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=..", u, n) }, 400, false},
    {"traversal /etc/passwd", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=%s&filename=/etc/passwd", u, n) }, 400, false},
    {"traversal in node_id", func(u, n string) string { return fmt.Sprintf("%s/api/v0/logs/file?node_id=../evil&filename=raylet.out", u) }, 400, false},
}
```

2. Support other parameters in dead cluster listed in: https://github.com/ray-project/kuberay/pull/4411#issue-3826219749
    1. Support `timeout, attempt_numbe, download_file, filter_ansi_c, interval(stream)` in dead cluster
    2. Support `node_ip, actor_id, task_id, pid, suffix, submission_id` in both live and dead cluster

### machichima · 2026-03-03

List of supported/not supported parameters in history server:

`/api/v0/logs`
- `node_id` ✅
- `glob` ✅
- `node_ip` ❌  (not used in Ray Dashboard frontend, see [here](https://github.com/ray-project/ray/blob/a37db563f2ca0f2bff34365381c76960f0900ec2/python/ray/dashboard/client/src/service/log.ts#L102-L102), only called with `node_id` [here](https://github.com/ray-project/ray/blob/a37db563f2ca0f2bff34365381c76960f0900ec2/python/ray/dashboard/client/src/pages/log/Logs.tsx#L146-L146))
- `timeout` ❌ (not used in Ray Dashboard frontend, see [here](https://github.com/ray-project/ray/blob/a37db563f2ca0f2bff34365381c76960f0900ec2/python/ray/dashboard/client/src/service/log.ts#L102-L102))

`/api/v0/logs/{media_type}`
- `media_type` (path) ✅ (`file` / `stream`)
- `node_id` ✅
- `node_ip` ✅
- `filename` ✅
- `task_id` ✅
- `actor_id` ✅
- `pid` ✅
- `suffix` ✅
- `lines` ✅
- `timeout` ❌ PR ongoing (not used in Ray Dashboard frontend, see [here](https://github.com/ray-project/ray/blob/a37db563f2ca0f2bff34365381c76960f0900ec2/python/ray/dashboard/client/src/service/log.ts#L49-L49))
- `attempt_number` ✅
- `download_filename` ✅
- `filter_ansi_code` ✅
- `interval` ✅ (for `stream`; effective in live-cluster proxy mode)
- `submission_id` ❌: do not need this https://github.com/ray-project/kuberay/blob/a6eb28b177d44b6ca1cb0c0dce24324b2a0643f2/historyserver/pkg/historyserver/router.go#L144-L147

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
