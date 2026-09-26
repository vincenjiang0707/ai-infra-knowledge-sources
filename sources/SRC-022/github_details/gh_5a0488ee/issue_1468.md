# [Issue #1468] [Issue]: [UB] ncclRealloc called with null arg in ncclProxyNewConnection

source: https://github.com/ROCm/rccl/issues/1468
state: closed | updated: 2025-01-17T15:12:55Z
labels: Under Investigation

## 正文

### Bug

The `ncclRealloc` call in `ncclProxyNewConnection` can trigger UB because `pool->pools` can be `nullptr`.


https://github.com/ROCm/rccl/blob/648a58dd27634830c8dde593b132597e228f5707/src/proxy.cc#L966-L976

```log
/nix/store/v8zhzm8sf5j71a4c5wmd1bnpm8rqrpr3-gcc-prefix-for-rocm-clang/lib/gcc/x86_64-unknown-linux-gnu/13.3.0/../../../../x86_64-unknown-linux-gnu/include/string.h:44:28: note: nonnull attribute specified here
    #0 0x7fff7bf6d65b in ncclResult_t ncclRealloc<ncclProxyConnection*>(ncclProxyConnection***, unsigned long, unsigned long) /build/source/build/hipify/src/include/alloc.h:79:3
    #1 0x7fff7bf5f1d7 in ncclProxyNewConnection(ncclProxyConnectionPool*, int*) /build/source/build/hipify/src/proxy.cc:968:5
    #2 0x7fff7bf5f1d7 in proxyConnInit(ncclProxyLocalPeer*, ncclProxyConnectionPool*, ncclProxyState*, ncclProxyInitReq*, ncclProxyInitResp*, ncclProxyConnection**) /build/source/build/hipify/src/proxy.cc:1309:3
    #3 0x7fff7bf5f1d7 in proxyProgressAsync(ncclProxyAsyncOp*, ncclProxyState*, int*, ncclProxyLocalPeer*, ncclProxyConnectionPool*) /build/source/build/hipify/src/proxy.cc:1378:11
    #4 0x7fff7bf5bc36 in proxyServiceInitOp(int, ncclProxyLocalPeer*, ncclProxyConnectionPool*, ncclProxyState*, int*) /build/source/build/hipify/src/proxy.cc:1442:3
    #5 0x7fff7bf5bc36 in ncclProxyService(void*) /build/source/build/hipify/src/proxy.cc:1574:19
    #6 0x7ffff749f0d4 in asan_thread_start(void*) (/nix/store/7r6z6nb443psc1ghiyjlqmhwkll7wiia-clr-6.3.0/llvm/lib/linux/libclang_rt.asan-x86_64.so+0x9f0d4)
    #7 0x7ffff69b0d01 in start_thread (/nix/store/pacbfvpzqz2mksby36awvbcn051zcji3-glibc-2.40-36/lib/libc.so.6+0x90d01) (BuildId: 2de6548b3bd2f2857c3c1d5f85e5e817ce2c4a7e)
    #8 0x7ffff6a303ab in __GI___clone3 (/nix/store/pacbfvpzqz2mksby36awvbcn051zcji3-glibc-2.40-36/lib/libc.so.6+0x1103ab) (BuildId: 2de6548b3bd2f2857c3c1d5f85e5e817ce2c4a7e)
```

### Possible Fix

Attempted fix that may be incorrect. It's possible pool->pools being null at this point means something already went wrong elsewhere, or it's expected for the first pool.

I'm not raising this as a PR because I'm not very confident it's correct, but it does prevent the sanitizer finding the UB at runtime.

