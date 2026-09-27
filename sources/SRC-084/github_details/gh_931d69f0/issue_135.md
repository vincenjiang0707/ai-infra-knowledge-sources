# [Issue #135] not run

source: https://github.com/dropbox/hqq/issues/135
state: closed | updated: 2025-02-11T15:03:51Z
labels: 

## 正文

colabb t4




from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer

#Load the model
model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq' 
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

# Optional: torch compile for faster inference
model = torch.compile(model)

#Streaming Inference
import torch, transformers
from threading import Thread

def chat_processor(chat, max_new_tokens=100, do_sample=True, device='cuda'):
```bash
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer,skip_prompt=True, skip_special_tokens=True)

    generate_params = dict(
        tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to(device),
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        pad_token_id=tokenizer.pad_token_id,
        top_p=0.90 if do_sample else None,
        top_k=50 if do_sample else None,
        temperature= 0.6 if do_sample else None,
        num_beams=1,
        repetition_penalty=1.2,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()
    
    print("User: ", chat); 
    print("Assistant: ");
    outputs = ""
    for text in streamer:
        outputs += text
        print(text, end="", flush=True)

    torch.cuda.empty_cache()
  
    return outputs
```


outputs = chat_processor("What is the solution to x^2 - 1 = 0", max_new_tokens=1000).to(cuda)







