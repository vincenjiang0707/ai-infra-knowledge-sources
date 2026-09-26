# [Issue #445] Networking requirements(latency, bandwidth, throughput) for EP vs TP?

source: https://github.com/deepseek-ai/DeepEP/issues/445
state: closed | updated: 2026-09-18T09:15:12Z
labels: 

## 正文

I'm curious about the differences in networking requirements between EP and TP, particularly regarding latency, bandwidth, and throughput. I know that both distribution strategies are highly demanding in terms of networking performance, but I'm not sure which one has higher requirements from latency, bandwidth, and throughput perspectives. Could someone elaborate on this a little for me?

I also know that NCCL wasn't well-optimized for all-to-all which EP requires, and that's why DeepEP was introduced. But why can NCCL meet TP's requirements? Is it because NCCL is well-suited for allreduce, or is it because TP is more tolerant of networking limitations compared to EP?

Thanks.

## 评论 (3)

### sphish · 2025-10-11

TP essentially consists of two communication patterns: **allgather** and **reduce-scatter**, both of which NCCL has optimized very effectively.  

Both EP and TP communication patterns have extremely high latency and bandwidth requirements. In fact, because NCCL’s latency optimization is not particularly strong, in many low-latency scenarios (primarily inference), people may replace NCCL with custom communication kernels.

### terrificdm · 2025-10-12

> TP essentially consists of two communication patterns: **allgather** and **reduce-scatter**, both of which NCCL has optimized very effectively.
> 
> Both EP and TP communication patterns have extremely high latency and bandwidth requirements. In fact, because NCCL’s latency optimization is not particularly strong, in many low-latency scenarios (primarily inference), people may replace NCCL with custom communication kernels.

Well noted. Thank you for your clarification.

### polarstormx · 2026-09-18

Closing as answered, as [the author confirmed](https://github.com/deepseek-ai/DeepEP/issues/445#issuecomment-3393871238) that the explanation clarified the question.
