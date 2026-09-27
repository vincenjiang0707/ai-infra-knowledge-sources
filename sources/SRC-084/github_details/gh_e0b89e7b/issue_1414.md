# [Issue #1414] Support for quantization of convolutional layers

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1414
state: closed | updated: 2026-03-31T18:05:51Z
labels: Contributions Welcome, Feature Request

## 正文

### Feature request

Would be great if the library could support more types of layers for quantization like with `torch.ao`, seems like it is already available with [conv2d](https://pytorch.org/docs/stable/generated/torch.ao.nn.quantized.Conv2d.html). Sadly `torch.ao` does not seem to support CUDA as a backend right now. Would it be possible to implement the 8-bit and 4-bit kernels in Triton or CUDA to allow for the quantization of convolutional layers? A similar issue has been raised [here](https://github.com/bitsandbytes-foundation/bitsandbytes/issues/29) earlier.

### Motivation

Make modules that use convolutional layers use less memory through quantization.

### Your contribution

Yes, I am willing to work on implementing convolutional kernels if it is possible to integrate with this library.

## 评论 (1)

### matthewdouglas · 2026-03-31

Closing as not planned — see the discussion on #1907 for context.
