# [Issue #1519] Multiple issues installing for AMD GPU (Radeon RX7600XT)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1519
state: closed | updated: 2026-02-24T15:20:42Z
labels: Documentation, High Priority, ROCm, Low Risk

## 正文

### System Info

I am under Linux Mint Xia (based on Ubuntu 24.04).
CPU: AMD Ryzen 9 5950X 16-Core Processor with 64GiB RAM.
GPU: Advanced Micro Devices, Inc. [AMD/ATI] Navi 33 [Radeon RX 7600/7600 XT/7600M XT/7600S/7700S / PRO W7600] (rev c0) (Actually: RX 7600 XT, if it matters)
Python: Python 3.10.16
Application: I am testing with `InvokeAI`

### Reproduction

I tried following [recipe](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/multi-backend-refactor/docs/source/installation.mdx#amd-gpu) but I found several errors:

- project has been converted to `.toml` and thus `pip install -r requirements-dev.txt` won't work.
- `cmake -DCOMPUTE_BACKEND=hip -S . && make` completes with no errors (just a few "kernels.hip:2857:17: warning: loop not unrolled:...".
- Installing in venv did not complain but usage resulted in hard error:
  ```
  Could not load bitsandbytes native library: /home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
  Traceback (most recent call last):
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 107, in <module>
    lib = get_native_library()
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
  File "/usr/local/lib/python3.10/ctypes/__init__.py", line 452, in LoadLibrary
    return self._dlltype(name)
  File "/usr/local/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
  OSError: /home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

  ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

  python -m bitsandbytes

  Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
  to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
  and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues
  ```
I also tried:
```
(invoke) mcon@ikea:~/tmp/t$ ROCM_PATH=/opt/rocm LD_LIBRARY_PATH=/opt/rocm/lib python -m bitsandbytes
Could not load bitsandbytes native library: /home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
Traceback (most recent call last):
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 107, in <module>
    lib = get_native_library()
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
  File "/usr/local/lib/python3.10/ctypes/__init__.py", line 452, in LoadLibrary
    return self._dlltype(name)
  File "/usr/local/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: /home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

python -m bitsandbytes

Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='63', rocm_version_tuple=(6, 3)
PyTorch settings found: ROCM_VERSION=63
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
Couldn't load the bitsandbytes library, likely due to missing binaries.
Please ensure bitsandbytes is properly installed.

For source installations, compile the binaries with `cmake -DCOMPUTE_BACKEND=hip -S .`.
See the documentation for more details if needed.

Trying a simple check anyway, but this will likely fail...
Traceback (most recent call last):
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/diagnostics/main.py", line 73, in main
    sanity_check()
  File "/home/mcon/tmp/t/invoke/lib/python3.10/site-packages/bitsandbytes/diagnostics/main.py", line 37, in sanity_check
    p1 = p.data.sum().item()
RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

Above we output some debug information.
Please provide this info when creating an issue via https://github.com/TimDettmers/bitsandbytes/issues/new/choose
WARNING: Please be sure to sanitize sensitive info from the output before posting it.
```

### Expected behavior

I expected to be able to use `bitsandbytes`.

## 评论 (39)

### matthewdouglas · 2025-02-19

Thanks for reporting. You're right that the `requirements-dev.txt` has been removed and we need to update the docs.

Unfortunately the preview branch is in a broken state at the moment on ROCm. We're working on it! The commit at `a0a95fd` might be the best bet in the meantime.

### mcondarelli · 2025-02-19

> Unfortunately the preview branch is in a broken state at the moment on ROCm. We're working on it! The commit at `a0a95fd` might be the best bet in the meantime.

Thanks, I am now using fork by AMD (https://github.com/ROCm/bitsandbytes) which seems to be working; what is advise? use that or commit at `a0a95fd`?

### matthewdouglas · 2025-02-19

I think either should be fine but if you've already achieved a working build then I would personally stick to that.

### visionscaper · 2025-02-20

I had exactly the same issue:
```
Could not load bitsandbytes native library: bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
```

Reverting to commit `a0a95fd` seem to have resolved this particular issue, however another one surfaced:
```
$ python -m bitsandbytes
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 187, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/usr/lib/python3.10/runpy.py", line 146, in _get_module_details
    return _get_module_details(pkg_main_name, error)
  File "/usr/lib/python3.10/runpy.py", line 110, in _get_module_details
    __import__(pkg_name)
  File "/home/freddy/workspace/bitsandbytes/bitsandbytes/__init__.py", line 70, in <module>
    from .nn import modules
  File "/home/freddy/workspace/bitsandbytes/bitsandbytes/nn/__init__.py", line 21, in <module>
    from .triton_based_modules import (
  File "/home/freddy/workspace/bitsandbytes/bitsandbytes/nn/triton_based_modules.py", line 7, in <module>
    from bitsandbytes.triton.int8_matmul_mixed_dequantize import (
  File "/home/freddy/workspace/bitsandbytes/bitsandbytes/triton/int8_matmul_mixed_dequantize.py", line 12, in <module>
    from triton.ops.matmul_perf_model import early_config_prune, estimate_matmul_time
ModuleNotFoundError: No module named 'triton.ops'
```

This seems to relate to issue #1492 . Is this correct?

Anything else I can do to make it work in the meantime?

### visionscaper · 2025-02-20

Also checked the [bitsandbytes AMD fork](https://github.com/ROCm/bitsandbytes) but this resulted in the same issue `ModuleNotFoundError: No module named 'triton.ops'`.

I'm using the latest PyTorch nightly:
```
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3
```

```
pip show torch
$ pip show torch
Name: torch
Version: 2.7.0.dev20250220+rocm6.3
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: lib/python3.10/site-packages
Requires: filelock, fsspec, jinja2, networkx, pytorch-triton-rocm, sympy, typing-extensions
Required-by: accelerate, bitsandbytes, lion-pytorch, torchaudio, torchvision
```

### Lier0 · 2025-02-21

https://github.com/triton-lang/triton/issues/5471
` pip install --force-reinstall triton==3.1.0` may work around.

### mcondarelli · 2025-02-21

> [triton-lang/triton#5471](https://github.com/triton-lang/triton/issues/5471) ` pip install --force-reinstall triton==3.1.0` may work around.

I assume you mean `pytorch-triton[-rocm]==3.1.0` as plain `triton` is at `v2.1.0`, right?

### Lier0 · 2025-02-21

Yeah.
But there is other dependencies about rocm. 
python-triton-rocm-3.1.0 goes with python-torch-2.5.1, about rocm6.2. xformer may complain.

### mcondarelli · 2025-02-22

FYI:
This incomplete and convoluted script produces an apparently working installation.
I will try to simplify it.

```
#!/bin/bash
set -e

script_path=$(readlink -f "$0" 2>/dev/null || realpath "$0" 2>/dev/null || echo "$0")
sdir="$(dirname "${script_path}")"
sdir="$(cd "$sdir" && pwd)"
echo "The path of this script is: $script_path ($sdir)"
here=$(pwd)
user=$(ls -ld "$script_path" | awk '{print $3}')
home=$(getent passwd "$user" | cut -d: -f6)
echo "Home directory of $user is $home"

VENV="torch_venv"
PYTHON="python3.11"
REPO=https://download.pytorch.org/whl/nightly/rocm6.3

# Function to extract and install missing packages
install_missing_packages() {
    local EXTRA=$1
    local continue=Y
    while [ "$continue" == Y ]
    do
        # Run pip check and capture the output
        output=$($VENV/bin/pip check 2>&1 || :)
        echo "$output"

        # Extract missing packages
        missing_packages=()
        while IFS= read -r line
        do
            echo "$line"
            if [[ $line =~ requires\ ([^,]+),\ which\ is\ not\ installed ]]
            then
                missing_packages+=("${BASH_REMATCH[1]}")
                echo "${missing_packages[*]}"
            fi
        done <<< "$output"

        # If no missing packages, exit the loop
        if [ ${#missing_packages[@]} -eq 0 ]; then
            echo "No more missing packages found."
            break
        fi

        continue=N
        # Install missing packages with --ignore-installed --no-deps
        echo "Installing missing packages: ${missing_packages[*]}"
        for pkg in "${missing_packages[@]}"
        do
            echo "Running: pip install --ignore-installed --no-deps $EXTRA $pkg"
            if $VENV/bin/pip install --ignore-installed --no-deps $EXTRA "$pkg"
            then
                continue=Y
            else
                echo "Failed to install $pkg. Continuing with the next package..."
            fi
        done
    done
}

check_base () {
    if [ -d "$VENV" ]
    then
        # check Virtual Environment exists
        if [ -x "$VENV/bin/python" ]
        then
            echo "Virtual Environment at '$VENV' already present, skipping..."
        else
            echo "Directory at '$VENV' exixts but doesn't look like a Virtual Environment: bailing out."
            exit 1
        fi
    else
        echo "Creating basic Virtual Environment at '$VENV'..."
        # prepare environment
        $PYTHON -m venv $VENV
        $VENV/bin/pip install -U pip wheel
    fi
}

check_torch () {
    modules='pytorch-triton-rocm==3.1.0 torch torchvision torchaudio'
    # shellcheck disable=SC2043
    for module in $modules
    do
        name=${module%%==*}
        name=${name//-/_}
        
        [ -n "$(ls -dl $VENV/lib/*/site-packages/${name}{-*,.*,} 2>/dev/null)" ] || $VENV/bin/pip install --index-url $REPO --no-deps $module
    done
    install_missing_packages "--index-url $REPO"
    install_missing_packages
}

check_bitsandbytes () {
    repository='https://github.com/ROCm/bitsandbytes'
    tag='rocm_enabled_multi_backend'
    arch='gfx1100;gfx1102'
    module='bitsandbytes'
    if [ ! -d "$VENV/lib/*/site-packages/$module" ]
    then
        echo "Module '$module' not present in $VENV: installing..."
        if [ ! -d "$sdir/$module" ]
        then
            echo "Sources for '$modules' not present in chache: rebuilding..."
            (
                cd "$sdir"
                git clone "$repository"
                cd "$module"
                git checkout "$tag"
                cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="$arch" -S .
                make
            )
        fi
        $VENV/bin/pip install --no-deps "$sdir/$module"
        install_missing_packages
    fi
}

check_base
check_torch
check_bitsandbytes

export PYTORCH_ROCM_ARCH=gfx1102
export HSA_OVERRIDE_GFX_VERSION=11.0.0
export PYTORCH_HIP_ALLOC_CONF=expandable_segments:True
export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
export INVOKEAI_ROOT=~/invokeai
export GPU_DRIVER=rocm
$VENV/bin/python -m bitsandbytes
```

### visionscaper · 2025-02-23

@Lier0 @mcondarelli  Did you mean `pytorch-triton-rocm==2.1.0`? `3.1.0` doesn't exist ...

Edit: I now see I have `pytorch-triton-rocm==3.2.0+git4b3bb1f8` after installing PyTorch nightly:
```
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3
```
But that results in the issue `No module named 'triton.ops'` mentioned before.

**How to get `pytorch-triton-rocm==3.1.0`?**



### visionscaper · 2025-02-23

@Lier0 I figured it out, thanks to @mcondarelli script. The correct command is:
```
pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.3
```

In your reply you didn't add the `--index-url https://download.pytorch.org/whl/nightly/rocm6.3` part, which threw me off.

### msyzzm · 2025-02-24

> [@Lier0](https://github.com/Lier0) I figured it out, thanks to [@mcondarelli](https://github.com/mcondarelli) script. The correct command is:
> 
> ```
> pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.3
> ```
> 
> In your reply you didn't add the `--index-url https://download.pytorch.org/whl/nightly/rocm6.3` part, which threw me off.

Works for me. Thank you!

### TimDettmers · 2025-02-28

Thank you for bringing this up and the discussion. We will try to understand the issues here and get back to you.

### mcondarelli · 2025-03-03

The error still holds true with latest wheel installed as:
```bash
pip install https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-1.0.0-py3-none-manylinux_2_24_x86_64.whl
```
Please fix before releasing v1.0.0.
I am available for testing, if useful.
```
ERROR    Could not load bitsandbytes native library: 
                             /home/mcon/LLaMaConda/FluxGym/fluxgym/env/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so:                   
                             undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi                            
                             Traceback (most recent call last):                                                                                               
                               File "/home/mcon/LLaMaConda/FluxGym/fluxgym/env/lib/python3.10/site-packages/bitsandbytes/cextension.py",                      
                             line 107, in <module>                                                                                                            
                                 lib = get_native_library()                                                                                                   
                               File "/home/mcon/LLaMaConda/FluxGym/fluxgym/env/lib/python3.10/site-packages/bitsandbytes/cextension.py",                      
                             line 86, in get_native_library                                                                                                   
                                 dll = ct.cdll.LoadLibrary(str(binary_path))                                                                                  
                               File "/usr/local/lib/python3.10/ctypes/__init__.py", line 452, in LoadLibrary                                                  
                                 return self._dlltype(name)                                                                                                   
                               File "/usr/local/lib/python3.10/ctypes/__init__.py", line 374, in __init__                                                     
                                 self._handle = _dlopen(self._name, mode)                                                                                     
                             OSError:                                                                                                                         
                             /home/mcon/LLaMaConda/FluxGym/fluxgym/env/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_rocm63.so:                   
                             undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi                            
```

### Disty0 · 2025-03-25

I can reproduce the;
```
undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
```
Issue on an RX 7900 XTX (different GPU than the OP and officially supported by ROCm) with ROCm 6.3 too.

PyTorch version: `2.8.0.dev20250325+rocm6.3`

Build from source steps:
```sh
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
cmake -DCOMPUTE_BACKEND=hip -S .
make
pip install .
```


Python trace:
```py
(venv) disty:/mnt/DataSSD/AI/Apps/bitsandbytes $ python
Python 3.12.9 (main, Feb  6 2025, 15:54:32) [GCC 14.2.1 20250128] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bitsandbytes
Could not load bitsandbytes native library: /mnt/DataSSD/AI/Apps/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
Traceback (most recent call last):
  File "/mnt/DataSSD/AI/Apps/bitsandbytes/bitsandbytes/cextension.py", line 107, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/mnt/DataSSD/AI/Apps/bitsandbytes/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ctypes/__init__.py", line 460, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /mnt/DataSSD/AI/Apps/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

python -m bitsandbytes

Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues

>>>
```

Also there were warnings when building kernels.hip too:

```
(venv) disty:/mnt/DataSSD/AI/Apps/bitsandbytes $ make
[ 16%] Building CXX object CMakeFiles/bitsandbytes.dir/csrc/common.cpp.o
[ 33%] Building CXX object CMakeFiles/bitsandbytes.dir/csrc/cpu_ops.cpp.o
[ 50%] Building CXX object CMakeFiles/bitsandbytes.dir/csrc/pythonInterface.cpp.o
[ 66%] Building HIP object CMakeFiles/bitsandbytes.dir/csrc/ops.hip.o
[ 83%] Building HIP object CMakeFiles/bitsandbytes.dir/csrc/kernels.hip.o
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
 2857 | __global__ void kspmm_coo_very_sparse_naive(int *max_count, int *max_idx, int *offset_rowidx, int *rowidx, int *colidx, half *values, T *B, half *out, float * __restrict__ const dequant_stats, int nnz, int rowsA, int rowsB, int colsB)
      |                 ^
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
/mnt/DataSSD/AI/Apps/bitsandbytes/csrc/kernels.hip:2857:17: warning: loop not unrolled: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering [-Wpass-failed=transform-warning]
6 warnings generated when compiling for gfx1100.
[100%] Linking CXX shared library bitsandbytes/libbitsandbytes_rocm63.so
[100%] Built target bitsandbytes
```

### erasmus74 · 2025-04-21

Same as above
```export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib
    uv run python -m bitsandbytes
Could not load bitsandbytes native library: /home/master/workspace/testing/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi. If you use Intel CPU or XPU, please pip install intel_extension_for_pytorch
Traceback (most recent call last):
  File "/home/master/workspace/testing/bitsandbytes/bitsandbytes/cextension.py", line 115, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/master/workspace/testing/bitsandbytes/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/master/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/ctypes/__init__.py", line 460, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/master/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /home/master/workspace/testing/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

    ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

    python -m bitsandbytes

    Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
    to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
    and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues
    
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='63', rocm_version_tuple=(6, 3)
PyTorch settings found: ROCM_VERSION=63
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
Couldn't load the bitsandbytes library, likely due to missing binaries.
Please ensure bitsandbytes is properly installed.

For source installations, compile the binaries with `cmake -DCOMPUTE_BACKEND=hip -S .`.
See the documentation for more details if needed.

Trying a simple check anyway, but this will likely fail...
Traceback (most recent call last):
  File "/home/master/workspace/testing/bitsandbytes/bitsandbytes/diagnostics/main.py", line 73, in main
    sanity_check()
  File "/home/master/workspace/testing/bitsandbytes/bitsandbytes/diagnostics/main.py", line 42, in sanity_check```

### billishyahao · 2025-04-25

The problem can be reproduced at MI300X too.

```
undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi.
```

For how to reproduce the error :
```
Step 1: docker pull rocm/pytorch-training:v25.5
 
Step 2: Install bitsandbytes from source
# Clone bitsandbytes repo, ROCm backend is currently enabled on multi-backend-refactor branch
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
 
# Compile & install
apt-get install -y build-essential cmake  # install build tools dependencies, unless present
cmake -DCOMPUTE_BACKEND=hip -S .  # Use -DBNB_ROCM_ARCH="gfx90a;gfx942" to target specific gpu arch
make -j
pip install .   # `-e` for "editable" install, when developing BNB (otherwise leave that out)
 
```

### Asherathe · 2025-04-28

I also get "warning: loop not unrolled" and "undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi" on RX 6800 with ROCm 6.4 and torch 2.8.0.dev20250418+rocm6.4. The resulting bitsandbytes throws errors but seems to work, basically, in InvokeAI.

```
Could not load bitsandbytes native library: /InvokeAI/.venv/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi. If you use Intel CPU or XPU, please pip install intel_extension_for_pytorch
Traceback (most recent call last):
  File "/InvokeAI/.venv/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 115, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/InvokeAI/.venv/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/ctypes/__init__.py", line 460, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /InvokeAI/.venv/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
    ROCm Setup failed despite ROCm being available. Please run the following command to get more information:
    python -m bitsandbytes
    Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
    to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
    and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues
```

### tarkh · 2025-04-29

Same here on 7800xt, rocm63

Installing with
```
# Install bitsandbytes from source
# Clone bitsandbytes repo, ROCm backend is currently enabled on multi-backend-refactor branch
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/

# Compile & install
apt-get install -y build-essential cmake  # install build tools dependencies, unless present
cmake -DCOMPUTE_BACKEND=hip -S .  # Use -DBNB_ROCM_ARCH="gfx90a;gfx942" to target specific gpu arch
make
pip install -e .   # `-e` for "editable" install, when developing BNB (otherwise leave that out)
```

Getting error
```
[repo: bitsandbytes] python -m bitsandbytes                                                                                                                           on  multi-backend-refactor via △ v4.0.1 via 🐍 v3.11.11 (venv) 
Could not load bitsandbytes native library: /Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi. If you use Intel CPU or XPU, please pip install intel_extension_for_pytorch
Traceback (most recent call last):
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/cextension.py", line 115, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ctypes/__init__.py", line 454, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ctypes/__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/libbitsandbytes_rocm63.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

    ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

    python -m bitsandbytes

    Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
    to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
    and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues
    
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='63', rocm_version_tuple=(6, 3)
PyTorch settings found: ROCM_VERSION=63
The directory listed in your path is found to be non-existent: //github.com/tarkh/archw/tarball/main
The directory listed in your path is found to be non-existent: //raw.githubusercontent.com/tarkh
The directory listed in your path is found to be non-existent: //raw.githubusercontent.com/tarkh/archw/main/package/archw-tools/VERSION
The directory listed in your path is found to be non-existent: //github.com/tarkh
The directory listed in your path is found to be non-existent: /net/tenshu/Terminator2
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
Couldn't load the bitsandbytes library, likely due to missing binaries.
Please ensure bitsandbytes is properly installed.

For source installations, compile the binaries with `cmake -DCOMPUTE_BACKEND=hip -S .`.
See the documentation for more details if needed.

Trying a simple check anyway, but this will likely fail...
Traceback (most recent call last):
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/diagnostics/main.py", line 73, in main
    sanity_check()
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/diagnostics/main.py", line 42, in sanity_check
    adam.step()
  File "/Apps/Applications/llm-finetune/venv/lib/python3.11/site-packages/torch/optim/optimizer.py", line 485, in wrapper
    out = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/Apps/Applications/llm-finetune/venv/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/optim/optimizer.py", line 292, in step
    self.update_step(group, p, gindex, pindex)
  File "/Apps/Applications/llm-finetune/venv/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/optim/optimizer.py", line 522, in update_step
    F.optimizer_update_32bit(
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/functional.py", line 1266, in optimizer_update_32bit
    return backends[g.device.type].optimizer_update_32bit(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Apps/Applications/llm-finetune/bitsandbytes/bitsandbytes/backends/cuda.py", line 780, in optimizer_update_32bit
    optim_func = str2optimizer32bit[optimizer_name][0]
                 ^^^^^^^^^^^^^^^^^^
NameError: name 'str2optimizer32bit' is not defined
Above we output some debug information.
Please provide this info when creating an issue via https://github.com/TimDettmers/bitsandbytes/issues/new/choose
WARNING: Please be sure to sanitize sensitive info from the output before posting it.
```

### matthewwang16czap · 2025-05-03

This setup works for me. I tried other versions and they have different issues.

```
pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.2
pip install --no-deps --force-reinstall 'https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.45.1.dev0-py3-none-manylinux_2_24_x86_64.whl'
```

### markg85 · 2025-05-04

> This setup works for me. I tried other versions and they have different issues.
> 
> ```
> pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.2
> pip install --no-deps --force-reinstall 'https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.45.1.dev0-py3-none-manylinux_2_24_x86_64.whl'
> ```

AMD... really, this is a f****** nightmare. I have this 7900XT card, high end. Or so it seems. We're now a couple years after the release and still AMD can't get it's shit together with their RDNA3. Every time i try it with image generation (LLMs work fine) it's a day long of compiling, downloading/building and fingers crossed hoping for it to work.

Another day wasted. I did install that as you suggested @matthewwang16czap and i did get bitsandbytes working on my host machine once. Exactly **once**. Then i installed hidream which subsequently screwed with my versions (it installs a newer torch and the cuda version 😠).. I gave up on that route.

Then i tried in docker. Been 6 hours since i started that, giving up on that too.

I tried:
* this very repo (multi-backend-refactor branch). Failed.
* mimicing how this repo makes a [build](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/multi-backend-refactor/.github/scripts/build-rocm.sh). Failed.
* tried the [amd fork](https://github.com/ROCm/bitsandbytes/tree/upstream/multi-backend-refactor). Failed.
* I even tried to modify those files that use `kOptimizer32bit1State`! While that did compile, i apparently missed something as the eventual error was still the same.

**_Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi**

Keeps coming back. Every. Damn. Time.

I envy the nvidia users that have such a breeze with all of this. I would've switched if only nvidia wasn't such a lame ass manufacturer that soft-locks features (like gpu passthrough is detected by it and blocked).

### xzuyn · 2025-05-05

@markg85 Try this. It uses the old recommended `a0a95fd` commit, and replaces `int8_matmul_mixed_dequantize.py` and `int8_matmul_rowwise_dequantize.py` with dummy code which I found on an issue page to fix the  `ModuleNotFoundError: No module named 'triton.ops'` problem.

```sh
git clone -b multi-backend-refactor-a0a95fd-hacky-fix https://github.com/xzuyn/bitsandbytes.git
cd bitsandbytes
cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="gfx1100" -S .  # change "gfx1100" to what you need
make
pip install .
```

```sh
> python -m bitsandbytes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='63', rocm_version_tuple=(6, 3)
PyTorch settings found: ROCM_VERSION=63
The directory listed in your path is found to be non-existent: local/JOHN-V4
The directory listed in your path is found to be non-existent: @/tmp/.ICE-unix/3021,unix/JOHN-V4
The directory listed in your path is found to be non-existent: /etc/xdg/xdg-ubuntu
The directory listed in your path is found to be non-existent: /org/gnome/Terminal/screen/f0f7a6d2_eb6d_4c72_aaf5_c516b27d3f8e
The directory listed in your path is found to be non-existent: /home/xzuyn/.cache/dotnet_bundle_extract
The directory listed in your path is found to be non-existent: path=/run/user/1000/bus,guid=b63035f21f12b618d0dd60d86817e791
The directory listed in your path is found to be non-existent: //debuginfod.ubuntu.com 
WARNING! ROCm runtime files not found in any environmental path.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
SUCCESS!
Installation was successful!
```

I checked with latest PyTorch stuff (`pip install --pre torch torchvision pytorch-triton-rocm --index-url https://download.pytorch.org/whl/nightly/rocm6.3`), but probably works with older versions as I remember doing this same fix months ago too.

### markg85 · 2025-05-05

@xzuyn That is so nice of you, thank you for that hint! It got me a lot further!
The thing after this that - nearly - kills it is `flash_attn`.
There is a [AMD rocm fork](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/model-acceleration-libraries.html) which, and i should've know as this is a pattern with AMD forks, doesn't work. Sure it compiles but nothing actually works beyond it and the errors stay the same.
Then there is [the official version](https://github.com/Dao-AILab/flash-attention?tab=readme-ov-file#amd-rocm-support) that also has rocm support.

I still had to recompile a dozen times... Mainly because of other commands screwing it up again. Till i started using `--ignore-installed` in the pip install commands to finally stop it from breaking things.

Then i got a lot further. But still bitsandbytes is breaking it but now for another reason (`python -m bitsandbytes` works now!):
```bash
Model loaded successfully!
/opt/conda/envs/py_3.12/lib/python3.12/site-packages/apex/normalization/fused_layer_norm.py:188: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=False):
`torch.nn.functional.scaled_dot_product_attention` does not support `output_attentions=True`. Falling back to eager attention. This warning can be removed using the argument `attn_implementation="eager"` when loading the model.
WARNING:transformers.models.llama.modeling_llama:`torch.nn.functional.scaled_dot_product_attention` does not support `output_attentions=True`. Falling back to eager attention. This warning can be removed using the argument `attn_implementation="eager"` when loading the model.
  0%|                                                                                                           | 0/28 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/dockerx/HiDream-I1-nf4/hdi1/__main__.py", line 39, in <module>
    image, seed = generate_image(pipe, model_type, args.prompt, resolution, args.seed)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/dockerx/HiDream-I1-nf4/hdi1/nf4.py", line 97, in generate_image
    images = pipe(
             ^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/dockerx/HiDream-I1-nf4/hdi1/pipelines/hidream_image/pipeline_hidream_image.py", line 676, in __call__
    noise_pred = self.transformer(
                 ^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/dockerx/HiDream-I1-nf4/hdi1/models/transformers/transformer_hidream_image.py", line 407, in forward
    hidden_states = self.x_embedder(hidden_states)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/dockerx/HiDream-I1-nf4/hdi1/models/embeddings.py", line 57, in forward
    latent = self.proj(latent)
             ^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/nn/modules.py", line 519, in forward
    out = bnb.matmul_4bit(x, weight, bias=bias, quant_state=self.weight.quant_state)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/autograd/_functions.py", line 634, in matmul_4bit
    return MatMul4Bit.apply(A, B, out, bias, quant_state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/autograd/function.py", line 575, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/autograd/_functions.py", line 527, in forward
    output = torch.nn.functional.linear(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t(), bias)
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/functional.py", line 1065, in dequantize_4bit
    return backends[A.device.type].dequantize_4bit(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/backends/cuda.py", line 563, in dequantize_4bit
    raise ValueError(
ValueError: The blockwise of 64 is not supported. Supported values: [2048, 4096, 1024, 512, 256, 128]
```

The last line probably is the most important one:
ValueError: **The blockwise of 64 is not supported**. Supported values: [2048, 4096, 1024, 512, 256, 128]

### xzuyn · 2025-05-05

> The thing after this that - nearly - kills it is `flash_attn`.

I've just been using the one built into PyTorch; `export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1`. Trying to built the official one has either been too annoying, or slower than it for me to bother.

I'm not sure about the blockwise problem, I don't know if I'll be able to do anything about that.

### markg85 · 2025-05-05

Then numpy is a problem,
Then torch is.
Then "nn" whatever the heck that might be.
Then bitsandbytes is broken.
Then it's all nvidia again (because project don't give a damn about amd, apparently)
Then i have rocm 6.4 builds while i installed 6.3... (latest rocm docker). In fact, the pytoch site doesn't even list 6.4 yet, not even as nightly. It's in the nightly, i tried.
And so on and on  and on  and on  and on  and on  and on  and on ......

Deeply frustrating.
I'll try again with a 6.3 docker as 6.4 seems a bit too new for other libraries.
I bet i'll get issues now of version being too old...

Good thing i don't have a datacap... Just the docker image is ~22GB. Installing everything is another easy 10. Then running (with these models) is another easy 15... 

### markg85 · 2025-05-06

So, i got it working

![Image](https://github.com/user-attachments/assets/3f41ab72-5a49-4c43-ad7f-28cb1bd9c4fa)

... That was supposed to be a middle finger to rocm btw ;) ....

I did get version issues.

cmake and ninja needed to be updated (aka, just installed and the rocm image provided one just removed). Then there was some weird python package stuff, it boiled rown to removing `rocket` and reinstalling it with the newer version.

I did still use your bitsandbytes @xzuyn, nothing else seemed to work otherwise.

### DGdev91 · 2025-06-09

> This setup works for me. I tried other versions and they have different issues.
> 
> ```
> pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.2
> pip install --no-deps --force-reinstall 'https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.45.1.dev0-py3-none-manylinux_2_24_x86_64.whl'
> ```

This used to work for me too, but unfortunatley that 0.45.1 wheel got deleted. the only one currently available seems to be this one:

https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-1.0.0-py3-none-manylinux_2_24_x86_64.whl

.....Wich gives me this:
`undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi`

### matthewwang16czap · 2025-06-12

> > This setup works for me. I tried other versions and they have different issues.
> > ```
> > pip install --force-reinstall pytorch-triton-rocm==3.1.0 --index-url https://download.pytorch.org/whl/nightly/rocm6.2
> > pip install --no-deps --force-reinstall 'https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.45.1.dev0-py3-none-manylinux_2_24_x86_64.whl'
> > ```
> 
> This used to work for me too, but unfortunatley that 0.45.1 wheel got deleted. the only one currently available seems to be this one:
> 
> https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-1.0.0-py3-none-manylinux_2_24_x86_64.whl
> 
> .....Wich gives me this: `undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi`

<del>I recently updated to rocm 6.4 and following this guide to install bitsandbytes from source works for my 7900xtx: 
https://huggingface.co/docs/bitsandbytes/en/installation</del>
Update, won't work. 

### TotallyTroll · 2025-06-16

> I recently updated to rocm 6.4 and following this guide to install bitsandbytes from source works for my 7900xtx: https://huggingface.co/docs/bitsandbytes/en/installation

Can you share full venv preparation steps? Since for me it doesn't work for both rocm 6.3 and 6.4. I have same GPU.
Running `python -m bitsandbytes` always complains that can't load bitsandbytes lib:
```
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
Couldn't load the bitsandbytes library, likely due to missing binaries.
Please ensure bitsandbytes is properly installed.
```


### matthewwang16czap · 2025-06-17

> > I recently updated to rocm 6.4 and following this guide to install bitsandbytes from source works for my 7900xtx: https://huggingface.co/docs/bitsandbytes/en/installation
> 
> Can you share full venv preparation steps? Since for me it doesn't work for both rocm 6.3 and 6.4. I have same GPU. Running `python -m bitsandbytes` always complains that can't load bitsandbytes lib:
> 
> ```
> ++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> Checking that the library is importable and ROCm is callable...
> Couldn't load the bitsandbytes library, likely due to missing binaries.
> Please ensure bitsandbytes is properly installed.
> ```

My fault, it doesn't work. It appears we have to wait for official support.

### jbelof · 2025-07-04

i'm on ROCm 6.4 and targetting gfx942, and getting same exact issue
```
OSError: /tmp/bitsandbytes/bitsandbytes/libbitsandbytes_rocm64.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi
```

any updates?


### cornpo · 2025-07-05

There was a working wheel. But now it's deleted? Who deleted it? Jensen Huang?

I'm so fucking over bitsandbytes. Years and years and years of this bullshit...

### markg85 · 2025-07-06

> There was a working wheel. But now it's deleted? Who deleted it? Jensen Huang?
> 
> I'm so fucking over bitsandbytes. Years and years and years of this bullshit...

Yeah, it sucks hard.
I do sometimes get it working with many many many hours of pain and trying a plethora of different branches and comment suggestion. This (from [above](https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1519#issuecomment-2849725956)) perhaps still works.

AMD keeps getting broken over and over again unfortunately.
What doesn't help one fucking bit (pun intended) is that AMD itself is really doing the best it can to make it as unclear and difficult as possible. Because hey, let's fork [bitsandbytes](https://github.com/ROCm/bitsandbytes) which they have done. And that is then partially upstream here, partially not... Then you have articles referring to either of these repos. Yeah, nice job AMD, it's a mess and us people using AMD cards just have to live through the pain if we want to use this mess for image generation.

What doesn't help either is all these "nice" AI tools you can install with pyhon assume essentially nvidia. Or they assume old versions. Or they don't even give you the option and are "user friendly" by choosing everything themselves in code internally. All of these options work wonderfully for nvidia. And thoroughly break your AMD setup because now your installed packages are fucked up and you have to redo it and pick the manual route.

### xzuyn · 2025-07-06

i tried to make some wheels for `multi-backend-refactor-a0a95fd-hacky-fix`, idk if it helps anyone

https://github.com/xzuyn/bitsandbytes/releases/tag/wheels

### DGdev91 · 2025-07-10

> i tried to make some wheels for `multi-backend-refactor-a0a95fd-hacky-fix`, idk if it helps anyone
> 
> https://github.com/xzuyn/bitsandbytes/releases/tag/wheels

Thanks, seems it's working fine.
It currently requires pytorch nightly since it's compiled on rocm6.4, usually the official build have the binaries for multiple rocm version. still nice to have a working wheel, thanks.

### jwkirchenbauer · 2025-08-27

> [@markg85](https://github.com/markg85) Try this. It uses the old recommended `a0a95fd` commit, and replaces `int8_matmul_mixed_dequantize.py` and `int8_matmul_rowwise_dequantize.py` with dummy code which I found on an issue page to fix the `ModuleNotFoundError: No module named 'triton.ops'` problem.
> 
> git clone -b multi-backend-refactor-a0a95fd-hacky-fix https://github.com/xzuyn/bitsandbytes.git
> cd bitsandbytes
> cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="gfx1100" -S .  # change "gfx1100" to what you need
> make
> pip install .
> > python -m bitsandbytes
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> ++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> ++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
> ROCm specs: rocm_version_string='63', rocm_version_tuple=(6, 3)
> PyTorch settings found: ROCM_VERSION=63
> The directory listed in your path is found to be non-existent: local/JOHN-V4
> The directory listed in your path is found to be non-existent: @/tmp/.ICE-unix/3021,unix/JOHN-V4
> The directory listed in your path is found to be non-existent: /etc/xdg/xdg-ubuntu
> The directory listed in your path is found to be non-existent: /org/gnome/Terminal/screen/f0f7a6d2_eb6d_4c72_aaf5_c516b27d3f8e
> The directory listed in your path is found to be non-existent: /home/xzuyn/.cache/dotnet_bundle_extract
> The directory listed in your path is found to be non-existent: path=/run/user/1000/bus,guid=b63035f21f12b618d0dd60d86817e791
> The directory listed in your path is found to be non-existent: //debuginfod.ubuntu.com 
> WARNING! ROCm runtime files not found in any environmental path.
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> ++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> Checking that the library is importable and ROCm is callable...
> SUCCESS!
> Installation was successful!
> I checked with latest PyTorch stuff (`pip install --pre torch torchvision pytorch-triton-rocm --index-url https://download.pytorch.org/whl/nightly/rocm6.3`), but probably works with older versions as I remember doing this same fix months ago too.

This also was the only solution for me just now, thanks @xzuyn!


The system is a 4xMI300A machine, and I am running
```
pip install torch==2.8.0+rocm6.3 --index-url https://download.pytorch.org/whl/rocm6.3
```
to install the recent stable 2.8 for rocm 6.3. The gpu target is `gfx942` so I changed that in the cmake command
```
cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="gfx942" -S .
```
(note @jbelof perhaps this can help you)

### xzuyn · 2025-09-06

Using the main branch seems to be working. Probably no need for `multi-backend-refactor-a0a95fd-hacky-fix` anymore.
```
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes
cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="gfx1100" -S .  # change "gfx1100" to what you need
make
pip install .
```

```
> python -m bitsandbytes
================ bitsandbytes v0.48.0.dev0 =================
Platform: Linux-6.8.0-79-generic-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.12.3
PyTorch: 2.9.0.dev20250811+rocm6.4
  CUDA: N/A
  HIP: 6.4.43484-123eb5128
  XPU: N/A
Related packages:
  accelerate: 1.6.0
  diffusers: 0.32.1
  numpy: 2.3.1
  pip: 25.2
  peft: not found
  safetensors: 0.4.5
  transformers: 4.54.1
  triton: not found
  trl: not found
============================================================
PyTorch settings found: ROCM_VERSION=64
Checking that the library is importable and ROCm is callable...
SUCCESS!
```

---

Actually it seems *slightly* broken. I get `RuntimeError: Configured ROCm binary not found at .../venv/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm63.so` in one of my venvs. Going in there and doing `ln -s libbitsandbytes_rocm64.so libbitsandbytes_rocm63.so` seems to solve it though.

### ashwinma · 2026-02-03

This issue seems to have been fixed in the latest version of bitsandbytes and installable from PyPI

https://huggingface.co/docs/bitsandbytes/main/en/installation#rocm-pip

`pip install bitsandbytes`

### matthewdouglas · 2026-02-24

Hi all,

Since we started shipping ROCm binaries with the PyPI release in v0.49.0, I'm going to close this issue. It also looks like there are multiple different issues discussed here. If there are still problems with the latest release, please open a new issue. Thanks!
