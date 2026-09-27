# [Issue #4491] [Bug] 使用lmdeploy在5090上cuda版本12.8，cuda toolkit同12.8

source: https://github.com/InternLM/lmdeploy/issues/4491
state: open | updated: 2026-04-07T06:29:34Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

The tokenizer you are loading from '/home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The tokenizer you are loading from '/home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The tokenizer you are loading from '/home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The tokenizer you are loading from '/home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[TM][WARNING] [TM] `max_context_token_num` is not set, default to 40960.
The tokenizer you are loading from '/home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
FlashAttention2 is not installed.
2026-04-03 16:27:57,872 - lmdeploy - WARNING - turbomind.py:246 - get 327 model params

Convert to turbomind format:   0%|          | 0/36 [00:00<?, ?it/s]
Convert to turbomind format:   3%|▎         | 1/36 [00:00<00:23,  1.51it/s]
Convert to turbomind format:  17%|█▋        | 6/36 [00:00<00:02, 10.00it/s]
Convert to turbomind format:  31%|███       | 11/36 [00:00<00:01, 17.76it/s]
Convert to turbomind format:  44%|████▍     | 16/36 [00:00<00:00, 24.59it/s]
Convert to turbomind format:  58%|█████▊    | 21/36 [00:01<00:00, 30.12it/s]
Convert to turbomind format:  72%|███████▏  | 26/36 [00:01<00:00, 33.81it/s]
Convert to turbomind format:  86%|████████▌ | 31/36 [00:01<00:00, 37.58it/s]
Convert to turbomind format: 100%|██████████| 36/36 [00:01<00:00, 40.56it/s]
                                                                            
[TM][WARNING] [SegMgr] prefix caching is disabled
[TM][FATAL] kernels/gemm/tuner/measurer.cu(83): Check failed: status == cudaSuccess no kernel image is available for execution on the device


### Reproduction

 CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server /home/lmz/limingze/models/OpenGVLab/InternVL3_5-4B --server-port 2004 --cache-max-entry-count 0.5 --tp 1 > /home/lmz/limingze/internvl3_8B_trained.log 2>&1 &

### Environment

```Shell
Package                   Version       Build
------------------------- ------------- -----
accelerate                1.13.0
addict                    2.4.0
aiohappyeyeballs          2.6.1
aiohttp                   3.13.5
aiosignal                 1.4.0
annotated-doc             0.0.4
annotated-types           0.7.0
anyio                     4.13.0
apache-tvm-ffi            0.1.9
async-timeout             5.0.1
attrs                     26.1.0
certifi                   2026.2.25
charset-normalizer        3.4.7
click                     8.3.1
cloudpickle               3.1.2
cuda-bindings             12.9.4
cuda-pathfinder           1.5.0
distro                    1.9.0
einops                    0.8.2
exceptiongroup            1.3.1
fastapi                   0.135.3
filelock                  3.25.2
fire                      0.7.1
fla-core                  0.4.2
flash-linear-attention    0.4.2
frozenlist                1.8.0
fsspec                    2026.3.0
h11                       0.16.0
hf-xet                    1.4.3
httpcore                  1.0.9
httpx                     0.28.1
huggingface_hub           1.8.0
idna                      3.11
Jinja2                    3.1.6
jiter                     0.13.0
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
lmdeploy                  0.12.2
markdown-it-py            4.0.0
MarkupSafe                3.0.3
mdurl                     0.1.2
ml_dtypes                 0.5.4
mmengine-lite             0.10.7
mpmath                    1.3.0
msgpack                   1.1.2
multidict                 6.7.1
networkx                  3.4.2
numpy                     2.2.6
nvidia-cublas-cu12        12.8.4.1
nvidia-cuda-cupti-cu12    12.8.90
nvidia-cuda-nvrtc-cu12    12.8.93
nvidia-cuda-runtime-cu12  12.8.90
nvidia-cudnn-cu12         9.10.2.21
nvidia-cufft-cu12         11.3.3.83
nvidia-cufile-cu12        1.13.1.3
nvidia-curand-cu12        10.3.9.90
nvidia-cusolver-cu12      11.7.3.90
nvidia-cusparse-cu12      12.5.8.93
nvidia-cusparselt-cu12    0.7.1
nvidia-ml-py              13.590.48
nvidia-nccl-cu12          2.27.5
nvidia-nvjitlink-cu12     12.8.93
nvidia-nvshmem-cu12       3.4.5
nvidia-nvtx-cu12          12.8.90
nvitop                    1.6.2
openai                    2.30.0
openai-harmony            0.0.8
opencv-python             4.13.0.92
packaging                 26.0
partial-json-parser       0.2.1.1.post7
peft                      0.14.0
pillow                    12.2.0
pip                       26.0.1
platformdirs              4.9.4
prometheus_client         0.24.1
propcache                 0.4.1
protobuf                  7.34.1
psutil                    7.2.2
pybase64                  1.4.3
pydantic                  2.12.5
pydantic_core             2.41.5
Pygments                  2.20.0
PyYAML                    6.0.3
pyzmq                     27.1.0
ray                       2.54.1
referencing               0.37.0
regex                     2026.3.32
requests                  2.33.1
rich                      14.3.3
rpds-py                   0.30.0
safetensors               0.7.0
sentencepiece             0.2.1
setuptools                82.0.1
shellingham               1.5.4
shortuuid                 1.0.13
sniffio                   1.3.1
starlette                 1.0.0
sympy                     1.14.0
termcolor                 3.3.0
tiktoken                  0.12.0
tilelang                  0.1.8
timm                      1.0.26
tokenizers                0.22.2
tomli                     2.4.1
torch                     2.10.0        3
torch_c_dlpack_ext        0.1.5
torchvision               0.25.0
tqdm                      4.67.3
transformers              5.5.0
triton                    3.6.0
typer                     0.24.1
typing_extensions         4.15.0
typing-inspection         0.4.2
urllib3                   2.6.3
uvicorn                   0.42.0
wheel                     0.46.3
xgrammar                  0.1.33
yapf                      0.43.0
yarl                      1.23.0
z3-solver                 4.15.4.0
```

### Error traceback

```Shell

```

## 评论 (1)

### lvhan028 · 2026-04-07

要使用 cu12.8 的 whl 包，在这里取吧：
https://github.com/InternLM/lmdeploy/releases/tag/v0.12.2
