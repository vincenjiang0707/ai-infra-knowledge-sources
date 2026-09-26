# [Issue #50] How to independently measure the performance of the Prefill phase and the Decode phase？

source: https://github.com/LLMServe/DistServe/issues/50
state: open | updated: 2025-04-08T14:35:25Z
labels: 

## 正文

As shown in the Figure 1 of the paper, I want to know how to independently measure the performance(rps or latency) of the Prefill phase and the Decode phase？

Now, I have tried these ways:
- Prefill: input_len = x, output_len = 1
- Decode: input_len = 1, output_len = y

Is this method correct? Maybe this method doesn't take into account kvcache, but I don't know how to simulate this part.

And is there any other more precise way? 


I would greatly appreciate any guidance on profiling these two phases separately.


## 评论 (1)

### Dreamer-HIT · 2025-04-08

Have you solved this problem? I have the same confusion
