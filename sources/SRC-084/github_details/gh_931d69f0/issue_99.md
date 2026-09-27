# [Issue #99] RuntimeError: Expected in.dtype() == at::kInt to be true, but got false.  (Could this error message be improved?  If so, please report an enhancement request to PyTorch.)

source: https://github.com/dropbox/hqq/issues/99
state: closed | updated: 2024-07-30T07:17:04Z
labels: 

## 正文

I want to use hqq optimization and torch.compile using llama3.1 models. What code should I run to make it run fastest?

examples/backends/torchao_int4_demo.py

```python

# pip install git+https://github.com/mobiusml/hqq.git;
# num_threads=12; OMP_NUM_THREADS=$num_threads CUDA_VISIBLE_DEVICES=0 ipython3 

# Tested on 4090: up to 154 tokens/sec with default compile_args
##########################################################################################################################################################
import torch, os

os.environ["TOKENIZERS_PARALLELISM"]  = "1"
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32       = True

cache_path     = '.'
model_id       = "/mnt/adllm/models/Meta-Llama-3.1-8B-Instruct"
compute_dtype  = torch.bfloat16 #int4 kernel only works with bfloat16
device         = 'cuda:1'

##########################################################################################################################################################
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
from hqq.core.quantize import *

#Load
tokenizer    = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_path)
model        = HQQModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype, attn_implementation="sdpa")

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
model.quantize_model(quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Set default backends, to compare with int4mm
if(quant_config['weight_quant_params']['axis']==0):
    HQQLinear.set_backend(HQQBackend.ATEN)
else:
    HQQLinear.set_backend(HQQBackend.PYTORCH)

##########################################################################################################################################################

#Replace HQQLinear layers matmuls to support int4 mm
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend="torchao_int4")

#Import custom HF generator
from hqq.utils.generation_hf import HFGenerator

#Generate
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() 

out = gen.generate("Write an essay about large language models.", print_tokens=True)
```


Error Message:
```bash
  .../python3.10/site-packages/hqq/backends/torchao.py", line 193, in process_hqq_quants
    self.weight_int4pack = torch.ops.aten._convert_weight_to_int4pack(
  .../python3.10/site-packages/torch/_ops.py", line 854, in __call__
    return self_._op(*args, **(kwargs or {}))
RuntimeError: Expected in.dtype() == at::kInt to be true, but got false.  (Could this error message be improved?  If so, please report an enhancement request to PyTorch.)
```

## 评论 (1)

### mobicham · 2024-07-30

Yeah I already pushed a fixed yesterday: https://github.com/mobiusml/hqq/commit/d09b4e6f93e9c387b0caee86c5df869baaa8fb12 
Just use the master branch, or use the bitblas backend instead (with `torch.float16` instead of `torch.bfloat16`, don't forget to install it first `pip install bitblas`)
