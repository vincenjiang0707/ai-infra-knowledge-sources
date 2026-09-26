# [Issue #28] Support autoscaled prefill/decode servers

source: https://github.com/LLMServe/DistServe/issues/28
state: closed | updated: 2024-08-08T04:03:44Z
labels: 

## 正文

When prefill servers are more loaded than decode, we need to adjust the ratio between decode and prefill servers. Is it possible to use distServe to achieve this mechanism?

## 评论 (1)

### interestingLSY · 2024-08-08

It is possible to do so, but it is not implemented in DistServe.
