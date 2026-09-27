# [Issue #158] dtype issue with ATEN backend

source: https://github.com/dropbox/hqq/issues/158
state: closed | updated: 2025-05-02T07:48:46Z
labels: 

## 正文

Hello,

first of all thanks to the authors for open-sourcing and maintaining this awesome quantization tool!

When using it with the ATEN backend, I noticed that during dequantization the resulting tensor is not cast to the compute dtype. As such, I encountered some dtype mismatches during inference.

Specifically, the issue seems to lie here: https://github.com/mobiusml/hqq/blob/master/hqq/core/quantize.py#L958

Changing this line from 
`return W_est`  
to  
`return W_est.to(meta["compute_dtype"])`  

seems to fix the issue.

## 评论 (16)

### mobicham · 2025-04-30

Hi, thank you! Do you have an small example to reproduce this ?

Kind of strange because this should not happen, it gets the dtype from the scales https://github.com/mobiusml/hqq/blob/master/hqq/kernels/hqq_aten_cuda_kernel.cu#L131-L132
So for some reason ```scale.dtype != meta['compute_dtype']``` which should not happen

On a separate note, the aten backend is kinda deprecated - it only supports `axis=0` mainly useful for QLORA training but we exclusively use `axis=1` since the fast inference kernels only support `axis=1`

### DominikHil · 2025-04-30

Thanks for the quick response! Below you'll find a code example that fails:  

Setup (Im using conda):
```
conda create -n hqq_dt_repro python=3.11
conda activate hqq_dt_repro
conda install -y conda-forge::uv
conda install -y cuda -c nvidia/label/cuda-12.4.1
uv pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
conda install -y conda-forge::transformers==4.49.0
uv pip install hqq
git clone https://github.com/mobiusml/hqq
cd hqq/hqq/kernels
mv hqq_aten_torch.cpp hqq_aten.cpp
python3 setup_torch.py install
```

code snippet (i called it `hqq_reproduce.py`)
```
import torch
import transformers

import hqq
from hqq.models.hf import base

hqq.core.quantize.HQQLinear.set_backend(hqq.core.quantize.HQQBackend.ATEN)

model = transformers.AutoModel.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", torch_dtype="bfloat16").to("cuda:0")
q_config = hqq.core.quantize.BaseQuantizeConfig(nbits=4, group_size=64, quant_zero=False, quant_scale=False, axis=0)
hqq_model = base.AutoHQQHFModel.quantize_model(model, quant_config=q_config, compute_dtype=torch.bfloat16, device=getattr(model, "hf_device_map", "cuda"))

tokenizer = transformers.AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

tokens = tokenizer("Hi! How are you?", return_tensors="pt")
enc = hqq_model(**{k:v.to("cuda:0") for k,v in tokens.items()})

```
Running:  
`CUDA_VISIBLE_DEVICES=0 python hqq_reproduce.py`

fails with (truncated log):
```
[...]
  File "[...]/python3.11/site-packages/hqq/core/quantize.py", line 281, in forward
    out = torch.matmul(x, dequantize().t())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: expected mat1 and mat2 to have the same dtype, but got: c10::BFloat16 != float

```


### mobicham · 2025-04-30

May I ask why do you run `mv hqq_aten_torch.cpp hqq_aten.cpp`? 

I pushed some fixes, can you try again please:
```pip uninstall hqq hqq_aten; pip install git+https://github.com/mobiusml/hqq/;```

This works for me:

```Python
import torch
device        = 'cuda:0'
compute_dtype = torch.float16
model_id      = 'meta-llama/Meta-Llama-3-8B-Instruct'

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *

#Load
tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype, attn_implementation="sdpa")

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=0)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Training/fallback backend
#HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE) #axis=0,1
HQQLinear.set_backend(HQQBackend.ATEN) #only axis=0

#Optimize for inference: ONLY FOR axis=1
#from hqq.utils.patching import prepare_for_inference
#prepare_for_inference(model, backend='gemlite', verbose=True)


prompt  = "Write an essay about large language models."
inputs  = tokenizer.apply_chat_template([{"role":"user", "content":prompt}], tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True)
outputs = model.generate(**inputs.to(model.device), max_new_tokens=32, cache_implementation="dynamic", pad_token_id=tokenizer.pad_token_id) 
print(tokenizer.decode(outputs[0]))
```

I would recommend you use the default Pytorch backend with `axis=1`  though.

### DominikHil · 2025-04-30

> May I ask why do you run `mv hqq_aten_torch.cpp hqq_aten.cpp`?

