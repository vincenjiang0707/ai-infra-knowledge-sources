# [Issue #145] Smarter units for bandwidths

source: https://github.com/ROCm/rocprofiler-compute/issues/145
state: closed | updated: 2025-08-06T18:41:00Z
labels: enhancement, metric definition

## 正文

It would be nice if we could get units for bandwidth values that scale with the size.  E.g., if we have > a GB/s, label it GB/s, or MB/s or KB/s, etc.

Not sure how possible this actually is in the current design, but would improve readability significantly.

cc: @feizheng10 

## 评论 (3)

### feizheng10 · 2023-07-19

Yes,  technically it is not hard to do for single run...a bit tricky for multiple runs with comparison.
I would suggest to do on tty/gui level.  

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/84

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
