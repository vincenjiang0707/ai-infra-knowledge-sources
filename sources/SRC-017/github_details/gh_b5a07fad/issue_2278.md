# [Issue #2278] [RFE]: Broadcast does not emit ncclProfileColl profiler events when NCCL_ALLGATHERV_ENABLE=1

source: https://github.com/NVIDIA/nccl/issues/2278
state: closed | updated: 2026-07-28T04:19:55Z
labels: enhancement

## 正文

### Please provide the below details to ensure we understand your needs

## Summary

When NCCL_ALLGATHERV_ENABLE is enabled, ncclBroadcast can be routed through the special ncclTaskBcast / AllGatherV scheduling path instead of the normal ncclTaskColl path. In this path, the operation may still trigger collective transport connection setup, but it does not emit a corresponding ncclProfileColl task event to the profiler plugin.

As a result, profiler plugins that rely on ncclProfileColl miss Broadcast task-level statistics, even though the Broadcast operation is actually executed.

## Environment

- NCCL_ALLGATHERV_ENABLE=1 or default enabled
- Test: broadcast_perf
- Profiler plugin enabled with ncclProfileColl
Observed Behavior

With broadcast_perf , the profiler does not receive ncclProfileColl events for Broadcast in the AllGatherV-enabled path. However, collective transport connectors can still be established, so connection-related state may indicate collective channels are connected while profiler task counters remain zero.

## Expected Behavior

A user-level ncclBroadcast should emit a Broadcast ncclProfileColl event regardless of whether NCCL internally schedules it through the normal collective path or the special AllGatherV/Bcast path.

Internal AllGatherV implementation details should not need to be exposed as user-visible collective events, but the original user operation should still be reported as Broadcast .

## Root Cause

In src/enqueue.cc , when this condition is true:

NCCL creates an ncclTaskBcast and enqueues it into planner->peers[root].bcastQueue instead of creating a normal ncclTaskColl .

Later, ncclProfilerStartTaskEvents() in src/plugin/profiler.cc only iterates:

```
plan->collTaskQueue
plan->p2pTaskQueue
```
It does not iterate plan->bcastTaskQueue , so no ncclProfileColl event is emitted for those Broadcast tasks.

Additionally, the special AllGatherV scheduler uses:

```
proxyOp.eActivationMask = 0;
```
so the internal path also does not emit proxy/kernel profiler events.

## Impact

Profiler plugins cannot correctly account for Broadcast operations when the AllGatherV optimization path is used. This causes missing task-level metrics such as operation count, protocol distribution, and channel utilization for Broadcast.

## 评论 (2)

### xiaofanl-nvidia · 2026-07-19

I think this is a known issue. We didn't add the profiler support for optimized allgatherv path yet.. 
@jynv can you confirm and track this for the next release to begin with? Let's scope it out.. 

### jynv · 2026-07-20

Confirmed, it's an known issue that has been tracked. We are working on adding support for profiler in allgatherv path.
