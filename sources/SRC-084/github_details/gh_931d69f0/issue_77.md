# [Issue #77] prepare_for_inference error

source: https://github.com/dropbox/hqq/issues/77
state: closed | updated: 2024-06-05T13:57:32Z
labels: 

## 正文

Hi! I have quantized the Llama-2-7b-hf model with the config as follows:
```python
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
```
When I try to use torchao backend to do some testing:
```python
prepare_for_inference(model, backend="torchao_int4") 
```
This error appears:
Exception: Invalid parameters: Both quant_config and linear_layer are None.

What should I do in order to use the torchao backend?

## 评论 (17)

### mobicham · 2024-05-29

Hey! I have never seen that error, I just tried on a 3090 and it works fine:
```Python
import torch, os

cache_path     = '.'
model_id       = "meta-llama/Llama-2-7b-chat-hf"
compute_dtype  = torch.bfloat16 #int4 kernel only works with bfloat16
device         = 'cuda:0'

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel
from hqq.core.quantize import *

tokenizer    = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path)
model        = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype, attn_implementation="sdpa")
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)

#Quantize 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Set default backends, to compare with int4mm
if(quant_config['weight_quant_params']['axis']==0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)

#Replace HQQLinear layers matmuls to support int4 mm
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4")
```



### BeichenHuang · 2024-05-29

Is that means I need to set the default backends as first step like this:
```python
if(quant_config['weight_quant_params']['axis']==0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)
```
and then use torchao as follow:
```python
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4")
```
Am I understand it right?

### mobicham · 2024-05-29

You can either do it before or after, it ensures that if there's some layer that is not compatible with the torchao backend (not 4-bit and/or uses axis=0), it will fallback to the default backend. If you don't do that, it will still work fine, just a bit slower on older gpus.

### BeichenHuang · 2024-05-29

Sure. I try to run exactly the same code as yours, but I see this issue:

