# [Issue #2190] [Issue]: NCCL WARN Error while attaching to shared memory segment

source: https://github.com/NVIDIA/nccl/issues/2190
state: open | updated: 2026-09-13T18:06:54Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs


Issue Description:
We are consistently encountering a specific NCCL initialization failure when launching vLLM (V1 Engine Core) with Tensor Parallelism = 8 on a single node equipped with 8x RTX 6000 Ada GPUs.
The failure happens during the ncclCommInitRank phase, specifically when late-joining ranks (typically Rank 4 and Rank 7) attempt to attach to the shared memory segments created in /dev/shm/. It throws a No such file or directory (size 0) warning, followed by an unhandled system error that crashes the distributed worker process pool.

Pre-checks & System Configurations Performed:
To rule out standard OS/container-level resource starvation, we have already verified and explicitly configured the following parameters
Shared Memory Limits (ulimit): Max locked memory (memlock) and virtual memory (as) have been set to unlimited on both host and inside the container.SHM Space Allocation: /dev/shm is fully provisioned with 252 GB of tmpfs space (via --ipc=host). 
Verified available space is >98% free during crash
Systemd IPC Cleanup: RemoveIPC=no has been explicitly configured and verified in /etc/systemd/logind.conf on the host to avoid systemd deleting active hooks.

Platform / OS: Linux (Ubuntu 22.04 / 24.04 via Docker Container)

GPU Topology: 8x NVIDIA RTX 6000 Ada (Hybrid topology: No NVLink, some rings connected via SHM/direct/direct, others via P2P/CUMEM through PCIe switches).

NCCL Version: 2.28.9 (Embedded inside vLLM)

Framework: vLLM V1 Engine (Python 3.12, utilizing standard multiproc_executor.py and custom pynccl wrapper).











LOG:
d4fde3314201:13736:13736 [3] NCCL INFO ProxyCall UDS comm 0x369ffdb0 rank 3 tpRank 2(2c7dfc1db2ea56b9) reqSize 8 respSize 0 respFd 0x7fff3d27a3a0 opId 0x6d421af0ba6e362e
d4fde3314201:13735:13936 [2] NCCL INFO proxyUDSRecvReq::ncclProxyMsgGetFd rank 3 opId 0x6d421af0ba6e362e handle=0x7fe2b800d420
d4fde3314201:13735:13936 [2] NCCL INFO UDS proxyGetFd received handle 0x7fe2b800d420 peer 3 opId 6d421af0ba6e362e
d4fde3314201:13739:13947 [6] NCCL INFO MMAP allocated shareable host buffer /dev/shm/nccl-Qdcygz size 4096 ptr 0x7f83a4c2f000
d4fde3314201:13739:13947 [6] NCCL INFO proxyProgressAsync opId=0x44f07f50 op.type=3 op.reqBuff=0x7f802800b220 op.respSize=112 done
d4fde3314201:13739:13739 [6] NCCL INFO ncclPollProxyResponse Received new opId=0x44f07f50
d4fde3314201:13739:13947 [6] NCCL INFO Received and initiated operation=Setup res=0
d4fde3314201:13739:13739 [6] NCCL INFO resp.opId=0x44f07f50 matches expected opId=0x44f07f50
d4fde3314201:13739:13739 [6] NCCL INFO Channel 00 : 6[6] -> 7[7] via SHM/direct/direct
d4fde3314201:13739:13947 [6] NCCL INFO New proxy send connection 3 from local rank 6, transport 1
d4fde3314201:13739:13947 [6] NCCL INFO proxyProgressAsync opId=0x44f07f50 op.type=1 op.reqBuff=0x7f802800c530 op.respSize=16 done
d4fde3314201:13739:13739 [6] NCCL INFO ncclPollProxyResponse Received new opId=0x44f07f50
d4fde3314201:13739:13947 [6] NCCL INFO Received and initiated operation=Init res=0
d4fde3314201:13739:13739 [6] NCCL INFO resp.opId=0x44f07f50 matches expected opId=0x44f07f50
d4fde3314201:13739:13739 [6] NCCL INFO Connected to proxy localRank 6 -> connection 0x7f80280050d8
d4fde3314201:13739:13947 [6] NCCL INFO Allocated 4100 bytes of shared memory in /dev/shm/nccl-ai1W3g
d4fde3314201:13736:13736 [3] NCCL INFO ProxyCall UDS comm 0x369ffdb0 rank 3 tpRank 2(2c7dfc1db2ea56b9) reqSize 8 respSize 0 respFd 147 opId 0x6d421af0ba6e362e - DONE
d4fde3314201:13736:13736 [3] NCCL INFO UDS: ClientGetFd handle 0x7fe2b800d420 tpRank 2 returned fd 147 sameProcess 0
d4fde3314201:13737:13737 [4] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-n8MtBp size 13832192 ptr 0x7fe7b1136000

