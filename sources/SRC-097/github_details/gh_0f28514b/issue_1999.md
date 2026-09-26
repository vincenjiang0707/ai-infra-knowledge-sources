# [Issue #1999] UCCL nixlbench test hangs

source: https://github.com/ai-dynamo/nixl/issues/1999
state: open | updated: 2026-09-20T06:00:54Z
labels: Network, CI

## 正文

Test hangs often in CI (nixl-ci-gpu job):

```
[2026-07-28T10:17:17.743Z] + command_line='./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group kFRfmLw74QuQ3AxH4r6hiYkUZfSZ6U43 --backend UCX --op_type WRITE --initiator_seg_type DRAM --target_seg_type DRAM --check_consistency'

[2026-07-28T10:17:17.743Z] + parallel --line-buffer --halt now,fail=1 ::: './bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group kFRfmLw74QuQ3AxH4r6hiYkUZfSZ6U43 --backend UCX --op_type WRITE --initiator_seg_type DRAM --target_seg_type DRAM --check_consistency' 'sleep 4 ; ./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group kFRfmLw74QuQ3AxH4r6hiYkUZfSZ6U43 --backend UCX --op_type WRITE --initiator_seg_type DRAM --target_seg_type DRAM --check_consistency'

[2026-07-28T10:17:18.674Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:17:18.674Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:17:18.674Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:17:18.674Z] ETCD Runtime: Registered as rank 0 item 1 of 2

[2026-07-28T10:17:18.933Z] Init nixl worker, dev all rank 0, type initiator, hostname mizu01

[2026-07-28T10:17:22.227Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:17:22.793Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:17:22.793Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:17:22.793Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:17:22.793Z] ETCD Runtime: Registered as rank 1 item 2 of 2

[2026-07-28T10:17:23.050Z] Init nixl worker, dev all rank 1, type target, hostname mizu01

[2026-07-28T10:17:26.327Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:17:26.327Z] All processes are ready to proceed

[2026-07-28T10:17:28.228Z] All processes are ready to proceed

[2026-07-28T10:17:33.487Z] ****************************************************************************************************************************************************************

[2026-07-28T10:17:33.487Z] NIXLBench Configuration

[2026-07-28T10:17:33.487Z] ****************************************************************************************************************************************************************

[2026-07-28T10:17:33.487Z] Runtime (--runtime_type=[ETCD,ASIO])                        : ETCD

[2026-07-28T10:17:33.487Z] ETCD Endpoint                                               : http://127.0.0.1:30901/

[2026-07-28T10:17:33.487Z] Worker type (--worker_type=[nixl,nvshmem])                  : nixl

[2026-07-28T10:17:33.487Z] Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCX

[2026-07-28T10:17:33.487Z] Enable pt (--enable_pt=[0,1])                               : 0

[2026-07-28T10:17:33.487Z] Progress threads (--progress_threads=N)                     : 0

[2026-07-28T10:17:33.487Z] Device list (--device_list=dev1,dev2,...)                   : all

[2026-07-28T10:17:33.487Z] Enable VMM (--enable_vmm=[0,1])                             : 0

[2026-07-28T10:17:33.487Z] Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0

[2026-07-28T10:17:33.487Z] Re-register memory each iteration (--reregister_mem=[0,1])  : 0

[2026-07-28T10:17:33.487Z] Prepared xfer (prep+make) (--prepared_xfer=[0,1])           : 0

[2026-07-28T10:17:33.487Z] Pipeline depth (--pipeline_depth=N)                         : 1

[2026-07-28T10:17:33.487Z] Use hugepages (--use_hugepages=[0,1])                       : 0

[2026-07-28T10:17:33.487Z] Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : DRAM

[2026-07-28T10:17:33.487Z] Target seg type (--target_seg_type=[DRAM,VRAM])             : DRAM

[2026-07-28T10:17:33.487Z] Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise

[2026-07-28T10:17:33.487Z] Mode (--mode=[SG,MG])                                       : SG

[2026-07-28T10:17:33.487Z] Op type (--op_type=[READ,WRITE])                            : WRITE

[2026-07-28T10:17:33.487Z] Check consistency (--check_consistency=[0,1])               : 1

[2026-07-28T10:17:33.487Z] Total buffer size (--total_buffer_size=N)                   : 80000000

[2026-07-28T10:17:33.487Z] Num initiator dev (--num_initiator_dev=N)                   : 1

[2026-07-28T10:17:33.487Z] Num target dev (--num_target_dev=N)                         : 1

[2026-07-28T10:17:33.487Z] Start block size (--start_block_size=N)                     : 16384

[2026-07-28T10:17:33.487Z] Max block size (--max_block_size=N)                         : 16384

[2026-07-28T10:17:33.487Z] Start batch size (--start_batch_size=N)                     : 4

[2026-07-28T10:17:33.487Z] Max batch size (--max_batch_size=N)                         : 4

[2026-07-28T10:17:33.487Z] Num iter (--num_iter=N)                                     : 1008

[2026-07-28T10:17:33.487Z] Warmup iter (--warmup_iter=N)                               : 112

[2026-07-28T10:17:33.487Z] Large block iter factor (--large_blk_iter_ftr=N)            : 16

[2026-07-28T10:17:33.487Z] Num threads (--num_threads=N)                               : 1

[2026-07-28T10:17:33.487Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:17:33.487Z] 

[2026-07-28T10:17:33.487Z] Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)    

[2026-07-28T10:17:33.487Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:17:41.612Z] 16384               4              4.524677       3.6            62.0           62.0           7.3            8.0            7.1            11.0           

[2026-07-28T10:17:41.612Z] + true

[2026-07-28T10:17:41.612Z] + for op_type in READ WRITE

[2026-07-28T10:17:41.612Z] + for initiator in $seg_types

[2026-07-28T10:17:41.612Z] + for target in $seg_types

[2026-07-28T10:17:41.612Z] + run_nixlbench_two_workers_etcd --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type VRAM --check_consistency

[2026-07-28T10:17:41.612Z] + args='--backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:17:41.612Z] ++ cat /dev/urandom

[2026-07-28T10:17:41.612Z] ++ tr -dc a-zA-Z0-9

[2026-07-28T10:17:41.612Z] ++ fold -w 32

[2026-07-28T10:17:41.612Z] ++ head -n 1

[2026-07-28T10:17:41.612Z] + benchmark_group=8n9dvrozF6IwiS2NSi4VbsQXsDFu6Dsk

[2026-07-28T10:17:41.613Z] + command_line='./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 8n9dvrozF6IwiS2NSi4VbsQXsDFu6Dsk --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:17:41.613Z] + parallel --line-buffer --halt now,fail=1 ::: './bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 8n9dvrozF6IwiS2NSi4VbsQXsDFu6Dsk --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type VRAM --check_consistency' 'sleep 4 ; ./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 8n9dvrozF6IwiS2NSi4VbsQXsDFu6Dsk --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:17:42.543Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:17:42.543Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:17:42.543Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:17:42.543Z] ETCD Runtime: Registered as rank 0 item 1 of 2

[2026-07-28T10:17:42.543Z] UCCL backend

[2026-07-28T10:17:42.543Z] Creating Engine

[2026-07-28T10:17:43.479Z] System assigned port: 40437

[2026-07-28T10:17:43.479Z] Endpoint initialized successfully

[2026-07-28T10:17:43.479Z] Waiting to accept incoming connection...

[2026-07-28T10:17:43.479Z] Waiting to accept incoming connection...

[2026-07-28T10:17:43.479Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:17:46.759Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:17:46.759Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:17:46.759Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:17:46.759Z] ETCD Runtime: Registered as rank 1 item 2 of 2

[2026-07-28T10:17:46.759Z] UCCL backend

[2026-07-28T10:17:46.759Z] Creating Engine

[2026-07-28T10:17:47.689Z] System assigned port: 41049

[2026-07-28T10:17:47.689Z] Endpoint initialized successfully

[2026-07-28T10:17:47.689Z] Waiting to accept incoming connection...

[2026-07-28T10:17:47.689Z] Waiting to accept incoming connection...

[2026-07-28T10:17:47.689Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:17:47.689Z] All processes are ready to proceed

[2026-07-28T10:17:47.689Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:17:47.689Z]   [0] mlx5_0

[2026-07-28T10:17:47.689Z]   [1] mlx5_1

[2026-07-28T10:17:47.689Z]   [2] mlx5_2

[2026-07-28T10:17:47.689Z]   [3] mlx5_3

[2026-07-28T10:17:47.689Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:47.689Z] [WARN mizu01 3522788 3522788 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:47.689Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:17:47.689Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:17:47.689Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:17:47.689Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:17:47.689Z] Lazy creation of engine for GPU 0

[2026-07-28T10:17:49.591Z] All processes are ready to proceed

[2026-07-28T10:17:49.591Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:17:49.591Z]   [0] mlx5_0

[2026-07-28T10:17:49.591Z]   [1] mlx5_1

[2026-07-28T10:17:49.591Z]   [2] mlx5_2

[2026-07-28T10:17:49.591Z]   [3] mlx5_3

[2026-07-28T10:17:49.591Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:49.591Z] [WARN mizu01 3522787 3522787 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:49.591Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:17:49.591Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:17:49.591Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:17:49.591Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:17:49.591Z] Lazy creation of engine for GPU 0

[2026-07-28T10:17:54.845Z] [ERROR mizu01 3522787 3522929 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:54.845Z] [ERROR mizu01 3522787 3522930 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:54.845Z] [ERROR mizu01 3522787 3522931 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:54.845Z] Attempting to connect to 1.1.101.1:0 via port 41049

[2026-07-28T10:17:56.217Z] [ERROR mizu01 3522788 3522919 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:56.217Z] [ERROR mizu01 3522788 3522920 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:56.217Z] [ERROR mizu01 3522788 3522921 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:17:56.217Z] Accepted connection fd=126 from 1.1.101.1:61330

[2026-07-28T10:17:56.217Z] [WARN mizu01 3522788 3522896 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:56.217Z] [WARN mizu01 3522788 3522896 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:56.217Z] [WARN mizu01 3522788 3522896 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:56.217Z] [WARN mizu01 3522788 3522896 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:56.217Z] Connected to 1.1.101.1:40437 (fd=127)

[2026-07-28T10:17:56.217Z] Waiting to accept incoming connection...

[2026-07-28T10:17:56.782Z] Connected to 1.1.101.1:41049 (fd=126)

[2026-07-28T10:17:56.782Z] Accepted connection fd=127 from 1.1.101.1:37338

[2026-07-28T10:17:56.782Z] [WARN mizu01 3522787 3522851 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:17:56.782Z] [WARN mizu01 3522787 3522851 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:17:56.782Z] [WARN mizu01 3522787 3522851 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:17:56.782Z] [WARN mizu01 3522787 3522851 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:17:56.782Z] ****************************************************************************************************************************************************************

[2026-07-28T10:17:56.782Z] NIXLBench Configuration

[2026-07-28T10:17:56.782Z] ****************************************************************************************************************************************************************

[2026-07-28T10:17:56.782Z] Runtime (--runtime_type=[ETCD,ASIO])                        : ETCD

[2026-07-28T10:17:56.782Z] ETCD Endpoint                                               : http://127.0.0.1:30901/

[2026-07-28T10:17:56.782Z] Worker type (--worker_type=[nixl,nvshmem])                  : nixl

[2026-07-28T10:17:56.782Z] Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCCL

[2026-07-28T10:17:56.782Z] Enable pt (--enable_pt=[0,1])                               : 0

[2026-07-28T10:17:56.782Z] Progress threads (--progress_threads=N)                     : 0

[2026-07-28T10:17:56.782Z] Device list (--device_list=dev1,dev2,...)                   : all

[2026-07-28T10:17:56.782Z] Enable VMM (--enable_vmm=[0,1])                             : 0

[2026-07-28T10:17:56.782Z] Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0

[2026-07-28T10:17:56.782Z] Re-register memory each iteration (--reregister_mem=[0,1])  : 0

[2026-07-28T10:17:56.782Z] Prepared xfer (prep+make) (--prepared_xfer=[0,1])           : 0

[2026-07-28T10:17:56.782Z] Pipeline depth (--pipeline_depth=N)                         : 1

[2026-07-28T10:17:56.782Z] Use hugepages (--use_hugepages=[0,1])                       : 0

[2026-07-28T10:17:56.782Z] Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : VRAM

[2026-07-28T10:17:56.782Z] Target seg type (--target_seg_type=[DRAM,VRAM])             : VRAM

[2026-07-28T10:17:56.782Z] Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise

[2026-07-28T10:17:56.782Z] Mode (--mode=[SG,MG])                                       : SG

[2026-07-28T10:17:56.782Z] Op type (--op_type=[READ,WRITE])                            : READ

[2026-07-28T10:17:56.782Z] Check consistency (--check_consistency=[0,1])               : 1

[2026-07-28T10:17:56.782Z] Total buffer size (--total_buffer_size=N)                   : 80000000

[2026-07-28T10:17:56.782Z] Num initiator dev (--num_initiator_dev=N)                   : 1

[2026-07-28T10:17:56.782Z] Num target dev (--num_target_dev=N)                         : 1

[2026-07-28T10:17:56.782Z] Start block size (--start_block_size=N)                     : 16384

[2026-07-28T10:17:56.782Z] Max block size (--max_block_size=N)                         : 16384

[2026-07-28T10:17:56.782Z] Start batch size (--start_batch_size=N)                     : 4

[2026-07-28T10:17:56.782Z] Max batch size (--max_batch_size=N)                         : 4

[2026-07-28T10:17:56.782Z] Num iter (--num_iter=N)                                     : 1008

[2026-07-28T10:17:56.782Z] Warmup iter (--warmup_iter=N)                               : 112

[2026-07-28T10:17:56.782Z] Large block iter factor (--large_blk_iter_ftr=N)            : 16

[2026-07-28T10:17:56.782Z] Num threads (--num_threads=N)                               : 1

[2026-07-28T10:17:56.782Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:17:56.782Z] 

[2026-07-28T10:17:56.782Z] Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)    

[2026-07-28T10:17:56.782Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:18:04.899Z] 16384               4              0.033098       495.0          61.0           61.0           1403.6         2144.0         576.3          1217.0         

[2026-07-28T10:18:04.899Z] Waiting to accept incoming connection...

[2026-07-28T10:18:04.899Z] Destroying Engine...

[2026-07-28T10:18:05.832Z] Engine destroyed

[2026-07-28T10:18:05.832Z] [WARN mizu01 3522787 3522851 event_loop rdma/epoll_client.h:207] Error/HUP on connection: 1.1.101.1:41049

[2026-07-28T10:18:08.393Z] Server closed connection: 1.1.101.1:40437

[2026-07-28T10:18:08.393Z] Waiting to accept incoming connection...

[2026-07-28T10:18:08.393Z] Destroying Engine...

[2026-07-28T10:18:08.962Z] Engine destroyed

[2026-07-28T10:18:09.897Z] + for target in $seg_types

[2026-07-28T10:18:09.897Z] + run_nixlbench_two_workers_etcd --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type DRAM --check_consistency

[2026-07-28T10:18:09.897Z] + args='--backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type DRAM --check_consistency'

[2026-07-28T10:18:09.897Z] ++ cat /dev/urandom

[2026-07-28T10:18:09.897Z] ++ tr -dc a-zA-Z0-9

[2026-07-28T10:18:09.897Z] ++ fold -w 32

[2026-07-28T10:18:09.897Z] ++ head -n 1

[2026-07-28T10:18:09.897Z] + benchmark_group=33BXdNRKjQx8nx4vPlsuCVFZPQRpcfZq

[2026-07-28T10:18:09.897Z] + command_line='./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 33BXdNRKjQx8nx4vPlsuCVFZPQRpcfZq --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type DRAM --check_consistency'

[2026-07-28T10:18:09.898Z] + parallel --line-buffer --halt now,fail=1 ::: './bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 33BXdNRKjQx8nx4vPlsuCVFZPQRpcfZq --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type DRAM --check_consistency' 'sleep 4 ; ./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group 33BXdNRKjQx8nx4vPlsuCVFZPQRpcfZq --backend UCCL --op_type READ --initiator_seg_type VRAM --target_seg_type DRAM --check_consistency'

[2026-07-28T10:18:11.272Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:18:11.272Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:18:11.272Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:18:11.272Z] ETCD Runtime: Registered as rank 0 item 1 of 2

[2026-07-28T10:18:11.272Z] UCCL backend

[2026-07-28T10:18:11.272Z] Creating Engine

[2026-07-28T10:18:12.646Z] System assigned port: 38391

[2026-07-28T10:18:12.646Z] Endpoint initialized successfully

[2026-07-28T10:18:12.646Z] Waiting to accept incoming connection...

[2026-07-28T10:18:12.646Z] Waiting to accept incoming connection...

[2026-07-28T10:18:12.646Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:18:15.174Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:18:15.174Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:18:15.174Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:18:15.174Z] ETCD Runtime: Registered as rank 1 item 2 of 2

[2026-07-28T10:18:15.174Z] UCCL backend

[2026-07-28T10:18:15.174Z] Creating Engine

[2026-07-28T10:18:16.546Z] System assigned port: 46245

[2026-07-28T10:18:16.546Z] Endpoint initialized successfully

[2026-07-28T10:18:16.546Z] Waiting to accept incoming connection...

[2026-07-28T10:18:16.546Z] Waiting to accept incoming connection...

[2026-07-28T10:18:16.546Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:18:16.546Z] All processes are ready to proceed

[2026-07-28T10:18:16.546Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:18:16.546Z]   [0] mlx5_0

[2026-07-28T10:18:16.546Z]   [1] mlx5_1

[2026-07-28T10:18:16.546Z]   [2] mlx5_2

[2026-07-28T10:18:16.546Z]   [3] mlx5_3

[2026-07-28T10:18:16.546Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:16.546Z] [WARN mizu01 3523293 3523293 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:16.546Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:18:16.546Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:18:16.546Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:18:16.546Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:18:16.546Z] Lazy creation of engine for GPU 0

[2026-07-28T10:18:18.451Z] All processes are ready to proceed

[2026-07-28T10:18:18.451Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:18:18.452Z]   [0] mlx5_0

[2026-07-28T10:18:18.452Z]   [1] mlx5_1

[2026-07-28T10:18:18.452Z]   [2] mlx5_2

[2026-07-28T10:18:18.452Z]   [3] mlx5_3

[2026-07-28T10:18:18.452Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:18.452Z] [WARN mizu01 3523292 3523292 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:18.452Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:18:18.452Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:18:18.452Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:18:18.452Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:18:18.452Z] Lazy creation of engine for GPU 0

[2026-07-28T10:18:20.976Z] [ERROR mizu01 3523292 3523404 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:20.976Z] [ERROR mizu01 3523292 3523405 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:20.976Z] [ERROR mizu01 3523292 3523406 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:20.976Z] Attempting to connect to 1.1.101.1:0 via port 46245

[2026-07-28T10:18:22.346Z] [ERROR mizu01 3523293 3523395 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:22.346Z] [ERROR mizu01 3523293 3523396 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:22.346Z] [ERROR mizu01 3523293 3523397 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:22.346Z] Accepted connection fd=126 from 1.1.101.1:44490

[2026-07-28T10:18:22.346Z] [WARN mizu01 3523293 3523390 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:22.346Z] [WARN mizu01 3523293 3523390 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:22.346Z] [WARN mizu01 3523293 3523390 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:22.346Z] [WARN mizu01 3523293 3523390 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:22.346Z] Connected to 1.1.101.1:38391 (fd=127)

[2026-07-28T10:18:22.346Z] Waiting to accept incoming connection...

[2026-07-28T10:18:22.604Z] Connected to 1.1.101.1:46245 (fd=123)

[2026-07-28T10:18:22.604Z] Accepted connection fd=127 from 1.1.101.1:33896

[2026-07-28T10:18:22.604Z] [WARN mizu01 3523292 3523356 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:22.604Z] [WARN mizu01 3523292 3523356 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:22.604Z] [WARN mizu01 3523292 3523356 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:22.604Z] [WARN mizu01 3523292 3523356 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:22.604Z] ****************************************************************************************************************************************************************

[2026-07-28T10:18:22.604Z] NIXLBench Configuration

[2026-07-28T10:18:22.604Z] ****************************************************************************************************************************************************************

[2026-07-28T10:18:22.604Z] Runtime (--runtime_type=[ETCD,ASIO])                        : ETCD

[2026-07-28T10:18:22.604Z] ETCD Endpoint                                               : http://127.0.0.1:30901/

[2026-07-28T10:18:22.604Z] Worker type (--worker_type=[nixl,nvshmem])                  : nixl

[2026-07-28T10:18:22.604Z] Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCCL

[2026-07-28T10:18:22.604Z] Enable pt (--enable_pt=[0,1])                               : 0

[2026-07-28T10:18:22.604Z] Progress threads (--progress_threads=N)                     : 0

[2026-07-28T10:18:22.604Z] Device list (--device_list=dev1,dev2,...)                   : all

[2026-07-28T10:18:22.604Z] Enable VMM (--enable_vmm=[0,1])                             : 0

[2026-07-28T10:18:22.604Z] Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0

[2026-07-28T10:18:22.604Z] Re-register memory each iteration (--reregister_mem=[0,1])  : 0

[2026-07-28T10:18:22.604Z] Prepared xfer (prep+make) (--prepared_xfer=[0,1])           : 0

[2026-07-28T10:18:22.604Z] Pipeline depth (--pipeline_depth=N)                         : 1

[2026-07-28T10:18:22.604Z] Use hugepages (--use_hugepages=[0,1])                       : 0

[2026-07-28T10:18:22.604Z] Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : VRAM

[2026-07-28T10:18:22.604Z] Target seg type (--target_seg_type=[DRAM,VRAM])             : DRAM

[2026-07-28T10:18:22.604Z] Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise

[2026-07-28T10:18:22.604Z] Mode (--mode=[SG,MG])                                       : SG

[2026-07-28T10:18:22.604Z] Op type (--op_type=[READ,WRITE])                            : READ

[2026-07-28T10:18:22.604Z] Check consistency (--check_consistency=[0,1])               : 1

[2026-07-28T10:18:22.604Z] Total buffer size (--total_buffer_size=N)                   : 80000000

[2026-07-28T10:18:22.604Z] Num initiator dev (--num_initiator_dev=N)                   : 1

[2026-07-28T10:18:22.604Z] Num target dev (--num_target_dev=N)                         : 1

[2026-07-28T10:18:22.604Z] Start block size (--start_block_size=N)                     : 16384

[2026-07-28T10:18:22.604Z] Max block size (--max_block_size=N)                         : 16384

[2026-07-28T10:18:22.604Z] Start batch size (--start_batch_size=N)                     : 4

[2026-07-28T10:18:22.605Z] Max batch size (--max_batch_size=N)                         : 4

[2026-07-28T10:18:22.605Z] Num iter (--num_iter=N)                                     : 1008

[2026-07-28T10:18:22.605Z] Warmup iter (--warmup_iter=N)                               : 112

[2026-07-28T10:18:22.605Z] Large block iter factor (--large_blk_iter_ftr=N)            : 16

[2026-07-28T10:18:22.605Z] Num threads (--num_threads=N)                               : 1

[2026-07-28T10:18:22.605Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:18:22.605Z] 

[2026-07-28T10:18:22.605Z] Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)    

[2026-07-28T10:18:22.605Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:18:34.794Z] 16384               4              1.707205       9.6            96.0           96.0           10.2           18.0           28.0           39.0           

[2026-07-28T10:18:34.794Z] Destroying Engine...

[2026-07-28T10:18:34.794Z] Engine destroyed

[2026-07-28T10:18:34.794Z] [WARN mizu01 3523292 3523356 event_loop rdma/epoll_client.h:207] Error/HUP on connection: 1.1.101.1:46245

[2026-07-28T10:18:37.318Z] Server closed connection: 1.1.101.1:38391

[2026-07-28T10:18:37.318Z] Destroying Engine...

[2026-07-28T10:18:37.318Z] Engine destroyed

[2026-07-28T10:18:37.881Z] + for initiator in $seg_types

[2026-07-28T10:18:37.881Z] + for target in $seg_types

[2026-07-28T10:18:37.881Z] + run_nixlbench_two_workers_etcd --backend UCCL --op_type READ --initiator_seg_type DRAM --target_seg_type VRAM --check_consistency

[2026-07-28T10:18:37.881Z] + args='--backend UCCL --op_type READ --initiator_seg_type DRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:18:37.881Z] ++ cat /dev/urandom

[2026-07-28T10:18:37.881Z] ++ tr -dc a-zA-Z0-9

[2026-07-28T10:18:37.881Z] ++ fold -w 32

[2026-07-28T10:18:37.881Z] ++ head -n 1

[2026-07-28T10:18:37.881Z] + benchmark_group=pBOAJggt8BExh9aBTI48gQOBLNPP5gLx

[2026-07-28T10:18:37.881Z] + command_line='./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group pBOAJggt8BExh9aBTI48gQOBLNPP5gLx --backend UCCL --op_type READ --initiator_seg_type DRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:18:37.881Z] + parallel --line-buffer --halt now,fail=1 ::: './bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group pBOAJggt8BExh9aBTI48gQOBLNPP5gLx --backend UCCL --op_type READ --initiator_seg_type DRAM --target_seg_type VRAM --check_consistency' 'sleep 4 ; ./bin/nixlbench --etcd_endpoints http://127.0.0.1:30901/ --filepath /tmp --total_buffer_size 80000000 --start_block_size 16384 --max_block_size 16384 --start_batch_size 4 --max_batch_size 4 --benchmark_group pBOAJggt8BExh9aBTI48gQOBLNPP5gLx --backend UCCL --op_type READ --initiator_seg_type DRAM --target_seg_type VRAM --check_consistency'

[2026-07-28T10:18:38.832Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:18:38.832Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:18:38.832Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:18:38.832Z] ETCD Runtime: Registered as rank 0 item 1 of 2

[2026-07-28T10:18:38.832Z] UCCL backend

[2026-07-28T10:18:38.832Z] Creating Engine

[2026-07-28T10:18:39.764Z] System assigned port: 39301

[2026-07-28T10:18:39.764Z] Endpoint initialized successfully

[2026-07-28T10:18:39.764Z] Waiting to accept incoming connection...

[2026-07-28T10:18:39.764Z] Waiting to accept incoming connection...

[2026-07-28T10:18:39.764Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:18:43.051Z] WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads

[2026-07-28T10:18:43.051Z] WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads

[2026-07-28T10:18:43.051Z] Connecting to ETCD at http://127.0.0.1:30901/

[2026-07-28T10:18:43.051Z] ETCD Runtime: Registered as rank 1 item 2 of 2

[2026-07-28T10:18:43.051Z] UCCL backend

[2026-07-28T10:18:43.051Z] Creating Engine

[2026-07-28T10:18:43.982Z] System assigned port: 43607

[2026-07-28T10:18:43.982Z] Endpoint initialized successfully

[2026-07-28T10:18:43.982Z] Waiting to accept incoming connection...

[2026-07-28T10:18:43.982Z] Waiting to accept incoming connection...

[2026-07-28T10:18:43.982Z] Waiting for all processes to start... (expecting 2 total: 1 initiators and 1 targets)

[2026-07-28T10:18:43.982Z] All processes are ready to proceed

[2026-07-28T10:18:43.982Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:18:43.982Z]   [0] mlx5_0

[2026-07-28T10:18:43.982Z]   [1] mlx5_1

[2026-07-28T10:18:43.982Z]   [2] mlx5_2

[2026-07-28T10:18:43.982Z]   [3] mlx5_3

[2026-07-28T10:18:43.982Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:18:43.982Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:43.983Z] [WARN mizu01 3523657 3523657 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:43.983Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:18:43.983Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:18:43.983Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:18:43.983Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:18:43.983Z] Lazy creation of engine for GPU 0

[2026-07-28T10:18:45.878Z] All processes are ready to proceed

[2026-07-28T10:18:45.878Z] RdmaDeviceManager: Found 4 RDMA device(s)

[2026-07-28T10:18:45.878Z]   [0] mlx5_0

[2026-07-28T10:18:45.878Z]   [1] mlx5_1

[2026-07-28T10:18:45.878Z]   [2] mlx5_2

[2026-07-28T10:18:45.878Z]   [3] mlx5_3

[2026-07-28T10:18:45.878Z] RdmaDeviceManager: Initialization complete

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:45.878Z] [WARN mizu01 3523656 3523656 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:45.878Z] GPU 0 uses device 0 (mlx5_0)

[2026-07-28T10:18:45.878Z] GPU 0 uses device 1 (mlx5_1)

[2026-07-28T10:18:45.878Z] GPU 0 uses device 2 (mlx5_2)

[2026-07-28T10:18:45.878Z] GPU 0 uses device 3 (mlx5_3)

[2026-07-28T10:18:45.878Z] Lazy creation of engine for GPU 0

[2026-07-28T10:18:48.415Z] [ERROR mizu01 3523656 3523774 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:48.415Z] [ERROR mizu01 3523656 3523776 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:48.415Z] [ERROR mizu01 3523656 3523775 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:48.415Z] Attempting to connect to 1.1.101.1:0 via port 43607

[2026-07-28T10:18:50.312Z] [ERROR mizu01 3523657 3523768 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:50.312Z] [ERROR mizu01 3523657 3523769 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:50.312Z] [ERROR mizu01 3523657 3523770 pin_thread_to_numa ../include/util/util.h:1305] Failed to set thread affinity to NUMA node 1

[2026-07-28T10:18:50.312Z] Accepted connection fd=126 from 1.1.101.1:51202

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523657 3523763 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523657 3523763 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523657 3523763 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523657 3523763 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:50.312Z] Connected to 1.1.101.1:39301 (fd=127)

[2026-07-28T10:18:50.312Z] Waiting to accept incoming connection...

[2026-07-28T10:18:50.312Z] Connected to 1.1.101.1:43607 (fd=126)

[2026-07-28T10:18:50.312Z] Accepted connection fd=127 from 1.1.101.1:42572

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523656 3523719 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_0, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523656 3523719 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_1, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523656 3523719 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_2, distance: 12

[2026-07-28T10:18:50.312Z] [WARN mizu01 3523656 3523719 selectNICs rdma/providers/ib/rdma_device_selection_ib.h:25] NIC: mlx5_3, distance: 12

[2026-07-28T10:18:50.312Z] ****************************************************************************************************************************************************************

[2026-07-28T10:18:50.312Z] NIXLBench Configuration

[2026-07-28T10:18:50.312Z] ****************************************************************************************************************************************************************

[2026-07-28T10:18:50.312Z] Runtime (--runtime_type=[ETCD,ASIO])                        : ETCD

[2026-07-28T10:18:50.312Z] ETCD Endpoint                                               : http://127.0.0.1:30901/

[2026-07-28T10:18:50.312Z] Worker type (--worker_type=[nixl,nvshmem])                  : nixl

[2026-07-28T10:18:50.312Z] Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): UCCL

[2026-07-28T10:18:50.312Z] Enable pt (--enable_pt=[0,1])                               : 0

[2026-07-28T10:18:50.312Z] Progress threads (--progress_threads=N)                     : 0

[2026-07-28T10:18:50.312Z] Device list (--device_list=dev1,dev2,...)                   : all

[2026-07-28T10:18:50.312Z] Enable VMM (--enable_vmm=[0,1])                             : 0

[2026-07-28T10:18:50.312Z] Recreate xfer each iteration (--recreate_xfer=[0,1])        : 0

[2026-07-28T10:18:50.312Z] Re-register memory each iteration (--reregister_mem=[0,1])  : 0

[2026-07-28T10:18:50.312Z] Prepared xfer (prep+make) (--prepared_xfer=[0,1])           : 0

[2026-07-28T10:18:50.312Z] Pipeline depth (--pipeline_depth=N)                         : 1

[2026-07-28T10:18:50.312Z] Use hugepages (--use_hugepages=[0,1])                       : 0

[2026-07-28T10:18:50.312Z] Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : DRAM

[2026-07-28T10:18:50.312Z] Target seg type (--target_seg_type=[DRAM,VRAM])             : VRAM

[2026-07-28T10:18:50.312Z] Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise

[2026-07-28T10:18:50.312Z] Mode (--mode=[SG,MG])                                       : SG

[2026-07-28T10:18:50.312Z] Op type (--op_type=[READ,WRITE])                            : READ

[2026-07-28T10:18:50.312Z] Check consistency (--check_consistency=[0,1])               : 1

[2026-07-28T10:18:50.312Z] Total buffer size (--total_buffer_size=N)                   : 80000000

[2026-07-28T10:18:50.312Z] Num initiator dev (--num_initiator_dev=N)                   : 1

[2026-07-28T10:18:50.312Z] Num target dev (--num_target_dev=N)                         : 1

[2026-07-28T10:18:50.312Z] Start block size (--start_block_size=N)                     : 16384

[2026-07-28T10:18:50.312Z] Max block size (--max_block_size=N)                         : 16384

[2026-07-28T10:18:50.312Z] Start batch size (--start_batch_size=N)                     : 4

[2026-07-28T10:18:50.312Z] Max batch size (--max_batch_size=N)                         : 4

[2026-07-28T10:18:50.312Z] Num iter (--num_iter=N)                                     : 1008

[2026-07-28T10:18:50.312Z] Warmup iter (--warmup_iter=N)                               : 112

[2026-07-28T10:18:50.312Z] Large block iter factor (--large_blk_iter_ftr=N)            : 16

[2026-07-28T10:18:50.312Z] Num threads (--num_threads=N)                               : 1

[2026-07-28T10:18:50.312Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:18:50.312Z] 

[2026-07-28T10:18:50.312Z] Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)    

[2026-07-28T10:18:50.312Z] ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[2026-07-28T10:19:02.498Z] 16384               4              0.025618       639.6          65.0           65.0           1887.7         4617.0         670.3          2469.0         

[2026-07-28T10:19:02.498Z] Waiting to accept incoming connection...

[2026-07-28T10:19:02.498Z] Destroying Engine...

[2026-07-28T10:19:02.498Z] Engine destroyed

[2026-07-28T10:19:05.779Z] Waiting to accept incoming connection...

[2026-07-28T10:19:05.779Z] Destroying Engine...

[2026-07-28T10:19:05.779Z] Stop background accept...

[2026-07-28T10:19:06.035Z] Engine destroyed

[2026-07-28T10:19:06.036Z] [WARN mizu01 3523657 3523764 event_loop rdma/epoll_client.h:207] Error/HUP on connection: 1.1.101.1:39301

[2026-07-28T10:36:15.025Z] Sending interrupt signal to process

[2026-07-28T10:36:15.025Z] Killing processes

[2026-07-28T10:36:15.275Z] kill finished with exit code 0

[2026-07-28T10:36:28.319Z] Terminated

[2026-07-28T10:36:28.324Z] script returned exit code 143
```

