# [Issue #3374] [Bug] undefined symbol: TVMFFIBacktrace

source: https://github.com/mlc-ai/mlc-llm/issues/3374
state: closed | updated: 2026-01-25T17:17:27Z
labels: bug

## 正文

## 🐛 Bug

Hi, I have compiled this project from source code, but when I tried to import mlc_llm, it would report an error about `undefined symbol: TVMFFIBacktrace.`

I have tried to set `USE_LIBBACKTRACE=OFF` in `/MLC/mlc-llm/3rdparty/tvm/CMakeLists.txt` and `TVM_FFI_USE_LIBBACKTRACE=OFF` in `/MLC/mlc-llm/3rdparty/tvm/build/config.cmake`, but it didn't help.

## To Reproduce

Steps to reproduce the behavior:

1. compile mlc-llm in `/MLC/mlc-llm/build`
1. compile tvm in `/MLC/mlc-llm/3rdparty/tvm/build`
1. cd `/MLC/mlc-llm/` and run command `python -c "import mlc_llm; print(mlc_llm.__path__)"`

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->
`(mlc-llm-251104) root@843c8f74d833:~/nfs/MLC/mlc-llm# python -c "import mlc_llm; print(mlc_llm.__path__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/root/nfs/MLC/mlc-llm/python/mlc_llm/__init__.py", line 6, in <module>
    from tvm import register_global_func
  File "/root/nfs/MLC/mlc-llm/3rdparty/tvm/python/tvm/__init__.py", line 27, in <module>
    from .base import TVMError, __version__, _RUNTIME_ONLY
  File "/root/nfs/MLC/mlc-llm/3rdparty/tvm/python/tvm/base.py", line 61, in <module>
    _LIB, _LIB_NAME = _load_lib()
                      ^^^^^^^^^^^
  File "/root/nfs/MLC/mlc-llm/3rdparty/tvm/python/tvm/base.py", line 48, in _load_lib
    lib = ctypes.CDLL(lib_path[0], ctypes.RTLD_GLOBAL)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/nfs/anaconda3/envs/mlc-llm-251104/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /root/nfs/MLC/mlc-llm/3rdparty/tvm/build/libtvm.so: undefined symbol: TVMFFIBacktrace`

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): 
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu 20.04
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): PC
 - How you installed MLC-LLM (`conda`, source): source
 - How you installed TVM (`pip`, source): source
 - Python version (e.g. 3.10): 3.12
 - GPU driver version (if applicable): 
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (8)

### MasterJH5574 · 2025-11-10

@Msyu1020 thanks for the question.  I wonder what will show if you run `python -c "import tvm_ffi"`.

### Msyu1020 · 2025-11-13

> [@Msyu1020](https://github.com/Msyu1020) thanks for the question. I wonder what will show if you run `python -c "import tvm_ffi"`.

I installed the **MLCLLM** Python package using the nightly pip wheels, and the command  
`python -c "import mlc_llm; print(mlc_llm.__path__)"` now prints the correct path.

However, when I tried to compile the models, I encountered the following error:

`tvm.error.InternalError: LLVM module verification failed with the following.`

[mlcllm_package_log.txt](https://github.com/user-attachments/files/23523666/mlcllm_package_log.txt)

I've attached the full log. Any help or guidance would be greatly appreciated!

### Msyu1020 · 2025-11-13

> [@Msyu1020](https://github.com/Msyu1020) thanks for the question. I wonder what will show if you run `python -c "import tvm_ffi"`.

run `python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`  and `conda list`, the related libs are as follow:

[tvm_libinfo.txt](https://github.com/user-attachments/files/23523801/tvm_libinfo.txt)

### Msyu1020 · 2025-11-16

I successfully ran llama-3.2-1B on the Xiaomi 14 Pro. The error` tvm.error.InternalError: LLVM module verification failed with the following. ` was caused by an incompatible LLVM version. I tried to compile MLC LLM from source again, and LLVM 15 works fine, but using version 21 leads to issues.

### westbrookwang-broodie · 2025-11-21

hi @Msyu1020 , I've met the same problem and I'd like to ask you that how you fix it. I downgrade my llvm from 21 to 15, but still go wrong.

### Msyu1020 · 2025-11-21

> hi [@Msyu1020](https://github.com/Msyu1020) , I've met the same problem and I'd like to ask you that how you fix it. I downgrade my llvm from 21 to 15, but still go wrong.

Hi! If you installed TVM or MLC-LLM via pip wheels, downgrading LLVM won't be effective. To resolve this, please build MLC from source, and also ensure that TVM is built from source (using the mlc/3rdparty/tvm directory). Hope this helps!

### westbrookwang-broodie · 2025-11-24

> > hi [@Msyu1020](https://github.com/Msyu1020) , I've met the same problem and I'd like to ask you that how you fix it. I downgrade my llvm from 21 to 15, but still go wrong.
> 
> Hi! If you installed TVM or MLC-LLM via pip wheels, downgrading LLVM won't be effective. To resolve this, please build MLC from source, and also ensure that TVM is built from source (using the mlc/3rdparty/tvm directory). Hope this helps!

It really help. Thank for your help

### MasterJH5574 · 2026-01-25

Hi @Msyu1020 @westbrookwang-broodie, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
