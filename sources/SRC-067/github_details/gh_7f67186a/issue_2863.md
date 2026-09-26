# [Issue #2863] CUDA build uses C++17 but PyTorch 2.13+ requires C++20

source: https://github.com/Dao-AILab/flash-attention/issues/2863
state: closed | updated: 2026-09-16T16:39:37Z
labels: 

## 正文

## Summary

The NVIDIA CUDA build in the current FlashAttention source explicitly passes
`-std=c++17` to both the host compiler and NVCC.

PyTorch 2.13 and newer require C++20 for extensions that include PyTorch/ATen
headers. When attempting to build FlashAttention against PyTorch 2.14 using the
existing C++17 configuration, the build encountered the PyTorch C++ standard
requirement:

```text
#error C++20 or later compatible compiler is required to use ATen
```

I changed the two NVIDIA build flags from C++17 to C++20. After this change,
FlashAttention 2.8.4 built and installed successfully against PyTorch
2.14.0+cu132.

No FlashAttention kernel implementation or mathematical behavior was modified.

## Environment

```text
Operating system: Linux x86_64
Python: 3.13
PyTorch: 2.14.0+cu132
CUDA runtime used by PyTorch: 13.2
CUDA toolkit / NVCC: 13.2
GPU: NVIDIA GeForce RTX 5090
Compute capability: 12.0
Compilation target: SM120
FlashAttention version: 2.8.4 from the current main branch
Build system: Ninja
```

## Current configuration

The NVIDIA build currently contains C++17 flags for both compiler paths:

```python
nvcc_flags = [
    "-O3",
    "-std=c++17",
    ...
]

compiler_c17_flag = [
    "-O3",
    "-std=c++17",
]
```

Because the standard is specified explicitly, PyTorch's extension build
machinery cannot select C++20 automatically.

## Local modification

I changed both C++17 flags:

```diff
 nvcc_flags = [
     "-O3",
-    "-std=c++17",
+    "-std=c++20",
     ...
 ]

-compiler_c17_flag = ["-O3", "-std=c++17"]
+compiler_cxx_flag = ["-O3", "-std=c++20"]
```

For the experiment, the variable name did not need to be changed; only the two
flag values were modified.

## Build procedure

I cloned the repository and initialized the NVIDIA CUTLASS submodule:

```bash
git clone --depth 1 \
    https://github.com/Dao-AILab/flash-attention.git

cd flash-attention

git submodule update \
    --init \
    --depth 1 \
    csrc/cutlass
```

I then replaced the two C++17 flags with C++20 and built using:

```bash
export BUILD_TARGET=cuda
export FLASH_ATTENTION_FORCE_BUILD=TRUE
export FLASH_ATTN_CUDA_ARCHS=120
export MAX_JOBS=6
export NVCC_THREADS=2

python -m pip install \
    . \
    --no-build-isolation \
    --no-deps \
    --force-reinstall \
    --verbose
```

`FLASH_ATTENTION_FORCE_BUILD=TRUE` was used to ensure that the modified source
was compiled instead of downloading a prebuilt wheel.

`--no-deps` was used to prevent pip from replacing the existing PyTorch 2.14
installation.

## C++20 propagation

The generated build commands confirmed that C++20 was used by all relevant
compiler stages.

Host compiler:

```text
c++ ... -O3 -std=c++20 ...
```

CUDA compiler:

```text
nvcc ... -O3 -std=c++20 ...
```

CUDA device compiler:

```text
cicc --c++20 ...
```

SM120 code generation was also correctly selected:

```text
-gencode arch=compute_120f,code=sm_120
-gencode arch=compute_120,code=compute_120
```

## Result

The complete extension compiled and linked successfully:

```text
Building wheel for flash_attn (pyproject.toml): finished with status 'done'
Successfully built flash_attn
Successfully installed flash_attn-2.8.4
```

The generated extension was:

```text
flash_attn_2_cuda.cpython-313-x86_64-linux-gnu.so
```

The generated wheel was:

```text
flash_attn-2.8.4-cp313-cp313-linux_x86_64.whl
```

The extension was linked against the PyTorch 2.14 libraries in the active
environment, including:

```text
libc10
libtorch
libtorch_cpu
libtorch_python
libc10_cuda
libtorch_cuda
libcudart
```

This confirms that changing the host and NVCC flags to C++20 allows the complete
FlashAttention extension to build and install with PyTorch 2.14 and CUDA 13.2.

## Requested change

Could the NVIDIA CUDA build be updated to use C++20 when compiling against
PyTorch 2.13 or newer?

A version-dependent implementation could be:

```python
torch_version = tuple(
    int(component)
    for component in torch.__version__.split("+")[0].split(".")[:2]
)

requires_cxx20 = torch_version >= (2, 13)
cxx_standard = "c++20" if requires_cxx20 else "c++17"

nvcc_flags = [
    "-O3",
    f"-std={cxx_standard}",
    ...
]

compiler_cxx_flags = [
    "-O3",
    f"-std={cxx_standard}",
]
```


It may also be useful to:

1. Rename `compiler_c17_flag` to a version-neutral name.
2. Keep the host and NVCC C++ standards synchronized.
3. Add a source-build CI job for PyTorch 2.13 and 2.14.
4. Test CUDA 13.x and SM120 in that CI matrix when suitable hardware is
   available.

## Scope of this report

This report concerns source-build compatibility only.

It does not claim that changing C++17 to C++20 improves FlashAttention runtime
performance. The CUDA kernel implementation was not changed; only its
compilation standard was updated.

## 评论 (2)

### Johnsonms · 2026-09-06

Will take a look soon

### Johnsonms · 2026-09-16

Closed, as the code merge, Thanks @Kitsunp for catching up
