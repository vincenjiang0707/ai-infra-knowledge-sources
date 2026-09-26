# [Issue #124] ArchLinux test Failed

source: https://github.com/NVIDIA/nccl-tests/issues/124
state: open | updated: 2025-07-02T17:44:43Z
labels: 

## 正文

Hi,
I use ArchLinux with dual GPUs and connected with NVLink. I install the `cuda` and `nccl` from the community repo. 
```
cuda 11.8.0-1
nccl 2.15.5-1
```
I use the following command 
`
CUDA_VISIBLE_DEVICES=0,1 NCCL_P2P_LEVEL=NVL ./all_reduce_perf -g 2 -c 0 -n 100 -w 20
`
and got the following error

```
# nThread 1 nGpus 2 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 20 iters: 100 agg iters: 1 validation: 0 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 353404 on    ArchLinux device  0 [0x01] NVIDIA GeForce RTX 3090
#  Rank  1 Group  0 Pid 353404 on    ArchLinux device  1 [0x09] NVIDIA GeForce RTX 3090
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
ArchLinux: Test NCCL failure all_reduce.cu:44 'unhandled cuda error / '
 .. ArchLinux pid 353404: Test failure common.cu:377
 .. ArchLinux pid 353404: Test failure common.cu:584
 .. ArchLinux pid 353404: Test failure all_reduce.cu:90
 .. ArchLinux pid 353404: Test failure common.cu:613
 .. ArchLinux pid 353404: Test failure common.cu:1016
 .. ArchLinux pid 353404: Test failure common.cu:842
```

Best Regards,
Jack Lu


## 评论 (6)

### jbachan · 2022-12-28

Please rerun with `NCCL_DEBUG=INFO` and share the output.

### jacklu333333 · 2022-12-29

Hi,
I rerun it with `NCCL_DEBUG=INFO`


This is the complete command
`CUDA_VISIBLE_DEVICES=0,1 NCCL_P2P_LEVEL=NVL  NCCL_DEBUG=INFO  ./all_reduce_perf -g 2 -c 0 -n 100 -w 20`


