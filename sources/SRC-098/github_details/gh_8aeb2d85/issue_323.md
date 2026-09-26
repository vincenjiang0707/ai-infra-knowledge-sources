# [Issue #323] NCCL runs with 1 GPU but with 2 GPUs gives 'invalid device ordinal'

source: https://github.com/NVIDIA/nccl-tests/issues/323
state: closed | updated: 2025-06-16T19:09:30Z
labels: 

## 正文

I have two nodes and can successfully run with 1 GPU on each node.  But when I run with 2 GPU per each node I get the 'invalid device ordinal' error.   I will show the successful run and the error run below.

`[root@nvidiatools-29-workload ~]$ mpirun --allow-run-as-root -H 192.168.10.1:1,192.168.10.2:1 -np 2 -bind-to none -map-by slot -mca pml ob1 -mca btl ^openib -mca btl_tcp_if_include 192.168.10.0/24 -mca plm_rsh_args "-p 20024" -x NCCL_IB_DISABLE=1 -x NCCL_DEBUG=VERSION -x NCCL_SOCKET_IFNAME=net1 -x NCCL_IB_HCA=mlx5_2,mlx5_8 -x UCX_NET_DEVICES=net1 -x NCCL_NET_GDR_READ=1 all_reduce_perf -b 8 -e 16G -f2 -g 1`

nThread 1 nGpus 1 minBytes 8 maxBytes 17179869184 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0

 Using devices
 Rank  0 Group  0 Pid  11004 on nvidiatools-29-workload device  0 [0000:61:00] NVIDIA L40S
  Rank  1 Group  0 Pid  11048 on nvidiatools-30-workload device  0 [0000:61:00] NVIDIA L40S

 Reducing maxBytes to 15534478677 due to memory limitation
