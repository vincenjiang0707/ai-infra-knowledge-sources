# [Issue #2580] ROCM + triton build broken

source: https://github.com/Dao-AILab/flash-attention/issues/2580
state: closed | updated: 2026-06-12T10:48:02Z
labels: 

## 正文

I'm trying to build in a new venv with the instructions from the README but the build is not working when it tries to build _aiter_.

```sh
cd flash-attention
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" pip install --no-build-isolation .
```

**output**
```
INFO: pip is looking at multiple versions of amd-aiter to determine which version is compatible with other requirements. This could take a while.
ERROR: Could not find a version that satisfies the requirement flydsl==0.1.1.dev409 (from amd-aiter) (from versions: 0.1.5.dev515, 0.1.5, 0.1.6.dev529, 0.1.6, 0.1.7.dev551, 0.1.7, 0.1.8.dev574, 0.1.8)
ERROR: No matching distribution found for flydsl==0.1.1.dev409
```

Any ideas how I should get (or opt out of) `flydsl` or otherwise get the build to work? cc @micmelesse 

I'm using python3.13 on Arch Linux.

Resolved by #2540

## 评论 (14)

### micmelesse · 2026-05-21

@alexheretic Can you try this pr, https://github.com/Dao-AILab/flash-attention/pull/2540? It should fix this

### alexheretic · 2026-05-21

Thanks @micmelesse that helps!

The build works now, though does output a warning/error for me due to triton: (But this seems ok to ignore).
```
    WARNING: Skipping triton as it is not installed.
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torch 2.12.0a0+rocm7.13.0a20260416 requires triton==3.7.0+gitfe493743.rocm7.13.0a20260416, but you have triton 3.5.1 which is incompatible.
```

I think we can close when #2540 is merged.

### alexheretic · 2026-05-21

> But this seems ok to ignore

Maybe not, as now I try to use it (e.g. startup comfyui) I get a failure: `[aiter] failed jit build [module_aiter_core]`.

<details>
  <summary>stderr</summary>

