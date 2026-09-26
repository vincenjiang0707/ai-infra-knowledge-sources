# [Issue #170] Add MPI awareness to Omniperf

source: https://github.com/ROCm/rocprofiler-compute/issues/170
state: closed | updated: 2025-08-06T18:40:13Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Add MPI awareness to Omniperf

**Justification**
Adding MPI awareness is something we've been meaning to address and is highly requested by users.  If Omniperf is MPI aware we can also begin to implement some clever ways to reduce the computational load by distributed counter collection (multi gpu scenario).

We've been holding off on this because we wanted to do it right. This seems like an appropriate opportunity to tackle implementation.

**Implementation**

1. Brute force approach would be to run our (~14x app replays) on each node. The profiling side of this method is straightforward, but post-processing could introduce some issues.
2. Alternatively, we could split runs up across nodes, assuming the same kernels are being launched.

**Additional Notes**

- A potential gotcha to consider is the number of MPI ranks we advertise as being supported. Launching hundreds of ranks introduces data processing difficulties due to the raw amount of data generated

_Originally posted by @coleramos425 in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6502477_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/82

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
