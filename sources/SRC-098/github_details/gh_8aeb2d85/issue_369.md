# [Issue #369] running multi-node with Exclusive Process

source: https://github.com/NVIDIA/nccl-tests/issues/369
state: open | updated: 2026-01-26T07:53:07Z
labels: 

## 正文

When running `all_reduce_perf` across 2 nodes / 4 GH200 GPUs per node I run into trouble: nccl-tests tell me GPUs are busy, although they are not. I have the following SLURM job:
```
#SBATCH --ntasks-per-node=4 --gpus-per-node=4 --nodes=2
srun ./build/all_reduce_perf -b 8 -e 128M -f 2
```
The output looks good in the start, but then the program fails:
```
# nccl-tests version 2.17.8 nccl-headers=22606 nccl-library=22606
# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 3617715 on    gpu-1-1 device  0 [0009:01:00] NVIDIA GH200 120GB
#  Rank  1 Group  0 Pid 3617716 on    gpu-1-1 device  1 [0019:01:00] NVIDIA GH200 120GB
#  Rank  2 Group  0 Pid 3617717 on    gpu-1-1 device  2 [0029:01:00] NVIDIA GH200 120GB
#  Rank  3 Group  0 Pid 3617718 on    gpu-1-1 device  3 [0039:01:00] NVIDIA GH200 120GB
#  Rank  4 Group  0 Pid 3230358 on    gpu-1-7 device  0 [0009:01:00] NVIDIA GH200 120GB
#  Rank  5 Group  0 Pid 3230359 on    gpu-1-7 device  1 [0019:01:00] NVIDIA GH200 120GB
#  Rank  6 Group  0 Pid 3230360 on    gpu-1-7 device  2 [0029:01:00] NVIDIA GH200 120GB
#  Rank  7 Group  0 Pid 3230361 on    gpu-1-7 device  3 [0039:01:00] NVIDIA GH200 120GB
gpu-1-1: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-1 pid 3617715: Test failure common.cu:1189
gpu-1-7: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-7 pid 3230359: Test failure common.cu:1189
gpu-1-7: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-7 pid 3230361: Test failure common.cu:1189
gpu-1-7: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-7 pid 3230358: Test failure common.cu:1189
gpu-1-7: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-7 pid 3230360: Test failure common.cu:1189
gpu-1-1: Test CUDA failure common.cu:1304 'CUDA-capable device(s) is/are busy or unavailable'
 .. gpu-1-1 pid 3617718: Test failure common.cu:1189
```
Now, my GPUs are configured with `Exclusive process`, so multiple processes cannot use one GPU. I guess this is what is happening in nccl-tests, because when I change to `Default`:
```
nvidia-smi -i 0,1,2,3 -c 0
```
the test runs through. Inspection with `nvidia-smi` shows that indeed, many processes use GPU0:
```
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A   3203007      C   ...ests-2.17.8/./build/all_reduce_perf        788MiB |
|    0   N/A  N/A   3203008      C   ...ests-2.17.8/./build/all_reduce_perf        556MiB |
|    0   N/A  N/A   3203009      C   ...ests-2.17.8/./build/all_reduce_perf        556MiB |
|    0   N/A  N/A   3203010      C   ...ests-2.17.8/./build/all_reduce_perf        556MiB |
|    1   N/A  N/A   3203008      C   ...ests-2.17.8/./build/all_reduce_perf        790MiB |
|    2   N/A  N/A   3203009      C   ...ests-2.17.8/./build/all_reduce_perf        786MiB |
|    3   N/A  N/A   3203010      C   ...ests-2.17.8/./build/all_reduce_perf        784MiB |
+-----------------------------------------------------------------------------------------+
```
Or rather, the 3 processes that should use GPUs 1,2,3 also in addition have a process running on GPU 0.

Is it possible to run nccl-tests with `Exclusive process`? Or do I have to consider changing that setting on the system? Also, do you know if this is this only `nccl-tests` limitation, or a general `nccl` issue?

## 评论 (18)

### sjeaugey · 2026-01-21

This looks like a bug, which we may have fixed. Can you try with a newer version?

