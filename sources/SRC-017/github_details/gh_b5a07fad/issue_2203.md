# [Issue #2203] [Issue]: NCCL-GIN hang during the initial AllGather

source: https://github.com/NVIDIA/nccl/issues/2203
state: closed | updated: 2026-08-14T23:05:42Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs

During GIN initialization (when `ncclGinIbAllGather` is called), if the CTS message is dropped (e.g., due to transport timeout),  [`srequest == NULL`](https://github.com/NVIDIA/nccl/blob/e80ce32bdd9de1c37dd9c1e4485bb326829ead25/src/transport/net_ib/gin.cc#L150) will stay true so it will not reach `ncclNetIb.test`.

Also, `GinIbAllGather` issues RDMA hairpin operations for intra-host ring neighbors, is it possible to provide an option similar to `bootstrapAllGather` where it can fallback to TCP/IP (for environments lacking RDMA hairpin capabilities causing the hang issue above)?

### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.30.4

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (6)

### xiaofanl-nvidia · 2026-06-07

++ @kgioioso @pakmarkthub to review and consider the suggestion. CC @sjeaugey 

### kgioioso · 2026-06-08

Hi @sheepx86 , Thanks for the report. I have some follow up questions:

> if the CTS message is dropped (e.g., due to transport timeout), [srequest == NULL](https://github.com/NVIDIA/nccl/blob/e80ce32bdd9de1c37dd9c1e4485bb326829ead25/src/transport/net_ib/gin.cc#L150) will stay true

Are you seeing this issue in a non-failure case as well? Or is this a suggestion for better error handling? We do not usually consider transport timeouts to be recoverable.

> Also, GinIbAllGather issues RDMA hairpin operations for intra-host ring neighbors

It sounds like you do not have cross-rail loopback connections (e.g. rank 0 on host 0 can connect to rank 1 on host 1, but cannot connect to rank 1 on host 0). Is my understanding correct? 

If so, I recommend you set `NCCL_CROSS_NIC=0`. GIN does not distinguish cross-rail loopback connections from other cross-rail connections and thus `NCCL_CROSS_NIC=0` must be set. We are aware this is a limitation and are considering fixes, but it's not as simple as adding a `bootstrapAllGather` fallback. Even after GIN is initialized, user applications may use GIN to communicate among ranks on the same host.

### sheepx86 · 2026-06-08

> Are you seeing this issue in a non-failure case as well? Or is this a suggestion for better error handling?

This is a suggestion of better error handling, instead of hang it should timeout (basically run `ncclNetIb.test` within the first while loop)

> It sounds like you do not have cross-rail loopback connections (e.g. rank 0 on host 0 can connect to rank 1 on host 1, but cannot connect to rank 1 on host 0). Is my understanding correct?

That's correct.
Understood that unlike host API can work with CROSS_NIC=1 in the above scenario, two ranks can fail on the same host can fail with the device API + GIN. 

### kgioioso · 2026-06-11

/mirror

### kgioioso · 2026-08-04

Hi @sheepx86 , this came up again in PR #2318 . I added a few more clarification questions there. Feel free to chime in or follow the thread.

### sheepx86 · 2026-08-14

Yes I think this is the same issue. I agree checking for CQE is better than adding another timeout.
