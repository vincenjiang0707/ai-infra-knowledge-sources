# [Issue #70] Problem in load from saved model

source: https://github.com/dropbox/hqq/issues/70
state: closed | updated: 2024-05-07T14:10:01Z
labels: 

## 正文

```python
import torch
from hqq.core.quantize import *
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel


save_dir   = 'mistral-7B-v0.1'
compute_dtype = torch.float16
model_id="mistralai/Mistral-7B-v0.1"
device="cuda"

#Load the model on CPU
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)

#Quantize
from hqq.models.hf.base import AutoHQQHFModel
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
```
this part works fine

```python
from hqq.models.hf.base import AutoHQQHFModel

#Save: Make sure to save the model BEFORE any patching
AutoHQQHFModel.save_quantized(model, save_dir)

#Load
model = AutoHQQHFModel.from_quantized(save_dir)
```
when i try this part of the code
I get the following error
```python
    456 
    457         # Load model from config
--> 458         model = cls.create_model(save_dir)
    459 
    460         # Track save directory

TypeError: BaseHQQHFModel.create_model() missing 1 required positional argument: 'kwargs'
```
thank you in advance for your support

## 评论 (2)

### mobicham · 2024-05-07

Thanks for reporting the issue, it should be fixed in master https://github.com/mobiusml/hqq/commit/3495a81e034e3cde72b7036e74c19c73a9746aa0

### uisikdag · 2024-05-07

Thank you so much 
