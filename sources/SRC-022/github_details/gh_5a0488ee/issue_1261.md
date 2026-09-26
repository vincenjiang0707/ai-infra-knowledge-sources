# [Issue #1261] Encountering issues while using the UCX plugin

source: https://github.com/ROCm/rccl/issues/1261
state: closed | updated: 2025-01-02T21:05:04Z
labels: Under Investigation

## 正文

When using rccl rdma sharp plugin, I encountered a program crash with the following log:
```
`[root@node01 ~]# mpirun \
>     -np 2\
>     --oversubscribe \
>     --allow-run-as-root\
>     -H node01,node02 \
>     -x NCCL_DEBUG=INFO \
>     -x UCX_PROTO_ENABLE=n\
>     -x NCCL_P2P_LEVEL=5 \
>     -x NCCL_NET_GDR_LEVEL=5 \
>     -x HSA_FORCE_FINE_GRAIN_PCIE=1\
>     -x NCCL_PLUGIN_P2P=UCX\
>     -x LD_LIBRARY_PATH=/root/hsm/rccl-rdma-sharp-plugins-master/install/lib:$LD_LIBRARY_PATH\
>     /root/hsm/rccl-tests-develop/build/reduce_perf -g 1 -n 20 -b 1024 -e 512M -f 2
# nThreads: 1 nGpus: 1 nRanks: 1 minBytes: 1024 maxBytes: 536870912 step: 2(factor) warmupIters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
node01:5646:5646 [0] NCCL INFO Bootstrap : Using ens52np0:192.168.2.11<0>
node01:5646:5646 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v6 symbol.
node01:5646:5646 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin (v4)
node01:5646:5646 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
node01:5646:5646 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin symbol (v4 or v5).

node01:5646:5646 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:115 NCCL WARN NUMA auto balancing enabled which can lead to variability in the RCCL performance! Disable by "sudo sysctl kernel.numa_balancing=0"
node01:5646:5646 [0] NCCL INFO Kernel version: 4.18.0-305.3.1.el8.x86_64

node01:5646:5646 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:136 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
node01:5646:5646 [0] NCCL INFO ROCr version 1.1
node01:5646:5646 [0] NCCL INFO Dmabuf feature disabled without NCCL_ENABLE_DMABUF_SUPPORT=1
RCCL version 2.18.3+hip5.7 HEAD:b502725
node01:5646:5657 [0] NCCL INFO Plugin Path : /root/hsm/rccl-rdma-sharp-plugins-master/install/lib/librccl-net.so
node01:5646:5657 [0] NCCL INFO P2P plugin UCX
node01:5646:5657 [0] NCCL INFO NET/IB : Using [0]bnxt_re0:1/RoCE ; OOB ens52np0:192.168.2.11<0>
node01:5646:5657 [0] NCCL INFO Using network UCX
node02:10366:10366 [0] NCCL INFO ROCr version 1.1
node02:10366:10366 [0] NCCL INFO Dmabuf feature disabled without NCCL_ENABLE_DMABUF_SUPPORT=1
node02:10366:10366 [0] NCCL INFO Bootstrap : Using ens7np0:192.168.2.12<0>
node02:10366:10366 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v6 symbol.
node02:10366:10366 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin (v4)
node02:10366:10366 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
node02:10366:10366 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin symbol (v4 or v5).
node02:10366:10366 [0] NCCL INFO Kernel version: 4.18.0-305.3.1.el8.x86_64