```diff
diff --git a/src/proxy.cc b/src/proxy.cc
index 50e5437..51bb401 100644
--- a/src/proxy.cc
+++ b/src/proxy.cc
@@ -965,7 +965,11 @@ struct ncclProxyConnectionPool {
 
 static ncclResult_t ncclProxyNewConnection(struct ncclProxyConnectionPool* pool, int* id) {
   if (pool->offset == NCCL_PROXY_CONN_POOL_SIZE) {
-    NCCLCHECK(ncclRealloc(&pool->pools, pool->banks, pool->banks+1));
+    if (pool->pools) {
+      NCCLCHECK(ncclRealloc(&pool->pools, pool->banks, pool->banks+1));
+    } else {
+      NCCLCHECK(ncclCalloc(&pool->pools, pool->banks+1));
+    }
     NCCLCHECK(ncclCalloc(pool->pools+pool->banks, NCCL_PROXY_CONN_POOL_SIZE));
     pool->banks++;
     pool->offset = 0;
```

### Log with UBSAN

```log
I1215 09:31:13.483000 4147518 torch/_inductor/config.py:635] compile_threads set to 12 via env
using device: cuda:2
using device: cuda:0
using device: cuda:3
using device: cuda:1
nixos:4147518:4147518 [0] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147518:4147518 [0] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147518:4147518 [0] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147518:4147518 [0] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147518:4147518 [0] NCCL INFO Kernel version: 6.12.0
nixos:4147518:4147518 [0] NCCL INFO ROCr version 1.1
nixos:4147518:4147518 [0] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147518:4147518 [0] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147518:4147518 [0] NCCL INFO DMA_BUF Support Enabled
RCCL version : 2.21.5-Unknown 
HIP version  : 6.3.42131-
ROCm version : 6.3.0.0-9999-unknown
Hostname     : nixos
Librccl path : /nix/store/54pjbxx1w3q2f3gf8v6jgici0j2ykim6-rccl-6.3.0/lib/librccl.so.1
nixos:4147520:4147520 [2] NCCL INFO ROCr version 1.1
nixos:4147520:4147520 [2] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147520:4147520 [2] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147520:4147520 [2] NCCL INFO DMA_BUF Support Enabled
nixos:4147518:4147518 [0] NCCL INFO Comm config Blocking set to 0
nixos:4147520:4147520 [2] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147520:4147520 [2] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147520:4147520 [2] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147520:4147520 [2] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147520:4147520 [2] NCCL INFO Kernel version: 6.12.0
nixos:4147520:4147520 [2] NCCL INFO Comm config Blocking set to 0
nixos:4147519:4147519 [1] NCCL INFO ROCr version 1.1
nixos:4147519:4147519 [1] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147519:4147519 [1] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147519:4147519 [1] NCCL INFO DMA_BUF Support Enabled
nixos:4147521:4147521 [3] NCCL INFO ROCr version 1.1
nixos:4147521:4147521 [3] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147521:4147521 [3] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147521:4147521 [3] NCCL INFO DMA_BUF Support Enabled
nixos:4147519:4147519 [1] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147521:4147521 [3] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147521:4147521 [3] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147521:4147521 [3] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147521:4147521 [3] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147519:4147519 [1] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147519:4147519 [1] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147519:4147519 [1] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147521:4147521 [3] NCCL INFO Kernel version: 6.12.0
nixos:4147519:4147519 [1] NCCL INFO Kernel version: 6.12.0
nixos:4147521:4147521 [3] NCCL INFO Comm config Blocking set to 0
nixos:4147519:4147519 [1] NCCL INFO Comm config Blocking set to 0
using device: cuda:5
nixos:4147523:4147523 [5] NCCL INFO ROCr version 1.1
nixos:4147523:4147523 [5] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147523:4147523 [5] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147523:4147523 [5] NCCL INFO DMA_BUF Support Enabled
nixos:4147523:4147523 [5] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147523:4147523 [5] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147523:4147523 [5] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147523:4147523 [5] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147523:4147523 [5] NCCL INFO Kernel version: 6.12.0
nixos:4147523:4147523 [5] NCCL INFO Comm config Blocking set to 0
using device: cuda:4
nixos:4147522:4147522 [4] NCCL INFO ROCr version 1.1
nixos:4147522:4147522 [4] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
nixos:4147522:4147522 [4] NCCL INFO Could not open kernel conf file, will assume CONFIG_DMABUF_MOVE_NOTIFY and CONFIG_PCI_P2PDMA are enabled
nixos:4147522:4147522 [4] NCCL INFO DMA_BUF Support Enabled
nixos:4147522:4147522 [4] NCCL INFO Bootstrap : Using eno1np0:10.5.5.236<0>
nixos:4147522:4147522 [4] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
nixos:4147522:4147522 [4] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
nixos:4147522:4147522 [4] NCCL INFO NET/Plugin: Using internal network plugin.
nixos:4147522:4147522 [4] NCCL INFO Kernel version: 6.12.0
nixos:4147522:4147522 [4] NCCL INFO Comm config Blocking set to 0
nixos:4147518:4147542 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147520:4147544 [2] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147521:4147551 [3] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147519:4147552 [1] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147523:4147556 [5] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147522:4147560 [4] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [RO]; OOB eno1np0:10.5.5.236<0>
nixos:4147520:4147544 [2] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147520:4147544 [2] NCCL INFO Using non-device net plugin version 0
nixos:4147520:4147544 [2] NCCL INFO Using network IB
nixos:4147518:4147542 [0] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147518:4147542 [0] NCCL INFO Using non-device net plugin version 0
nixos:4147518:4147542 [0] NCCL INFO Using network IB
nixos:4147520:4147544 [2] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147521:4147551 [3] NCCL INFO Using non-device net plugin version 0
nixos:4147521:4147551 [3] NCCL INFO Using network IB
nixos:4147521:4147551 [3] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147519:4147552 [1] NCCL INFO Using non-device net plugin version 0
nixos:4147519:4147552 [1] NCCL INFO Using network IB
nixos:4147519:4147552 [1] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147523:4147556 [5] NCCL INFO Using non-device net plugin version 0
nixos:4147523:4147556 [5] NCCL INFO Using network IB
nixos:4147523:4147556 [5] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147522:4147560 [4] NCCL INFO Using non-device net plugin version 0
nixos:4147522:4147560 [4] NCCL INFO Using network IB
nixos:4147522:4147560 [4] NCCL INFO [node_id = 4; gpu_id = 30316; unique_id = 2876663883641298920; location_id = 35584; bdf = 35584; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO [node_id = 5; gpu_id = 58073; unique_id = 3090750370579070170; location_id = 50432; bdf = 50432; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO [node_id = 2; gpu_id = 17080; unique_id = 4359167370986682921; location_id = 17664; bdf = 17664; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO [node_id = 6; gpu_id = 30493; unique_id = 13203522840874857286; location_id = 51200; bdf = 51200; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO [node_id = 1; gpu_id = 17353; unique_id = 17700076029037887337; location_id = 1536; bdf = 1536; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO [node_id = 3; gpu_id = 55164; unique_id = 18169316936904435185; location_id = 18432; bdf = 18432; domain = 0; partition = 0], 
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 5 nranks 6 cudaDev 5 nvmlDev 5 busId c8000 commId 0xd3c919769d841c22 - Init START
nixos:4147522:4147560 [4] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 4 nranks 6 cudaDev 4 nvmlDev 4 busId c5000 commId 0xd3c919769d841c22 - Init START
nixos:4147521:4147551 [3] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 3 nranks 6 cudaDev 3 nvmlDev 3 busId 8b000 commId 0xd3c919769d841c22 - Init START
nixos:4147519:4147552 [1] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 1 nranks 6 cudaDev 1 nvmlDev 1 busId 45000 commId 0xd3c919769d841c22 - Init START
nixos:4147520:4147544 [2] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 2 nranks 6 cudaDev 2 nvmlDev 2 busId 48000 commId 0xd3c919769d841c22 - Init START
nixos:4147518:4147542 [0] NCCL INFO ncclCommInitRank comm 0x530000380400 rank 0 nranks 6 cudaDev 0 nvmlDev 0 busId 6000 commId 0xd3c919769d841c22 - Init START
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147520:4147544 [2] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147519:4147552 [1] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147521:4147551 [3] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147523:4147556 [5] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147518:4147542 [0] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147522:4147560 [4] NCCL INFO initialized internal alternative rsmi functionality
nixos:4147522:4147560 [4] NCCL INFO GDRDMA not enabled. Could not find memory_peers directory or peer_memory symbol
nixos:4147521:4147551 [3] NCCL INFO Setting affinity for GPU 3 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147520:4147544 [2] NCCL INFO Setting affinity for GPU 2 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147519:4147552 [1] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147523:4147556 [5] NCCL INFO Setting affinity for GPU 5 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147522:4147560 [4] NCCL INFO Setting affinity for GPU 4 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147518:4147542 [0] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff,ffffffff,ffffffff
nixos:4147519:4147552 [1] NCCL INFO comm 0x530000380400 rank 1 nRanks 6 nNodes 1 localRanks 6 localRank 1 MNNVL 0
nixos:4147518:4147542 [0] NCCL INFO comm 0x530000380400 rank 0 nRanks 6 nNodes 1 localRanks 6 localRank 0 MNNVL 0
nixos:4147523:4147556 [5] NCCL INFO comm 0x530000380400 rank 5 nRanks 6 nNodes 1 localRanks 6 localRank 5 MNNVL 0
nixos:4147518:4147542 [0] NCCL INFO Channel 00/04 :    0   1   2   3   4   5
nixos:4147519:4147552 [1] NCCL INFO Trees [0] 2/-1/-1->1->0 [1] 2/-1/-1->1->0 [2] 2/-1/-1->1->0 [3] 2/-1/-1->1->0 comm 0x530000380400 nRanks 06 busId 45000
nixos:4147522:4147560 [4] NCCL INFO comm 0x530000380400 rank 4 nRanks 6 nNodes 1 localRanks 6 localRank 4 MNNVL 0
nixos:4147521:4147551 [3] NCCL INFO comm 0x530000380400 rank 3 nRanks 6 nNodes 1 localRanks 6 localRank 3 MNNVL 0
nixos:4147518:4147542 [0] NCCL INFO Channel 01/04 :    0   1   2   3   4   5
nixos:4147519:4147552 [1] NCCL INFO P2P Chunksize set to 131072
nixos:4147518:4147542 [0] NCCL INFO Channel 02/04 :    0   1   2   3   4   5
nixos:4147518:4147542 [0] NCCL INFO Channel 03/04 :    0   1   2   3   4   5
nixos:4147523:4147556 [5] NCCL INFO Trees [0] -1/-1/-1->5->4 [1] -1/-1/-1->5->4 [2] -1/-1/-1->5->4 [3] -1/-1/-1->5->4 comm 0x530000380400 nRanks 06 busId c8000
nixos:4147518:4147542 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 [2] 1/-1/-1->0->-1 [3] 1/-1/-1->0->-1 comm 0x530000380400 nRanks 06 busId 6000
nixos:4147523:4147556 [5] NCCL INFO P2P Chunksize set to 131072
nixos:4147522:4147560 [4] NCCL INFO Trees [0] 5/-1/-1->4->3 [1] 5/-1/-1->4->3 [2] 5/-1/-1->4->3 [3] 5/-1/-1->4->3 comm 0x530000380400 nRanks 06 busId c5000
nixos:4147518:4147542 [0] NCCL INFO P2P Chunksize set to 131072
nixos:4147521:4147551 [3] NCCL INFO Trees [0] 4/-1/-1->3->2 [1] 4/-1/-1->3->2 [2] 4/-1/-1->3->2 [3] 4/-1/-1->3->2 comm 0x530000380400 nRanks 06 busId 8b000
nixos:4147522:4147560 [4] NCCL INFO P2P Chunksize set to 131072
nixos:4147521:4147551 [3] NCCL INFO P2P Chunksize set to 131072
nixos:4147520:4147544 [2] NCCL INFO comm 0x530000380400 rank 2 nRanks 6 nNodes 1 localRanks 6 localRank 2 MNNVL 0
nixos:4147520:4147544 [2] NCCL INFO Trees [0] 3/-1/-1->2->1 [1] 3/-1/-1->2->1 [2] 3/-1/-1->2->1 [3] 3/-1/-1->2->1 comm 0x530000380400 nRanks 06 busId 48000
nixos:4147520:4147544 [2] NCCL INFO P2P Chunksize set to 131072
/build/source/build/hipify/src/include/alloc.h:79:13: runtime error: null pointer passed as argument 2, which is declared to never be null
/nix/store/v8zhzm8sf5j71a4c5wmd1bnpm8rqrpr3-gcc-prefix-for-rocm-clang/lib/gcc/x86_64-unknown-linux-gnu/13.3.0/../../../../x86_64-unknown-linux-gnu/include/string.h:44:28: note: nonnull attribute specified here
    #0 0x7fff7bf6d65b in ncclResult_t ncclRealloc<ncclProxyConnection*>(ncclProxyConnection***, unsigned long, unsigned long) /build/source/build/hipify/src/include/alloc.h:79:3
    #1 0x7fff7bf5f1d7 in ncclProxyNewConnection(ncclProxyConnectionPool*, int*) /build/source/build/hipify/src/proxy.cc:968:5
    #2 0x7fff7bf5f1d7 in proxyConnInit(ncclProxyLocalPeer*, ncclProxyConnectionPool*, ncclProxyState*, ncclProxyInitReq*, ncclProxyInitResp*, ncclProxyConnection**) /build/source/build/hipify/src/proxy.cc:1309:3
    #3 0x7fff7bf5f1d7 in proxyProgressAsync(ncclProxyAsyncOp*, ncclProxyState*, int*, ncclProxyLocalPeer*, ncclProxyConnectionPool*) /build/source/build/hipify/src/proxy.cc:1378:11
    #4 0x7fff7bf5bc36 in proxyServiceInitOp(int, ncclProxyLocalPeer*, ncclProxyConnectionPool*, ncclProxyState*, int*) /build/source/build/hipify/src/proxy.cc:1442:3
    #5 0x7fff7bf5bc36 in ncclProxyService(void*) /build/source/build/hipify/src/proxy.cc:1574:19
    #6 0x7ffff749f0d4 in asan_thread_start(void*) (/nix/store/7r6z6nb443psc1ghiyjlqmhwkll7wiia-clr-6.3.0/llvm/lib/linux/libclang_rt.asan-x86_64.so+0x9f0d4)
    #7 0x7ffff69b0d01 in start_thread (/nix/store/pacbfvpzqz2mksby36awvbcn051zcji3-glibc-2.40-36/lib/libc.so.6+0x90d01) (BuildId: 2de6548b3bd2f2857c3c1d5f85e5e817ce2c4a7e)
    #8 0x7ffff6a303ab in __GI___clone3 (/nix/store/pacbfvpzqz2mksby36awvbcn051zcji3-glibc-2.40-36/lib/libc.so.6+0x1103ab) (BuildId: 2de6548b3bd2f2857c3c1d5f85e5e817ce2c4a7e)
```

Triggered by using pytorch DDP with dist nccl backend `dist.init_process_group(backend='nccl', device_id=device)`.

## 评论 (5)

### sohaibnd · 2025-01-02

Hi @LunNova, can you please provide more information about your setup and a sample of the pytorch code you are running to reproduce this issue. Also, did you observe any other problem running the code normally or is it just being flagged by UBSAN?

### sohaibnd · 2025-01-15

@LunNova Closing this issue due to inactivity. If you are still seeing the sanitizer detecting undefined behavior, please re-open this issue and provide the information asked above.

### LunNova · 2025-01-15

Sorry for the delay here, I missed your response. I'll provide a reproducer script or confirm it's fixed depending on what I find when I retest.

### LunNova · 2025-01-17

Testing on develop (2e35417fe5252b3fbc9713b542b8ee89e3e8ee56) I wasn't able to reproduce it. I didn't take sufficient notes on what exactly I did when I ran into it initially so I'm not sure if that's because it's fixed now or if I've just failed to reproduce it 😅
If I run into it again I'll be more thorough documenting.

### sohaibnd · 2025-01-17

No worries, you can update this ticket if you run into it again.
