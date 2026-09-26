# [Issue #27] 分离部署多个prefill实例与多个decode实例支持问题

source: https://github.com/LLMServe/DistServe/issues/27
state: closed | updated: 2024-08-12T22:19:07Z
labels: 

## 正文

请问当前distserve的实现，支持多个prefill实例与多个decode实例一起进行分离部署推理吗？

## 评论 (1)

### interestingLSY · 2024-08-12

Currently we do not support that. In the current implementation of DistServe, there is only one prefill instance and one decoding instance. While it should be possible to have multiple instances, we did not implement that.
