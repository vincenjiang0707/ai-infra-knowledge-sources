# [Issue #368] Is it applicable to the L20 card?

source: https://github.com/NVIDIA/nccl-tests/issues/368
state: open | updated: 2026-01-29T09:27:48Z
labels: 

## 正文

<img width="1512" height="120" alt="Image" src="https://github.com/user-attachments/assets/4ee473cb-5919-4e8d-b0b2-4343313d13d3" />

## 评论 (4)

### AddyLaddy · 2026-01-20

It looks like your CUDA toolkit is not installed correctly.
I see it says `nvlink` not found


### jiaozenghui · 2026-01-29

> It looks like your CUDA toolkit is not installed correctly. I see it says `nvlink` not found

Yes my CUDA tookit does not have nvlink component,  does nccl-tests must require nvlink to run?

### sjeaugey · 2026-01-29

`nvlink` is the NVIDIA linker program, which should come as part of the CUDA compiler. You need it to link CUDA code. It should be in `/usr/local/cuda/bin/nvlink` unless your CUDA installation is broken. If so, you should reinstall CUDA.

Note, it has nothing to do with NVLink, the hardware connecting GPUs for high-bandwidth communication.

### jiaozenghui · 2026-01-29

> `nvlink` is the NVIDIA linker program, which should come as part of the CUDA compiler. You need it to link CUDA code. It should be in `/usr/local/cuda/bin/nvlink` unless your CUDA installation is broken. If so, you should reinstall CUDA.
> 
> Note, it has nothing to do with NVLink, the hardware connecting GPUs for high-bandwidth communication.

The communication between NVIDIA L20 cards does not support NVLink and mainly relies on PCIe Gen4 x16 to achieve multi card communication within nodes. High speed interconnection between nodes is achieved through RDMA (InfiniBand/RoCE)+NCCL.
