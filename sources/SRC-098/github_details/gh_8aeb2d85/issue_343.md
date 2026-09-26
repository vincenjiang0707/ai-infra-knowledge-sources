# [Issue #343] Latest release broke compilation entirely for < NCCL 27

source: https://github.com/NVIDIA/nccl-tests/issues/343
state: closed | updated: 2025-09-05T16:35:17Z
labels: 

## 正文

`common.cu(966): error: identifier "ctaPolicy" is undefined
            ctaPolicy = (int)strtol(optarg, 
`

Bad guards somewhere surrounding use of ctaPolicy.

This is in a fresh Pytorch 2.8 container, was compiling cleanly right before your latest commit e12dbb0. 

`>>> torch.cuda.nccl.version()
(2, 25, 1)
`

## 评论 (3)

### murat-runpod · 2025-09-05

It's because you have compile time guards on definition and runtime guards on usage of `ctaPolicy`

### AddyLaddy · 2025-09-05

We've just pushed a fix. Can you retest please.


### murat-runpod · 2025-09-05

Works great thanks!
