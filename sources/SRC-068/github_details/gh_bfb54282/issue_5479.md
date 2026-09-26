# [Issue #5479] [Bug ]err in compilation code about "Unknown option --compress-mode=size " when using FlashInfer version 0.6.18, which is automatically downloaded by vLLM 0.29.0.

source: https://github.com/flashinfer-ai/flashinfer/issues/5479
state: open | updated: 2026-09-23T15:02:53Z
labels: bug, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and did not find a solution or an existing report.

### Environment

```text
==== FlashInfer ====
flashinfer                   : 0.6.18
flashinfer commit            : 69ff11fc4954396d98326656dc85debd2223f637
flashinfer file              : /home/xxx/test/.venv/lib/python3.12/site-packages/flashinfer/__init__.py
flashinfer-cubin             : not installed
flashinfer-jit-cache         : not installed
JIT cache                    : /home/xxx/.cache/flashinfer (1 compiled .so)
Cubin store (local)          : /home/xxx/.cache/flashinfer/cubins (0 cubins, 0 MiB)
Target CUDA archs (resolved) : {(8, '6')}

==== Python / Platform ====
Python            : 3.12.14 (main, Sep  1 2026, 14:16:52) [Clang 22.1.3 ]
Python executable : /home/xxx/test/.venv/bin/python
Virtual env       : /home/xxx/test/.venv
Platform          : Linux-6.5.0-18-generic-x86_64-with-glibc2.35
libc              : glibc 2.35
OS                : Ubuntu 22.04.4 LTS
Container         : no / not detected

==== GPU / Driver ====
Driver version       : 595.91.07
CUDA_VISIBLE_DEVICES : <unset>
GPU 0 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 1 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 2 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 3 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 4 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 5 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 6 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB
GPU 7 (CUDA order)   : NVIDIA RTX A6000 | SM86 | 84 SMs | 47.4 GiB

==== CUDA Toolkit ====
nvcc on PATH                            : not found
CUDA_HOME (env)                         : <unset>
CUDA toolkit resolved by flashinfer JIT : /usr/local/cuda (version 12.1)

==== PyTorch ====
torch                          : 2.13.0+cu130
torch.version.cuda             : 13.0
torch CXX11 ABI                : True
torch compiled archs           : sm_75 sm_80 sm_86 sm_90 sm_100 sm_120
torch.backends.cudnn.version() : 92000
torch file                     : /home/xxx/test/.venv/lib/python3.12/site-packages/torch/__init__.py

==== Relevant Packages ====
apache-tvm-ffi               : 0.1.11
cuda-bindings                : 13.4.2
cuda-core                    : 1.2.0
cuda-pathfinder              : 1.8.2
cuda-python                  : 13.4.1
cuda-tile                    : 1.6.0
cuda-toolkit                 : 13.0.3.0
flashinfer-python            : 0.6.18
ninja                        : 1.13.2
numpy                        : 2.3.5
nvidia-cublas                : 13.1.1.3
nvidia-cuda-cccl             : 13.3.4.3.1
nvidia-cuda-crt              : 13.4.92
nvidia-cuda-cupti            : 13.0.85
nvidia-cuda-nvcc             : 13.4.92
nvidia-cuda-nvdisasm         : 13.4.92
nvidia-cuda-nvrtc            : 13.0.88
nvidia-cuda-runtime          : 13.0.96
nvidia-cudnn-cu13            : 9.20.0.48
nvidia-cudnn-frontend        : 1.29.0
nvidia-cufft                 : 12.0.0.61
nvidia-cufile                : 1.15.1.6
nvidia-curand                : 10.4.0.35
nvidia-cusolver              : 12.0.4.66
nvidia-cusparse              : 12.6.3.3
nvidia-cusparselt-cu13       : 0.8.1
nvidia-cutlass-dsl           : 4.6.2
nvidia-cutlass-dsl-libs-base : 4.6.2
nvidia-cutlass-dsl-libs-core : 4.6.2
nvidia-cutlass-dsl-libs-cu12 : 4.6.2
nvidia-cutlass-dsl-libs-cu13 : 4.6.2
nvidia-ml-py                 : 13.610.43
nvidia-nccl-cu13             : 2.29.7
nvidia-nvjitlink             : 13.4.92
nvidia-nvshmem-cu13          : 3.4.5
nvidia-nvtx                  : 13.0.85
nvidia-nvvm                  : 13.4.92
torch                        : 2.13.0+cu130
torch-c-dlpack-ext           : 0.1.5
torchaudio                   : 2.11.0+cu130
torchcodec                   : 0.16.0+cu130
torchvision                  : 0.28.0+cu130
transformers                 : 5.17.0
triton                       : 3.7.1
vllm                         : 0.29.0  (declares flashinfer-python==0.6.18)
```

### Bug description

