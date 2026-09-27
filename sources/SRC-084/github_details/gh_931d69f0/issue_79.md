# [Issue #79] AttributeError: 'LlamaForCausalLM' object has no attribute '_setup_cache'

source: https://github.com/dropbox/hqq/issues/79
state: closed | updated: 2024-06-01T01:20:28Z
labels: bug

## 正文

Excellent work! 

I use hqq to qunatizer the Llama-2-13b model, but when I use the quant model to inference, I meet the following error:
```
Traceback (most recent call last):
  File "/mnt/afs/19110/lich/quantization/hqq/examples/llama2_benchmark/quant_llama2_hqq_demo.py", line 73, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/miniconda3/envs/lich/lib/python3.11/site-packages/hqq/utils/generation_hf.py", line 52, in __init__
    self.setup_cache()
  File "/usr/local/lib/miniconda3/envs/lich/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/miniconda3/envs/lich/lib/python3.11/site-packages/hqq/utils/generation_hf.py", line 68, in setup_cache
    self.model._setup_cache(StaticCache, 1, max_cache_len=self.cache_size)
    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/miniconda3/envs/lich/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1709, in __getattr__
    raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
AttributeError: 'LlamaForCausalLM' object has no attribute '_setup_cache'
```
The quantization code:
```
import torch, os
os.environ["TOKENIZERS_PARALLELISM"] = "1"
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True
hf_auth    = None #HuggingFace token
cache_path = ''   #cache directory to store data

#Chose a model
model_id = "/mnt/afs/data/model/open_source_data/LLaMA/Llama-2-13b-hf"

print(f"model = {model_id}")
#Load model on the CPU
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
model     = HQQModelForCausalLM.from_pretrained(model_id, use_auth_token=hf_auth, cache_dir=cache_path)
tokenizer = AutoTokenizer.from_pretrained(model_id,       use_auth_token=hf_auth, cache_dir=cache_path)

#Quantize the model
from hqq.core.quantize import *
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)

device = 'cuda:0'
compute_dtype = torch.bfloat16  # int4 kernel only works with bfloat16
model.quantize_model(quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Evaluate the quantized model
#from eval_model import eval_wikitext2
#eval_wikitext2(model, tokenizer, verbose=True)

# Set default backends, to compare with int4mm
if (quant_config['weight_quant_params']['axis'] == 0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)

# Replace HQQLinear layers matmuls to support int4 mm
from hqq.utils.patching import prepare_for_inference

prepare_for_inference(model, backend="torchao_int4")

# Import custom HF generator
from hqq.utils.generation_hf import HFGenerator

# Generate
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial")

out = gen.generate("Write an essay about large language models.", print_tokens=True)
out = gen.generate("Tell me a funny joke!", print_tokens=True)
out = gen.generate("How to make a yummy chocolate cake?", print_tokens=True)
```
Do you have any idea about it？ 

Thanks！


## 评论 (3)

### mobicham · 2024-05-31

Thank you! Yeah I noticed that just this week. The newer version of transformers removed the `_setup_cache()` call, and it's necessary to do it manually to properly compile the model. 
You can use the previous version of transformers until we figure out how to fix this. I will reach out the HF team.

### mobicham · 2024-05-31

Reported here: https://github.com/huggingface/transformers/issues/31157

### ChuanhongLi · 2024-05-31

> Thank you! Yeah I noticed that just this week. The newer version of transformers removed the `_setup_cache()` call, and it's necessary to do it manually to properly compile the model. You can use the previous version of transformers until we figure out how to fix this. I will reach out the HF team.

Thanks for your quick reply! 
