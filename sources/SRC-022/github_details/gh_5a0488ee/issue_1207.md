# [Issue #1207] [Feature]: Profiling

source: https://github.com/ROCm/rccl/issues/1207
state: closed | updated: 2024-07-02T16:17:42Z
labels: 

## 正文

### Suggestion Description

Is there any tool or an option which provides the compute time of the reduction operation

### Operating System

Ubuntu

### GPU

MI250A

### ROCm Component

RCCL

## 评论 (2)

### tks2004 · 2024-07-01

Could someone respond to this 

### gilbertlee-amd · 2024-07-02

Hi @tks2004 - Sorry for the late reply.

There's no way to isolate just the compute time for the reduction operation, as the arithmetic is generally not the bottleneck, and it's tied closely to the communication.

If you would like to get some in-depth profiling, I'd recommend trying using[ NPKit](https://github.com/ROCm/rccl?tab=readme-ov-file#npkit).
