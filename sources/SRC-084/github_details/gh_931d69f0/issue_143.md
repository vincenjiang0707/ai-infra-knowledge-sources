# [Issue #143] How to quantize a model and use vllm to do the inference

source: https://github.com/dropbox/hqq/issues/143
state: closed | updated: 2025-02-05T08:46:47Z
labels: 

## 正文

Hi, I want to use hqq to quantize a model and then use vllm to do the inference. I run "from hqq.models.hf.base import AutoHQQHFModel
#Save: Make sure to save the model BEFORE any patching
AutoHQQHFModel.save_quantized(model, save_dir)", and I only get "config.json" and "  qmodel.pt; ", and it seems that I cannot directly pass it to vllm's "llm" function to do the inference. Can you show some solutions?


## 评论 (2)

### mobicham · 2025-01-21

You need to use transformers to quantize the model not the hqq lib:

```Python
# pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/b63ba848323efd88207b12d7582501d525503b8a/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl;
# pip install hqq;
####################################################################################
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig

model_path = "meta-llama/Meta-Llama-3-8B-Instruct"
quant_model = "quant_model"

quant_config = HqqConfig(nbits=4, group_size=64, axis=1)

model = AutoModelForCausalLM.from_pretrained(model_path,
                                            torch_dtype=torch.float16,
                                            cache_dir='.',
                                            device_map="cuda:0",
                                            quantization_config=quant_config,
                                            low_cpu_mem_usage=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model.save_pretrained(quant_model)
tokenizer.save_pretrained(quant_model)
#Close this 

####################################################################################
from vllm import LLM
from vllm import SamplingParams
import random

llm = LLM(model="quant_model", max_model_len=4096)
```

### ZeleiShao · 2025-02-05

Thank you..
