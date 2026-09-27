# [Issue #1218] please provide python whel package in nvidia jetson agx orin (aarch64 + cuda)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1218
state: open | updated: 2026-05-04T16:22:28Z
labels: Cross Platform, aarch64

## 正文

### Feature request

please provide python whel package in nvidia jetson agx orin (aarch64 + cuda)

### Motivation

please provide python whel package in nvidia jetson agx orin (aarch64 + cuda)

### Your contribution

please provide python whel package in nvidia jetson agx orin (aarch64 + cuda)

## 评论 (4)

### WangFengtu1996 · 2024-05-24

version 0.43.1

### KungFuPandaPro · 2024-09-24

seems that do not support aarch64 

### shubhamgupto · 2025-01-27

Hey any updates on this?
Im runing jetson orin nano with CUDA 12.4 

currently can install only version `0.42.0` which results in this
```
python -m bitsandbytes
False

===================================BUG REPORT===================================
/xxxxxxxxxxxxxx/miniconda3/envs/minicpm/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: Welcome to bitsandbytes. For bug reports, please run

python -m bitsandbytes


  warn(msg)
================================================================================
/xxxxxxxxxxxxxx/miniconda3/envs/minicpm/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: /xxxxxxxxxxxxxx/miniconda3/envs/minicpm did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
/home/rivet01/miniconda3/envs/minicpm/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: /usr/local/cuda-12.4/lib64:/usr/local/cuda-12.4/lib64:/usr/local/cuda-12.4/lib64:/usr/local/cuda-12.4/lib64:/usr/local/cuda-12.4/lib64: did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
The following directories listed in your path were found to be non-existent: {PosixPath('local/ubuntu'), PosixPath('@/tmp/.ICE-unix/2522,unix/ubuntu')}
The following directories listed in your path were found to be non-existent: {PosixPath('/etc/xdg/xdg-ubuntu')}
The following directories listed in your path were found to be non-existent: {PosixPath('1'), PosixPath('0')}
The following directories listed in your path were found to be non-existent: {PosixPath('/org/gnome/Terminal/screen/5c11be7d_873d_4dd0_87b2_1d2f56aedfc9')}
The following directories listed in your path were found to be non-existent: {PosixPath('path=/run/user/1000/bus,guid=31fede2ecb96f8ad387a6ac90000003a'), PosixPath('unix')}
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching in backup paths...
DEBUG: Possible options found for libcudart.so: {PosixPath('/usr/local/cuda/lib64/libcudart.so')}
CUDA SETUP: PyTorch settings found: CUDA_VERSION=124, Highest Compute Capability: 8.7.
CUDA SETUP: To manually override the PyTorch CUDA version please see:https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
CUDA SETUP: Required library version not found: libbitsandbytes_cuda124.so. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. You need to manually override the PyTorch CUDA version. Please see: "https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
2. CUDA driver not installed
3. CUDA not installed
4. You have multiple conflicting CUDA libraries
5. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Something unexpected happened. Please compile from source:
git clone https://github.com/TimDettmers/bitsandbytes.git
cd bitsandbytes
CUDA_VERSION=124
python setup.py install
CUDA SETUP: Setup Failed!

```

### neil-the-nowledgeable · 2026-05-04

FWIW, I've been running bnb 0.46.1 source-built for sm_87 (Jetson Orin Nano Super, JetPack 6.2, CUDA 12.6) at scale and it is working reliably.  Sharing this for others in absence of prebuilt wheel

Here's what I got working (Jetson Orin Nano Super, sm_87 — SHA 4bca844 on 0.46.1):

  git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
  cd bitsandbytes && git checkout 0.46.1
  cmake -DCOMPUTE_BACKEND=cuda -DCOMPUTE_CAPABILITY=87 -S .
  make -j4   # MAX_JOBS=6 OOMs on 8 GB Nano; 4 is the empirical max
  pip install .

The key param is -DCOMPUTE_CAPABILITY=87 — without it, build  sm_87  is skipped and likely your kernels silently fall back to CPU. AGX Orin is also sm_87, so the same recipe should apply, but I didnt test it. ( my understanding is the compute capability is what matters for kernel selection).

  Validated workloads at this build (Jetson Orin Nano Super 8 GB):
  - Single-device QLoRA on TinyLlama-1.1B, Qwen2.5-{1.5B, 3B}, Llama-3.1-Nemotron-Nano-4B (clean; ~3.5–4.4 GB peak depending on model)
  - Multi-Jetson FSDP1 + QLoRA on TinyLlama-1.1B (N=3 corroborated, ~1174 MB / rank)
  - Multi-Jetson FSDP2 + QLoRA on Qwen2.5-3B (N=3 30-step + N=1 1000-step long-horizon, 2378 ± 1 MB / rank, no system-RAM growth across the long-horizon i observed.   DeviceMesh.from_group(pg, "cuda") bypasses the FSDP2 NCCL constraint on Tegra)
  - Single-Jetson Mistral-7B-v0.3 QLoRA (N=4 across 10 / 200 / 5000-step horizons, 15,610 cumulative stable training steps, 5044 ± 1 MB peak deterministic to <0.01% σ)

A suggestion for whoever ends up shipping the wheel: the sm_87 NF4 dequant path has a reproducible fault that bites at 7B-class workloads — see #1936 (multi-shape Linear4bit sequence reproducibly reboots the Jetson). It doesn't affect the 1B–4B class workloads above, but it does affect Llama-3.1-8B / Qwen2.5-7B (Mistral-7B-v0.3 is able to dodges it via its 32K vocab + intermediate=14336 + no-FSDP path). Seemed worth sharing and maybe mentioning in the wheel release notes.

I'm happy to share the full single-device and or multi Jetson reproducers, including the dual-NIC topology setup for the FSDP path, or instrumentation runs against #1936 that's helpful.
