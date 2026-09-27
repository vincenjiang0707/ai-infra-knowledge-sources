# [Issue #2805] During the gptq quantization process, the gpu memory usage increases until the oom?

source: https://github.com/ModelCloud/GPTQModel/issues/2805
state: closed | updated: 2026-04-23T04:16:15Z
labels: 

## 正文

quant llama2-7b use NV A800 *4

quant first layers use memory :

```py
 GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    4   N/A  N/A   1738415      C   python3                                    3418MiB |
|    5   N/A  N/A   1738415      C   python3                                    4298MiB |
|    6   N/A  N/A   1738415      C   python3                                    3590MiB |
|    7   N/A  N/A   1738415      C   python3                                    3654MiB |

but quant 30th layers the memory:
---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    4   N/A  N/A   1738415      C   python3                                    3558MiB |
|    5   N/A  N/A   1738415      C   python3                                   28370MiB |
|    6   N/A  N/A   1738415      C   python3                                   29572MiB |
|    7   N/A  N/A   1738415      C   python3                                   28114MiB |
```

I try gptqmodel=5.6.12 transformers==4.57.3 do not have this question
but use gptqmodel=6.1.0 transformers==5.4.0 have the question out of memory, follow shows:
```py
NFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram                             | dynamic |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 2.01G, 31.18G, 31.2G, 31.25G  |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  | gptq    | 15    | self_attn.v_proj          | 4096, 4096    | bf16: 33.0MB | 0.0000005537 | 10496   | 0.01000 | 3.535 | 1.190    | cuda 2.01G, 31.18G, 31.2G, 31.25G  |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 2.13G, 31.44G, 31.45G, 31.5G  |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +--------------------+-------+--------+-------+---------+--------+---------------------------------------------------+           
INFO  | Forward hook       | 18368 | 0.003  | 0.002 | 33.233  | 5.6%   | model.layers.15.mlp.down_proj                     |           
INFO  | Finalize create    | 105   | 0.569  | 0.192 | 20.178  | 3.4%   | model.layers.14.mlp.down_proj                     |           
INFO  | Post-quant replay  | 16    | 0.342  | 0.786 | 12.575  | 2.1%   | model.layers.15:subset4/4                         |           
INFO  | Capture inputs     | 1     | 2.760  | 2.760 | 2.760   | 0.5%   | cache_inputs:LlamaDecoderLayer                    |           
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram                             | dynamic |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 3.04G, 33.56G, 33.57G, 34.79G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  | gptq    | 16    | self_attn.q_proj          | 4096, 4096    | bf16: 33.0MB | 0.0000013944 | 10496   | 0.01000 | 3.581 | 0.260    | cuda 3.04G, 33.56G, 33.57G, 34.79G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 3.04G, 33.56G, 33.57G, 34.79G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +--------------------+-------+--------+-------+---------+--------+---------------------------------------------------+           
INFO  | Forward hook       | 19516 | 0.001  | 0.002 | 34.228  | 5.5%   | model.layers.16.mlp.down_proj                     |           
INFO  | Finalize create    | 112   | 0.411  | 0.192 | 21.510  | 3.5%   | model.layers.15.mlp.down_proj                     |           
INFO  | Post-quant replay  | 17    | 0.322  | 0.759 | 12.898  | 2.1%   | model.layers.16:subset4/4                         |           
INFO  | Capture inputs     | 1     | 2.760  | 2.760 | 2.760   | 0.4%   | cache_inputs:LlamaDecoderLayer                    |           
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram                             | dynamic |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 3.49G, 35.55G, 36.73G, 35.24G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  | gptq    | 17    | self_attn.q_proj          | 4096, 4096    | bf16: 33.0MB | 0.0000013474 | 10496   | 0.01000 | 3.683 | 0.246   
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+------------------------------------+---------+
INFO  | gptq    | 17    | self_attn.o_proj          | 4096, 4096    | bf16: 33.0MB | 0.0000000254 | 10496   | 0.01000 | 1.139 | 0.291   -+------------------------------------+---------+
INFO  GC completed in 0.036s (pass #7) at 2026-04-22T09:22:00.830032+00:00; devices=cuda:0, cuda:1, cuda:2, cuda:3; VRAM cuda:0=3.5G, cu
INFO  +--------------------+-------+--------+-------+---------+--------+---------------------------------------------------+           
INFO  | Forward hook       | 20664 | 0.002  | 0.002 | 35.217  | 5.4%   | model.layers.17.mlp.down_proj                     |           
INFO  | Finalize create    | 119   | 0.403  | 0.192 | 22.826  | 3.5%   | model.layers.16.mlp.down_proj                     |           
INFO  | Post-quant replay  | 18    | 0.289  | 0.733 | 13.187  | 2.0%   | model.layers.17:subset4/4                         |           
INFO  | Capture inputs     | 1     | 2.760  | 2.760 | 2.760   | 0.4%   | cache_inputs:LlamaDecoderLayer                    |           
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram                             | dynamic |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 3.48G, 38.64G, 37.06G, 37.48G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  | gptq    | 18    | self_attn.k_proj          | 4096, 4096    | bf16: 33.0MB | 0.0000014718 | 10496   | 0.01000 | 4.397 | 1.096    | cuda 3.48G, 38.64G, 37.06G, 37.48G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 3.48G, 38.64G, 37.21G, 37.49G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
INFO  +--------------------+-------+--------+-------+---------+--------+---------------------------------------------------+           
INFO  | Forward hook       | 21812 | 0.001  | 0.002 | 36.958  | 5.4%   | model.layers.18.mlp.down_proj                     |           
INFO  | Finalize create    | 126   | 0.428  | 0.192 | 24.192  | 3.5%   | model.layers.17.mlp.down_proj                     |           
INFO  | Post-quant replay  | 19    | 0.330  | 0.711 | 13.517  | 2.0%   | model.layers.18:subset4/4                         |           
INFO  | Capture inputs     | 1     | 2.760  | 2.760 | 2.760   | 0.4%   | cache_inputs:LlamaDecoderLayer                    |           
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram                             | dynamic |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+--------- | cuda 4.39G, 39.1G, 39.45G, 39.48G  |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+---------
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                        
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
WARN  GPTQ module 'mlp.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
Traceback (most recent call last):ll back to CPU Hessian accumulation due to GPU OOM during batch processing.                          
  File "/host/data/wdd/GPTQModel-6.1.0/basic_usage_wikitext2.py", line 232, in <module>░░░░░░░░░░░░░░░░| 0:04:59 / 0:07:58 [20/32] 62.5%
  File "/host/data/wdd/GPTQModel-6.1.0/basic_usage_wikitext2.py", line 186, in main
    print(f"保存量化模型到: {quantized_model_id}")
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/models/base.py", line 917, in quantize
    result = self._quantize_with_calibration(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/models/base.py", line 1077, in _quantize_with_calibration
    return module_looper.loop(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/module_looper.py", line 1385, in loop
    return self._loop_impl(fallback=fallback, **kwargs)
  File "/opt/gptqmodel/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/module_looper.py", line 1507, in _loop_impl
    run_layer_stage(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/stage_layer.py", line 574, in run_layer_stage
    subset_result = run_subset_stage(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/stage_subset.py", line 1261, in run_subset_stage
    processed_results, new_layer_inputs, _ = _run_single_subset_pass(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/stage_subset.py", line 965, in _run_single_subset_pass
    target_device = looper._prepare_named_module_for_quantization(
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/looper/module_looper.py", line 1101, in _prepare_named_module_for_quantization
    move_to(named_module.module, device=target_device)
  File "/host/data/wdd/GPTQModel-6.1.0/gptqmodel/utils/model.py", line 264, in move_to
    obj = obj.to(device=device, dtype=dtype, non_blocking=False)
  File "/opt/gptqmodel/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1371, in to
    return self._apply(convert)
  File "/opt/gptqmodel/lib/python3.10/site-packages/torch/nn/modules/module.py", line 957, in _apply
    param_applied = fn(param)
  File "/opt/gptqmodel/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1357, in convert
    return t.to(
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 86.00 MiB. GPU 1 has a total capacity of 39.56 GiB of which 34.81 MiB is free. Process 1738415 has 39.52 GiB memory in use. Of the allocated memory 37.10 GiB is allocated by PyTorch, and 1.35 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
```
my script

