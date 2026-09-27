# [Issue #35] KeyError: 'self_attn.dense'

source: https://github.com/dropbox/hqq/issues/35
state: closed | updated: 2024-05-06T16:31:25Z
labels: help wanted

## 正文

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
[<ipython-input-2-e196b2f48cff>](https://localhost:8080/#) in <cell line: 31>()
     29 
     30 #Apply LoRA
---> 31 PeftUtils.add_lora(model, lora_params)
     32 
     33 #Dataset

1 frames
[/usr/local/lib/python3.10/dist-packages/hqq/models/hf/phi.py](https://localhost:8080/#) in patch_linearlayers(cls, model, patch_fct, patch_params, verbose)
     53             )
     54             layers[i].self_attn.dense = patch_fct(
---> 55                 layers[i].self_attn.dense, patch_params["self_attn.dense"]
     56             )
     57             layers[i].mlp.fc1 = patch_fct(layers[i].mlp.fc1, patch_params["mlp.fc1"])

KeyError: 'self_attn.dense'

Unable to add lora module for training

## 评论 (2)

### mobicham · 2024-04-02

Could you please add a code to reproduce this?

### mobicham · 2024-05-06

Closing since no follow-up code to reproduce the issue was provided.
