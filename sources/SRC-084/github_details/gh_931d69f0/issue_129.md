# [Issue #129] cache_size_limit reached

source: https://github.com/dropbox/hqq/issues/129
state: closed | updated: 2024-11-01T18:45:28Z
labels: 

## 正文

Hello, brother. I am running this https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py on A100-40GB, and I get the following error. What should I do?

## code
The code is the code in the link. Adding the following two lines should not affect it:
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false

## result
root@0d2c83196670:/workspace# python example2_4.py
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00,  3.02it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 130/130 [00:00<00:00, 332.59it/s]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 225/225 [00:19<00:00, 11.38it/s]
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 225/225 [00:01<00:00, 116.87it/s]
  0%|                                                                                                                                                     | 0/5 [00:00<?, ?it/s]No chat template is set for this tokenizer, falling back to a default class-level template. This is very error-prone, because models are often trained with templates different from the class default! Default chat templates are a legacy feature and will be removed in Transformers v4.43, at which point any code depending on them will stop working. We recommend setting a valid chat template before then to ensure that this model continues working without issues.
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
/usr/lib/python3.8/contextlib.py:83: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
W1031 00:31:42.775483 139927651080000 torch/_dynamo/convert_frame.py:762] [0/8] torch._dynamo hit config.cache_size_limit (8)
W1031 00:31:42.775483 139927651080000 torch/_dynamo/convert_frame.py:762] [0/8]    function: 'forward' (/usr/local/lib/python3.8/dist-packages/transformers/models/llama/modeling_llama.py:1126)
W1031 00:31:42.775483 139927651080000 torch/_dynamo/convert_frame.py:762] [0/8]    last reason: tensor 'L['input_ids']' stride mismatch at index 0. expected 19, actual 27
W1031 00:31:42.775483 139927651080000 torch/_dynamo/convert_frame.py:762] [0/8] To log all recompilation reasons, use TORCH_LOGS="recompiles".
W1031 00:31:42.775483 139927651080000 torch/_dynamo/convert_frame.py:762] [0/8] To diagnose recompilation issues, see https://pytorch.org/docs/main/torch.compiler_troubleshooting.html.
  0%|                                                                                                                                                     | 0/5 [01:57<?, ?it/s]