When running `setup_torch.py` (https://github.com/mobiusml/hqq/blob/master/hqq/kernels/setup_torch.py) to install ATEN it fails with (only showing last 4 lines of log):
```
[...]
g++: error: hqq_aten.cpp: No such file or directory
g++: fatal error: no input files
compilation terminated.
error: command '/usr/bin/g++' failed with exit code 1
```
Looking into  `setup_torch.py` I saw it provides installation instructions as follow:  
`# python3 setup.py install`
 but `setup.py`does not exist so I assume this file was renamed without updating the instructions. Hence, it is likely that `hqq_aten.cpp` was renamed as well and indeed undoing the name change resulted in a working installation. 


### DominikHil · 2025-04-30

> May I ask why do you run `mv hqq_aten_torch.cpp hqq_aten.cpp`?
> 
> I pushed some fixes, can you try again please: `pip uninstall hqq hqq_aten; pip install git+https://github.com/mobiusml/hqq/;`
> 
> This works for me:
> 
> import torch
> device        = 'cuda:0'
> compute_dtype = torch.float16
> model_id      = 'meta-llama/Meta-Llama-3-8B-Instruct'
> 
> from transformers import AutoModelForCausalLM, AutoTokenizer
> from hqq.models.hf.base import AutoHQQHFModel
> from hqq.core.quantize import *
> 
> #Load
> tokenizer = AutoTokenizer.from_pretrained(model_id)
> model     = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype, attn_implementation="sdpa")
> 
> #Quantize
> quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=0)
> AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
> 
> #Training/fallback backend
> #HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE) #axis=0,1
> HQQLinear.set_backend(HQQBackend.ATEN) #only axis=0
> 
> #Optimize for inference: ONLY FOR axis=1
> #from hqq.utils.patching import prepare_for_inference
> #prepare_for_inference(model, backend='gemlite', verbose=True)
> 
> 
> prompt  = "Write an essay about large language models."
> inputs  = tokenizer.apply_chat_template([{"role":"user", "content":prompt}], tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True)
> outputs = model.generate(**inputs.to(model.device), max_new_tokens=32, cache_implementation="dynamic", pad_token_id=tokenizer.pad_token_id) 
> print(tokenizer.decode(outputs[0]))
> 

The above fails with: 
```
ValueError: Invalid `cache_implementation` (dynamic). Choose one of: ['static', 'offloaded_static', 'sliding_window', 'hybrid', 'mamba', 'quantized', 'static', 'offloaded']
```
However, changing cache implementation to `static` works although the output seems non-sensical (see below):
```
W0430 15:23:01.871000 150544 site-packages/torch/_inductor/utils.py:1137] [0/0] Not enough SMs to use max_autotune_gemm mode
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

Write an essay about large language models.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Largeléawaiaidplexitsuplexembers Geile Geile Geile Philippine Geile Schn Philippine Geile Philippine Geile Philippine Philippine Philippine Philippine Geile Philippine Geile Geile Philippine Philippine Schn Schn Philippine Philippine
```




### DominikHil · 2025-04-30

> I would recommend you use the default Pytorch backend with axis=1 though.

The documentation does not seem to recommend any backend in particular (although "torchao" is indicated to be the fastest). Could you please elaborate further?



### mobicham · 2025-04-30

You don't have to install it yourself, it should be installed automatically. `setup_torch.py` is actually not the right setup file, it's `setup_cuda.py` that should be automatically called when you install hqq.

What transformers and torch version are you using? I am using the following and it works:
```
In [230]: torch.__version__
Out[230]: '2.7.0+cu126'

In [233]: transformers.__version__
Out[233]: '4.51.3'
```

### DominikHil · 2025-04-30

> You don't have to install it yourself, it should be installed automatically. `setup_torch.py` is actually not the right setup file, it's `setup_cuda.py` that should be automatically called when you install hqq.
> 
> What transformers and torch version are you using? I am using the following and it works:
> 
> ```
> In [230]: torch.__version__
> Out[230]: '2.7.0+cu126'
> 
> In [233]: transformers.__version__
> Out[233]: '4.51.3'
> ```

Without manually installing I recieved the following warning:
`ATEN/CUDA backend not availabe. Make sure you install the hqq_aten library.`

The warning disappeared after manually runnning `setup_torch.py`

### mobicham · 2025-04-30

> The documentation does not seem to recommend any backend in particular (although "torchao" is indicated to be the fastest). Could you please elaborate further?

It's a bit confusing, but there are 2 separate things:
-`HQQBackend`: that's the fallback backend that is used, mainly for training. It's either pytorch or aten.
-Inference backends like torchao_int, gemlite are something for inference only. When the right settings are used, it will overwrite the pytorch/aten backends. It will only use the HQQBackend as a fallback if the inference kernels don't support such a config. 

If you mainly want to do inference, just follow the examples like this: https://github.com/mobiusml/hqq/blob/master/examples/hqq_lib_demo.py

### DominikHil · 2025-04-30

