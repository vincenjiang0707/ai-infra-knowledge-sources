# [Issue #105] Warning: failed to import the BitBlas backend

source: https://github.com/dropbox/hqq/issues/105
state: closed | updated: 2024-08-25T18:39:52Z
labels: 

## 正文

I installed bitblas with 'pip install bitblas'

However, running an example shows the following warning:

'Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS

Any suggestions ?  

## 评论 (7)

### mobicham · 2024-08-16

Strange! Are you able to import bitblas in Python ?

### jinz2014 · 2024-08-16

It is caused by OSError: Multi-gpu environment must set `CUDA_DEVICE_ORDER=PCI_BUS_ID`.   PCI_BUS_ID could be queried with nvidia-smi ?



### mobicham · 2024-08-16

You can select the GPUs you want to use via `CUDA_VISIBLE_DEVICES=0 ipython3` 
What model and GPUs are you trying to use ? If you want to use multi-gpu runtime, I think it's broken when you load a model via `.from_quantized`, but I think it should work fine if you quantize on-the-fly

### jinz2014 · 2024-08-16

I loaded a quantized model via 'from_quantized" without knowing the multi-gpu issue. However, running the following command still shows the warning

CUDA_VISIBLE_DEVICES=0  python main.py  

### mobicham · 2024-08-17

Can you please share a code snippet of what model you are trying to use and your system settings (what gpus does your machine have?)

### jinz2014 · 2024-08-17

The code snippet is from https://huggingface.co/mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib 

The system has two Nvidia A100 GPUs. 

### mobicham · 2024-08-17

Strange, try this:
```Python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
#model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq' #no calib version
model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib' #calibrated version

compute_dtype = torch.bfloat16 #bfloat16 for torchao, float16 for bitblas
device    = 'cuda:0'
cache_dir = '.'
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
patch_linearlayers(model, patch_add_quant_config, quant_config)

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
prepare_for_inference(model, backend="torchao_int4") 
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter 
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

gen.generate("Write an essay about large language models", print_tokens=True)
gen.generate("Tell me a funny joke!", print_tokens=True)
gen.generate("How to make a yummy chocolate cake?", print_tokens=True)
```
