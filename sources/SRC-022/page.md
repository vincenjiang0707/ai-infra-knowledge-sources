source: https://github.com/ROCm/rccl/releases

# Releases: ROCm/rccl

Releases · ROCm/rccl

## Release list

## rocm-7.2.4

RCCL code for ROCm 7.2 did not change. The library was rebuilt for the updated ROCm 7.2 stack.

## rccl 2.27.7 for ROCm 7.2.3

RCCL code for ROCm 7.2.3 did not change. The library was rebuilt for the updated ROCm 7.2.3 stack.

## rccl 2.27.7 for ROCm 7.2.2

RCCL code for ROCm 7.2.2 did not change. The library was rebuilt for the updated ROCm 7.2.2 stack.

## rccl 2.27.7 for ROCm 7.2.1

RCCL code for ROCm 7.2.1 did not change. The library was rebuilt for the updated ROCm 7.2.1 stack.

## therock-7.11

## therock-7.10

## RCCL 2.27.7 for ROCm 7.2.0

### Changed

- RCCL error messages have been made more verbose in several cases. RCCL now prints out fatal error messages by default. Fatal error messages can be suppressed by setting
`NCCL_DEBUG=NONE`

. - Disabled
`reduceCopyPacks`

pipelining for`gfx950`

.

## RCCL 2.27.7 for ROCm 7.1.1

### Resolved Issues

- Fixed a single node data corruption issue in MSCCL on the Instinct MI350X and MI355X for the LL protocol. This previously affected about 2% of the runs for single node AllReduce with inputs smaller than 512 KiB.

## RCCL 2.27.7 for ROCm 7.1.0

### Added

- Added
`RCCL_P2P_BATCH_THRESHOLD`

to set the message size limit for batching P2P operations. This mainly affects small message performance for alltoall at a large scale but also applies to alltoallv. - Added
`RCCL_P2P_BATCH_ENABLE`

to enable batching P2P operations to receive performance gains for smaller messages up to 4MB for alltoall when the workload requires it. This is to avoid performance dips for larger messages.

### Changed

- The MSCCL++ feature is now disabled by default. The
`--disable-mscclpp`

build flag is replaced with`--enable-mscclpp`

in the`rccl/install.sh`

script. - Compatibility with NCCL 2.27.7

### Resolved issues

- Improve small message performance for alltoall by enabling and optimizing batched P2P operations.

### Known issues

- Symmetric memory kernels are currently disabled due to ongoing CUMEM enablement work.

## RCCL 2.26.6 for ROCm 7.0.2

### Added

- Enabled double-buffering in
`reduceCopyPacks`

to trigger pipelining, especially to overlap bf16 arithmetic. - Added
`--force-reduce-pipeline`

as an option that can be passed to the`install.sh`

script. Passing this option will enable software-triggered pipelining`bfloat16`

reductions (i.e.`all_reduce`

,`reduce_scatter`

and`reduce`

).