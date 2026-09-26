# [Issue #1454] [Issue]: RCCL is compleatly broken in most configurations

source: https://github.com/ROCm/rccl/issues/1454
state: closed | updated: 2026-01-22T01:59:09Z
labels: Under Investigation

## 正文

### Problem Description

System:
GPUS: 3x MI100 GFX908
AMD EPYC 7452
OS: Ubuntu 24.04 and Archlinux (same behavior)
Kernel: 6.12.3
Rocm: 6.2.4
rccl: 2.20.5

# Tests: 

| Test      |  Command      | Url
| ------------- | ------------- | --- |
| Test 1 | `./build/all_reduce_perf -b 2 -e 128M -f 2 -g 2` | https://github.com/ROCm/rccl-tests
| Test 2 | `torchrun --nnode=1 --node_rank=0 --nproc_per_node=2 multigpu_torchrun.py --batch_size 8 100 10` |  https://github.com/pytorch/examples

# Test Configurations:

| Test      |  IOMMU  | CONFIG_HSA_AMD_P2P |  CONFIG_DMABUF_MOVE_NOTIFY | Broken?
| ------- | ---------- | ------------------------- | ------------------------------------ | --------
| Test 1 | Disabled | n | n | No
| Test 1 | Enabled  | n | n | No
| Test 1 | Disabled | y | y | Yes (Note 1)
| Test 1 | Enabled  | y | y | Yes (Note 1)
| Test 1 | Pass-Though | y | y | Yes (Note 1)
| Test 2 | Disabled | n | n | Partially (Note 2)
| Test 2 | Enabled  | n | n | Partially (Note 2)
| Test 2 | Disabled | y | y | Yes (Note 3)
| Test 2 | Enabled  | y | y | Yes (Note 3)
| Test 2 | Pass-Though | y | y | Yes (Note 3)


### Note 1:
<details>
<summary>
Console output:
</summary>
`
# nThread 1 nGpus 2 minBytes 2 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:ae3e635
# Using devices
#   Rank  0 Pid  31965 on  UVOSLinux device  0 [0000:c3:00.0] AMD Radeon RX 6800 XT
#   Rank  1 Pid  31965 on  UVOSLinux device  1 [0000:83:00.0] AMD Instinct MI100
UVOSLinux:31965:31965 [0] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:31965:31965 [0] NCCL INFO NET/Plugin : dlerror=librccl-net.so: cannot open shared object file: No such file or directory No plugin found (librccl-net.so), using internal implementation
UVOSLinux:31965:31965 [0] NCCL INFO Kernel version: 6.12.3-arch1-1
UVOSLinux:31965:31965 [1] NCCL INFO ROCr version 1.1
UVOSLinux:31965:31965 [1] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
RCCL version 2.20.5+hip6.2 Unknown 
UVOSLinux:31965:31971 [0] NCCL INFO Failed to open libibverbs.so[.1]
UVOSLinux:31965:31971 [0] NCCL INFO NET/Socket : Using [0]bond0:10.0.0.2<0> [1]uvosvpn:10.8.0.3<0>
UVOSLinux:31965:31971 [0] NCCL INFO Using non-device net plugin version 0
UVOSLinux:31965:31971 [0] NCCL INFO Using network Socket
UVOSLinux:31965:31972 [1] NCCL INFO Using non-device net plugin version 0
UVOSLinux:31965:31972 [1] NCCL INFO Using network Socket
UVOSLinux:31965:31972 [1] NCCL INFO comm 0x5fa38772fe50 rank 1 nranks 2 cudaDev 1 busId 83000 commId 0xb8d3e001a8f1faf - Init START
UVOSLinux:31965:31971 [0] NCCL INFO comm 0x5fa38764e0a0 rank 0 nranks 2 cudaDev 0 busId c3000 commId 0xb8d3e001a8f1faf - Init START
UVOSLinux:31965:31972 [1] NCCL INFO [node_id = 3; gpu_id = 4106; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0], 
UVOSLinux:31965:31972 [1] NCCL INFO [node_id = 2; gpu_id = 45163; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0], 
UVOSLinux:31965:31972 [1] NCCL INFO [node_id = 1; gpu_id = 4755; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0], 
UVOSLinux:31965:31972 [1] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:31965:31972 [1] NCCL INFO Setting affinity for GPU 1 to ffff,ffffffff
UVOSLinux:31965:31971 [0] NCCL INFO [node_id = 3; gpu_id = 4106; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0], 
UVOSLinux:31965:31971 [0] NCCL INFO [node_id = 2; gpu_id = 45163; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0], 
UVOSLinux:31965:31971 [0] NCCL INFO [node_id = 1; gpu_id = 4755; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0], 
UVOSLinux:31965:31971 [0] NCCL INFO Setting affinity for GPU 2 to ffff,ffffffff
UVOSLinux:31965:31972 [1] NCCL INFO comm 0x5fa38772fe50 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
UVOSLinux:31965:31971 [0] NCCL INFO comm 0x5fa38764e0a0 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
UVOSLinux:31965:31972 [1] NCCL INFO Trees [0] 0/-1/-1->1->-1 [1] 0/-1/-1->1->-1 comm 0x5fa38772fe50 nRanks 02 busId 83000
UVOSLinux:31965:31972 [1] NCCL INFO P2P Chunksize set to 131072
UVOSLinux:31965:31971 [0] NCCL INFO Channel 00/02 :    0   1
UVOSLinux:31965:31971 [0] NCCL INFO Channel 01/02 :    0   1
UVOSLinux:31965:31971 [0] NCCL INFO Trees [0] -1/-1/-1->0->1 [1] -1/-1/-1->0->1 comm 0x5fa38764e0a0 nRanks 02 busId c3000
UVOSLinux:31965:31971 [0] NCCL INFO P2P Chunksize set to 131072

UVOSLinux:31965:31973 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:235 NCCL WARN hipIpcGetMemHandle failed : invalid argument

UVOSLinux:31965:31973 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:237 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:31965:31973 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:646 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:473 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1585 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1902 -> 1
UVOSLinux:31965:31972 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/misc/socket.cc:49 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/misc/socket.cc:752 -> 3

UVOSLinux:31965:31971 [0] /usr/src/debug/rccl/build/hipify/src/proxy.cc:1190 NCCL WARN Socket recv failed while polling for opId=0x7d9e780c40c0
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:473 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1585 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1902 -> 3
UVOSLinux:31965:31971 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:68 -> 3 [Async thread]
UVOSLinux:31965:31965 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:437 -> 1
UVOSLinux:31965:31965 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:107 -> 1
UVOSLinux:31965:31965 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2241 -> 1
UVOSLinux: Test NCCL failure /home/philipp/Programming/rccl-tests/build/hipify/common.cu.cpp:1291 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. UVOSLinux pid 31965: Test failure /home/philipp/Programming/rccl-tests/build/hipify/common.cu.cpp:1165

UVOSLinux:31965:31975 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:235 NCCL WARN hipIpcGetMemHandle failed : invalid argument

UVOSLinux:31965:31975 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:237 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:646 -> 1
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/misc/socket.cc:49 -> 3
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/misc/socket.cc:60 -> 3
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/misc/socket.cc:775 -> 3
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/proxy.cc:1390 -> 3
UVOSLinux:31965:31975 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/proxy.cc:1431 -> 3

UVOSLinux:31965:31975 [0] /usr/src/debug/rccl/build/hipify/src/proxy.cc:1573 NCCL WARN [Proxy Service 0] Failed to execute operation Setup from rank 0, retcode 3
`
</details>


