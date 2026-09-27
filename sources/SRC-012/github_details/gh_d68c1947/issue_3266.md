# [Issue #3266] Build mlc-llm and tvm from source code and failed

source: https://github.com/mlc-ai/mlc-llm/issues/3266
state: closed | updated: 2026-03-02T14:49:49Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->

## To Reproduce

Steps to reproduce the behavior:

1.build tvm sucessfully and install
2.build mlc-llm succesfully and install
3.run "mlc_llm chat -h " and failed
Traceback (most recent call last):
  File "<frozen runpy>", line 189, in _run_module_as_main
  File "<frozen runpy>", line 148, in _get_module_details
  File "<frozen runpy>", line 112, in _get_module_details
  File "/home/lpy/mlc-llm/python/mlc_llm/__init__.py", line 8, in <module>
    from . import protocol, serve
  File "/home/lpy/mlc-llm/python/mlc_llm/serve/__init__.py", line 4, in <module>
    from .. import base
  File "/home/lpy/mlc-llm/python/mlc_llm/base.py", line 47, in <module>
    _LIB, _LIB_PATH = _load_mlc_llm_lib()
                      ^^^^^^^^^^^^^^^^^^^
  File "/home/lpy/mlc-llm/python/mlc_llm/base.py", line 24, in _load_mlc_llm_lib
    return ctypes.CDLL(lib_path[0]), lib_path[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wzh/miniconda3/envs/tvm-build-venv/lib/python3.11/ctypes/__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /home/lpy/mlc-llm/python/mlc_llm/libmlc_llm_module.so: undefined symbol: _ZN3tvm7runtime10ModuleNode10SaveToFileERKNS0_6StringES4_

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA):CUDA
 - Operating system (e.g. Ubuntu/Windows/MacOS/...):Ubuntu
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) android
 - How you installed MLC-LLM (`conda`, source): source
 - How you installed TVM-Unity (`pip`, source): source
 - Python version (e.g. 3.10):3.11
 - GPU driver version (if applicable):Nvidia
 - CUDA/cuDNN version (if applicable):CUDA11.5
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (1)

### grabbou · 2025-10-13

When building, I suggest checking out v19. This worked for me. Currently main/v0.20 branch doesn't work well with precompiled CLI.
