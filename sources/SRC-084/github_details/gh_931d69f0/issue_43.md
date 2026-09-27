# [Issue #43] How to accelerate the inference speed of 1bit+lora model

source: https://github.com/dropbox/hqq/issues/43
state: closed | updated: 2024-08-28T10:08:45Z
labels: enhancement

## 正文

Because it's so slow, 34b model 1bit+lora is about 1token/s

## 评论 (4)

### mobicham · 2024-04-04

Yeah, we are actively looking for ways to speed it up, but it might take a while, because re-using available kernels is not fully compatible with HQQ's logic.

### Minami-su · 2024-05-02

🥺

### mobicham · 2024-05-02

We have accelerated inference for 4-bit now: https://github.com/mobiusml/hqq/?tab=readme-ov-file#backend
1-bit acceleration is the holy grail and is work in progress.

### mobicham · 2024-08-28

You can use the bitblas backend with 2-bit. You can follow this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/bitblas_int4_demo.py
