# [Issue #362] Low NCCL Performance in ubuntu kernel 6.8.x

source: https://github.com/NVIDIA/nccl-tests/issues/362
state: open | updated: 2026-07-21T00:41:30Z
labels: 

## 正文


I have tested Multinode ( 2 node ) NCCL Tests on Ubuntu 5.15.x Kernel and 6.8.X kernel. NCCL performnce is very low on 6.8.x kernel. I have mentioned the results below. ANy specific reason for it ?  for both of them I have used nvidia-driver-570 and Cuda-12.8

****_5.15.X Kernel_**** 

export NCCL_DEBUG=INFO
export NCCL_IB_DISABLE=0
export NCCL_SOCKET_IFNAME=bond0           
export NCCL_IB_GID_INDEX=3
export NCCL_MIN_NCHANNELS=32
export NCCL_MAX_NCHANNELS=32

export NCCL_IB_HCA="mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1, mlx5_11:1"




$Launch: 8 ranks per node (total 16). Ensure you give each host 8 slots.
mpirun --map-by ppr:8:node --bind-to none -np 16 \
  --host que-srv-hpc-49p:8,que-srv-hpc-30p:8 \
  -x NCCL_DEBUG -x NCCL_IB_DISABLE -x NCCL_SOCKET_IFNAME \
  -x NCCL_IB_HCA -x NCCL_IB_GID_INDEX \
  -x NCCL_MIN_NCHANNELS -x NCCL_MAX_NCHANNELS \
  -x LD_LIBRARY_PATH -x PATH \
  ~/nccl-tests/build/all_reduce_perf -b 16G -e 16G -f 2 -g 1

Out of bounds values : 0 OK
Avg bus bandwidth    : 481


****_6.8.X Kernel_**** 

export NCCL_DEBUG=INFO
export NCCL_IB_DISABLE=0
export NCCL_SOCKET_IFNAME=bond0           
export NCCL_IB_GID_INDEX=3
export NCCL_MIN_NCHANNELS=32
export NCCL_MAX_NCHANNELS=32


export NCCL_IB_HCA="mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1, mlx5_11:1"





mpirun --map-by ppr:8:node --bind-to none -np 16 \
  --host que-srv-hpc-49p:8,que-srv-hpc-30p:8 \
  -x NCCL_DEBUG -x NCCL_IB_DISABLE -x NCCL_SOCKET_IFNAME \
  -x NCCL_IB_HCA -x NCCL_IB_GID_INDEX \
  -x NCCL_MIN_NCHANNELS -x NCCL_MAX_NCHANNELS \
  -x LD_LIBRARY_PATH -x PATH \
  ~/nccl-tests/build/all_reduce_perf -b 16G -e 16G -f 2 -g 1

Out of bounds values : 0 OK
 Avg bus bandwidth    :  104 



## 评论 (6)

### AddyLaddy · 2025-12-11

This is probably a question for the main nccl GitHub project really, as it's not an issue with nccl-tests.

But there are many reasons for systems not reaching peak performance such as GDRDMA not being enabled or incorrect ACS configuration.
I see in this case you suspect the Linux kernel may be the root cause? So I would guess that GDRDMA is not being enabled for some reason.
Also note that the latest Linux kernels and Open Nvidia drivers normally support GDRDMA via DMA-BUF and the nvidia-peermem kernel module is no longer required.

Uploading the NCCL_DEBUG=INFO log is always very helpful too.



### fazlan1990 · 2025-12-14


Thanks for your quick response. I am doing Multinode NCCL with 2 nodes. 

Nvidia_peermem enabled and ACS also disabled . I have attached NCCL logs below

[NCCL Logs.txt](https://github.com/user-attachments/files/24148057/NCCL.Logs.txt)

root@que-srv-hpc-8p:~# lsmod | grep nvidia_peermem
nvidia_peermem         16384  0
ib_uverbs             200704  3 nvidia_peermem,rdma_ucm,mlx5_ib
nvidia              104964096  96 nvidia_uvm,nvidia_peermem,nvidia_modeset
root@que-srv-hpc-8p:~# 
root@que-srv-hpc-8p:~# 
root@que-srv-hpc-8p:~# sudo lspci -vvv | grep ACSCtl
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-


### AddyLaddy · 2025-12-15

Why are you restricting the channels to just 2? I would expect at least 2 channels per NIC

```
que-srv-hpc-49p:80581:80627 [6] NCCL INFO NCCL_MAX_NCHANNELS set by environment to 2.
que-srv-hpc-49p:80581:80627 [6] NCCL INFO NCCL_MIN_NCHANNELS set by environment to 2.
```

### AddyLaddy · 2025-12-15

I also see some NICs are not being selecting for GDRDMA.
That should be investigated futher.


### fazlan1990 · 2025-12-17

[5.15.x_kernel-logs with nvidia_peermem.txt](https://github.com/user-attachments/files/24204121/5.15.x_kernel-logs.with.nvidia_peermem.txt)

[6.8.x-kernel-logs with nvidia_peermem.txt](https://github.com/user-attachments/files/24204124/6.8.x-kernel-logs.with.nvidia_peermem.txt)            I have  attached the both NCCL logs. one was done on ubuntu 22.04-5.15.x kernel  and other was done on ubuntu-6.8.x kernel.   In 6.8.x we are getting very low bandwith . All Interfaces are using GDRDMA still getting low performance. Both were tested on identical setup and ACS disabled and Nvidia_peermem enabled. 

### SPD9112 · 2026-07-21

Maybe it is too late, but if your server's virtualization is enabled, you need to add iommu=pt to your grub, since after ubuntu kernel 6.8.X, GPUdirect RDMA takes DMA-BUF instead of nvidia_peermem. 
