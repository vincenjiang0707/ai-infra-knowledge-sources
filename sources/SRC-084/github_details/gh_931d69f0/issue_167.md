# [Issue #167] AutoHQQHFModel.save_to_safetensors() failed

source: https://github.com/dropbox/hqq/issues/167
state: closed | updated: 2025-10-27T17:47:48Z
labels: 

## 正文

Following https://github.com/dropbox/hqq, but it failed. Seem quite unblievable.

Here is the code:
#Load the model on CPU
from transformers import AutoModelForCausalLM
import torch
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import BaseQuantizeConfig

model_id = '/home/lf/models/Qwen3-0.6B'
save_dir = '/home/lf/models/Qwen3-0.6B-hqq-4bits'

compute_dtype = torch.bfloat16 
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

from hqq.models.hf.base import AutoHQQHFModel

#Save: Make sure to save the model BEFORE any patching
AutoHQQHFModel.save_quantized(model, save_dir)

#Save as safetensors (to be load via transformers or vllm)
AutoHQQHFModel.save_to_safetensors(model, save_dir)

#Load
model = AutoHQQHFModel.from_quantized(save_dir)

here is the error:
/usr/bin/env /home/lf/q/bin/python /home/lf/.vscode-server/extensions/ms-python.debugpy-2025.14.1/bundled/libs/debugpy/adapter/../../debugpy/launcher 51737 -- hqq-quantize.py 
`torch_dtype` is deprecated! Use `dtype` instead!
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 143/143 [00:00<00:00, 337.04it/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 197/197 [00:04<00:00, 44.23it/s]
mkdir: cannot create directory ‘/home/lf/models/Qwen3-0.6B-hqq-4bits/’: File exists
Traceback (most recent call last):
  File "/home/lf/codes/q/hqq-quantize.py", line 25, in <module>
    AutoHQQHFModel.save_to_safetensors(model, save_dir)
  File "/home/lf/q/lib/python3.12/site-packages/hqq/models/base.py", line 599, in save_to_safetensors
    total_size += tensors[key].numel() * tensors[key].element_size()
                  ^^^^^^^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'numel'

## 评论 (3)

### mobicham · 2025-10-26

Hello, it works fine, you just copy-pasted the code which saves twice: 
```Python
#Load the model on CPU
from transformers import AutoModelForCausalLM
import torch
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import BaseQuantizeConfig

model_id = 'Qwen/Qwen3-0.6B'
save_dir = './Qwen3-0.6B-hqq-4bits'

compute_dtype = torch.bfloat16
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Save: Make sure to save the model BEFORE any patching
AutoHQQHFModel.save_quantized(model, save_dir)

#Save as safetensors (to be load via transformers or vllm)
#AutoHQQHFModel.save_to_safetensors(model, save_dir)

#Load
model_quant = AutoHQQHFModel.from_quantized(save_dir)
```

Alternatively, you can use transformers directly
```Python
import torch
from transformers import AutoModelForCausalLM, HqqConfig

model_id = 'Qwen/Qwen3-0.6B'
save_dir = './Qwen3-0.6B-hqq-4bits'
device = 'cuda:0'
compute_dtype = torch.bfloat16

quant_config = HqqConfig(nbits=4, group_size=64)

model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=compute_dtype, 
    device_map=device, 
    quantization_config=quant_config
)

model.save_pretrained(save_dir)

model_quant = AutoModelForCausalLM.from_pretrained(save_dir)
```

### notfreemanliu-bot · 2025-10-27

@mobicham Thanks for your timely help! There is a follow-up issue. Details below.
This works without any problem.
```
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=compute_dtype, 
    device_map=device, 
    quantization_config=quant_config
)

model.save_pretrained(save_dir)
```

This generated the model but the model failed to be loaded by vllm.
```
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

from hqq.models.hf.base import AutoHQQHFModel

#Save: Make sure to save the model BEFORE any patching
# AutoHQQHFModel.save_quantized(model, save_dir)

#Save as safetensors (to be load via transformers or vllm)
AutoHQQHFModel.save_to_safetensors(model, save_dir)
```

Further debugging shows that the generate model is suspicious. The config.json does not include quantizaiton_config. Here is it:
```
{
  "architectures": [
    "Qwen3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": 3072,
  "layer_types": [
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention"
  ],
  "max_position_embeddings": 40960,
  "max_window_layers": 28,
  "model_type": "qwen3",
  "num_attention_heads": 16,
  "num_hidden_layers": 28,
  "num_key_value_heads": 8,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 1000000,
  "sliding_window": null,
  "tie_word_embeddings": true,
  "transformers_version": "4.56.2",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}
```
vllm loading error is:
```
(EngineCore_DP0 pid=395378) ERROR 10-27 15:54:43 [core.py:708]   File "/home/lf/q/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 437, in load_weights
(EngineCore_DP0 pid=395378) ERROR 10-27 15:54:43 [core.py:708]     param = params_dict[name]
(EngineCore_DP0 pid=395378) ERROR 10-27 15:54:43 [core.py:708]             ~~~~~~~~~~~^^^^^^
(EngineCore_DP0 pid=395378) ERROR 10-27 15:54:43 [core.py:708] KeyError: 'layers.0.mlp.down_proj.W_q'
(EngineCore_DP0 pid=395378) Process EngineCore_DP0:
```


### mobicham · 2025-10-27

You should only use the official transformers implementation in order to load the model in vLLM
```Python
import torch
from transformers import AutoModelForCausalLM, HqqConfig

model_id = 'Qwen/Qwen3-0.6B'
save_dir = './Qwen3-0.6B-hqq-4bits'
device = 'cuda:0'
compute_dtype = torch.bfloat16

quant_config = HqqConfig(nbits=4, group_size=64)

model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=compute_dtype, 
    device_map=device, 
    quantization_config=quant_config
)

model.save_pretrained(save_dir)
```