tokenizer = AutoTokenizer.from_pretrained(
        pretrained_model_id, 
        # use_fast=True,
        trust_remote_code=True  
    )
    
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
   
    traindataset = get_calibration_data(tokenizer, nsamples=164, seqlen=64)
    
    quantize_config = QuantizeConfig(
            bits=8,
            group_size=128,
            damp_percent=0.01,
            desc_act=True,
            offload_to_disk=False,
            act_group_aware=False,
            sym=True,
        )
    

    model = GPTQModel.load(pretrained_model_id, 
        quantize_config,
        device="cuda",
        trust_remote_code=True,
        dtype=torch.bfloat16
        )
   
    
    model.quantize(traindataset,batch_size=1,backend=BACKEND.TORCH)
    
my venv:
```py
Package                           Version       Editable project location
--------------------------------- ------------- -----------------------------------------
absl-py                           2.3.1
accelerate                        1.13.0
addict                            2.4.0
aihit                             0.3.1         /host/data/wdd/aihit0.3
aiohappyeyeballs                  2.6.1
aiohttp                           3.13.3
aiosignal                         1.4.0
annotated-doc                     0.0.4
annotated-types                   0.7.0
anthropic                         0.71.0
antlr4-python3-runtime            4.13.2
anyio                             4.12.1
apache-tvm-ffi                    0.1.7
astor                             0.8.1
async-timeout                     5.0.1
attrs                             25.4.0
autopep8                          2.3.2
blake3                            1.0.8
cachetools                        6.2.4
cbor2                             5.8.0
certifi                           2026.1.4
cffi                              2.0.0
chardet                           5.2.0
charset-normalizer                3.4.4
click                             8.3.1
cloudpickle                       3.1.2
colorama                          0.4.6
colorlog                          6.10.1
compressed-tensors                0.12.2
contourpy                         1.3.2
cryptography                      46.0.3
cuda-bindings                     13.1.1
cuda-pathfinder                   1.3.3
cuda-python                       13.1.1
cupy-cuda12x                      13.6.0
cycler                            0.12.1
DataProperty                      1.1.0
datasets                          3.6.0
Defuser                           0.0.20
depyf                             0.20.0
Device-SMI                        0.5.5
dill                              0.3.8
diskcache                         5.6.3
distro                            1.9.0
dnspython                         2.8.0
docstring_parser                  0.17.0
dotenv                            0.9.9
editdistance                      0.8.1
einops                            0.8.1
email-validator                   2.3.0
et_xmlfile                        2.0.0
evalscope                         0.0.0.dev0    /host/data/wdd/evalscope-main
evaluate                          0.4.6
exceptiongroup                    1.3.1
fast_hadamard_transform           1.0.4.post1
fastapi                           0.128.0
fastapi-cli                       0.0.20
fastapi-cloud-cli                 0.8.0
fastar                            0.8.0
fastrlock                         0.8.3
filelock                          3.20.2
flashinfer-python                 0.5.3
fonttools                         4.61.1
frozenlist                        1.8.0
fsspec                            2025.3.0
gguf                              0.17.1
GPTQModel                         6.1.0.dev0    /host/data/wdd/GPTQModel-6.1.0
h11                               0.16.0
hf_transfer                       0.1.9
hf-xet                            1.4.3
httpcore                          1.0.9
httptools                         0.7.1
httpx                             0.28.1
httpx-sse                         0.4.3
huggingface_hub                   1.11.0
idna                              3.11
ijson                             3.4.0.post0
iniconfig                         2.3.0
interegular                       0.3.3
jieba                             0.42.1
Jinja2                            3.1.6
jiter                             0.12.0
jmespath                          1.0.1
joblib                            1.5.3
jsonlines                         4.0.0
jsonschema                        4.26.0
jsonschema-specifications         2025.9.1
kiwisolver                        1.4.9
langdetect                        1.0.9
lark                              1.2.2
latex2sympy2_extended             1.10.2
llguidance                        1.3.0
llvmlite                          0.44.0
lm_eval                           0.4.10.dev0   /host/data/wdd/lm-evaluation-harness-main
lm-format-enforcer                0.11.3
LogBar                            0.4.3
loguru                            0.7.3
lxml                              6.0.2
markdown-it-py                    4.0.0
MarkupSafe                        3.0.3
matplotlib                        3.10.8
maturin                           1.11.2
mbstrdecoder                      1.1.4
mcp                               1.25.0
mdurl                             0.1.2
mistral_common                    1.8.8
model-hosting-container-standards 0.1.12
modelscope                        1.33.0
more-itertools                    10.8.0
mpmath                            1.3.0
msgpack                           1.1.2
msgspec                           0.20.0
multidict                         6.7.0
multiprocess                      0.70.16
networkx                          3.4.2
ninja                             1.13.0
nltk                              3.9.2
numba                             0.61.2
numexpr                           2.14.1
numpy                             2.2.6
nvidia-cublas-cu12                12.8.4.1
nvidia-cuda-cupti-cu12            12.8.90
nvidia-cuda-nvrtc-cu12            12.8.93
nvidia-cuda-runtime-cu12          12.8.90
nvidia-cudnn-cu12                 9.10.2.21
nvidia-cudnn-frontend             1.17.0
nvidia-cufft-cu12                 11.3.3.83
nvidia-cufile-cu12                1.13.1.3
nvidia-curand-cu12                10.3.9.90
nvidia-cusolver-cu12              11.7.3.90
nvidia-cusparse-cu12              12.5.8.93
nvidia-cusparselt-cu12            0.7.1
nvidia-cutlass-dsl                4.3.4
nvidia-ml-py                      13.590.44
nvidia-nccl-cu12                  2.27.5
nvidia-nvjitlink-cu12             12.8.93
nvidia-nvshmem-cu12               3.3.20
nvidia-nvtx-cu12                  12.8.90
openai                            2.14.0
openai-harmony                    0.0.8
opencv-python-headless            4.12.0.88
openpyxl                          3.1.5
outlines_core                     0.2.11
overrides                         7.7.0
packaging                         25.0
pandas                            2.3.3
partial-json-parser               0.2.1.1.post7
pathvalidate                      3.3.1
peft                              0.18.0
pillow                            12.1.0
pip                               22.0.2
pluggy                            1.6.0
portalocker                       3.2.0
prometheus_client                 0.23.1
prometheus-fastapi-instrumentator 7.1.0
propcache                         0.4.1
protobuf                          7.34.1
psutil                            7.2.1
py-cpuinfo                        9.0.0
pyarrow                           22.0.0
pybase64                          1.4.3
pybind11                          3.0.1
pycodestyle                       2.14.0
pycountry                         24.6.1
pycparser                         2.23
pydantic                          2.12.5
pydantic_core                     2.41.5
pydantic-extra-types              2.11.0
pydantic-settings                 2.12.0
Pygments                          2.19.2
PyJWT                             2.10.1
pylatexenc                        2.10
pyparsing                         3.3.1
PyPcre                            0.3.2
pytablewriter                     1.2.1
pytest                            8.4.2
python-dateutil                   2.9.0.post0
python-dotenv                     1.2.1
python-json-logger                4.0.0
python-multipart                  0.0.21
pytz                              2025.2
PyYAML                            6.0.3
pyzmq                             27.1.0
random_word                       1.0.13
ray                               2.53.0
referencing                       0.37.0
regex                             2025.11.3
requests                          2.32.5
rich                              14.2.0
rich-toolkit                      0.17.1
rignore                           0.7.6
rouge-chinese                     1.0.3
rouge-score                       0.1.2
rpds-py                           0.30.0
sacrebleu                         2.5.1
safetensors                       0.7.0
scikit-learn                      1.7.2
scipy                             1.15.3
seaborn                           0.13.2
sentencepiece                     0.2.1
sentry-sdk                        2.48.0
setproctitle                      1.3.7
setuptools                        80.9.0
shellingham                       1.5.4
simplejson                        3.20.2
six                               1.17.0
sniffio                           1.3.1
sortedcontainers                  2.4.0
sqlitedict                        2.1.0
sse-starlette                     3.1.2
starlette                         0.50.0
supervisor                        4.3.0
sympy                             1.14.0
tabledata                         1.3.4
tabulate                          0.9.0
tcolorpy                          0.1.7
tensorboardX                      2.6.4
threadpoolctl                     3.6.0
tiktoken                          0.12.0
TokeNicer                         0.0.13
tokenizers                        0.22.2
tomli                             2.3.0
torch                             2.9.0
torchao                           0.17.0
torchaudio                        2.9.0
torchvision                       0.24.0
tqdm                              4.67.1
tqdm-multiprocess                 0.0.11
transformers                      5.4.0
triton                            3.5.0
typepy                            1.3.4
typer                             0.21.1
typing_extensions                 4.15.0
typing-inspection                 0.4.2
tzdata                            2025.3
urllib3                           2.6.3
uvicorn                           0.40.0
uvloop                            0.22.1
watchfiles                        1.1.1
websockets                        15.0.1
wheel                             0.45.1
word2number                       1.1
xgrammar                          0.1.27
xxhash                            3.6.0
yarl                              1.22.0
zhconv                            1.4.3
zstandard                         0.25.0
```