> You don't have to install it yourself, it should be installed automatically. `setup_torch.py` is actually not the right setup file, it's `setup_cuda.py` that should be automatically called when you install hqq.
> 
> What transformers and torch version are you using? I am using the following and it works:
> 
> ```
> In [230]: torch.__version__
> Out[230]: '2.7.0+cu126'
> 
> In [233]: transformers.__version__
> Out[233]: '4.51.3'
> ```

Updating transformers to 4.51.3 seems sufficient:

```
Warning: the ATEN/CUDA backend only supports axis=0 and GPU runtime.
Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

Write an essay about large language models.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Large language models (LLMs) have revolutionized the field of natural language processing (NLP) in recent years, enabling machines to process and generate human-like
```

Looking good :D

### mobicham · 2025-04-30

> > You don't have to install it yourself, it should be installed automatically. `setup_torch.py` is actually not the right setup file, it's `setup_cuda.py` that should be automatically called when you install hqq.
> > What transformers and torch version are you using? I am using the following and it works:
> > ```
> > In [230]: torch.__version__
> > Out[230]: '2.7.0+cu126'
> > 
> > In [233]: transformers.__version__
> > Out[233]: '4.51.3'
> > ```
> 
> Without manually installing I recieved the following warning: `ATEN/CUDA backend not availabe. Make sure you install the hqq_aten library.`
> 
> The warning disappeared after manually runnning `setup_torch.py`

But you should not install `setup_torch.py` you should install `setup_cuda.py`, `setup_torch.py` is not doing any cuda. 
Can you try that and share the logs if it breaks?

### DominikHil · 2025-04-30

> > The documentation does not seem to recommend any backend in particular (although "torchao" is indicated to be the fastest). Could you please elaborate further?
> 
> It's a bit confusing, but there are 2 separate things: -`HQQBackend`: that's the fallback backend that is used, mainly for training. It's either pytorch or aten. -Inference backends like torchao_int, gemlite are something for inference only. When the right settings are used, it will overwrite the pytorch/aten backends. It will only use the HQQBackend as a fallback if the inference kernels don't support such a config.
> 
> If you mainly want to do inference, just follow the examples like this: https://github.com/mobiusml/hqq/blob/master/examples/hqq_lib_demo.py

I see - thanks for clarifying!

### DominikHil · 2025-04-30

> > > You don't have to install it yourself, it should be installed automatically. `setup_torch.py` is actually not the right setup file, it's `setup_cuda.py` that should be automatically called when you install hqq.
> > > What transformers and torch version are you using? I am using the following and it works:
> > > ```
> > > In [230]: torch.__version__
> > > Out[230]: '2.7.0+cu126'
> > > 
> > > In [233]: transformers.__version__
> > > Out[233]: '4.51.3'
> > > ```
> > 
> > 
> > Without manually installing I recieved the following warning: `ATEN/CUDA backend not availabe. Make sure you install the hqq_aten library.`
> > The warning disappeared after manually runnning `setup_torch.py`
> 
> But you should not install `setup_torch.py` you should install `setup_cuda.py`, `setup_torch.py` is not doing any cuda. Can you try that and share the logs if it breaks?

This is what I got from when running `python setup_cuda.py install`:

