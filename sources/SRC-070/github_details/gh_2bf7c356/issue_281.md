# [Issue #281] performance using NCCL

source: https://github.com/deepseek-ai/DeepEP/issues/281
state: closed | updated: 2026-09-18T09:15:20Z
labels: 

## 正文

I'm curious about how is the performance will be if I use NCCL' alltoall or send/recv to implement EP in pure python? have you ever tried? Thanks!

## 评论 (3)

### sphish · 2025-07-10

https://github.com/ppl-ai/pplx-kernels has compared the performance of PyTorch all-to-all and DeepEP. You can refer to it.

### jing-4369 · 2025-07-10

Thanks!

### polarstormx · 2026-09-18

Closing as answered: the requested performance comparison was provided and [acknowledged by the author](https://github.com/deepseek-ai/DeepEP/issues/281#issuecomment-3058157040).
