# [Issue #2586] [Installation]: Build release wheels in the PyTorch manylinux image instead of ubuntu-22.04

source: https://github.com/kvcache-ai/Mooncake/issues/2586
state: open | updated: 2026-09-24T03:17:11Z
labels: stale

## 正文

## Issue

The release wheels are built on a plain `ubuntu-22.04` runner (`release.yaml`, `release-cuda13.yaml`, `pre-release.yaml`, etc.). I'd like to build them inside the PyTorch manylinux images instead, the way PyTorch and vLLM build their wheels for broad system support.

## Background

Building on ubuntu-22.04 ties the wheels to that environment in two ways:

- **glibc floor of 2.35.** `build_wheel.sh` tags the wheel from the runner's glibc, so it comes out `manylinux_2_35`. That leaves out RHEL/Rocky/Alma 9 (glibc 2.34), the RHEL 8 family (2.28), Ubuntu 20.04 (2.31), and a lot of HPC images.

- **The toolchain's libstdc++ leaks in.** ubuntu-22.04 ships GCC 12, so the binaries require `GLIBCXX_3.4.30`. glibc and libstdc++ are versioned separately, so a host can satisfy the `manylinux_2_35` floor and still fail to load:

  ```
  mooncake_master: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.30' not found
  ```

  `import mooncake.store` fails the same way. #2585 statically links the C++ runtime to stop that leak, but the wheel still carries the 2.35 floor.

## Proposal

Build in `pytorch/manylinux2_28-builder` (AlmaLinux 8, glibc 2.28) — the standard image for CUDA Python wheels:

- `:cuda12.8` and `:cuda13.0` tags cover both CUDA lines; matching aarch64 images exist for ARM.
- The CUDA toolkit is already in the image, so the `Jimver/cuda-toolkit` step goes away.
- Python lives at `/opt/python/cp${XY}-cp${XY}/`, and `dependencies.sh` already has a `yum` path for AlmaLinux.
- `build_wheel.sh` already runs `auditwheel repair`; on a 2.28 base it just tags `manylinux_2_28`.

vLLM did exactly this with its `BUILD_OS=manylinux` build base (`pytorch/manylinux2_28-builder:cuda13.0`) to get a glibc 2.28 floor that matches PyTorch's own wheels - see `vllm/docker/Dockerfile` and https://github.com/vllm-project/vllm/pull/41416.

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (5)

### github-actions[bot] · 2026-06-23

Thanks for opening this issue, @mgoin!

| Field | Value |
|-------|-------|
| **Issue** | #2586 |
| **GitHub user ID** | `3195154` |
| **Reporter** | @mgoin |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### Aionw · 2026-06-24

Thanks for reporting this. Are you interested in submitting a PR? If not, i can take care of it.

### mgoin · 2026-06-24

I can work on a PR to demonstrate! Thanks

### mgoin · 2026-06-25

https://github.com/kvcache-ai/Mooncake/pull/2605

### github-actions[bot] · 2026-09-24

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
