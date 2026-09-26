# [Issue #320] Test NCCL failure common.cu:1119 unhandled system error

source: https://github.com/NVIDIA/nccl-tests/issues/320
state: closed | updated: 2025-06-13T18:13:59Z
labels: 

## 正文

Hi there, I have been running into the unhandled system error trying to use nccl in a 3 gpu setup.  This is the nvidia-smi log:
```
$ nvidia-smi
Thu Jun 12 16:51:17 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A6000               On  |   00000000:81:00.0 Off |                  Off |
| 30%   27C    P8             25W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX A6000               On  |   00000000:A1:00.0 Off |                  Off |
| 30%   26C    P8             24W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX A6000               On  |   00000000:C1:00.0 Off |                  Off |
| 30%   26C    P8             21W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

Running `all_reduce_perf` results in the following error:
```
$ NCCL_DEBUG=TRACE ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 3
# nThread 1 nGpus 3 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 842624 on    gpu0301 device  0 [0000:81:00] NVIDIA RTX A6000
#  Rank  1 Group  0 Pid 842624 on    gpu0301 device  1 [0000:a1:00] NVIDIA RTX A6000
#  Rank  2 Group  0 Pid 842624 on    gpu0301 device  2 [0000:c1:00] NVIDIA RTX A6000
gpu0301:842624:842624 [0] NCCL INFO Bootstrap: Using int0:10.0.5.121<0>
gpu0301:842624:842624 [0] NCCL INFO cudaDriverVersion 12060
gpu0301:842624:842624 [0] NCCL INFO NCCL version 2.26.2+cuda12.6
gpu0301:842624:842643 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal net plugin.
gpu0301:842624:842643 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB int0:10.0.5.121<0>
gpu0301:842624:842643 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu0301:842624:842643 [0] NCCL INFO Using network IB
gpu0301:842624:842644 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu0301:842624:842644 [1] NCCL INFO Using network IB

[2025-06-12 16:57:52] gpu0301:842624:842643 [0] misc/nvmlwrap.cc:74 NCCL WARN Failed to open libnvidia-ml.so.1
gpu0301:842624:842643 [0] NCCL INFO misc/nvmlwrap.cc:200 -> 2
gpu0301:842624:842643 [0] NCCL INFO init.cc:355 -> 2
gpu0301:842624:842643 [0] NCCL INFO init.cc:1397 -> 2
gpu0301:842624:842644 [1] NCCL INFO misc/nvmlwrap.cc:200 -> 2
gpu0301:842624:842644 [1] NCCL INFO init.cc:355 -> 2
gpu0301:842624:842644 [1] NCCL INFO init.cc:1397 -> 2
gpu0301:842624:842644 [1] NCCL INFO group.cc:75 -> 2 [Async thread]
gpu0301:842624:842643 [0] NCCL INFO group.cc:75 -> 2 [Async thread]
gpu0301:842624:842645 [2] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu0301:842624:842645 [2] NCCL INFO Using network IB
gpu0301:842624:842645 [2] NCCL INFO misc/nvmlwrap.cc:200 -> 2
gpu0301:842624:842645 [2] NCCL INFO init.cc:355 -> 2
gpu0301:842624:842645 [2] NCCL INFO init.cc:1397 -> 2
gpu0301:842624:842645 [2] NCCL INFO group.cc:75 -> 2 [Async thread]
gpu0301:842624:842624 [2] NCCL INFO group.cc:422 -> 2
gpu0301:842624:842624 [2] NCCL INFO group.cc:581 -> 2
gpu0301:842624:842624 [2] NCCL INFO init.cc:1791 -> 2
gpu0301: Test NCCL failure common.cu:1119 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '
 .. gpu0301 pid 842624: Test failure common.cu:937
```

This is what the topology looks like:
```
[nccl-tests]$ nvidia-smi topo -m
        GPU0    GPU1    GPU2    NIC0    NIC1    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV4     NODE    NODE    NODE    64-71   1               N/A
GPU1    NV4      X      NODE    NODE    NODE    64-71   1               N/A
GPU2    NODE    NODE     X      PHB     PHB     64-71   1               N/A
NIC0    NODE    NODE    PHB      X      PIX
NIC1    NODE    NODE    PHB     PIX      X

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
```

The network interfaces look like this:
```
[nccl-tests]$ ifconfig
enp226s0f0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether xx:xx:xx:xx:xx:xx  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xa3420000-a343ffff

enp226s0f1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether xx:xx:xx:xx:xx:xx  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device memory 0xa3400000-a341ffff

ibp194s0f1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 4092
Infiniband hardware address can be incorrect! Please read BUGS section in ifconfig(8).
        infiniband xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx  txqueuelen 256  (InfiniBand)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

int0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9000
        inet 10.0.5.121  netmask 255.255.248.0  broadcast 10.0.7.255
        inet6 xxxx::xxxx:xxxx:xxxx:xxxx  prefixlen 64  scopeid 0x20<link>
        ether xx:xx:xx:xx:xx:xx  txqueuelen 1000  (Ethernet)
        RX packets 158176424  bytes 578482990188 (538.7 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 52775595  bytes 165543394561 (154.1 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 16602685  bytes 1337339100 (1.2 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16602685  bytes 1337339100 (1.2 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
Any help or direction is greatly appreciated.
Thanks

## 评论 (2)

### sjeaugey · 2025-06-13

It looks like your system has a CUDa installation problem:
```
[2025-06-12 16:57:52] gpu0301:842624:842643 [0] misc/nvmlwrap.cc:74 NCCL WARN Failed to open libnvidia-ml.so.1
```
The NVML library should be there and functional. Other things might also be broken, so I'd suggest to check the CUDA install.

### Pkoiralap · 2025-06-13

@sjeaugey thanks for the response. It was indeed because of a missing file. I ended up making it work by loading it with `LD_PRELOAD=/usr/lib64/libnvidia-ml.so.1`.

Thanks again for the help.