### Note 2:

Only broken sometimes (about 1/10 of tries)
fails with:
<details>
  <summary>
    Console output:
  </summary>
  NCCL error: unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5
ncclSystemError: System call (e.g. socket, malloc) or external library call failed or device error. 
Last error:
Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
Exception raised from checkForNCCLErrorsInternal at /home/philipp/python-pytorch/src/pytorch-opt-rocm/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:2027 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xa7 (0x70e71e1918b7 in /usr/lib/libc10.so)
frame #1: <unknown function> + 0x2083762 (0x70e71ba83762 in /usr/lib/libtorch_hip.so)
frame #2: c10d::ProcessGroupNCCL::checkForNCCLErrorsInternal(std::shared_ptr<c10d::NCCLComm>&) + 0x27a (0x70e71baa222a in /usr/lib/libtorch_hip.so)
frame #3: c10d::ProcessGroupNCCL::WorkNCCL::checkAndSetException() + 0xa7 (0x70e71baa2427 in /usr/lib/libtorch_hip.so)
frame #4: c10d::ProcessGroupNCCL::WorkNCCL::isCompleted() + 0x98 (0x70e71baa26a8 in /usr/lib/libtorch_hip.so)
frame #5: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f9 (0x70e71baa3189 in /usr/lib/libtorch_hip.so)
frame #6: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x118 (0x70e71baa4b08 in /usr/lib/libtorch_hip.so)
frame #7: <unknown function> + 0xe1c34 (0x70e6c02e1c34 in /usr/lib/libstdc++.so.6)
frame #8: <unknown function> + 0x9439d (0x70e735ca339d in /usr/lib/libc.so.6)
frame #9: <unknown function> + 0x11949c (0x70e735d2849c in /usr/lib/libc.so.6)
UVOSLinux:916050:916334 [1] NCCL INFO comm 0x5d96f02dc720 rank 1 nranks 2 cudaDev 1 busId 3000 - Abort COMPLETE
I20241209 23:20:43.484511 140354185590464 ProcessGroupNCCL.cpp:1197] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL destroyed  communicator on CUDA device: 1
I20241209 23:20:43.484621 140373116939136 ProcessGroupNCCL.cpp:1116] [PG ID 0 PG GUID 0(default_pg) Rank 1] future is successfully executed for: ProcessGroup abort
I20241209 23:20:43.484655 140373116939136 ProcessGroupNCCL.cpp:1237] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL aborts successfully.
</details>

### Note 3:

