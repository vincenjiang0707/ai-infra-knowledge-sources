# [Issue #360] Multi-node all_reduce_perf / alltoall_perf failures: socketFinalizeAccept wrong type 4 != 3 over TCP and IB QP invalid request errors

source: https://github.com/NVIDIA/nccl-tests/issues/360
state: open | updated: 2025-11-24T17:57:54Z
labels: 

## 正文

I'm trying to run all_reduce_perf script and it fails in any configuration. For example following script:
```bash
#!/usr/bin/env bash
set -euo pipefail

IFACE="ens1"
BIN="./build/all_reduce_perf_mpi"

export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=INIT,NET
export NCCL_ASYNC_ERROR_HANDLING=1

export NCCL_IB_DISABLE=1
export NCCL_SOCKET_IFNAME="${IFACE}"

mpirun --allow-run-as-root --mca orte_base_help_aggregate 0 --mca oob_tcp_if_include ens1 --mca btl_tcp_if_include ens1 \
  -H "${HEAD_HOST}:8,${WORKER_HOST}:8" \
  -np 16 \
  "${BIN}" -b 8M -e 128M -f 2 -g 1
```
gives this output:
```
node-0:5124:5182 [7] NCCL INFO Connected to proxy localRank 7 -> connection 0x7c82e0002238
node-0:5124:5182 [7] NCCL INFO Channel 14/0 : 7[7] -> 6[6] via P2P/CUMEM
node-0:5124:5166 [7] NCCL INFO New proxy send connection 46 from local rank 7, transport 0
node-0:5124:5182 [7] NCCL INFO Connected to proxy localRank 7 -> connection 0x7c82e00022b0
node-0:5124:5182 [7] NCCL INFO Channel 15/0 : 7[7] -> 6[6] via P2P/CUMEM
node-0:5124:5166 [7] NCCL INFO New proxy send connection 47 from local rank 7, transport 0
node-0:5124:5182 [7] NCCL INFO Connected to proxy localRank 7 -> connection 0x7c82e0002328
node-0:5113:5183 [3] NCCL INFO Connected to proxy localRank 2 -> connection 0x7b6fc0002b98
node-0:5111:5176 [2] NCCL INFO New proxy send connection 65 from local rank 3, transport 0
node-0:5121:5169 [6] NCCL INFO New proxy send connection 65 from local rank 7, transport 0
node-0:5124:5166 [7] NCCL INFO New proxy send connection 48 from local rank 6, transport 0
node-0:5124:5182 [7] NCCL INFO Connected to proxy localRank 6 -> connection 0x76d3d0002b98
node-0:5121:5186 [6] NCCL INFO Connected to proxy localRank 7 -> connection 0x7c82e00023a0
node-0:5118:5168 [5] NCCL INFO New proxy send connection 65 from local rank 6, transport 0
node-0:5121:5186 [6] NCCL INFO Connected to proxy localRank 5 -> connection 0x7dc2cc002b98
node-0:5124:5166 [7] NCCL INFO New proxy send connection 49 from local rank 0, transport 0
node-0:5109:5188 [0] NCCL INFO Connected to proxy localRank 7 -> connection 0x7c82e0002418

node-0:5109:5177 [0] misc/socket.cc:502 NCCL WARN socketFinalizeAccept: wrong type 4 != 3
node-0:5109:5177 [0] NCCL INFO misc/socket.cc:628 -> 3
node-0:5109:5177 [0] NCCL INFO misc/socket.cc:653 -> 3
node-0:5109:5177 [0] NCCL INFO transport/net_socket.cc:403 -> 3
node-0:5109:5177 [0] NCCL INFO transport/net.cc:883 -> 3

node-0:5109:5177 [0] misc/socket.cc:502 NCCL WARN socketFinalizeAccept: wrong type 4 != 3
node-0:5109:5177 [0] NCCL INFO misc/socket.cc:628 -> 3
node-0:5109:5177 [0] NCCL INFO misc/socket.cc:653 -> 3
node-0:5109:5177 [0] NCCL INFO transport/net_socket.cc:403 -> 3
node-0:5109:5177 [0] NCCL INFO transport/net.cc:883 -> 3

node-0:5111:5176 [2] misc/socket.cc:502 NCCL WARN socketFinalizeAccept: wrong type 4 != 3
node-0:5111:5176 [2] NCCL INFO misc/socket.cc:628 -> 3
node-0:5111:5176 [2] NCCL INFO misc/socket.cc:653 -> 3
node-0:5111:5176 [2] NCCL INFO transport/net_socket.cc:403 -> 3
node-0:5111:5176 [2] NCCL INFO transport/net.cc:883 -> 3

node-0:5111:5176 [2] misc/socket.cc:502 NCCL WARN socketFinalizeAccept: wrong type 4 != 3
node-0:5111:5176 [2] NCCL INFO misc/socket.cc:628 -> 3
node-0:5111:5176 [2] NCCL INFO misc/socket.cc:653 -> 3
node-0:5111:5176 [2] NCCL INFO transport/net_socket.cc:403 -> 3
node-0:5111:5176 [2] NCCL INFO transport/net.cc:883 -> 3
```
Complete log is in the attachment. 

