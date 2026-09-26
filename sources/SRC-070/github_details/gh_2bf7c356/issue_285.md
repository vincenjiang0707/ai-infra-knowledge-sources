# [Issue #285] [Question]: Why RDMA bandwidth can exceed 50GB/s

source: https://github.com/deepseek-ai/DeepEP/issues/285
state: closed | updated: 2026-09-20T01:56:44Z
labels: 

## 正文

Hi folks, I found that the RDMA bandwidth in README.md can exceed 50GB/s, just what to ask how is this number measured? Is this actually algorithm bandwidth instead of bus bandwidth? 

To my knowledge, for algorithm bandwidth we can compute with BW = total_bytes / duration and for bus bandwidth, we compute with BWrdma = rdma_total_bybtes / duration.

Please correct me if I'm wrong, thanks!

## 评论 (4)

### TianDi101 · 2025-07-09

I just noticed that this PR https://github.com/deepseek-ai/DeepEP/pull/130 explains the calculation. However, in this case the EP16 performance is a little wierd since its bus bandwidth is only 43 * 0.5 = 21.5GB/s, far less than 50GB/s. I think under the setting of 4096 token per GPU, it should be able to saturate RDMA bandwidth.

### sphish · 2025-07-10

On the H800, the RDMA network bandwidth utilization is indeed not high in EP16 case. A main reason for this is that in our EP16 test case, when the RDMA bandwidth reaches 43 GB/s, the NVLink bandwidth will exceeds 140 GB/s, making NVLink the bottleneck.

With GPUs that have higher NVLink bandwidth, you'd get better results.

### TianDi101 · 2025-07-14

> On the H800, the RDMA network bandwidth utilization is indeed not high in EP16 case. A main reason for this is that in our EP16 test case, when the RDMA bandwidth reaches 43 GB/s, the NVLink bandwidth will exceeds 140 GB/s, making NVLink the bottleneck.
> 
> With GPUs that have higher NVLink bandwidth, you'd get better results.

Thanks for the explanation, could you please elaborate on this more?

I'm thinking in this way, for each GPU in the EP16 case, the inbound RDMA bandwidth is 50GB/s while the outbound NVLink bandwidth is 160GB/s, seems that no matter how the algorithm is designed, RDMA bandwidth is always the bottleneck, right?

This is under the assumption that 8 GPUs in a node don't compete for NVLink bandwidth, that being said, each GPU will always get 160GB/s for each direction. But I'm not sure if this assumption is right. 

### sphish · 2025-07-15

> I'm thinking in this way, for each GPU in the EP16 case, the inbound RDMA bandwidth is 50GB/s while the outbound NVLink bandwidth is 160GB/s, seems that no matter how the algorithm is designed, RDMA bandwidth is always the bottleneck, right?

Since the tokens received from RDMA may be forwarded multiple times via NVLink, RDMA is not always the bottleneck. he NVLink 160GB/s bandwidth is also just a ideal upper bound. 

Based on previous feedback and test results from the Tencent team, testing with H20 servers that have higher NVLink bandwidth shows significantly better performance in the EP16 case, which leads me to believe that this case is NVLink-bottlenecked.
