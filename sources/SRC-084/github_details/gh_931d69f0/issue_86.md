# [Issue #86] Activation quantization

source: https://github.com/dropbox/hqq/issues/86
state: closed | updated: 2024-11-01T18:45:02Z
labels: 

## 正文

Can activation quantization also be introduced in Hqq as well? Or if not, is there any process/method can further quantize the activation after using Hqq to quantize the weight?

## 评论 (9)

### mobicham · 2024-06-21

Technically possible, but hqq is for asymmetric quantization not symmetric, and the available kernels like <a href="https://github.com/microsoft/BitBLAS">BitBLAS</a> only support int8 activations as far as I know, which can only be used for symmetric activation quantization. 
Have you tried int8  (row-wise) symmetric quantization for the activations and n-bit HQQ quantized weights ? Should work ok, I  have tried that on Llama2 a while ago and it was working fine.


### kaizizzzzzz · 2024-06-26

Thanks for you valuable response! I still has some questions: so what technology, or more specifically, what repo will you use for activation quantization? Or you just simply add "int8 (row-wise) symmetric quantization for the activations" in hqq repo, and fine-tuning this activation quantization with hqq's weight quantization at the same time? 

I'm happy that the activation could be quantized to 8 bit, and I'm more interested in if the activation could be further quantized to 4 bits or even two bits? Is this theoretically hard to realize for such a low bit activation? Thanks!

### mobicham · 2024-06-26

To quantize the activations, you can simply do some dynamic quantization like:
``` Python
# Quantize 
axis=1;
x_scale = 127. / x.abs().amax(axis=axis, keepdim=True);
x_int8 = (x * x_scale).to(torch.int8); 
# Dequantize
x_deq = (x_int8.to(x_scale.dtype) / x_scale);
```
No need to fine-tune I think, but we need an optimized cuda kernel that works with int8 activations / int4 weights for example. 
That quantization step, since it's done on-the-fly, actually slows down everything. But this will work great if the whole model works with int8 (including the KV cache and the rest of the layers).

Regarding int4 activations, I think the results will be pretty bad with simple dynamic quantization. One solution would be to implement hqq inside the cuda kernel and it will quantize the activations in the shared memory, but it requires a lot of work.
Otherwise, somekind of quantization-aware training to make sure that the activations are easily quantizable to 4-bit.
You can also take a look at : https://github.com/spcl/QuaRot

### kaizizzzzzz · 2024-06-26

Thank you so much for your detailed response! I appreciate the clarity you provided. Is there any method can support W1A4 (W1A2) quantization done before inference? Not leaving the activation quantization on-the-fly, QAT is acceptable! Thanks!

### mobicham · 2024-06-26

I haven't seen that yet, it's a bit too extreme, W4A4 like QuaRot seems to work, lower than that, maybe W3A4 could work with QA. By the way, for A8W4 for example, you could try BitBlas: https://github.com/microsoft/BitBLAS/, but I am not sure they support grouping for int8 activations, they do for fp16 activations. 

### kaizizzzzzz · 2024-06-26

I see, thanks

### kaizizzzzzz · 2024-06-27

Btw, what is the `"compute_dtype"` argument in HQQ? Does it mean the original precision of the weight? We set it as torch.float16 all the time? Thanks!

### mobicham · 2024-06-27

Yes, it's compute precision, if the inputs are float16, `compute_dtype` should be float16 as well, same applies to float32 and bfloa16.

### kaizizzzzzz · 2024-06-27

Thanks!