Traceback (most recent call last):
  File "example2_4.py", line 44, in <module>
    patch_model_for_compiled_runtime(model, tokenizer, warmup=True)
  File "/usr/local/lib/python3.8/dist-packages/hqq/utils/generation_hf.py", line 93, in patch_model_for_compiled_runtime
    model.generate(
  File "/usr/local/lib/python3.8/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/transformers/generation/utils.py", line 1914, in generate
    result = self._sample(
  File "/usr/local/lib/python3.8/dist-packages/transformers/generation/utils.py", line 2651, in _sample
    outputs = self(
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/hqq/utils/generation_hf.py", line 83, in custom_forward
    out = out_fct(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torch/_dynamo/eval_frame.py", line 433, in _fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torch/_dynamo/convert_frame.py", line 1116, in __call__
    return self._torchdynamo_orig_callable(
  File "/usr/local/lib/python3.8/dist-packages/torch/_dynamo/convert_frame.py", line 472, in __call__
    return _compile(
  File "/usr/local/lib/python3.8/dist-packages/torch/_utils_internal.py", line 84, in wrapper_function
    return StrobelightCompileTimeProfiler.profile_compile_time(
  File "/usr/local/lib/python3.8/dist-packages/torch/_strobelight/compile_time_profiler.py", line 129, in profile_compile_time
    return func(*args, **kwargs)
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "/usr/local/lib/python3.8/dist-packages/torch/_dynamo/convert_frame.py", line 774, in _compile
    unimplemented(f"{limit_type} reached")
  File "/usr/local/lib/python3.8/dist-packages/torch/_dynamo/exc.py", line 221, in unimplemented
    raise Unsupported(msg)
torch._dynamo.exc.Unsupported: cache_size_limit reached



## 评论 (22)

### zhangy659 · 2024-10-30

### When I remove these two lines from the code, there are no more errors reported.

```python
from hqq.utils.generation_hf import patch_model_for_compiled_runtime
patch_model_for_compiled_runtime(model, tokenizer, warmup=True)
```

### mobicham · 2024-10-30

Hello, this is related to torch.compile, what version of pytorch are you running? You need at least 2.4.1, if not 2.5.0 or the nightly 

### zhangy659 · 2024-10-31

I changed torch2.5, transformers=4.42.1, hqq=0.2.2, on A100-40GB, the previous problem did not occur, but the warmup process occupied too much memory, and I ran out of memory when I reached the third sentence. What should I do? @mobicham 


# code
```python
import torch
import os
import torch._dynamo
from transformers import HqqConfig
torch._dynamo.config.cache_size_limit = 64  
os.environ["TORCH_LOGS"] = "recompiles"
```

os.environ["TOKENIZERS_PARALLELISM"] = "false"
device = 'cuda:0'
backend = 'torchao_int4' #"torchao_int4" (4-bit only) or "bitblas" (4-bit + 2-bit)
compute_dtype = torch.float16 if backend=="bitblas" else torch.bfloat16
cache_dir = '.' 
model_id = './llama/llama2_hf'

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *

HQQLinear.set_backend(HQQBackend.PYTORCH)
quant_config = HqqConfig(nbits=4,group_size=64,axis=1)

tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_dir, torch_dtype=compute_dtype,quantization_config = quant_config,device_map=device,attn_implementation="sdpa")


from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend=backend, verbose=True)
```

from hqq.utils.generation_hf import patch_model_for_compiled_runtime

patch_model_for_compiled_runtime(model, tokenizer, warmup=True)

```python
system_prompt = None 
prompt = "Write an essay about large language models."

messages = [] if(system_prompt is None) else [{"role": "system", "content": system_prompt}]
messages += [{"role": "user", "content": prompt},]
```

inputs = tokenizer([tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)],return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=1000, cache_implementation="static", pad_token_id=tokenizer.pad_token_id) 



# result
root@306f48790b3a:/workspace# python example2_4.py
Warning: Quantized meta-data is deprecated and will be removed. It is not supported for quantized model serialization.
Loading checkpoint shards:   0%|                                                                                                                          | 0/3 [00:00<?, ?it/s]Warning: Quantizing zeros/scales is deprecated. This setting will be ignored.
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:21<00:00,  7.00s/it]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 225/225 [00:01<00:00, 128.16it/s]
get here 54
  0%|                                                                                                                                                     | 0/3 [00:00<?, ?it/s]Write an essay about large language models.
No chat template is set for this tokenizer, falling back to a default class-level template. This is very error-prone, because models are often trained with templates different from the class default! Default chat templates are a legacy feature and will be removed in Transformers v4.43, at which point any code depending on them will stop working. We recommend setting a valid chat template before then to ensure that this model continues working without issues.
CUDAGraph supports dynamic shapes by recording a new graph for each distinct input size. Recording too many CUDAGraphs may lead to extra overhead. We have observed 51 distinct sizes. Please consider the following options for better performance: a) padding inputs to a few fixed number of shapes; or b) set torch._inductor.config.triton.cudagraph_skip_dynamic_graphs=True. Set torch._inductor.config.triton.cudagraph_dynamic_shape_warn_limit=None to silence this warning.
 33%|███████████████████████████████████████████████                                                                                              | 1/3 [00:58<01:57, 58.72s/it]Tell me a funny joke!
 67%|█████████████████████████████████████████████████████████████████████████████████████████████▎                                              | 2/3 [09:08<05:12, 312.49s/it]How to make a yummy chocolate cake?
CUDAGraph supports dynamic shapes by recording a new graph for each distinct input size. Recording too many CUDAGraphs may lead to extra overhead. We have observed 51 distinct sizes. Please consider the following options for better performance: a) padding inputs to a few fixed number of shapes; or b) set torch._inductor.config.triton.cudagraph_skip_dynamic_graphs=True. Set torch._inductor.config.triton.cudagraph_dynamic_shape_warn_limit=None to silence this warning.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [09:56<00:00, 198.78s/it]
Traceback (most recent call last):
  File "/workspace/example2_4.py", line 63, in <module>
    outputs = model.generate(**inputs, max_new_tokens=1000, cache_implementation="static", pad_token_id=tokenizer.pad_token_id) 
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 1914, in generate
    result = self._sample(
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2651, in _sample
    outputs = self(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/hqq/utils/generation_hf.py", line 82, in custom_forward
    out = out_fct(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/external_utils.py", line 38, in inner
    @functools.wraps(fn)
  File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_functorch/aot_autograd.py", line 1100, in forward
    return compiled_fn(full_args)
  File "/usr/local/lib/python3.10/dist-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 321, in runtime_wrapper
    all_outs = call_func_at_runtime_with_args(
  File "/usr/local/lib/python3.10/dist-packages/torch/_functorch/_aot_autograd/utils.py", line 124, in call_func_at_runtime_with_args
    out = normalize_as_list(f(args))
  File "/usr/local/lib/python3.10/dist-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 667, in inner_fn
    outs = compiled_fn(args)
  File "/usr/local/lib/python3.10/dist-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 488, in wrapper
    return compiled_fn(runtime_args)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/codecache.py", line 1478, in __call__
    return self.current_callable(inputs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/compile_fx.py", line 1008, in run
    return compiled_fn(new_inputs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 382, in deferred_cudagraphify
    return fn(inputs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/utils.py", line 1977, in run
    return model(new_inputs)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 1919, in run
    out = self._run(new_inputs, function_id)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 2089, in _run
    return self.record_function(new_inputs, function_id)
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 2123, in record_function
    node = CUDAGraphNode(
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 970, in __init__
    self.recording_outputs: Optional[OutputType] = self._record(
  File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/cudagraph_trees.py", line 1196, in _record
    with preserve_rng_state(), torch.cuda.device(
  File "/usr/local/lib/python3.10/dist-packages/torch/cuda/graphs.py", line 186, in __exit__
    self.cuda_graph.capture_end()
  File "/usr/local/lib/python3.10/dist-packages/torch/cuda/graphs.py", line 84, in capture_end
    super().capture_end()
RuntimeError: CUDA error: out of memory
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. 

### mobicham · 2024-10-31

You are using `device_map=device` which will cause the model to be transferred to the GPU before quantization, among other things.

Can you run this script exactly as it is, **please don't change anything other than the model_id**: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py

I just tried it, it should work fine and should only take 5-6 GB for a 7-8B model.

### zhangy659 · 2024-10-31

Sorry, brother. Now, I just ran the code in the link directly. I first ran llama2-7B, then llama3-8B. I could only run the third sample in warmup on llama2, but I completed the entire program on llama3. For llama3, the initial video memory usage was 6758MiB, and at 20% it was 7424MiB. Here, the video memory usage slowly increased by almost 20GB, and then the video memory usage increased for each example, finally using up almost 40g. I saw the output prompt message saying that 51 computation graphs were generated, and I could skip dynamic computation graphs
torch._ inductor.config.triton.cudagraph_skip_dynamic_graphs = True, do I need to do this?  @mobicham 
![图片1](https://github.com/user-attachments/assets/41de53ca-bb2a-43a1-8e83-c02a80faedf8)
![图片2](https://github.com/user-attachments/assets/6a839e16-972b-41d9-bfe2-1aa56f8f7f7b)
![图片3](https://github.com/user-attachments/assets/a53997fd-3232-409a-9fe7-9ab8fac3ccad)




### mobicham · 2024-10-31

The increase from 6GB to 7GB is normal: the model is taking 6GB in VRAM but it needs to allocate the KV cache, so that's the rest. But the increase to 40 GB is very strange indeed! I am not sure why is it's complaining about dynamic shapes, there are no dynamic shapes in the decoding phase. So maybe it's not using static cache :thinking: 

Can you please print the following:
```Python
import torch; print(torch.__version__);
import transformers; print(transformers.__version__);
```
and your CUDA version as well. 

### mobicham · 2024-10-31

Are running the models in the same python session or are you closing the session after each model? 

### zhangy659 · 2024-10-31

Ok, thank you. This is my configuration
![图片4](https://github.com/user-attachments/assets/91b3d2aa-ac8e-4e2e-8391-5f44ec8dd541)


### zhangy659 · 2024-10-31

I ran python hqq_lib_demo.py twice in the terminal, for llama2 and llama3 respectively. This time, I tried to 
import torch._ inductor.config
torch._inductor.config.triton.cudagraph_skip_dynamic_graphs = True, this has the effect. For llama2 and llama3, the maximum size should not exceed 7GB. Here are some tips during the testing process
![image](https://github.com/user-attachments/assets/82c87011-e406-449f-8105-3fbef67c4d86)


### mobicham · 2024-10-31

Can you try the following:
Install CUDA 12.1 and do this:

```
export CUDA_HOME=/usr/local/cuda-12.1
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
export PATH=${CUDA_HOME}/bin:${PATH}
```
Then
```
pip uninstall torch; pip uninstall hqq;
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install --upgrade  transformers hqq;
```



### zhangy659 · 2024-10-31

 Okay, let me try.


### mobicham · 2024-10-31

> I ran python hqq_lib_demo.py twice in the terminal, for llama2 and llama3 respectively. This time, I tried to import torch._ inductor.config torch._inductor.config.triton.cudagraph_skip_dynamic_graphs = True, this has the effect. For llama2 and llama3, the maximum size should not exceed 7GB. Here are some tips during the testing process ![image](https://private-user-images.githubusercontent.com/70420272/381955537-82c87011-e406-449f-8105-3fbef67c4d86.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzAzODA3NTksIm5iZiI6MTczMDM4MDQ1OSwicGF0aCI6Ii83MDQyMDI3Mi8zODE5NTU1MzctODJjODcwMTEtZTQwNi00NDlmLTgxMDUtM2ZiZWY2N2M0ZDg2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDMxVDEzMTQxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE0MGU4NDk4MzUyOWEzODgxODg1ZjEwYWQyNzVkNTg2OTQ5MDM1OGQwODEyN2FkYTlkM2YzYTE0ODM2ODk4ODQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.tQ4Pw5jem7KvPHcA2oK5JemAF4WYbStA0TqdWd7PjpY)

But this should not happen, if it happens it means it cannot run cuda graphs and performance will be very bad

### zhangy659 · 2024-10-31

I forgot to mention that the environment I used before was NVIDIA's docker image nvcr.io/nvidia/pytorch:24.02-py3. Since it contained torch2.3, I uninstalled torch2.3 and installed torch2.5. Then, I installed transformers=4.42.1 and hqq. This is the basic environment of this image
![image](https://github.com/user-attachments/assets/eae7ee88-886e-48c8-bc81-846822433e24)


### mobicham · 2024-10-31

Yeah that should work fine I think, but I haven't tested with CUDA 12.4 (your pytorch version is using 12.4), if you can test with CUDA 12.1 with the commands I shared then we can confirm if the problem comes from CUDA version. Because right now I can't reproduce it and I tested across various gpus with CUDA 12.1, no issue

### zhangy659 · 2024-10-31

Ok, thank you. I am now configuring the environment for CUDA 12.1.

### mobicham · 2024-10-31

I tested with `pytorch/pytorch:2.3.1-cuda12.1-cudnn8-devel`
but of course had to upgrade torch, etc.

### zhangy659 · 2024-10-31

@mobicham  This time I tested on CUDA 12.1, torch2.5.1+cu121. The test results are the same as before, and the memory usage increases significantly during warmup. I think there are several possible reasons: 1. I used transformers==4.42.1 instead of the latest transformers==4.46.1 because 4.46.1 would report template errors; 2. The following prompts are constantly generated when the code is executed
/usr/lib/python3.10/contextlib.py:103: FutureWarning: torch.backends.cuda.sdp_kernel() is deprecated. In the future, this context manager will be removed. Please see torch.nn.attention.sdpa_kernel() for the new context manager, with updated signature.
The issue with the self.gen = func(*args, **kwds)3 computation graph is that the model I tested was llama3-8B, not llama3-8B-instruct. All the points I can think of are here. The good thing is that this program is still a little short of the maximum memory, but it runs smoothly.
![image](https://github.com/user-attachments/assets/14ed4538-c47a-477c-8d23-88dcbd3f2298)
![image](https://github.com/user-attachments/assets/74f32e4e-ff84-4c28-8049-02071ea1a5c9)


### zhangy659 · 2024-10-31

When I use transformers==4.46.1, the following error occurs
![image](https://github.com/user-attachments/assets/4a6499aa-3d3e-446b-b018-35853031b758)


### zhangy659 · 2024-10-31

## the result of pip list:

Package                  Version
------------------------ -------------------------------
absl-py                  1.4.0
accelerate               1.0.1
aiohttp                  3.8.4
aiosignal                1.3.1
apex                     0.1
argon2-cffi              21.3.0
argon2-cffi-bindings     21.2.0
asttokens                2.2.1
astunparse               1.6.3
async-timeout            4.0.2
attrs                    23.1.0
audioread                3.0.0
backcall                 0.2.0
beautifulsoup4           4.12.2
bleach                   6.0.0
blis                     0.7.9
cachetools               5.3.0
catalogue                2.0.8
certifi                  2022.12.7
cffi                     1.15.1
charset-normalizer       3.1.0
click                    8.1.3
cloudpickle              2.2.1
cmake                    3.24.1.1
comm                     0.1.3
confection               0.0.4
contourpy                1.0.7
cubinlinker              0.2.2+2.g2f92cb3
cuda-python              12.1.0rc5+1.gcdeccdd
cudf                     23.4.0
cugraph                  23.4.0
cugraph-dgl              23.4.0
cugraph-service-client   23.4.0
cugraph-service-server   23.4.0
cuml                     23.4.0
cupy-cuda12x             12.0.0b3
cycler                   0.11.0
cymem                    2.0.7
Cython                   0.29.34
dask                     2023.3.2
dask-cuda                23.4.0
dask-cudf                23.4.0
debugpy                  1.6.7
decorator                5.1.1
defusedxml               0.7.1
distributed              2023.3.2.1
einops                   0.6.1
exceptiongroup           1.1.1
execnet                  1.9.0
executing                1.2.0
expecttest               0.1.3
fastjsonschema           2.16.3
fastrlock                0.8.1
filelock                 3.12.0
flash-attn               1.0.5
fonttools                4.39.3
frozenlist               1.3.3
fsspec                   2024.10.0
gast                     0.4.0
google-auth              2.18.1
google-auth-oauthlib     0.4.6
graphsurgeon             0.4.6
grpcio                   1.54.2
hqq                      0.2.2
hqq-aten                 0.0.0
huggingface-hub          0.26.2
hypothesis               5.35.1
idna                     3.4
importlib-metadata       6.6.0
iniconfig                2.0.0
intel-openmp             2021.4.0
ipykernel                6.23.1
ipython                  8.13.2
ipython-genutils         0.2.0
jedi                     0.18.2
Jinja2                   3.1.2
joblib                   1.2.0
json5                    0.9.14
jsonschema               4.17.3
jupyter_client           8.2.0
jupyter_core             5.3.0
jupyter-tensorboard      0.2.0
jupyterlab               2.3.2
jupyterlab-pygments      0.2.2
jupyterlab-server        1.2.0
jupytext                 1.14.5
kiwisolver               1.4.4
langcodes                3.3.0
librosa                  0.9.2
lit                      16.0.5
llvmlite                 0.39.1
locket                   1.0.0
Markdown                 3.4.3
markdown-it-py           2.2.0
MarkupSafe               2.1.2
matplotlib               3.7.1
matplotlib-inline        0.1.6
mdit-py-plugins          0.3.5
mdurl                    0.1.2
mistune                  2.0.5
mkl                      2021.1.1
mkl-devel                2021.1.1
mkl-include              2021.1.1
mock                     5.0.2
mpmath                   1.3.0
msgpack                  1.0.5
multidict                6.0.4
murmurhash               1.0.9
nbclient                 0.7.4
nbconvert                7.4.0
nbformat                 5.8.0
nest-asyncio             1.5.6
networkx                 2.6.3
ninja                    1.11.1
notebook                 6.4.10
numba                    0.56.4
numpy                    1.24.4
nvidia-cublas-cu12       12.1.3.1
nvidia-cuda-cupti-cu12   12.1.105
nvidia-cuda-nvrtc-cu12   12.1.105
nvidia-cuda-runtime-cu12 12.1.105
nvidia-cudnn-cu12        9.1.0.70
nvidia-cufft-cu12        11.0.2.54
nvidia-curand-cu12       10.3.2.106
nvidia-cusolver-cu12     11.4.5.107
nvidia-cusparse-cu12     12.1.0.106
nvidia-dali-cuda120      1.25.0
nvidia-nccl-cu12         2.21.5
nvidia-nvjitlink-cu12    12.1.105
nvidia-nvtx-cu12         12.1.105
nvidia-pyindex           1.0.9
nvtx                     0.2.5
oauthlib                 3.2.2
onnx                     1.13.1rc2
opencv                   4.6.0
packaging                23.1
pandas                   1.5.2
pandocfilters            1.5.0
parso                    0.8.3
partd                    1.4.0
pathy                    0.10.1
pexpect                  4.8.0
pickleshare              0.7.5
Pillow                   9.2.0
pip                      24.3.1
platformdirs             3.5.1
pluggy                   1.0.0
ply                      3.11
polygraphy               0.47.1
pooch                    1.7.0
preshed                  3.0.8
prettytable              3.7.0
prometheus-client        0.16.0
prompt-toolkit           3.0.38
protobuf                 3.20.3
psutil                   5.9.4
ptxcompiler              0.7.0+27.g601c71a
ptyprocess               0.7.0
pure-eval                0.2.2
pyarrow                  10.0.1.dev0+ga6eabc2b.d20230428
pyasn1                   0.5.0
pyasn1-modules           0.3.0
pybind11                 2.10.4
pycocotools              2.0+nv0.7.3
pycparser                2.21
pydantic                 1.10.7
Pygments                 2.15.1
pylibcugraph             23.4.0
pylibcugraphops          23.4.0
pylibraft                23.4.0
pynvml                   11.4.1
pyparsing                3.0.9
pyrsistent               0.19.3
pytest                   7.3.1
pytest-rerunfailures     11.1.2
pytest-shard             0.1.2
pytest-xdist             3.3.1
python-dateutil          2.8.2
python-hostlist          1.23.0
pytorch-quantization     2.1.2
pytz                     2023.3
PyYAML                   6.0
pyzmq                    25.0.2
raft-dask                23.4.0
regex                    2023.5.5
requests                 2.29.0
requests-oauthlib        1.3.1
resampy                  0.4.2
rmm                      23.4.0
rsa                      4.9
safetensors              0.4.5
scikit-learn             1.2.0
scipy                    1.10.1
seaborn                  0.12.2
Send2Trash               1.8.2
setuptools               65.5.1
six                      1.16.0
smart-open               6.3.0
sortedcontainers         2.4.0
soundfile                0.12.1
soupsieve                2.4.1
spacy                    3.5.3
spacy-legacy             3.0.12
spacy-loggers            1.0.4
sphinx-glpi-theme        0.3
srsly                    2.4.6
stack-data               0.6.2
sympy                    1.13.1
tabulate                 0.9.0
tbb                      2021.9.0
tblib                    1.7.0
tensorboard              2.9.0
tensorboard-data-server  0.6.1
tensorboard-plugin-wit   1.8.1
tensorrt                 8.6.1
termcolor                2.5.0
terminado                0.17.1
thinc                    8.1.10
threadpoolctl            3.1.0
thriftpy2                0.4.16
tinycss2                 1.2.1
tokenizers               0.20.1
toml                     0.10.2
tomli                    2.0.1
toolz                    0.12.0
torch                    2.5.1+cu121
torch-tensorrt           1.4.0.dev0
torchdata                0.9.0
torchtext                0.18.0
torchvision              0.20.1+cu121
tornado                  6.3.1
tqdm                     4.65.0
traitlets                5.9.0
transformer-engine       0.8.0
transformers             4.46.1
treelite                 3.2.0
treelite-runtime         3.2.0
triton                   3.1.0
typer                    0.7.0
types-dataclasses        0.6.6
typing_extensions        4.9.0
ucx-py                   0.31.0
uff                      0.6.9
urllib3                  1.26.15
wasabi                   1.1.1
wcwidth                  0.2.6
webencodings             0.5.1
Werkzeug                 2.3.4
wheel                    0.40.0
xdoctest                 1.0.2
xgboost                  1.7.5
yarl                     1.9.2
zict                     3.0.0
zipp                     3.15.0

### zhangy659 · 2024-10-31

I think I have solved this problem. @mobicham  I took two steps. First, I used transformers=4.46.1, so I changed the chat_template. This should not be the key; Secondly, I added the following two lines after AutoTokenizer.from_pretrain() in hqq_lib_demo.py, 
  if tokenizer.pad_token_id is None:
       tokenizer.pad_token_id = tokenizer.eos_token_id 
Because I suddenly realized that some models do not have tokenizer.pad_token_id, I have seen tokenizer.pad_token_id = tokenizer.eos_token_id in many codes. I think this is the key to solving the problem. After making the two modifications above, the code executed as expected, with a video memory usage of 6-7G.
![image](https://github.com/user-attachments/assets/a2797fec-def8-4f96-9a8f-59ae893d1d66)
![image](https://github.com/user-attachments/assets/1e4539da-f1bc-4bd9-8bcf-3677556385c4)
![image](https://github.com/user-attachments/assets/8dc0c17f-fd8a-4497-8049-ba8e26fed233)


### zhangy659 · 2024-10-31

I used transformers==4.42.1 again, this time I didn't modify the template, only added pad_token_id, but the memory usage was still high and there were still problems. It seems that there is a problem with the template. Then I modified the template without adding pad_token_id, but the same problem of large memory usage occurred. Then I modified the template and added pad_token_id, but the memory usage was still very high. It seems that there is a problem with transformers==4.42.1. Finally, I changed back to transformers==4.46.1 + without adding pad_token_id, and the problem was resolved. Now I can confirm that it has nothing to do with pad_token_id, and should use transformers==4.46.1 + the correct template design.
![image](https://github.com/user-attachments/assets/3bbea233-47c2-4912-b3f7-0e3c12730e7e)


### mobicham · 2024-11-01

Thanks a lot for investigating! Strange, I didn't have a problem. You don't need the chat template for the warm-up actually, but you need for generation after.
