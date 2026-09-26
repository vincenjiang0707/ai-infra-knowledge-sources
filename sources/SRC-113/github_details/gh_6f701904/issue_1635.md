# [Issue #1635] How to handle failed requests(5XX) of an online inference service?

source: https://github.com/mlcommons/inference/issues/1635
state: closed | updated: 2026-05-07T00:39:57Z
labels: Stale

## 正文

When I want to test an online inference service by POST requests, it is necessary to record all response, because of [this](https://github.com/mlcommons/inference/blob/268bc9dc8a3c0a96bbb7d38482c0ce5016507633/loadgen/logging.h#L398)

However, if the response's status code is not 200, recording this response and calculating latency based on it would be inaccurate, because of [this](https://github.com/mlcommons/inference/blob/268bc9dc8a3c0a96bbb7d38482c0ce5016507633/loadgen/results.cc#L406). Moreover, using this approach to find peak performance would not yield the optimal QPS. 

Is there any support or recommended approach for handling this scenario?

## 评论 (1)

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
