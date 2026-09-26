# [Issue #175] Better normalization modes over multiple kernels.

source: https://github.com/ROCm/rocprofiler-compute/issues/175
state: closed | updated: 2025-08-06T18:39:12Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**

Better normalization modes over multiple kernels.

**Justification**

In conversation with users, I have found that there is significant confusion over values that are presented when multiple kernels are selected for analysis.  In particular, folks ask questions like "why did my bandwidth go down when I executed <10x more kernels>"?
My feeling is that the way we present normalization over multiple kernels is flawed.

**Implementation**

Options include: 
  - universally take the same tact as the standalone GUI, and refuse to show details until the user has filtered to a specific kernel/dispatch (or group of them).  Basically, unless there's some filter flag, don't show any details?  I don't really love this, as it's a very weird UX to see only the kernel breakdown and not anything else, especially for existing users.
  - Use a _time_ based normalization over the included kernels, instead of a simple count based one.  That way, a user gets a more representative view of what the code was doing.  This can also be implemented along-side the last one
  - Make more options to let the user switch between these modes, but this requires docs and code maintenance.

_Originally posted by @arghdos in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6576521_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/79

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
