# [Issue #328] NCCL RING Crash on Odd Number of Nodes in Virtualized RoCEv2 Environment

source: https://github.com/NVIDIA/nccl-tests/issues/328
state: open | updated: 2025-07-01T09:29:21Z
labels: 

## 正文

## Describe the issue
We are running nccl-tests in a virtualized environment. We observed that the test runs **normally with an even number of nodes** (e.g., 2, 4, 6, 8), but **fails with an odd number of nodes** (e.g., 3, 5, 7).

When running with 3 nodes, the test errors out. Interestingly, when we manually disable one mlx5 device on each node (e.g., by removing one network interface from nccl environment: NCCL_IB_HCA), the error disappears and the test runs successfully. This behavior is confusing to us.

We are seeking help on how to debug or workaround this issue.

## Environment
Component | Version
-- | --
OS | Ubuntu 20.04
Driver | 550.90.07
CUDA | 12.4
NCCL | 2.20.5-1+cuda12.4
OFED | 23.10-3.2.2.0
Network | RoCEv2
Deployment | Virtual Machines (QEMU)
GPU topo file | [virtualTopology.txt](https://github.com/user-attachments/files/20982866/virtualTopology.txt)

## Test Setup
Tool: nccl-tests (e.g., all_reduce_perf)
Topology: 8 GPUs per node
NCCL-Test command sample:
```bash
mpirun --oversubscribe -np 24 \
-H node1,node2,node3 \
--allow-run-as-root \
-mca plm_rsh_args "-p 22 -q -o StrictHostKeyChecking=no" \
-mca btl_tcp_if_include eth0 \
-x NCCL_IB_DISABLE=0 \
-x NCCL_P2P_DISABLE=0 \
-x NCCL_SOCKET_IFNAME=eth0 \
-x NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_6,mlx5_7 \
-x NCCL_IB_GID_INDEX=3 \
-x NCCL_IB_TC=184 \
-x NCCL_NVLS_ENABLE=1 \
-x NCCL_NET_GDR_LEVEL=3 \
-x NCCL_NET_GDR_READ=1 \
-x NCCL_DEBUG=WARN \
-x NCCL_ALGO=RING \
-x PATH \
/home/nccl-tests/build/all_reduce_perf -b 128M -e 8G -f 2 -g 1
```

## Behavior
Node Count | Result
-- | --
2 nodes | ✅ Normal
3 nodes | ❌ Error
4 nodes | ✅ Normal
5 nodes | ❌ Error
6 nodes | ✅ Normal
7 nodes | ❌ Error
8 nodes | ✅ Normal

## Logs

✅ [2-nodes-nccl-tests.log](https://github.com/user-attachments/files/20983392/2-nodes-nccl-tests.log)
❌ [3-nodes-nccl-tests.log](https://github.com/user-attachments/files/20983406/3-nodes-nccl-tests.log)


Could this be related to the GPU topology configuration file? Any recommended debugging steps or environment variables to trace the issue?



## 评论 (3)

### sjeaugey · 2025-06-30

Could it be you have rails which can't talk to each other hence on odd number of nodes we may try to cross rails and fail?

Would setting NCCL_CROSS_NIC=0 fix the issue?

### pokitpeng · 2025-07-01

> Could it be you have rails which can't talk to each other hence on odd number of nodes we may try to cross rails and fail?
> 
> Would setting NCCL_CROSS_NIC=0 fix the issue?

After configuring with NCCL_CROSS_NIC=0, the 3 nodes can finally work properly, but the performance has decreased. Does this mean that there are communication - unavailable channels in our cluster? We will try to debug each channel. If you have a better way of debugging, please let us know. Thank you very much. 👍

### sjeaugey · 2025-07-01

Thanks for the confirmation. 

Alternate rings(*) avoid crossing rails while minimizing extra NVLink usage, but on an odd number of nodes, they need to cross rails once.

Disabling cross-rail communication unfortunately also disables alternate rings (so that it doesn't crash on odd number of nodes) but it's a bit of a shame for all the even number of nodes cases. Ideally, NCCL would still enable alternate rings even if NCCL_CROSS_NIC is set to 0 when NCCL detects the number of nodes is even. But that would need a bit of work.

What you could do in the meantime is set NCCL_CROSS_NIC=0 when you launch on an odd number of nodes. I know it's not ideal though. Alternatively you could enable cross-rail communication.

* see my GTC 2024 talk on NVIDIA on demand for a full explanation
