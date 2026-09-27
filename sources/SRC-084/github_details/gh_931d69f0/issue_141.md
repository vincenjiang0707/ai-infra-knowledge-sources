# [Issue #141] Question about the fused quantized kernel

source: https://github.com/dropbox/hqq/issues/141
state: closed | updated: 2025-01-15T08:17:03Z
labels: 

## 正文

Hi, thank you very much for developing and maintaining such a great project!
I don't have an experimental environment at the moment, and I haven't found any instructions in the relevant documents, so I'd like to ask here: As far as I understand, hqq provides unfused dequantization kernels, right? If we want to use fused kernels to get actual acceleration, do we have to rely on libraries such as torchao or bitblas?

Among these backends, does any of them provide 3bit fused quantized Gemm kernels? (I noticed that bitblas provides 4/2/1 bitwidth fused kernels)

In addition, does hqq currently have any backend that can provide fused quantization kernels for MoE's groupgemm?

## 评论 (3)

### mobicham · 2025-01-14

Hey thank you, great questions!
 
- That's correct, it relies on other libraries for the fused kernel inference (which can be used elsewhere, like using HQQ directly in VLLM for example)

- Regarding the 3-bit support there's nothing really ready to use at this time. I wrote an experimental A16W3 kernel in <a href="https://github.com/mobiusml/gemlite/">gemlite</a> which works well, but it would need some work to make it ready for use. There's <a href="https://github.com/HanGuo97/flute">flute</a> that supports 3-bit but it's a look-up table quantization format, it's not compatible with hqq because the look-up table is symmetric while hqq is asymmetric. 

- Regarding the MoE's groupgemm: kind of. We don't have a full fused MoE groupgemm implementation in GemLite, However, there's <a href="https://github.com/mobiusml/hqq/blob/master/hqq/utils/aria.py#L19">this version</a> we made for Aria which works fairly well. A fused groupgemm in GemLite should run faster though but requires quite some work. If there's more demand for it I can spend time on it. 

### cat538 · 2025-01-15

Wow, thank you very much for your prompt, detailed and specific answer! Your answer has completely cleared up my doubts. I'm really glad to see such an enthusiastic developer like you in the community!

I think MoE is becoming more popular. Perhaps low-precision groupgemm could be beneficial, but this is just my personal opinion. You can just follow your development plan. Thanks again!😻

### mobicham · 2025-01-15

Thank you! 
