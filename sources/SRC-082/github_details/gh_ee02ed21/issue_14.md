# [Issue #14] Question about Activation-aware Scaling and its implementation

source: https://github.com/mit-han-lab/llm-awq/issues/14
state: open | updated: 2024-06-27T14:11:59Z
labels: 

## 正文

Hi, 

Thank you for your outstanding work and make it accessible to the public.

I would like to inquire about the correlation between the **activation distribution** and the chosen alpha through **grid search**.

According to the paper, AWQ aims to reduce quantization error by preserving significant weights identified by the activation distribution. However, in the implementation, alpha is selected based on the mean square error (MSE) between the original output and the output of the quantized layer.

Paper insights path:   activation distribution -> salient weight -> keep the salient weight with high precision -> reduce quantization error
Implementation path: layer-wise MSE -> alpha -> migrate activation outlier -> reduce quantization error

Is there a connection between the activation distribution and the lowest MSE? In other words, does the alpha value determined by MSE reflect the underlying activation distribution?

For example, if we found the best alpha, does it reflect the activation distribution and found the real salient weights?

Please let me know if I have missed anything or if there are any misunderstandings. 

Your clarification would be greatly appreciated :).

## 评论 (2)

### abhinavkulkarni · 2023-06-18

Hey @yiliu30,

I am not sure if this will answer your question, but here it is:

The authors do indeed posit that higher input activation for a feature channel is indicative of it being more salient.

So, when you are trying to quantize a feature matrix:

1. You'll want to boost a feature channel that has higher incoming input activation
2. You'll want to squash a feature channel that has a higher magnitude because outliers cause loss of information upon quantization (read `LLM.int8()` to understand this)

The scaling factor is thus made of two different scaling factors - one that looks to boost a feature channel based on input activation and one that looks to squash it based on its magnitude.

Through ablation studies, they find that combination of Sw & Sx > Sx alone > Sw alone

### TangHengxuan · 2024-06-27

Hi @abhinavkulkarni,
I am currently studying the AWQ paper and am having trouble locating the ablation studies you mentioned. Could you please point me to where they are discussed in the paper?
Additionally, I would appreciate it if you could clarify what you mean by "the combination of Sw & Sx" in your previous response. 
Thank you!
