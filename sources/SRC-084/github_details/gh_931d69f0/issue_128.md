# [Issue #128] 4bit slower?

source: https://github.com/dropbox/hqq/issues/128
state: closed | updated: 2024-11-01T18:45:16Z
labels: 

## 正文

I used the hqq quantization opt model on the A100-40GB and used eval_model.py to test the model performance before and after quantization. The results I obtained are as follows. Why is the inference speed slower after 4bit quantization than bfloat16?

## result: 

 root@0d2c83196670:/workspace# python test_example.py
/usr/local/lib/python3.8/dist-packages/scipy/__init__.py:138: UserWarning: A NumPy version >=1.16.5 and <1.23.0 is required for this version of SciPy (detected version 1.24.4)
  warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion} is required for this version of "
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 73/73 [00:00<00:00, 233372.10it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 562/562 [00:03<00:00, 145.87it/s]
perplexity 26.25
time 0.007  sec
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 562/562 [00:02<00:00, 216.09it/s]
perplexity 26.25
time 0.005  sec



## code: 
import torch
device        = 'cuda:0'
backend       = 'torchao_int4' #"torchao_int4" (4-bit only) or "bitblas" (4-bit + 2-bit)
compute_dtype = torch.bfloat16
cache_dir     = '.' 
model_id      = './opt'


from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig 

quant_config = HqqConfig(nbits=4, group_size=64, axis=1)

model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=compute_dtype, 
    cache_dir=cache_dir,
    device_map=device, 
    low_cpu_mem_usage=True,
    quantization_config=quant_config
)

tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend=backend, verbose=True) 

from eval_model import eval_wikitext2

eval_wikitext2(model,tokenizer,verbose=True)

origin_model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype = compute_dtype,
    cache_dir=cache_dir,
    device_map = device,
    low_cpu_mem_usage=True,
)
eval_wikitext2(origin_model,tokenizer,verbose=True)


## 评论 (3)

### mobicham · 2024-10-30

Two things:
* You are measuring the prefill time: the prefill time will be slower with `torchao_int4` and `bitblas` backends because they are GEMV kernels not GEMM. It's the *decoding* time that will be much faster not the prefill because in quantization we are interested in memory bound scenarios. If you want to still get fast prefill, you need the `gemlite` backend (which is experimental).
* On top of that, to benefit from faster decoding, you need torch.compile

You can test with this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py

### zhangy659 · 2024-10-30

Wow, thank you, thank you, but how do I start torch.compile()? @mobicham 

### mobicham · 2024-10-30

Just follow the example here: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py
It will quantize and prepare the model for inference with torch.compile, you should see ~4x speed-up in decoding
