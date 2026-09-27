# [Issue #81] AttributeError: 'HQQLinearTorchWeightOnlynt4' object has no attribute 'weight'

source: https://github.com/dropbox/hqq/issues/81
state: closed | updated: 2024-06-05T14:00:12Z
labels: 

## 正文

Hi, I install the hqq package by the command "pip install hqq" and I also try to build it from the source(pip install .). But when I  quantizer the LLaMA2-7B mode, using it to inference,  the following error occurs: 
```
File "/miniconda/envs/default_env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 822, in _setup_cache
    dtype = layer.self_attn.o_proj.weight.dtype
  File "/miniconda/envs/default_env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1709, in __getattr__
    raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
AttributeError: 'HQQLinearTorchWeightOnlynt4' object has no attribute 'weight'
```
The quantization code:
```
import torch

model_id  = "/workspace/data2/models/Llama-2-7b-hf"

compute_dtype = torch.bfloat16
device     = "cuda"
cache_path = None

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

print(f"load model...")
model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path)
print(f"load model done")

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
print(f"start quantization...")
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
print(f"quantization done")

if (quant_config['weight_quant_params']['axis'] == 0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)

from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4")

# Import custom HF generator
from hqq.utils.generation_hf import HFGenerator

# Generate
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial")

out = gen.generate("Write an essay about large language models.", print_tokens=True)
out = gen.generate("Tell me a funny joke!", print_tokens=True)
out = gen.generate("How to make a yummy chocolate cake?", print_tokens=True)
```
And the transformers I use is 4.39.1:
```
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq# pip3 list | grep transformers
transformers             4.39.1
```
Do you have any idea about this error?

Thanks! 

## 评论 (7)

### mobicham · 2024-06-04

Hi, can you try with `transformers==4.39.0`, they have changed a couple of stuff lately in transformers

### ChuanhongLi · 2024-06-04

> Hi, can you try with `transformers==4.39.0`, they have changed a couple of stuff lately in transformers

```
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq# CUDA_VISIBLE_DEVICES=7 python qwen_quant.py
load model...
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.02s/it]
load model done
start quantization...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 130/130 [00:00<00:00, 789.43it/s]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 225/225 [00:27<00:00,  8.27it/s]
quantization done
Traceback (most recent call last):
  File "/workspace/home/lich/qunantization/hqq/qwen_quant.py", line 37, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial")
  File "/workspace/home/lich/qunantization/hqq/hqq/utils/generation_hf.py", line 52, in __init__
    self.setup_cache()
  File "/miniconda/envs/default_env/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/workspace/home/lich/qunantization/hqq/hqq/utils/generation_hf.py", line 68, in setup_cache
    self.model._setup_cache(StaticCache, 1, max_cache_len=self.cache_size)
  File "/miniconda/envs/default_env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 822, in _setup_cache
    dtype = layer.self_attn.o_proj.weight.dtype
  File "/miniconda/envs/default_env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1709, in __getattr__
    raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
AttributeError: 'HQQLinearTorchWeightOnlynt4' object has no attribute 'weight'
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq#
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq#
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq# pip3 list | grep transformers
transformers             4.39.0
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq#
```
The same error!

### mobicham · 2024-06-04

Are you sure you are using the latest version from master?
```pip uninstall hqq; pip install git+https://github.com/mobiusml/hqq.git```
I think this error happens because, for some reason, this call is not executed, probably because you are using an older version i guess: https://github.com/mobiusml/hqq/blob/master/hqq/utils/patching.py#L98-L100


### ChuanhongLi · 2024-06-04

> Are you sure you are using the latest version from master? `pip uninstall hqq; pip install git+https://github.com/mobiusml/hqq.git` I think this error happens because, for some reason, this call is not executed, probably because you are using an older version i guess: https://github.com/mobiusml/hqq/blob/master/hqq/utils/patching.py#L98-L100

Sure.
```
(default_env) root@master-3104f-0:/workspace/home/lich/qunantization/hqq/examples/llama2_benchmark# pip3 list | grep hqq
hqq                      0.1.7.post3
```
So strange，when I change examples/llama2_benchmark/quant_llama2_hqq_demo.py for inference as the following codes,  it works well...  There is a difference btw them? 
```
import torch, os

os.environ["TOKENIZERS_PARALLELISM"] = "1"
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

#Settings
######################################################################################
hf_auth    = None #HuggingFace token
cache_path = ''   #cache directory to store data

#Chose a model
model_id = "/workspace/data2/models/Llama-2-7b-hf"

print(f"model = {model_id}")
#Load model on the CPU
######################################################################################
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
model     = HQQModelForCausalLM.from_pretrained(model_id, use_auth_token=hf_auth, cache_dir=cache_path)
tokenizer = AutoTokenizer.from_pretrained(model_id,       use_auth_token=hf_auth, cache_dir=cache_path)

#Quantize the model
######################################################################################
from hqq.core.quantize import *

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)

device = 'cuda:0'
compute_dtype = torch.bfloat16  # int4 kernel only works with bfloat16
model.quantize_model(quant_config=quant_config, compute_dtype=compute_dtype, device=device)


if (quant_config['weight_quant_params']['axis'] == 0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)

##########################################################################################################################################################

# Replace HQQLinear layers matmuls to support int4 mm
from hqq.utils.patching import prepare_for_inference

prepare_for_inference(model, backend="torchao_int4")

# Import custom HF generator
from hqq.utils.generation_hf import HFGenerator

# Generate
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial")

out = gen.generate("Write an essay about large language models.", print_tokens=True)
out = gen.generate("Tell me a funny joke!", print_tokens=True)
out = gen.generate("How to make a yummy chocolate cake?", print_tokens=True)
```

### mobicham · 2024-06-04

Strange, it's doing the same thing :D ! Happy it worked for you with the example provided!

### ChuanhongLi · 2024-06-05

> Strange, it's doing the same thing :D ! Happy it worked for you with the example provided!

Thanks!  Hqq has already been merged into the transformers library(version=4.41.0). It there a complete example on how to use hqq to quantizer model, save the quant model to the dir, and load it from the dir to inference using the transformers library？ I found these information to be very fragmentary, which is not convenient. 

### mobicham · 2024-06-05

We don't support model serialization yet in transformers, so you'd still need to use `AutoHQQHFModel` for saving/loading, here's the thread: https://github.com/huggingface/transformers/issues/30689

You also need to make sure you don't save a patched model, you can only save an un-patched model. 
Since quantization is very fast, why would you want to save the quantized model? You can simply quantize on-the-fly.

I prepared a complete example you can follow, but I noticed that hqq is only supported from `4.41.0` while the cache setup is broken in that version as well: https://github.com/mobiusml/hqq/blob/master/examples/hf/save_load_patch.py

Make sure you upgrade hqq, I just fixed a bug related to  `no attribute weight ` which happens when you load a quantized model.
