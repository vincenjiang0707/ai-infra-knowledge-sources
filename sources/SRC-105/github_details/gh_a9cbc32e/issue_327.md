# [Issue #327] Allow not profiling a specific "troublesome" kernel

source: https://github.com/ROCm/rocprofiler-compute/issues/327
state: closed | updated: 2025-08-06T18:30:37Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
Some users have knowingly "troublesome" kernels that can trip up omniperf. It would be nice to temporarily avoid these kernels during profiling, essentially kernel filtering *out* rather than *in* certain kernels. This may partially work with `-k` regex's for `omniperf profile` but it seems all kernels are being profiled with and without `-k` (see #325 ). 

**Describe the solution you'd like**
For excluding only kernel `ABC`, I'd like to do a exclude regex like `-k "(?!^ABC$)"` or something similar.

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/62

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
