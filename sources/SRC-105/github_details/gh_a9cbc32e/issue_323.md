# [Issue #323] Add a batch mode that parallelizes counter collection over multiple identical GPUs

source: https://github.com/ROCm/rocprofiler-compute/issues/323
state: closed | updated: 2025-08-06T18:32:52Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
This feature is related to benchmarks that may not be able to be cut down to a smaller representative problem. Collecting counters in parallel would significantly cut down the profile time.

**Describe the solution you'd like**
An argument to `omniperf profile` that allows running several counter collections at a time across multiple identical GPUs

**Describe alternatives you've considered**

**Additional context**
Suggested by Shane Fogerty at the SNL hackathon


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/64

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
