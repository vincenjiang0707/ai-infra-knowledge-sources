# [Issue #36] TypeError: HQQWrapper.from_quantized() got an unexpected keyword argument 'adapter'

source: https://github.com/dropbox/hqq/issues/36
state: closed | updated: 2024-05-06T16:30:57Z
labels: help wanted

## 正文

hi there!

youre results seems very promising, unfortunatly i was unable to get the code to work

lambdalabs H10 instance

### installed by:
pip install git+https://github.com/mobiusml/hqq.git

### trying to run:
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer

#Load the model
model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_2bitgs8_hqq' 
model     = HQQModelForCausalLM.from_quantized(model_id, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)

```
#Setup Inference Mode
tokenizer.add_bos_token = False
tokenizer.add_eos_token = False
if not tokenizer.pad_token: tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.config.use_cache  = True
model.eval();
```


### the exception
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_3024/2511671864.py in <module>
      3 #Load the model
      4 model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_2bitgs8_hqq'
----> 5 model     = HQQModelForCausalLM.from_quantized(model_id, adapter='adapter_v0.1.lora')
      6 tokenizer = AutoTokenizer.from_pretrained(model_id)
      7 

TypeError: HQQWrapper.from_quantized() got an unexpected keyword argument 'adapter'

## 评论 (1)

### mobicham · 2024-04-02

Hi, thanks! Seems like you are not using the latest version from master. Can you re-install it: ```pip uninstall hqq.``` then re-install ```pip install git+https://github.com/mobiusml/hqq.git```
