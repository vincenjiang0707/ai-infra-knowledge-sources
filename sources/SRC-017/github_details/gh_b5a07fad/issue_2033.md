# [Issue #2033] [Issue]: CPU affinity is not restored at the end of `initTransportsRank()` (introduced in 2.29.2-1)

source: https://github.com/NVIDIA/nccl/issues/2033
state: closed | updated: 2026-09-19T01:42:58Z
labels: 

## 正文

### NCCL Version

2.29.2-1-2.29.7-1

### Error Description

Hi NCCL Team!

We found a bug in NCCL that was introduced in the **2.29.2-1** Release:
https://github.com/NVIDIA/nccl/commit/ebd1e929285881cb4df02c3459588a2e12b2d8c0

At the end of `initTransportsRank()`, NCCL should restore the original CPU affinity saved in `affinitySave`. In an earlier version, it did:
https://github.com/NVIDIA/nccl/blob/dbc86fd06e8b0c4517b95d8958a09ccacf9520c9/src/init.cc#L1395

In 2.29.2-1 this was replaced with:
https://github.com/NVIDIA/nccl/blob/ebd1e929285881cb4df02c3459588a2e12b2d8c0/src/init.cc#L1465

This change re-applies the temporary `comm->cpuAffinity` instead of restoring `affinitySave`. As a result, the temporary CPU affinity leaks into the current thread and remains in effect after `initTransportsRank()` returns.

## 评论 (3)

### AddyLaddy · 2026-03-04

Thanks for reporting this. We'll aim to fix it in the next NCCL release.

### xiaofanl-nvidia · 2026-03-06

This has been merged in the next release (2.30). 

### albertz · 2026-09-19

Just a note:

Fixing this issue here is probably the correct thing to do. But having this fixed can cause unexpected slowdown of trainings, because the CPU affinity was actually helpful.

For me, training slowed after upgrading from NCCL 2.29.7 to 2.30.7. Version 2.29.7 unintentionally retained GPU-local CPU affinity as explained here, so our old setup needed no explicit binding. Now this issue here being fixed in 2.30.3, we must do the CPU binding explicitly, via `/sys/bus/pci/devices/<PCI-address>/local_cpulist` (PCI-address of the GPU).

A controlled four-node, 32-GPU replay with NCCL 2.30.7 showed:

| Metric | Without explicit binding | With explicit binding |
|---|---:|---:|
| Median loader state-snapshot CPU time | 163 ms | 90 ms |
| Mean worker batch-fetch CPU time | 871 ms | 609 ms |
| Mean major garbage-collection pause | 2.76 s | 1.75 s |
| Steps with batch-fetch waits >100 ms | 7 / 250 | 2 / 250 |
| Training speed | ~4,720 steps/h | 5,450–5,625 steps/h |

(cc @pzelasko)