## 评论 (7)

### ovidiusm · 2026-07-28

@praveingk could you please take a look?

### praveingk · 2026-07-28

@ovidiusm Thanks for posting the log. This is a weird behavior, where I see that the test has passed, but unable to exit, or observes seg fault. https://github.com/ai-dynamo/nixl/pull/1724 
For now, would it be ok to disable the UCCL tests, while I try to reproduce this is my testbed, and investigate with the above traces enabled.

### ovidiusm · 2026-07-28

Sounds good, thanks! Let me know if you need help

### aranadive · 2026-07-29

@ovidiusm we need to skip the ASIO UCCL tests as well:
https://github.com/ai-dynamo/nixl/blob/3e3e083c97550a1ddca5653389897cb4ebe5e86e/.gitlab/test_nixlbench.sh#L99

### 0z5a · 2026-09-18

@ovidiusm I'd like to take a look at this. I'll first reproduce the UCCL nixlbench hang against current main and narrow down whether it is in transfer completion or teardown/background connection handling.

The attached failure appears to finish the benchmark and destroy both engines before the process stops making progress, so I'll start by instrumenting the UCCL shutdown/accept/event-loop path. If it still reproduces, I'll work on the fix and add regression coverage.


### 0z5a · 2026-09-18

I reproduced a teardown hang in the UCCL p2p engine and have a fix up in
uccl-project/uccl#1054. Posting what is measured, and one thing in the log
above that I do **not** think my fix covers, so we can agree on which hang the
CI is hitting.

