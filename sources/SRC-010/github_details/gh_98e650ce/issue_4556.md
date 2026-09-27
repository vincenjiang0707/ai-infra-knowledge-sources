# [Issue #4556] [Feature] 0.12.3现在支持Qwen3.6-35B-A3B的量化版本了吗？比如4bit的量化版本？

source: https://github.com/InternLM/lmdeploy/issues/4556
state: open | updated: 2026-06-14T07:29:42Z
labels: 

## 正文

### Motivation

[Feature] 0.12.3现在支持Qwen3.6-35B-A3B的量化版本了吗？比如4bit的量化版本？

### Related resources

_No response_

### Additional context

_No response_

## 评论 (12)

### shrisha108 · 2026-04-25

Hello,
Was wondering the same about support of Qwen3.6-27B with Turbomind?  That would be great!

### huliangbing2000 · 2026-04-26

lmdeploy支持qwen3.6-35b-a3b-awq

### shrisha108 · 2026-04-27

I'm getting "Invalid Argument.  Aborted, Core Dumped." with Qwen3.6 27B AWQ 4Bit model. Just any simple prompt and LMDeploy crashing.

### bash99 · 2026-04-27

> lmdeploy支持qwen3.6-35b-a3b-awq

NVFP4 这类版本有支持吗？ 例如 sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP 这种？

### 43758726 · 2026-04-29

I'm adding Qwen3.5-35B-A3B awq model support, i will add Qwen3.6-35B-A3B awq model support later.

### lvhan028 · 2026-04-29

Hi, folks.
Regarding the inference of qwen3.6-35b-a3b awq model, turbomind engine already supported it, since its model arch is the same as qwen3.5.

We are also working on the lmdeploy lite module to provide the function of quantizing qwen3.5/3.6 models



### lvhan028 · 2026-04-29

> I'm getting "Invalid Argument. Aborted, Core Dumped." with Qwen3.6 27B AWQ 4Bit model. Just any simple prompt and LMDeploy crashing.

May kindly let us know your target device. Turbomind engine hasn't support Qwen3.5/3.5 27B awq inference on Turing GPUs



### lvhan028 · 2026-04-29

> > lmdeploy支持qwen3.6-35b-a3b-awq
> 
> NVFP4 这类版本有支持吗？ 例如 sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP 这种？

还没有支持 NVFP4

### shrisha108 · 2026-05-04

> > I'm getting "Invalid Argument. Aborted, Core Dumped." with Qwen3.6 27B AWQ 4Bit model. Just any simple prompt and LMDeploy crashing.
> 
> May kindly let us know your target device. Turbomind engine hasn't support Qwen3.5/3.5 27B awq inference on Turing GPUs


Sorry just saw your message , Yes I have 2 x Titan RTXs with NV-Link. Is gptq of Qwen3.5/3.5 27B models supported? or int8?


### sacrrie · 2026-05-21

the current support is with CUDA / pytorch right? Any plan for turbomind optimization and adaptation?

### 43758726 · 2026-05-21

> the current support is with CUDA / pytorch right? Any plan for turbomind optimization and adaptation?

Hi sacrrie, the imference of qwen3.6-35b-a3b awq model is supported by turbomind, since it its model arch is the same as qwen3.5.

### simonjhy · 2026-06-14

qwen3.5-122B awq版本现在能支持吗？

