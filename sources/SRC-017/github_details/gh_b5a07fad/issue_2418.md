# [Issue #2418] [Issue]: Dual RTX PRO 6000 Blackwell: NCCL 2.26.2 illegal memory access for >=512 KiB collectives, not reproducible with 2.31.2

source: https://github.com/NVIDIA/nccl/issues/2418
state: closed | updated: 2026-09-21T00:57:47Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

[minimal_nccl_2262.log](https://github.com/user-attachments/files/32340239/minimal_nccl_2262.log)
[minimal_nccl_2312.log](https://github.com/user-attachments/files/32340238/minimal_nccl_2312.log)
[nccl_tests_2312_8B_512MiB.log](https://github.com/user-attachments/files/32340240/nccl_tests_2312_8B_512MiB.log)


### Steps to Reproduce the Issue

### Minimal reproduction

The problem is reproducible on a single bare-metal workstation with two NVIDIA RTX PRO 6000 Blackwell Workstation Edition GPUs.

#### Environment

- GPU: 2 x NVIDIA RTX PRO 6000 Blackwell Workstation Edition, 96 GB each
- Driver: 580.173.02
- NVIDIA Open Kernel Module
- OS: Ubuntu 24.04.4 LTS
- Kernel: 6.8.0-139-generic
- PyTorch: 2.7.0+cu128
- CUDA runtime reported by PyTorch: 12.8
- Failing NCCL runtime: 2.26.2+cuda12.2
- Working NCCL runtime tested: 2.31.2+cuda12.9
- Bare metal, no container
- One node, two ranks
- No NVLink
- `nvidia-smi topo -m` reports GPU0 <-> GPU1 as `NODE`
- Both GPUs are on the same NUMA node

#### Reproduction with NCCL 2.26.2

Using nccl-tests with two GPUs:

```bash
all_reduce_perf -b 8 -e 16M -f 2 -g 2

The test succeeds for smaller message sizes but reproducibly fails when reaching 524288 bytes:

262144 B  -> PASS
524288 B  -> Test CUDA failure: an illegal memory access was encountered

A separate PyTorch two-rank 16 MiB all-reduce also reproduces the same failure.

The problem is deterministic in our testing rather than intermittent.

Protocol observations with NCCL 2.26.2

For the same two-GPU setup:

NCCL_PROTO=LL      -> PASS
NCCL_PROTO=LL128   -> FAIL with illegal memory access
NCCL_PROTO=Simple  -> FAIL with illegal memory access

The default local transport was reported as:

SHM/direct/direct

Forcing PCIe P2P/CUMEM did not resolve the failure with NCCL 2.26.2.

IOMMU / ACS checks

The machine normally runs with Intel IOMMU translated mode.

As a diagnostic only, we booted once with:

intel_iommu=off

and confirmed Intel DMA remapping was disabled. The NCCL 2.26.2 failure remained unchanged.

Relevant ACS controls on the PCIe path showed:

ReqRedir-
CmpltRedir-

so ACS P2P Request Redirect and Completion Redirect were not enabled.

A/B with NCCL 2.31.2

We kept the following unchanged:

GPUs
driver
OS/kernel
PyTorch
CUDA runtime
topology
IOMMU configuration

Only the runtime NCCL shared library was changed by using LD_PRELOAD.

Example:

LD_PRELOAD=/path/to/nccl-2.31.2/libnccl.so.2 \
NCCL_DEBUG=INFO \
all_reduce_perf -b 8 -e 512M -f 2 -g 2

The NCCL debug log confirms:

NCCL version 2.31.2+cuda12.9

With NCCL 2.31.2:

512 KiB -> PASS
4 MiB   -> PASS
16 MiB  -> PASS

nccl-tests completes successfully from 8 B through 512 MiB with:

# Out of bounds values : 0 OK
# Collective test concluded: all_reduce_perf

The test was also repeated after a normal reboot with IOMMU enabled, and it remained successful.

Previous success / version comparison

This does not work with NCCL 2.26.2 on this machine.

The failure is not reproducible with NCCL 2.31.2 under otherwise unchanged conditions.

We have not identified the exact NCCL change between these releases responsible for the behavior.

### NCCL Version

2.26.2+cuda12.2

### Your platform details

- Bare-metal workstation
- 2 x NVIDIA RTX PRO 6000 Blackwell Workstation Edition, 96 GB each
- NVIDIA driver 580.173.02
- NVIDIA Open Kernel Module
- Ubuntu 24.04.4 LTS
- Linux kernel 6.8.0-139-generic
- PyTorch 2.7.0+cu128
- CUDA runtime 12.8
- Single node, 2 NCCL ranks
- No NVLink
- `nvidia-smi topo -m`: GPU0 <-> GPU1 = NODE
- Both GPUs are on the same NUMA node
- PCIe Gen5 x16
- No InfiniBand/RDMA involved; this is a local two-GPU reproducer
- CUDA peer access is available in both GPU directions

### Error Message & Behavior

### First observed error

There was no useful NCCL WARN preceding the failure in the minimal nccl-tests reproduction.

The first visible failure is:

```text
524288        131072     float     sum      -1
Test CUDA failure common.cu:516 'an illegal memory access was encountered'
Test failure common.cu:731
Test failure common.cu:958
Test failure all_reduce.cu:574

The corresponding PyTorch reproduction terminates with CUDA illegal memory access / SIGABRT.

Expected behavior

Two-GPU all-reduce should complete correctly for all tested message sizes.

Actual behavior with NCCL 2.26.2

Small messages complete successfully, but the run reproducibly fails when the message size reaches approximately 512 KiB.

Behavior with NCCL 2.31.2

Under otherwise unchanged conditions, the same two-GPU system successfully completes all-reduce tests from 8 B through 512 MiB with no data errors.

A real two-GPU DeepSpeed ZeRO-3 training run also completes 50 optimizer steps successfully with NCCL 2.31.2, whereas the NCCL 2.26.2 run fails with an illegal memory access.

## 评论 (2)

### cnbelusar · 2026-09-17

@AlbertLee98 , 

Please see the [CUDA compatibility matrix](https://docs.nvidia.com/datacenter/tesla/drivers/cuda-toolkit-driver-and-architecture-matrix.html) .
RTX PRO 6000 Blackwell is supported with CUDA 12.8 and later. Are you only seeing failures when compiling NCCL with earlier versions of the CUDA toolkit?




### xiaofanl-nvidia · 2026-09-21

I'm closing this issue since the issue does not reproduce with 2.31.2. Please open a new issue if this remains a problem for your usage. Thanks! 
