# [Issue #1918] Linux CUDA detection failed!

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1918
state: closed | updated: 2026-04-09T06:05:43Z
labels: 

## 正文

### System Info

Debian 13
Python 3.11.14
libcuda.so.590.48.01
cuda:0 NVIDIA GeForce RTX 5060 Ti : cudaMallocAsync

```
pip list |grep bitsandbytes
bitsandbytes                             0.49.1
bitsandbytes-windows                     0.37.5
``

### Reproduction


python -m bitsandbytes

### Expected behavior

```
/home/test/.venvs/py311/lib/python3.11/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you.
  import pynvml  # type: ignore[import]

===================================BUG REPORT===================================
Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues
================================================================================
binary_path: /home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/cuda_setup\libbitsandbytes_cuda116.dll
CUDA SETUP: Required library version not found: cuda_setup\libbitsandbytes_cuda116.dll. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. CUDA driver not installed
2. CUDA not installed
3. You have multiple conflicting CUDA libraries
4. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Problem: The main issue seems to be that the main CUDA library was not detected.
CUDA SETUP: Solution 1): Your paths are probably not up-to-date. You can update them via: sudo ldconfig.
CUDA SETUP: Solution 2): If you do not have sudo rights, you can do the following:
CUDA SETUP: Solution 2a): Find the cuda library via: find / -name libcuda.so 2>/dev/null
CUDA SETUP: Solution 2b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_2a
CUDA SETUP: Solution 2c): For a permanent solution add the export from 2b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Required library version not found: cuda_setup\libbitsandbytes_cuda116.dll. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. CUDA driver not installed
2. CUDA not installed
3. You have multiple conflicting CUDA libraries
4. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Problem: The main issue seems to be that the main CUDA library was not detected.
CUDA SETUP: Solution 1): Your paths are probably not up-to-date. You can update them via: sudo ldconfig.
CUDA SETUP: Solution 2): If you do not have sudo rights, you can do the following:
CUDA SETUP: Solution 2a): Find the cuda library via: find / -name libcuda.so 2>/dev/null
CUDA SETUP: Solution 2b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_2a
CUDA SETUP: Solution 2c): For a permanent solution add the export from 2b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Setup Failed!
CUDA SETUP: Required library version not found: cuda_setup\libbitsandbytes_cuda116.dll. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. CUDA driver not installed
2. CUDA not installed
3. You have multiple conflicting CUDA libraries
4. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Problem: The main issue seems to be that the main CUDA library was not detected.
CUDA SETUP: Solution 1): Your paths are probably not up-to-date. You can update them via: sudo ldconfig.
CUDA SETUP: Solution 2): If you do not have sudo rights, you can do the following:
CUDA SETUP: Solution 2a): Find the cuda library via: find / -name libcuda.so 2>/dev/null
CUDA SETUP: Solution 2b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_2a
CUDA SETUP: Solution 2c): For a permanent solution add the export from 2b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Setup Failed!
CUDA SETUP: Required library version not found: cuda_setup\libbitsandbytes_cuda116.dll. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. CUDA driver not installed
2. CUDA not installed
3. You have multiple conflicting CUDA libraries
4. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Problem: The main issue seems to be that the main CUDA library was not detected.
CUDA SETUP: Solution 1): Your paths are probably not up-to-date. You can update them via: sudo ldconfig.
CUDA SETUP: Solution 2): If you do not have sudo rights, you can do the following:
CUDA SETUP: Solution 2a): Find the cuda library via: find / -name libcuda.so 2>/dev/null
CUDA SETUP: Solution 2b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_2a
CUDA SETUP: Solution 2c): For a permanent solution add the export from 2b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Setup Failed!
CUDA SETUP: Problem: The main issue seems to be that the main CUDA library was not detected.
CUDA SETUP: Solution 1): Your paths are probably not up-to-date. You can update them via: sudo ldconfig.
CUDA SETUP: Solution 2): If you do not have sudo rights, you can do the following:
CUDA SETUP: Solution 2a): Find the cuda library via: find / -name libcuda.so 2>/dev/null
CUDA SETUP: Solution 2b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_2a
CUDA SETUP: Solution 2c): For a permanent solution add the export from 2b into your .bashrc file, located at ~/.bashrc
Traceback (most recent call last):
  File "<frozen runpy>", line 189, in _run_module_as_main
  File "<frozen runpy>", line 148, in _get_module_details
  File "<frozen runpy>", line 112, in _get_module_details
  File "/home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/__init__.py", line 7, in <module>
    from .autograd._functions import (
  File "/home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/autograd/__init__.py", line 1, in <module>
    from ._functions import undo_layout, get_inverse_transform_indices
  File "/home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/autograd/_functions.py", line 9, in <module>
    import bitsandbytes.functional as F
  File "/home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/functional.py", line 17, in <module>
    from .cextension import COMPILED_WITH_CUDA, lib
  File "/home/test/.venvs/py311/lib/python3.11/site-packages/bitsandbytes/cextension.py", line 22, in <module>
    raise RuntimeError('''
RuntimeError: 
        CUDA Setup failed despite GPU being available. Inspect the CUDA SETUP outputs above to fix your environment!
        If you cannot find any issues and suspect a bug, please open an issue with detals about your environment:
        https://github.com/TimDettmers/bitsandbytes/issues
```
```
# ls -la /usr/lib/x86_64-linux-gnu/libcuda.so
lrwxrwxrwx 1 root root 12 14 janv. 10:40 /usr/lib/x86_64-linux-gnu/libcuda.so -> libcuda.so.1
# ls -la /usr/lib/x86_64-linux-gnu/libcuda.so.1 
lrwxrwxrwx 1 root root 20 14 janv. 10:40 /usr/lib/x86_64-linux-gnu/libcuda.so.1 -> libcuda.so.590.48.01
# ls -la /usr/lib/x86_64-linux-gnu/libcuda.so.590.48.01 
-rwxr-xr-x 1 root root 98760392 14 janv. 10:40 /usr/lib/x86_64-linux-gnu/libcuda.so.590.48.01
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu
Not solve the issue.
Thanks.

## 评论 (2)

### matthewdouglas · 2026-04-08

Hi,

`bitsandbytes-windows` is not an official bitsandbytes distribution. Secondly, you're not on Windows anyway. Please uninstall it. Then reinstall the latest `bitsandbytes` and try again.

### zz64 · 2026-04-09

> Please uninstall it. Then reinstall the latest `bitsandbytes` and try again.

Yeah, is fixed.

i have no idea why "bitsandbytes-windows" installed in Linux with ComfyUI-Manager. 

Thanks.

