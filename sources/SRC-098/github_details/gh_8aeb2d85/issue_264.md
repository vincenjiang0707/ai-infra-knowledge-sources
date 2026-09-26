# [Issue #264] Test CUDA failure common.cu:941 'system not yet initialized'

source: https://github.com/NVIDIA/nccl-tests/issues/264
state: open | updated: 2025-04-09T02:13:11Z
labels: 

## 正文

We have a server with 8 H100 GPU with cuda version 12.6 and nccl version 2.23.4.

When we are running nccl test as per the command provided in - https://github.com/nvidia/nccl-tests we are facing below issue.

[root@test nccl-tests-master]# ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 8
# nThread 1 nGpus 8 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
test: Test CUDA failure common.cu:941 'system not yet initialized'
 .. test pid 54340: Test failure common.cu:891

##################################################################

More info from nvidia-smi

[root@test nccl-tests-master]# nvidia-smi
Fri Nov  8 02:11:26 2024
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          Off |   00000000:19:00.0 Off |                    0 |
| N/A   38C    P0             70W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 80GB HBM3          Off |   00000000:3B:00.0 Off |                    0 |
| N/A   35C    P0             73W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H100 80GB HBM3          Off |   00000000:4C:00.0 Off |                    0 |
| N/A   32C    P0             71W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H100 80GB HBM3          Off |   00000000:5D:00.0 Off |                    0 |
| N/A   35C    P0             73W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H100 80GB HBM3          Off |   00000000:9B:00.0 Off |                    0 |
| N/A   38C    P0             73W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H100 80GB HBM3          Off |   00000000:BB:00.0 Off |                    0 |
| N/A   35C    P0             70W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H100 80GB HBM3          Off |   00000000:CB:00.0 Off |                    0 |
| N/A   37C    P0             72W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H100 80GB HBM3          Off |   00000000:DB:00.0 Off |                    0 |
| N/A   32C    P0             71W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

How to proceed further and run the nccl test suit??




## 评论 (7)

### sjeaugey · 2024-11-07

Looks like CUDA isn't functional; I'd run a simple CUDA test first and ensure it works before running the NCCL perf tests.

### vijayaramaraju-kalidindi · 2024-11-07

> Looks like CUDA isn't functional; I'd run a simple CUDA test first and ensure it works before running the NCCL perf tests.

I have run dgcm diagnostics. It says unable to initialize the CUDA library. How do we correct it??

sh-5.1# /usr/bin/dcgmi diag --run 3 --fail-early
Successfully ran diagnostic for group.
+---------------------------+------------------------------------------------+
| Diagnostic                | Result                                         |
+===========================+================================================+
|-----  Metadata  ----------+------------------------------------------------|
| DCGM Version              | 3.3.8                                          |
| Driver Version Detected   | 560.35.03                                      |
| GPU Device IDs Detected   | 2330,2330,2330,2330,2330,2330,2330,2330        |
|-----  Deployment  --------+------------------------------------------------|
| Denylist                  | Pass                                           |
| NVML Library              | Pass                                           |
| CUDA Main Library         | Pass                                           |
| Permissions and OS Blocks | Pass                                           |
| Persistence Mode          | Pass                                           |
| Info                      | Persistence mode for GPU 0 is disabled. Enabl  |
|                           | e persistence mode by running "nvidia-smi -i   |
|                           | <gpuId> -pm 1 " as root.,Persistence mode for  |
|                           |  GPU 1 is disabled. Enable persistence mode b  |
|                           | y running "nvidia-smi -i <gpuId> -pm 1 " as r  |
|                           | oot.,Persistence mode for GPU 2 is disabled.   |
|                           | Enable persistence mode by running "nvidia-sm  |
|                           | i -i <gpuId> -pm 1 " as root.,Persistence mod  |
|                           | e for GPU 3 is disabled. Enable persistence m  |
|                           | ode by running "nvidia-smi -i <gpuId> -pm 1 "  |
|                           |  as root.,Persistence mode for GPU 4 is disab  |
|                           | led. Enable pers                               |
| Environment Variables     | Pass                                           |
| Page Retirement/Row Remap | Pass                                           |
| Graphics Processes        | Pass                                           |
| Inforom                   | Pass                                           |
+-----  Integration  -------+------------------------------------------------+
| PCIe                      | Skip - All                                     |
+-----  Hardware  ----------+------------------------------------------------+
| GPU Memory                | Fail - All                                     |
| Warning                   | GPU 0 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 1 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 2 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 3 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 4 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 5 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 6 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
| Warning                   | GPU 7 Error using CUDA API cuInit Check DCGM   |
|                           | and system logs for errors. Reset GPU. Restar  |
|                           | t DCGM. Rerun diagnostics. Unable to initiali  |
|                           | ze CUDA library: 'system not yet initialized'  |
|                           | . . Please check if a CUDA sample program can  |
|                           |  be run successfully on this host. Refer to h  |
|                           | ttps://github.com/nvidia/cuda-samples          |
+-----  Stress  ------------+------------------------------------------------+
| Memory Bandwidth          | Skip - All                                     |
| EUD Test                  | Skip - All                                     |
+---------------------------+------------------------------------------------+