[2026-05-22 10:26:17] d4fde3314201:13737:13737 [4] misc/shmutils.cc:93 NCCL WARN Call to open failed: No such file or directory

[2026-05-22 10:26:17] d4fde3314201:13737:13737 [4] misc/shmutils.cc:132 NCCL WARN Error while attaching to shared memory segment /dev/shm/nccl- ▒ (size 0), error: No such file or directory (2)
d4fde3314201:13737:13737 [4] NCCL INFO transport/shm.cc:634 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO transport/shm.cc:203 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO transport.cc:231 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO transport/generic.cc:25 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO group.cc:149 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO group.cc:209 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO group.cc:76 -> 2 [Async thread]
d4fde3314201:13737:13737 [4] NCCL INFO group.cc:587 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO group.cc:743 -> 2
d4fde3314201:13737:13737 [4] NCCL INFO enqueue.cc:2655 -> 2
d4fde3314201:13739:13947 [6] NCCL INFO MMAP allocated shareable host buffer /dev/shm/nccl-ai1W3g size 4096 ptr 0x7f836353f000
d4fde3314201:13739:13947 [6] NCCL INFO proxyProgressAsync opId=0x44f07f50 op.type=3 op.reqBuff=0x7f802800c550 op.respSize=112 done
d4fde3314201:13739:13739 [6] NCCL INFO ncclPollProxyResponse Received new opId=0x44f07f50
d4fde3314201:13739:13947 [6] NCCL INFO Received and initiated operation=Setup res=0
d4fde3314201:13739:13739 [6] NCCL INFO resp.opId=0x44f07f50 matches expected opId=0x44f07f50
d4fde3314201:13739:13739 [6] NCCL INFO Channel 01 : 6[6] -> 7[7] via SHM/direct/direct

[2026-05-22 10:26:17] d4fde3314201:13740:13740 [7] misc/shmutils.cc:93 NCCL WARN Call to open failed: No such file or directory

