# [Issue #174] Build SMI-sampling to get more accurate clock rates

source: https://github.com/ROCm/rocprofiler-compute/issues/174
state: closed | updated: 2025-08-06T18:39:27Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Build SMI-sampling to get more accurate clock rates

**Justification**
see here: https://github.com/AMDResearch/omniperf/issues/149#issuecomment-1652360211.  Basically, we'd ideally want a good average of clock rates from the profiler for each kernel.  Note that 'other' profilers give the ability to either control the clock rate (subject to throttling) or actively _report_ the number of clocks elapsed in various time domains.

**Implementation**
It can be as simple as spinning up a background thread to sample the clock rate during the app, but a more robust version would be able to assign clocks to specific kernels (e.g., if we control rocprofiler directly as well).  We might also ask for enhanced rocprofiler support.

**Additional Notes**
We might also be able to do this by using (EndNs - BeginNs) / GRBM_GUI_ACTIVE to get an approximate clock rate?

_Originally posted by @arghdos in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6555273_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/81

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
