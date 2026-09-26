# [Issue #338] Test CUDA failure common.cu:1030 'system not yet initialized'

source: https://github.com/NVIDIA/nccl-tests/issues/338
state: closed | updated: 2025-09-05T01:29:26Z
labels: 

## 正文

Hi

I recently run nccl_perf_test between two nodes which each has one H20, but I get this error:

```
# Using devices
gpu: Test CUDA failure common.cu:1030 'system not yet initialized'
 .. gpu pid 3018: Test failure common.cu:937
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
An MPI communication peer process has unexpectedly disconnected.  This
usually indicates a failure in the peer process (e.g., a crash or
otherwise exiting without calling MPI_FINALIZE first).

Although this local MPI process will likely now behave unpredictably
(it may even hang or crash), the root cause of this problem is the
failure of the peer -- that is what you need to investigate.  For
example, there may be a core file that you can examine.  More
generally: such peer hangups are frequently caused by application bugs
or other external events.

  Local host: gpu
  Local PID:  4870
  Peer host:  gpu
--------------------------------------------------------------------------
--------------------------------------------------------------------------
mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[58461,1],0]
  Exit code:    2
--------------------------------------------------------------------------
```

This is my environment on both node:
OS: Ubuntu 22.04
kernel: 5.15.0-119-generic
nccl test version: 2.16.4
nvcc -V:
```
root@gpu:/home/gpu/nccl-tests-2.16.4/src# nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Tue_Feb_27_16:19:38_PST_2024
Cuda compilation tools, release 12.4, V12.4.99
Build cuda_12.4.r12.4/compiler.33961263_0
```

nvidia-smi:
```
root@gpu:/home/gpu/nccl-tests-2.16.4/src# nvidia-smi
Wed Aug 13 14:33:34 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H20                     Off |   00000000:09:00.0 Off |                    0 |
| N/A   29C    P0            112W /  500W |       0MiB /  97871MiB |     10%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

libnccl version

```
ii  libnccl-dev                            2.27.7-1+cuda12.4                            amd64        NVIDIA Collective Communication Library (NCCL) Development Files
ii  libnccl2                               2.27.7-1+cuda12.4                            amd64        NVIDIA Collective Communication Library (NCCL) Runtime
```

Do you have any idea why this error occurs?
Thank you in advance!!

## 评论 (2)

### kiskra-nvidia · 2025-08-13

Does CUDA work on this system at all? E.g., can you run anything from [cuda-samples](https://github.com/nvidia/cuda-samples)? Because, as far as I can tell, it's the very first CUDA call in NCCL tests that's failing...

### rucawang · 2025-08-15

@kiskra-nvidia Thank you for the reply.
I solve the problem and share my case below.

Actually, I use two VM to tun nccl test and get the error. I try to run cuda-samples,on each VM, one pass and the other fails.
Then I check the fabric manager on hosts, one is running and the other fails. 
The reason is that fabric manager version **not same as** the driver version. After I keep them same, fabric manager is running, and nccl test runs successfully.

