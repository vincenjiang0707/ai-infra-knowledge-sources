# [Issue #98] ImportError: cannot import name 'is_flash_attn_available' from 'transformers.utils'

source: https://github.com/FasterDecoding/Medusa/issues/98
state: open | updated: 2025-03-11T09:10:33Z
labels: 

## 正文

I got a error when I refer to https://github.com/FasterDecoding/Medusa to prepare to run the Demo .

1. The basic environment was successfully installed without any errors.
```
git clone https://github.com/FasterDecoding/Medusa.git
cd Medusa
pip install -e .
```

2. Run `python -m medusa.inference.cli` and get an error
```
❯ python -m medusa.inference.cli --model FasterDecoding/medusa-1.0-vicuna-13b-v1.5
^[[ATraceback (most recent call last):
  File "/usr/local/anaconda3/envs/medusa/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/anaconda3/envs/medusa/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/lab/Medusa/medusa/inference/cli.py", line 24, in <module>
    from medusa.model.medusa_model import MedusaModel
  File "/data/lab/Medusa/medusa/model/medusa_model.py", line 3, in <module>
    from .modeling_llama_kv import LlamaForCausalLM as KVLlamaForCausalLM
  File "/data/lab/Medusa/medusa/model/modeling_llama_kv.py", line 22, in <module>
    from transformers.utils import (
ImportError: cannot import name 'is_flash_attn_available' from 'transformers.utils' (/medusa/lib/python3.10/site-packages/transformers/utils/__init__.py)
```
     


3. environment
```
❯ uname -a
Linux i-zigfc13j 5.15.0-43-generic #46-Ubuntu SMP Tue Jul 12 10:30:17 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
❯ python -V
Python 3.10.14
❯ pip list
Package                  Version     Editable project location
------------------------ ----------- -------------------------
accelerate               0.29.2
aiohttp                  3.9.4
aiosignal                1.3.1
annotated-types          0.6.0
anyio                    4.3.0
asttokens                2.0.5
async-timeout            4.0.3
attrs                    23.2.0
certifi                  2024.2.2
charset-normalizer       3.3.2
click                    8.1.7
comm                     0.2.1
debugpy                  1.6.7
decorator                5.1.1
exceptiongroup           1.2.0
executing                0.8.3
fastapi                  0.110.1
filelock                 3.13.4
frozenlist               1.4.1
fschat                   0.2.36
fsspec                   2024.3.1
h11                      0.14.0
httpcore                 1.0.5
httpx                    0.27.0
huggingface-hub          0.22.2
idna                     3.7
ipykernel                6.28.0
ipython                  8.20.0
jedi                     0.18.1
Jinja2                   3.1.3
jupyter_client           8.6.0
jupyter_core             5.5.0
markdown-it-py           3.0.0
markdown2                2.4.13
MarkupSafe               2.1.5
matplotlib-inline        0.1.6
mdurl                    0.1.2
medusa-llm               1.0         /data/lab/Medusa
mpmath                   1.3.0
multidict                6.0.5
nest-asyncio             1.6.0
networkx                 3.3
nh3                      0.2.17
numpy                    1.26.4
nvidia-cublas-cu12       12.1.3.1
nvidia-cuda-cupti-cu12   12.1.105
nvidia-cuda-nvrtc-cu12   12.1.105
nvidia-cuda-runtime-cu12 12.1.105
nvidia-cudnn-cu12        8.9.2.26
nvidia-cufft-cu12        11.0.2.54
nvidia-curand-cu12       10.3.2.106
nvidia-cusolver-cu12     11.4.5.107
nvidia-cusparse-cu12     12.1.0.106
nvidia-nccl-cu12         2.19.3
nvidia-nvjitlink-cu12    12.4.127
nvidia-nvtx-cu12         12.1.105
packaging                23.2
parso                    0.8.3
pexpect                  4.8.0
pip                      23.3.1
platformdirs             3.10.0
prompt-toolkit           3.0.43
protobuf                 5.26.1
psutil                   5.9.0
ptyprocess               0.7.0
pure-eval                0.2.2
pydantic                 2.7.0
pydantic_core            2.18.1
Pygments                 2.15.1
python-dateutil          2.8.2
PyYAML                   6.0.1
pyzmq                    25.1.2
regex                    2023.12.25
requests                 2.31.0
rich                     13.7.1
safetensors              0.4.2
sentencepiece            0.2.0
setuptools               68.2.2
shortuuid                1.0.13
six                      1.16.0
sniffio                  1.3.1
stack-data               0.2.0
starlette                0.37.2
svgwrite                 1.4.3
sympy                    1.12
tiktoken                 0.6.0
tokenizers               0.15.2
torch                    2.2.2
tornado                  6.3.3
tqdm                     4.66.2
traitlets                5.7.1
transformers             4.39.3
triton                   2.2.0
typing_extensions        4.11.0
urllib3                  2.2.1
uvicorn                  0.29.0
wavedrom                 2.0.3.post3
wcwidth                  0.2.5
wheel                    0.41.2
yarl                     1.9.4
```

## 评论 (3)

### imneov · 2024-04-12

I found the [issue](https://github.com/huggingface/transformers/issues/27319) is talking about this error.

There were two ways to fix it:

1. Use the 4.34.1 version of Transformers.
```
# Install the specific version using pip
pip install transformers==4.34.1
```

2.Replace s_flash_attn_available() with is_flash_attn_2_available(), but I  don't sure if this will cause problems.


### huangzl19 · 2024-09-21

I also encounterd the same issue.

### nanxue2023 · 2025-03-11

> Replace s_flash_attn_available() with is_flash_attn_2_available()

this solution is okay for me so far
