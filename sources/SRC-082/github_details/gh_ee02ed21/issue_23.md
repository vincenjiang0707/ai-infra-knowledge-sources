# [Issue #23] How to measure the speedup of W4A16 kernel like Figure 6？

source: https://github.com/mit-han-lab/llm-awq/issues/23
state: open | updated: 2024-08-12T05:39:08Z
labels: 

## 正文

Hi,

Thanks for your outstanding work.  I have tested the quantized model using the W4A16 kernel on the WikiText2 datasets. Specially, the WikiText2 validation datasets is split into non-overlapping segments of width 2048. I have observed that the W4A16 kernel significantly reduces memory usage. However, the actual speed is even slow than the W16A16 in my setup. 

For example, for LLaMa-30B, the test time of W16A16 on the WikiText2 validation datasets is 177 seconds, whereas the test time increase to 420 seconds when using the W4A16 kernel.

I would like to know how to accurately measure the speedup. Am I overlooking something?

Thank you.

## 评论 (5)

### hych2020 · 2023-07-03

+1

### Jiang-Stan · 2023-07-03

+1

### Oliver-ss · 2023-07-03

+1

### Sakits · 2023-07-03

Hi all, thank you for your interests in our work!

In our speed benchmark, we based on the generation stage starting from zero context and measured the median latency of generating 2048 tokens, since evaluating speed using the WikiText2 perplexity evaluation may not accurately reflect the practical usage of LLM.

And it's necessary to replace some inefficient FP16 kernels (such as layernorm and rotary position embedding) in the HuggingFace implementation when testing the speed. At present, we have not released a version for speed testing yet. Please stay tuned for our further updates.


### kiucho · 2024-08-12

For real quantization, I figured out that it reduces memory but much slower than FP16 inference(pseudo quantization) even when the quantized module has been changed to WQLinear module which need awq_inference_engine. In ppl evaluation code, can't we see speedup cuz of layer norm and rotary position embedding?