Traceback (most recent call last):
  File "/u/bhuang4/mixtral_offloading/llama2/test.py", line 28, in <module>
    prepare_for_inference(model, backend="torchao_int4")
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/utils/patching.py", line 87, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/utils/patching.py", line 16, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/models/hf/llama.py", line 44, in patch_linearlayers
    layers[i].self_attn.q_proj = patch_fct(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 320, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 193, in process_hqq_quants
    self.weight_int4pack = torch.ops.aten._convert_weight_to_int4pack(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/torch/_ops.py", line 755, in __call__
    return self._op(*args, **(kwargs or {}))
RuntimeError: _convert_weight_to_int4pack_cuda is not available for build.

Do you know what is the problem?

### mobicham · 2024-05-29

Make sure you have:
* A relatively modern gpu (3090 or 4090 should work fine)
* CUDA 12.x or higher
* a newer Pytorch version (nightly recommended) 

This is not related to the hqq lib, it's related to Pytorch.

### BeichenHuang · 2024-05-31

I update the CUDA version and able to run your code now. But I still get this error:
Exception: Invalid parameters: Both quant_config and linear_layer are None.

I think the difference is I try to load the saved quantized model and do testing. Here is the code for quantizing:
```python
import torch

model_id  = "meta-llama/Llama-2-7b-hf" 

compute_dtype = torch.bfloat16
device     = "cuda"
cache_path = "/scratch/bcjw/bhuang4/cache"

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path) 

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

dir_s = '/scratch/bcjw/bhuang4/llama2/llama2_HQQ_4bit'
AutoHQQHFModel.save_quantized(model, dir_s)
```

And here is the code for testing:
```python
model = AutoHQQHFModel.from_quantized(dir_s)
tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token, cache_dir=cache_path) 


HQQLinear.set_backend(HQQBackend.PYTORCH)

prepare_for_inference(model, backend="torchao_int4") 
```

And get that error at:
```python
prepare_for_inference(model, backend="torchao_int4") 
```
Could you please help?

### mobicham · 2024-05-31

Oh I see! The reason you get that error is because, during the patching phase, it needs to check the quantization config of each layer to see if it's compatible with the backend (4-bit / axis=1 in the case of `torchao_int4`). When you save the model, it doesn't save the quant config. So you have two solutions:

- Don't save the model and quantize on the fly: should be ok since quantization takes ~15 secs.
- When you load the model, do this: 

```Python
from hqq.utils.patching import prepare_for_inference, patch_linearlayers, patch_add_quant_config
patch_linearlayers(model, patch_add_quant_config, quant_config)
prepare_for_inference(model, backend="torchao_int4") 
```

This will add the quant_config to the layers and it should work.

FYI: `HFGenerator` is broken in the new version of transformers because they removed the `_setup_cache()` call: https://github.com/mobiusml/hqq/blob/master/examples/backends/torchao_int4_demo.py#L47C7-L47C18
You can either try with an older version of transformers or use HF's official `generate` function, but it will be slow everytime the prompt length changes

### BeichenHuang · 2024-06-01

I try the first solution, and quantize the model every time and it is good! Thanks for your help! 
I further apply HQQ to quantize the Mixtral-7B*8 model to 4bit, and try to load with torchao backend. There is a CUDA OOM error at this function:
```python
prepare_for_inference(model, backend="torchao_int4") 
```
I am using a A100 with 40G VRAM, and I the quantized model is around 23GB, which is smaller than the VRAM. Is there any process that prepare_for_inference takes a lot VRAM? Or how can I use the Mixtral-7B*8 model with torchao backend?

### mobicham · 2024-06-02

@BeichenHuang well it should work fine, I am not sure why you get OOM, do you get this issue even when you do?
```prepare_for_inference(model) ```
Or just when you use `backend="torchao_int4"`

### BeichenHuang · 2024-06-03

It only happens to backend="torchao_int4". I test with prepare_for_inference(model), and it is good

### mobicham · 2024-06-03

I see, I think it's not properly freeing the original HQQLinear layer after deletion. Can you the following:
```Python
import gc
import hqq.backends.torchao 


def patch_hqq_to_aoint4(layer, patch_params):
    hqq_layer = None
    if type(layer) is HQQLinear:
        hqq_layer = layer
    if type(layer) is HQQLinearLoRA:
        hqq_layer = layer.linear_layer

    if hqq_layer is None:
        return layer

    if hqq_layer.meta["nbits"] != 4 or hqq_layer.meta["axis"] != 1:
        print("Skipping aoint4 conversion for ", hqq_layer.name)
        return layer

    quant_config = getattr(hqq_layer, "quant_config", None)

    hqq_aoint4_layer = HQQLinearTorchWeightOnlynt4(
        None,
        quant_config=quant_config,
        compute_dtype=hqq_layer.compute_dtype,
        device=hqq_layer.device,
        del_orig=False,
        initialize=False,
        padding=False,
    )
    hqq_aoint4_layer.initialize_with_hqq_quants(
        hqq_layer.W_q, hqq_layer.meta, hqq_layer.bias
    )

    del hqq_layer
    
    torch.cuda.empty_cache()
    gc.collect()

    if type(layer) is HQQLinear:
        return hqq_aoint4_layer

    if type(layer) is HQQLinearLoRA:
        layer.linear_layer = hqq_aoint4_layer

    return layer


torchao.patch_hqq_to_aoint4 = patch_hqq_to_aoint4

...
prepare_for_inference(model, backend="torchao_int4")

```

It's gonna run `gc.collect()` after each linear layer replacement, which is a bit slow, but it should fix this memory issue hopefully.
Can you please run it and confirm if it works?


### BeichenHuang · 2024-06-03

It works now! Thanks for helping!

### mobicham · 2024-06-03

Cool, then I am gonna push this change to the master branch: https://github.com/mobiusml/hqq/commit/f49d7b7bca2336320bdcd9ba2ebac2a693abf727

### BeichenHuang · 2024-06-05

Sorry I think we have to reopen the OOM problem. When I testing, I was still using the llama2-7B, which does not have the OOM problem originally. The OOM still happens to the Mixtral 7B*8, the fix was not working. Here is thet OOM error:

```
Traceback (most recent call last):
  File "/u/bhuang4/mixtral_offloading/doQuant_HQQ/doEval_HQQ_4bit_p.py", line 82, in <module>
    prepare_for_inference(model, backend="torchao_int4") 
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/utils/patching.py", line 87, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/utils/patching.py", line 16, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/models/hf/mixtral.py", line 68, in patch_linearlayers
    layers[i].block_sparse_moe.experts[k].w1 = patch_fct(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 320, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 190, in process_hqq_quants
    W_q_torch, scales_torch, zeros_torch = self.hqq_quants_to_torch_quants(
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/scratch/bcjw/bhuang4/anaconda3/envs/doHQQ/lib/python3.10/site-packages/hqq/backends/torchao.py", line 226, in hqq_quants_to_torch_quants
    .to(torch.int32)
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 39.39 GiB of which 203.06 MiB is free. Including non-PyTorch memory, this process has 39.19 GiB memory in use. Of the allocated memory 38.61 GiB is allocated by PyTorch, and 102.73 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
srun: error: gpua072: task 0: Exited with exit code 1
```

### mobicham · 2024-06-05

I can reproduce the error on an A6000, let me try to find a solution

### mobicham · 2024-06-05

Fixed: https://github.com/mobiusml/hqq/commit/9d4c9d08d22cbf9d44f187ddddf5825a20d0b618 
However, I just noticed that Mixtral doesn't support static cache, I guess I need to refactor the generator to support the new external cache logic: https://github.com/huggingface/transformers/issues/31157

For Mixtral, it's better to not quantize the gate layer, you can use the custom class `hqq.models.mixtral.MixtralHQQ`

Also, I am not sure why sometimes Mixtral produces [0, 4096] tensors with the torchao backend, trying to see what's going on.


### mobicham · 2024-06-05

I am not sure exactly why this happens randomly:
```Python
forward model.layers.0.block_sparse_moe.experts.4.w1 torch.Size([0, 4096]) cuda:0
model.layers.0.block_sparse_moe.experts.4.w1
in torch.Size([0, 4096]) cuda:0
```

Seems to be a bug in transformers' implementation of the ```MixtralSparseMoeBlock```
