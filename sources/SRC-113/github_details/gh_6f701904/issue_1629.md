# [Issue #1629] Reintroducing min_query_count for SingleStream (64) and Server (662)

source: https://github.com/mlcommons/inference/issues/1629
state: closed | updated: 2026-05-07T00:40:05Z
labels: Stale

## 正文

The minimum query count (`min_query_count`) was [removed](https://github.com/mlcommons/inference/commit/995ffee37682a0870f359bb00d5f4672d78d6424) from `mlperf.conf` a while ago. I believe the thinking was that submitters could choose how many samples to process. As long as the minimum run duration (`min_duration`) constraint of 10 minutes was met, early stopping would take care of estimating the 90th percentile for SingleStream, and the 99th percentile for MultiStream and Server.

However, for SingleStream early stopping still requires at least 64 samples to estimate the 90th percentile. Similarly, for MultiStream early stopping requires at least 662 samples to estimate the 99th percentile. So trying to process less than 64 samples for SingleStream and 662 queries for Server will result in `INVALID` runs.

Perhaps it would be better to reintroduce these constraints to match [the one for MultiStream](https://github.com/mlcommons/inference/blob/486a629ea4d5c5150f452d0b0a196bf71fd2021e/mlperf.conf#L37):
```
*.MultiStream.min_query_count = 662
```

## 评论 (2)

### arjunsuresh · 2024-02-20

yes, it'll be good to make loadgen generate minimum that many queries, right?

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
