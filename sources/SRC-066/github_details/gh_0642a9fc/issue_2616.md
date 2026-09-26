# [Issue #2616] [BUG] Cutlass Profiler not working

source: https://github.com/NVIDIA/cutlass/issues/2616
state: closed | updated: 2026-09-02T16:54:36Z
labels: bug, ? - Needs Triage, inactive-30d, CUTLASS C++

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

Hi, I am using H100 to profile gemm by using cutlass_profiler. But nothing comes out here are the steps.
1. clone cutlass and install it by
`cmake .. -DCUTLASS_NVCC_ARCHS=90a -DCUTLASS_LIBRARY_KERNELS=ALL -DCUTLASS_LIBRARY_OPERATIONS=gemm -DCMAKE_BUILD_TYPE=Release`
2. install cutlass_profiler
`make -j 32 cutlass_profiler`
3. execute
Then I execute cutlass_profiler, and nothing comes out.

<img width="750" height="48" alt="Image" src="https://github.com/user-attachments/assets/3305d54a-b15e-406d-a114-c4909ab2c616" />

## 评论 (3)

### github-actions[bot] · 2025-10-04

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-01-02

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### Junkai-Wu · 2026-01-20

@HaoKang-Timmy Sorry for the late response. First of all, please check the file `tools/library/generated_kernels.txt` under build folder to see whether there are kernels generated. If yes, you can try to add some more command line options to narrow down the kernel scope, detailed usage please refer to https://github.com/NVIDIA/cutlass/blob/main/media/docs/cpp/profiler.md 
