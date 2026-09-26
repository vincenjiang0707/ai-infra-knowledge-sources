# [Issue #171] Use the rocprofiler API interface instead

source: https://github.com/ROCm/rocprofiler-compute/issues/171
state: closed | updated: 2025-08-06T18:39:56Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Use the rocprofiler API interface instead of doing \<rocprof run foo>

**Justification**
The idea here is that we can be _way_ more selective about which kernels we want to profile.  For instance, we could give the users the mode to (attempt) to **not replay** the application at all, by e.g., cycling through various sets of counters to collect for successive launches of the 'same' kernel.  This lines up with some of the stuff we've talking about internally re: kernel selection / cutting down replays.

**Implementation**
- Hook into rocprofiler API such that we can cycle through selection of counter sets per instance of the same kernel to reduce need for replay, probably an opt-in mode

_Originally posted by @arghdos in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6503094_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/80

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
