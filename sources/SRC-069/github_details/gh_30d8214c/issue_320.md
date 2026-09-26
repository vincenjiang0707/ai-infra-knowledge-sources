# [Issue #320] [Question]About the new maga kernel and swapab feature

source: https://github.com/deepseek-ai/DeepGEMM/issues/320
state: closed | updated: 2026-05-06T01:52:00Z
labels: 

## 正文

I have some question about the new mega kernel and other w4a8 group gemm kernel.
1. Can someone explain why the ‘swapab’ is used in the new mega kernel and w4a8 group gemm kernel? The pr description say it is for the better performance, "dynamic swap A/B, much faster MoE GEMM".But I am confused about where the performance benefits come from. 
       1. For mega kernel, The first mma result can load from tmem to register, the epilogue multiply src can complete in a thread with 'swapab'. It should be a performance benefit. Is there other perf optimization from the 'swapab'? 
       2. For w4a8 grouped gemm kernel,  Is it to reduce memory load from global memory or to reduce invalid computation of umma? 
2. In the mega kernel, why is the regular store instruction used in the mega kernel to store data to the remote rank in the combine phase, instead of using async instructions like 'tma_1d' or 'tma_reduce_1d' in the dispatch phase? Is there any consideration for this? 

Thanks!

## 评论 (4)

### zheanxu · 2026-04-30

Thanks for the questions!

After swapping A/B, `block_m`/`block_n` map to `umma_n`/`umma_m` respectively. For MoE, this enables a 2-CTA GEMM with `umma_m=256` fixed and `umma_n` dynamically scheduled. The 2-CTA design saves shared memory, allowing more pipeline stages for better latency hiding, and placing the token dimension on `umma_n` avoids wasted Tensor Core compute when experts are assigned few tokens. The epilogue scaling can also be completed within the same thread as you noted. For w4a8 grouped GEMM, it's primarily to reduce HBM bandwidth pressure.

For the combine phase, tokens are scattered to different remote addresses at ~256B granularity. TMA instructions have high launch latency overhead, making them inefficient for many fine-grained irregular stores — regular store instructions are more suitable here.

Hope this helps!

### gyhintel · 2026-04-30

Hi, @zheanxu thank you for your detailed explanation, but I still have some questions.
1. Seem for the 2CTA GEMM, we consider the [layout D](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-data-path-layout-d) to [layout A](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-data-path-layout-a). But I found that the [lyaout B](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-data-path-layout-b) is also for 2CTA. Why haven't we considered using layoutB? If using layout B, it also can save the shared memory. 
2. I have tried benchmarking tcgen05.mma instruction before, for the case of M=128, when N is less than 128, reducing N cannot further reduce the instruction latency. So does reducing Tensor Core compute really improve performance?
3. For w4a8 grouped GEMM, I think it can reduce HBM bandwidth after swapab because BLOCK-N can be flexible. But for the decoding, if the src amount data is small, will the improvement be not significant?

### zheanxu · 2026-04-30

Hi @gyhintel, thanks for following up.

We chose layout D / layout A mainly because a larger `umma` block reduces shared memory bandwidth pressure, and placing the token dimension on `umma_n` lets us dynamically shrink `umma_n` for experts with few tokens, saving Tensor Core work. Layout B would fix `umma_n` and vary `umma_m`, giving less control over wasted compute for tail experts.

In our case `umma_n` can be as large as 232, so reducing it definitely avoids idle cycles; even smaller reductions help cut latency and you can measure the effect yourself.

The HBM bandwidth saving comes almost entirely from the `w4` data type, not from swapping A/B. The swap A/B primarily improves the `fp8` GEMM performance ceiling by better utilizing the Tensor Core pipeline – for pure grouped GEMM we saw roughly a 15% speedup.

### gyhintel · 2026-05-06

@zheanxu I see the layout B is  "M = 128 + .cta_group::2 + Dense A matrix" in the doc. It should fix `umma_m` is 128 and vary `umma_n` in "N = {16, 32, … 256} steps of 16"?

<img width="1081" height="336" alt="Image" src="https://github.com/user-attachments/assets/c0a0047c-77e0-473e-99f6-b0415e8173a0" />
