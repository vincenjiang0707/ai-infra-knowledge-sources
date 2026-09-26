# [Issue #44] 使用NPU推理Transfomers模型，AiCore占用为0

source: https://github.com/Ascend/pytorch/issues/44
state: open | updated: 2024-08-13T03:46:22Z
labels: 

## 正文

一、问题现象：
```python
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
import numpy as np
import torch 
import torch_npu

device = "npu:4" # the device to load the model onto


model_dir = "models/qwen/Qwen1___5-7B-Chat"
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map=device,
    torch_dtype=torch.float16,
    #bf16 = True,
    trust_remote_code=True,x``
).eval()
tokenizer = AutoTokenizer.from_pretrained(model_dir,trust_remote_code=True)
#@torch.inference_mode()
def infer(model, tokenizer, prompt):
    #prompt = "帮助我制定一份去上海的旅游攻略。"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    start = time.time()
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512,
        do_sample = False,
        use_cache = True,
    )
    end = time.time()
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    print(f"{len(generated_ids)/(end-start)}tokens/s")
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response
```
通过上面代码调用模型推理时ai core占用为0，推理速度慢

二、软件版本:
-- CANN 版本: 8.0RC1  
--Pytorch版本:2.1.0
--torch-npu版本：2.1.0.post3
--Python 版本:3.9.14
--Transformers: 4.38.2

## 评论 (1)

### yunyiyun · 2024-08-13

https://gitee.com/ascend/pytorch/issues/IAGSVZ?from=project-issue
