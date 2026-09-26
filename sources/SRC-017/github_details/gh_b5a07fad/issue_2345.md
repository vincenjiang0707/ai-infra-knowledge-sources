# [Issue #2345] [Issue]: Ring and tree both create cross-rail inter-node links, violating rail isolation and despite `NCCL_CROSS_NIC=0`

source: https://github.com/NVIDIA/nccl/issues/2345
state: open | updated: 2026-09-15T02:18:32Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs

logs from head node rank 0 (2 node setup, `kg35-nvl03` is head, `k35-nvl04` is worker)

[ncclDebug.kg35-nvl03.3359602.log](https://github.com/user-attachments/files/31123128/ncclDebug.kg35-nvl03.3359602.log)
[ncclSystem.kg35-nvl03.txt](https://github.com/user-attachments/files/31123130/ncclSystem.kg35-nvl03.txt)


### Steps to Reproduce the Issue

setting these env vars:
```bash
# ---- fabric selection ----
# control plane: one interface, routable from every node
export NCCL_SOCKET_IFNAME=ens80f0np0
export GLOO_SOCKET_IFNAME=ens80f0np0

# data plane: unchanged, both rails, per-rank affinity
export NCCL_IB_HCA=rocep80s0,rocep203s0
export NCCL_IB_DISABLE=0

# ---- rail-isolated fabric ----
export NCCL_CROSS_NIC=0
export NCCL_ALGO=Ring

# ---- GPUDirect RDMA ----
export NCCL_NET_GDR_LEVEL=PIX
export NCCL_IB_GID_INDEX=3
export NCCL_IB_TIMEOUT=22
export NCCL_IB_RETRY_CNT=10
export NCCL_IB_QPS_PER_CONNECTION=4

# ---- intra-node ----
export NCCL_NVLS_ENABLE=0
export NCCL_BUFFSIZE=8388608

# ---- logging ----
# export NCCL_DEBUG=WARN
export NCCL_DEBUG=INFO
# export NCCL_DEBUG_SUBSYS=INIT,GRAPH,NET
```

with a thin script that does an all reduce:
```python
# probe.py
import os, torch, torch.distributed as dist
dist.init_process_group("nccl")
torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))
x = torch.ones(64*1024*1024, device="cuda")
for _ in range(3):
    dist.all_reduce(x)
torch.cuda.synchronize()
dist.destroy_process_group()
```

and using the following torchruns:
```bash
# node 0
torchrun --nnodes=2 --nproc_per_node=4 --node_rank=0 --master_addr=10.32.12.33 --master_port=29612 probe.py

# node 1
torchrun --nnodes=2 --nproc_per_node=4 --node_rank=1 --master_addr=10.32.12.33 --master_port=29612 probe.py
```


### NCCL Version

2.30.7+cuda13.3

### Your platform details

- NCCL 2.30.7+cuda13.3
- 2 nodes x 4 H200, **2 NVLink pairs per node** (GPU0-GPU1, GPU2-GPU3; NV18
  within a pair, SYS across pairs)
- 2-socket board, 2 GPUs per socket, 1 rail NIC per socket
- 2 rail NICs per node, ConnectX-7 400Gb, RoCEv2, one per NVLink pair
- Separate OOB/management NIC used for bootstrap

annotated `nvidia-smi topo -m` output, identical on both nodes
```
        GPU0  GPU1  GPU2  GPU3  NIC0  NIC1
GPU0     X    NV18  SYS   SYS   PIX   SYS
GPU1    NV18   X    SYS   SYS   PIX   SYS
GPU2    SYS   SYS    X    NV18  SYS   PIX
GPU3    SYS   SYS   NV18   X    SYS   PIX

NIC0: rocep80s0   -> ens2005np0  10.32.16.0/24   (rail 0)
NIC1: rocep203s0  -> ens5008np0  10.32.15.0/24   (rail 1)
OOB : rocep167s0f0 -> ens80f0np0 10.32.12.0/24
```

**There is currently no route between `10.32.16.0/24` and `10.32.15.0/24`.** Each rail is an isolated L2/L3 domain.

### Error Message & Behavior

NCCL creates the ring but hangs because some links are not possible, e.g. from the log:
```
NCCL INFO Channel 03/0 : 7[3] -> 0[0] [receive] via NET/IB/0/GDRDMA
```

where GPU3 on node 1 rail 1 via NIC 1 cannot see GPU0 on node 0 rail 0 via NIC 0. this seems like `NCCL_CROSS_NIC=0` is not having the desired effect, from the 2.30.7 docs:
> 0: Always use the same NIC for the same ring/tree, to avoid crossing network rails

Other symptoms:
* Similar cross-rail connections are attempted using tree algorithm
* NCCL_CROSS_NIC=2 similarly fails
* Ring is recoverable when manually reversing device order (via `CUDA_VISIBLE_DEVICES=3,2,1,0`) on peer node 1. I believe this solution is generalizable to an even number of nodes, however an odd-number of nodes in a ring cannot be closed with this solution. Also feels like this should potentially be handled by NCCL?

Have we misconfigured the fabric? Does there need to exist some link between the two rails?

## 评论 (6)

### xiaofanl-nvidia · 2026-08-23

++ @thomasgillis to take a look

### thomasgillis · 2026-09-14

Thanks for the logs, could you share with us the log with the following env variables?
`NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,NET`

### StevenSong · 2026-09-14

> Thanks for the logs, could you share with us the log with the following env variables? `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,NET`

@thomasgillis thanks for the reply, here's that log:

[ncclDebug.kg35-nvl03.1541487.log](https://github.com/user-attachments/files/32205041/ncclDebug.kg35-nvl03.1541487.log)

### thomasgillis · 2026-09-15

A few things do not click for me and it seems to indicate that the communicator is ill-formed.

- the log shows that you only have 2 GPUs per host in the communicator `kg35-nvl03:1541487:1541487 [0] NCCL INFO comm 0x55dae9e8f270 rank 0 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0`.
- where is the rest of the communicator running?
GPU/3 will logically select NET/0-1, while GPU/0 will logically select NET/0-0. That selection is expected based on the topology of the node. If you do not have connectivity between those 2 NETs, it will hang (as you observed).

Could you share the log for all the ranks in the communicator?
Also, if you can't control the communicator split, maybe you can force GPU/3 to choose NET/0? The only way to do so based on the topology is to set the value of NCCL_IB_HCA accordingly.

Some context on crossNIC: setting crossNIC = 0 for ring will only impact the intra-host NIC selection. It will not force all the GPUs to align on which NET to choose. That logic is based on the assumption of a communicator split that follows the node topology.

### StevenSong · 2026-09-15

> the log shows that you only have 2 GPUs per host in the communicator

Maybe relatedly, I also see `nNodes 4`, but there's only 2 host machines. Could that be something with the 2-way NVLink pairs per host making it look like 4 "nodes" instead of the actual 2 hosts?

> Could you share the log for all the ranks in the communicator?

yes, here's logs from all 8 ranks:
- [ncclDebug.kg35-nvl03.1541487.log](https://github.com/user-attachments/files/32218612/ncclDebug.kg35-nvl03.1541487.log)
- [ncclDebug.kg35-nvl03.1541488.log](https://github.com/user-attachments/files/32218616/ncclDebug.kg35-nvl03.1541488.log)
- [ncclDebug.kg35-nvl03.1541489.log](https://github.com/user-attachments/files/32218620/ncclDebug.kg35-nvl03.1541489.log)
- [ncclDebug.kg35-nvl03.1541490.log](https://github.com/user-attachments/files/32218621/ncclDebug.kg35-nvl03.1541490.log)
- [ncclDebug.kg35-nvl04.847972.log](https://github.com/user-attachments/files/32218626/ncclDebug.kg35-nvl04.847972.log)
- [ncclDebug.kg35-nvl04.847973.log](https://github.com/user-attachments/files/32218627/ncclDebug.kg35-nvl04.847973.log)
- [ncclDebug.kg35-nvl04.847974.log](https://github.com/user-attachments/files/32218629/ncclDebug.kg35-nvl04.847974.log)
- [ncclDebug.kg35-nvl04.847975.log](https://github.com/user-attachments/files/32218631/ncclDebug.kg35-nvl04.847975.log)

> setting crossNIC = 0 for ring will only impact the intra-host NIC selection

ah, thanks for the clarification on this point


### StevenSong · 2026-09-15

I was looking at #1405 and set the env var `NCCL_NET_DISABLE_INTRA=1` (and keeping `NCCL_CROSS_NIC=0`) - this lets it detect 2 nodes, 4 local ranks:
```
kg35-nvl03:1572954:1572954 [0] NCCL INFO comm 0x563410046730 rank 0 nRanks 8 nNodes 2 localRanks 4 localRank 0 MNNVL 0
```

and the job runs with no hangs. here's those per-rank logs when setting `NCCL_NET_DISABLE_INTRA=1` (I had the following debug subsystems enabled: `NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,NET,BOOTSTRAP,P2P,SHM`):
- [ncclDebug.kg35-nvl03.1572954.log](https://github.com/user-attachments/files/32219620/ncclDebug.kg35-nvl03.1572954.log)
- [ncclDebug.kg35-nvl03.1572955.log](https://github.com/user-attachments/files/32219622/ncclDebug.kg35-nvl03.1572955.log)
- [ncclDebug.kg35-nvl03.1572956.log](https://github.com/user-attachments/files/32219623/ncclDebug.kg35-nvl03.1572956.log)
- [ncclDebug.kg35-nvl03.1572957.log](https://github.com/user-attachments/files/32219625/ncclDebug.kg35-nvl03.1572957.log)
- [ncclDebug.kg35-nvl04.876730.log](https://github.com/user-attachments/files/32219627/ncclDebug.kg35-nvl04.876730.log)
- [ncclDebug.kg35-nvl04.876731.log](https://github.com/user-attachments/files/32219629/ncclDebug.kg35-nvl04.876731.log)
- [ncclDebug.kg35-nvl04.876732.log](https://github.com/user-attachments/files/32219632/ncclDebug.kg35-nvl04.876732.log)
- [ncclDebug.kg35-nvl04.876733.log](https://github.com/user-attachments/files/32219633/ncclDebug.kg35-nvl04.876733.log)

I'm not sure if this is correct though, I see in e.g. rank 0's logs connections using both NICs where the far NIC needs to go through host memory on both ends:
```
kg35-nvl03:1572954:1572954 [0] NCCL INFO Channel 00/0 : 7[3] -> 0[0] [receive] via NET/IB/0/GDRDMA
kg35-nvl03:1572954:1572954 [0] NCCL INFO Channel 01/0 : 7[3] -> 0[0] [receive] via NET/IB/1
kg35-nvl03:1572954:1572954 [0] NCCL INFO Channel 02/0 : 7[3] -> 0[0] [receive] via NET/IB/0/GDRDMA
kg35-nvl03:1572954:1572954 [0] NCCL INFO Channel 03/0 : 7[3] -> 0[0] [receive] via NET/IB/1
```

I imagine under load this would be slower given lots of traffic over the cross socket bridge
