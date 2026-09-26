# [Issue #975] ImportError: /home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

source: https://github.com/Dao-AILab/flash-attention/issues/975
state: open | updated: 2026-06-30T18:21:30Z
labels: 

## 正文

I'm trying to use `text-generation-webui`  to load an AWQ model but I encountered this error:
```shell
Traceback (most recent call last):
  File "/home/linjl/text-generation-webui/modules/ui_model_menu.py", line 249, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(selected_model, loader)
  File "/home/linjl/text-generation-webui/modules/models.py", line 94, in load_model
    output = load_func_map[loader](model_name)
  File "/home/linjl/text-generation-webui/modules/models.py", line 293, in AutoAWQ_loader
    from awq import AutoAWQForCausalLM
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/__init__.py", line 2, in <module>
    from awq.models.auto import AutoAWQForCausalLM
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/__init__.py", line 1, in <module>
    from .mpt import MptAWQForCausalLM
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/mpt.py", line 1, in <module>
    from .base import BaseAWQForCausalLM
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/base.py", line 46, in <module>
    from awq.quantize.quantizer import AwqQuantizer
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/quantize/quantizer.py", line 10, in <module>
    from awq.quantize.scale import apply_scale, apply_clip
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/quantize/scale.py", line 8, in <module>
    from transformers.models.llama.modeling_llama import LlamaRMSNorm
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 55, in <module>
    from flash_attn import flash_attn_func, flash_attn_varlen_func
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn/__init__.py", line 3, in <module>
    from flash_attn.flash_attn_interface import (
  File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn/flash_attn_interface.py", line 10, in <module>
    import flash_attn_2_cuda as flash_attn_cuda
ImportError: /home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
```
env:
```shell
python 3.10.13
torch 2.2.2+cu121
flash-attn-2.5.9.post1
```

## 评论 (22)

### cryptal-mc · 2024-06-05

I have the same issue. Not resolved yet.

### rkuo2000 · 2024-06-05

flash-attn==2.5.8 works
(mine is python 3.10.14, torch 2.3.0, ubuntu 22.04.4 LTS)

### AlexYoung757 · 2024-06-06

i have same the issue.
python 3.8.10
torch 2.1.2+cu121
flash-attn-2.5.8

### rkuo2000 · 2024-06-06

> i have same the issue. python 3.8.10 torch 2.1.2+cu121 flash-attn-2.5.8

you will need to roll back flash-attn version, I remembered flash-attn was working with torch 2.1.2+cu121

### AlexYoung757 · 2024-06-06

> > i have same the issue. python 3.8.10 torch 2.1.2+cu121 flash-attn-2.5.8
> 
> you will need to roll back flash-attn version, I remembered flash-attn was working with torch 2.1.2+cu121

i try 2.5.4, 2.5.6, 2.5.7  still not works

### rkuo2000 · 2024-06-06

> > > i have same the issue. python 3.8.10 torch 2.1.2+cu121 flash-attn-2.5.8
> > 
> > 
> > you will need to roll back flash-attn version, I remembered flash-attn was working with torch 2.1.2+cu121
> 
> i try 2.5.4, 2.5.6, 2.5.7 still not works

it was few weeks back, I dont remember the verison, keep rolling back till it works.
or go for torch 2.3.0

### AlexYoung757 · 2024-06-06

> > > > i have same the issue. python 3.8.10 torch 2.1.2+cu121 flash-attn-2.5.8
> > > 
> > > 
> > > you will need to roll back flash-attn version, I remembered flash-attn was working with torch 2.1.2+cu121
> > 
> > 
> > i try 2.5.4, 2.5.6, 2.5.7 still not works
> 
> it was few weeks back, I dont remember the verison, keep rolling back till it works. or go for torch 2.3.0

python 3.10  torch ==2.30 still not works

### rkuo2000 · 2024-06-06

pip uninstall flash-attn 
pip install flash-attn --no-build-isolation


### Queuecumber · 2024-06-06

It looks like this is because the pytorch wheel on pypi uses cuda 12.1 but flash attention is compiled with cuda 12.2.  I don't even know where you would get a cuda 12.2 wheel for pytorch to work with this, but the only option would be to compile from source I think.

### AlexYoung757 · 2024-06-07

> It looks like this is because the pytorch wheel on pypi uses cuda 12.1 but flash attention is compiled with cuda 12.2. I don't even know where you would get a cuda 12.2 wheel for pytorch to work with this, but the only option would be to compile from source I think.

