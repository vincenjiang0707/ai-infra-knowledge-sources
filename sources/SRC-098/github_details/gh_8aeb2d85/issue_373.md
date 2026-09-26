# [Issue #373] NCCL_IB_DISABLE=1 not work

source: https://github.com/NVIDIA/nccl-tests/issues/373
state: open | updated: 2026-02-25T17:49:36Z
labels: 

## 正文

```
bigo:1884:1884 [0] NCCL INFO cudaDriverVersion 12020
bigo:1884:1884 [0] NCCL INFO Bootstrap : Using bond0.526:169.136.106.9<0>
bigo:1884:2298 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
bigo:1884:2298 [0] NCCL INFO P2P plugin IBext_v8
bigo:1884:2298 [0] NCCL INFO NET/IB : Using [0]={[0] mlx5_2:1/RoCE, [1] mlx5_3:1/RoCE} [1]={[2] mlx5_0:1/RoCE, [3] mlx5_1:1/RoCE} [RO]; OOB bond0.526:169.136.106.9<0>
bigo:1884:2298 [0] NCCL INFO Using non-device net plugin version 0
bigo:1884:2298 [0] NCCL INFO Using network IBext_v8
bigo:1884:2298 [0] NCCL INFO ncclCommInitRank comm 0x564531f27c80 rank 2 nranks 3 cudaDev 0 nvmlDev 0 busId 31000 commId 0x9ca74fa6e40df7f4 - Init START
bigo:1884:2298 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to LOC
bigo:1884:2298 [0] NCCL INFO Setting affinity for GPU 0 to ffffffff,00000000,ffffffff
bigo:1884:2298 [0] NCCL INFO comm 0x564531f27c80 rank 2 nRanks 3 nNodes 3 localRanks 1 localRank 0 MNNVL 0
bigo:1884:2298 [0] NCCL INFO Trees [0] 1/-1/-1->2->0 [1] -1/-1/-1->2->0
bigo:1884:2298 [0] NCCL INFO P2P Chunksize set to 131072
bigo:1884:2298 [0] NCCL INFO Channel 00/0 : 1[0] -> 2[0] [receive] via NET/IBext_v8/1
bigo:1884:2298 [0] NCCL INFO Channel 01/0 : 1[0] -> 2[0] [receive] via NET/IBext_v8/1
bigo:1884:2298 [0] NCCL INFO Channel 00/0 : 2[0] -> 0[0] [send] via NET/IBext_v8/1
bigo:1884:2298 [0] NCCL INFO Channel 01/0 : 2[0] -> 0[0] [send] via NET/IBext_v8/1

bigo:1884:2346 [0] socket.c:446 NCCL WARN socketFinalizeAccept: wrong type 3 != 4
```

## 评论 (2)

### haolujun · 2026-02-25

start script is like this:
```
MASTER_PORT=12455
MASTER_ADDR="169.136.138.55"
WORLD_SIZE=1
ENTRY=recis_run.py
export NCCL_P2P_DISABLE="1"
export NCCL_IB_DISABLE="1"
export NCCL_DEBUG=INFO
torchrun --nnodes=3 --node-rank=2 --nproc_per_node=$WORLD_SIZE --master_addr=${MASTER_ADDR} --master_port=$MASTER_PORT $ENTRY --config xdl_run.json
```

### AddyLaddy · 2026-02-25

Are those NCCL environment variables being exported to all ranks by the torch runtime?
You can check the INFO logs from each rank to confirm NCCL has seen each environment variable.

