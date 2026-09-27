# [Issue #111] Quesiton on the speed for generating the response

source: https://github.com/dropbox/hqq/issues/111
state: closed | updated: 2024-08-28T07:44:06Z
labels: 

## 正文

Can I ask, I tried following the usage on Hugging Face, but it takes almost 100 seconds to generate a response to the question 'Write an essay about large language models.' However, when I use the ollama/llama3.1 model directly, it only takes about 7-8 seconds to generate the response. Is this normal?

This is the code i using

import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
#model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq' #no calib version
model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib' #calibrated version

compute_dtype = torch.float16 #bfloat16 for torchao, float16 for bitblas
cache_dir = '.'
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype, map_location=torch.device('cuda'))
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
patch_linearlayers(model, patch_add_quant_config, quant_config)

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
#prepare_for_inference(model, backend="torchao_int4") 
prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter 
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

gen.generate("Write an essay about large language models", print_tokens=True)
gen.generate("Tell me a funny joke!", print_tokens=True)
gen.generate("How to make a yummy chocolate cake?", print_tokens=True)

## 评论 (18)

### mobicham · 2024-08-27

Hi! What gpu did you use ? You need at least Ampere

### NEWbie0709 · 2024-08-27

hi im using 4090


### mobicham · 2024-08-27

Can you try this, and run with `OMP_NUM_THREADS=$NUM_THREADS CUDA_VISIBLE_DEVICES=0 ipython3 `
where `$NUM_THREADS` is the number of the threads available in your machine/virtual env (not the total number of threads in the case of a virtual env). Also, please wait for the wamup to finish:

Also, did you install BitBlas before ? `pip install bitblas`, you should have seen a warning:

> Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).


```Python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
#model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq' #no calib version
model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib' #calibrated version

compute_dtype = torch.bfloat16 #bfloat16 for torchao, float16 for bitblas
cache_dir = '.'
device = 'cuda:0`
model = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
patch_linearlayers(model, patch_add_quant_config, quant_config)

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
prepare_for_inference(model, backend="torchao_int4")
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

import time
t1 = time.time()
out = gen.generate("Write an essay about large language models", print_tokens=False)
t2 = time.time()
print('Took', t2-t1, 'secs')
```

### mobicham · 2024-08-27

I am getting ~138 tokens per sec, which is about 6-7 seconds end-to-end, depending on the output (since sampling is enabled `do_sample=True` so the output is not deterministic), so it's actually faster than ollama

### NEWbie0709 · 2024-08-27

yeah i did install and received the warning
![image](https://github.com/user-attachments/assets/80663e1b-9c14-4a6a-a763-156f6b1e8a20)
and also can i know how to set OMP_NUM_THREADS=$NUM_THREADS CUDA_VISIBLE_DEVICES=0 ipython3 ?


### NEWbie0709 · 2024-08-27

I tried running the code you gave me, and it showed this error
![image](https://github.com/user-attachments/assets/9421264f-c5b3-4137-80ca-41a65ef8862c)


### mobicham · 2024-08-27

It seems like you are using an older version of Pytorch, can you try the following: 
### Step 1: Installation
Make sure you use the right CUDA version (here it's using 12.1)
```
pip uninstall torch -y; pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121;
pip install git+https://github.com/mobiusml/hqq.git;
pip install bitblas; # only if you want to use the bitblas backend
```
### Step 2: Run
```
export OMP_NUM_THREADS=16; #if you have 16 threads for example
```
then you can run the code:
```Python
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator

#Load the model
###################################################
#model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq' #no calib version
model_id = 'mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib' #calibrated version

compute_dtype = torch.bfloat16 #bfloat16 for torchao, float16 for bitblas
cache_dir = '.'
device = 'cuda:0`
model = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1)
patch_linearlayers(model, patch_add_quant_config, quant_config)

#Use optimized inference kernels
###################################################
HQQLinear.set_backend(HQQBackend.PYTORCH)
#prepare_for_inference(model) #default backend
prepare_for_inference(model, backend="torchao_int4")
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

