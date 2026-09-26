# [Issue #1983] [Issue]:

source: https://github.com/NVIDIA/nccl/issues/1983
state: open | updated: 2026-09-06T19:12:00Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

ncclIbIsend is reading idx, nreqs from slot without any fencing. On architectures without load-acquire ordering, nreqs can be read before idx. As a result, we can use nreqs from an older request. 

### Steps to Reproduce the Issue

_No response_

### NCCL Version

master

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (3)

### sjeaugey · 2026-01-19

Thanks for the report. It sounds like this issue may cause more than a lower performance; it may cause crashes or data corruption. Is it the case?

Also, can you point to precise lines in the code, to make sure we're looking at the same issue and can confirm the problem?

### sjeaugey · 2026-01-19

To confirm, the problem is between those two lines, right?
https://github.com/NVIDIA/nccl/blob/master/src/transport/net_ib/p2p.cc#L190-L191

It seems like a legitimate concern indeed. `nreqs` being reset to zero every time, I'm not sure what would actually happen if we load nreqs = 0 instead of a new value.

It seems like this could be fixed by simply replacing:
```
   nreqs = slots[0].nreqs;
```
by:
```
  while ((nreqs = slots[0].nreqs) == 0);
```
Since `idx` was written, it's only a matter of time before nreqs is set to its correct value, which should be non-zero.

### kodlan · 2026-09-06

Created #2393  for this. It adds an acquire fence between the slots[0].idx check and the slots[0].nreqs load in ncclIbIsend so the the nreqs read cannot be satisfied before the idx read on weakly ordered CPUs.
