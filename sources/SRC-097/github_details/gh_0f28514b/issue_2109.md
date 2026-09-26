# [Issue #2109] NIXL_ERR_REMOTE_DISCONNECT race between UCX endpoint close and reconnect when remove_remote_agent/add_remote_agent are called back-to-back

source: https://github.com/ai-dynamo/nixl/issues/2109
state: closed | updated: 2026-08-24T07:46:50Z
labels: Network

## 正文

remove_remote_agent() immediately followed by add_remote_agent() for the same peer intermittently fails with NIXL_ERR_REMOTE_DISCONNECT / UCS_ERR_CONNECTION_RESET.
 
This happens in Ray's RDT nixl_tensor_transport.py: when a remote agent's cached metadata version is stale (because the sender deregistered memory), the receiver evicts and re-adds that agent to pick up the new metadata — with no delay between the two calls.
 
**Root cause**
nixlUcxEp::closeImpl() (src/plugins/ucx/ucx_utils.cpp) closes the UCX endpoint fire-and-forget: 
it calls ucp_ep_close_nbx() and immediately ucp_request_free()s the request without waiting for completion. 
If add_remote_agent() creates a new endpoint to the same peer before the old endpoint's close has actually completed on the wire, the peer can still be processing the old close when the new connection attempt arrives, causing UCS_ERR_CONNECTION_RESET.
 
**Proposed fix**
 [PR 2101](https://github.com/ai-dynamo/nixl/pull/2101)
 - closes the endpoint synchronously in disconnect() 
    busy-waits via ucp_worker_progress() + ucp_request_check_status() until the close actually completes.
 
 
**Repro script:** 

[cpu_scatter_disconnect_race.py](https://github.com/user-attachments/files/31167069/cpu_scatter_disconnect_race.py)

python cpu_scatter_disconnect_race.py -N 16 --shape 3,2048,64000,128 --warmup 2 --iters 3
 
**Debug log:** 

[nixl_1.4.0_debug_log.txt](https://github.com/user-attachments/files/31167099/nixl_1.4.0_debug_log.txt) crash traceback at lines 9031-9105.
 
**Environment**
- NIXL v1.4.0 @ c0a1102b
- Ray 3.0.0.dev0, TransferQueue (RDT) 0.1.7.dev0
- PyTorch 2.10.0+cu129, CUDA 12.9, Python 3.13.12
- 2×8 NVIDIA H100 80GB HBM3 (driver 535.216.03)

## 评论 (1)

### linear-code[bot] · 2026-08-24

from mikhailb:
> Should be fixed in the app according to analysis