and this is the output
```
# nThread 1 nGpus 2 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 20 iters: 100 agg iters: 1 validation: 0 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   6482 on    ArchLinux device  0 [0x01] NVIDIA GeForce RTX 3090
#  Rank  1 Group  0 Pid   6482 on    ArchLinux device  1 [0x09] NVIDIA GeForce RTX 3090
ArchLinux:6482:6482 [0] NCCL INFO Bootstrap : Using enp8s0:143.248.56.121<0>
ArchLinux:6482:6482 [0] NCCL INFO NET/Plugin : No plugin found (libnccl-net.so), using internal implementation
ArchLinux:6482:6482 [1] NCCL INFO cudaDriverVersion 12000
NCCL version 2.15.5+cuda11.8
ArchLinux:6482:6500 [0] NCCL INFO Failed to open libibverbs.so[.1]
ArchLinux:6482:6500 [0] NCCL INFO NET/Socket : Using [0]enp8s0:143.248.56.121<0> [1]br-2178a67b2ff7:172.23.0.1<0> [2]veth018915b:fe80::6832:a2ff:fe5b:c212%veth018915b<0> [3]veth2d267e7:fe80::b07e:48ff:fe46:3fe2%veth2d267e7<0> [4]veth13a831b:fe80::4036:64ff:fe56:4cd6%veth13a831b<0> [5]vethbffaff7:fe80::4c9b:4bff:fef4:30b6%vethbffaff7<0>
ArchLinux:6482:6500 [0] NCCL INFO Using network Socket
ArchLinux:6482:6501 [1] NCCL INFO Using network Socket
ArchLinux:6482:6500 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
ArchLinux:6482:6500 [0] NCCL INFO Channel 00/04 :    0   1
ArchLinux:6482:6500 [0] NCCL INFO Channel 01/04 :    0   1
ArchLinux:6482:6500 [0] NCCL INFO Channel 02/04 :    0   1
ArchLinux:6482:6500 [0] NCCL INFO Channel 03/04 :    0   1
ArchLinux:6482:6501 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1 [2] -1/-1/-1->1->0 [3] 0/-1/-1->1->-1
ArchLinux:6482:6500 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1 [2] 1/-1/-1->0->-1 [3] -1/-1/-1->0->1
ArchLinux:6482:6500 [0] NCCL INFO Channel 00/0 : 0[1000] -> 1[9000] via P2P/direct pointer
ArchLinux:6482:6501 [1] NCCL INFO Channel 00/0 : 1[9000] -> 0[1000] via P2P/direct pointer
ArchLinux:6482:6500 [0] NCCL INFO Channel 01/0 : 0[1000] -> 1[9000] via P2P/direct pointer
ArchLinux:6482:6500 [0] NCCL INFO Channel 02/0 : 0[1000] -> 1[9000] via P2P/direct pointer
ArchLinux:6482:6500 [0] NCCL INFO Channel 03/0 : 0[1000] -> 1[9000] via P2P/direct pointer
ArchLinux:6482:6501 [1] NCCL INFO Channel 01/0 : 1[9000] -> 0[1000] via P2P/direct pointer
ArchLinux:6482:6501 [1] NCCL INFO Channel 02/0 : 1[9000] -> 0[1000] via P2P/direct pointer
ArchLinux:6482:6501 [1] NCCL INFO Channel 03/0 : 1[9000] -> 0[1000] via P2P/direct pointer
ArchLinux:6482:6500 [0] NCCL INFO Connected all rings
ArchLinux:6482:6500 [0] NCCL INFO Connected all trees
ArchLinux:6482:6501 [1] NCCL INFO Connected all rings
ArchLinux:6482:6501 [1] NCCL INFO Connected all trees
ArchLinux:6482:6501 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
ArchLinux:6482:6501 [1] NCCL INFO 4 coll channels, 4 p2p channels, 4 p2p channels per peer
ArchLinux:6482:6500 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
ArchLinux:6482:6500 [0] NCCL INFO 4 coll channels, 4 p2p channels, 4 p2p channels per peer
ArchLinux:6482:6500 [0] NCCL INFO comm 0x55a756b3ceb0 rank 0 nranks 2 cudaDev 0 busId 1000 - Init COMPLETE
ArchLinux:6482:6501 [1] NCCL INFO comm 0x55a756b3f940 rank 1 nranks 2 cudaDev 1 busId 9000 - Init COMPLETE
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       

ArchLinux:6482:6482 [0] misc/strongstream.cc:60 NCCL WARN Cuda failure 'CUDA driver is a stub library'
ArchLinux:6482:6482 [0] NCCL INFO enqueue.cc:1496 -> 1
ArchLinux:6482:6482 [0] NCCL INFO enqueue.cc:1537 -> 1
ArchLinux: Test NCCL failure all_reduce.cu:44 'unhandled cuda error / '
 .. ArchLinux pid 6482: Test failure common.cu:377
 .. ArchLinux pid 6482: Test failure common.cu:584
 .. ArchLinux pid 6482: Test failure all_reduce.cu:90
 .. ArchLinux pid 6482: Test failure common.cu:613
 .. ArchLinux pid 6482: Test failure common.cu:1016
 .. ArchLinux pid 6482: Test failure common.cu:842
```


Best Regards,
Jack Lu

### sjeaugey · 2023-01-03

Seems NCCL is trying to use a libcuda.so which is not the one coming from the driver but an empty library only supposed to be used for compiling. 

### HenryJia · 2024-12-20

I'm also experiencing this. Any fixes?

### sjeaugey · 2024-12-20

This is a CUDA installation issue. Unfortunately I'm not an expert of Archlinux + CUDA. That should probably be asked on CUDA forums...

### sempervictus · 2025-07-02

Arch packages `nccl` separately from `cuda` - `pacman -S cuda nccl` to get both. Installation path for CUDA tends to be in /opt where a lot of applications still search but it does differ from the Canonical paths commonly used in production containers.
