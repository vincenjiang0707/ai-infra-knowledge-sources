# [Issue #1738] Use `__CUDA_ARCH__` instead of `__NVCC__` to disambiguate device and host code

source: https://github.com/NVIDIA/nccl/issues/1738
state: open | updated: 2026-09-06T12:17:36Z
labels: 

## 正文

In this [block](https://github.com/NVIDIA/nccl/blob/v2.27.3-1/src/include/gdrwrap.h#L38) and this [block](https://github.com/NVIDIA/nccl/blob/v2.27.3-1/src/include/bitops.h#L13), `__NVCC__` looks like it's used to disambiguate device and host code. 

When compiling on-device code, it's more correct to use `__CUDA_ARCH__`, as `clang++` (and not `NVCC`) may be used to compile device code.

Right now it works because without extra `__device__` and `__host__` annotations, it's just treated as host code.

Happy to open a PR.

## 评论 (1)

### kodlan · 2026-09-06

both places are still there and nothing else uses __NVCC__ for this.
Opened #2392 which switches both checks to __CUDACC__, tested with defined()
