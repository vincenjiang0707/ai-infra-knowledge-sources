# [Issue #2763] [QST] CuTeDSL should drop cuda.stream when creating mangle name.

source: https://github.com/NVIDIA/cutlass/issues/2763
state: closed | updated: 2026-09-18T16:37:05Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**What is your question?**
Hi everyone, I modified the example to JIT mode, i.e., `gemm(mA, mB, mC, stream)`, but observed cache missing among different processes. 

In fact, stream is only used in kernel launch, and does not affect the compilation. Adding it as a placeholder in mangle name might help. 

Do you have any suggestions? Thanks!

http://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/examples/python/CuTeDSL/hopper/dense_gemm.py#L381

http://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/python/CuTeDSL/cutlass/base_dsl/dsl.py#L555

Furthermore, could you kindly expose the `mangle_name` API so that users could check if they need re-compilation (i.e., the AoT)? 

## 评论 (2)

### github-actions[bot] · 2025-12-18

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-18

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