## What I reproduced

`del agent` on a UCCL-backed NIXL agent with **no peer and no transfer** — no
nixlbench, no networking partner, no timing threshold other than a 25 s
deadline. Three repetitions per arm, NCCL transport:

| arm | run 1 | run 2 | run 3 | agent release |
| --- | --- | --- | --- | --- |
| unpatched `main` | `rc=137` | `rc=137` | `rc=137` | never returns |
| patched | `rc=0` | `rc=0` | `rc=0` | completes in **0.81 ms** |

`rc=137` is `SIGKILL` from the deadline. The 25 s budget is ~30,000x the patched
release cost, so the unpatched arm is not merely slow.

## Mechanism

`Endpoint::accept()` (`p2p/engine.cc:554`) blocks until `engine_initialized_`,
which is only ever set by `initialize_engine()`, which runs from `reg()`:

```cpp
std::cout << "Waiting to accept incoming connection..." << std::endl;
while (!engine_initialized_) {
  std::this_thread::sleep_for(std::chrono::milliseconds(1));
}
```

An endpoint that never registers memory never leaves that loop.
`Endpoint::~Endpoint()` (`p2p/engine.cc:339`) then joins
`passive_accept_thread_` (`:348`), so the destructor cannot complete.

`stop_accept()` already existed (from #755) but was not observable from this
wait, so shutdown had no way to break it. The patch adds
`RDMAEndpoint::accept_stopped()` / `NCCLEndpoint::accept_stopped()`, wraps them
as `uccl_accept_stopped()`, and checks the stop request inside the wait. It also
seeds `peer_id` with `UINT64_MAX` in `RDMAEndpoint::uccl_accept()` so an aborted
accept returns the invalid `ConnID` callers already reject, instead of a
well-formed id pointing at peer 0.

## What in the log above may be a *different* hang

`"Engine destroyed"` is the **last** statement of `~Endpoint()`
(`p2p/engine.cc:427`), printed after every join. The log shows both engines
reaching it:

```
Waiting to accept incoming connection...
Destroying Engine...
Engine destroyed
...
Stop background accept...
Engine destroyed
[WARN ... event_loop rdma/epoll_client.h:207] Error/HUP on connection: 1.1.101.1:39301
<17 minutes of no progress>
```

So in that run the destructor **did** complete, and the last progress came from
an `event_loop` in `p2p/util/epoll_client.h` on the **RDMA** transport. In my
reproducer the process never even reaches `"Destroying Engine..."`, and I ran it
on the **NCCL** transport (`UCCL_P2P_TRANSPORT=nccl`).

That is a real difference, and I would rather not claim #1054 fixes your CI
until it is checked. Two possibilities:

1. It is the same class of defect on a second thread — a shutdown path that
   waits on progress that only `stop_accept()`/`stop_` can break, this time in
   the rdma epoll loop.
2. It is the same defect and the log ordering is masking it (the two engines in
   the log are separate ranks).

My reproducer is narrow and portable; if you point me at the RDMA-transport
path you use in `nixl-ci-gpu` (or the current `test_nixlbench.sh` skip
conditions from #1724 / the ASIO skip above), I can extend it to the rdma
`event_loop` and confirm which of the two the CI is hitting before we talk about
re-enabling anything.

No NIXL-side change is implied by what I have so far — the defect and the fix are
entirely inside the UCCL p2p engine, so #1054 is where the change belongs.

/cc @ovidiusm @praveingk


### praveingk · 2026-09-20

Thanks @0z5a for taking a look, I will look at the attached UCCL PR. 