there is not have  a  cuda 12.2 wheel for pytorch

### AlexYoung757 · 2024-06-07

> pip uninstall flash-attn pip install flash-attn --no-build-isolation

i try whl to install , still can't 

### AlexYoung757 · 2024-06-07

> I'm trying to use `text-generation-webui` to load an AWQ model but I encountered this error:
> 
> ```shell
> Traceback (most recent call last):
>   File "/home/linjl/text-generation-webui/modules/ui_model_menu.py", line 249, in load_model_wrapper
>     shared.model, shared.tokenizer = load_model(selected_model, loader)
>   File "/home/linjl/text-generation-webui/modules/models.py", line 94, in load_model
>     output = load_func_map[loader](model_name)
>   File "/home/linjl/text-generation-webui/modules/models.py", line 293, in AutoAWQ_loader
>     from awq import AutoAWQForCausalLM
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/__init__.py", line 2, in <module>
>     from awq.models.auto import AutoAWQForCausalLM
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/__init__.py", line 1, in <module>
>     from .mpt import MptAWQForCausalLM
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/mpt.py", line 1, in <module>
>     from .base import BaseAWQForCausalLM
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/models/base.py", line 46, in <module>
>     from awq.quantize.quantizer import AwqQuantizer
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/quantize/quantizer.py", line 10, in <module>
>     from awq.quantize.scale import apply_scale, apply_clip
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/awq/quantize/scale.py", line 8, in <module>
>     from transformers.models.llama.modeling_llama import LlamaRMSNorm
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 55, in <module>
>     from flash_attn import flash_attn_func, flash_attn_varlen_func
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn/__init__.py", line 3, in <module>
>     from flash_attn.flash_attn_interface import (
>   File "/home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn/flash_attn_interface.py", line 10, in <module>
>     import flash_attn_2_cuda as flash_attn_cuda
> ImportError: /home/linjl/anaconda3/envs/sd/lib/python3.10/site-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
> ```
> 
> env:
> 
> ```shell
> python 3.10.13
> torch 2.2.2+cu121
> flash-attn-2.5.9.post1
> ```

i try flash_attn-2.5.8+cu122torch2.3cxx11abiFALSE-cp310-cp310-linux_x86_64.whl. it works
i guess  only  "abiFALSE" can use


### ghost · 2024-06-07

I have the same issue when i am using vllm.
Just uninstall flash-attn, it works.

pip3 list | grep flash
flash-attn                        2.5.9.post1
pip3 uninstall flash-attn

### zzc0208 · 2024-06-13

> I have the same issue when i am using vllm.
> Just uninstall flash-attn, it works.
> 
> pip3 list | grep flash
> flash-attn                        2.5.9.post1
> pip3 uninstall flash-attn

😂😂😂I still hope to solve this problem. Flash-attn can accelerate inference. Of course, xformers can also be used in vllm to accelerate

### aulaywang · 2024-06-24

+1. `flash-attn=2.5.8` is unable to install.
My version:
```
CUDA 12.1
torch 2.3.0
python 3.10.14
```

### cxg2333 · 2024-07-16

+1 
My version:
```
CUDA 11.7
torch 2.0.1
python 3.9.18
```
help!

### Bellocccc · 2024-07-26

Thanks. Python 3.9.19，cuda12.2，torch2.3.0 flash_attn==2.5.8, it works.

### GallonDeng · 2024-08-30

python3.9 cuda12.1 torch2.2, build the flash-attn from source, it did not work, same error

### montagetao · 2025-02-23

> I have the same issue when i am using vllm. Just uninstall flash-attn, it works.
> 
> pip3 list | grep flash flash-attn 2.5.9.post1 pip3 uninstall flash-attn

its works for me, but i have to remove the flash attn from the python files

### jinwater88 · 2025-06-25

torch=2.4.0+cu118，flash_attn-2.6.2+cu118torch2.4cxx11abiTRUE-cp312-cp312-linux_x86_64.whl+python3.12
I have this problem too, have you solved it?

### billysx · 2025-08-07

https://github.com/huggingface/open-r1/issues/684
just using `flash_attn==2.7.4.post1` released earlier this year.

### SturgeonYang · 2026-06-30

I use flash_attn-2.6.0+cu122torch2.4cxx11abiFALSE-cp310-cp310-linux_x86_64.whl in Ubuntu 22.04. It works.
Python 3.10.14; torch2.4