Same issue as https://github.com/ROCm/rccl/issues/1421
Fails with:
<details>
  <summary>
    Console output:
  </summary>
  W1209 23:39:39.912000 19400 site-packages/torch/distributed/run.py:793]
W1209 23:39:39.912000 19400 site-packages/torch/distributed/run.py:793] *****************************************
W1209 23:39:39.912000 19400 site-packages/torch/distributed/run.py:793] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed.
W1209 23:39:39.912000 19400 site-packages/torch/distributed/run.py:793] *****************************************
WARNING: Logging before InitGoogleLogging() is written to STDERR
I20241209 23:39:42.495619 138559122262912 ProcessGroupNCCL.cpp:905] [PG ID 0 PG GUID 0 Rank 1] ProcessGroupNCCL initialization options: size: 2, global rank: 1, TIMEOUT(ms): 600000, USE_HIGH_PRIORITY_STREAM: 0, SPLIT_FROM: 0, SPLIT_COLOR: 0, PG Name: 0
I20241209 23:39:42.495654 138559122262912 ProcessGroupNCCL.cpp:914] [PG ID 0 PG GUID 0 Rank 1] ProcessGroupNCCL environments: NCCL version: 2.20.5, TORCH_NCCL_ASYNC_ERROR_HANDLING: 1, TORCH_NCCL_DUMP_ON_TIMEOUT: 0, TORCH_NCCL_WAIT_TIMEOUT_DUMP_MILSEC: 60000, TORCH_NCCL_DESYNC_DEBUG: 0, TORCH_NCCL_ENABLE_TIMING: 0, TORCH_NCCL_BLOCKING_WAIT: 0, TORCH_DISTRIBUTED_DEBUG: OFF, TORCH_NCCL_USE_TENSOR_REGISTER_ALLOCATOR_HOOK: 0, TORCH_NCCL_ENABLE_MONITORING: 1, TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC: 480, TORCH_NCCL_TRACE_BUFFER_SIZE: 0, TORCH_NCCL_COORD_CHECK_MILSEC: 1000, TORCH_NCCL_NAN_CHECK: 0, TORCH_NCCL_CUDA_EVENT_CACHE: 0, TORCH_NCCL_LOG_CPP_STACK_ON_UNCLEAN_SHUTDOWN: 1
WARNING: Logging before InitGoogleLogging() is written to STDERR
I20241209 23:39:42.528390 129938276596608 ProcessGroupNCCL.cpp:905] [PG ID 0 PG GUID 0 Rank 0] ProcessGroupNCCL initialization options: size: 2, global rank: 0, TIMEOUT(ms): 600000, USE_HIGH_PRIORITY_STREAM: 0, SPLIT_FROM: 0, SPLIT_COLOR: 0, PG Name: 0
I20241209 23:39:42.528424 129938276596608 ProcessGroupNCCL.cpp:914] [PG ID 0 PG GUID 0 Rank 0] ProcessGroupNCCL environments: NCCL version: 2.20.5, TORCH_NCCL_ASYNC_ERROR_HANDLING: 1, TORCH_NCCL_DUMP_ON_TIMEOUT: 0, TORCH_NCCL_WAIT_TIMEOUT_DUMP_MILSEC: 60000, TORCH_NCCL_DESYNC_DEBUG: 0, TORCH_NCCL_ENABLE_TIMING: 0, TORCH_NCCL_BLOCKING_WAIT: 0, TORCH_DISTRIBUTED_DEBUG: OFF, TORCH_NCCL_USE_TENSOR_REGISTER_ALLOCATOR_HOOK: 0, TORCH_NCCL_ENABLE_MONITORING: 1, TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC: 480, TORCH_NCCL_TRACE_BUFFER_SIZE: 0, TORCH_NCCL_COORD_CHECK_MILSEC: 1000, TORCH_NCCL_NAN_CHECK: 0, TORCH_NCCL_CUDA_EVENT_CACHE: 0, TORCH_NCCL_LOG_CPP_STACK_ON_UNCLEAN_SHUTDOWN: 1
Loading snapshot
/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py:41: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  snapshot = torch.load(snapshot_path, map_location=loc)
Resuming training from snapshot at Epoch 90
Loading snapshot
/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py:41: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  snapshot = torch.load(snapshot_path, map_location=loc)
Resuming training from snapshot at Epoch 90
UVOSLinux:19402:19402 [0] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:19402:19402 [0] NCCL INFO NET/Plugin : dlerror=librccl-net.so: cannot open shared object file: No such file or directory No plugin found (librccl-net.so), using internal implementation
UVOSLinux:19402:19402 [0] NCCL INFO Kernel version: 6.12.3-arch1-1

