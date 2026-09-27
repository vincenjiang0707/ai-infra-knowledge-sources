# [Issue #65] Issue with torchao patching with loaded model

source: https://github.com/dropbox/hqq/issues/65
state: closed | updated: 2024-05-08T09:05:55Z
labels: bug

## 正文

Basically, when I quantize a model and patch it to use torchao_int4 ops, it works, but if I then save this model and load it again the patching fails. Am I doing something wrong ? I have been trying to follow the instructions.


This works:

```python
import torch
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer

#Model and setttings
model_id      = 'mistralai/Mixtral-8x22B-Instruct-v0.1'
compute_dtype = torch.bfloat16
device        = 'cuda:0'

#Load model on the CPU
######################
model     = HQQModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id) 

#Quantize the model
######################
from hqq.core.quantize import *
quant_config = BaseQuantizeConfig(nbits=4, group_size=64)
model.quantize_model(quant_config=quant_config, compute_dtype=compute_dtype, device=device) 

#Save the quantized model
model.save_quantized(save_dir="./quantized_mixtral_huge_attempt2/")

#Load from local directory or Hugging Face Hub on a specific device
#model = HQQModelForCausalLM.from_quantized(save_dir_or_hfhub, device='cuda', compute_dtype=torch.bfloat16)

from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4") #torchao's int4mm kernel, use compute_dtype=bfloat16
#prepare_for_inference(model, backend="marlin", allow_merge=True) #marlin int4 kernel.

model = torch.compile(model, mode='max-autotune')

#Text Generation
prompt = "<s> [INST] How do I build a car? [/INST] "

inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
outputs = model.generate(**(inputs.to('cuda')), max_new_tokens=1000)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Output:

```
Loading checkpoint shards: 100%|██████████| 59/59 [33:36<00:00, 34.18s/it]
100%|██████████| 56/56 [00:01<00:00, 41.41it/s]
100%|██████████| 56/56 [16:14<00:00, 17.40s/it]
Setting `pad_token_id` to `eos_token_id`:2 for open-end generation.
How do I build a car? 1. Gather resources: You will need a variety of tools, materials, and equipment to build a car. This includes a chassis, engine, transmission, suspension, brakes, wheels, tires, body panels, interior components, and electrical systems. You will also need specialized tools such as welding equipment, a lift, and diagnostic tools.

... truncated
```

However, when I then try to load the quantized and saved model the patching step fails:


```python
import torch
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer

model_id      = 'mistralai/Mixtral-8x22B-Instruct-v0.1'
tokenizer = AutoTokenizer.from_pretrained(model_id) 

#Load from local directory or Hugging Face Hub on a specific device
model = HQQModelForCausalLM.from_quantized("./quantized_mixtral_huge/", device='cuda', compute_dtype=torch.bfloat16)

from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4") #torchao's int4mm kernel, use compute_dtype=bfloat16
#prepare_for_inference(model, backend="marlin", allow_merge=True) #marlin int4 kernel.

model = torch.compile(model, mode='max-autotune')

#Text Generation
prompt = "<s> [INST] How do I build a car? [/INST] "

inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
outputs = model.generate(**(inputs.to('cuda')), max_new_tokens=1000)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

```
Traceback (most recent call last):
  File "/home/rohitg/vision_llm/scratch/infer_saved_llm.py", line 12, in <module>
    prepare_for_inference(model, backend="torchao_int4") #torchao's int4mm kernel, use compute_dtype=bfloat16
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/utils/patching.py", line 74, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4)
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/utils/patching.py", line 13, in patch_linearlayers
    model.base_class.patch_linearlayers(model, fct, dict([(k, patch_param) for k in model.base_class.get_linear_tags()]), verbose=verbse)
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/models/hf/mixtral.py", line 53, in patch_linearlayers
    layers[i].self_attn.q_proj = patch_fct(
                                 ^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/backends/torchao.py", line 243, in patch_hqq_to_aoint4
    w_q_config = hqq_layer.quant_config['weight_quant_params']
                 ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

```

## 评论 (8)

### mobicham · 2024-05-04

I see, that's actually a bug, thanks for reporting, I will fix this soon.
Work around, after you load, before you apply the patching, do this:
```Python
from hqq.utils.patching import patch_linearlayers, patch_add_quant_config
patch_linearlayers(model, patch_add_quant_config, quant_config)
# where quant_config is the quant config you used to quantize the model
```

Your quant settings are also not correct to work with that backend, as the documentation says, you need to use `axis=1`. It will not use the faster backend if you feed it the default `axis=0`. Try:
```Python
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
```


### rohit-gupta · 2024-05-04

Oh thanks for the help ! 

### mobicham · 2024-05-06

I think this should fix it: https://github.com/mobiusml/hqq/commit/3a62b11a82f1ab81b3f902a224ac11cdc2cbd1ab