[2026-05-22 10:26:17] d4fde3314201:13740:13740 [7] misc/shmutils.cc:132 NCCL WARN Error while attaching to shared memory segment /dev/shm/nccl- (size 0), error: No such file or directory (2)
d4fde3314201:13740:13740 [7] NCCL INFO transport/shm.cc:634 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO transport/shm.cc:169 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO transport.cc:212 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO transport/generic.cc:25 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO group.cc:149 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO group.cc:209 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO group.cc:76 -> 2 [Async thread]
d4fde3314201:13740:13740 [7] NCCL INFO group.cc:587 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO group.cc:743 -> 2
d4fde3314201:13740:13740 [7] NCCL INFO enqueue.cc:2655 -> 2
d4fde3314201:13736:13736 [3] NCCL INFO CUMEM imported shareable host buffer from proxyRank 2 size 4096 ptr 0x7f6e33400000, granularity 2097152
d4fde3314201:13739:13739 [6] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-I9oUed size 13832192 ptr 0x7f802659c000
d4fde3314201:13738:13738 [5] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-7uoCFt size 13832192 ptr 0x7f91d659c000
d4fde3314201:13736:13736 [3] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-6L5T3m size 13832192 ptr 0x7f6df0f9b000
d4fde3314201:13736:13736 [3] NCCL INFO ProxyCall UDS comm 0x369ffdb0 rank 3 tpRank 2(2c7dfc1db2ea56b9) reqSize 8 respSize 0 respFd 0x7fff3d27a3a0 opId 0xb8d39ad4cfac38e8
d4fde3314201:13735:13936 [2] NCCL INFO proxyUDSRecvReq::ncclProxyMsgGetFd rank 3 opId 0xb8d39ad4cfac38e8 handle=0x7fe2b800f640
d4fde3314201:13735:13936 [2] NCCL INFO UDS proxyGetFd received handle 0x7fe2b800f640 peer 3 opId b8d39ad4cfac38e8
d4fde3314201:13739:13739 [6] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-aDc4PE size 4096 ptr 0x7f8323c3f000
d4fde3314201:13738:13738 [5] NCCL INFO MMAP imported shareable host buffer /dev/shm/nccl-c1yq9L size 4096 ptr 0x7f9533b2f000
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870] WorkerProc failed to start.
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870] Traceback (most recent call last):
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 837, in worker_main
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     worker = WorkerProc(*args, **kwargs)
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return func(*args, **kwargs)
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 611, in __init__
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.worker.init_device()
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/worker_base.py", line 317, in init_device
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.worker.init_device()  # type: ignore
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return func(*args, **kwargs)
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 263, in init_device
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     init_worker_distributed_environment(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 1057, in init_worker_distributed_environment
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     ensure_model_parallel_initialized(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1747, in ensure_model_parallel_initialized
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     initialize_model_parallel(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1578, in initialize_model_parallel
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     _TP = init_model_parallel_group(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]           ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1159, in init_model_parallel_group
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return GroupCoordinator(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 376, in __init__
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.device_communicator = device_comm_cls(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]                                ^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 75, in __init__
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.pynccl_comm = PyNcclCommunicator(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]                        ^^^^^^^^^^^^^^^^^^^
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl.py", line 142, in __init__
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.all_reduce(data)
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl.py", line 175, in all_reduce
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.nccl.ncclAllReduce(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl_wrapper.py", line 438, in ncclAllReduce
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.NCCL_CHECK(
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl_wrapper.py", line 382, in NCCL_CHECK
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870] WorkerProc failed to start.
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     raise RuntimeError(f"NCCL error: {error_str}")
(Worker pid=13740) ERROR 05-22 10:26:17 [multiproc_executor.py:870] RuntimeError: NCCL error: unhandled system error (run with NCCL_DEBUG=INFO for details)
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870] Traceback (most recent call last):
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 837, in worker_main
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     worker = WorkerProc(*args, **kwargs)
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return func(*args, **kwargs)
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 611, in __init__
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.worker.init_device()
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/worker_base.py", line 317, in init_device
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.worker.init_device()  # type: ignore
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return func(*args, **kwargs)
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 263, in init_device
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     init_worker_distributed_environment(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 1057, in init_worker_distributed_environment
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     ensure_model_parallel_initialized(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1747, in ensure_model_parallel_initialized
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     initialize_model_parallel(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1578, in initialize_model_parallel
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     _TP = init_model_parallel_group(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]           ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 1159, in init_model_parallel_group
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     return GroupCoordinator(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]            ^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 376, in __init__
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.device_communicator = device_comm_cls(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]                                ^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 75, in __init__
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.pynccl_comm = PyNcclCommunicator(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]                        ^^^^^^^^^^^^^^^^^^^
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl.py", line 142, in __init__
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.all_reduce(data)
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl.py", line 175, in all_reduce
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.nccl.ncclAllReduce(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl_wrapper.py", line 438, in ncclAllReduce
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     self.NCCL_CHECK(
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]   File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/device_communicators/pynccl_wrapper.py", line 382, in NCCL_CHECK
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870]     raise RuntimeError(f"NCCL error: {error_str}")
(Worker pid=13737) ERROR 05-22 10:26:17 [multiproc_executor.py:870] RuntimeError: NCCL error: unhandled system error (run with NCCL_DEBUG=INFO for details)


### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.28.9

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (7)

### stephenmsachs · 2026-05-29

@MoraruMaxim can you help triage this one?

### MoraruMaxim · 2026-06-01

> [@MoraruMaxim](https://github.com/MoraruMaxim) can you help triage this one?

Mirrored internally!

### MoraruMaxim · 2026-06-03

@liseng1997 

We need a bit more information to debug this. Could you please provide the complete per-process NCCL logs from one failing test by re-running the same vLLM command with only these logging variables added:

```
NCCL_DEBUG=INFO
NCCL_DEBUG_SUBSYS=INIT,GRAPH,SHM,PROXY,ENV
NCCL_DEBUG_FILE=<path_to>/nccl-vllm-%h-%p.log
```

Could you please also include:
- the exact vLLM launch command
- the `nvidia-smi` output from inside the container
- the `nvidia-smi topo -m` output
- the CUDA runtime/toolkit version from inside the container

### MoraruMaxim · 2026-07-08

@liseng1997 

We haven't heard back since our last comment. Please note that if we don't get a response in the next two weeks, we'll have to close this issue. Feel free to comment anytime if the issue is still happening!

### stephenmsachs · 2026-08-05

Closing due to inactivity. Please feel free to open another issue if this problem persists.

### XingZYu · 2026-09-03

Hi, we reproduced this failure and traced it to **asymmetric CUDA host-NUMA allocation support across ranks**.

### Why NCCL fails

Since **NCCL 2.26.3**, NCCL has tested cuMem host allocation independently in each process and fallen back to `/dev/shm` when the probe fails.

- **Probe divergence:** the probe succeeds on one rank but fails on another.
- **Path divergence:** the ranks select different host-memory paths.
- **Failure:** a fallback rank can decode its peer's cuMem descriptor as legacy SHM metadata, producing the malformed SHM pathname and **size 0** reported in this issue.

### Trigger

The underlying trigger is that **`cuMemCreate(HOST_NUMA)` succeeds for some GPU-affine NUMA nodes but fails for others**. Possible causes include:

- inconsistent online-CPU and NUMA cpumap views;
- sparse or filtered CPU IDs;
- valid memory NUMA nodes that contain no CPUs.

> **Key observation:** In the tested driver, NUMA eligibility followed CPU presence rather than memory metadata. A memory-bearing node with an empty CPU map was rejected, while removing the node's memory information alone did not clear its eligibility. Other topology or memory conditions may still cause the later allocation itself to fail.

### How we found it

**1. System-call trace**

A simplified version of the observed topology was:

```text
/sys/devices/system/cpu/online -> 0-11
Mems_allowed_list              -> 0-1
node0 CPUs                     -> 0-47,96-143
node1 CPUs                     -> 48-95,144-191
```

The process reported **12 online CPUs**, while both NUMA nodes remained visible and node 1 contained only CPU IDs starting from **48**.

**2. Driver inspection**

For NVIDIA driver **580.126.09**, we identified an unsymbolized initialization routine at offset `0x21063d0`, invoked through `pthread_once` during `cuInit`. Its disassembly showed that it:

```text
calls sysconf
enumerates /sys/devices/system/node
reads nodeN/cpumap
builds a CPU-to-node table and a NUMA-node bitmap
```

Changing only the processor count returned by `sysconf` also changed the internal NUMA-related state observed with GDB. This served as a cross-check rather than standalone proof.

**3. Behavioral validation**

With the NUMA cpumaps unchanged, the result changed exactly at node 1's lowest CPU ID:

```text
reported CPUs = 48 -> cuMemCreate(HOST_NUMA, node=1) fails
reported CPUs = 49 -> cuMemCreate(HOST_NUMA, node=1) succeeds
```

Consequently, `cuMemCreate(HOST_NUMA)` succeeded for GPUs associated with node 0 but failed with **`CUDA_ERROR_INVALID_VALUE`** for GPUs associated with node 1.

**Workaround:** Restoring a consistent CPU/NUMA topology view avoided the failure.

**Diagnostic:** `NCCL_CUMEM_HOST_ENABLE=0` can be used to force all ranks onto the same fallback path.


### MoraruMaxim · 2026-09-13

@liseng1997, could you please rerun the same vLLM command with `NCCL_CUMEM_HOST_ENABLE=0` and confirm whether this resolves the issue?
