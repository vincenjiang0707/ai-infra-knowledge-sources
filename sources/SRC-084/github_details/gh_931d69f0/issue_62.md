# [Issue #62] How to load quantized model with flash_attn?

source: https://github.com/dropbox/hqq/issues/62
state: closed | updated: 2024-05-06T16:30:05Z
labels: 

## 正文

Hi, I have saved a quantized model using `AutoHQQHFModel.save_quantized(model, save_dir)`.
Now I want to load the quantized model using `model = AutoHQQHFModel.from_quantized(save_dir)`. What should I do if I want to set params like `low_cpu_mem_usage`,`attn_implementation` and `torch_dtype` to conduct training.

## 评论 (2)

### mobicham · 2024-04-24

Hi @mxjmtxrm 
`low_cpu_mem_usage`: you can't, memory is managed automatically. If you want to load on a specific gpu device, you can pass `device='cuda:1'` for example

`torch_dtype`: just use `compute_dtype=torch.bfloat16` for example. 

`attn_implementation`: there's no direct way of doing it for the moment. Here are 2 solutions:
* edit the config here: https://github.com/mobiusml/hqq/blob/master/hqq/models/hf/base.py#L17
* edit the config file directly (`config.json`)

Note: the quantized model is always frozen, you need to add trainable LoRA on top of it. If you add LoRA via ,<a href="https://github.com/mobiusml/hqq/?tab=readme-ov-file#peft-training">HQQ's lora implementation</a>, you can switch the LoRA type via: `PeftUtils.cast_lora_weights(model, dtype=train_dtype)`

Let me know if that solves your issue!

### mobicham · 2024-05-06

This should fix it: https://github.com/mobiusml/hqq/commit/474f09b11c8bb791f10d1aa6b9e3277197b4a0af
