# [Issue #342] ctaPolicy undefined in common.cu when compiling with NCCL 2.26

source: https://github.com/NVIDIA/nccl-tests/issues/342
state: closed | updated: 2025-09-08T15:42:52Z
labels: 

## 正文

https://github.com/NVIDIA/nccl-tests/blame/e12dbb0a14f915c25d0bdaec631d98587b156d97/src/common.cu#L111

A recent change defines ctaPolicy only when NCCL >= v2.27 is used. Appears in tagged release 2.17.

When compiling with NCCL 2.26 this leads to the compiler error

common.cu(966): error: identifier "ctaPolicy" is undefined
            ctaPolicy = (int)strtol(optarg,

because that code is not protected by a similar #if block.

## 评论 (2)

### AddyLaddy · 2025-09-05

We've just pushed a fix. Can you retest.


### jpcoles-cscs · 2025-09-07

Yes, this fixed it for me. Thank you!
