# [Issue #2756] [QST] About Example 23: Ampere GEMM Operand Reduction Fusion with kGemmSplitKParallel

source: https://github.com/NVIDIA/cutlass/issues/2756
state: closed | updated: 2026-09-07T17:09:15Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

I’m checking out Example 23 and found a thing when using kGemmSplitKParallel mode; I’d like to get this cleared up:

In this mode, the example explicitly allocates a block of workspace memory as part of its setup. However, when the GEMM kernel actually executes, this pre-allocated workspace is not being utilized—there are no read or write operations to it during kernel runtime.

 I’m not sure if I’ve missed any conditions that would explain why I can’t detect the usage of this workspace.

## 评论 (3)

### kitecats · 2025-11-07

When I run this example, I also fail to get the correct result:
```
./example23 --split-k-slices=2 --parallel-split-k
ERROR - results miscompared.
ID,M,N,K,SplitK-Slices,Parallel-SplitK,Runtime
gemm_1,1024,1024,1024,2,1,0
```

### github-actions[bot] · 2025-12-07

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-07

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