Let me know if you still have the same issue

### rohit-gupta · 2024-05-07

@mobicham this is tangentially related, but the new quantization config caused the model's size to increase from 73 to 75GB which makes it no longer fit on a single A100, so I was trying to use 2 A6000s. Is that possible to do in HQQ ? I tried passing `device_map` but it seems unlike the HuggingFace version HQQ doesn't support that.


```
Traceback (most recent call last):
  File "/home/rohitg/vision_llm/scratch/infer_saved_llm.py", line 11, in <module>
    model = HQQModelForCausalLM.from_quantized("./quantized_mixtral_huge/", device_map='auto', compute_dtype=torch.bfloat16)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: HQQWrapper.from_quantized() got an unexpected keyword argument 'device_map'

```

### mobicham · 2024-05-07

Oh I see, because by default it quantizes the meta-data, and the settings I shared turned them off. You have two options: 
* Option 1: use the native backends in hqq that support all nbits and scale/zero quantization, but it is a bit slower. Since you are using Mixtral, you can quantize the MoEs to lower bits and fit everything even in a lower-end gpu, try something like this:
```Python 
axis = 0
attn_params    = BaseQuantizeConfig(nbits=4, group_size=64, axis=axis)
experts_params = BaseQuantizeConfig(nbits=3, group_size=64, axis=axis)

quant_config = {}
#Attention
quant_config['self_attn.q_proj'] = attn_prams
quant_config['self_attn.k_proj'] = attn_prams
quant_config['self_attn.v_proj'] = attn_prams
quant_config['self_attn.o_proj'] = attn_prams
#Experts
quant_config['block_sparse_moe.experts.w1'] = experts_params
quant_config['block_sparse_moe.experts.w2'] = experts_params
quant_config['block_sparse_moe.experts.w3'] = experts_params

from hqq.utils.patching import prepare_for_inference
HQQLinear.set_backend(HQQBackend.ATEN if (axis==0) else HQQBackend.PYTORCH)
prepare_for_inference(model)

torch.compile(...)
```
With settings like this, you'd expect a drop of about ~1-1.5 point in performance: https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-attn-4bit-moe-3bit-metaoffload-HQQ


Option 2:
Multi-gpu: just pass `device=['cuda:0', 'cuda:1']` here:
```Python
model.quantize_model(quant_config=quant_config, compute_dtype=compute_dtype, device=['cuda:0', 'cuda:1']) 
```
You can also do it with transformers directly (`pip install git+https://github.com/huggingface/transformers.git`) for that you need to use `HqqConfig` as explained here: https://huggingface.co/docs/transformers/main/en/quantization#hqq
I think multi-gpu runtime with the hqq lib is faster than transformers, at least with the models I tried. Let me know !


### rohit-gupta · 2024-05-07

So question about option 2, can I utilize multi-GPU with quantized weights that have already been saved ?

`HQQModelForCausalLM.from_quantized(device=['cuda:0', 'cuda:1'])` 

results in errors:

```Traceback (most recent call last):
  File "/home/rohitg/vision_llm/scratch/infer_saved_llm.py", line 11, in <module>
    model = HQQModelForCausalLM.from_quantized("./quantized_mixtral_huge/", device=['cuda:0', 'cuda:1'], compute_dtype=torch.bfloat16)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/engine/base.py", line 86, in from_quantized
    model = cls._get_hqq_class(arch_key).from_quantized(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/models/base.py", line 469, in from_quantized
    cls.patch_model(
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/models/base.py", line 185, in patch_model
    cls.patch_nonlinearlayers(model, patch_nonlinear_fct, verbose=verbose)
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/models/hf/mixtral.py", line 26, in patch_nonlinearlayers
    model.lm_head = patch_fct(model.lm_head)  ###
                    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/c3-0/rohitg/mforge/envs/quantllm/lib/python3.11/site-packages/hqq/models/base.py", line 459, in _load_module
    state_dict[key].to(
TypeError: to() received an invalid combination of arguments - got (non_blocking=bool, dtype=torch.dtype, device=list, ), but expected one of:
 * (torch.device device, torch.dtype dtype, bool non_blocking, bool copy, *, torch.memory_format memory_format)
 * (torch.dtype dtype, bool non_blocking, bool copy, *, torch.memory_format memory_format)
 * (Tensor tensor, bool non_blocking, bool copy, *, torch.memory_format memory_format)```



### mobicham · 2024-05-08

@rohit-gupta multi-gpu was only implemented for the quantization call. Let me see how to add that to the `from_quantized` call.

### mobicham · 2024-05-08

@rohit-gupta I created a separate issue for this since it's not related to the original thread: https://github.com/mobiusml/hqq/issues/71 . I will give it a try tomorrow.
