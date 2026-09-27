# [Issue #113] Question about Quantization

source: https://github.com/dropbox/hqq/issues/113
state: closed | updated: 2024-09-03T02:19:36Z
labels: 

## 正文

Hey, it's me again! 😆 I've done testing on the HQQ pre-trained model inside the Linux system, and it is working well with the custom transformer code you gave me. Now, I want to test the quantization for this model, and this is my code. Can you give any suggestions for it?

https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B


import torch

model_id  = "akjindal53244/Llama-3.1-Storm-8B" 

```bash
compute_dtype = torch.bfloat16
device     = "cuda"
cache_path = "."

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path) 

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

dir_s = 'output/Llama-3.1-Storm-8B_HQQ_4bit'
AutoHQQHFModel.save_quantized(model, dir_s)
```

## 评论 (4)

### NEWbie0709 · 2024-08-30

 successfully ran the quantization code above, but when I tried to test it, it showed some errors. This is the code
```
`import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
#model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq' #no calib version
model_id = "akjindal53244/Llama-3.1-Storm-8B"  #calibrated version
compute_dtype = torch.bfloat16 #bfloat16 for torchao, float16 for bitblas
cache_dir = '.'
device = 'cuda:0'
model = AutoHQQHFModel.from_quantized("output/Llama-3.1-Storm-8B_HQQ_4bit")
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
patch_linearlayers(model, patch_add_quant_config, quant_config)

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
prepare_for_inference(model,backend="torchao_int4")
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

import time
t1 = time.time()
gen.generate("Write an essay about large language models", print_tokens=True)
t2 = time.time()
print('Took', t2-t1, 'secs')`
```

and this is the error shown

> Traceback (most recent call last):
>   File "/mnt/c/users/i9-4090/documents/tianyi/storm_testing.py", line 25, in <module>
>     prepare_for_inference(model,backend="torchao_int4")
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/patching.py", line 116, in prepare_for_inference
>     patch_linearlayers(model, patch_hqq_to_aoint4, verbose=verbose)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/patching.py", line 25, in patch_linearlayers
>     model.base_class.patch_linearlayers(
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py", line 154, in patch_linearlayers
>     patch_fct(tmp_mapping[name], patch_param),
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/backends/torchao.py", line 314, in patch_hqq_to_aoint4
>     hqq_aoint4_layer = HQQLinearTorchWeightOnlynt4(
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/backends/torchao.py", line 73, in __init__
>     assert (
> AssertionError: Only bfloat16 compute_dtype is supported.

### NEWbie0709 · 2024-08-30

But I managed to solve it by running the testing code directly after quantizing the model. This is the code I am using
```
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

model_id  = "akjindal53244/Llama-3.1-Storm-8B" 

compute_dtype = torch.bfloat16
device     = "cuda"
cache_path = "."

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path) 

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

prepare_for_inference(model,backend="torchao_int4")
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

import time
t1 = time.time()
gen.generate("Write an essay about large language models", print_tokens=True)
t2 = time.time()
print('Took', t2-t1, 'secs')
```

### mobicham · 2024-08-30

When you are loading a quantized model, you need to specify the `compute_dtype`  (default `torch.float16`) and the device if necessary:

```Python
model = AutoHQQHFModel.from_quantized("output/Llama-3.1-Storm-8B_HQQ_4bit", compute_dtype=torch.bfloat16, device='cuda:0')
```
`torch.bfloat16` is because you are using the `torchao_int4` backend which only supports `bfloat16`
See the examples on the HF repo: https://huggingface.co/mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib

### NEWbie0709 · 2024-08-30

Thanks! It's working 😄 
