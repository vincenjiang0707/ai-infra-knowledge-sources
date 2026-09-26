# [Issue #1868] Question: intentional FP16-only path for int8_vectorwise_quant / LLM.int8 activation quant? (BF16 support + removing casts)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1868
state: open | updated: 2026-07-23T11:21:23Z
labels: 

## 正文

Hi guys, first of all, incredible work👍

Just a quick design question about the `LLM.int8` activation quantization path.

### Context

In `MatMul8bitLt.forward`, activations A are always cast to FP16 before quantization:

```py
#bitsandbytes/autograd/_functions.py::MatMul8bitLt.forward
CA, SCA, outlier_cols = F.int8_vectorwise_quant(A.to(torch.float16), threshold=state.threshold)
```

and the CUDA kernel implementation currently hard-requires FP16:
```py
# bitsandbytes/backends/cuda/ops.py
@register_kernel("bitsandbytes::int8_vectorwise_quant", "cuda")
def _(A, threshold=0.0):
    torch._check(A.dtype == torch.float16, ...)
    lib.cint8_vector_quant(get_ptr(A), ...)
```
On the native side, the exported ABI and launcher are also half-only:

- `csrc/pythonInterface.cpp`: cint8_vector_quant(half* A, ...)
- `csrc/ops.cu`: int8VectorQuant(half* A, ...)
- `csrc/kernels.cu`: instantiations only for half
So BF16 inputs get an extra bf16 -> fp16 cast + warning even though the rest of the pipeline tries to preserve output dtype (int8_scaled_mm(..., dtype=A.dtype)).

### Question

Was the FP16-only design for `int8_vectorwise_quant / LLM.int8` activation quantization intentional (e.g. for kernel simplicity, CUB reduction constraints, arch compatibility), or is it mainly an unimplemented gap?

I’m asking because I see a lot of LLM inference/training frameworks use BF16 activations by default these days, and this path currently forces an FP16 cast for quantization.

## 评论 (6)

### matthewdouglas · 2026-02-18

Great question! This is mostly a side-effect of the fact that the original [LLM.int8 paper](https://arxiv.org/pdf/2208.07339) explored older models like OPT and BLOOM, and was only implemented for FP16.

I'm going to mark this as a feature request, because essentially it is just an unimplemented gap. I'm not aware of anything that would prevent us from implementing BF16 for LLM.int8.

### sanghyunna · 2026-02-18

Thanks for the clarification,that makes sense.
If you’re open to it, I’d be happy to take this on and work on adding BF16 support for LLM.int8.
Would it be okay if I draft a PR?

### matthewdouglas · 2026-02-20

@sanghyunna We'd be happy to review a PR for this!

### kru2710shna · 2026-07-05

Hi @matthewdouglas 
I've implemented BF16 support for int8_vectorwise_quant / LLM.int8 and would like to open a PR. @sanghyunna , you mentioned back in February you might take this on; I didn't want to step on your work, so please let me know if you're still on it and I'll happily hold off. If not, I have a working implementation ready to go.

Approach (mirrors the existing 
gemm_4bit_inference_naive fp16/bf16/fp32 
pattern):

Templated int8VectorQuant on T and added bnb_bfloat16 kernel instantiations New cint8_vector_quant_bf16 C ABI entry point; Python dispatches on A.dtype Removed the forced A.to(torch.float16) casts in MatMul8bitLt so BF16 activations quantize natively
The blockwise absmax reduction now accumulates in float rather than T as it required for BF16 to compile cleanly, and it slightly improves FP16 accuracy too (rowStats was already float, so nothing downstream changes)

Extended test_int8_vectorwise_quant to cover both dtypes

Happy to adjust the approach if you'd prefer something different.

### sanghyunna · 2026-07-23

@kru2710shna 
Hi there! Thanks for stepping in. I've been quite tied up lately and haven't had the chance to work on this, so I would really appreciate it if you could take it over. Thanks again!

### kru2710shna · 2026-07-23

Thanks! I’ll take it from here and submit the PR shortly. I’ll make sure it’s well-tested and incorporate any feedback during review.
