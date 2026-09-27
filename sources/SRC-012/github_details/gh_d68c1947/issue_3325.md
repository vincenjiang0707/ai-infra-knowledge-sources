# [Issue #3325] [Feature Request] cuda 13 support

source: https://github.com/mlc-ai/mlc-llm/issues/3325
state: closed | updated: 2026-01-25T17:23:45Z
labels: feature request

## 正文

## 🚀 Feature
Thor is out and baseline is cuda 13 and Spark is coming.

## Motivation

Use last versions of flashinfer 3.1, cutlass 4.2 etc making compatible with cuda 13

## Alternatives

Cuda 13 is needed

## Additional context



## 评论 (7)

### dylanlanigansmith · 2025-09-07

TVM runs on a Thor.

add the flag from this: https://github.com/flashinfer-ai/flashinfer/pull/1523 to `CMAKE_CUDA_FLAGS` 
and then in `flashinfer/include/flashinfer/sampling.cuh` change all `cub::Min()` to `::cuda::minimum()`, do the same for `cub::Max()` respectively. 

set cuda arch to 110 and it mostly just works. 


### johnnynunez · 2025-09-07

> CMAKE_CUDA_FLAGS



> TVM runs on a Thor.
> 
> add the flag from this: [flashinfer-ai/flashinfer#1523](https://github.com/flashinfer-ai/flashinfer/pull/1523) to `CMAKE_CUDA_FLAGS` and then in `flashinfer/include/flashinfer/sampling.cuh` change all `cub::Min()` to `::cuda::minimum()`, do the same for `cub::Max()` respectively.
> 
> set cuda arch to 110 and it mostly just works.


> TVM runs on a Thor.
> 
> add the flag from this: [flashinfer-ai/flashinfer#1523](https://github.com/flashinfer-ai/flashinfer/pull/1523) to `CMAKE_CUDA_FLAGS` and then in `flashinfer/include/flashinfer/sampling.cuh` change all `cub::Min()` to `::cuda::minimum()`, do the same for `cub::Max()` respectively.
> 
> set cuda arch to 110 and it mostly just works.

yeah, i could compile some weeks ago but, i open this issue for mlc team upgrade their framework
https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.3.1

### MasterJH5574 · 2025-09-09

Thank you for bringing this up.  We will work on that

### johnnynunez · 2025-09-09

> Thank you for bringing this up. We will work on that

I did a PR that is compiling for me. But there are bugs with tvm, maybe it needs upstream also

### johnnynunez · 2025-09-09

@MasterJH5574 https://github.com/mlc-ai/mlc-llm/pull/3327

### MasterJH5574 · 2025-09-17

CUDA 13 is now supported

### MasterJH5574 · 2026-01-25

Hi @johnnynunez, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
