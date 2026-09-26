# [Issue #1695] vram to vram performance too low

source: https://github.com/ai-dynamo/nixl/issues/1695
state: open | updated: 2026-07-02T11:30:50Z
labels: Network

## 正文

hi why VRAM TO VRAM over RDMA/UCX  Backend is too slow 
Setup 
CX7 400G 
H200 GPU
PCIE GEN 5
Attached log 

```
NIXLBench Configuration
****************************************************************************************************************************************************************
Runtime (--runtime_type=[etcd])                             : ETCD
ETCD Endpoint                                               : http://10.28.38.84:2379/
Worker type (--worker_type=[nixl,nvshmem])                  : nixl
Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCX
Enable pt (--enable_pt=[0,1])                               : 0
Progress threads (--progress_threads=N)                     : 0
Device list (--device_list=dev1,dev2,...)                   : all
Enable VMM (--enable_vmm=[0,1])                             : 0
Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0
Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : VRAM
Target seg type (--target_seg_type=[DRAM,VRAM])             : VRAM
Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise
Mode (--mode=[SG,MG])                                       : SG
Op type (--op_type=[READ,WRITE])                            : WRITE
Check consistency (--check_consistency=[0,1])               : 0
Total buffer size (--total_buffer_size=N)                   : 8589934592
Num initiator dev (--num_initiator_dev=N)                   : 1
Num target dev (--num_target_dev=N)                         : 1
Start block size (--start_block_size=N)                     : 4096
Max block size (--max_block_size=N)                         : 8388608
Start batch size (--start_batch_size=N)                     : 1
Max batch size (--max_batch_size=N)                         : 1
Num iter (--num_iter=N)                                     : 1008
Warmup iter (--warmup_iter=N)                               : 112
Large block iter factor (--large_blk_iter_ftr=N)            : 16
Num threads (--num_threads=N)                               : 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
4096                1              0.206109       19.9           45.0           45.0           9.1            10.0           10.8           13.0
8192                1              0.304999       26.9           203.0          203.0          16.5           18.0           10.1           11.0
16384               1              0.432932       37.8           14.0           14.0           28.2           30.0           9.6            11.0
32768               1              0.566934       57.8           58.0           58.0           48.3           50.0           9.4            10.0
65536               1              0.771732       84.9           17.0           17.0           75.8           78.0           9.1            10.0
131072              1              0.852881       153.7          95.0           95.0           144.6          150.0          9.0            10.0
262144              1              0.797524       328.7          141.0          141.0          320.4          325.0          8.2            9.0
524288              1              0.938796       558.5          43.0           43.0           551.0          630.0          7.4            8.0
1048576             1              0.970152       1080.8         19.0           19.0           1074.8         1086.0         6.0            7.0
2097152             1              1.005530       2085.6         16.0           16.0           2083.8         2096.0         1.5            7.0
4194304             1              0.901915       4650.4         201.0          201.0          4639.4         5516.0         7.5            194.0
8388608             1              0.975764       8597.0         16.0           16.0           8490.9         8734.0         105.7          109.0

NIXLBench Configuration
****************************************************************************************************************************************************************
Runtime (--runtime_type=[etcd])                             : ETCD
ETCD Endpoint                                               : http://10.28.38.84:2379/
Worker type (--worker_type=[nixl,nvshmem])                  : nixl
Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCX
Enable pt (--enable_pt=[0,1])                               : 0
Progress threads (--progress_threads=N)                     : 0
Device list (--device_list=dev1,dev2,...)                   : all
Enable VMM (--enable_vmm=[0,1])                             : 0
Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0
Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : VRAM
Target seg type (--target_seg_type=[DRAM,VRAM])             : VRAM
Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise
Mode (--mode=[SG,MG])                                       : SG
Op type (--op_type=[READ,WRITE])                            : READ
Check consistency (--check_consistency=[0,1])               : 0
Total buffer size (--total_buffer_size=N)                   : 8589934592
Num initiator dev (--num_initiator_dev=N)                   : 1
Num target dev (--num_target_dev=N)                         : 1
Start block size (--start_block_size=N)                     : 4096
Max block size (--max_block_size=N)                         : 8388608
Start batch size (--start_batch_size=N)                     : 1
Max batch size (--max_batch_size=N)                         : 1
Num iter (--num_iter=N)                                     : 1008
Warmup iter (--warmup_iter=N)                               : 112
Large block iter factor (--large_blk_iter_ftr=N)            : 16
Num threads (--num_threads=N)                               : 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
4096                1              0.195834       20.9           195.0          195.0          1.5            2.0            19.2           21.0
8192                1              0.293560       27.9           20.0           20.0           1.4            2.0            26.5           28.0
16384               1              0.451700       36.3           103.0          103.0          1.5            2.0            34.7           37.0
32768               1              0.642235       51.0           16.0           16.0           1.2            2.0            49.8           52.0
65536               1              0.795754       82.4           44.0           44.0           1.3            2.0            81.0           84.0
131072              1              0.903055       145.1          105.0          105.0          1.3            2.0            143.7          148.0
262144              1              0.969027       270.5          76.0           76.0           1.4            2.0            269.0          278.0
524288              1              0.999671       524.5          90.0           90.0           1.5            2.0            522.8          532.0
1048576             1              0.262022       4001.9         128.0          128.0          1.4            2.0            4000.2         1141.0
2097152             1              1.025566       2044.9         186.0          186.0          36.5           2175.0         2005.0         2091.0
4194304             1              1.019449       4114.3         155.0          155.0          67.0           4099.0         4044.4         4158.0
8388608             1              1.018200       8238.7         113.0          113.0          2.3            19.0           8234.2         8415.0
```

## 评论 (4)

### alokprasad · 2026-05-29

[intiator.txt](https://github.com/user-attachments/files/28392949/intiator.txt)

### ztxdcyy · 2026-06-03

Start batch size (--start_batch_size=N)                     : 1
Max batch size (--max_batch_size=N)                         : 1

Change these two arguments to 128 can help somehow.

### alokprasad · 2026-06-03

@ztxdcyy tried 128 , still seeing same numbers

i am using
```
UCX_IB_GPU_DIRECT_RDMA=1 UCX_TLS=rc,cuda_copy UCX_IB_GID_INDEX=3 UCX_NET_DEVICES=mlx5_0:1 ./benchmark/nixlbench/build/nixlbench --etcd-endpoints http://10.28.38.84:2379 --backend UCX  --initiator_seg_type VRAM  --target_seg_type VRAM  --filepath . --max_block_size 8388608   --start_batch_size 128 --max_batch_size 128   --scheme pairwise --num_files 1  --op_type READ
```

### brminich · 2026-07-02

Can you pls share logs collected with `UCX_PROTO_INFO=y` and `UCX_LOG_LEVEL=debug`?
