# [Issue #1954] ERROR: [DOCA][ERR][linux_device_adapter.cpp:1268] failed to extract sockaddr_in

source: https://github.com/ai-dynamo/nixl/issues/1954
state: open | updated: 2026-08-11T11:37:16Z
labels: 

## 正文

# Running Command
```
nixlbench --backend GPUNETIO --initiator_seg_type VRAM --target_seg_type VRAM --op_type write --etcd_endpoints http://localhost:2379 --device_list=mlx5_bond_0
```


# Error Message

```
ETCD Runtime: Registered as rank 0 item 1 of 2
GPUNETIO backend, network device mlx5_bond_0 GPU device 1
[16:06:20:096585][701476864][DOCA][INF][doca_log.cpp:628] DOCA version 3.1.0105
[16:06:21:232863][701476864][DOCA][ERR][linux_device_adapter.cpp:1268] failed to extract sockaddr_in
Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)
```

Related to #788, nixl GPUNETIO backend failed to run on machines with bonded network ports.
In our test environment, `mlx5_bond_0` is a bonded device consisting of the two ports on each ConnectX-7 network card.





cc @foraxe @e-ago




## 评论 (4)

### foraxe · 2026-07-26

Single node testing? 
Have you ran the gpunetio sample (without nixl)?  Is it on the 3.1.0105 DOCA version like this nixlbench env? 
@tong1heng 

### foraxe · 2026-07-26

Can you provide more infos? @tong1heng 

### foraxe · 2026-08-11

Fixed in https://github.com/ai-dynamo/nixl/pull/2052

### foraxe · 2026-08-11

> Fixed in [#2052](https://github.com/ai-dynamo/nixl/pull/2052)

Hi @e-ago @brminich, would you mind taking a look when you have a chance?
