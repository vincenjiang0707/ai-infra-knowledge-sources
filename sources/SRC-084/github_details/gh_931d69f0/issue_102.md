# [Issue #102] Bug of the saved model when applying zero and scale quantization

source: https://github.com/dropbox/hqq/issues/102
state: closed | updated: 2024-08-09T00:52:29Z
labels: 

## 正文

Hi, I encountered a bug as title.

When I using peft to ft the low bit model and apply zero and scale quantization. The model in that script is correct ( I examined the `.linear_layer.meta` in the original script , it is correct). However, after I using `save_quantized` to save the model and using `from_quantized` to reload the model again in another script, the meta data of scale and zero is wrong. So I guess this may be the bug of `save_quantized` of metadata of zero and scale. Thx!

## 评论 (1)

### kaizizzzzzz · 2024-08-09

figured. My mistake

