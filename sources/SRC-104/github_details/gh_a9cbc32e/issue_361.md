# [Issue #361] Baseline comparison with multiple kernels doesn't 'select' multiple kernels in table 0

source: https://github.com/ROCm/rocprofiler-compute/issues/361
state: closed | updated: 2025-08-06T18:29:05Z
labels: bug

## 正文

**Describe the bug**

E.g., if you try to compare two kernels from two different runs:

```
omniperf analyze -p workloads/stream/MI300A_A1/ -k 0 -p workloads/stream-copy/MI300A_A1/ -k 1 <...>
```

only the first kernel supplied is 'selected':

![image](https://github.com/ROCm/omniperf/assets/6463881/cb0e3ee8-e91c-4897-a5eb-534da2b28398)

Minor issue at best, but I typically check this to ensure I'm analyzing the right kernels.

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/56

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
