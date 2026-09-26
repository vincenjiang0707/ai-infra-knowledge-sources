# [Issue #2397] [QST] Optimal configuration for large-scale GEMM on B100

source: https://github.com/NVIDIA/cutlass/issues/2397
state: closed | updated: 2026-09-05T17:12:29Z
labels: question, ? - Needs Triage, inactive-90d

## 正文

I have read and tried the GEMM example for sm100a in [`cutlass/examples/70_blackwell_gemm/70_blackwell_fp16_gemm.cu`](https://github.com/NVIDIA/cutlass/blob/main/examples/70_blackwell_gemm/70_blackwell_fp16_gemm.cu).
In the example, two SMs cooperatively compute 256x128x64 MMA in single stage of pipeline, and the total pipeline stage is set to 8. The cluster size is also chosen to be 2x2.

I have the following questions:
1. Is this configuration optimal for large scale (M, N, K > 1024) GEMM on B100?
2. Why 8-stage pipeline is needed? I remember 3-4 stages are enough to hide the load latency on H100.
3. On H100, a single SM is capable of 256x128x64 MMA, why 2 SMs of B100 also take the same size. Why not use larger scale to improve data reuse?
4. It is reported (https://cudaforfun.substack.com/p/outperforming-cublas-on-h100-a-worklog) that the best practice of cluster size on H100 is 2x1, although H100 support maximal cluster size of 16. So the best practice of cluster size on B100 is also only 2x2 for large-scale GEMM?


## 评论 (11)

### Junkai-Wu · 2025-06-16

For question 1, the configuration of the example is not guaranteed to be optimal. It is just to show an example of how to setup a blackwell gemm kernel in CUTLASS.

For question 2, the stage number of 8 is automatically calculated according to the total shared memory size of one SM and single-stage shared memory size of the kernel. The goal is to hide the latency as much as possible under shared memory size limit.

For question 3, we have 2sm kernel in blackwell where two SMs calculate one MMA together.

For question 4, as stated above, the example configuration is not guaranteed to be optimal. What is the best practice of cluster size on B100 for different scale GEMM needs to be tuned.

### SimonZh1234 · 2025-06-17

@Junkai-Wu Thank you for your reply. Must I get the optimal configuration by test-and-trial? Is there any experience on the optimal configuration (only for GEMM of **large** enough scale)? How does the CUTLASS team configure the hyperparameter when running the performance regression (https://github.com/NVIDIA/cutlass?tab=readme-ov-file#performance)?

### thakkarV · 2025-06-19

CUTLASS profiler now has an autotuner built in. Please use that to search for the best kernel with the largest instantiation list that you're comfortable compiling. Alternatively you can also use the Python DSL GEMM for much faster compile times 

### sleepwalker2017 · 2025-07-12

> CUTLASS profiler now has an autotuner built in. Please use that to search for the best kernel with the largest instantiation list that you're comfortable compiling. Alternatively you can also use the Python DSL GEMM for much faster compile times

I'm sorry but I want to ask what is the auto tuner in cutlass profiler? 
Is is the command like this? 
```
tools/profiler/cutlass_profiler --operation=Gemm --enable-best-kernel-for-fixed-shape --A=f16:col --B=f16:col --C=f16:col --D=f16:col --m=5120 --n=4096 --k=4096 --sort-results-flops-per-sec
```

I use it to get best config for gemm+relu example . But the best config for gemm seems not still best for gemm+relu. 

Any advice? thank you!

### Junkai-Wu · 2025-07-24

@sleepwalker2017 To find the best performance for a specific GEMM problem size, you can use following command:
```
cutlass_profiler --kernels=*gemm* --enable-best-kernel-for-fixed-shape --m=6144 --n=6144 --k=6144 --sort-results-flops-per-sec
```

Replace the `--kernels=*gemm*` to the specific kernels you want. Also it's possible that the best config for gemm is not the best for gemm+relu.

### sleepwalker2017 · 2025-07-24

Thank you. So I still need to choose some configs and try them on gemm+relu





------------------ Original ------------------
From: Junkai-Wu ***@***.***&gt;
Date: Thu,Jul 24,2025 10:48 AM
To: NVIDIA/cutlass ***@***.***&gt;
Cc: fade_away ***@***.***&gt;, Mention ***@***.***&gt;
Subject: Re: [NVIDIA/cutlass] [QST] Optimal configuration for large-scale GEMMon B100 (Issue #2397)

### github-actions[bot] · 2025-08-23

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### sleepwalker2017 · 2025-08-30

> [@sleepwalker2017](https://github.com/sleepwalker2017) To find the best performance for a specific GEMM problem size, you can use following command:
> 
> ```
> cutlass_profiler --kernels=*gemm* --enable-best-kernel-for-fixed-shape --m=6144 --n=6144 --k=6144 --sort-results-flops-per-sec
> ```
> 
> Replace the `--kernels=*gemm*` to the specific kernels you want. Also it's possible that the best config for gemm is not the best for gemm+relu.

Hi， I have a question about the 1st example `https://github.com/NVIDIA/cutlass/blob/master/examples/00_basic_gemm/basic_gemm.cu`

In the example code, it selects A B C all column major, I wonder why? 

I thought A row major, B column major,  and C row major is the best layout for GPU, It seems not? 

Can you give some explanation? thank you! 

### michael604work · 2025-11-18

> CUTLASS profiler now has an autotuner built in. Please use that to search for the best kernel with the largest instantiation list that you're comfortable compiling. Alternatively you can also use the Python DSL GEMM for much faster compile times

Hi experts :-)

Could you explain how to use Python DSL GEMM, while using the cutlass profiler/auto-tuner?

Thanks!

### Junkai-Wu · 2025-12-05

@michael604work cutlass profiler targets at C++ codes, not python dsl. Please refer to https://github.com/NVIDIA/cutlass/tree/main/media/docs/pythonDSL to check how to use python dsl.

### github-actions[bot] · 2026-03-05

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
