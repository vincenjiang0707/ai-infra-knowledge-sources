# [Issue #2372] [Question]: NCCL GIN GDAKI (type 3) hangs during Pure GIN AlltoAll, PROXY (type 2) works

source: https://github.com/NVIDIA/nccl/issues/2372
state: open | updated: 2026-09-21T10:29:56Z
labels: question

## 正文


## Summary

Running the official `06_device_api/02_alltoall_gin` example on an 8-GPU H200 node:

- `NCCL_GIN_TYPE=3` (GDAKI): the device communicator is created successfully, but the kernel **hangs forever** at `=== Executing Pure GIN AlltoAll ===`.
- `NCCL_GIN_TYPE=2` (PROXY): **passes** (`Pure GIN AlltoAll result: PASSED`).

## Environment

| Item | Value |
|------|-------|
| GPU | 8x NVIDIA H200 (143771 MiB each) |
| Driver | 580.105.08 |
| Driver CUDA | 13.0 |
| CUDA toolkit | 12.9 (`/usr/local/cuda -> cuda-12.9`) |
| NCCL | 2.30.7+cuda12.9 |
| NCCL commit | `5067397c2676d5aed50042fc39e5c8ee96eb0027` |
| MLNX_OFED | `26.04-0.8.6` |
| DOCA host | `doca-host-3.4.0-085000_26.04_openeuler2203` |
| `nvidia_peermem` | loaded (`nvidia_peermem 16384 0`, referenced by `ib_uverbs`) |
| `libcuda.so.1` | present at `/usr/lib64/libcuda.so.1 -> libcuda.so.580.105.08` |

## Repro steps

```bash
# 1. clean python env
uv venv ncclenv --python 3.11 --seed

# 2. torch
pip3 install torch==2.10.0 --no-user

# 3. NCCL source (exact commit)
git clone git@github.com:NVIDIA/nccl.git   # 5067397c2676d5aed50042fc39e5c8ee96eb0027

# 4. build NCCL
cd nccl && make -j"$(nproc)" src.build CUDA_HOME=/usr/local/cuda BUILDDIR=/nccl/build

# 5. GIN alltoall example
cd /nccl/docs/examples/06_device_api/02_alltoall_gin/c/

# GDAKI (type 3) -> HANGS
export LD_PRELOAD=/nccl/build/lib/libnccl.so.2.30.7
export EP_NCCL_ROOT_DIR=/nccl/build
export LD_LIBRARY_PATH="$EP_NCCL_ROOT_DIR/lib:${LD_LIBRARY_PATH:-}"
NTHREADS=8 NCCL_GIN_TYPE=3 ./alltoall_gin

# PROXY (type 2) -> PASSES
NTHREADS=8 NCCL_GIN_TYPE=2 ./alltoall_gin
```

## Observed behavior

### GDAKI (type 3) — hangs

All 8 ranks reach `created device communicator with GIN support`, then hang at the kernel:

```
  Rank 0 created device communicator with GIN support
  Rank 1 created device communicator with GIN support
  ...
  Rank 7 created device communicator with GIN support
Starting Pure GIN AlltoAll with 1024 elements per rank (8192 total elements, 0 MB)

=== Executing Pure GIN AlltoAll ===
<hang — no "completed pure GIN AlltoAll kernel" lines, must Ctrl+C>
```

### PROXY (type 2) — passes

```
  Rank 0 created device communicator with GIN support
  ...
=== Executing Pure GIN AlltoAll ===
  Rank 0 completed pure GIN AlltoAll kernel
  ...
  Rank 7 completed pure GIN AlltoAll kernel
Pure GIN AlltoAll result: PASSED

All NCCL communicators finalized successfully!
```

## What we already checked

1. `nvidia_peermem` is loaded and referenced by `ib_uverbs` (GPU direct RDMA peer memory is present).
2. `libcuda.so.1` is present in `/usr/lib64` and visible via `ldconfig -p`.
3. Plain (non-GIN) NCCL collective init completes fine (`ncclCommInitRank ... Init COMPLETE` for all 8 ranks).
4. The hang is reproducible and consistent (not intermittent).

## Question

Why does the GDAKI (`NCCL_GIN_TYPE=3`) data path hang during the pure GIN AlltoAll kernel while the PROXY (`NCCL_GIN_TYPE=2`) path completes successfully? Is there an additional runtime dependency (e.g. a specific DOCA GPUNetIO userspace library/version) or a driver/toolkit mismatch we should check?

Full logs attached (`NCCL_DEBUG=INFO` for both type 2 and type 3 runs).

[nccl_gin_gdaki_sanitized.log](https://github.com/user-attachments/files/31461761/nccl_gin_gdaki_sanitized.log)
[nccl_gin_proxy_sanitized.log](https://github.com/user-attachments/files/31461762/nccl_gin_proxy_sanitized.log)

## 评论 (2)

### WoShiAPei · 2026-09-17

Hi，using NCCL_GIN_TYPE=3 + NCCL_GIN_GDAKI_NIC_HANDLER=1  will solve the problem？

### teojgo · 2026-09-21

@HPC4AI can you test with the latest release [v2.32](https://github.com/NVIDIA/nccl/releases/tag/v2.32.3-1)?
