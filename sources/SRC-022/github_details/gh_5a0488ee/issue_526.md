# [Issue #526] Distributed data parallel training stalls with ROCm 5.0.2

source: https://github.com/ROCm/rccl/issues/526
state: closed | updated: 2024-04-01T16:26:41Z
labels: 

## 正文

Distributed data parallel training hangs using pytorch with the ROCm 5.0.2 release when training on more than one node.

I am testing on OLCF crusher with eight MI250x GPUs in one node https://docs.olcf.ornl.gov/systems/crusher_quick_start_guide.html

However, the behavior can be exhibited when only using 1 GPU per node on two nodes.

Minimal reproducer script (`harness.py`)

```
import os
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.optim as optim

if __name__ == '__main__':
    local_rank = 0
    if 'LOCAL_RANK' in os.environ:
        local_rank = int(os.environ["LOCAL_RANK"])

    torch.cuda.set_device(local_rank)
    print('Initialized GPU {}'.format(local_rank))

    dist.init_process_group(backend='nccl')
    print('Initialized process group on rank {}'.format(dist.get_rank()))

    rank = dist.get_rank()
    tensor_sizes = []
    k = 1
    for i in range(16):
        tensor_sizes.append(k)
        k*=2

    for tensor_size in tensor_sizes:
        print(tensor_size)
        model = torch.nn.Linear(tensor_size, tensor_size).to(local_rank)
        ddp_model = DDP(model, device_ids=[local_rank])
        optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

        tensor = torch.tensor(range(tensor_size), dtype=torch.float32).cuda(
            local_rank)
        ddp_model(tensor).sum().backward()
        optimizer.step()
```

Launcher (`run_harness.sh`)
```
torchrun --nproc_per_node 1 --nnodes 2 --rdzv_backend=c10d --rdzv_endpoint=$1:29400 harness.py ${@:2}
```

Output (on a two node allocation):
```
$ ip a # show IP of preferred network interface on the master node
$ srun sh run_harness.sh <master_ip>
# I am omitting some messages related to torchrun
Initialized GPU 0
Initialized GPU 0
Initialized process group on rank 0
Initialized process group on rank 1
1
1
2
2
4
4
8
8
16
16
32
32
64
64
128
128
^C
```

The process stalls after a few iterations.

It is possible to get the loop to finish by setting the environment variable `NCCL_PROTO=Simple`.

Digging deeper, the hang was introduced between ROCm 4.5.2 and 5.0.2, in this commit:
https://github.com/ROCmSoftwarePlatform/rccl/commit/565fbeb5e9b6a9c7668498193648ac12ede6f7db

Specifically, the change in `BROADCAST_CHUNKSTEPS` from 1 to 2 causes the problem.

Versions:
- pytorch: 1.12.0a0+git9429dbb (master branch)
  - compilation command line:
     - `CXX=g++ CC=gcc CXXFLAGS=-lncurses PYTORCH_ROCM_ARCH="gfx90a" USE_MPI=0 USE_ROCM=1 python setup.py bdist_wheel --verbose`
- ROCm: 5.0.2 (the problem still exists in RCCL branch rocm-5.1.0)

