# [Issue #330] Add Checkpointing to profiling to save profiling progress

source: https://github.com/ROCm/rocprofiler-compute/issues/330
state: closed | updated: 2025-08-06T18:30:08Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
Heavy weight benchmarks that take a significant time to profile may be cut short by time limits on scheduled systems, resulting in losing all profiling data

**Describe the solution you'd like**
Add a feature that checkpoints profiling progress when an omniperf run gets interrupted, which will save time when resuming a profile.

**Describe alternatives you've considered**
Running several filtered profile runs on IP blocks _could_ emulate this feature, but has significant manual overhead for users. Ideally checkpointing would happen transparently


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/60

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
