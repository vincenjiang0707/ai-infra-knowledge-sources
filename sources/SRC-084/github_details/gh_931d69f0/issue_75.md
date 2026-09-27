# [Issue #75] Not able to save quantized model

source: https://github.com/dropbox/hqq/issues/75
state: closed | updated: 2024-05-29T04:58:02Z
labels: 

## 正文

Hi! I am trying to quantize Llama-2-7b-hf model, here is some part of the code:
the quantization is done by
```python
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
```
and save the model
```python
AutoHQQHFModel.save_quantized(model, dir_s)
```
But the output says: Model was already quantized
and the saved model has no decrease in size.
Which part is wrong?

## 评论 (5)

### mobicham · 2024-05-26

Hi, it works fine, just make sure you have the latest version (from master):

```Python
import torch

model_id  = "meta-llama/Llama-2-7b-hf" 

compute_dtype = torch.bfloat16
device     = 'cuda'
cache_path = ""

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path) 

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

AutoHQQHFModel.save_quantized(model, "llama_quant")

model_quant = AutoHQQHFModel.from_quantized("llama_quant")

with torch.no_grad():
	model_quant(torch.randint(0, 100, (1, 1024), device=device, dtype=torch.int64))
```

### BeichenHuang · 2024-05-28

Thank you for helping! I upgrade the package and it works now.

### mobicham · 2024-05-28

I just checked the commits history and it turns out the fix was not in the latest release. So I created a new one: https://github.com/mobiusml/hqq/releases/tag/v0.1.7.post3
Also updated the `pip` version, so it should work with `pip install hqq`

### mobicham · 2024-05-28

I just tried saving and loading from the example and it's working fine: https://github.com/mobiusml/hqq/issues/75#issuecomment-2132253550

I think you are still not using the latest version. you are missing this commit https://github.com/mobiusml/hqq/commit/3495a81e034e3cde72b7036e74c19c73a9746aa0
`pip uninstall hqq`
`pip install git+https://github.com/mobiusml/hqq.git` or `pip install hqq==0.1.7.post3`

### BeichenHuang · 2024-05-29

You are right. Now the latest version works. Thank you for helping!
