# [Issue #180] Question about the sf layout

source: https://github.com/deepseek-ai/DeepGEMM/issues/180
state: closed | updated: 2025-09-01T14:09:27Z
labels: 

## 正文

This function is checking if the sf layout is MN-major:
https://github.com/deepseek-ai/DeepGEMM/blob/ea9c5d9270226c5dd7a577c212e9ea385f6ef048/csrc/utils/layout.hpp#L81

It asserts `stride(-2)==1`, that means MN is the contiguous axis. IIRC, the contiguous axis is the minor axis, not the major axis (which changes the slowest). 
https://github.com/deepseek-ai/DeepGEMM/blob/ea9c5d9270226c5dd7a577c212e9ea385f6ef048/csrc/utils/layout.hpp#L85

cc: @RayWang96 @LyricZhao 

## 评论 (2)

### RayWang96 · 2025-09-01

We adopted the terminology in CUTLASS 3.0. For details, please see the doc at:

https://docs.nvidia.com/cutlass/media/docs/cpp/cutlass_3x_backwards_compatibility.html

<img width="1600" height="654" alt="Image" src="https://github.com/user-attachments/assets/d1927bc9-dcba-4985-b8cc-340d3e47a6d2" />

### ispobock · 2025-09-01

Thanks for the clarification! That makes sense to me.