UVOSLinux:19402:19402 [0] /usr/src/debug/rccl/build/hipify/src/init.cc:136 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
I20241209 23:39:43.535403 129938276596608 ProcessGroupNCCL.cpp:2262] [PG ID 0 PG GUID 0(default_pg) Rank 0] ProcessGroupNCCL broadcast unique ID through store took 0.060293 ms
UVOSLinux:19402:19402 [0] NCCL INFO ROCr version 1.1
UVOSLinux:19402:19402 [0] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
RCCL version 2.20.5+hip6.2 Unknown
I20241209 23:39:43.535686 138559122262912 ProcessGroupNCCL.cpp:2262] [PG ID 0 PG GUID 0(default_pg) Rank 1] ProcessGroupNCCL broadcast unique ID through store took 17.5191 ms
UVOSLinux:19403:19403 [1] NCCL INFO ROCr version 1.1
UVOSLinux:19403:19403 [1] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
UVOSLinux:19403:19403 [1] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:19403:19403 [1] NCCL INFO NET/Plugin : dlerror=librccl-net.so: cannot open shared object file: No such file or directory No plugin found (librccl-net.so), using internal implementation
UVOSLinux:19403:19403 [1] NCCL INFO Kernel version: 6.12.3-arch1-1

UVOSLinux:19403:19403 [1] /usr/src/debug/rccl/build/hipify/src/init.cc:136 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
UVOSLinux:19402:19415 [0] NCCL INFO Failed to open libibverbs.so[.1]
UVOSLinux:19403:19416 [1] NCCL INFO Failed to open libibverbs.so[.1]
UVOSLinux:19402:19415 [0] NCCL INFO NET/Socket : Using [0]bond0:10.0.0.2<0> [1]uvosvpn:10.8.0.3<0>
UVOSLinux:19403:19416 [1] NCCL INFO NET/Socket : Using [0]bond0:10.0.0.2<0> [1]uvosvpn:10.8.0.3<0>
UVOSLinux:19402:19415 [0] NCCL INFO Using non-device net plugin version 0
UVOSLinux:19402:19415 [0] NCCL INFO Using network Socket
UVOSLinux:19403:19416 [1] NCCL INFO Using non-device net plugin version 0
UVOSLinux:19403:19416 [1] NCCL INFO Using network Socket
UVOSLinux:19403:19416 [1] NCCL INFO comm 0x62a02f5bcbb0 rank 1 nranks 2 cudaDev 1 busId 83000 commId 0xa6a3e04444abaedd - Init START
UVOSLinux:19402:19415 [0] NCCL INFO comm 0x55ef05816e60 rank 0 nranks 2 cudaDev 0 busId c3000 commId 0xa6a3e04444abaedd - Init START
UVOSLinux:19403:19416 [1] NCCL INFO [node_id = 3; gpu_id = 4106; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0],
UVOSLinux:19403:19416 [1] NCCL INFO [node_id = 2; gpu_id = 45163; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0],
UVOSLinux:19403:19416 [1] NCCL INFO [node_id = 1; gpu_id = 4755; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0],
UVOSLinux:19402:19415 [0] NCCL INFO [node_id = 3; gpu_id = 4106; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0],
UVOSLinux:19402:19415 [0] NCCL INFO [node_id = 2; gpu_id = 45163; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0],
UVOSLinux:19402:19415 [0] NCCL INFO [node_id = 1; gpu_id = 4755; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0],
UVOSLinux:19403:19416 [1] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:19402:19415 [0] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:19403:19416 [1] NCCL INFO Setting affinity for GPU 1 to ffff,ffffffff
UVOSLinux:19402:19415 [0] NCCL INFO Setting affinity for GPU 2 to ffff,ffffffff
UVOSLinux:19403:19416 [1] NCCL INFO comm 0x62a02f5bcbb0 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
UVOSLinux:19402:19415 [0] NCCL INFO comm 0x55ef05816e60 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
UVOSLinux:19403:19416 [1] NCCL INFO Trees [0] 0/-1/-1->1->-1 [1] 0/-1/-1->1->-1 comm 0x62a02f5bcbb0 nRanks 02 busId 83000
UVOSLinux:19403:19416 [1] NCCL INFO P2P Chunksize set to 131072
UVOSLinux:19402:19415 [0] NCCL INFO Channel 00/02 :    0   1
UVOSLinux:19402:19415 [0] NCCL INFO Channel 01/02 :    0   1
UVOSLinux:19402:19415 [0] NCCL INFO Trees [0] -1/-1/-1->0->1 [1] -1/-1/-1->0->1 comm 0x55ef05816e60 nRanks 02 busId c3000
UVOSLinux:19402:19415 [0] NCCL INFO P2P Chunksize set to 131072

UVOSLinux:19403:19417 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:235 NCCL WARN hipIpcGetMemHandle failed : invalid argument

UVOSLinux:19403:19417 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:237 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:19403:19417 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:646 -> 1
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:473 -> 1
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 1
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 1

UVOSLinux:19402:19419 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:235 NCCL WARN hipIpcGetMemHandle failed : invalid argument
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1585 -> 1
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1902 -> 1
UVOSLinux:19403:19416 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]

