# [Issue #144] quantization with transformers of RWKV/v6-Finch-1B6-HF

source: https://github.com/dropbox/hqq/issues/144
state: closed | updated: 2025-08-18T08:59:17Z
labels: 

## 正文

I made a quantization with transformers of RWKV/v6-Finch-1B6-HF, but I got this error when load:


```
Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\hqq2b_RWKV_load.py", line 28, in <module>
    model = AutoModelForCausalLM.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\venv\Lib\site-packages\transformers\models\auto\auto_factory.py", line 559, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\venv\Lib\site-packages\transformers\modeling_utils.py", line 4255, in from_pretrained
    ) = cls._load_pretrained_model(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\venv\Lib\site-packages\transformers\modeling_utils.py", line 4828, in _load_pretrained_model
    new_error_msgs, offload_index, state_dict_index = _load_state_dict_into_meta_model(
                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\venv\Lib\site-packages\transformers\modeling_utils.py", line 873, in _load_state_dict_into_meta_model
    set_module_tensor_to_device(model, param_name, param_device, **set_module_kwargs)
  File "C:\Users\Admin\Desktop\Python\0.LLMs\hqq\venv\Lib\site-packages\accelerate\utils\modeling.py", line 286, in set_module_tensor_to_device
    raise ValueError(
ValueError: Trying to set a tensor of shape torch.Size([1, 1, 2048]) in "time_decay" (which has shape torch.Size([32, 64])), this looks incorrect.
```


Quantization:


```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig

model_id      = "RWKV/v6-Finch-1B6-HF"
repo          = "v6-Finch-1B6-HF"
nbits         = 4
group_size    = 64
axis          = 1
save_path     = repo+"-HQQ"
cache_dir     = repo+"-cache"
device        = "cpu" # "cpu"    cuda:0
compute_dtype = torch.float16

#Quantize
quant_config  = HqqConfig(nbits=nbits, group_size=group_size, axis=axis)

#Load the model
print("model: "+str(model_id))
print("Quantize to: "+str(save_path))
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=compute_dtype, 
    cache_dir=cache_dir,
    device_map=device, 
    quantization_config=quant_config,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

#Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir, trust_remote_code=True)

# Save
print("saving...")
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
```


Load:



```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_prompt(instruction, input=""):
    instruction = instruction.strip().replace('\r\n','\n').replace('\n\n','\n')
    input = input.strip().replace('\r\n','\n').replace('\n\n','\n')
    if input:
        return f"""Instruction: {instruction}

Input: {input}

Response:"""
    else:
        return f"""User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: {instruction}

Assistant:"""


model = AutoModelForCausalLM.from_pretrained("RWKV/v6-Finch-1B6-HF", trust_remote_code=True, torch_dtype=torch.float16).to(0)
tokenizer = AutoTokenizer.from_pretrained("RWKV/v6-Finch-1B6-HF", trust_remote_code=True)

text = "Write an essay about large language models."
prompt = generate_prompt(text)

inputs = tokenizer(prompt, return_tensors="pt").to(0)
attention_mask = inputs["attention_mask"]
output = model.generate(inputs["input_ids"], attention_mask=attention_mask, max_new_tokens=128, do_sample=True, temperature=1.0, top_p=0.3, top_k=0, )
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```









## 评论 (4)

### mobicham · 2025-01-27

It seems this is more of a transformers issue: it's not an official transformers model (`trust_remote=True`), so it's difficult to make sure everything would work fine. 

The model is actually very small and it takes a few seconds to quantize and load. Any reasons why you want to save the quantized version instead of just quantizing on-the-fly?

### blap · 2025-01-27

> It seems this is more of a transformers issue: it's not an official transformers model (`trust_remote=True`), so it's difficult to make sure everything would work fine.
> 
> The model is actually very small and it takes a few seconds to quantize and load. Any reasons why you want to save the quantized version instead of just quantizing on-the-fly?

I would like to upload just to spread hqq.
But it is a test too for big models.

### mobicham · 2025-01-28

Cool! Yeah unfortunately since RWKV doesn't have official support in transformers, there are no guarantees it's gonna work. 
There's probably a workaround with hqq lib but it's not gonna be safetensors

### mobicham · 2025-04-09

Hey, have you found a solution to this?
