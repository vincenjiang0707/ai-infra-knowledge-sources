# [Issue #139] Quantized aria with vllm serving

source: https://github.com/dropbox/hqq/issues/139
state: closed | updated: 2025-04-09T10:57:42Z
labels: 

## 正文

Excellent work! I have 2 questions.
Is it possible to host quantized aria with vllm now? 
How can i save quantized aria?

## 评论 (2)

### mobicham · 2025-01-06

Thank you!

I haven't followed much what's going with Aria, just checked and it looks like it's merged in Hugging Face, but the example is still using `trust_remote=True` hm.  

The main issue is that in Aria, the quantized MoEs are a custom layer, not `HQQLinear` ,while the integration in HF and VLLM only supports `HQQLinear`, so unless the quantized MoEs are replaced on the fly-on-the while loading, even with saving I don't think it's gonna work out-of-the-box with the current code.

Unfortunately, this will require some work/testing and I don't have enough time on my plate, but happy to guide you. Which one is more important to you: being able to run it in VLLM or being able to save/load to use with HF?
Either way, I think if you rewrite  <a href="https://github.com/mobiusml/hqq/blob/master/hqq/utils/aria.py#L19">this</a> to use `HQQLinear` it could work actually with some post-loading patching function.
Basically the idea is to only use supported layers before saving - in this case the quantized MoEs will be a torch.nn.Sequential of HQQLinear layers instead of HQQGroupedGemm. Then after loading, we replace the forward pass call of the Sequential modules with the correct call via a patching function. 

### argentum047101 · 2025-01-07

Thank you for fast reply! Got the idea. Will try it out.