### angainor · 2026-01-21

@sjeaugey so git main? I was running with 2.17.8 - that's the newest I can find. I also tried with an earlier 2.14.1.

### angainor · 2026-01-21

@sjeaugey I see the same behavior with `main`.

### sjeaugey · 2026-01-21

So you ran with NCCL 2.29 and the latest NCCL perf tests?

### angainor · 2026-01-21

I ran with NCCL/2.26.6 and latest perf tests. I can try newer NCCL and report back, if you think this will help.

### sjeaugey · 2026-01-21

Ok thanks. I remember such a bug in the past which was fixed, that's why I wanted to try something more recent. 2.26 should be recent enough.

We should try to repro and confirm whether we see the same or not.

EDIT: I tried on a random machine with NCCL 2.26.6 and the latest NCCL tests and I could not see the same problem. So either it's related to that specific platform, or something else is going on. 

### angainor · 2026-01-22

@sjeaugey FYI, I have tested now with NCCL/2.29.2 and `nccl-tests:main` and the behavior is the same.

### sjeaugey · 2026-01-22

I still can't reproduce, even on a similar system. Did you set any environment variable which could alter the behavior of the NCCL library or the NCCL test?

### angainor · 2026-01-22

Interesting. I guess I should describe the system better. This is a Cray EX system. I am compiling `ncc-tests` using OpenMPI with libfabric support. There are a bunch of envars set:
```
NCCL_NET_GDR_LEVEL=PHB
OMPI_MCA_mtl=ofi
OMPI_MCA_pml=cm
OMPI_MCA_ras_base_launch_orted_on_hn=1
PRTE_MCA_ras_base_launch_orted_on_hn=1
FI_CXI_RX_MATCH_MODE=hybrid
FI_PROVIDER=cxi
```
I start the tests as follows:
```
#SBATCH --ntasks-per-node=4 --gpus-per-node=4 --nodes=2
srun ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 1
```
I will also test with the Cray MPI instead and let you know.

### angainor · 2026-01-22

Note that this is a Slingshot11 system, where you have to run the jobs through SLURM in order for the interconnect to work.

### angainor · 2026-01-22

@sjeaugey Yes, that's it - compiled with Cray MPI and started with srun - all works fine with `Exclusive process`. There is only 1 process per GPU at any time. But compiled with OpenMPI and started with srun I see this problem.

### angainor · 2026-01-22

@sjeaugey Not sure this is relevant, but OpenMPI expects `cudaChooseDevice(), cudaSetDevice()`, etc. to be called _before_ `MPI_Init`. Maybe in `nccl-tests` it's done later?

### sjeaugey · 2026-01-22

I see. I've been using Open MPI in my experiments. But I'm also not using the same network plugin. Could it be the network plugin could be allocating GPU resources before the device is set?

### angainor · 2026-01-23

@sjeaugey Thanks a lot - that was helpful. I think OpenMPI + libfabric does something during the initialization that is incompatible with either NCCL, or nccl-tests. A solution (workaround?) to this is to turn off HMEM support in the OFI mtl:
```
export OMPI_MCA_mtl_ofi_disable_hmem=true
```
or to not use the OFI mtl at all, e.g.
```
export OMPI_MCA_pml=ob1
export OMPI_MCA_btl=tcp,sm,self
```
I guess both solutions have their issues for hybrid NCCL-MPI applications. Do you have any thoughts on this?

### sjeaugey · 2026-01-23

I'd need to fully understand which SW part allocates the CUDA resources/context and why, to be able to reason on how to solve this.

Maybe it would be useful to report this issue to the aws-ofi-nccl project, as they may have a better understanding of the full picture including how CUDA-aware Open MPI + OFI works.

Other than that, the best would be to report this issue to your vendor, as they are in the best position to reproduce the issue and coordinate a fix between the different projects.

### angainor · 2026-01-23

