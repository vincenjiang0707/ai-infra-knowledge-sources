# [Issue #58] dist.broadcast_object_list not work, hang with no response

source: https://github.com/Ascend/pytorch/issues/58
state: open | updated: 2025-02-05T08:30:28Z
labels: 

## 正文

code: 

import torch
import torch_npu
import torch.distributed as dist
import torch.multiprocessing as mp

def worker(rank, world_size):
    device = torch.device(f"npu:{rank}")
    torch.set_default_device(device)
    dist.init_process_group(backend="hccl", init_method="env://", rank=rank, world_size=world_size)
    print(f"Rank {rank} initialized")
    # 广播操作
    object_list = [None]  # 所有进程的列表长度必须一致
    if rank == 0:
        object_list[0] = {"message": "Hello from rank 0", "data": [1, 2, 3]}
    # this api not work
    dist.broadcast_object_list(object_list, src=0)   ==> program will hang here!!!!
    print(f"Rank {rank} received: {object_list[0]}")
    # dist.destroy_process_group()

if __name__ == "__main__":
    import os
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    world_size = 2
    mp.spawn(worker, args=(world_size,), nprocs=world_size, join=True)


version:
torch                     2.1.0
torch-npu                 2.1.0.post6



## 评论 (1)

### yunyiyun · 2025-02-05

You should set_device when use distributed.
torch.set_default_device(device) replace with torch.npu.set_device(device)
