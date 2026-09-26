# [Issue #1405] computeColl never defined

source: https://github.com/ROCm/rccl/issues/1405
state: closed | updated: 2024-11-06T15:44:37Z
labels: Under Investigation

## 正文

This appears to be a leftover static declaration of computeColl(). Should it be removed?

https://github.com/ROCm/rccl/blob/develop/src/enqueue.cc#L46

## 评论 (2)

### ppanchad-amd · 2024-11-04

Hi @ryanhankins. Internal ticket has been created to assist with your issue. Thanks!

### darren-amd · 2024-11-06

Hi @ryanhankins,

Thanks for pointing that out, I have submitted a PR here with the fixes you highlighted: https://github.com/ROCm/rccl/pull/1406.