8]
1
outputs = chat_processor("What is the solution to x^2 - 1 = 0", max_new_tokens=1000).to(cuda)
Exception in thread Thread-17 (generate):
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2215, in generate
    result = self._sample(
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 3206, in _sample
    outputs = self(**model_inputs, return_dict=True)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 1190, in forward
    outputs = self.model(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 921, in forward
    position_embeddings = self.rotary_emb(hidden_states, position_ids)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 158, in forward
    freqs = (inv_freq_expanded.float() @ position_ids_expanded.float()).transpose(1, 2)
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)






## 评论 (33)

### werruww · 2024-12-13



```python
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
import torch
import transformers  # Make sure transformers is imported
from threading import Thread  # Make sure Thread is imported
```

# Load the model
```bash
model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq'
model = HQQModelForCausalLM.from_quantized(model_id, adapter='adapter_v0.1.lora', compute_dtype=torch.float16, device="cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

# Define the device before using it
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Move the model to the selected device
model.to(device)

# Setup Inference Mode
```
tokenizer.add_bos_token = False
tokenizer.add_eos_token = False
if not tokenizer.pad_token:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.config.use_cache = True
model.eval()
```

# Optional: torch compile for faster inference
# model = torch.compile(model)  # You might want to enable this for potential speedup

def chat_processor(chat, max_new_tokens=100, do_sample=True, device='cuda'):
```bash
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
```

# Now you can call the function:
```bash
results = chat_processor("What is the solution to x^2 - 1 = 0", max_new_tokens=100, device=device)
print(results)
```



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
```yaml
User:  What is the solution to x^2 - 1 = 0
Assistant: 
```

### werruww · 2024-12-13

colab t4

### werruww · 2024-12-13

```python
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
from transformers import AutoModelForCausalLM
import torch
```

# Device configuration
```bash
device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch_dtype = torch.float16
```

# Load the quantized model
quantized_model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq'
one_bit_model = HQQModelForCausalLM.from_quantized(
    quantized_model_id, 
    adapter='adapter_v0.1.lora'
)
```bash
one_bit_model = one_bit_model.to(device)
one_bit_model.config.use_cache = True
one_bit_model.eval()
```

# Load tokenizer
```python
tokenizer = AutoTokenizer.from_pretrained(quantized_model_id)
tokenizer.add_bos_token = False
tokenizer.add_eos_token = False
if not tokenizer.pad_token:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
```
tokenizer.padding_side = 'left'

def debug_tensor_devices(inputs):
```json
    """Helper function to print device information for all tensors"""
    for key, value in inputs.items():
        if torch.is_tensor(value):
            print(f"Tensor {key} is on device: {value.device}")
```

def chat_processor(chat, current_model, current_tokenizer, max_new_tokens=100, do_sample=True, device=device):
    print(f"\nStarting chat_processor with device: {device}")
    current_tokenizer.use_default_system_prompt = False
    
    # Create inputs
    input_text = "<s> [INST] " + chat + " [/INST] "
    
    # Tokenize and explicitly move to device
    inputs = current_tokenizer(
        input_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=2048
    )
    
    # Move each tensor to the correct device
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    print("\nInput tensor devices:")
    debug_tensor_devices(inputs)
    print(f"Model device: {next(current_model.parameters()).device}")
    
    # Create streamer
    streamer = transformers.TextIteratorStreamer(
        current_tokenizer,
        timeout=10.0,
        skip_prompt=True,
        skip_special_tokens=True
    )

    # Prepare generation parameters
    generate_params = {
        'input_ids': inputs['input_ids'],
        'attention_mask': inputs['attention_mask'] if 'attention_mask' in inputs else None,
        'streamer': streamer,
        'max_new_tokens': max_new_tokens,
        'do_sample': do_sample,
        'pad_token_id': current_tokenizer.pad_token_id,
        'top_p': 0.90 if do_sample else None,
        'top_k': 50 if do_sample else None,
        'temperature': 0.6 if do_sample else None,
        'num_beams': 1,
        'repetition_penalty': 1.2,
    }
    
    # Remove None values from generate_params
    generate_params = {k: v for k, v in generate_params.items() if v is not None}
    
    print("\nGeneration parameters devices:")
    debug_tensor_devices(generate_params)

    # Start generation in a separate thread
    from threading import Thread
    t = Thread(target=current_model.generate, kwargs=generate_params)
    t.start()

    print("\nUser: ", chat)
    print("Assistant: ")
    outputs = ""
    for text in streamer:
        outputs += text
        print(text, end="", flush=True)

    # Clean up
    torch.cuda.empty_cache()
    return outputs

# Test with explicit error handling
question = "What is 2 + 2?"
try:
    with torch.no_grad():
        outputs = chat_processor(
            question,
            one_bit_model,
            tokenizer,
            max_new_tokens=256,
            do_sample=False
        )
except Exception as e:
    print(f"\nError during processing: {str(e)}")
    import traceback
    print("\nFull traceback:")
    print(traceback.format_exc())



Fetching 9 files: 100%
 9/9 [00:00<00:00, 325.83it/s]
100%|██████████| 32/32 [00:00<00:00, 3756.34it/s]
100%|██████████| 32/32 [00:01<00:00, 29.25it/s]
100%|██████████| 32/32 [00:00<00:00, 39.99it/s]
100%|██████████| 32/32 [00:00<00:00, 465.35it/s]
100%|██████████| 32/32 [00:00<00:00, 3185.12it/s]
Exception in thread Thread-16 (generate):
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2215, in generate
    result = self._sample(
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 3206, in _sample
    outputs = self(**model_inputs, return_dict=True)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 1190, in forward
    outputs = self.model(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 921, in forward
    position_embeddings = self.rotary_emb(hidden_states, position_ids)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 158, in forward
    freqs = (inv_freq_expanded.float() @ position_ids_expanded.float()).transpose(1, 2)
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

Starting chat_processor with device: cuda

Input tensor devices:
Tensor input_ids is on device: cuda:0
Tensor attention_mask is on device: cuda:0
Model device: cuda:0

Generation parameters devices:
Tensor input_ids is on device: cuda:0
Tensor attention_mask is on device: cuda:0

User:  What is 2 + 2?
Assistant: 

Error during processing: 

Full traceback:
Traceback (most recent call last):
  File "<ipython-input-16-7fa7e613b1dd>", line 105, in <cell line: 103>
    outputs = chat_processor(
  File "<ipython-input-16-7fa7e613b1dd>", line 93, in chat_processor
    for text in streamer:
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/streamers.py", line 223, in __next__
    value = self.text_queue.get(timeout=self.timeout)
  File "/usr/lib/python3.10/queue.py", line 179, in get
    raise Empty
_queue.Empty


### werruww · 2024-12-13

What is the solution?

### werruww · 2024-12-13

All ideas for 1bit, 2bit

never work





### mobicham · 2024-12-13

Hi, sorry I don't understand, what is the problem exactly?
I just tired it with the specified versions and it works fine: https://huggingface.co/mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq#usage


### werruww · 2025-02-04

What are the versions and where is the code used and is there Colab T4?

### werruww · 2025-02-04

https://github.com/werruww/hqq-/blob/main/%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92%D9%92XXXXXXXXXXXXX.ipynb

### werruww · 2025-02-04

it run in colab t4 very goooooooood
thank you


https://github.com/werruww/hqq-/blob/main/run_hqq.ipynb

### werruww · 2025-02-04

it no run


https://github.com/werruww/hqq-/blob/main/hqq.ipynb

### werruww · 2025-02-04

mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq

not run never
whyyyyyyyyyyyyyy?

### mobicham · 2025-02-04

Hi, can you please explain what is the problem? 
Did you follow the doc and tried using `pip install hqq==0.1.8` ?

### Qarqor5555555 · 2025-02-04

I uploaded the Colab pages, the models work for Lama 2 and the model for the kvv The problem is in the Lama 3 model, and I don’t know where the problem is.

### Qarqor5555555 · 2025-02-04

Is there a Python code to run hqq models without problems with its libraries and versions as I did with the Llama 2 model it worked because of the specific library versions and the code is complete 

### Qarqor5555555 · 2025-02-04

> مرحبًا، هل يمكنك توضيح المشكلة؟ هل اتبعت التعليمات وحاولت استخدام `pip install hqq==0.1.8`؟

https://github.com/werruww/hqq-/blob/main/hqq.ipynb

### Qarqor5555555 · 2025-02-04


Fetching 9 files:   0%|          | 0/9 [00:00<?, ?it/s]
  0%|          | 0/32 [00:00<?, ?it/s]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-2-cdfe9eb0cb94> in <cell line: 0>()
      8 ###################################################
      9 model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq'
---> 10 model     = HQQModelForCausalLM.from_quantized(model_id, cache_dir='.')
     11 tokenizer = AutoTokenizer.from_pretrained(model_id)
     12 

/usr/local/lib/python3.11/dist-packages/hqq/engine/base.py in from_quantized(cls, save_dir_or_hub, compute_dtype, device, cache_dir, adapter)
     85         cls._check_arch_support(arch_key)
     86 
---> 87         model = cls._get_hqq_class(arch_key).from_quantized(
     88             save_dir,
     89             compute_dtype=compute_dtype,

/usr/local/lib/python3.11/dist-packages/hqq/models/base.py in from_quantized(cls, save_dir_or_hub, compute_dtype, device, cache_dir, adapter, **kwargs)
    515 
    516         # Load modules
--> 517         cls.patch_model(
    518             model, _load_module, _load_module, {k: None for k in model.linear_tags}
    519         )

/usr/local/lib/python3.11/dist-packages/hqq/models/base.py in patch_model(cls, model, patch_nonlinear_fct, patch_linear_fct, patch_params, verbose)
    213         cls.freeze_model(model)
    214         cls.autoname_modules(model)
--> 215         cls.patch_nonlinearlayers(model, patch_nonlinear_fct, verbose=verbose)
    216         cls.patch_linearlayers(model, patch_linear_fct, patch_params, verbose=verbose)
    217         cleanup()

/usr/local/lib/python3.11/dist-packages/hqq/models/hf/llama.py in patch_nonlinearlayers(cls, model, patch_fct, verbose)
     30         layers = base_model.layers
     31         for i in tqdm(range(len(base_model.layers)), disable=not verbose):
---> 32             layers[i].self_attn.rotary_emb = patch_fct(layers[i].self_attn.rotary_emb)
     33             layers[i].mlp.act_fn = patch_fct(layers[i].mlp.act_fn)
     34             layers[i].input_layernorm = patch_fct(layers[i].input_layernorm)

/usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in __getattr__(self, name)
   1929             if name in modules:
   1930                 return modules[name]
-> 1931         raise AttributeError(
   1932             f"'{type(self).__name__}' object has no attribute '{name}'"
   1933         )

AttributeError: 'LlamaAttention' object has no attribute 'rotary_emb'

!pip list
     
DEPRECATION: Loading egg at /usr/local/lib/python3.11/dist-packages/hqq_aten-0.0.0-py3.11-linux-x86_64.egg is deprecated. pip 24.3 will enforce this behaviour change. A possible replacement is to use pip for package installation. Discussion can be found at https://github.com/pypa/pip/issues/12330
Package                            Version
---------------------------------- -------------------
absl-py                            1.4.0
accelerate                         1.2.1
aiohappyeyeballs                   2.4.4
aiohttp                            3.11.11
aiohttp-cors                       

### mobicham · 2025-02-04

Try this
```Python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq' 
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir='.', compute_dtype=torch.float16, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

### mobicham · 2025-02-04

I have updated the doc for all the models. Basically, the old models need the following versions in order to work:
```
pip install hqq==0.1.8
pip install transformers==4.46.0
```
The newer models would use `AutoHQQHFModel` instead of ``HQQModelForCausalLM` and should work with the latest transformers version. `hqq==0.1.8` is required for the old quantized models since we no longer support meta-data offloading and lower group-sizes than 32.

### Qarqor5555555 · 2025-02-04

Thank you, I will try and let you know the results. 

### werruww · 2025-02-04

It worked, thank you.

But the problem is in the back-end. I have uploaded a Colab T4 page for you.

If it is possible, I will complete the code that you sent.

I am working in Colab T4, which does not support flash attention.


https://github.com/werruww/hqq-/blob/main/hQQ%20(1).ipynb

### werruww · 2025-02-04

```python
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend, verbose=True)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)



