# [Issue #1544] Query: NIXL over RDMA Network using Mellanox

source: https://github.com/ai-dynamo/nixl/issues/1544
state: closed | updated: 2026-04-20T16:10:21Z
labels: 

## 正文

what is the best way to use NIXL over Mellanox ( RDMA) , UCX or Libfabric?

## 评论 (2)

### aranadive · 2026-04-20

Please use UCX

### alokprasad · 2026-04-20

@aranadive is there documentation, running nixl over rdma network is very sparse and not clear.
I understand we need etcd to exchange info but how nixlbench will detect which is initiator and which one is target.
i only see reference of below command 

./build/nixlbench
--runtime_type=ETCD
--etcd-endpoints http://x.x.x.x:2379/
--backend UCX
--target_seg_type VRAM
--initiator_seg_type VRAM
--start_batch_size 128
--max_batch_size 1024
--start_block_size 1024
--max_block_size 1024

how the nixlbench parameters changes on intiator side and target side.
