# [Issue #59] How to handle preemption cases

source: https://github.com/LLMServe/DistServe/issues/59
state: open | updated: 2025-04-15T13:48:13Z
labels: 

## 正文

Thank you for the contribution.

In the paper, you mentioned that DistServe does not consider preemption. During experiments/benchmarking, how do you control the request rates and the number of token generated for each request to make sure the decode GPU doesn't hit the memory limit? Thanks.

## 评论 (2)

### Dreamer-HIT · 2025-04-08

I have the same question. Have you solved this problem?

### Mrxiangli · 2025-04-15

@Dreamer-HIT I think based on the code, when preemption occurs, the KV cache is transferred to host memory, and reload to the GPU when memory is available.
