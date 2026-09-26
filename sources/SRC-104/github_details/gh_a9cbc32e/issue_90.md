# [Issue #90] Change Default Normal Unit to per_kernel

source: https://github.com/ROCm/rocprofiler-compute/issues/90
state: closed | updated: 2025-03-09T20:21:26Z
labels: Under Investigation

## 正文

As an application developer I think in terms of kernels rather than wave/wavefronts.
Per kernel is also the normalization used in nsight compute so using per kernel makes it easier to compare output with ncu which is one of my common use cases.

## 评论 (3)

### feizheng10 · 2023-02-16

Thanks for the suggestion. The mode "Per kernel comparison to ncu" is not "only" your case. We did put it in our plan. 

### sohaibnd · 2025-02-28

Hi @MrBurmark, sorry for the late follow-up. @feizheng10 has put in a change (https://github.com/ROCm/rocprofiler-compute/pull/555) to make the default normalization to be per kernel. Let me know if you have any other concerns.

### sohaibnd · 2025-03-09

Closing this issue as it is resolved. @MrBurmark Feel free to re-open the issue if you have any follow-up questions/concerns.