UVOSLinux:19402:19419 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:237 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:19402:19419 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:646 -> 1
UVOSLinux:19403:19403 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:437 -> 1
UVOSLinux:19403:19403 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2278 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:473 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1585 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1902 -> 1
UVOSLinux:19402:19415 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
UVOSLinux:19402:19402 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:437 -> 1
UVOSLinux:19402:19402 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2278 -> 1
[rank0]: Traceback (most recent call last):
[rank0]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 111, in <module>
[rank0]:     main(args.save_every, args.total_epochs, args.batch_size)
[rank0]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 98, in main
[rank0]:     trainer = Trainer(model, train_data, optimizer, save_every, snapshot_path)
[rank0]:               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 37, in __init__
[rank0]:     self.model = DDP(self.model, device_ids=[self.gpu_id])
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/lib/python3.12/site-packages/torch/nn/parallel/distributed.py", line 825, in __init__
[rank0]:     _verify_param_shape_across_processes(self.process_group, parameters)
[rank0]:   File "/usr/lib/python3.12/site-packages/torch/distributed/utils.py", line 288, in _verify_param_shape_across_processes
[rank0]:     return dist._verify_params_across_processes(process_group, tensors, logger)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]: torch.distributed.DistBackendError: NCCL error in: /home/philipp/python-pytorch/src/pytorch-opt-rocm/torch/csrc/distributed/c10d/NCCLUtils.hpp:317, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5
[rank0]: ncclUnhandledCudaError: Call to CUDA function failed.
[rank0]: Last error:
[rank0]: Cuda failure 'invalid argument'
[rank1]: Traceback (most recent call last):
[rank1]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 111, in <module>
[rank1]:     main(args.save_every, args.total_epochs, args.batch_size)
[rank1]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 98, in main
[rank1]:     trainer = Trainer(model, train_data, optimizer, save_every, snapshot_path)
[rank1]:               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/home/philipp/machine-lerning/repos/examples/distributed/ddp-tutorial-series/multigpu_torchrun.py", line 37, in __init__
[rank1]:     self.model = DDP(self.model, device_ids=[self.gpu_id])
[rank1]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/lib/python3.12/site-packages/torch/nn/parallel/distributed.py", line 825, in __init__
[rank1]:     _verify_param_shape_across_processes(self.process_group, parameters)
[rank1]:   File "/usr/lib/python3.12/site-packages/torch/distributed/utils.py", line 288, in _verify_param_shape_across_processes
[rank1]:     return dist._verify_params_across_processes(process_group, tensors, logger)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]: torch.distributed.DistBackendError: NCCL error in: /home/philipp/python-pytorch/src/pytorch-opt-rocm/torch/csrc/distributed/c10d/NCCLUtils.hpp:317, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5
[rank1]: ncclUnhandledCudaError: Call to CUDA function failed.
[rank1]: Last error:
[rank1]: Cuda failure 'invalid argument'
E1209 23:39:44.740000 19400 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 0 (pid: 19402) of binary: /bin/python
Traceback (most recent call last):
  File "/bin/torchrun", line 33, in <module>
    sys.exit(load_entry_point('torch==2.5.1', 'console_scripts', 'torchrun')())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 355, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/torch/distributed/run.py", line 919, in main
    run(args)
  File "/usr/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/usr/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
============================================================
multigpu_torchrun.py FAILED
</details>

### Operating System

Ubuntu 24.04 and Archlinux (same behavior)

### CPU

EPYC 7452

### GPU

MI100

### ROCm Version

ROCm 6.2.4

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (14)

### nileshnegi · 2024-12-10