can you help me? ths very much


## 评论 (4)

### Qubitium · 2026-04-23

@wangddcsu-ui  Fix is pending in PR #2808. Please test. 

### wangddcsu-ui · 2026-04-23

I modified the file gptqmodel/looper/awq_processor.py  gptqmodel/looper/stage_layer.py gptqmodel/models/base.py like PR 2808 shows.
but The problem still exists.

I try modified the QuantizeConfig like this:
quantize_config = QuantizeConfig(
            bits=8,
            group_size=128,
            damp_percent=0.01,
            desc_act=True,
            offload_to_disk=False,
            act_group_aware=False,
            sym=True,
            auto_forward_data_parallel=False,       # new add 
            gc_mode="on_stage_end",                 # new add
)


oom is not exist, but I have a new question .GLM-5.1 is too big ,I use 4 nv cards. but  all memory is in the 1th card


log shows:

WARN  GPTQ module 'mlp.experts.141.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.            
WARN  GPTQ module 'mlp.experts.141.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.              
WARN  GPTQ module 'mlp.experts.142.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.            
WARN  GPTQ module 'mlp.experts.142.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.              
WARN  GPTQ module 'mlp.experts.143.gate_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.            
WARN  GPTQ module 'mlp.experts.143.up_proj' fell back to CPU Hessian accumulation due to GPU OOM during batch processing.              
Quantizing self_attn.o_proj in layer             [3 of 3] ██████████████████████████████████████████████| 0:06:56 / 0:06:56 [4/4] 100.0%
Forward: Layer=`model.layers.3`, subset=4/7, batches=164 Forward rows 9/164 █▌░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:04:42 / 1:25:38 [9/164] 5.5%

mem
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A   3952325      C   python3                                   40366MiB |  # out of memory
|    1   N/A  N/A   3952325      C   python3                                     754MiB |
|    2   N/A  N/A   3952325      C   python3                                     734MiB |
|    3   N/A  N/A   3952325      C   python3                                     754MiB |

Can the quantitative process be distributed to 4 cards?



### wangddcsu-ui · 2026-04-23

<img width="1855" height="942" alt="Image" src="https://github.com/user-attachments/assets/6282b09f-bdf6-4083-b36a-2193bae84c11" />

To confirm that I've applied all the changes completely, I've attached a screenshot for your reference.

### Qubitium · 2026-04-23

@wangddcsu-ui  Please open an new issue. Your new issue is no longer relevant to this bug. You have changed models and the model is now MoE, not dense. 