[log_no_ib.txt](https://github.com/user-attachments/files/23700264/log_no_ib.txt)

Enabling IB somehow makes all_reduce_perf pass, but when I change to alltoall_perf I encounter different issue:

```
node-0:5898:6033 [0] NCCL INFO NET/IB: IbDev 0 Port 1 qpn 2740 set_ece={supported=1, vendor_id=0x15b3, options=0x0, comp_mask=0x0}

node-0:5911:5971 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_3:1 async fatal event on QP (0x732d78661238): invalid request local work queue error

node-0:5911:5971 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_3:1 async fatal event on QP (0x732d78f4d338): invalid request local work queue error

node-0:5911:5971 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_3:1 async fatal event on QP (0x732d78f9bc38): invalid request local work queue error

node-0:5914:6002 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_7:1 async fatal event on QP (0x777e20ed1a48): invalid request local work queue error

node-0:5914:6002 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_7:1 async fatal event on QP (0x777e2033fa48): invalid request local work queue error

node-0:5900:5962 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_2:1 async fatal event on QP (0x71b3442663d8): invalid request local work queue error

node-0:5902:5992 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_6:1 async fatal event on QP (0x7bf530835c08): invalid request local work queue error

node-0:5907:6008 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_5:1 async fatal event on QP (0x741c98c56c08): invalid request local work queue error

node-0:5907:6008 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_5:1 async fatal event on QP (0x741c985a0be8): invalid request local work queue error

node-0:5899:5969 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_4:1 async fatal event on QP (0x762cfc06f8c8): invalid request local work queue error

node-0:5899:5969 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_4:1 async fatal event on QP (0x762cfc0e23c8): invalid request local work queue error

node-0:5899:6045 [1] transport/net_ib.cc:113 NCCL WARN communicator encountered a fatal error (detected in ncclIbIrecv)

node-0:5899:6045 [1] NCCL INFO transport/net_ib.cc:2117 -> 2
node-0:5899:6045 [1] NCCL INFO transport/net.cc:1335 -> 2
node-0:5899:6045 [1] NCCL INFO proxy.cc:728 -> 2
node-0:5899:6045 [1] NCCL INFO proxy.cc:912 -> 2 [Progress Thread]

node-0:5899:6045 [1] transport/net_ib.cc:113 NCCL WARN communicator encountered a fatal error (detected in ncclIbIrecv)
```
Full log: 

[log_ib.txt](https://github.com/user-attachments/files/23700306/log_ib.txt)

All single node tests pass without any issues.

Is it a known symptom of misconfiguration or does it point to something else? 


## 评论 (4)

### AddyLaddy · 2025-11-24

With `mpirun` you have to pass every env var on the command line with `-x <env>` e.g. `-x NCCL_DEBUG=INFO` or `-x LD_LIBRARY_PATH`

### AlexanderNekrasov · 2025-11-24

I noticed that changing env vars using export changes behavior of scripts, that's why I used that. And also mpirun --help doesn't show me -x option. But if I pass everything using -x i can get all_reduce_perf run both with ib and without it. alltoall_perf once again runs without ib and fails when I turn it on. It looks like error messages are mostly the same as before, but I'll attach everything once again.
```bash
#!/usr/bin/env bash
set -euo pipefail

IFACE="ens1"
BIN="./build/alltoall_perf_mpi"

mpirun --allow-run-as-root --mca orte_base_help_aggregate 0 --mca oob_tcp_if_include ens1 --mca btl_tcp_if_include ens1 \
  -x NCCL_DEBUG=INFO -x NCCL_DEBUG_SUBSYS=INIT,NET -x NCCL_ASYNC_ERROR_HANDLING=1 -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=ens1 \
  -H "${HEAD_HOST}:8,${WORKER_HOST}:8" \
  -np 16 \
  "${BIN}" -b 8M -e 128M -f 2 -g 1
```

[new_log_ib.txt](https://github.com/user-attachments/files/23728077/new_log_ib.txt)

### AddyLaddy · 2025-11-24

Ok great thanks that looks better but the issue still remains 

```
node-0:139583:139647 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_3:1 async fatal event on QP (0x76fda4c32a68): invalid request local work queue error

node-0:139586:139664 [0] transport/net_ib.cc:154 NCCL WARN NET/IB : mlx5_7:1 async fatal event on QP (0x7c59288369b8): invalid request local work queue error

node-0:139572:139720 [1] transport/net_ib.cc:113 NCCL WARN communicator encountered a fatal error (detected in ncclIbIrecv)

node-0:139572:139720 [1] NCCL INFO transport/net_ib.cc:2117 -> 2
node-0:139572:139720 [1] NCCL INFO transport/net.cc:1335 -> 2
node-0:139572:139720 [1] NCCL INFO proxy.cc:728 -> 2
node-0:139572:139720 [1] NCCL INFO proxy.cc:912 -> 2 [Progress Thread]
```

I am not familar with that particular failure mechanism from RoCE. 
Perhaps you should move this issue over to the NCCL library itself as this repo is just for the nccl-tests
Also have you tried a newer NCCL version. The latest is NCCL 2.28.9


### AlexanderNekrasov · 2025-11-24

I use nccl version that is supported by pytorch version that I need, so I haven't tried other versions yet