Please note the [OS compatibility matrix](https://rocm.docs.amd.com/en/docs-6.2.4/compatibility/compatibility-matrix.html#operating-systems-and-kernel-versions) for ROCm 6.2.4.
AMD does not officially support linux kernel 6.12.3 at the moment. For Ubuntu 24.04, ROCm 6.2.4 supports 6.8 GA.




### IMbackK · 2024-12-10

I have to use a mainline supported kernel for unrelated reasons, so 6.8 is off the table, however i tried 6.6.64, since the matrix lists 6.5 and 6.8 i belive this should be a safe choice, none the less there is no change in behavior, all configurations listed in the first post remainn broken.
I also tried RCCL 2.21.5 with no change in behavior

I also tried NCCL_DMABUF_ENABLE=1 with iommu in enabled state which is also broken in a yet another different way:
```
#   Rank  0 Pid   2386 on  UVOSLinux device  0 [0000:83:00.0] AMD Instinct MI100
#   Rank  1 Pid   2386 on  UVOSLinux device  1 [0000:03:00.0] AMD Instinct MI100
UVOSLinux:2386:2386 [0] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:2386:2386 [0] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
UVOSLinux:2386:2386 [0] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
UVOSLinux:2386:2386 [0] NCCL INFO NET/Plugin: Using internal network plugin.
UVOSLinux:2386:2386 [0] NCCL INFO Kernel version: 6.6.64-1

UVOSLinux:2386:2386 [0] /usr/src/debug/rccl/build/hipify/src/init.cc:163 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
UVOSLinux:2386:2386 [1] NCCL INFO ROCr version 1.1
UVOSLinux:2386:2386 [1] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
UVOSLinux:2386:2386 [1] NCCL INFO Could not open kernel conf file
[1]    2386 segmentation fault (core dumped)  NCCL_DEBUG=INFO ./build/all_reduce_perf -b 2 -e 128M -f 2 -g 2
```

The same allso occures whe the iommu is in pt state:
```
UVOSLinux:2508:2508 [0] /usr/src/debug/rccl/build/hipify/src/misc/api_trace.cc:283 NCCL WARN [rocprofiler-sdk-rccl][2508] rocprofiler-register failed with error code 4 : Library's API is not supported
# nThread 1 nGpus 2 minBytes 2 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:ae3e635
# Using devices
#   Rank  0 Pid   2508 on  UVOSLinux device  0 [0000:83:00.0] AMD Instinct MI100
#   Rank  1 Pid   2508 on  UVOSLinux device  1 [0000:03:00.0] AMD Instinct MI100
UVOSLinux:2508:2508 [0] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:2508:2508 [0] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
UVOSLinux:2508:2508 [0] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
UVOSLinux:2508:2508 [0] NCCL INFO NET/Plugin: Using internal network plugin.
UVOSLinux:2508:2508 [0] NCCL INFO Kernel version: 6.6.64-1
UVOSLinux:2508:2508 [1] NCCL INFO ROCr version 1.1
UVOSLinux:2508:2508 [1] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
UVOSLinux:2508:2508 [1] NCCL INFO Could not open kernel conf file
[1]    2508 segmentation fault (core dumped)  NCCL_DEBUG=INFO ./build/all_reduce_perf -b 2 -e 128M -f 2 -g 2
```

without NCCL_DMABUF_ENABLE=1 rccl remains broken on 6.6 also with the iommu in pt state:
```
UVOSLinux:2421:2421 [0] /usr/src/debug/rccl/build/hipify/src/misc/api_trace.cc:283 NCCL WARN [rocprofiler-sdk-rccl][2421] rocprofiler-register failed with error code 4 : Library's API is not supported
# nThread 1 nGpus 2 minBytes 2 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:ae3e635
# Using devices
#   Rank  0 Pid   2421 on  UVOSLinux device  0 [0000:83:00.0] AMD Instinct MI100
#   Rank  1 Pid   2421 on  UVOSLinux device  1 [0000:03:00.0] AMD Instinct MI100
UVOSLinux:2421:2421 [0] NCCL INFO Bootstrap : Using bond0:10.0.0.2<0>
UVOSLinux:2421:2421 [0] NCCL INFO NET/Plugin: No plugin found (librccl-net.so)
UVOSLinux:2421:2421 [0] NCCL INFO NET/Plugin: Plugin load returned 2 : librccl-net.so: cannot open shared object file: No such file or directory : when loading librccl-net.so
UVOSLinux:2421:2421 [0] NCCL INFO NET/Plugin: Using internal network plugin.
UVOSLinux:2421:2421 [0] NCCL INFO Kernel version: 6.6.64-1
UVOSLinux:2421:2421 [1] NCCL INFO ROCr version 1.1
UVOSLinux:2421:2421 [1] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
RCCL version : 2.21.5-main:a29a210+
HIP version  : 6.2.41134-
ROCm version : 6.2.4.0-139
Hostname     : UVOSLinux
Librccl path : /opt/rocm/lib/librccl.so.1
UVOSLinux:2421:2428 [0] NCCL INFO Failed to open libibverbs.so[.1]
UVOSLinux:2421:2428 [0] NCCL INFO NET/Socket : Using [0]bond0:10.0.0.2<0> [1]uvosvpn:10.8.0.3<0>
UVOSLinux:2421:2428 [0] NCCL INFO Using non-device net plugin version 0
UVOSLinux:2421:2428 [0] NCCL INFO Using network Socket
UVOSLinux:2421:2428 [0] NCCL INFO [node_id = 3; gpu_id = 56831; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0], 
UVOSLinux:2421:2428 [0] NCCL INFO [node_id = 2; gpu_id = 61754; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0], 
UVOSLinux:2421:2428 [0] NCCL INFO [node_id = 1; gpu_id = 25600; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0], 
UVOSLinux:2421:2428 [0] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2429 [1] NCCL INFO Using non-device net plugin version 0
UVOSLinux:2421:2429 [1] NCCL INFO Using network Socket
UVOSLinux:2421:2429 [1] NCCL INFO [node_id = 3; gpu_id = 56831; unique_id = 13656021927992722742; location_id = 768; bdf = 768; domain = 0; partition = 0], 
UVOSLinux:2421:2429 [1] NCCL INFO [node_id = 2; gpu_id = 61754; unique_id = 17978643005310382498; location_id = 33536; bdf = 33536; domain = 0; partition = 0], 
UVOSLinux:2421:2429 [1] NCCL INFO [node_id = 1; gpu_id = 25600; unique_id = 18248875242260470704; location_id = 49920; bdf = 49920; domain = 0; partition = 0], 
UVOSLinux:2421:2429 [1] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2429 [1] NCCL INFO ncclCommInitRank comm 0x55fcdca73ed0 rank 1 nranks 2 cudaDev 1 nvmlDev 0 busId 3000 commId 0x52df99801c58eaa6 - Init START
UVOSLinux:2421:2428 [0] NCCL INFO ncclCommInitRank comm 0x55fcdca84240 rank 0 nranks 2 cudaDev 0 nvmlDev 1 busId 83000 commId 0x52df99801c58eaa6 - Init START
UVOSLinux:2421:2428 [0] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2428 [0] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2429 [1] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2429 [1] NCCL INFO initialized internal alternative rsmi functionality
UVOSLinux:2421:2428 [0] NCCL INFO Setting affinity for GPU 1 to ffff,ffffffff
UVOSLinux:2421:2429 [1] NCCL INFO Setting affinity for GPU 0 to ffff,ffffffff
UVOSLinux:2421:2428 [0] NCCL INFO comm 0x55fcdca84240 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
UVOSLinux:2421:2429 [1] NCCL INFO comm 0x55fcdca73ed0 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
UVOSLinux:2421:2428 [0] NCCL INFO Channel 00/04 :    0   1
UVOSLinux:2421:2428 [0] NCCL INFO Channel 01/04 :    0   1
UVOSLinux:2421:2428 [0] NCCL INFO Channel 02/04 :    0   1
UVOSLinux:2421:2428 [0] NCCL INFO Channel 03/04 :    0   1
UVOSLinux:2421:2429 [1] NCCL INFO Trees [0] 0/-1/-1->1->-1 [1] 0/-1/-1->1->-1 [2] 0/-1/-1->1->-1 [3] 0/-1/-1->1->-1 comm 0x55fcdca73ed0 nRanks 02 busId 3000
UVOSLinux:2421:2428 [0] NCCL INFO Trees [0] -1/-1/-1->0->1 [1] -1/-1/-1->0->1 [2] -1/-1/-1->0->1 [3] -1/-1/-1->0->1 comm 0x55fcdca84240 nRanks 02 busId 83000
UVOSLinux:2421:2428 [0] NCCL INFO P2P Chunksize set to 131072
UVOSLinux:2421:2429 [1] NCCL INFO P2P Chunksize set to 131072

UVOSLinux:2421:2430 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:238 NCCL WARN hipIpcGetMemHandle failed : invalid argument

UVOSLinux:2421:2431 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:238 NCCL WARN hipIpcGetMemHandle failed : invalid argument

UVOSLinux:2421:2430 [0] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:240 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:2421:2430 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:651 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:476 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 1

UVOSLinux:2421:2431 [1] /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:240 NCCL WARN Cuda failure 'invalid argument'
UVOSLinux:2421:2431 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:651 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1691 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2017 -> 1
UVOSLinux:2421:2428 [0] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:69 -> 1 [Async thread]
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport/p2p.cc:476 -> 1
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:45 -> 1
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/transport.cc:147 -> 1
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:1691 -> 1
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2017 -> 1
UVOSLinux:2421:2429 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:69 -> 1 [Async thread]
UVOSLinux:2421:2421 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:438 -> 1
UVOSLinux:2421:2421 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/group.cc:108 -> 1
UVOSLinux:2421:2421 [1] NCCL INFO /usr/src/debug/rccl/build/hipify/src/init.cc:2415 -> 1
UVOSLinux: Test NCCL failure /home/philipp/Programming/rccl-tests/build/hipify/common.cu.cpp:1291 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. UVOSLinux pid 2421: Test failure /home/philipp/Programming/rccl-tests/build/hipify/common.cu.cpp:1165
```

### IMbackK · 2024-12-10

So the proximte cause of the errors below Note 1 and Note 3 is ncclGroupEnd() returning ncclUnhandledCudaError here: 
https://github.com/ROCm/rccl/blob/6d34fb76321600d5693b24f1edc875605c5cc638/src/init.cc#L2428
however things go off the rails before that already with ncclCalloc here:
https://github.com/ROCm/rccl/blob/6d34fb76321600d5693b24f1edc875605c5cc638/src/init.cc#L2401
not returing any failure but failing to allocate any memory:

```
# nThread 1 nGpus 2 minBytes 2 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:ae3e635
# Using devices
#   Rank  0 Pid  19276 on  UVOSLinux device  0 [0000:83:00.0] AMD Instinct MI100
#   Rank  1 Pid  19276 on  UVOSLinux device  1 [0000:03:00.0] AMD Instinct MI100
[New Thread 0x7fffe2fff6c0 (LWP 19280)]
[New Thread 0x7fffe27fe6c0 (LWP 19281)]

Thread 1 "all_reduce_perf" hit Breakpoint 1.1, run () at /home/philipp/Programming/rccl-tests/build/src/hipify/common.cu.cpp:1291
1291           NCCLCHECK(ncclCommInitAll(comms, nGpus*nThreads, gpus));
(gdb) c
Continuing.

Thread 1 "all_reduce_perf" hit Breakpoint 2, ncclCommInitAll_impl (comms=0x555557343c90, ndev=2, devlist=0x7fffffffb990) at /usr/src/debug/rccl/build/hipify/src/init.cc:2388
2388        NCCLCHECKGOTO(ncclCalloc(&gpuFlags, totalnDev), ret, fail);
(gdb) p gpuFlags
$21 = (int *) 0x0
(gdb) n
2389        for (int i = 0; i < ndev; ++i) {
(gdb) p gpuFlags
$22 = (int *) 0x0
```



### IMbackK · 2024-12-10

rccl allso apears to have a double free in ncclCommInitAll_impl as gpuFlags is freed here:
https://github.com/ROCm/rccl/blob/6d34fb76321600d5693b24f1edc875605c5cc638/src/init.cc#L2417

and if any of the other calls with NCCLCHECKGOTO( fail it is again freed here:
https://github.com/ROCm/rccl/blob/6d34fb76321600d5693b24f1edc875605c5cc638/src/init.cc#L2431

### IMbackK · 2024-12-10

compileing with rccl "-O1 -fno-strict-aliasing" solves ncclCalloc not allocateing any memory, clearly rccl has UB.
But this dose not solve ncclGroupEnd failing.

### IMbackK · 2024-12-10

Note the gpus are connected via PCIE only not xgmi/if

Futher traceing has the failure occureing at:
https://github.com/ROCm/rccl/blob/9aa5b9f02e20cc95e465004af728b907ab178fe9/src/group.cc#L331

due to the other thread failing in ncclCommInitRankFunc

I dont think futher traceing on my part will be useful.

### LunNova · 2024-12-15

> and if any of the other calls with NCCLCHECKGOTO( fail it is again freed here:

That part should be fine, it sets it to nullptr after the first free and free(nullptr) is defined to be a noop.

Are you using in-tree amdgpu or amdgpu-dkms (ROCm/ROCK-Kernel-Driver)?  
Some rccl functionality appears to rely on things that are in amdgpu-dkms and not in-tree like `kfd_peerdirect.c`.

I was able to repro some UB on mainline kernel with ASAN and UBSAN enabled + a small patch to assume the kernel config options are on since the config file isn't available and I confirmed they are on this system.  
Here's the log in case it's helpful: https://gist.github.com/LunNova/0809398bd1abce6dbe2402bf0a89d881

### LunNova · 2024-12-15

Workarounds for UB: https://gist.github.com/LunNova/1aeafef9239e129985714b8edbcfd58f

You may also need to set env var `HSA_ENABLE_IPC_MODE_LEGACY=0`. It's undocumented and defaults to 1. If set to 1 hipIpcGetMemHandle will fail on mainline drivers because it tries to use the out-of-tree only hsaKmtShareMemory API instead of DMABUF.  
https://github.com/ROCm/ROCR-Runtime/blob/e93efba9cc892e8ef878ef25ddea16c7773af51a/runtime/hsa-runtime/core/runtime/runtime.cpp#L1248-L1264

AMD, it'd be great if you turned on UBSAN and ASAN in CI for your RCCL tests and tested against in-tree amdgpu so these issues get caught sooner.

### IMbackK · 2024-12-16

> > and if any of the other calls with NCCLCHECKGOTO( fail it is again freed here:
> 
> That part should be fine, it sets it to nullptr after the first free and free(nullptr) is defined to be a noop.

Right, i missed the = nullptr there.



> Workarounds for UB: https://gist.github.com/LunNova/1aeafef9239e129985714b8edbcfd58f
> 
> You may also need to set env var `HSA_ENABLE_IPC_MODE_LEGACY=0`. It's undocumented and defaults to 1. If set to 1 hipIpcGetMemHandle will fail on mainline drivers because it tries to use the out-of-tree only hsaKmtShareMemory API instead of DMABUF. https://github.com/ROCm/ROCR-Runtime/blob/e93efba9cc892e8ef878ef25ddea16c7773af51a/runtime/hsa-runtime/core/runtime/runtime.cpp#L1248-L1264

I am running upstream amdgpu.ko, unfortionatly  applying your patch and running `HSA_ENABLE_IPC_MODE_LEGACY=0 ./all_reduce_perf -b 2 -e 128M -f 2 -g 2` makes no difference on my machine, so i am encountering a different/additional issue.

### huanrwan-amd · 2024-12-16

@IMbackK can you check the amdgpu kernel driver version using "dkms status"? You can refer: 
- https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/amdgpu-install.html#install-amdgpu-dkms

I ran the tests with amdgpu/6.10.5-2084815.22.04 on MI100 with ROCm 6.3, it works fine. Please let me know you output. Thanks



### IMbackK · 2024-12-18

@LunNova @LunNova 

Ok so the issue is actually that in rocm 6.2.x HSA_ENABLE_IPC_MODE_LEGACY is ineffective:
https://github.com/ROCm/ROCR-Runtime/blob/df7549038b458c9387a2c6ea8d9328e3c9e6620c/src/core/util/flag.h#L233

IMO the main problem here is that ROCR simply chooses kfd_ipc on the mainline kernel with no regard for the fact that the related ioctls are not supported. It needs to 1. use dmabuf in this case or at least 2. print a proper error message and abort.

### IMbackK · 2024-12-18

this shows the issues under note 1 and note 3 are ROCR's fault and not RCCL's however the issue under Note 2 seams wholly unrelated, different problem and the UB still requires fixing.

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2779

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