Debug output (`NCCL_DEBUG=info`):
```
crusher002:81767:81767 [0] NCCL INFO Bootstrap : Using bond0:100.65.2.2<0>
crusher002:81767:81767 [0] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation
crusher002:81767:81767 [0] NCCL INFO NET/IB : No device found.
crusher002:81767:81767 [0] NCCL INFO NET/Socket : Using [0]bond0:100.65.2.2<0> [1]hsn0:10.129.0.13<0> [2]hsn1:10.129.0.14<0> [3]hsn2:10.129.0.15<0> [4]hsn3:10.129.0.16<0>
crusher002:81767:81767 [0] NCCL INFO Using network Socket
RCCL version 2.10.3+hip5.0
crusher003:24359:24359 [0] NCCL INFO Bootstrap : Using bond0:100.65.2.3<0>
crusher003:24359:24359 [0] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation
crusher003:24359:24359 [0] NCCL INFO NET/IB : No device found.
crusher003:24359:24359 [0] NCCL INFO NET/Socket : Using [0]bond0:100.65.2.3<0> [1]hsn0:10.129.0.17<0> [2]hsn1:10.129.0.18<0> [3]hsn2:10.129.0.19<0> [4]hsn3:10.129.0.20<0>
crusher003:24359:24359 [0] NCCL INFO Using network Socket
crusher002:81767:81779 [0] NCCL INFO Not performing bootstrap root for clique kernels as clique mode not enabled.
crusher002:81767:81780 [0] NCCL INFO rocm_smi_lib: version 5.0.0.0
crusher003:24359:24369 [0] NCCL INFO rocm_smi_lib: version 5.0.0.0
crusher002:81767:81780 [0] NCCL INFO Clique kernels disabled
crusher003:24359:24369 [0] NCCL INFO Clique kernels disabled
crusher003:24359:24369 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1 [2] -1/-1/-1->1->0 [3] 0/-1/-1->1->-1 comm 0x7f9e80000ef0 nRanks 02 busId c1000
crusher003:24359:24369 [0] NCCL INFO Channel 00 : 0[c1000] -> 1[c1000] [receive] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 01 : 0[c1000] -> 1[c1000] [receive] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 02 : 0[c1000] -> 1[c1000] [receive] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 03 : 0[c1000] -> 1[c1000] [receive] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 00/04 :    0   1
crusher002:81767:81780 [0] NCCL INFO Channel 01/04 :    0   1
crusher002:81767:81780 [0] NCCL INFO Channel 02/04 :    0   1
crusher002:81767:81780 [0] NCCL INFO Channel 03/04 :    0   1
crusher002:81767:81780 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1 [2] 1/-1/-1->0->-1 [3] -1/-1/-1->0->1 comm 0x7f6400000ef0 nRanks 02 busId c1000
crusher002:81767:81780 [0] NCCL INFO Channel 00 : 1[c1000] -> 0[c1000] [receive] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 01 : 1[c1000] -> 0[c1000] [receive] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 02 : 1[c1000] -> 0[c1000] [receive] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 03 : 1[c1000] -> 0[c1000] [receive] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 00 : 0[c1000] -> 1[c1000] [send] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 01 : 0[c1000] -> 1[c1000] [send] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 00 : 1[c1000] -> 0[c1000] [send] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 02 : 0[c1000] -> 1[c1000] [send] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 01 : 1[c1000] -> 0[c1000] [send] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Channel 03 : 0[c1000] -> 1[c1000] [send] via NET/Socket/1 comm 0x7f6400000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 02 : 1[c1000] -> 0[c1000] [send] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher003:24359:24369 [0] NCCL INFO Channel 03 : 1[c1000] -> 0[c1000] [send] via NET/Socket/1 comm 0x7f9e80000ef0 nRanks 02
crusher002:81767:81780 [0] NCCL INFO Connected all rings comm 0x7f6400000ef0 nRanks 02 busId c1000
crusher002:81767:81780 [0] NCCL INFO Connected all trees comm 0x7f6400000ef0 nRanks 02 busId c1000
crusher003:24359:24369 [0] NCCL INFO Connected all rings comm 0x7f9e80000ef0 nRanks 02 busId c1000
crusher003:24359:24369 [0] NCCL INFO Connected all trees comm 0x7f9e80000ef0 nRanks 02 busId c1000
crusher003:24359:24369 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 8/8/512
crusher003:24359:24369 [0] NCCL INFO 4 coll channels, 4 p2p channels, 1 p2p channels per peer
crusher002:81767:81780 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 8/8/512
crusher002:81767:81780 [0] NCCL INFO 4 coll channels, 4 p2p channels, 1 p2p channels per peer
crusher003:24359:24369 [0] NCCL INFO comm 0x7f9e80000ef0 rank 1 nranks 2 cudaDev 0 busId c1000 used 27440 bytes - Init COMPLETE
crusher002:81767:81780 [0] NCCL INFO comm 0x7f6400000ef0 rank 0 nranks 2 cudaDev 0 busId c1000 used 27440 bytes - Init COMPLETE
crusher002:81767:81767 [0] NCCL INFO Launch mode Parallel/CGMD
```

## 评论 (3)

### wenkaidu · 2022-04-25

The issue is being worked on through email.

### visionscaper · 2024-03-30

@wenkaidu What was the resolution to this issue? I opened a [similar issue](https://github.com/ROCm/rccl/issues/1129).

### wenkaidu · 2024-04-01

The issue was exactly what Jens reported: changing BROADCAST_CHUNKSTEPS from 1 to 2 causes the problem.
BROADCAST_CHUNKSTEPS has been reverted to 1:
https://github.com/ROCm/rccl/blob/develop/src/include/collectives.h#L22
