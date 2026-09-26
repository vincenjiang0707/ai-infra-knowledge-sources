# [Issue #267] [Question] How is latency measured with CUDA Shared Mem enabled?

source: https://github.com/triton-inference-server/perf_analyzer/issues/267
state: open | updated: 2025-02-18T18:16:12Z
labels: 

## 正文

I've reviewed: https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/measurements_metrics.md#how-latency-is-calculated

but I still have some outstanding questions about how latency interacts with the various shared memory implementations.

We're sending quite large image payloads and have noticed a substantially decreased latency when switching between gRPC and gRPC w/ Cuda Shared Mem. We're suspicious that the time taken to perform the "Cuda Share Memory Memcpy" is not being accounted for, and that part of what we are measuring is simply moving latency from Triton to the Client code?

I've tried reviewing the code and have found the location where the cuda memcpy is being performed, but am struggling to understand how that code is or isn't incorporated into the latency statistics.

## 评论 (6)

### the-david-oy · 2025-02-05

CC: @matthewkotila @nicolasnoble 

### Carter12s · 2025-02-17

Bump on this still curious if we can get an answer

### the-david-oy · 2025-02-18

Thanks for bumping this thread, Carter. @matthewkotila, do you know more about the about whether the CUDA memory copy is included in the e2e latency measurement or know who would?

### Carter12s · 2025-02-18

I think we've managed to answer this question ourselves.

We wrote an independent testing script and tracked the latency ourselves and determined that this tool is NOT including the CUDA memcpy time in its report.

Note: that because "GRPC Transit" is reported, and the CUDA memcpy transit is NOT, this makes CUDA memcpy appear quite a bit better than it actually is for large payload sizes.

For large image payloads this can misrepresent real world latency by >20%.

Would call it a bug per say, but it could be good to clarify in the documentation.

### matthewkotila · 2025-02-18

Not off the top of my head.

### the-david-oy · 2025-02-18

Thank you to you and your team for identifying this, Carter! I created a ticket for us to investigate this.

Ref: TPA-978
