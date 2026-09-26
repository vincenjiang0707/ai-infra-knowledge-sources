# [Issue #1566] Query: CMD Usage of NIXLBench over UCX Backend( RDMA) - How to decide op_type and initator/target_seq_type

source: https://github.com/ai-dynamo/nixl/issues/1566
state: closed | updated: 2026-05-27T18:23:45Z
labels: 

## 正文

On a Two node (A and B) how does NIXLBench over RDMA decides who will be initator and who will be target, does it depends on 
Order of executing of nixlbench ? The first to run will be initiator? 

Also how to decide on the --initiator_seg_type  --target_seg_type on A and B.
Suppose i want to do 

```
GPU- VRAM ---> NIC--------------WIRE----------------> NIC ---> DRAM
( Host A)			                               (Host B)
```
Now suppose Host B needs to do RDMA Read from Host A VRAM . 
Is below config right?

Host B
 --initiator_seg_type DRAM  --target_seg_type VRAM
--op_type READ

Host A
 --initiator_seg_type VRAM  --target_seg_type DRAM
--op_type   WRITE



## 评论 (4)

### aranadive · 2026-04-23

The operation is always from the initiator (the target is passive) point of view and is started first. So if Host B wants do a READ, then run nixlbench first on Host B with  --initiator_seg_type DRAM --target_seg_type VRAM --op_type READ. 
Then, on Host A run the same nixlbench command.

### alokprasad · 2026-04-28

> The operation is always from the initiator (the target is passive) point of view and is started first. So if Host B wants do a READ, then run nixlbench first on Host B with --initiator_seg_type DRAM --target_seg_type VRAM --op_type READ. Then, on Host A run the same nixlbench command.

If i follow the logic and use below cmds
Host B
```
UCX_IB_GID_INDEX=3 UCX_NET_DEVICES=mlx5_0:1 ./benchmark/nixlbench/build/nixlbench --etcd-endpoints http://10.28.38.84:2379 --backend UCX  --initiator_seg_type DRAM  --target_seg_type VRAM  --filepath . --max_block_size 8388608   --max_batch_size 1   --scheme pairwise   --num_files 1   --num_threads 1   --op_type WRITE
```
Host A
```
UCX_IB_GID_INDEX=3 UCX_NET_DEVICES=rocep161s0:1  ./benchmark/nixlbench/build/nixlbench --etcd-endpoints http://10.28.38.84:2379 --backend UCX  --initiator_seg_type DRAM  --target_seg_type VRAM  --filepath . --max_block_size 8388608   --max_batch_size 1   --scheme pairwise   --num_files 1   --num_threads 1   --op_type WRITE
```

Getting below error on Host B 

E0428 15:58:07.582960 1088856 serdes.cpp:66] Deserialization of tag c failed for incomplete data
E0428 15:58:07.583202 1088856 nixl_agent.cpp:1512] loadRemoteMD: failed to deserialize remote metadata
NIXL: loadRemoteMD failed: NIXL_ERR_MISMATCH


### linear-code[bot] · 2026-05-05

from aranadive:
> In one instance of nixlbench you have provided the IB device and in another the ethernet device. Can you provide the mlx5 device in the Host A command as well? What is the output of ibv_devices on both hosts?

### alokprasad · 2026-05-27

@aranadive 
when  VRAM is initiator and DRAM as target  doesn't that automatically mean VRAM -> DRAM write ?
when DRAM is initiator and VRAM is target  doesn't that automatically mean DRAM -> VRAM write ?
why we need to define op_type?