```
[aiter] [pid=2639762 pname=MainProcess] start build [module_aiter_core] under /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core
[aiter] Current hipcc not support: -mllvm -amdgpu-coerce-illegal-types=1, skip it.
[aiter] ^[[31mfailed jit build [module_aiter_core]^[[0m↓↓↓↓↓↓↓↓↓↓
-->[History]: Traceback (most recent call last):
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 1431, in wrapper
    module = get_module(md)
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 588, in get_module
    get_module_custom_op(md_name)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 288, in wrapper_custom
    else getattr(torch.ops.aiter, f"{loadName}")(
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        torch.empty(1, device=device), *args, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/torch/_ops.py", line 1275, in __call__
    return self._op(*args, **kwargs)
           ~~~~~~~~^^^^^^^^^^^^^^^^^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 326, in outer_wrapper_dummy
    wrapper(*args, **kwargs)
    ~~~~~~~^^^^^^^^^^^^^^^^^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 204, in wrapper
    return func(*args, **kwargs)
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 580, in get_module_custom_op
    __mds[md_name] = importlib.import_module(f"{__package__}.{md_name}")
                     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-->  File "/usr/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-->  File "<frozen importlib._bootstrap>", line 1395, in _gcd_import
-->  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
-->  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
-->ModuleNotFound^[[31merror:^[[0m No module named 'aiter.jit.module_aiter_core'
-->
During handling of the above exception, another exception occurred:

-->Traceback (most recent call last):
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1477, in _run_ninja_build
    subprocess.run(
    ~~~~~~~~~~~~~~^
        command,
        ^^^^^^^^
    ...<4 lines>...
        env=env,
        ^^^^^^^^
    )
    ^
-->  File "/usr/lib/python3.13/subprocess.py", line 577, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
-->subprocess.CalledProcess^[[31merror:^[[0m Command '['ninja', '-v', '-j', '12']' returned non-zero exit status 1.
-->
The above exception was the direct cause of the following exception:

-->Traceback (most recent call last):
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 907, in MainFunc
    _jit_compile(
    ~~~~~~~~~~~~^
        md_name,
        ^^^^^^^^
    ...<11 lines>...
        hipify=hipify,
        ^^^^^^^^^^^^^^
    )
    ^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1226, in _jit_compile
    _write_ninja_file_and_build_library(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        name=name,
        ^^^^^^^^^^
    ...<10 lines>...
        torch_exclude=torch_exclude,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1352, in _write_ninja_file_and_build_library
    _run_ninja_build(
    ~~~~~~~~~~~~~~~~^
        build_directory, verbose, error_prefix=f"Error building extension '{name}'"
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
-->  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1494, in _run_ninja_build
    raise RuntimeError(message) from e
-->Runtime^[[31merror:^[[0m Error building extension 'module_aiter_core': [1/2] /home/alex2/ComfyUI/venv-p313-gfx110X-2/bin/hipcc  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden --offload-arch=native -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o aiter_core_pybind.cuda.o 
FAILED: [code=1] aiter_core_pybind.cuda.o 
/home/alex2/ComfyUI/venv-p313-gfx110X-2/bin/hipcc  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden --offload-arch=native -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o aiter_core_pybind.cuda.o 
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu:3:
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/rocm_ops.hpp:5:
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/aiter_tensor.h:4:
/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/aiter_hip_common.h:12:10: fatal ^[[31merror:^[[0m 'ck_tile/core.hpp' file not found
   12 | #include "ck_tile/core.hpp"
      |          ^~~~~~~~~~~~~~~~~~
1 error generated when compiling for gfx1100.
failed to execute:/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/_rocm_sdk_core/lib/llvm/bin/clang++  --offload-arch=native  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c -x hip /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o "aiter_core_pybind.cuda.o"
ninja: build stopped: subcommand failed.

^[[31mfailed jit build [module_aiter_core]^[[0m↑↑↑↑↑↑↑↑↑↑
[aiter] [pid=2639762 pname=MainProcess] ^[[32mfinish build [module_aiter_core], cost 6.4s ^[[0m
Traceback (most recent call last):
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 1431, in wrapper
    module = get_module(md)
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 588, in get_module
    get_module_custom_op(md_name)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 288, in wrapper_custom
    else getattr(torch.ops.aiter, f"{loadName}")(
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        torch.empty(1, device=device), *args, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/torch/_ops.py", line 1275, in __call__
    return self._op(*args, **kwargs)
           ~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 326, in outer_wrapper_dummy
    wrapper(*args, **kwargs)
    ~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 204, in wrapper
    return func(*args, **kwargs)
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 580, in get_module_custom_op
    __mds[md_name] = importlib.import_module(f"{__package__}.{md_name}")
                     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1395, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'aiter.jit.module_aiter_core'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1477, in _run_ninja_build
    subprocess.run(
    ~~~~~~~~~~~~~~^
        command,
        ^^^^^^^^
    ...<4 lines>...
        env=env,
        ^^^^^^^^
    )
    ^
  File "/usr/lib/python3.13/subprocess.py", line 577, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['ninja', '-v', '-j', '12']' returned non-zero exit status 1.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 907, in MainFunc
    _jit_compile(
    ~~~~~~~~~~~~^
        md_name,
        ^^^^^^^^
    ...<11 lines>...
        hipify=hipify,
        ^^^^^^^^^^^^^^
    )
    ^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1226, in _jit_compile
    _write_ninja_file_and_build_library(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        name=name,
        ^^^^^^^^^^
    ...<10 lines>...
        torch_exclude=torch_exclude,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1352, in _write_ninja_file_and_build_library
    _run_ninja_build(
    ~~~~~~~~~~~~~~~~^
        build_directory, verbose, error_prefix=f"Error building extension '{name}'"
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/cpp_extension.py", line 1494, in _run_ninja_build
    raise RuntimeError(message) from e
RuntimeError: Error building extension 'module_aiter_core': [1/2] /home/alex2/ComfyUI/venv-p313-gfx110X-2/bin/hipcc  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden --offload-arch=native -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o aiter_core_pybind.cuda.o 
FAILED: [code=1] aiter_core_pybind.cuda.o 
/home/alex2/ComfyUI/venv-p313-gfx110X-2/bin/hipcc  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden --offload-arch=native -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o aiter_core_pybind.cuda.o 
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu:3:
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/rocm_ops.hpp:5:
In file included from /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/aiter_tensor.h:4:
/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include/aiter_hip_common.h:12:10: fatal error: 'ck_tile/core.hpp' file not found
   12 | #include "ck_tile/core.hpp"
      |          ^~~~~~~~~~~~~~~~~~
1 error generated when compiling for gfx1100.
failed to execute:/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/_rocm_sdk_core/lib/llvm/bin/clang++  --offload-arch=native  -DWITH_HIP -D_GLIBCXX_USE_CXX11_ABI=1 -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/include -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/blob -I/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/pybind11/include -isystem /usr/include/python3.13 -fPIC -std=c++20 -O3 -std=c++20 -Wno-unknown-warning-option -DENABLE_CK=1 -DENABLE_ROPE_POSITIONS_INT32=0 -DAITER_CK_FREE=1 -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF_CONVERSIONS__=1 -mcmodel=large -fno-unique-section-names -ffunction-sections -fdata-sections -fvisibility=hidden -fvisibility-inlines-hidden -DDLLVM_MAIN_REVISION=554784 -DENABLE_ROPE_POSITIONS_INT32=0 -DLEGACY_HIPBLAS_DIRECT -DUSE_PROF_API=1 -D__Float4_e2m1fn_x2 -D__HIP_PLATFORM_AMD__=1 -D__HIP_PLATFORM_HCC__=1 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Wno-macro-redefined -Wno-missing-template-arg-list-after-template-kw -Wno-switch-bool -Wno-undefined-func-template -Wno-unused-result -Wno-vla-cxx-extension -fgpu-flush-denormals-to-zero -fno-offload-uniform-block -mllvm --amdgpu-kernarg-preload-count=16 -mllvm --lsr-drop-solution=1 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -mllvm -enable-post-misched=0 -fno-gpu-rdc -c -x hip /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter_meta/csrc/pybind/aiter_core_pybind.cu -o "aiter_core_pybind.cuda.o"
ninja: build stopped: subcommand failed.


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/alex2/ComfyUI/main.py", line 206, in <module>
    import execution
  File "/home/alex2/ComfyUI/execution.py", line 22, in <module>
    from latent_preview import set_preview_method
  File "/home/alex2/ComfyUI/latent_preview.py", line 5, in <module>
    from comfy.sd import VAE
  File "/home/alex2/ComfyUI/comfy/sd.py", line 13, in <module>
    import comfy.ldm.genmo.vae.model
  File "/home/alex2/ComfyUI/comfy/ldm/genmo/vae/model.py", line 13, in <module>
    from comfy.ldm.modules.attention import optimized_attention
  File "/home/alex2/ComfyUI/comfy/ldm/modules/attention.py", line 44, in <module>
    from flash_attn import flash_attn_func
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/flash_attn/__init__.py", line 8, in <module>
    from flash_attn.flash_attn_interface import (
    ...<7 lines>...
    )
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/flash_attn/flash_attn_interface.py", line 21, in <module>
    from aiter.ops.triton._triton_kernels.flash_attn_triton_amd import flash_attn_2 as flash_attn_gpu
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/__init__.py", line 79, in <module>
    from .utility import dtypes as dtypes  # noqa: E402
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/utility/dtypes.py", line 5, in <module>
    from ..ops.enum import QuantType, ActivationType
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/ops/enum.py", line 15, in <module>
    ActivationType = type(_ActivationType(0))
                          ~~~~~~~~~~~~~~~^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/utils/torch_guard.py", line 204, in wrapper
    return func(*args, **kwargs)
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 1661, in custom_wrapper
    return wrapper(*args, **kwargs)
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 1456, in wrapper
    build_module(
    ~~~~~~~~~~~~^
        md_name,
        ^^^^^^^^
    ...<11 lines>...
        hipify,
        ^^^^^^^
    )
    ^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 950, in build_module
    mp_lock(lockPath=lock_path, MainFunc=MainFunc, FinalFunc=FinalFunc)
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 58, in mp_lock
    ret = MainFunc()
  File "/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/core.py", line 940, in MainFunc
    raise RuntimeError(
        f"[aiter] build [{md_name}] under {opbd_dir} failed !!!!!!"
    ) from e
RuntimeError: [aiter] build [module_aiter_core] under /home/alex2/ComfyUI/venv-p313-gfx110X-2/lib/python3.13/site-packages/aiter/jit/build/module_aiter_core/build failed !!!!!!
```

