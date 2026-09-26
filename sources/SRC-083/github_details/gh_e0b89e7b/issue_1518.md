# [Issue #1518] Required library version not found: libbitsandbytes_cuda124_nocublaslt.so

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1518
state: closed | updated: 2026-06-11T13:20:44Z
labels: Question, CUDA Setup, Linux

## 正文

### System Info

False

===================================BUG REPORT===================================
/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: Welcome to bitsandbytes. For bug reports, please run

python -m bitsandbytes


  warn(msg)
================================================================================
/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: /home/sklioui/miniconda3/envs/luma_unbias did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: /trinity/shared/apps/tr17.10/x86_64/cuda-12.4/lib64 did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
The following directories listed in your path were found to be non-existent: {PosixPath('/trinity/shared/apps/tr17.10/x86_64/cuda-12.4/doc/man')}
The following directories listed in your path were found to be non-existent: {PosixPath('/usr/lib64/qt-3.3/include')}
The following directories listed in your path were found to be non-existent: {PosixPath('//matplotlib_inline.backend_inline'), PosixPath('module')}
The following directories listed in your path were found to be non-existent: {PosixPath('cuda/12.4'), PosixPath('userspace/all')}
The following directories listed in your path were found to be non-existent: {PosixPath('/run/user/2569/vscode-git-2cb3a4d16d.sock')}
The following directories listed in your path were found to be non-existent: {PosixPath('/run/user/2569/vscode-ipc-c2b58e1d-ebe4-4b31-a2eb-0f592a570bed.sock')}
The following directories listed in your path were found to be non-existent: {PosixPath('() {  eval `/usr/bin/modulecmd bash $*`\n}')}
DEBUG: Possible options found for libcudart.so: {PosixPath('/trinity/shared/apps/tr17.10/x86_64/cuda-12.4/lib64/libcudart.so')}
CUDA SETUP: PyTorch settings found: CUDA_VERSION=124, Highest Compute Capability: 7.0.
CUDA SETUP: To manually override the PyTorch CUDA version please see:https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:167: UserWarning: WARNING: Compute capability < 7.5 detected! Only slow 8-bit matmul is supported for your GPU!                     If you run into issues with 8-bit matmul, you can try 4-bit quantization: https://huggingface.co/blog/4bit-transformers-bitsandbytes
  warn(msg)
CUDA SETUP: Required library version not found: libbitsandbytes_cuda124_nocublaslt.so. Maybe you need to compile it from source?
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
CUDA_VERSION=124_nomatmul
python setup.py install
CUDA SETUP: Setup Failed!
Traceback (most recent call last):
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/runpy.py", line 187, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/runpy.py", line 146, in _get_module_details
    return _get_module_details(pkg_main_name, error)
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/runpy.py", line 110, in _get_module_details
    __import__(pkg_name)
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/__init__.py", line 6, in <module>
    from . import cuda_setup, utils, research
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/research/__init__.py", line 1, in <module>
    from . import nn
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/research/nn/__init__.py", line 1, in <module>
    from .modules import LinearFP8Mixed, LinearFP8Global
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/research/nn/modules.py", line 8, in <module>
    from bitsandbytes.optim import GlobalOptimManager
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/optim/__init__.py", line 6, in <module>
    from bitsandbytes.cextension import COMPILED_WITH_CUDA
  File "/home/sklioui/miniconda3/envs/luma_unbias/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 20, in <module>
    raise RuntimeError('''
RuntimeError: 
        CUDA Setup failed despite GPU being available. Please run the following command to get more information:

        python -m bitsandbytes

        Inspect the output of the command and see if you can locate CUDA libraries. You might need to add them
        to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
        and open an issue at: https://github.com/TimDettmers/bitsandbytes/issues

### Reproduction

```cmd
python -m bitsandbytes
```

### Expected behavior

```True``` ?

## 评论 (6)

### djbyrne · 2025-02-17

I am also seeing this, any ideas on how to fix? 


### MostHumble · 2025-02-17

I haven't had time to investigate this. For me, it might be caused by one of the following:  
- Either the fact that I'm using SLURM with MODULE, and the paths are not being handled correctly  
- Or because I'm using a V100, which might not be supported for some reason  

### djbyrne · 2025-02-17

I am seeing the same on H200 just using kubernetes batch jobs 

### matthewdouglas · 2025-02-19

V100 is supported, as well as H200. Please upgrade to the latest bitsandbytes release.

### TimDettmers · 2025-02-28

I am closing this since this seems to be related to an old bitsandbytes version that did not support this CUDA version / GPUs.

### hover03 · 2026-06-11

I solved the problem by updating bitsandbytes to the newest version
