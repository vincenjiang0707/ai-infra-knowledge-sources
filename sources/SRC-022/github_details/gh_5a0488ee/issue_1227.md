# [Issue #1227] NOTICES.txt needs to update to the corresponding NCCL version?

source: https://github.com/ROCm/rccl/issues/1227
state: closed | updated: 2024-07-04T15:18:49Z
labels: 

## 正文

Hi developers,

The NOTICES.txt from [ROCm 6.0.0](https://github.com/ROCm/rccl/releases/tag/rocm-6.0.0) is unchanged, need it update to the corresponding NCCL version?

`Dependencies on nvidia-nccl v2.17.1-1 (BSD3)`

And When the NCCL v2.20.3 will be adapt to RCCL, thank you.


## 评论 (1)

### corey-derochie-amd · 2024-07-04

RCCL will be updated to NCCL v2.20.5 in ROCm 6.2.0. Please see: https://github.com/ROCm/rccl/pull/1111 .

Thank you for catching the out-of-date NOTICES.txt.
