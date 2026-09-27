# [Issue #109] zero and scale quant

source: https://github.com/dropbox/hqq/issues/109
state: closed | updated: 2024-08-26T07:41:46Z
labels: 

## 正文

Due to the update. Now loading model with zero and scale quant will trigger error

## 评论 (1)

### mobicham · 2024-08-26

Yes that is correct. Unfortunately, we need to drop support for quantizing the scale and zero parameters because it makes things too complicated to store everything in safetensors. Additionally, the optimized kernels for fast decoding do not support quantized scales/zeros which will slow down inference. 
If you wish to sill save/load quant zero/scales you can use `https://github.com/mobiusml/hqq/releases/tag/v0.1.8`, after that, it will not work. Will  update the documentation once everything is up-to-day with transformers. We might get back to it to add support for scale/zeros if it's something of importance.
