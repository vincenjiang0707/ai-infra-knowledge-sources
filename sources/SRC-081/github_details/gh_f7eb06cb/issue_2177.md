# [Issue #2177] [BUG] Quant Qwen3-Next-80B-A3B-Instruction takes a long time

source: https://github.com/ModelCloud/GPTQModel/issues/2177
state: closed | updated: 2025-12-21T11:39:09Z
labels: bug

## 正文

**Describe the bug**
Quant Qwen3-Next-80B-A3B-Instruction takes a long time
Quantification requires more than 1 day of time，I only used one GPU，
1 Should this 80B model adopt multi GPU quantization？How much VRAM should be used to quantify this 80B model？
2 My GPU is H20 with 96GB of VRAM, but 60GB of VRAM is occupied and only 30GB of VRAM is available for quantization. Is this the reason for slow quantization

gptqmodel==5.0.0

<img width="2510" height="980" alt="Image" src="https://github.com/user-attachments/assets/64385341-6459-41d5-90d4-fcfa18983f5b" />

**GPU Info**

Show output of:

```
nvidia-smi
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (4)

### leipan797 · 2025-11-06

I encountered the same condition under GPTQModel == 4.2.0, but i cannot quantize Qwen3-Next in GPTQModel == 5.2.0, could you please share your python environment? 

### xiaotianns · 2025-11-06

> I encountered the same condition under GPTQModel == 4.2.0, but i cannot quantize Qwen3-Next in GPTQModel == 5.2.0, could you please share your python environment?

sure


> accelerate                               1.10.1
aiofiles                                 24.1.0
aiohappyeyeballs                         2.6.1
aiohttp                                  3.12.15
aiosignal                                1.4.0
airportsdata                             20250811
annotated-types                          0.7.0
antlr4-python3-runtime                   4.9.3
anyio                                    4.10.0
astor                                    0.8.1
asttokens                                3.0.0
async-timeout                            5.0.1
attrs                                    25.3.0
audioread                                3.0.1
autopep8                                 2.3.2
av                                       14.2.0
bitsandbytes                             0.48.0.dev0
blake3                                   1.0.5
cachetools                               6.1.0
cbor2                                    5.7.0
certifi                                  2025.8.3
cffi                                     1.17.1
charset-normalizer                       3.4.3
click                                    8.2.1
cloudpickle                              3.1.1
comm                                     0.2.3
compressed-tensors                       0.11.0
contourpy                                1.3.2
cupy-cuda12x                             13.5.1
cut-cross-entropy                        25.1.1
cycler                                   0.12.1
datasets                                 3.6.0
debugpy                                  1.8.17
decorator                                5.2.1
deepspeed                                0.16.4
Deprecated                               1.2.18
depyf                                    0.19.0
Device-SMI                               0.5.1
diffusers                                0.35.1
dill                                     0.3.8
diskcache                                5.6.3
distro                                   1.9.0
dnspython                                2.7.0
docstring_parser                         0.17.0
einops                                   0.8.1
email_validator                          2.2.0
et_xmlfile                               2.0.0
exceptiongroup                           1.3.0
executing                                2.2.1
fastapi                                  0.116.1
fastapi-cli                              0.0.8
fastapi-cloud-cli                        0.1.5
fastrlock                                0.8.3
ffmpeg                                   1.4
ffmpy                                    0.6.1
filelock                                 3.18.0
fire                                     0.7.0
flash_attn                               2.8.1
fonttools                                4.59.0
frozendict                               2.4.6
frozenlist                               1.7.0
fsspec                                   2025.3.0
gekko                                    1.3.0
gguf                                     0.17.1
googleapis-common-protos                 1.70.0
GPTQModel                                5.0.0+cu128torch2.8
gradio                                   5.31.0
gradio_client                            1.10.1
groovy                                   0.1.2
grpcio                                   1.74.0
h11                                      0.16.0
hf_transfer                              0.1.9
hf-xet                                   1.1.7
hjson                                    3.1.0
httpcore                                 1.0.9
httptools                                0.6.4
httpx                                    0.28.1
huggingface-hub                          0.34.4
idna                                     3.10
importlib_metadata                       8.0.0
iniconfig                                2.1.0
interegular                              0.3.3
ipykernel                                7.0.1
ipython                                  8.37.0
jedi                                     0.19.2
jieba                                    0.42.1
Jinja2                                   3.1.6
jiter                                    0.10.0
joblib                                   1.5.1
jsonschema                               4.25.0
jsonschema-specifications                2025.4.1
jupyter_client                           8.6.3
jupyter_core                             5.9.1
kiwisolver                               1.4.9
lark                                     1.2.2
lazy_loader                              0.4
librosa                                  0.11.0
llamafactory                             0.9.4.dev0          
llguidance                               0.7.30
llvmlite                                 0.44.0
lm-format-enforcer                       0.11.3
LogBar                                   0.1.8
markdown-it-py                           3.0.0
MarkupSafe                               3.0.2
matplotlib                               3.10.5
matplotlib-inline                        0.1.7
maturin                                  1.9.4
mdurl                                    0.1.2
mistral_common                           1.8.3
modelscope                               1.28.2
mpmath                                   1.3.0
msgpack                                  1.1.1
msgspec                                  0.19.0
multidict                                6.6.3
multiprocess                             0.70.16
nest_asyncio                             1.6.0
networkx                                 3.4.2
ninja                                    1.13.0
nltk                                     3.9.1
numba                                    0.61.2
numpy                                    2.2.6
nvidia-cublas-cu12                       12.8.4.1
nvidia-cuda-cupti-cu12                   12.8.90
nvidia-cuda-nvrtc-cu12                   12.8.93
nvidia-cuda-runtime-cu12                 12.8.90
nvidia-cudnn-cu12                        9.10.2.21
nvidia-cufft-cu12                        11.3.3.83
nvidia-cufile-cu12                       1.13.1.3
nvidia-curand-cu12                       10.3.9.90
nvidia-cusolver-cu12                     11.7.3.90
nvidia-cusparse-cu12                     12.5.8.93
nvidia-cusparselt-cu12                   0.7.1
nvidia-ml-py                             13.580.65
nvidia-nccl-cu12                         2.27.3
nvidia-nvjitlink-cu12                    12.8.93
nvidia-nvtx-cu12                         12.8.90
omegaconf                                2.3.0
openai                                   1.99.9
openai-harmony                           0.0.4
opencv-python-headless                   4.12.0.88
openpyxl                                 3.1.5
opentelemetry-api                        1.26.0
opentelemetry-exporter-otlp              1.26.0
opentelemetry-exporter-otlp-proto-common 1.26.0
opentelemetry-exporter-otlp-proto-grpc   1.26.0
opentelemetry-exporter-otlp-proto-http   1.26.0
opentelemetry-proto                      1.26.0
opentelemetry-sdk                        1.26.0
opentelemetry-semantic-conventions       0.47b0
opentelemetry-semantic-conventions-ai    0.4.12
optimum                                  1.27.0
orjson                                   3.11.1
outlines                                 0.1.11
outlines_core                            0.2.11
packaging                                25.0
pandas                                   2.3.1
parso                                    0.8.5
partial-json-parser                      0.2.1.1.post6
peft                                     0.15.2
pexpect                                  4.9.0
pickleshare                              0.7.5
pillow                                   11.3.0
pip                                      25.1
platformdirs                             4.3.8
pluggy                                   1.6.0
pooch                                    1.8.2
prometheus_client                        0.22.1
prometheus-fastapi-instrumentator        7.1.0
prompt_toolkit                           3.0.52
propcache                                0.3.2
protobuf                                 6.32.0
psutil                                   7.0.0
ptyprocess                               0.7.0
pure_eval                                0.2.3
py-cpuinfo                               9.0.0
py-spy                                   0.4.1
pyarrow                                  21.0.0
pybase64                                 1.4.2
pycodestyle                              2.14.0
pycountry                                24.6.1
pycparser                                2.22
pydantic                                 2.11.7
pydantic_core                            2.33.2
pydantic-extra-types                     2.10.5
pydub                                    0.25.1
Pygments                                 2.19.2
pyparsing                                3.2.3
pytest                                   8.4.1
python-dateutil                          2.9.0.post0
python-dotenv                            1.1.1
python-json-logger                       3.3.0
python-multipart                         0.0.20
pytz                                     2025.2
PyYAML                                   6.0.2
pyzmq                                    27.0.2
random_word                              1.0.13
ray                                      2.48.0
referencing                              0.36.2
regex                                    2025.7.34
requests                                 2.32.4
rich                                     14.1.0
rich-toolkit                             0.15.0
rignore                                  0.6.4
rouge                                    1.0.1
rouge-chinese                            1.0.3
rpds-py                                  0.27.0
ruff                                     0.12.8
safehttpx                                0.1.6
safetensors                              0.6.2
scikit-learn                             1.7.1
scipy                                    1.15.3
semantic-version                         2.10.0
sentence-transformers                    5.1.0
sentencepiece                            0.2.0
sentry-sdk                               2.34.1
setproctitle                             1.3.6
setuptools                               78.1.1
shellingham                              1.5.4
shtab                                    1.7.2
six                                      1.17.0
sniffio                                  1.3.1
some-package                             0.1
soundfile                                0.13.1
soxr                                     0.5.0.post1
sse-starlette                            3.0.2
stack_data                               0.6.3
starlette                                0.47.2
sympy                                    1.14.0
termcolor                                3.1.0
threadpoolctl                            3.6.0
tiktoken                                 0.11.0
tokenicer                                0.0.5
tokenizers                               0.22.0
tomli                                    2.2.1
tomlkit                                  0.13.3
torch                                    2.8.0
torchao                                  0.14.1
torchaudio                               2.8.0
torchvision                              0.23.0
tornado                                  6.5.2
tqdm                                     4.67.1
traitlets                                5.14.3
transformers                             4.57.1
transformers-v4.55.0-GLM-4.5V-preview    4.56.0.dev0
triton                                   3.4.0
trl                                      0.9.6
typer                                    0.16.0
typing_extensions                        4.14.1
typing-inspection                        0.4.1
tyro                                     0.8.14
tzdata                                   2025.2
unsloth                                  2025.8.9
unsloth_zoo                              2025.8.8
urllib3                                  2.5.0
uvicorn                                  0.35.0
uvloop                                   0.21.0
vllm                                     0.10.2
watchfiles                               1.1.0
wcwidth                                  0.2.14
websockets                               15.0.1
wheel                                    0.45.1
wrapt                                    1.17.3
xformers                                 0.0.32.post1
xgrammar                                 0.1.23
xxhash                                   3.5.0
yarl                                     1.20.1
zipp                                     3.23.0
zstandard                                0.25.0

### Qubitium · 2025-11-07

@xiaotianns  I need more logs. Screenshot with more logs. 

More importantly, we do support multiple gpu accelerated quantizstion for MoE models. But you need to make sure you have the following:

1. More than 1 gpu
2. installed Python 3.14 or 3.13t and running with `PYTHON_GIL=0` so gil is disabled for max thread performance. 
3. You should see 2x-4x your quant speed this way with large MoE as we will use all gpus. 

Make sure you install gptqmodel from `main` branch as well. 

### Qubitium · 2025-11-14

Quantization duplicate fwd bug/regression was just fixed on `main` that should speed up quantization of larger models. 