</details>

### micmelesse · 2026-05-22

@alexheretic Can you try putting `export ENABLE_CK=0` before launching. Also can you tell me your config?

### alexheretic · 2026-05-23

With `ENABLE_CK=0` it still fails in a somewhat similar way, but with:

```
-->Runtime^[[31merror:^[[0m Error building extension 'module_aiter_core': [1/1] c++ @module_aiter_core.so.rsp -shared -mcmodel=large -ffunction-sections -fdata-sections -Wl,--gc-sections -Wl,--cref -L/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib -lamdhip64 -o module_aiter_core.so
FAILED: [code=1] module_aiter_core.so
c++ @module_aiter_core.so.rsp -shared -mcmodel=large -ffunction-sections -fdata-sections -Wl,--gc-sections -Wl,--cref -L/home/alex2/ComfyUI/venv-p313-gfx110X-2/lib -lamdhip64 -o module_aiter_core.so
/usr/bin/ld: cannot find -lamdhip64: No such file or directory
collect2: ^[[31merror:^[[0m ld returned 1 exit status
```

### alexheretic · 2026-05-23

My config is a fresh python3.13 venv setup for comfyui. I documented it [here](https://gist.github.com/alexheretic/d868b340d1cef8664e1b4226fd17e0d0). 

So I'm installing torch with `pip install --pre torch torchvision torchaudio --index-url https://rocm.nightlies.amd.com/v2/gfx110X-all/`. 

### micmelesse · 2026-05-26

Can you try this dockerfile?


```
FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install ninja pybind11 packaging \
    && pip install --pre torch --index-url https://rocm.nightlies.amd.com/v2/gfx110X-all/ \
    && pip install amd-aiter

# Fix link
ENV ROCM_LIB=/usr/local/lib/python3.13/site-packages/_rocm_sdk_core/lib
RUN ln -sf "$ROCM_LIB"/libamdhip64.so.* "$ROCM_LIB/libamdhip64.so"

ENV ENABLE_CK=0
ENV LIBRARY_PATH=$ROCM_LIB
ENV LD_LIBRARY_PATH=$ROCM_LIB

RUN python -c "import aiter; from aiter.ops.enum import ActivationType; print('aiter JIT OK')"
```

### alexheretic · 2026-05-28

Yes that works, thanks. I can also do this in a venv.

When I install flash-attn it unfortunately re-installs triton to 3.5.0 which breaks aiter again. But re-running: `pip install --pre torch --index-url https://rocm.nightlies.amd.com/v2/gfx110X-all/` puts triton back to `3.7.0+gitfe493743.rocm7.13.0a20260416` and this seems to work.

I've tested comfy sdxl & wan generations successfully. There are some perf regressions compared to my older venv, pre-aiter (something like wan ~17s/it -> 24s/it). However, these may be due to other factors. Overall the workarounds seem good.

Of course it isn't great to have to manually link libs like this, is there a path to not needing these workarounds? 

### alexheretic · 2026-05-28

Actually perf seems around the same as before now 👍 I've documented the workaround for venv installs [here](https://gist.github.com/alexheretic/d868b340d1cef8664e1b4226fd17e0d0#issuesworkarounds).

Thanks for the help!

### micmelesse · 2026-06-01

@alexheretic, [this PR](https://github.com/Dao-AILab/flash-attention/pull/2614) should simplify things. The standard install should work now. Try `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" pip install --no-build-isolation .` 

### alexheretic · 2026-06-02

Thanks, I'll re-test when I get a sec!

### micmelesse · 2026-06-02

Hey @alexheretic , I am planning a small follow-up to #2614 that drops the auto-set `AITER_TRITON_ONLY=1` in FA's `setup.py`. It might affect other users in uninteded ways. You will need to set `AITER_TRITON_ONLY=1` in your shell yourself before installing FA. If you are on windows it is automatically set to triton only mode. Sorry about that. 

### micmelesse · 2026-06-02

This is the pr. https://github.com/Dao-AILab/flash-attention/pull/2620

### alexheretic · 2026-06-12

Thanks, I've retested and the lib symlinking step is no longer necessary 👍 

Installing no longer complains about triton version, however it does still re-install triton so I still had to re-install triton from the rocm gfx110X-all repo after installing flash-attn.

`AITER_TRITON_ONLY=1` replaces `ENABLE_CK`, and this seems clearer 👍 It may be worth adding info about this to the amd readme section?