NameError                                 Traceback (most recent call last)
[<ipython-input-9-665b4604ab72>](https://localhost:8080/#) in <cell line: 0>()
      1 from hqq.utils.patching import prepare_for_inference
----> 2 prepare_for_inference(model, backend, verbose=True)
      3 
      4 HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

NameError: name 'backend' is not defined

### werruww · 2025-02-04

```python
from hqq.utils.patching import prepare_for_inference
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchao
prepare_for_inference(model, backend="torchao_int4", verbose=True)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)



100%|██████████| 225/225 [00:00<00:00, 8980.70it/s]
Skipping aoint4 conversion for  model.layers.0.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.0.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.1.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.2.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.3.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.4.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.5.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.6.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.7.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.8.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.9.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.10.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.11.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.12.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.13.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.14.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.15.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.16.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.17.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.18.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.19.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.20.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.21.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.22.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.23.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.24.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.25.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.26.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.27.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.28.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.29.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.30.mlp.down_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.self_attn.q_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.self_attn.k_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.self_attn.v_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.self_attn.o_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.mlp.gate_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.mlp.up_proj.linear_layer
Skipping aoint4 conversion for  model.layers.31.mlp.down_proj.linear_layer
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
[<ipython-input-10-e012298ac440>](https://localhost:8080/#) in <cell line: 0>()
      4 import torch.nn.functional as F
      5 import torchao
----> 6 prepare_for_inference(model, backend="torchao_int4", verbose=True)
      7 
      8 HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

3 frames
[/usr/local/lib/python3.11/dist-packages/hqq/utils/patching.py](https://localhost:8080/#) in patch_add_weight_param(layer, patch_param)
     38 
     39         fp_param = [p for p in layer.parameters() if p.is_floating_point()]
---> 40         dtype_ = fp_param[0].dtype if (len(fp_param) > 0) else patch_param["dtype"]
     41 
     42         layer.weight = torch.nn.Parameter(

TypeError: 'NoneType' object is not subscriptable

### werruww · 2025-02-04

https://github.com/werruww/hqq-/blob/main/succ_hqq.ipynb



```python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq'
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir='.', compute_dtype=torch.float16, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)

