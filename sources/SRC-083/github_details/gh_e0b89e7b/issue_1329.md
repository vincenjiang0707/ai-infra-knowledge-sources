# [Issue #1329] Any plan to support block size 32?

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1329
state: closed | updated: 2026-02-23T20:13:28Z
labels: Enhancement, High Priority, High Risk, To Discuss Internally

## 正文

### Feature request

support block size 32

### Motivation

Recently many models can be better when quanted in block size 32 and many benchmarks are run in 32 as block size.

Several types of models, like vision models and image generators, are also more sensitive to block size, and 32 (or even 16) as block size can be better suited for those tasks.

### Your contribution

If one point out where I should look at I can also PR. But I am not sure about compiling with different version 

## 评论 (6)

### matthewdouglas · 2024-08-22

We haven't had any immediate plans for this, but if it is useful to the community then we can consider it. I'm making the assumption here that we're talking about 4bit. If we added a naive implementation for this based on the existing kernels it probably wouldn't be ideal from an occupancy standpoint but I think it could potentially work as a first step.

In csrc/ops.cu, we'd be looking at `quantizeBlockwise`, `dequantizeBlockwise`, and `gemm_4bit_inference_naive`. On the Python side, there's assertions around the blocksize in `functional.py` in `quantize_4bit()` and `dequantize_4bit()`.

Gentle ping @TimDettmers - any thoughts/concerns?



### lllyasviel · 2024-08-22

Thanks for the comments. 

Recently image generators are entering large model era like [Flux](https://huggingface.co/black-forest-labs/FLUX.1-dev) and in need for low bit computation.

The influence of block size is much more salient in image models than LLMs. As a result, many people are currently using slower pytorch workarounds like 

```python
d = blocks[:, :2].view(torch.float16)
qs = blocks[:, 2:]
qs = qs.reshape((n_blocks, -1, 1, block_size // 2)) >> torch.tensor([0, 4], device=d.device, dtype=torch.uint8).reshape((1, 1, 2, 1))
qs = (qs & 0x0F).reshape((n_blocks, -1)).to(torch.int8) - 8
````

to get smaller block size for those image models.

It will be a great advancement for low bit image generation models if bnb can support smaller block size natively like 32 (or even 16)

### TimDettmers · 2024-08-26

Instead of replying, I quickly tried to implement it, but I failed. Despite this is might be a good starting point to implement this. You can find my changed on the branch `small_blocksizes`: https://github.com/bitsandbytes-foundation/bitsandbytes/tree/small_blocksizes

I tried this before, but there is one main problem with the kernels: they operate on a warp level which assumes 32 values in total, but for 4-bit there are only 16 values to process when quantized as packed char values. This causes problems. I fixed some problems of these, but currently the kernel has a bug.

The bug is likely related to my change: instead of storing 16 values, I store 32 values. I thought `valid_items` would make sure that the right amount of values are stored, but this does not seem true. As such, the bug is likely in one of these locations:

https://github.com/bitsandbytes-foundation/bitsandbytes/blob/small_blocksizes/csrc/kernels.cu#L738
https://github.com/bitsandbytes-foundation/bitsandbytes/blob/small_blocksizes/csrc/kernels.cu#L825

I will not have time to look into more detail, but I hope this draft can help you develop a PR that works. I already added tests for the block sizes which you can run via:

`pytest -vsk 32-nested`

I think this is an important contribution and it would be awesome if you could work on this PR!r

### lllyasviel · 2024-08-26

Thanks a lot for the draft! I took a look – I may be wrong but it seems that all changes are on the quantizing part? Does this mean once I have an already quantized model, I can just infer in block size 32 using existing codes? 

### TimDettmers · 2026-02-21

Following up on the earlier draft work — we now have PR #1858 which adds k-bit blockwise quantization (k=2-5) with warp-level CUDA kernels, including support for smaller block sizes. Once that PR is merged, this issue should be resolved.

### matthewdouglas · 2026-02-23

To add to this, we recently released v0.49.2 which includes support for blocksize of 32 for 4bit quantization via #1854. Closing as this should resolve this feature request!
