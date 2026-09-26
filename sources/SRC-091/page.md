source: https://github.com/LMCache/LMCache/releases

# Releases: LMCache/LMCache

## Release list

## Nightly 2026-09-24 · ROCm 7.2 (gfx942, gfx950)

Nightly ROCm 7.2 wheels built from `dev`

on 2026-09-24,

for AMD Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X),

ABI-matched to the upstream `vllm/vllm-openai-rocm`

image

(torch 2.11, cp312).

Install into an upstream vLLM ROCm container:

```
pip install lmcache==0.5.6.dev98+rocm7.2 --no-deps \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-rocm
```


## Nightly 2026-09-24 · Moore Threads MUSA

Nightly MUSA wheel for LMCache, built from `dev`

on 2026-09-24.

Built and smoke-tested in the validated public MUSA image. TorchMUSA,

the MUSA SDK, and device drivers remain host-owned and are not bundled

in the wheel.

Install inside the matching MUSA runtime image:

```
pip install lmcache==0.5.6.dev98+musa --no-deps \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-musa
```

## Nightly 2026-09-24 · CUDA 12.9

Nightly CUDA 12.9 wheels built from `dev`

on 2026-09-24.

```
uv pip install lmcache --pre \
--extra-index-url https://download.pytorch.org/whl/cu129 \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-cu129 \
--index-strategy unsafe-best-match
```


## Nightly 2026-09-24 · CUDA 13.0

Nightly CUDA 13.0 wheels built from `dev`

on 2026-09-24.

```
uv pip install lmcache --pre \
--extra-index-url https://download.pytorch.org/whl/cu130 \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly \
--index-strategy unsafe-best-match
```


## operator-v0.5.5

[good-first-issue] storage: convert f-string log calls in eic_connect…

## Release v0.5.5rc7 · Intel XPU (SYCL)

Intel XPU/SYCL wheel for LMCache v0.5.5rc7.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:

```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+xpu --no-deps \
--no-index \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```


## Release v0.5.5rc7 · AMD ROCm 7.2.4 / torch 2.10.0 git3d3aa833 / cp312 / CXX11 ABI=1

ROCm wheel for LMCache v0.5.5rc7, built and tested in

`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`


at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`

.

Supported ABI (exact):

- AMD torch wheel source:
[https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl](https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl) - torch runtime:
`2.10.0+rocm7.2.4.git3d3aa833`

(git`3d3aa833db84eed6b7f5595cb5f162c2f78300a4`

) - ROCm:
`7.2.4`

(HIP runtime`7.2.53211`

) - Python/platform:
`cp312-cp312-manylinux_2_39_x86_64`

- C++ ABI:
`_GLIBCXX_USE_CXX11_ABI=1`


It includes gfx942/gfx950 GPU code objects and all integrations shipped

by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:

```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```

## Release v0.5.5rc7 · ROCm (gfx942, gfx950)

ROCm 7.2 wheel for LMCache v0.5.5rc7, built for AMD

Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched

to the upstream `vllm/vllm-openai-rocm`

image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:

```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+rocm7.2 --no-deps \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```


## Release v0.5.5rc7 · Moore Threads MUSA

MUSA-compatible wheel for LMCache v0.5.5rc7.

Built and smoke-tested in the validated TorchMUSA/MUSA SDK image. TorchMUSA, musa_aiter, and the MUSA userspace runtime stay in the host image and are not installed from PyPI.

Install inside the matching MUSA runtime image:

```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+musa --no-deps \
--no-index \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-musa
```

## Release v0.5.5rc7 · CUDA 12.9

CUDA 12.9 wheel for LMCache v0.5.5rc7.

```
VERSION=v0.5.5rc7
uv pip install lmcache== \
--extra-index-url https://download.pytorch.org/whl/cu129 \
--find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
--index-strategy unsafe-best-match
```