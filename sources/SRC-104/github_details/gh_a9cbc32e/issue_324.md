# [Issue #324] --list-metrics requires a workload directory be specified

source: https://github.com/ROCm/rocprofiler-compute/issues/324
state: closed | updated: 2025-08-06T18:30:54Z
labels: bug

## 正文

**Describe the bug**
`omniperf analyze --list-metrics gfx90a` does not list the metrics for gfx90a because the command is missing a workloads directory, but the workloads directory doesn't seem to be required for any output.

**Development Environment:**
 - Linux Distribution: 
 - Omniperf Version: 2.x
 - GPU: Mi200
 - Custer (if applicable): 

**To Reproduce**
Try `omniperf analyze --list-metrics <arch>`

**Expected behavior**
Should show the metrics relevant to <arch>


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/63

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
