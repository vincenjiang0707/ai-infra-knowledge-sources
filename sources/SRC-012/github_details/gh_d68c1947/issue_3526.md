# [Issue #3526] [Bug] MLC-LLM CLI Crashes with malloc Error on macOS after Source Build

source: https://github.com/mlc-ai/mlc-llm/issues/3526
state: open | updated: 2026-07-26T15:49:22Z
labels: bug

## 正文

## 🐛 Bug

Cannot execute `python -m mlc_llm serve -h` or any other MLC-LLM CLI commands after building from source on macOS with Metal support. The process crashes with a memory allocation error during import.

## To Reproduce

Steps to reproduce the behavior:

1. Build MLC-LLM from source on macOS with Metal support:
   ```bash
   # Configure build
   cd mlc-llm
   mkdir -p build && cd build
   python ../cmake/gen_cmake_config.py
   # Select Metal, disable CUDA/ROCm/Vulkan/OpenCL
   cmake ..
   make -j 10
   ```

2. Set up environment variables:
   ```bash
   export MLC_LLM_SOURCE_DIR=$PWD
   export PYTHONPATH=$MLC_LLM_SOURCE_DIR/python:$PYTHONPATH
   export PYTHONPATH=$PWD/3rdparty/tvm/python:$PYTHONPATH
   export DYLD_LIBRARY_PATH="$PWD/build/lib:$DYLD_LIBRARY_PATH"
   ```

3. Install required packages:
   ```bash
   pip install apache-tvm-ffi numpy
   ```

4. Attempt to run any MLC-LLM command:
   ```bash
   python -m mlc_llm -h
   python -m mlc_llm serve -h
   ```

5. Observe the crash with malloc error:
   ```
   python(xxxxx,0x20bb3a240) malloc: *** error for object 0x600001720008: pointer being freed was not allocated
   python(xxxxx,0x20bb3a240) malloc: *** set a breakpoint in malloc_error_break to debug
   zsh: abort      python -m mlc_llm -h
   ```

## Expected behavior

MLC-LLM CLI should display help information or start properly without crashing. The import of the `mlc_llm` module should complete successfully, and the command-line interface should be functional.

## Environment

- **Platform**: Metal (Apple M4)
- **Operating system**: macOS 15.7.4
- **Device**: Macbook Air M4
- **MLC-LLM Installation**: Source (branch: main, v0.20.0.dev0)
- **Python Installation**: miniconda (conda environment: mlc-build)
- **Python version**: 3.13.14
- **TVM Installation**: Source (`mlc-llm/3rdparty/tvm`, commit hash: 837cb9de1127b48ce48e4cefe09e83215b9d4ba7)
- **TVM-FFI**: apache-tvm-ffi 0.1.12 (installed via pip)
- **Compiler**: AppleClang 17.0.0.17000013
- **CMake**: Build configured with `USE_METAL ON`, other GPU backends disabled

## Additional context

### Build Output Summary
- Successfully built with `make -j 10`
- Produced libraries: `libtvm_runtime.dylib`, `libtvm_ffi.dylib`, `libmlc_llm.dylib`
- Build warnings: 
  - `Cannot find libflash_attn`
  - Version mismatch warnings for tokenizers_c.a (built for macOS 15.5 vs linked for 15.0)
  - Unused private field warning in `paged_kv_cache.cc`

### Diagnostic Steps Performed

1. **TVM import test** initially failed with missing `tvm_ffi` module (resolved by `pip install apache-tvm-ffi`)

2. **TVM import test** then failed with missing `numpy` (resolved by `pip install numpy`)

3. **TVM import test** succeeded after all dependencies installed:
   ```bash
   python -c "import tvm; print(tvm.support.libinfo())"
   ```
   Output shows TVM detected the environment and libraries correctly.

4. **MLC-LLM import** fails with malloc corruption during module initialization.

### Potential Root Causes
1. **ABI/Symbol mismatch**: The MLC-LLM build process may be producing binaries with different compilation flags than the Python bindings expect, or there may be version mismatches between the compiled libraries and the Python wrapper.

2. **Double-free or memory corruption**: The `pointer being freed was not allocated` error suggests that the C++ runtime is attempting to free memory that was either:
   - Already freed
   - Not allocated by malloc
   - Corrupted heap

3. **Library loading order**: Multiple dynamic libraries may be loading conflicting versions of symbols, especially given the libbacktrace dependency and the various `tvm_ffi` components.

4. **Missing `tvm_ffi` library path**: The build produces `libtvm_ffi.dylib` in `build/lib`, but this directory may not be properly registered with the runtime loader despite `DYLD_LIBRARY_PATH` being set. The `tvm_ffi` Python package from PyPI might conflict with the built version.

5. **Python/C++ interface mismatch**: Python 3.13.14 might have ABI differences that cause memory management issues with the compiled C++ code.

### Additional Notes
- The error occurs only when importing the full `mlc_llm` package, not when importing `tvm` alone
- The crash happens consistently for all `mlc_llm` subcommands
- The `malloc` error suggests the issue is in the C++ layer rather than pure Python

### Workarounds Attempted
- Installed `apache-tvm-ffi` (resolved initial import issues)
- Installed `numpy` (resolved TVM import issues)
- Set `DYLD_LIBRARY_PATH` (resolved library discovery)
- Still crashes on MLC-LLM import

## 评论 (1)

### scottorly · 2026-07-26

+1