When attempting to launch Qwen3 series models (Qwen3-8B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B) using the `vllm serve` command within a fresh uv Python environment—following the instructions in the official documentation's "Quickstart" section—the service failed to start due to an error (as shown in the image below): the automatically installed flashinfer 0.6.18 failed to correctly compile code for certain CUDA kernels.
installed instruction:
```
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
```
vllm serve instruction:
```
vllm serve  /data/models/Qwen3.5-35B-A3B \
  --served-model-name Qwen3.5-35B-A3B \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 4 \
  --gpu-memory-utilization 0.8 \
  --max-model-len 16384 \
  --max-num-seqs 64 \
  --enable-prefix-caching \
  --enable-expert-parallel \
  --reasoning-parser qwen3 \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}' 
```
showing error:
> nvcc fatal : Unknown option '--compress-mode=size'


### Minimal reproduction

```python
The latest stable version of vLLM is currently 0.29.0; using version 0.28.0 or 0.30.0 might not allow for reproduction, so you need to specifically download version 0.29.0.

uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
```

### Error messages / logs

```text
like this:

(EngineCore pid=3164713) ERROR 09-23 10:35:19 [core.py:1374] RuntimeError: Ninja build failed. Ninja output:
(EngineCore pid=3164713) ERROR 09-23 10:35:19 [core.py:1374] ninja: Entering directory `/home/xxx/.cache/flashinfer/0.6.18/86/cached_ops/sampling'

FAILED: [code=1] /home/xxx/.cache/flashinfer/0.6.18/86/cached_ops/sampling/csrc_renorm.cuda.o
            (EngineCore pid=3164713) ERROR 09-23 10:35:19 [core.py:1374]  /usr/local/cuda/bin/nvcc --generate-dependencies-with-compile -MF /home/xxx/.cache/flashinfer/0.6.18/86/cached_ops/sampling/csrc_renorm.cuda.o.d -DPy_LIMITED_API=0x03090000 -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/cccl/cub -I/home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/cccl/libcudacxx/include -I/home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/cccl/thrust -isystem /home/xxx/.local/share/uv/python/cpython-3.12.14-linux-x86_64-gnu/include/python3.12 -isystem /usr/local/cuda/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/tvm_ffi/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/tvm_ffi/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/csrc -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/cutlass/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/cutlass/tools/util/include -isystem /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/spdlog/include --compiler-options=-fPIC --expt-relaxed-constexpr -gencode=arch=compute_86,code=sm_86 -DFLASHINFER_ENABLE_FP8_E8M0 -DFLASHINFER_ENABLE_FP4_E2M1 -std=c++17 --threads=1 -use_fast_math -Xfatbin=-compress-all --compress-mode=size -DFLASHINFER_ENABLE_F16 -DFLASHINFER_ENABLE_BF16 -DFLASHINFER_ENABLE_FP8_E4M3 -DFLASHINFER_ENABLE_FP8_E5M2 -DNDEBUG -O3 -c /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/data/csrc/renorm.cu -o /home/xxx/.cache/flashinfer/0.6.18/86/cached_ops/sampling/csrc_renorm.cuda.o

(EngineCore pid=3164713) nvcc fatal   : Unknown option '--compress-mode=size'
(EngineCore pid=3164713) ninja: build stopped: subcommand failed.
(EngineCore pid=3164713)
```

### Additional context

When I install vLLM 0.28.0, the imported flashinfer is as follows:
```
==== FlashInfer ====
flashinfer                   : 0.6.16.post3
flashinfer commit            : ?: AttributeError: module 'flashinfer' has no attribute '__git_commit__'
flashinfer file              : /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/flashinfer/__init__.py
flashinfer-cubin             : not installed
flashinfer-jit-cache         : not installed
JIT cache                    : /home/xxx/.cache/flashinfer (1 compiled .so)
Cubin store (local)          : /home/xxx/.cache/flashinfer/cubins (0 cubins, 0 MiB)
Target CUDA archs (resolved) : {(8, '6')}

==== CUDA Toolkit ====
nvcc on PATH                            : not found
CUDA_HOME (env)                         : <unset>
CUDA toolkit resolved by flashinfer JIT : /usr/local/cuda (version 12.1)

==== PyTorch ====
torch                          : 2.13.0+cu132
torch.version.cuda             : 13.2
torch CXX11 ABI                : True
torch compiled archs           : sm_75 sm_80 sm_86 sm_90 sm_100 sm_120
torch.backends.cudnn.version() : 92000
torch file                     : /home/xxx/xxxenv/.venv/lib/python3.12/site-packages/torch/__init__.py
```
At this point, the vllm serve service can start up normally.

## 评论 (2)

### apex-mochen · 2026-09-23

!claim

### flashinfer-bot · 2026-09-23

Issue assigned to @apex-mochen.