@sjeaugey One more question. I ran the tests now with newest libfabric / aws-ofi-nccl / nccl, and it seems that 1/3 of the runs fail with some `#wrong` transfers. What's interesting is, this happens for both Cray MPI, and OpenMPI, and it seems in 99% of the cases it fails for one particular problem size (`1048576`), e.g., :
```
# nccl-tests version 2.17.8 nccl-headers=22902 nccl-library=22902
# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 662195 on    gpu-1-1 device  0 [0009:01:00] NVIDIA GH200 120GB
#  Rank  1 Group  0 Pid 2448661 on    gpu-1-7 device  0 [0009:01:00] NVIDIA GH200 120GB
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong 
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)         
           8             2     float     sum      -1    17.49    0.00    0.00       0    16.41    0.00    0.00       0
          16             4     float     sum      -1    16.08    0.00    0.00       0    16.04    0.00    0.00       0
          32             8     float     sum      -1    16.59    0.00    0.00       0    17.58    0.00    0.00       0
          64            16     float     sum      -1    17.63    0.00    0.00       0    16.97    0.00    0.00       0
         128            32     float     sum      -1    18.25    0.01    0.01       0    18.02    0.01    0.01       0
         256            64     float     sum      -1    18.84    0.01    0.01       0    18.51    0.01    0.01       0
         512           128     float     sum      -1    18.27    0.03    0.03       0    18.43    0.03    0.03       0
        1024           256     float     sum      -1    18.94    0.05    0.05       0    18.62    0.06    0.06       0
        2048           512     float     sum      -1    19.27    0.11    0.11       0    19.32    0.11    0.11       0
        4096          1024     float     sum      -1    19.79    0.21    0.21       0    19.52    0.21    0.21       0
        8192          2048     float     sum      -1    21.04    0.39    0.39       0    20.48    0.40    0.40       0
       16384          4096     float     sum      -1    24.21    0.68    0.68       0    24.55    0.67    0.67       0
       32768          8192     float     sum      -1    29.02    1.13    1.13       0    27.27    1.20    1.20       0
       65536         16384     float     sum      -1    45.91    1.43    1.43       0    49.37    1.33    1.33       0
      131072         32768     float     sum      -1    89.43    1.47    1.47       0    86.11    1.52    1.52       0
      262144         65536     float     sum      -1   244.70    1.07    1.07       0   557.18    0.47    0.47       0
      524288        131072     float     sum      -1   377.76    1.39    1.39       0   327.38    1.60    1.60       0
     1048576        262144     float     sum      -1   477.32    2.20    2.20      96   492.81    2.13    2.13      32
     2097152        524288     float     sum      -1   338.61    6.19    6.19       0   351.38    5.97    5.97       0
     4194304       1048576     float     sum      -1   787.11    5.33    5.33       0   404.71   10.36   10.36       0
     8388608       2097152     float     sum      -1   785.48   10.68   10.68       0   773.37   10.85   10.85       0
    16777216       4194304     float     sum      -1   891.09   18.83   18.83       0   876.17   19.15   19.15       0
    33554432       8388608     float     sum      -1  1587.57   21.14   21.14       0  1572.73   21.34   21.34       0
    67108864      16777216     float     sum      -1  3003.09   22.35   22.35       0  3017.06   22.24   22.24       0
   134217728      33554432     float     sum      -1  5869.38   22.87   22.87       0  5886.67   22.80   22.80       0
# Out of bounds values : 4 FAILED
# Avg bus bandwidth    : 4.79995 
#
# Collective test concluded: all_reduce_perf
#

 .. gpu-1-1 pid 662195: Test failure common.cu:1189
 .. gpu-1-7 pid 2448661: Test failure common.cu:1189
```
Does this mean the data was not transferred correctly? Some synchronization issue? I guess I have to report this to either `libfabric`, or better `aws-ofi-nccl`, but I just wanted to know your opinion on what this might be caused by. Thanks!

### angainor · 2026-01-23

I forgot to mention that I do not see this with an older version of libfabric provided by HPE. Just with recent versions that I compile.

### sjeaugey · 2026-01-26

Indeed that's not good. It could be a bug in any layer, from NCCL down to libfabrics. But I would suggest to start from libfabric if switching different versions makes a difference.
