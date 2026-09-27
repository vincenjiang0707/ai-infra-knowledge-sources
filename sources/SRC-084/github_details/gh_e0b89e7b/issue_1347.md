# [Issue #1347] Torch autograd support for dequantize methods

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1347
state: open | updated: 2026-03-30T16:56:23Z
labels: Low Priority

## 正文

### Feature request

Hi,

Could you please also provide support codes for autograd in the dequantization function?

### Motivation

It can be helpful for future research on the available quantization methods

### Your contribution

I can help to write autograd Functions for backward if you could please guide me on the available forwards for dequantize_blockwise functions

## 评论 (1)

### matthewdouglas · 2025-03-07

Hi!

We do not have the capacity to prioritize this, but contributions are welcome! The backward would likely need to be written as a CUDA function for efficiency. 

The `dequantize_blockwise` function is implemented in [functional.py](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/b8223fed8aa3f6422f2426828f358f760e208a52/bitsandbytes/functional.py#L959).

For more details on the dynamic data type, see (8-Bit Approximations for Parallelism in Deep Learning)[https://arxiv.org/abs/1511.04561].

