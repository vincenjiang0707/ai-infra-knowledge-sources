# [Issue #4280] [history server][collector] Migrate to new AWS S3 SDK version

source: https://github.com/ray-project/kuberay/issues/4280
state: open | updated: 2026-09-22T16:57:35Z
labels: stale

## 正文

The current implementation uses a deprecated version of the AWS S3 SDK.
Need to update to the latest version.
If possible, please test at both minio and aws.

## 评论 (5)

### 400Ping · 2025-12-17

May I take this?

### my-vegetable-has-exploded · 2025-12-17

Btw, maybe we could consider using [OpenDAL](https://opendal.apache.org/bindings/go/) here？

### Future-Outlier · 2025-12-17

Hi, @my-vegetable-has-exploded 
what's the benefit of using [OpenDAL](https://opendal.apache.org/bindings/go/) here？

### dentiny · 2025-12-17

> Btw, maybe we could consider using [OpenDAL](https://opendal.apache.org/bindings/go/) here？

Curious what's the benefit of using a FFI here?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
