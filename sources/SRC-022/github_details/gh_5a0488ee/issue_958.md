# [Issue #958] RCCL ignores AMDGPU_TARGETS and builds for all hardcoded arches anyway

source: https://github.com/ROCm/rccl/issues/958
state: closed | updated: 2024-01-16T22:59:48Z
labels: 

## 正文

Hi, while updating build script for rccl-5.7.1 in Gentoo, I noticed that RCCL ignores `-DAMDGPU_TARGETS=...` parameter, which makes compilation for a single GPU significantly slower than it could be.

AMDGPU_TARGETS works for every ROCm package I checked (miopen, hipCUB, rocBLAS, hipRAND, rocFFT, and so on), the only difference, why it does not work in rccl is because it uses `FORCE` in `set(AMDGPU_TARGETS` definition:
https://github.com/ROCmSoftwarePlatform/rccl/blob/rocm-5.7.1/CMakeLists.txt#L65

Can you remove this `FORCE` in some future release? Thanks!

## 评论 (1)

### nileshnegi · 2024-01-16

Fixed in https://github.com/ROCm/rccl/commit/414884c6cbc18f40c880d9b7bed39132e9f349fa