from hqq.utils.patching import prepare_for_inference
#prepare_for_inference(model)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

gen = HFGenerator(model, tokenizer, max_new_tokens=5, do_sample=True, compile="partial").warmup() #Faster generation, but warm-up takes a while

gen.generate("What is the result of the following addition operation 34+67?", print_tokens=True)


### werruww · 2025-02-04

```python
from hqq.utils.patching import prepare_for_inference
#prepare_for_inference(model)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

I made this part like this so it doesn't cause problems. What do you think?

### werruww · 2025-02-04

16m 57s

colab t4

### werruww · 2025-02-04

```python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq' 
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir='.', compute_dtype=torch.float16, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

patch_linearlayers(model, patch_add_quant_config, 
                          BaseQuantizeConfig(nbits=2, group_size=64, quant_scale=False, quant_zero=False, axis=1))

model.eval();
cleanup()

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
prepare_for_inference(model, backend="bitblas", allow_merge=False) #It takes a while...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter 
#gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile=None) #Slower generation but no warm-up 
gen = HFGenerator(model, tokenizer, max_new_tokens=5, do_sample=True, compile="partial").warmup() #Faster generation, but warm-up takes a while

gen.generate("Write an essay about large language models", print_tokens=True)



Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
/usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(
Fetching 9 files: 100%
 9/9 [00:00<00:00, 232.70it/s]
/usr/local/lib/python3.11/dist-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|██████████| 99/99 [00:00<00:00, 3039.15it/s]
100%|██████████| 225/225 [00:00<00:00, 3164.12it/s]
/usr/local/lib/python3.11/dist-packages/hqq/core/peft.py:513: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  lora_data = torch.load(filename, map_location="cpu")
100%|██████████| 225/225 [00:00<00:00, 433.33it/s]
100%|██████████| 225/225 [00:00<00:00, 167563.64it/s]
100%|██████████| 225/225 [00:00<00:00, 182290.59it/s]
2025-02-04 23:08:07 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-04 23:09:37 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-04 23:10:04 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-04 23:10:45 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
[<ipython-input-1-43f7ff76db48>](https://localhost:8080/#) in <cell line: 0>()
     22 HQQLinear.set_backend(HQQBackend.PYTORCH)
     23 #prepare_for_inference(model) #default backend
---> 24 prepare_for_inference(model, backend="bitblas", allow_merge=False) #It takes a while...
     25 
     26 #Generate

3 frames
[/usr/local/lib/python3.11/dist-packages/hqq/utils/patching.py](https://localhost:8080/#) in patch_add_weight_param(layer, patch_param)
     46 
     47         fp_param = [p for p in layer.parameters() if p.is_floating_point()]
---> 48         dtype_ = fp_param[0].dtype if (len(fp_param) > 0) else patch_param["dtype"]
     49 
     50         layer.weight = torch.nn.Parameter(

TypeError: 'NoneType' object is not subscriptable

### werruww · 2025-02-05

```python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq'
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir='.', compute_dtype=torch.float16, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)

from hqq.utils.patching import prepare_for_inference
#prepare_for_inference(model, backend="torchao_int4", verbose=True)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

```python
#Warmup
for i in range(10):
    with torch.no_grad():
        out = model(torch.ones((1, 1), dtype=torch.int32, device='cuda'))
```
del out
cleanup()

```python
import transformers
from threading import Thread
```

def chat_processor(chat, max_new_tokens=100, do_sample=True):
```bash
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    generate_params = dict(
        tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to('cuda'),
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        top_p=0.80,
        top_k=40,
        temperature= 0.2,
        num_beams=1,
        repetition_penalty=1.3,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()

    print('------------------------------------------------------------')
    cleanup()
    print(chat); print();
    outputs = []
    for text in streamer:
        outputs.append(text)
        print(text, end="", flush=True)

    return outputs
```

################################################################################################
#Generation
outputs = chat_processor("How do I build a car?", max_new_tokens=100, do_sample=True)





Setting `pad_token_id` to `eos_token_id`:128009 for open-end generation.
------------------------------------------------------------
How do I build a car?

 ( us in and his home. ( we is moved by, your very being you self B ( F E h L main that too with all one H B S F to $ B O ( F I b2FOUSOSLEHB/ Teachers " Clark L I W L its L Millions P L L L HD n and the rain.
 ($I and this Re LA (0 p I L L L + V I my of fun H K I love H I L Rain


The output is very bad.

### werruww · 2025-02-05

```python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq'
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir='.', compute_dtype=torch.float16, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)
from hqq.utils.patching import prepare_for_inference
#prepare_for_inference(model, backend="torchao_int4", verbose=True)
```

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

```python
#Warmup
for i in range(10):
    with torch.no_grad():
        out = model(torch.ones((1, 1), dtype=torch.int32, device='cuda'))
del out
cleanup()
import transformers
from threading import Thread
```

def chat_processor(chat, max_new_tokens=100, do_sample=True):
```bash
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    generate_params = dict(
        tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to('cuda'),
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        top_p=0.80,
        top_k=40,
        temperature= 0.2,
        num_beams=1,
        repetition_penalty=1.3,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()

    print('------------------------------------------------------------')
    cleanup()
    print(chat); print();
    outputs = []
    for text in streamer:
        outputs.append(text)
        print(text, end="", flush=True)

    return outputs
```

################################################################################################
#Generation
outputs = chat_processor("How do I build a car?", max_new_tokens=100, do_sample=True)





It works but its answers are very bad

### mobicham · 2025-02-05

Thanks for reporting, I can indeed reproduce the issue and just made a fix. 
Can you please try again by upgrading the package 
`pip install git+https://github.com/mobiusml/hqq`

and use the new code here: https://huggingface.co/mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq

### werruww · 2025-02-05

```python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
from hqq.utils.patching import *
from hqq.utils.generation_hf import HFGenerator

#Settings
###################################################
backend       = "bitblas" #bitblas or gemlite for 2-bit runtime
compute_dtype = torch.bfloat16 if backend=="torchao_int4" else torch.float16
device        = 'cuda:0'
cache_dir     = '.'

#Load the model
###################################################
model_id = 'mobiuslabsgmbh/Llama-3-8b-instruct_2bitgs64_hqq' 
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype, device=device, adapter='adapter_v0.1.lora').eval();
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
```

#Use optimized inference kernels
###################################################
prepare_for_inference(model, backend=backend) #It takes a while...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter 
#gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile=None) #Slower generation but no warm-up 
gen = HFGenerator(model, tokenizer, max_new_tokens=10, do_sample=True, compile="partial").warmup() #Faster generation, but warm-up takes a while

```
gen.generate("Write an essay about large language models", print_tokens=True)
#gen.generate("Tell me a funny joke!", print_tokens=True)
#gen.generate("How to make a yummy chocolate cake?", print_tokens=True)
```





/usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(
Fetching 9 files: 100%
 9/9 [01:42<00:00, 22.38s/it]
.gitattributes: 100%
 1.70k/1.70k [00:00<00:00, 75.2kB/s]
llama3-2bit.gif: 100%
 25.8M/25.8M [00:00<00:00, 41.1MB/s]
adapter_v0.1.lora: 100%
 83.0M/83.0M [00:02<00:00, 41.8MB/s]
README.md: 100%
 4.17k/4.17k [00:00<00:00, 70.2kB/s]
special_tokens_map.json: 100%
 296/296 [00:00<00:00, 3.47kB/s]
tokenizer.json: 100%
 9.09M/9.09M [00:00<00:00, 26.8MB/s]
config.json: 100%
 728/728 [00:00<00:00, 7.74kB/s]
qmodel.pt: 100%
 4.28G/4.28G [01:41<00:00, 41.9MB/s]
tokenizer_config.json: 100%
 51.0k/51.0k [00:00<00:00, 1.63MB/s]
100%|██████████| 131/131 [00:00<00:00, 1362.95it/s]
100%|██████████| 225/225 [00:00<00:00, 5040.58it/s]
100%|██████████| 225/225 [00:00<00:00, 284.09it/s]
100%|██████████| 225/225 [00:00<00:00, 101040.51it/s]
2025-02-05 19:32:39 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-05 19:34:13 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-05 19:34:40 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
2025-02-05 19:35:23 [BitBLAS:WARNING]: TVM target not found. Please set the TVM target environment variable using `export TVM_TARGET=<target>`, where <target> is one of the available targets can be found in the output of `tools/get_available_targets.py`.
The 'batch_size' argument of StaticCache is deprecated and will be removed in v4.49. Use the more precisely named 'max_batch_size' argument instead.
The 'batch_size' attribute of StaticCache is deprecated and will be removed in v4.49. Use the more precisely named 'self.max_batch_size' attribute instead.
100%|██████████| 9/9 [03:19<00:00, 22.14s/it]
100%|██████████| 9/9 [00:01<00:00,  5.07it/s]
100%|██████████| 9/9 [00:00<00:00, 30.45it/s]
100%|██████████| 9/9 [00:00<00:00, 34.61it/s]
100%|██████████| 9/9 [00:00<00:00, 33.36it/s]
The rapid advancements in the field of artificial intelligence have
{'output_text': 'The rapid advancements in the field of artificial intelligence',
 'output_tokens': tensor([  791, 11295, 83787,   304,   279,  2115,   315, 21075, 11478],
        dtype=torch.int32),
 'input_tokens': tensor([128000, 128000, 128006,    882, 128007,    271,   8144,    459,   9071,
            922,   3544,   4221,   4211, 128009, 128006,  78191, 128007,    271],
        dtype=torch.int32)}

### werruww · 2025-02-05

it run very gooooooooooooooooooooooooood

thank you mobicham

### werruww · 2025-02-05

https://github.com/werruww/hqq-/blob/main/suc_hqq_good.ipynb

### werruww · 2025-02-05

https://github.com/werruww/hqq-/blob/main/suc_hqq_good%20(2).ipynb
with 100 token
