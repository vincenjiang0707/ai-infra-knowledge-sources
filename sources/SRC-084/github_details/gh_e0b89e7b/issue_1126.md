# [Issue #1126] Linux binaries should ship with appropriate RPATH

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1126
state: open | updated: 2026-07-24T17:43:26Z
labels: Medium Priority, Linux, Build

## 正文

### Feature request

Modify the build process for Linux to set an RPATH on the shared libraries to help locate the CUDA libraries in use by PyTorch. The goal is to make installation more painless.

Currently, the binaries have a RUNPATH based on the build system's configuration where the CUDA libraries are located at `/usr/local/cuda/lib64`:

```
$ readelf -d libbitsandbytes_cuda121.so

Dynamic section at offset 0x1937790 contains 33 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libcudart.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcublas.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcusparse.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcublasLt.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libm.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000e (SONAME)             Library soname: [libbitsandbytes_cuda121.so]
 0x000000000000001d (RUNPATH)            Library runpath: [/usr/local/cuda/lib64]
 ```
 
 Users may not necessarily have the appropriate CUDA Toolkit installed in this location, or even at all. Sometimes things work, and other times we have docs/error messages instructing to use `LD_LIBRARY_PATH` to try and resolve that. There's some extra work on top of that in the `CUDASetup` where additional paths from env are considered, e.g.`CONDA_PREFIX`, `CUDA_PATH`, and others.
 
 Instead, we should consider an RPATH using $ORIGIN, similar to PyTorch:
 
 ```$ readelf -d libtorch_cuda.so

Dynamic section at offset 0x303339f8 contains 46 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc10_cuda.so]
 0x0000000000000001 (NEEDED)             Shared library: [libcudart.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcusparse.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcufft.so.11]
 0x0000000000000001 (NEEDED)             Shared library: [libcusparseLt-f8b4a9fb.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libnvToolsExt.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libcurand.so.10]
 0x0000000000000001 (NEEDED)             Shared library: [libcublas.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcublasLt.so.12]
 0x0000000000000001 (NEEDED)             Shared library: [libcudnn.so.8]
 0x0000000000000001 (NEEDED)             Shared library: [libnccl.so.2]
 0x0000000000000001 (NEEDED)             Shared library: [libpthread.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libdl.so.2]
 0x0000000000000001 (NEEDED)             Shared library: [librt.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc10.so]
 0x0000000000000001 (NEEDED)             Shared library: [libtorch_cpu.so]
 0x0000000000000001 (NEEDED)             Shared library: [libm.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [ld-linux-x86-64.so.2]
 0x000000000000000e (SONAME)             Library soname: [libtorch_cuda.so]
 0x000000000000000f (RPATH)              Library rpath: [$ORIGIN/../../nvidia/cublas/lib:$ORIGIN/../../nvidia/cuda_cupti/lib:$ORIGIN/../../nvidia/cuda_nvrtc/lib:$ORIGIN/../../nvidia/cuda_runtime/lib:$ORIGIN/../../nvidia/cudnn/lib:$ORIGIN/../../nvidia/cufft/lib:$ORIGIN/../../nvidia/curand/lib:$ORIGIN/../../nvidia/cusolver/lib:$ORIGIN/../../nvidia/cusparse/lib:$ORIGIN/../../nvidia/nccl/lib:$ORIGIN/../../nvidia/nvtx/lib:$ORIGIN]
 ```
 
 In the case of `bitsandbytes`, the RPATH should include:
 * `$ORIGIN/../../nvidia/cuda_runtime/lib` - for libcudart.so
 * `$ORIGIN/../../nvidia/cublas/lib` - for libcublas.so, libcublasLt.so
 * `$ORIGIN/../../nvidia/cusparse/lib` - for libcusparse.so
 
 **Note:** PyTorch wheels installed with nvidia packages this way since ~1.13 (TODO: confirm). It might be reasonable to set that as the minimum requirement if necessary. I'm not sure yet if the typical layout from conda is different so that needs to be determined as well. 


### Motivation

The motivation is to make the library more accessible and easier to install on a wider range of system configurations.

Possibly related issues:
#1073 and several others on this repo
pytorch/pytorch#101314
unslothai/unsloth#200
unslothai/unsloth#221

### Your contribution

I plan to submit a PR for this. There's some potential overlap with #1041 as well.

## 评论 (1)

### Titus-von-Koeller · 2025-04-28

Testing Across Scenarios: After implementing the RPATH change, test Bitsandbytes in at least: (1) a fresh machine with no CUDA toolkit but with PyTorch installed (pip), (2) a conda environment with only conda PyTorch, (3) a system with an outdated CUDA toolkit installed and see that Bitsandbytes still loads the intended libs (from pip or conda, not the old system ones). Also test that if the nvidia folders are missing (simulate PyTorch <1.13 or user didn’t get the deps), Bitsandbytes fails gracefully with an informative error (perhaps instructing to upgrade PyTorch or install CUDA). Ideally, Bitsandbytes’ Python code can detect this scenario and fall back to the old behavior: e.g., if libbitsandbytes.so fails to load, try loading via ctypes.CDLL with a manual search in CUDA_PATH or raise a clear message. This would cover any corner case without leaving the user confused.
