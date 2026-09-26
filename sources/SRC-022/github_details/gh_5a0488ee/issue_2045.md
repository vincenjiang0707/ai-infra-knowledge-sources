# [Issue #2045] [Issue]: ProxyTrace broken, DONE counter never set

source: https://github.com/ROCm/rccl/issues/2045
state: closed | updated: 2025-12-16T17:15:56Z
labels: status: triage

## 正文

### Problem Description

The call to mark proxy operations as complete for the ProxyTrace was deleted in src/transport/net.cc in this commit:
https://github.com/ROCm/rccl/pull/1880/commits/08a7be231b2adece49b4ff742e271d50a68343fe#diff-21f67af679373b33829eeb475f28de6be29c5fad2e757719c52d89fd49bbc177L1811

Now, the operations are never marked as completed or added to ProxyTrace::finishedOps. This leads to inaccurate trace contents. Can we revert this change?

### Operating System

Not relevant

### CPU

Not relevant

### GPU

Not relevant

### ROCm Version

Not relevant

### ROCm Component

rccl

### Steps to Reproduce

You can add a log like this in ProxyTrace::checkOpCompleted()
```
    WARN(
        "[dbg] posted %i, trans %i, flush %i, done %i",
        traceOp.counters[facebook_rccl::ProxyCounterTypes::POSTED],
        traceOp.counters[facebook_rccl::ProxyCounterTypes::TRANSMITTED],
        traceOp.counters[facebook_rccl::ProxyCounterTypes::FLUSHED],
        traceOp.counters[facebook_rccl::ProxyCounterTypes::DONE]);
```
The output logs will show that all the done counter are set to 0 because they are never updated.
```
[1] /data/users/ahmedkkhan/rccl/build/release/hipify/src/misc/proxy_trace/proxy_trace.cc:67 NCCL WARN [dbg] posted 148, trans 140, flush 0, done 0
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### isaki001 · 2025-11-13

We have a PR open for this https://github.com/ROCm/rccl/pull/2052

### huanrwan-amd · 2025-12-16

Close as fixed 
