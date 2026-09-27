# [Issue #496] NCCL timeout while different ranks execute DeepEP and NCCL communications in different order

source: https://github.com/deepseek-ai/DeepEP/issues/496
state: open | updated: 2026-04-04T18:42:40Z
labels: 

## 正文

Reproduced code
```python
if rank % 2 == 0:
    with torch.cuda.stream(test_alt_stream):
        dist.all_gather_into_tensor(all_topk_idx, topk_idx, group=group)

buffer.low_latency_dispatch(current_x, topk_idx, num_tokens, num_experts,
                            use_fp8=dispatch_use_fp8, round_scale=round_scale, use_ue8m0=use_ue8m0,
                            cumulative_local_expert_recv_stats=cumulative_local_expert_recv_stats,
                            async_finish=not return_recv_hook, return_recv_hook=return_recv_hook)

if rank % 2 != 0:
    with torch.cuda.stream(test_alt_stream):
        dist.all_gather_into_tensor(all_topk_idx, topk_idx, group=group)
default_stream.wait_stream(test_alt_stream)
```
@sphish  mentioned in https://github.com/deepseek-ai/DeepEP/issues/414: ' If each rank executes DeepEP and NCCL communications in the same order, there should be no conflicts. ' What is the reason for this restriction?

## 评论 (7)

### sphish · 2025-11-17

DeepEP’s low-latency kernels use cooperative launch to attempt launching a large number of SMs simultaneously. If NCCL occupies some of the SMs, it may prevent DeepEP’s kernels from being launched, which could result in a deadlock.

### jiangjiang-coder66 · 2025-11-17

> DeepEP’s low-latency kernels use cooperative launch to attempt launching a large number of SMs simultaneously. If NCCL occupies some of the SMs, it may prevent DeepEP’s kernels from being launched, which could result in a deadlock.

@sphish Thanks for your reply. I set low-latency kernel just use 64 Blocks while NCCL uses 2 Blocks, timeout still occur. In case, I disabled the cluster feature by setting attr[1].val.clusterDim.x = 1. On the other hand, for each rank, ag is executed first, followed by deepEP. The torch profiler shows that ag and deepEP can be executed in parallel on the two streams. SM resources are a potential risk, but not the root cause of the current problem.

### jiangjiang-coder66 · 2025-11-18

A question about “If NCCL occupies some of the SMs, it may prevent DeepEP’s kernels from being launched“, Why can't deepEP wait for NCCL to finish？

### xiaofanl-nvidia · 2025-11-25

Hi @defei-coder can you confirm if both the allgather and low_latency_dispatch operations are collective operations for all ranks? 
I'm suspecting the above issue is simply caused by doing two collective operations in the wrong order. 

E.g. collective ops require all ranks to participate to make progress. If the even ranks doing allgather is waiting for odd ranks to participate, meanwhile odd ranks are doing another collective operations and waiting for even ranks, it would naturally deadlock.. 

Let me know if that makes sense.. It's a guess since I'm not super familiar with low_latency_dispatch yet. :) 

### jiangjiang-coder66 · 2025-12-02

Thaks for your reply @xiaofanl-nvidia . In my view, low_latency_dispatch differs from all_gather in that low_latency_dispatch accomplishes communication waiting through hook functions, eliminating the need for all ranks to execute simultaneously. @sphish @LyricZhao Can you help me answer this question?

> Hi [@defei-coder](https://github.com/defei-coder) can you confirm if both the allgather and low_latency_dispatch operations are collective operations for all ranks? I'm suspecting the above issue is simply caused by doing two collective operations in the wrong order.
> 
> E.g. collective ops require all ranks to participate to make progress. If the even ranks doing allgather is waiting for odd ranks to participate, meanwhile odd ranks are doing another collective operations and waiting for even ranks, it would naturally deadlock..
> 
> Let me know if that makes sense.. It's a guess since I'm not super familiar with low_latency_dispatch yet. :)



### alpha-baby · 2025-12-18

@defei-coder do you sure DeepEP hang or NCCL hang?  

you demo: 

```
if rank % 2 == 0:
    with torch.cuda.stream(test_alt_stream):
        dist.all_gather_into_tensor(all_topk_idx, topk_idx, group=group) # this python CPU func will async return ?

buffer.low_latency_dispatch(current_x, topk_idx, num_tokens, num_experts,
                            use_fp8=dispatch_use_fp8, round_scale=round_scale, use_ue8m0=use_ue8m0,
                            cumulative_local_expert_recv_stats=cumulative_local_expert_recv_stats,
                            async_finish=not return_recv_hook, return_recv_hook=return_recv_hook)  # this python CPU func will async return ?

if rank % 2 != 0:
    with torch.cuda.stream(test_alt_stream):
        dist.all_gather_into_tensor(all_topk_idx, topk_idx, group=group)  # this python CPU func will async return ?
default_stream.wait_stream(test_alt_stream)
```

You must make sure that these three functions are non-blocking. Otherwise, the communication will hang.


### xiaofanl-nvidia · 2026-04-04

Based on this fix/WAR from vLLM side https://github.com/vllm-project/vllm/pull/32860 It seems the issue is actually CTA resource contention. 
@defei-coder does the same fix works for you or did you confirm your u-benchmark has a different issue? 
