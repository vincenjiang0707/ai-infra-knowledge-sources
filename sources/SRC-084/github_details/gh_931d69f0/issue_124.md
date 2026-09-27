# [Issue #124] Group size and restrictions: documentation and implementation contradict each other

source: https://github.com/dropbox/hqq/issues/124
state: closed | updated: 2025-04-09T10:58:45Z
labels: 

## 正文

According to readme:

 [group_size (int): no restrictions as long as weight.numel() is divisible by the group_size](https://github.com/mobiusml/hqq/blob/085c15b7c393434db39d2f78a31e8406b3290557/Readme.md?plain=1#L67) however [group_size should be divisible by 8](https://github.com/mobiusml/hqq/blob/085c15b7c393434db39d2f78a31e8406b3290557/hqq/core/quantize.py#L1064)

(Zamba2 1.2B has `torch.Size([8512, 2048])` linears. With readme in mind, I intentionally tried to make `group size = 38` (64 was to imprecise, 32 didn't decrease memory too much). 

So readme probably should has this restriction for divisibility or there should be no assert in code.




## 评论 (5)

### mobicham · 2024-10-16

The readme is correct, you are not seeing a reduction in memory because your group-size is too small, you need to use a larger group-size. 

Ideally, your group-size should be a power of 2 (32, 64, 128, ...) or channel-wise via `group_size=None`.
You also need to check  which group-sizes are supported by the fast backends (torchao, bitblas, etc.), because each fast backend supports a different set of group-size, and that constraint is independent of the quantization algorithm.

Why would you like to quantize a 1B model? The model is already too small, quantization is useful for larger models.


### Maykeye · 2024-10-16

> The readme is correct,

Then assert is incorrect?

As if "no restrictions as long as weight.numel() is divisible by the group_size"  is correct, I must be able to use group size 38 for [8512, 2048]: 17432576 / 38 = 458752

> Why would you like to quantize a 1B model? 

Proof of concept to see what parts can be quantized making model smaller without making model too bad.
1B  loads  instantly.  7B takes quite a while, barely fits in 16GB VRAM, and takes time to run compared to 1B.  



### mobicham · 2024-10-16

Using a group-size of 38 is an edge-case which is incompatible with the fast backends. As a rule of thumb, all matrix/vector shapes should be ideally powers of 2, so try to choose from 32, 64, 128, etc. I can change the readme to only include powers of 2 / out_features size + mention the fast backends to avoid any confusion :+1:  

7B like a Llama2-7B should take ~5GB of VRAM and should run at 170 tokens/sec on a 4090. Would you mind sharing your code to quantize and run? I can assist you to run it properly, start with this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py

### Maykeye · 2024-10-17

>  to only include powers of 2 / out_features size + mention the fast backends to avoid any confusion 👍

Yeah, that would help avoid confusion

>Would you mind sharing your code to quantize and run? 

It actually would be helpful. 

In general non transformers documentation would be helpful as it's where hqq can shine the most. Where exllama and gguf can't be used easily if it all, with HQQ it's just possible to replace nn.Linears after loading the model without finetuning it.

I'm targeting  [zamba2 adapted to HF transformers instead of their fork](https://github.com/Maykeye/Zamba2_HQQ/blob/main/makezamba2-7b-quantie.ipynb). Zamba2 7B version  has 81 layers of mamba2 and mamba2 has two linears that make majority of weights. 

Also the  culprit of the slowness was found: most backends(aten, torch, torch_compile).
At least on my laptops's 3080 with 16GB vram only torchao_int4 runs as fast as bf16. On 7B model to generate ~1K tokens ATEN takes ~5 minutes. AO4 and BF16 both take around a minute.  

I didn't test backends pytorch/pytorch_compile on 7B, but on 1.2B they already were too slow, to the point if in each mamba block instead of quantizing in_proj and out_proj, I quantizied just in_proj, the speed doubled.

Also I didn't see `from hqq.utils.generation_hf import HFGenerator` before that hqq_lib_demo, but it seems it's tied to usual architecture: Zamba uses very own custom cache, so when I use HFGenerator/  static cache doesn't work.



### mobicham · 2024-10-17

`HQQLinear.set_backend` will not speed-up inference much, that's the backend for the dequantization op, mainly used as a fallback solution for inference, but mostly useful for training. 

What you want is the backend for faster inference, which is enabled via  `prepare_for_inference(model, backend=infer_backend, verbose=True)` . Valid infer_backend here would be `torchao_int4` or `bitblas`, on top of that you need torch.compile with static cache via `HFGenerator`, otherwise you'll not see that 3-4 speed-up.

As you said, `HFGenerator` is for transformers so it wouldn't work. Instead try to compile the forward pass of the model:
```Python
model.forward = torch.compile(model.forward, mode="reduce-overhead", fullgraph=True )
```
You'll have to run it for a couple of iterations to warm-up. I saw there are some people trying to refactor Mamba for torch.compile, so maybe that work would be useful. 
