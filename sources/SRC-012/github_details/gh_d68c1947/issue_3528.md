# [Issue #3528] [Bug] AttributeError: module 'tvm.ir._ffi_api' has no attribute 'RegisterOpAttr' when running mlc_llm serve -h

source: https://github.com/mlc-ai/mlc-llm/issues/3528
state: open | updated: 2026-09-11T09:05:49Z
labels: bug

## 正文

## 🐛 Bug

The `mlc_llm serve -h` command fails with an `AttributeError: module 'tvm.ir._ffi_api' has no attribute 'RegisterOpAttr'` during module import. The error occurs when trying to register gradient operations in the TVM Relax module.

## To Reproduce

Steps to reproduce the behavior:
1. Follow the official [docs](https://llm.mlc.ai/docs/install/mlc_llm.html#option-1-prebuilt-package) and install via `python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu`
2. Navigate to the MLC-LLM project directory
3. Run the command: `python -m mlc_llm serve -h`
4. Observe the traceback error

Error message:
```
Traceback (most recent call last):
  File "<frozen runpy>", line 194, in _run_module_as_main
  File "<frozen runpy>", line 151, in _get_module_details
  File "<frozen runpy>", line 114, in _get_module_details
  File "/Users/ferdem/Projects/mlc-llm/python/mlc_llm/__init__.py", line 8, in <module>
    from . import protocol, serve
  File "/Users/ferdem/Projects/mlc-llm/python/mlc_llm/serve/__init__.py", line 7, in <module>
    from .embedding_engine import AsyncEmbeddingEngine
  File "/Users/ferdem/Projects/mlc-llm/python/mlc_llm/serve/embedding_engine.py", line 11, in <module>
    from tvm import relax
  File "/Users/ferdem/Projects/mlc-llm/3rdparty/tvm/python/tvm/relax/__init__.py", line 68, in <module>
    from .op.base import (
    ...<5 lines>...
    )
  File "/Users/ferdem/Projects/mlc-llm/3rdparty/tvm/python/tvm/relax/op/__init__.py", line 22, in <module>
    from . import _op_gradient, builtin, ccl, distributed, grad, image, memory, nn, op_attrs
  File "/Users/ferdem/Projects/mlc-llm/3rdparty/tvm/python/tvm/relax/op/_op_gradient.py", line 128, in <module>
    @register_gradient("relax.add")
     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/ferdem/Projects/mlc-llm/3rdparty/tvm/python/tvm/ir/op.py", line 186, in _register
    _ffi_api.RegisterOpAttr(op_name, attr_key, v, level)
    ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'tvm.ir._ffi_api' has no attribute 'RegisterOpAttr'
```

## Expected behavior

The `python -m mlc_llm serve -h` command should display help information about the MLC-LLM serve module without any errors.

## Environment

 - Platform: Metal (hardware-accelerated backend)
 - Operating system: MacOS 15.7.4
 - Device: Macbook Air M4
 - How you installed MLC-LLM: source (from local build)
 - How you installed TVM: source (via pip, built from 3rdparty/tvm)
 - Python version: 3.13
 - GPU driver version: N/A (Apple Silicon)
 - CUDA/cuDNN version: N/A
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`):

```
USE_CUDA: ON
USE_LLVM: ON
USE_NCCL: ON
USE_NVTX: ON
USE_NVSHMEM: OFF
USE_HEXAGON: OFF
USE_CUDNN: OFF
USE_CUTLASS: OFF
USE_VULKAN: OFF
USE_OPENCL: OFF
USE_METAL: OFF
USE_ROCM: OFF
USE_CLML: OFF
USE_NNAPI_RUNTIME: OFF
USE_NNAPI_CODEGEN: OFF
```

## Additional context

- The issue appears to be related to TVM's `_ffi_api.RegisterOpAttr` not being available in the current TVM build
- The error occurs when trying to register gradient operations for Relax operators
- This might be due to a version mismatch between MLC-LLM and the TVM submodule, or incomplete TVM compilation
- The TVM build shows `USE_METAL: OFF` despite being on an M4 Mac, which might be relevant for Metal support
- Possible causes:
  - TVM was built without necessary gradient support flags
  - The TVM submodule version is outdated or incompatible with the current MLC-LLM version
  - Python 3.13 might have compatibility issues with the TVM FFI interface
- Consider rebuilding TVM with proper configuration flags for the target platform

## 评论 (2)

### adityaanikam · 2026-08-15

Checked the actual pinned commit rather than guessing, 3rdparty/tvm is submoduled from mlc-ai/relax at 837cb9d, and at that exact commit, ir.RegisterOpAttr is registered in src/ir/op.cc, and op.py looks it up the standard way through _ffi_api. So the registration genuinely exists in source at the commit your build is pointed at.

That points away from a source level gap and toward your actual compiled libtvm not matching that source tree, a stale build, a partial rebuild that didn't pick up this registration, or a different checked out commit than what .gitmodules shows. Worth confirming with a clean submodule checkout and full rebuild before this gets treated as a code bug, since I can't find anything in the pinned source that would produce the error you're seeing.


### azhuvath · 2026-09-11

I am facing this same problem in a Windows machine. Steps followed.

# Create Environment & Install Relevant Packages
py -3.12 -m venv .venv312
.venv312\Scripts\activate

python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu

# Verification
python -c "import tvm.relax; print('TVM Relax: OK')"
python -c "import mlc_llm; print('MLC LLM: OK')"

# What is installed
pip list | findstr /I "mlc tvm"

apache-tvm-ffi      0.1.14rc4
mlc-ai-nightly-cpu  0.26.dev246
mlc-llm-nightly-cpu 0.26.dev6
