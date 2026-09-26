# [Issue #75] Implement CUDA/VMM memory detection in UCX backend

source: https://github.com/ai-dynamo/nixl/issues/75
state: closed | updated: 2026-08-19T15:58:20Z
labels: enhancement

## 正文

Currently, we only detect cuda-malloc'd memory:
https://github.com/ai-dynamo/nixl/blob/main/src/plugins/ucx/ucx_backend.cpp#L50

UCX is also capable of detecting VMM memory:
https://github.com/openucx/ucx/blob/master/src/uct/cuda/cuda_copy/cuda_copy_md.c#L633

This code needs to be proted to NIXL too

## 评论 (1)

### rakhmets · 2026-08-19

Detecting the memory is not needed anymore, as it's covered by UCX library. https://github.com/ai-dynamo/nixl/pull/946
