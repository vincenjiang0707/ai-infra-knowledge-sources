# [Issue #173] Zero point dtype

source: https://github.com/dropbox/hqq/issues/173
state: closed | updated: 2026-01-02T18:15:17Z
labels: 

## 正文

Hi, I have a question regarding zero-point dtype handling.
Typically, the zero-point is serialized using the target quantization dtype (int8/uint8...), but during optimization it is cast to float.

When serializing it back, is it sufficient to simply cast it back to the original integer dtype, or should the zero-point itself be quantized again, thus introducing a scale and (possibly) a zero-point for it ?

Thanks

## 评论 (4)

### mobicham · 2025-12-30

Hi @AyoubMDL , the zero-point was quantized in the earlier version of hqq but we no longer do that because it was a mess to manage. The original math formulation is for floating-point scales/zeros and you don't really need to quantize them anyway because the optimized matmul kernels don't need 8-bit scales/zeros, both in Gemlite and vLLM via Marlin work with fp16/bfloat16 zeros/scales.

If you wanna quantize them yourself, just make sure you keep track of the scaling. Note that the zero-point here is quite different from what is used in AWQ/GPTQ, the zero-point in HQQ is the result of an optimization problem and has no guarantees to be in a specific range.

I hope this answers your question

### AyoubMDL · 2025-12-30

Hi, thanks for the response. I am talking from an implementation perspective (I am looking to add HQQ to vllm/llm-compressor repo).

When applying HQQ and serializing the result, I need to store the zero as a float32 right ? If so, my understanding is:

1. In the case of symmetric quantization, I have to add an extra param which has same shape/dtype as scale.
2. In the case of asymmetric quantization with int/uint zero, I have to replace the int/uint zero point with the optimized param that has same shape/dtype as scale.

### mobicham · 2025-12-31

The zeros/scales should be float16/bfloat16, depending on the dtype of the rest of the weights. The zeros/scales have the same shape regardless if they are 16-bit or 8-bit and you can simply reshape them directly. Note that hqq lib uses `(Wq - zeros) * scales)`.
The uint8 zeros was a limitation from the older AWQ/GPTQ kernels. They were quantizing the zeros to load the meta-data faster. However, if the meta-data loading is correctly pipelined and the group-size is not too small, using 16-bit zeros will have minimum impact on the speed. Since the zeros in hqq are the result of an optimization problem, they should not be quantized directly otherwise it will heavily impact the quality.
Since there are already kernels to run HQQ kernels with 16-bit zeros, there's no need to quantize them anyway.

Btw, vLLM already supports running HQQ with 16-bit zeros: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/hqq_marlin/
it works out-of-the-box with models exported via transformers. Alternatively, there's also the option to run them via <a href="https://github.com/dropbox/gemlite">Gemlite</a>

### AyoubMDL · 2026-01-02

I see. Thanks for the pointers and the explanation !
