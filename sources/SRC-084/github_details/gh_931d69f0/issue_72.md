# [Issue #72] Compatibility Issue: TypeError for Union Type Hints with Python Versions Below 3.10

source: https://github.com/dropbox/hqq/issues/72
state: closed | updated: 2024-05-09T08:29:33Z
labels: 

## 正文

when I try to quantize model like this
```
  from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
  model     = HQQModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)
  tokenizer = AutoTokenizer.from_pretrained(model_id) 

  from hqq.core.quantize import BaseQuantizeConfig
  quant_config = BaseQuantizeConfig(nbits=4, group_size=64)
  model.quantize_model(quant_config=quant_config, compute_dtype=model.dtype, device=model.device)
```
I encountered the error "unsupported operand type(s) for |: 'type' and 'NoneType'" because of this line of code.

https://github.com/mobiusml/hqq/blob/b92ef48a89ecf2bedeae15d4e8621778e5d7f624/hqq/core/peft.py#L370

 It appears to be due to using a Python version older than 3.10. Would you consider making it compatible with earlier Python versions?

## 评论 (1)

### mobicham · 2024-05-09

Hi @hjh0119 , this should fix it https://github.com/mobiusml/hqq/commit/3254f0172d639838f2c28e1951f6749da873a56c 
Let me know if there's another issue!