import time
t1 = time.time()
out = gen.generate("Write an essay about large language models", print_tokens=False)
t2 = time.time()
print('Took', t2-t1, 'secs')
```




### NEWbie0709 · 2024-08-27

i tried following all the step and it shows this error
![image](https://github.com/user-attachments/assets/e11d617d-7487-41c5-98b8-7b2634bd5ddd)
the device im using is window 
tried to pip install it and it shows this
![Uploading image.png…]()


### NEWbie0709 · 2024-08-27

this is the full error 
(pytorch_model) PS C:\Users\i9-4090\documents\tianyi> python testing.py
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
Fetching 7 files: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<?, ?it/s]
C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\hqq\models\base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 131/131 [00:00<00:00, 4507.27it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 225/225 [00:00<00:00, 15890.46it/s]
  0%|                                                                                                                                     | 0/999 [00:00<?, ?it/s]C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\contextlib.py:87: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
  0%|                                                                                                                                     | 0/999 [00:14<?, ?it/s]
Traceback (most recent call last):
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\output_graph.py", line 1446, in _call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\repro\after_dynamo.py", line 129, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\repro\after_dynamo.py", line 129, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\__init__.py", line 2239, in __call__
    return compile_fx(model_, inputs_, config_patches=self.config)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 1253, in compile_fx
    return compile_fx(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 1521, in compile_fx
    return aot_autograd(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\backends\common.py", line 72, in __call__
    cg = aot_module_simplified(gm, example_inputs, **self.kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_functorch\aot_autograd.py", line 1071, in aot_module_simplified
    compiled_fn = dispatch_and_compile()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_functorch\aot_autograd.py", line 1056, in dispatch_and_compile
    compiled_fn, _ = create_aot_dispatcher_function(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_functorch\aot_autograd.py", line 522, in create_aot_dispatcher_function
    return _create_aot_dispatcher_function(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_functorch\aot_autograd.py", line 759, in _create_aot_dispatcher_function
    compiled_fn, fw_metadata = compiler_fn(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_functorch\_aot_autograd\jit_compile_runtime_wrappers.py", line 179, in aot_dispatch_base
    compiled_fw = compiler(fw_module, updated_flat_args)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 1350, in fw_compiler_base
    return _fw_compiler_base(model, example_inputs, is_inference)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 1421, in _fw_compiler_base
    return inner_compile(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 475, in compile_fx_inner
    return wrap_compiler_debug(_compile_fx_inner, compiler_name="inductor")(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\repro\after_aot.py", line 85, in debug_wrapper
    inner_compiled_fn = compiler_fn(gm, example_inputs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 661, in _compile_fx_inner
    compiled_graph = FxGraphCache.load(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\codecache.py", line 1327, in load
    compiled_graph = compile_fx_fn(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 570, in codegen_and_compile
    compiled_graph = fx_codegen_and_compile(gm, example_inputs, **fx_kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\compile_fx.py", line 878, in fx_codegen_and_compile
    compiled_fn = graph.compile_to_fn()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\graph.py", line 1855, in compile_to_fn
    return self.compile_to_module().call
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\graph.py", line 1781, in compile_to_module
    return self._compile_to_module()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\graph.py", line 1787, in _compile_to_module
    self.codegen_with_cpp_wrapper() if self.cpp_wrapper else self.codegen()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\graph.py", line 1722, in codegen
    self.scheduler = Scheduler(self.operations)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 1624, in __init__
    self._init(nodes)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 1642, in _init
    self.nodes = [self.create_scheduler_node(n) for n in nodes]
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 1642, in <listcomp>
    self.nodes = [self.create_scheduler_node(n) for n in nodes]
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 1748, in create_scheduler_node
    return SchedulerNode(self, node)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 819, in __init__
    self._compute_attrs()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 830, in _compute_attrs
    group_fn = self.scheduler.get_backend(self.node.get_device()).group_fn
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 3126, in get_backend
    self.backends[device] = self.create_backend(device)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_inductor\scheduler.py", line 3118, in create_backend
    raise RuntimeError(
RuntimeError: Cannot find a working triton installation. Either the package is not installed or it is too old. More information on installing Triton can be found at https://github.com/openai/triton

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\i9-4090\documents\tianyi\testing.py", line 155, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\hqq\utils\generation_hf.py", line 100, in warmup
    self.generate(prompt, print_tokens=False);
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\utils\_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\hqq\utils\generation_hf.py", line 253, in generate
    return self.next_token_iterator(self.prefill(), self.max_new_tokens, verbose, print_tokens)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\hqq\utils\generation_hf.py", line 222, in next_token_iterator
    next_token = self.gen_next_token(next_token)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\hqq\utils\generation_hf.py", line 200, in gen_next_token
    next_token = self.decode_one_token(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\eval_frame.py", line 469, in _fn
    return fn(*args, **kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 1243, in __call__
    return self._torchdynamo_orig_callable(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 516, in __call__
    return _compile(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 907, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 655, in compile_inner
    return _compile_inner(code, one_graph, hooks, transform)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_utils_internal.py", line 87, in wrapper_function
    return function(*args, **kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 688, in _compile_inner
    out_code = transform_code_object(code, transform)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\bytecode_transformation.py", line 1322, in transform_code_object
    transformations(instructions, code_options)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 210, in _fn
    return fn(*args, **kwargs)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\convert_frame.py", line 624, in transform
    tracer.run()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\symbolic_convert.py", line 2797, in run
    super().run()
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\symbolic_convert.py", line 983, in run
    while self.step():
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\symbolic_convert.py", line 2988, in RETURN_VALUE
    self._return(inst)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\symbolic_convert.py", line 2973, in _return
    self.output.compile_subgraph(
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\output_graph.py", line 1142, in compile_subgraph
    self.compile_and_call_fx_graph(tx, pass2.graph_output_vars(), root)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\output_graph.py", line 1369, in compile_and_call_fx_graph
    compiled_fn = self.call_user_compiler(gm)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\output_graph.py", line 1416, in call_user_compiler
    return self._call_user_compiler(gm)
  File "C:\Users\i9-4090\miniconda3\envs\pytorch_model\lib\site-packages\torch\_dynamo\output_graph.py", line 1465, in _call_user_compiler
    raise BackendCompilerFailed(self.compiler_fn, e) from e
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
RuntimeError: Cannot find a working triton installation. Either the package is not installed or it is too old. More information on installing Triton can be found at https://github.com/openai/triton

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True


### mobicham · 2024-08-27

The error message says that you don't have `triton` installed. Normally it should be installed automatically when you install the latest torch version.
Can you show me your torch version
```import torch
print(torch.__version__)
```
Also install triton if it was not installed
```pip install triton```

### NEWbie0709 · 2024-08-27

torch version :2.5.0.dev20240825+cu121
i tried installing the triton using pip install but it show this
![image](https://github.com/user-attachments/assets/a8d01d87-65c9-455e-a93f-1bc5a71eaab5)
is it because of window doesnt support triton?




### mobicham · 2024-08-27

Oh you are right, seems like it's not supported on Windows: https://github.com/triton-lang/triton/issues/1640 :disappointed: 

### NEWbie0709 · 2024-08-27

owh understand! thanks for the reply and explanation will try on the linux later ! 👍 

### NEWbie0709 · 2024-08-28

Sorry, one last question. Can I know what the format is after quantization using HQQ? Is it also in .pt, safetensor, or gguf? 
I'm planning to quantize this model, 
https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B-GGUF
and does it support Ollama (llama.cpp) after the quantization? Currently, we can run it directly on Ollama by creating a model file for it.

### mobicham · 2024-08-28

The format is custom only compatible with transformers. I am currently working to add full support directly on transformers https://github.com/huggingface/transformers/pull/33141 
It's not gonna work with GGUF / Ollama, only with transformers with custom code. 
There's some work to make it work with VLLM though.

### NEWbie0709 · 2024-08-28

Oh, okay, understand. Can you share some thoughts or guidance on how to make the HQQ quantized model work in VLLM?

### mobicham · 2024-08-28

I don't use it personally, but <a href="https://github.com/AnswerDotAI/vllm/commits/torchao/">this branch</a> implements the fast backends used in HQQ, but I can't find a clean example to see how it works 

### NEWbie0709 · 2024-08-28

understand thanks for the reply! 😃 