```
hqq_aten_cuda_kernel.cu(58): error: no suitable conversion function from "const at::DeprecatedTypeProperties" to "c10::ScalarType" exists
   [&] { const auto& the_type = W_r.type(); constexpr const char* at_dispatch_name = "dequantize_8bit_u8"; at::ScalarType _st = ::detail::scalar_type(the_type); ; switch (_st) { case at::ScalarType::Double: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Double)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(58), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Double), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Double>; return ([&] { dequantize_8bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Float: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Float)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(58), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Float), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Float>; return ([&] { dequantize_8bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Half: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Half)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(58), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Half), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Half>; return ([&] { dequantize_8bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::BFloat16: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::BFloat16)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(58), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::BFloat16), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::BFloat16>; return ([&] { dequantize_8bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } default: if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(58), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", '"', at_dispatch_name, "\" not implemented for '", toString(_st), "'"))); }; } }()
                                                                                                                                                      ^

hqq_aten_cuda_kernel.cu(136): error: no suitable conversion function from "const at::DeprecatedTypeProperties" to "c10::ScalarType" exists
   [&] { const auto& the_type = W_r.type(); constexpr const char* at_dispatch_name = "dequantize_4bit_u8"; at::ScalarType _st = ::detail::scalar_type(the_type); ; switch (_st) { case at::ScalarType::Double: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Double)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(136), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Double), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Double>; return ([&] { dequantize_4bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Float: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Float)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(136), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Float), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Float>; return ([&] { dequantize_4bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Half: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Half)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(136), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Half), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Half>; return ([&] { dequantize_4bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::BFloat16: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::BFloat16)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(136), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::BFloat16), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::BFloat16>; return ([&] { dequantize_4bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } default: if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(136), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", '"', at_dispatch_name, "\" not implemented for '", toString(_st), "'"))); }; } }()
                                                                                                                                                      ^

hqq_aten_cuda_kernel.cu(221): error: no suitable conversion function from "const at::DeprecatedTypeProperties" to "c10::ScalarType" exists
   [&] { const auto& the_type = W_r.type(); constexpr const char* at_dispatch_name = "dequantize_2bit_u8"; at::ScalarType _st = ::detail::scalar_type(the_type); ; switch (_st) { case at::ScalarType::Double: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Double)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(221), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Double), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Double>; return ([&] { dequantize_2bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Float: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Float)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(221), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Float), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Float>; return ([&] { dequantize_2bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Half: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Half)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(221), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Half), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Half>; return ([&] { dequantize_2bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::BFloat16: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::BFloat16)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(221), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::BFloat16), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::BFloat16>; return ([&] { dequantize_2bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } default: if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(221), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", '"', at_dispatch_name, "\" not implemented for '", toString(_st), "'"))); }; } }()
                                                                                                                                                      ^

hqq_aten_cuda_kernel.cu(313): error: no suitable conversion function from "const at::DeprecatedTypeProperties" to "c10::ScalarType" exists
   [&] { const auto& the_type = W_r.type(); constexpr const char* at_dispatch_name = "dequantize_1bit_u8"; at::ScalarType _st = ::detail::scalar_type(the_type); ; switch (_st) { case at::ScalarType::Double: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Double)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(313), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Double), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Double>; return ([&] { dequantize_1bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Float: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Float)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(313), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Float), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Float>; return ([&] { dequantize_1bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Half: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Half)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(313), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Half), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Half>; return ([&] { dequantize_1bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::BFloat16: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::BFloat16)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(313), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::BFloat16), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::BFloat16>; return ([&] { dequantize_1bit_u8_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<unsigned char>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } default: if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(313), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", '"', at_dispatch_name, "\" not implemented for '", toString(_st), "'"))); }; } }()
                                                                                                                                                      ^

hqq_aten_cuda_kernel.cu(412): error: no suitable conversion function from "const at::DeprecatedTypeProperties" to "c10::ScalarType" exists
   [&] { const auto& the_type = W_r.type(); constexpr const char* at_dispatch_name = "dequantize_3bit_32"; at::ScalarType _st = ::detail::scalar_type(the_type); ; switch (_st) { case at::ScalarType::Double: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Double)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(412), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Double), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Double>; return ([&] { dequantize_3bit_32_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<int32_t>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Float: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Float)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(412), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Float), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Float>; return ([&] { dequantize_3bit_32_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<int32_t>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::Half: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::Half)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(412), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::Half), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::Half>; return ([&] { dequantize_3bit_32_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<int32_t>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } case at::ScalarType::BFloat16: { do { if constexpr (!at::should_include_kernel_dtype( at_dispatch_name, at::ScalarType::BFloat16)) { if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(412), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", "dtype '", toString(at::ScalarType::BFloat16), "' not selected for kernel tag ", at_dispatch_name))); }; } } while (0); using scalar_t [[maybe_unused]] = c10::impl::ScalarTypeToCPPTypeT<at::ScalarType::BFloat16>; return ([&] { dequantize_3bit_32_kernel<scalar_t><<<blocks, 256>>>(Wq_packed.data_ptr<int32_t>(), scale.data_ptr<scalar_t>(), zero.data_ptr<scalar_t>(), W_r.data_ptr<scalar_t>(), h, w); })(); } default: if (!(false)) { ::c10::detail::torchCheckFail( __func__, "hqq_aten_cuda_kernel.cu", static_cast<uint32_t>(412), (::c10::detail::torchCheckMsgImpl( "Expected " "false" " to be true, but got false.  " "(Could this error message be improved?  If so, " "please report an enhancement request to PyTorch.)", '"', at_dispatch_name, "\" not implemented for '", toString(_st), "'"))); }; } }()
                                                                                                                                                      ^

5 errors detected in the compilation of "hqq_aten_cuda_kernel.cu".
error: command [...]/bin/nvcc' failed with exit code 2

```


### mobicham · 2025-04-30

You need to pull the latest version from master

> I pushed some fixes, can you try again please:
> `pip uninstall hqq hqq_aten; pip install git+https://github.com/mobiusml/hqq/;`



### DominikHil · 2025-05-02

I did that and it worked without issues. However, just to make sure I also ran cloned the hqq repo again and ran `python3 setup_cuda.py install` in `hqq/hqq/kernels`. That also worked without any issues :)
From my side you can close this issue. Thanks for your help!

### mobicham · 2025-05-02

Great, thanks!
