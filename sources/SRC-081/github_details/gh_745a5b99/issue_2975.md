# [Issue #2975] [ModelFreePTQ] Memory issues with multi-gpu

source: https://github.com/vllm-project/llm-compressor/issues/2975
state: closed | updated: 2026-08-18T13:54:04Z
labels: enhancement, good first issue, model_free_ptq

## 正文

## Background ##
https://github.com/vllm-project/llm-compressor/pull/2773 introduced multi-gpu model free PTQ jobs. It works by statically assigning jobs to gpus round-robin style. However, this can lead to bad memory allocation, as slower gpus will accumulate more jobs than faster gpus, leading to OOM errors.

I have observed this behavior when using 6 gpus.

The better approach is to use a thread pool which dynamically assigns jobs to the gpu with the most resources. The best solution involves estimating job memory size (to account for hetereogenous gpu/job sizes), perhaps folding this into the validation step. Whenever the thread pool has an unassigned thread, the main thread checks which gpus can accommodate the job size and assigns it to the gpu with the most capacity.

This mechanism would also prevent OOMs caused by users picking too many workers

## Proposed Changes ##
1. Make GPU assignment dynamic and scheduled via the main thread
2. Add a multi-gpu test on a small model with many safetensors (you can adjust the safetensors file size when saving models with transformers)


## 评论 (1)

### rohan9446 · 2026-07-27

Hi @kylesayrs, I'd love to work on this! Could you please assign it to me?
