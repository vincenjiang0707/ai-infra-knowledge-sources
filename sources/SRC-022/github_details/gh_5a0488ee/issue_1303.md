# [Issue #1303] RCCL initialization fails when PXN is disabled (RoCEv2, ibv_modify_qp failed with error)

source: https://github.com/ROCm/rccl/issues/1303
state: closed | updated: 2024-11-11T21:21:18Z
labels: Under Investigation

## 正文

Hello, I have 4 AI servers, each equipped with 8 MI300x and 8 ConnectX-6 (RoCEv2).

System configuration
- All CX6 NICs are connected through a single L2 Ethernet switch.
- GPUDirect RDMA is being used.
- ROCm 6.2.0 is installed
- I have assigned different subnets to different NICs within a node to avoid ARP flux issues.

![image](https://github.com/user-attachments/assets/94e55211-b1e1-4f99-888d-20e558f7980a)

According to this issue ([link](https://github.com/ROCm/rccl/issues/1209)), RCCL has PXN disabled by default. However, when I run AI training workloads, if PXN is disabled, RCCL initialization fails with an error: `NCCL WARN Call to ibv_modify_qp failed with error`. When I enable PXN, the workload runs fine.




Here, I confirmed that when PXN is disabled, RCCL attempts to create a Queue pair (QP) between two NICs that have different subnets. For example, a QP is created between NIC3 of node1 and NIC7 of node2. However, since the subnets of these NICs are different, the QP connection does not function properly, and it seems that RCCL initialization fails as a result. I also tried configuring all NICs in the system to have the same subnet, but when multiple NICs within the same node share the same subnet, ARP flux causes the system to still not function properly.


Therefore, **my question is whether this error is expected behavior and whether I must always run my workload with PXN enabled.** Based on the figure below describing PXN, it seems that such cross-rail communication is indeed expected. If that's the case, is there any way to avoid `ibv_modify_qp failed with error` when PXN is disabled?

![image](https://github.com/user-attachments/assets/eaefe8ba-993d-4f46-8783-a278e5c5f4de)




## 评论 (3)

### jlochhead · 2024-10-17

In NCCL environments we have to set NCCL_IB_GID_INDEX=3 for communications to work between subnets. I haven't tried with RCCL yet, but I suspect it is the same.

### tcgu-amd · 2024-10-29

Hi @cold2stone sorry for the lack of response and thank you for reaching out! Based on your description, it seems to be a known routing issue of RCCL and we are working on fixing it. In the meantime, you may want to try a workaround by setting `NCCL_CROSS_NIC=0` to get NCCL working without using PXN for now. 

In addition, in case that wasn't your issue, it would help us better diagnose the problem if you can set `NCCL_DEBUG=INFO` and `NCCL_TOPO_DUMP_FILE=<path to your file>`, and show the corresponding outputs. 

Hope this helps. Thanks!

### tcgu-amd · 2024-11-11

@cold2stone This issue will be closed for now due to inactivity. Please feel free to re-open for more follow up. Thanks!
