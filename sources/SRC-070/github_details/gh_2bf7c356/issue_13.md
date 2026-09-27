# [Issue #13] Test fail use 2node on tests/test_internode.py

source: https://github.com/deepseek-ai/DeepEP/issues/13
state: closed | updated: 2026-08-12T13:27:43Z
labels: 

## 正文

script:
```
MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=0 python tests/test_internode.py
MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=1 python tests/test_internode.py
```

generate log:
```
[config] num_tokens=4096, hidden=7168, num_topk_groups=2, num_topk=8
[layout] Kernel performance: 0.068 ms

[testing] Running with BF16, without top-k (async=True, previous=True) ...Global rank: 13, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 15, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 10, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 12, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 9, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
Global rank: 11, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[15]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 8, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
Global rank: 14, num_recv_tokens: -1, num_rdma_recv_tokens: -1
moe_recv_expert_counter[0]: -1
moe_recv_expert_counter[1]: -1
moe_recv_expert_counter[2]: -1
moe_recv_expert_counter[3]: -1
moe_recv_expert_counter[4]: -1
moe_recv_expert_counter[5]: -1
moe_recv_expert_counter[6]: -1
moe_recv_expert_counter[7]: -1
moe_recv_expert_counter[8]: -1
moe_recv_expert_counter[9]: -1
moe_recv_expert_counter[10]: -1
moe_recv_expert_counter[11]: -1
moe_recv_expert_counter[12]: -1
moe_recv_expert_counter[13]: -1
moe_recv_expert_counter[14]: -1
moe_recv_expert_counter[15]: -1
W0225 17:27:34.774000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75292 via signal SIGTERM
W0225 17:27:34.775000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75293 via signal SIGTERM
W0225 17:27:34.775000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75294 via signal SIGTERM
W0225 17:27:34.775000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75295 via signal SIGTERM
W0225 17:27:34.776000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75296 via signal SIGTERM
W0225 17:27:34.776000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75297 via signal SIGTERM
W0225 17:27:34.776000 75225 site-packages/torch/multiprocessing/spawn.py:169] Terminating process 75298 via signal SIGTERM
Traceback (most recent call last):
  File "/root/tmp/code/DeepEP/tests/test_internode.py", line 247, in <module>
    torch.multiprocessing.spawn(test_loop, args=(num_processes, ), nprocs=num_processes)
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/torch/multiprocessing/spawn.py", line 340, in spawn
    return start_processes(fn, args, nprocs, join, daemon, start_method="spawn")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/torch/multiprocessing/spawn.py", line 296, in start_processes
    while not context.join():
              ^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/torch/multiprocessing/spawn.py", line 215, in join
    raise ProcessRaisedException(msg, error_index, failed_process.pid)
torch.multiprocessing.spawn.ProcessRaisedException:

-- Process 7 terminated with the following error:
Traceback (most recent call last):
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/torch/multiprocessing/spawn.py", line 90, in _wrap
    fn(i, *args)
  File "/root/tmp/code/DeepEP/tests/test_internode.py", line 235, in test_loop
    test_main(i, local_rank, num_local_ranks, num_ranks, num_nodes, rank, buffer, group)
  File "/root/tmp/code/DeepEP/tests/test_internode.py", line 109, in test_main
    recv_x, recv_topk_idx, recv_topk_weights, recv_num_tokens_per_expert_list, handle, event = buffer.dispatch(**dispatch_args)
                                                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/deep_ep-1.0.0+ebfe47e-py3.12-linux-x86_64.egg/deep_ep/buffer.py", line 288, in dispatch
    return self.internode_dispatch(x, handle, num_tokens_per_rank, num_tokens_per_rdma_rank, is_token_in_rank, num_tokens_per_expert,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/anaconda3/envs/cogvideox/lib/python3.12/site-packages/deep_ep-1.0.0+ebfe47e-py3.12-linux-x86_64.egg/deep_ep/buffer.py", line 396, in internode_dispatch
    recv_src_meta, send_rdma_head, send_nvl_head, event = self.runtime.internode_dispatch(
                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: DeepEP error: timeout (dispatch CPU)
```
This error is in `csrc/deep_ep.cpp` [L765](https://github.com/deepseek-ai/DeepEP/blob/1a0a8bda09d627e67c787795aa2d984bd63dde27/csrc/deep_ep.cpp#L765C8-L787C10)
It is caught and thrown after timeout. How to analyze the specific problem?

## 评论 (11)

### Desperadoze · 2025-02-25

hello，can I ask you how you compile nvshmem,my gdrcopy_copybw had data performence,but when compile  nvshmem,I can't find the path of gdrcopy.it's different with gdrcopy_copybw?

### xesdiny · 2025-02-25

> helloО╪▄can I ask you how you compile nvshmem,my gdrcopy_copybw had data performence,but when compile nvshmem,I can't find the path of gdrcopy.it's different with gdrcopy_copybw?


1.install gdrcopy
when you has installed,
check your compile gdrcopy version.
```
ls /var/lib/dkms/gdrdrv/
```
1.2 Soft link full path
```
cd /var/lib/dkms/gdrdrv/
sudo ln -s  /var/lib/dkms/gdrdrv/2.5/ 2.5-1
```
1.3 install deb package
```
cd gdrcopy/packages
sudo dpkg -i gdrdrv-dkms_2.5-1_amd64.Ubuntu20_04.deb libgdrapi_2.5-1_amd64.Ubuntu20_04.deb gdrcopy-tests_2.5-1_amd64.Ubuntu20_04+cuda12.0.deb gdrcopy_2.5-1_amd64.Ubuntu20_04.deb
```

2.install nvshmem_src
2.1Enable IBGDA by modifying &Update kernel configuration:
2.2 build
cd nvshmem_src
```
CUDA_HOME=/usr/local/cuda \
**GDRCOPY_HOME=/opt/gdrcopy** \
NVSHMEM_SHMEM_SUPPORT=0 \
NVSHMEM_UCX_SUPPORT=0 \
NVSHMEM_USE_NCCL=0 \
NVSHMEM_IBGDA_SUPPORT=1 \
NVSHMEM_PMIX_SUPPORT=0 \
NVSHMEM_TIMEOUT_DEVICE_POLLING=0 \
NVSHMEM_USE_GDRCOPY=1 \
cmake -S . -B build/ \
**-DCMAKE_INSTALL_PREFIX=/opt/nvshme**


### HanHan009527 · 2025-02-25

I think the script should be
MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=0 python tests/test_internode.py
MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=1 python tests/test_internode.py

### xesdiny · 2025-02-25

> I think the script should be MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=0 python tests/test_internode.py MASTER_ADDR=WL0 WORLD_SIZE=2 RANK=1 python tests/test_internode.py

Yeah, there's a little glitch in my paste run script.

### haswelliris · 2025-02-25

It appears that you are experiencing network connectivity issues. Please provide additional information, including:

- **Operating system**: 
- **GPU and NIC driver version**: 
- **CUDA version**: 

Additionally, include hardware details, such as:

- **Network card**: ibstatus
- **GPU topology**:  nvidia-smi topo -m

Furthermore, please share the results of the following reports, if available:

- **`gdrcopy_copybw` report**: 
- **`nvshmem perftest` report**:

### xesdiny · 2025-03-03

@haswelliris 
Operating system: ubuntu 20.04
GPU and NIC driver version:
A100-SXM 525.105.17,  NVSHMEM v3.1.7
CUDA Version: 12.1
Network card:
```
Infiniband device 'mlx5_0' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:dcd8
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_1' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:dcd9
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_2' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:eb34
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_3' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:eb35
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_4' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:eb28
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_5' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:eb29
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_6' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:e3cc
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet

Infiniband device 'mlx5_7' port 1 status:
        default gid:     fe80:0000:0000:0000:1270:fdff:fe5d:e3cd
        base lid:        0x0
        sm lid:          0x0
        state:           4: ACTIVE
        phys state:      5: LinkUp
        rate:            100 Gb/sec (4X EDR)
        link_layer:      Ethernet
```

GPU topology
```
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    NIC4    NIC5    NIC6    NIC7    CPU Affinity    NUMA Affinity
GPU0     X      NV12    NV12    NV12    NV12    NV12    NV12    NV12    PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS     0-31,64-95      0
GPU1    NV12     X      NV12    NV12    NV12    NV12    NV12    NV12    PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS     0-31,64-95      0
GPU2    NV12    NV12     X      NV12    NV12    NV12    NV12    NV12    NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     0-31,64-95      0
GPU3    NV12    NV12    NV12     X      NV12    NV12    NV12    NV12    NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     0-31,64-95      0
GPU4    NV12    NV12    NV12    NV12     X      NV12    NV12    NV12    SYS     SYS     SYS     SYS     PXB     PXB     NODE    NODE    32-63,96-127    1
GPU5    NV12    NV12    NV12    NV12    NV12     X      NV12    NV12    SYS     SYS     SYS     SYS     PXB     PXB     NODE    NODE    32-63,96-127    1
GPU6    NV12    NV12    NV12    NV12    NV12    NV12     X      NV12    SYS     SYS     SYS     SYS     NODE    NODE    PXB     PXB     32-63,96-127    1
GPU7    NV12    NV12    NV12    NV12    NV12    NV12    NV12     X      SYS     SYS     SYS     SYS     NODE    NODE    PXB     PXB     32-63,96-127    1
NIC0    PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS      X      PIX     NODE    NODE    SYS     SYS     SYS     SYS
NIC1    PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS     PIX      X      NODE    NODE    SYS     SYS     SYS     SYS
NIC2    NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     NODE    NODE     X      PIX     SYS     SYS     SYS     SYS
NIC3    NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     NODE    NODE    PIX      X      SYS     SYS     SYS     SYS
NIC4    SYS     SYS     SYS     SYS     PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS      X      PIX     NODE    NODE
NIC5    SYS     SYS     SYS     SYS     PXB     PXB     NODE    NODE    SYS     SYS     SYS     SYS     PIX      X      NODE    NODE
NIC6    SYS     SYS     SYS     SYS     NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     NODE    NODE     X      PIX
NIC7    SYS     SYS     SYS     SYS     NODE    NODE    PXB     PXB     SYS     SYS     SYS     SYS     NODE    NODE    PIX      X

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
  NIC2: mlx5_2
  NIC3: mlx5_3
  NIC4: mlx5_4
  NIC5: mlx5_5
  NIC6: mlx5_6
  NIC7: mlx5_7
```

gdrcopy_copybw
```
GPU id:0; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:5b:00
GPU id:1; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:5e:00
GPU id:2; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:75:00
GPU id:3; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:78:00
GPU id:4; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:9d:00
GPU id:5; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:a1:00
GPU id:6; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:f5:00
GPU id:7; name: NVIDIA A100-SXM4-80GB; Bus id: 0000:f9:00
selecting device 0
testing size: 131072
rounded size: 131072
gpu alloc fn: cuMemAlloc
device ptr: 7f85e3200000
map_d_ptr: 0x7f86068b3000
info.va: 7f85e3200000
info.mapped_size: 131072
info.page_size: 65536
info.mapped: 1
info.wc_mapping: 1
page offset: 0
user-space pointer:0x7f86068b3000
writing test, size=131072 offset=0 num_iters=10000
write BW: 20084.5MB/s
reading test, size=131072 offset=0 num_iters=100
read BW: 434.413MB/s
unmapping buffer
unpinning buffer
closing gdrdrv
```

nvshmem perftest report:
```
 ucx_perftest -d mlx5_0:1 10.117.71.211 -t tag_bw

+--------------+--------------+-----------------------------+---------------------+-----------------------+
|              |              |      overhead (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+---------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | typical | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+---------+---------+---------+----------+----------+-----------+-----------+
Final:               1000000     0.039     0.125     0.125       60.84      60.84     7974856     7974856

 ucx_perftest -d mlx5_0:1 -t tag_bw
Waiting for connection...
+------------------------------------------------------------------------------------------+
| API:          protocol layer                                                             |
| Test:         tag match bandwidth                                                        |
| Data layout:  (automatic)                                                                |
| Send memory:  host                                                                       |
| Recv memory:  host                                                                       |
| Message size: 8                                                                          |
+------------------------------------------------------------------------------------------+
```

### haswelliris · 2025-03-03

@xesdiny 
1. Your NVSHMEM perftest configuration appears to be incorrect. It seems to be running `ucx_perftest` locally (self-to-self) and is utilizing CPU host memory. 
To properly test NVSHMEM performance, you can find the `perftest` directory in your NVSHMEM installation path. After building it with CMake, you can run the `device/pt-to-pt/shmem_put_bw` test for accurate GPU-to-GPU performance measurements.
3. It appears that you are using a RoCE network. Please verify the following settings:   
  - Proper IP and network interface configuration.     
  - For RoCE, ensure the following settings are correctly configured:  
     * `NVSHMEM_IB_GID_INDEX`  
     * `NVSHMEM_IB_TRAFFIC_CLASS`  


### renwuli · 2025-03-07

hi @haswelliris  I have 8 Hopper GPUs and 4 50GB/s Mellanox CX7 NICs per node, NCCL 2 node allreduce busbw can achieve 193GB/, I following the deepep guide and run test_intranode.py, but the performance is extramely low (while intranode is normal), do you have any ideas?

[tuning] Best dispatch (FP8): SMs 24, NVL chunk 12, RDMA chunk 12: 5.36 GB/s (RDMA), 17.49 GB/s (NVL)
[tuning] Best dispatch (BF16): SMs 24, NVL chunk 16, RDMA chunk 8: 5.51 GB/s (RDMA), 17.99 GB/s (NVL)
[tuning] Best combine: SMs 24, NVL chunk 1, RDMA chunk 20: 6.45 GB/s (RDMA), 21.05 GB/s (NVL)

### zhangml · 2025-03-19

I encountered the same issue. Could you please explain how you resolved it and what the cause was? @xesdiny 

### juinshell · 2026-03-02

same issue, did you fix it? @zhangml 

### fanfanaaaa · 2026-08-12

same issue, did you fix it? @juinshell 

