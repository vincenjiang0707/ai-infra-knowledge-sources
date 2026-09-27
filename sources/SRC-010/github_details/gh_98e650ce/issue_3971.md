# [Issue #3971] 在jetson orin  16G上，无法运行turbomind格式的模型，使用torch可以

source: https://github.com/InternLM/lmdeploy/issues/3971
state: closed | updated: 2026-03-26T07:05:21Z
labels: awaiting response, Stale

## 正文

报错显示内存不足

(py10) admin@admin:~/Qwen2.5-VL$ lmdeploy chat ./Qwen2.5-VL-3B-Instruct-AWQ/ --model-format awq
/home/admin/miniforge3/envs/py10/lib/python3.10/site-packages/torch/cuda/__init__.py:56: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you.
  import pynvml  # type: ignore[import]
chat_template_config:
ChatTemplateConfig(model_name='qwen2d5-vl', system=None, meta_instruction=None, eosys=None, user=None, eoh=None, assistant=None, eoa=None, tool=None, eotool=None, separator=None, capability='chat', stop_words=None)
engine_cfg:
TurbomindEngineConfig(dtype='auto', model_format='awq', tp=1, dp=1, device_num=None, attn_tp_size=None, attn_dp_size=None, mlp_tp_size=None, mlp_dp_size=None, outer_dp_size=None, session_len=128000, max_batch_size=1, cache_max_entry_count=0.8, cache_chunk_size=-1, cache_block_seq_len=64, enable_prefix_caching=False, quant_policy=0, rope_scaling_factor=0.0, use_logn_attn=False, download_dir=None, revision=None, max_prefill_token_num=8192, num_tokens_per_iter=0, max_prefill_iters=1, devices=None, empty_init=False, communicator='nccl', hf_overrides=None)
[TM][ERROR] CUDA runtime error: out of memory /opt/lmdeploy/src/turbomind/core/allocator.cc:49
Aborted (core dumped)


环境和版本如下
(py10) admin@admin:~/Qwen2.5-VL$ pip list
Package                   Version
------------------------- ----------------
accelerate                1.10.1
addict                    2.4.0
annotated-types           0.7.0
anyio                     4.10.0
attrs                     25.3.0
av                        15.1.0
blinker                   1.9.0
certifi                   2025.8.3
charset-normalizer        3.4.3
click                     8.2.1
cloudpickle               3.1.1
diskcache                 5.6.3
distro                    1.9.0
einops                    0.8.1
exceptiongroup            1.3.0
fastapi                   0.116.1
filelock                  3.19.1
fire                      0.7.1
Flask                     3.1.2
fsspec                    2025.9.0
genson                    1.3.0
gunicorn                  23.0.0
h11                       0.16.0
hf-xet                    1.1.10
httpcore                  1.0.9
httpx                     0.28.1
huggingface-hub           0.34.4
idna                      3.10
itsdangerous              2.2.0
Jinja2                    3.1.6
jiter                     0.10.0
jsonpath-ng               1.7.0
jsonschema                4.25.1
jsonschema-specifications 2025.9.1
lmdeploy                  0.9.2+cu126
markdown-it-py            4.0.0
MarkupSafe                3.0.2
mdurl                     0.1.2
mmengine-lite             0.10.7
mpmath                    1.3.0
msgpack                   1.1.1
networkx                  3.4.2
numpy                     1.26.4
nvidia-cublas-cu12        12.9.1.4
nvidia-cuda-runtime-cu12  12.9.79
nvidia-curand-cu12        10.3.10.19
nvidia-ml-py              13.580.82
nvidia-nccl-cu12          2.28.3
openai                    1.107.2
outlines                  1.2.4
outlines_core             0.2.11
packaging                 25.0
partial-json-parser       0.2.1.1.post6
peft                      0.14.0
pillow                    11.3.0
pip                       25.2
platformdirs              4.4.0
ply                       3.11
protobuf                  6.32.1
psutil                    7.0.0
pydantic                  2.11.9
pydantic_core             2.33.2
Pygments                  2.19.2
pynvml                    13.0.1
PyYAML                    6.0.2
pyzmq                     27.1.0
qwen-vl-utils             0.0.11
ray                       2.49.1
referencing               0.36.2
regex                     2025.9.1
requests                  2.32.5
rich                      14.1.0
rpds-py                   0.27.1
safetensors               0.6.2
sentencepiece             0.2.1
setuptools                80.9.0
shortuuid                 1.0.13
sniffio                   1.3.1
starlette                 0.47.3
sympy                     1.14.0
termcolor                 3.1.0
tiktoken                  0.11.0
timm                      1.0.19
tokenizers                0.22.0
tomli                     2.2.1
torch                     2.3.0
torchvision               0.18.0a0+6043bc2
tqdm                      4.67.1
transformers              4.56.1
typing_extensions         4.15.0
typing-inspection         0.4.1
urllib3                   2.5.0
uvicorn                   0.35.0
Werkzeug                  3.1.3
wheel                     0.45.1
yapf                      0.43.0


LMdeploy-jetson社区很久没有维护了，是不是最新版的lmdeploy在支持turbomind上有点问题？

## 评论 (0)
