# [Issue #1561] Not able to use UCX Plugin for NIXL over RDMA

source: https://github.com/ai-dynamo/nixl/issues/1561
state: closed | updated: 2026-04-22T11:08:48Z
labels: 

## 正文

I have installed ucx ( 1.20.0) and compiled nixl using that, able to see ./build/src/plugins/ucx/libplugin_UCX.so created but while running UCX backend nixlbenc still throws error about missing UCX

```
 UCX_TLS=rc,rc_v UCX_NET_DEVICES=mxl5_0:1 ./benchmark/nixlbench/build/nixlbench --etcd-endpoints http://10.28.38.84:2379   -
-backend UCX   --initiator_seg_type DRAM  --target_seg_type VRAM   --filepath .   --max_block_size 8388608   --max_batch_size 1   --scheme pairwise   --num_files 1   -
-num_threads 1   --op_type READ
WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads
WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads
Connecting to ETCD at http://10.28.38.84:2379
ETCD Runtime: Registered as rank 1 item 2 of 2
E0421 11:56:59.774282  709103 nixl_agent.cpp:259] getPluginParams: backend 'UCX' not found
Init nixl worker, dev all rank 1, type target, hostname S-5126GS-TNRT2
E0421 11:56:59.775353  709103 nixl_agent.cpp:322] createBackend: unsupported backend 'UCX'
NIXL: createBackend failed! (Error code: E0421 11:56:59.776371  709103 nixl_agent.cpp:322] createBackend: unsupported backend 'UCX'
```

## 评论 (1)

### alokprasad · 2026-04-22

Got it resolved , it was issue with UCX library path ( libucp.so.0 ) and plugin path libplugin_UCX.so