node02:10366:10366 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:136 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
node02:10366:10376 [0] NCCL INFO Plugin Path : /root/hsm/rccl-rdma-sharp-plugins-master/install/lib/librccl-net.so
node02:10366:10376 [0] NCCL INFO P2P plugin UCX
node02:10366:10376 [0] NCCL INFO NET/IB : Using [0]bnxt_re0:1/RoCE ; OOB ens7np0:192.168.2.12<0>
node02:10366:10376 [0] NCCL INFO Using network UCX
node01:5646:5657 [0] NCCL INFO comm 0x22fcfb0 rank 0 nranks 2 cudaDev 0 busId b7000 commId 0xf503b714f0d84435 - Init START
node02:10366:10376 [0] NCCL INFO comm 0x2197130 rank 1 nranks 2 cudaDev 0 busId 7000 commId 0xf503b714f0d84435 - Init START
node02:10366:10376 [0] NCCL INFO rocm_smi_lib: version 2.8.0.0
node01:5646:5657 [0] NCCL INFO rocm_smi_lib: version 2.8.0.0
node02:10366:10376 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to SYS
node02:10366:10376 [0] NCCL INFO PXN Disabled as plugin is v4
node02:10366:10376 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to SYS
node01:5646:5657 [0] NCCL INFO NCCL_TOPO_DUMP_FILE set by environment to /root/hsm/topo/topo2.xml
node02:10366:10376 [0] NCCL INFO Setting affinity for GPU 0 to 01,00000000,00000001
node01:5646:5657 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to SYS
node01:5646:5657 [0] NCCL INFO PXN Disabled as plugin is v4
node01:5646:5657 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to SYS
node01:5646:5657 [0] NCCL INFO Channel 00/04 :    0   1
node01:5646:5657 [0] NCCL INFO Channel 01/04 :    0   1
node01:5646:5657 [0] NCCL INFO Channel 02/04 :    0   1
node01:5646:5657 [0] NCCL INFO Channel 03/04 :    0   1
node01:5646:5657 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1 [2] 1/-1/-1->0->-1 [3] -1/-1/-1->0->1 comm 0x22fcfb0 nRanks 02 busId b7000
node01:5646:5657 [0] NCCL INFO P2P Chunksize set to 131072
node02:10366:10376 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1 [2] -1/-1/-1->1->0 [3] 0/-1/-1->1->-1 comm 0x2197130 nRanks 02 busId 7000
node02:10366:10376 [0] NCCL INFO P2P Chunksize set to 131072
node01:5646:5657 [0] NCCL INFO Channel 00/0 : 1[7000] -> 0[b7000] [receive] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 01/0 : 1[7000] -> 0[b7000] [receive] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 02/0 : 1[7000] -> 0[b7000] [receive] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 03/0 : 1[7000] -> 0[b7000] [receive] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 00/0 : 0[b7000] -> 1[7000] [send] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 01/0 : 0[b7000] -> 1[7000] [send] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 02/0 : 0[b7000] -> 1[7000] [send] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node01:5646:5657 [0] NCCL INFO Channel 03/0 : 0[b7000] -> 1[7000] [send] via NET/UCX/0/GDRDMA comm 0x22fcfb0 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 00/0 : 0[b7000] -> 1[7000] [receive] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 01/0 : 0[b7000] -> 1[7000] [receive] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 02/0 : 0[b7000] -> 1[7000] [receive] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 03/0 : 0[b7000] -> 1[7000] [receive] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 00/0 : 1[7000] -> 0[b7000] [send] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 01/0 : 1[7000] -> 0[b7000] [send] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 02/0 : 1[7000] -> 0[b7000] [send] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
node02:10366:10376 [0] NCCL INFO Channel 03/0 : 1[7000] -> 0[b7000] [send] via NET/UCX/0/GDRDMA comm 0x2197130 nRanks 02
[1721186746.658016] [node02:10366:1]          rcache.c:985  UCX  ERROR failed to insert region 0x1479900ba210 [0x0..0x0]: Invalid parameter

node02:10366:10377 [0] ucx_plugin.c:498 NCCL WARN Failed: UCX error ucx_plugin.c:498 '-5' Invalid parameter

node02:10366:10377 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport/net.cc:858 -> 3
node02:10366:10377 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1311 -> 3
node02:10366:10377 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1382 -> 3

node02:10366:10377 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1524 NCCL WARN [Proxy Service 1] Failed to execute operation Connect from rank 1, retcode 3

node02:10366:10376 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/misc/socket.cc:57 NCCL WARN socketProgress: Connection closed by remote peer node02<35187>
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/misc/socket.cc:791 -> 6

node02:10366:10376 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1148 NCCL WARN Socket recv failed while polling for opId=0x147999b41d80
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport/net.cc:311 -> 3
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport.cc:164 -> 3
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:1448 -> 3
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:1758 -> 3
node02:10366:10376 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:69 -> 3 [Async thread]
node02:10366:10366 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:431 -> 3
node02:10366:10366 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:116 -> 3
node02: Test NCCL failure common.cu:1158 'internal error - please report this issue to the NCCL developers / '
 .. node02 pid 10366: Test failure common.cu:1000
[1721186744.314330] [node01:5646 :0]          rcache.c:985  UCX  ERROR failed to insert region 0x15045c0b4ad0 [0x0..0x0]: Invalid parameter

node01:5646:5659 [0] ucx_plugin.c:498 NCCL WARN Failed: UCX error ucx_plugin.c:498 '-5' Invalid parameter

node01:5646:5659 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport/net.cc:858 -> 3
node01:5646:5659 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1311 -> 3
node01:5646:5659 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1382 -> 3

node01:5646:5659 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1524 NCCL WARN [Proxy Service 0] Failed to execute operation Connect from rank 0, retcode 3
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------

node01:5646:5657 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/misc/socket.cc:57 NCCL WARN socketProgress: Connection closed by remote peer node01<51339>
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/misc/socket.cc:791 -> 6

node01:5646:5657 [0] /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/proxy.cc:1148 NCCL WARN Socket recv failed while polling for opId=0x1503f5b41a28
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport/net.cc:385 -> 3
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/transport.cc:184 -> 3
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:1448 -> 3
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/init.cc:1758 -> 3
node01:5646:5657 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:69 -> 3 [Async thread]
node01:5646:5646 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:431 -> 3
node01:5646:5646 [0] NCCL INFO /data/jenkins_workspace/workspace/rccl_release/build/hipify/src/group.cc:116 -> 3
node01: Test NCCL failure common.cu:1158 'internal error - please report this issue to the NCCL developers / '
 .. node01 pid 5646: Test failure common.cu:1000
--------------------------------------------------------------------------
mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[2403,1],1]
  Exit code:    3
`
```
It seems that there is an issue with enabling GDR when using the UCX plugin with the parameter HSA_FORCE. FINE-GRAIN-PCIE=1. However, when HSA_FORCE. FINE-GRAIN-PCIE=0, it can run, but performance may decrease due to the inability to use GDR. Without using the UCX plugin (calling IB), there is no such issue. May I ask if there is a better solution?


## 评论 (1)

### huanrwan-amd · 2024-11-11

Hi @clearsky07, can you please provide the ROCm and rccl version and hardware info? Thanks.