NCCL version 2.27.3+cuda12.9

                                                             out-of-place                       in-place          
     size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
       (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    12.63    0.00    0.00      0    12.08    0.00    0.00      0
          16             4     float     sum      -1    11.99    0.00    0.00      0    12.07    0.00    0.00      0
          32             8     float     sum      -1    12.31    0.00    0.00      0    12.24    0.00    0.00      0
          64            16     float     sum      -1    12.19    0.01    0.01      0    12.19    0.01    0.01      0
         128            32     float     sum      -1    12.59    0.01    0.01      0    12.29    0.01    0.01      0
         256            64     float     sum      -1    12.49    0.02    0.02      0    12.53    0.02    0.02      0
         512           128     float     sum      -1    12.60    0.04    0.04      0    12.64    0.04    0.04      0
        1024           256     float     sum      -1    12.91    0.08    0.08      0    12.78    0.08    0.08      0
        2048           512     float     sum      -1    13.14    0.16    0.16      0    13.23    0.15    0.15      0
        4096          1024     float     sum      -1    14.03    0.29    0.29      0    13.96    0.29    0.29      0
        8192          2048     float     sum      -1    15.43    0.53    0.53      0    15.28    0.54    0.54      0
       16384          4096     float     sum      -1    17.72    0.92    0.92      0    17.64    0.93    0.93      0
       32768          8192     float     sum      -1    21.50    1.52    1.52      0    21.33    1.54    1.54      0
       65536         16384     float     sum      -1    29.66    2.21    2.21      0    29.24    2.24    2.24      0
      131072         32768     float     sum      -1    46.20    2.84    2.84      0    46.24    2.83    2.83      0
      262144         65536     float     sum      -1    83.70    3.13    3.13      0    82.99    3.16    3.16      0
      524288        131072     float     sum      -1    157.8    3.32    3.32      0    157.2    3.34    3.34      0
     1048576        262144     float     sum      -1    166.5    6.30    6.30      0    167.9    6.25    6.25      0
     2097152        524288     float     sum      -1    291.9    7.19    7.19      0    292.7    7.16    7.16      0
     4194304       1048576     float     sum      -1    554.0    7.57    7.57      0    553.8    7.57    7.57      0
     8388608       2097152     float     sum      -1   1072.5    7.82    7.82      0   1070.9    7.83    7.83      0
    16777216       4194304     float     sum      -1   2129.8    7.88    7.88      0   2131.3    7.87    7.87      0
  

`[root@nvidiatools-29-workload ~]$ mpirun --allow-run-as-root -H 192.168.10.1:2,192.168.10.2:2 -np 2 -bind-to none -map-by slot -mca pml ob1 -mca btl ^openib -mca btl_tcp_if_include 192.168.10.0/24 -mca plm_rsh_args "-p 20024" -x NCCL_IB_DISABLE=1 -x NCCL_DEBUG=VERSION -x NCCL_SOCKET_IFNAME=net1 -x NCCL_IB_HCA=mlx5_2,mlx5_8 -x UCX_NET_DEVICES=net1 -x NCCL_NET_GDR_READ=1 all_reduce_perf -b 8 -e 16G -f2 -g 2`

`nThread 1 nGpus 2 minBytes 8 maxBytes 17179869184 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0

Using devices
nvidiatools-29-workload: Test CUDA failure common.cu:1030 invalid device ordinal
nvidiatools-29-workload pid 11024: Test failure common.cu:937

Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.

mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[2153,1],1]
  Exit code:    2
`

I know two GPUs are visible because I can run nvidia-smi through the same mpi run command get the GPUS showing:

`[root@nvidiatools-29-workload ~]$ mpirun -mca coll_hcoll_enable 0 --allow-run-as-root  -H 192.168.10.1:2,192.168.10.2:2 -np 2 -mca plm_rsh_args "-p 20024" nvidia-smi`

Mon Jun 16 16:15:43 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
Mon Jun 16 16:15:43 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L40S                    On  |   00000000:61:00.0 Off |                    0 |
| N/A   27C    P8             34W /  350W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   0  NVIDIA L40S                    On  |   00000000:61:00.0 Off |                    0 |
| N/A   27C    P8             34W /  350W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA L40S                    On  |   00000000:E1:00.0 Off |                    0 |
| N/A   28C    P8             34W /  350W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|   1  NVIDIA L40S                    On  |   00000000:E1:00.0 Off |                    0 |
| N/A   28C    P8             34W /  350W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
`

So the question is what am I missing here?

## 评论 (1)

### schmaustech · 2025-06-16

I figured this out - I was setting the value of -g to 2 but also setting -H to the ipaddresses and :2.  If I leave the -H portion to :1 then it runs and I use all four of my GPUs .

`[root@nvidiatools-29-workload ~]# mpirun --allow-run-as-root -H 192.168.10.1:1,192.168.10.2:1 -np 2 -bind-to none -map-by slot -mca pml ob1 -mca btl ^openib -mca btl_tcp_if_include 192.168.10.0/24 -mca plm_rsh_args "-p 20024" -x NCCL_IB_DISABLE=1 -x NCCL_DEBUG=VERSION -x NCCL_SOCKET_IFNAME=net1 -x NCCL_IB_HCA=mlx5_2,mlx5_8 -x UCX_NET_DEVICES=net1 -x NCCL_NET_GDR_READ=1 all_reduce_perf -b 8 -e 16G -f2 -g 2`

nThread 1 nGpus 2 minBytes 8 maxBytes 17179869184 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0

Using devices
Rank  0 Group  0 Pid  11117 on nvidiatools-29-workload device  0 [0000:61:00] NVIDIA L40S
Rank  1 Group  0 Pid  11117 on nvidiatools-29-workload device  1 [0000:e1:00] NVIDIA L40S
Rank  2 Group  0 Pid  11270 on nvidiatools-30-workload device  0 [0000:61:00] NVIDIA L40S
Rank  3 Group  0 Pid  11270 on nvidiatools-30-workload device  1 [0000:e1:00] NVIDIA L40S

Reducing maxBytes to 15534478677 due to memory limitation
NCCL version 2.27.3+cuda12.9


I will leave this here in case someone else ever needs help.
