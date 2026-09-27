# [Issue #114] Issue when loading the quantized model

source: https://github.com/dropbox/hqq/issues/114
state: closed | updated: 2024-09-03T12:08:38Z
labels: 

## 正文

Hi, I tried the same ways to quantize and load the HQQ quantized model, but right now I am quantizing the Qwen/Qwen2-VL-2B-Instruct   https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct 
![image](https://github.com/user-attachments/assets/cf634d03-6448-4563-bd09-56a26148c143)
When I load the quantized model, it shows the error below.

> (hqq) user@AMARIS-i9-4090:/mnt/c/users/i9-4090/documents/tianyi$ python storm_testing.py
> Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
> /home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
>   return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
>   0%|                                                                                           | 0/114 [00:00<?, ?it/s]
> Traceback (most recent call last):
>   File "/mnt/c/users/i9-4090/documents/tianyi/storm_testing.py", line 16, in <module>
>     model = AutoHQQHFModel.from_quantized("output/Qwen2-VL-2B-Instruct", compute_dtype=torch.bfloat16, device='cuda')
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py", line 517, in from_quantized
>     cls.patch_model(
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py", line 215, in patch_model
>     cls.patch_nonlinearlayers(model, patch_nonlinear_fct, verbose=verbose)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py", line 125, in patch_nonlinearlayers
>     patch_fct(tmp_mapping[name]),
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
>     return func(*args, **kwargs)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py", line 490, in _load_module
>     return module.to(device=device, dtype=compute_dtype, non_blocking=True)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1340, in to
>     return self._apply(convert)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 927, in _apply
>     param_applied = fn(param)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1333, in convert
>     raise NotImplementedError(
> NotImplementedError: Cannot copy out of meta tensor; no data! Please use torch.nn.Module.to_empty() instead of torch.nn.Module.to() when moving module from meta to a different device.

And if i run directly without saving the quantized model? it will show this error

> Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████| 2/2 [00:01<00:00,  1.47it/s]
> 100%|█████████████████████████████████████████████████████████████████████████████████| 214/214 [00:06<00:00, 31.13it/s]
> 100%|█████████████████████████████████████████████████████████████████████████████████| 327/327 [00:30<00:00, 10.56it/s]
> Traceback (most recent call last):
>   File "/mnt/c/users/i9-4090/documents/tianyi/quantize.py", line 31, in <module>
>     gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 100, in warmup
>     self.generate(prompt, print_tokens=False);
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
>     return func(*args, **kwargs)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 253, in generate
>     return self.next_token_iterator(self.prefill(), self.max_new_tokens, verbose, print_tokens)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 183, in prefill
>     out = self.model(
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
>     return forward_call(*args, **kwargs)
> TypeError: forward() got an unexpected keyword argument 'cache_position'


this is the code i using
```
import torch

model_id = "Qwen/Qwen2-VL-2B-Instruct"
compute_dtype = torch.bfloat16
device = "cuda"
cache_path = "."

from transformers import AutoModelForCausalLM, AutoTokenizer,Qwen2VLForConditionalGeneration
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

model = Qwen2VLForConditionalGeneration.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path)

quant_config = BaseQuantizeConfig(nbits=4, group_size=None, quant_scale=False, quant_zero=False, axis=1)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

# #Use optimized inference kernels
# ###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
# #prepare_for_inference(model) #default backend
prepare_for_inference(model,backend="torchao_int4")
# #prepare_for_inference(model, backend="bitblas") #takes a while to init...

# #Generate
# ###################################################
# #For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
```

## 评论 (5)

### mobicham · 2024-09-03

`Qwen2 VL` is new and not fully supported, the main call `from_config` seems to be broken, it's not creating the whole model. 

Solution 1:
For this specific model since it is very small and it takes just 5 seconds to quantize, you can just quantize on the fly. Also, you don't need to quantize the vision model, only the LLMs since the faster backend is for memory-bound problems (quantized vision will run slower  actually)

Solution 2:
Try the official support in transformers via this pull request: https://github.com/huggingface/transformers/pull/33141

Solution 3:
I made a custom loader for Qwen2 VL (from master branch not pip):
https://github.com/mobiusml/hqq/commit/84499909c0c36021d79bf678be42e39edfd5c7ab
As I mentioned before, since the base model `from_config` call is broken, you need to pass it the original model id. However, with this loader it's not gonna load it to cpu first. 

Solution 1 imo is enough. 


### mobicham · 2024-09-03

Reported here: https://github.com/huggingface/transformers/issues/33273

### NEWbie0709 · 2024-09-03

Actually i tried the solution one ady using this code
```
import torch

model_id = "Qwen/Qwen2-VL-2B-Instruct"
compute_dtype = torch.bfloat16
device = "cuda"
cache_path = "."

from transformers import AutoModelForCausalLM, AutoTokenizer,Qwen2VLForConditionalGeneration
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

model = Qwen2VLForConditionalGeneration.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path)

quant_config = BaseQuantizeConfig(nbits=4, group_size=None, quant_scale=False, quant_zero=False, axis=1)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

# #Use optimized inference kernels
# ###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
# #prepare_for_inference(model) #default backend
prepare_for_inference(model,backend="torchao_int4")
# #prepare_for_inference(model, backend="bitblas") #takes a while to init...

# #Generate
# ###################################################
# #For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
```

and i get the error from the `gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() ` part

> Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████| 2/2 [00:01<00:00, 1.47it/s]
> 100%|█████████████████████████████████████████████████████████████████████████████████| 214/214 [00:06<00:00, 31.13it/s]
> 100%|█████████████████████████████████████████████████████████████████████████████████| 327/327 [00:30<00:00, 10.56it/s]
> Traceback (most recent call last):
> File "/mnt/c/users/i9-4090/documents/tianyi/quantize.py", line 31, in
> gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 100, in warmup
> self.generate(prompt, print_tokens=False);
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
> return func(*args, **kwargs)
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 253, in generate
> return self.next_token_iterator(self.prefill(), self.max_new_tokens, verbose, print_tokens)
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 183, in prefill
> out = self.model(
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
> return self._call_impl(*args, **kwargs)
> File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
> return forward_call(*args, **kwargs)
> TypeError: forward() got an unexpected keyword argument 'cache_position'

### mobicham · 2024-09-03

You should not use `HFGenerator`, that's for LLMs only, Qwen2 VL is a Vision-Language model. And it seems like Qwen2 VL doesn't support static cache if it says that the `cache_position` is missing.

You could still compile the forward pass of the model:
`model.forward = torch.compile(model.forward, mode="reduce-overhead", fullgraph=True)` and see if it speeds-up performance <b>after</b> a warm-up phase of a couple of predictions. 

### NEWbie0709 · 2024-09-03

ok thanks for your explanation will try this tomorrow 😸 