### vijayaramaraju-kalidindi · 2024-11-14

Mentioned issue was resolved post enabling fabric manger service. We have then ran NCCL tests with in the server successfully.

NCCL tests across the server still gives an issue.

We are using below command to run NCCL tests across 2 hosts, but command is not yielding any output. Even environment variables like NCC_DEBUG=INFO are not working as they are not giving any info output while running the command.

/usr/lib64/openmpi/bin/mpirun -x NCCL_DEBUG=INFO --bind-to numa -np 16 -H jm01gp1jiobrain02:8,jm01gp1jiobrain03:8 ./build/all_reduce_perf -b8 -e16G -f2 --mca btl tcp,self --mca btl_tcp_if_include bond0.1239

Note: NCCL tests are being run on baremetal hosts which has 8 H100 GPU per host with RHEL 9.4 OS.



### AddyLaddy · 2024-11-14

I would expect the command line to look more like this

```
/usr/lib64/openmpi/bin/mpirun -x NCCL_DEBUG=INFO --bind-to numa -np 16 -H jm01gp1jiobrain02:8,jm01gp1jiobrain03:8 \
 --mca btl tcp,self --mca btl_tcp_if_include bond0.1239 ./build/all_reduce_perf -b8 -e16G -f2
```

Can you also try compiling & running a simple MPI program such as:

https://raw.githubusercontent.com/pmodels/mpich/main/examples/cpi.c

on 16 processes across both nodes.

### vijayaramaraju-kalidindi · 2024-11-15

> I would expect the command line to look more like this
> 
> ```
> /usr/lib64/openmpi/bin/mpirun -x NCCL_DEBUG=INFO --bind-to numa -np 16 -H jm01gp1jiobrain02:8,jm01gp1jiobrain03:8 \
>  --mca btl tcp,self --mca btl_tcp_if_include bond0.1239 ./build/all_reduce_perf -b8 -e16G -f2
> ```
> 
> Can you also try compiling & running a simple MPI program such as:
> 
> https://raw.githubusercontent.com/pmodels/mpich/main/examples/cpi.c
> 
> on 16 processes across both nodes.

Hi,

Tried but didn't work. Got to know that command was not yielding output as host from where mpirun command is being ran is unable to autossh the target node. Post enabling auto ssh things worked.

### tedli · 2024-11-22

My case was caused by `nvidia-fabricmanager` fault.
Messages of nvidia-fabricmanager service is expressive enough to to figure out what wrong. After makes nvidia-fabricmanager happy, cuda work as expected.

### LiquidFLOPS · 2025-04-09

 Systemctl enable nvidia-fabricmanager is a must, otherwise after a gpu host reboot, you'll encounter this error during multi-node NCCL test. Recently I ran into this issue.
