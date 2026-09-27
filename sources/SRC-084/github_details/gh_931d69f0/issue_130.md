# [Issue #130] 8bit + Aten + compile

source: https://github.com/dropbox/hqq/issues/130
state: closed | updated: 2025-04-09T11:01:16Z
labels: 

## 正文

When I try to run patch_model_for_compiled_runtime on 8bit + aten, the program reports an error. How can I solve this problem?
![image](https://github.com/user-attachments/assets/f0a85477-f36e-4081-bf45-833ca3fa5eec)

# code
import torch
import torch.fx
import time
device        = 'cuda:0'
backend       = 'torchao_int4' #"torchao_int4" (4-bit only) or "bitblas" (4-bit + 2-bit)
compute_dtype = torch.float16 if backend=="bitblas" else torch.bfloat16
cache_dir     = '.' 
model_id = './llama/llama3/Meta-Llama-3-8B'
########################################################################
#Load model
from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *


tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_dir, torch_dtype=compute_dtype, attn_implementation="sdpa")
#Quantize
quant_config = BaseQuantizeConfig(nbits=8, group_size=64, axis=0)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
HQQLinear.set_backend(HQQBackend.ATEN_FORWARD)

#Inference
from hqq.utils.generation_hf import patch_model_for_compiled_runtime

patch_model_for_compiled_runtime(model, tokenizer, warmup=True)

WARMUP_PROMPTS = [
    "Write an essay about large language models.",
    "Tell me a funny joke!",
    "Hello, my name is Kiven, I like England for five reasons. First,",
    "Who is Elon Musk?",
    "Write a Python code snippet that adds two numbers together.",
]
for prompt in WARMUP_PROMPTS:
    inputs_warmup = tokenizer(prompt,return_tensors='pt',padding='max_length',max_length=128,truncation=True).to(model.device)
    torch.cuda.synchronize()
    warmup_start = time.time()
    output = model.generate(**inputs_warmup,max_new_tokens=1000,cache_implementation="static", pad_token_id=tokenizer.pad_token_id)
    torch.cuda.synchronize()
    warmup_end = time.time()
    print(warmup_end-warmup_start)


## 评论 (7)

### mobicham · 2024-11-01

You need to patch the model for inference before. Because by default, the model is raady for QLoRa training which is not compatible with torch.compile

```Python
...
HQQLinear.set_backend(HQQBackend.ATEN)
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model)

#Inference
from hqq.utils.generation_hf import patch_model_for_compiled_runtime
patch_model_for_compiled_runtime(model, tokenizer, warmup=True)
...
```


### mobicham · 2024-11-01

If you are using the compiled runtime, you can also use the `HQQLinear.set_backend(HQQBackend.PYTORCH)` which will work with both `axis=0` and `axis=1`, ATEN only works with `axis=0` 

### zhangy659 · 2024-11-01

Thank you very much. I noticed that the patch_hqq_inference() in prepare_for_inference replaces the forward function with forward_hqq_inferece. This forward_hqq_inferece() is different from the forward_aten of HQQLinear itself. In this case, won't backend=aten not work?

### mobicham · 2024-11-01

Oh yes, it's a bit confusing, in short no. 
ATEN, PYTORCH and PYTORCH_COMPILE are native backends for the hqq lib. 
The ones in `prepare_for_inference` are external CUDA / Triton kernels to speed-up inference, the HQQLinear layers are swapped with a whole new layer that uses those external backends. So when you patch_for_inference with a backend like `torchao_int4` or `bitblas` it will no longer use HQQBackend, it will use the CUDA / Triton kernels from those backends

### zhangy659 · 2024-11-01

Thank you very much. However, I don’t think this is the main issue. After PyTorch 2.4, the binding implementation for C++/CUDA operators has changed (https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html). When testing, I found that the methods in hqq/kernels are not compatible with torch.compile() and report the following issue:
![image](https://github.com/user-attachments/assets/33645e6b-223e-4c05-ac99-7734cf3980b2)
I'm not sure if this bug is due to an issue with the binding logic or a problem with my environment.

### mobicham · 2024-11-01

Oh could be actually, thanks for checking! Just use the `PYTORCH` backend, then `prepare_for_inference`, it should work. 
I haven't used ATEN with axis=0 since months : D !

### werruww · 2024-12-13



from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
import torch
import transformers  # Make sure transformers is imported
from threading import Thread  # Make sure Thread is imported

# Load the model
model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq'
model = HQQModelForCausalLM.from_quantized(model_id, adapter='adapter_v0.1.lora', compute_dtype=torch.float16, device="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Define the device before using it
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Move the model to the selected device
model.to(device)

# Setup Inference Mode
tokenizer.add_bos_token = False
tokenizer.add_eos_token = False
if not tokenizer.pad_token:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.config.use_cache = True
model.eval()

# Optional: torch compile for faster inference
# model = torch.compile(model)  # You might want to enable this for potential speedup

def chat_processor(chat, max_new_tokens=100, do_sample=True, device='cuda'):
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

    # Get the input tensor
    inputs = tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to(device)

    # Access the shape attribute of the input tensor
    batch_size = inputs["input_ids"].shape[0]

    generate_params = dict(
        inputs=inputs,  # Pass the input tensor directly
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        pad_token_id=tokenizer.pad_token_id,
        top_p=0.90 if do_sample else None,
        top_k=50 if do_sample else None,
        temperature=0.6 if do_sample else None,
        num_beams=1,
        repetition_penalty=1.2,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()

    print("User: ", chat)
    print("Assistant: ")
    outputs = ""
    for text in streamer:
        outputs += text
        print(text, end="", flush=True)

    torch.cuda.empty_cache()

    return outputs

# Now you can call the function:
results = chat_processor("What is the solution to x^2 - 1 = 0", max_new_tokens=100, device=device)
print(results)




/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(
Fetching 9 files: 100%
 9/9 [00:00<00:00, 169.05it/s]
/usr/local/lib/python3.10/dist-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|██████████| 32/32 [00:00<00:00, 764.78it/s]
100%|██████████| 32/32 [00:01<00:00, 20.53it/s]
/usr/local/lib/python3.10/dist-packages/hqq/core/peft.py:513: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  lora_data = torch.load(filename, map_location="cpu")
100%|██████████| 32/32 [00:00<00:00, 32.98it/s]
100%|██████████| 32/32 [00:00<00:00, 182.07it/s]
100%|██████████| 32/32 [00:00<00:00, 1747.24it/s]
Exception in thread Thread-12 (generate):
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/transformers/tokenization_utils_base.py", line 283, in __getattr__
    return self.data[item]
KeyError: 'shape'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 1990, in generate
    batch_size = inputs_tensor.shape[0]
  File "/usr/local/lib/python3.10/dist-packages/transformers/tokenization_utils_base.py", line 285, in __getattr__
    raise AttributeError
AttributeError
User:  What is the solution to x^2 - 1 = 0
Assistant: 




