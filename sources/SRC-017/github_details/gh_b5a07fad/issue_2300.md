# [Issue #2300] [RFE]: Profiler API-events eDescr report incorrect rank (always 0)

source: https://github.com/NVIDIA/nccl/issues/2300
state: closed | updated: 2026-08-25T06:30:09Z
labels: enhancement

## 正文

### What is the goal of this request?
Fixes a bug in the profiler plugin API:

In multi-GPU communicator setups, profiler API events (groupApi/p2pApi/collApi/kernelLaunch) report eDescr.rank=0 for all ranks:

The bug is in src/plugin/profiler.cc:
- ncclProfilerStartGroupApiEvent() [line ~275]
- ncclProfilerStartP2pApiEvent() [line ~316]
- ncclProfilerStartCollApiEvent() [line ~346]
- ncclProfilerStartKernelLaunchEvent() [line ~384]

All of these initialize eDescr to {0} and never set eDescr.rank, leaving it at 0 for all ranks. However, the comm/plan context is available and contains the correct rank (comm->rank or plan->comm->rank) - other profiler events correctly set eDescr.rank.

**Steps to Reproduce:**

Set up a multi-GPU communicator with `ncclCommInitAll()`
Enable profiler tracing with v5/v6 API events
Run a collective operation
Examine profiler output; all ranks show eDescr.rank=0 instead of differentiating by rank
**Expected:** eDescr.rank should match comm->rank for each rank 

**Actual:** eDescr.rank is always 0

**Suggested fix:** Set eDescr.rank = `comm->rank` (or `plan->comm->rank`) in each of the four functions above, matching the pattern used by the other types of events



### Who will benefit from this feature?
custom profilers will not accidently report wrong values

### Is this request for a specific GPU architecture or network infrastructure?
no 

### What is the priority level of this request?
low? it does not impact performance, and a workaround exists.



## 评论 (2)

### Wahid612 · 2026-07-30

@pha-Z Thanks for reporting this and we can effectively repro. The fix will be in upcoming releases.

### Wahid612 · 2026-08-25

Fixed in [94a66251](https://github.com/NVIDIA/nccl/commit/94a66251adbb9751ef5e4b031221d50c3af5dd51). The profiler now reports the originating communicator rank for group API, P2P API, collective API, and kernel launch events. Thanks for reporting this.
