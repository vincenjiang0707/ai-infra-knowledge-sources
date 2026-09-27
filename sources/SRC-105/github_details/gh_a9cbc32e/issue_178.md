# [Issue #178] Add embedded performance profiling capability.

source: https://github.com/ROCm/rocprofiler-compute/issues/178
state: closed | updated: 2025-08-06T18:38:39Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Add embedded performance profiling capability.

**Justification**
Optional capability to enable reporting of execution time required across major functions within OmniPerf . Useful for ongoing development optimization and performance regression detection.

**Implementation**
Include a timer class that can be used to demarcate start/stop for regions of interest and aggregate wall-clock execution.

**Additional Notes**
Integrate with logger option mentioned above or have separate command-line argument to enable.

_Originally posted by @koomie in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6630057_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/77

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
