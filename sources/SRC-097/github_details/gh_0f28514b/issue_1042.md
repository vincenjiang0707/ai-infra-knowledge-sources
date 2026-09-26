# [Issue #1042] Segmentation fault with cuda_ipc

source: https://github.com/ai-dynamo/nixl/issues/1042
state: closed | updated: 2026-03-16T12:41:37Z
labels: 

## 正文

Hi, i've encountered issues when trying to use cuda_ipc with UCX and the backend for NiXL. I've been getting segmentation faults when trying to use NVLink with `UCX_TLS=cuda_ipc,cuda_copy,tcp,sm,self`. The code seems to work with `rc_mlx5` however that only yields ~20GB/s transfer bandwidth.

Environment Setup:
NiXL 0.7.1 (built from source)
UCX 1.19.0 (built from source)

Hardware: H100 80GB x 2

Error message:
```
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:50 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:51 NIXL H100 NVLink Bandwidth Test
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:52 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:53 Mode: target
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:54 GPU: 0 - NVIDIA H100 80GB HBM3
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:50 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:51 NIXL H100 NVLink Bandwidth Test
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:52 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:53 Mode: initiator
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:54 GPU: 1 - NVIDIA H100 80GB HBM3
2025-11-20 12:44:45 NIXL INFO    _api.py:361 Backend UCX was instantiated
2025-11-20 12:44:45 NIXL INFO    _api.py:251 Initialized NIXL agent: initiator
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:61 NIXL agent created (listen_port=0)
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:62 Check UCX log above for transport selection!
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:63 Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!
2025-11-20 12:44:45 NIXL INFO    _api.py:361 Backend UCX was instantiated
2025-11-20 12:44:45 NIXL INFO    _api.py:251 Initialized NIXL agent: target
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:61 NIXL agent created (listen_port=3005)
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:62 Check UCX log above for transport selection!
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:63 Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:78 Transfer size: 5.0000 GB (10 x (1024, 2, 32, 4096))
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:79 Expected H100 NVLink: ~400 GB/s
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:80 Iterations: warmup=3, test=10
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:81 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:78 Transfer size: 5.0000 GB (10 x (1024, 2, 32, 4096))
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:84 Registering GPU memory with NIXL...
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:79 Expected H100 NVLink: ~400 GB/s
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:80 Iterations: warmup=3, test=10
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:81 ================================================================================
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:84 Registering GPU memory with NIXL...
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:89 Memory registered
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:93 
TARGET: Listening on port 3005...
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:89 Memory registered
2025-11-20 12:44:45 NIXL INFO    nixl_h100_nvlink.py:132 
INITIATOR: Waiting for target...
2025-11-20 12:44:47 NIXL INFO    nixl_h100_nvlink.py:135 INITIATOR: Connecting to 127.0.0.1:3005
2025-11-20 12:44:47 NIXL INFO    nixl_h100_nvlink.py:107 TARGET: Initiator connected
2025-11-20 12:44:47 NIXL INFO    nixl_h100_nvlink.py:109 TARGET: Sent descriptors, ready for transfers
2025-11-20 12:44:48 NIXL INFO    nixl_h100_nvlink.py:165 INITIATOR: Connected and ready
2025-11-20 12:44:48 NIXL INFO    nixl_h100_nvlink.py:166 ================================================================================
2025-11-20 12:44:48 NIXL INFO    nixl_h100_nvlink.py:171 
WARMUP PHASE
[h000:2722682:0:2722812] Caught signal 11 (Segmentation fault: invalid permissions for mapped object at address 0x147980000000)
==== backtrace (tid:2722812) ====
 0 0x000000000003ebf0 __GI___sigaction()  :0
 1 0x0000000000190acd __memmove_avx512_unaligned_erms()  :0
 2 0x000000000008fc91 ucp_get()  ???:0
 3 0x0000000000029b69 uct_tcp_ep_am_bcopy()  ???:0
 4 0x000000000008f81a ucp_get()  ???:0
 5 0x00000000000905a1 ucp_get_req_handler()  ???:0
 6 0x0000000000027a10 uct_tcp_ep_handle_io_err()  ???:0
 7 0x000000000002aedd uct_tcp_iface_progress()  ???:0
 8 0x000000000007ac9c ucs_event_set_wait()  ???:0
 9 0x000000000002ae17 uct_tcp_iface_progress()  ???:0
10 0x000000000006187a ucp_worker_progress()  ???:0
11 0x000000000003f131 nixlUcxSharedThread::run()  :0
12 0x00000000000df0e6 execute_native_thread_routine()  /home/task_176276935360828/conda-bld/gcc_compilers_1762769419537/work/build/x86_64-conda-linux-gnu/libstdc++-v3/src/c++11/../../../../../libstdc++-v3/src/c++11/thread.cc:104
13 0x000000000008a19a start_thread()  ???:0
14 0x000000000010f210 __clone3()  :0
=================================
Traceback (most recent call last):
  File "/scratch/gautschi/wang6199/nixl/nixl_h100_nvlink.py", line 300, in <module>
    main()
  File "/scratch/gautschi/wang6199/nixl/nixl_h100_nvlink.py", line 194, in main
    state = agent.check_xfer_state(xfer_handle)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/python3.12/site-packages/nixl_cu12/_api.py", line 613, in check_xfer_state
    status = self.agent.getXferStatus(handle._handle)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
nixl_cu12._bindings.nixlRemoteDisconnectError: NIXL_ERR_REMOTE_DISCONNECT
```

My code:

```
import argparse
import os

import torch
import time
import numpy as np
from nixl._api import nixl_agent, nixl_agent_config
from nixl.logging import get_logger

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, required=True)
    parser.add_argument("--port", type=int, default=3005)
    parser.add_argument("--mode", type=str, required=True, choices=["target", "initiator"])
    parser.add_argument("--num_tensors", type=int, default=10)
    parser.add_argument("--tensor_shape", type=str, default="1024,2,32,4096")
    parser.add_argument("--warmup_iters", type=int, default=3)
    parser.add_argument("--test_iters", type=int, default=10)
    return parser.parse_args()


def main():
    args = parse_args()
    
    tensor_shape = tuple(map(int, args.tensor_shape.split(',')))

    # Device setup
    device_id = 0 if args.mode == "target" else 1
    torch.cuda.set_device(device_id)
    torch.set_default_device(f"cuda:{device_id}")
    torch.cuda.synchronize()
    
    # Verify CUDA IPC
    try:
        torch.cuda.ipc_collect()
    except Exception as e:
        logger.error(f"CUDA IPC not available: {e}")
        exit(1)
    
    logger.info("=" * 80)
    logger.info("NIXL H100 NVLink Bandwidth Test")
    logger.info("=" * 80)
    logger.info(f"Mode: {args.mode}")
    logger.info(f"GPU: {device_id} - {torch.cuda.get_device_name(device_id)}")

    # Create agent with progress and listener threads enabled
    listen_port = args.port if args.mode == "target" else 0
    config = nixl_agent_config(True, True, listen_port, backends=["UCX"])
    agent = nixl_agent(args.mode, config)
    
    logger.info(f"NIXL agent created (listen_port={listen_port})")
    logger.info("Check UCX log above for transport selection!")
    logger.info("Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!")
    
    # Allocate contiguous GPU memory
    if args.mode == "target":
        tensors = [torch.ones(tensor_shape, dtype=torch.bfloat16, device='cuda').contiguous() 
                   for _ in range(args.num_tensors)]
    else:
        tensors = [torch.zeros(tensor_shape, dtype=torch.bfloat16, device='cuda').contiguous() 
                   for _ in range(args.num_tensors)]
    
    torch.cuda.synchronize()
    
    total_bytes = tensors[0].numel() * tensors[0].element_size() * len(tensors)
    total_gb = total_bytes / (1024 ** 3)
    
    logger.info(f"Transfer size: {total_gb:.4f} GB ({len(tensors)} x {tensor_shape})")
    logger.info(f"Iterations: warmup={args.warmup_iters}, test={args.test_iters}")
    logger.info("=" * 80)

    # Register memory
    logger.info("Registering GPU memory with NIXL...")
    reg_descs = agent.register_memory(tensors)
    if not reg_descs:
        logger.error("Memory registration failed")
        exit(1)
    logger.info("Memory registered")

    if args.mode == "target":
        # TARGET
        logger.info("\nTARGET: Listening on port %d...", args.port)
        
        target_descs = reg_descs.trim()
        target_desc_str = agent.get_serialized_descs(target_descs)

        # Wait for initiator
        timeout = 60
        start = time.time()
        while not agent.check_remote_metadata("initiator"):
            if time.time() - start > timeout:
                logger.error("Timeout waiting for initiator")
                exit(1)
            time.sleep(0.1)

        logger.info("TARGET: Initiator connected")
        agent.send_notif("initiator", target_desc_str)
        logger.info("TARGET: Sent descriptors, ready for transfers")

        # Wait for all transfers
        total_iters = args.warmup_iters + args.test_iters
        for i in range(total_iters):
            iter_uuid = f"UUID_{i}".encode()
            start = time.time()
            
            while not agent.check_remote_xfer_done("initiator", iter_uuid):
                if time.time() - start > timeout:
                    logger.error(f"Timeout on transfer {i}")
                    exit(1)
                time.sleep(0.001)
            
            if i < args.warmup_iters:
                logger.info(f"TARGET: Warmup {i+1}/{args.warmup_iters} done")
            else:
                logger.info(f"TARGET: Test {i-args.warmup_iters+1}/{args.test_iters} done")

        logger.info("TARGET: All transfers complete")

    else:
        # INITIATOR
        logger.info("\nINITIATOR: Waiting for target...")
        time.sleep(2)

        logger.info("INITIATOR: Connecting to %s:%d", args.ip, args.port)
        try:
            agent.fetch_remote_metadata("target", args.ip, args.port)
            agent.send_local_metadata(args.ip, args.port)
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            exit(1)

        # Wait for descriptors
        timeout = 60
        start = time.time()
        notifs = []
        while len(notifs) == 0:
            notifs = agent.get_new_notifs()
            if time.time() - start > timeout:
                logger.error("Timeout waiting for descriptors")
                exit(1)
            time.sleep(0.1)

        target_descs = agent.deserialize_descs(notifs["target"][0])
        initiator_descs = reg_descs.trim()

        # Verify metadata
        start = time.time()
        while not agent.check_remote_metadata("target"):
            if time.time() - start > timeout:
                logger.error("Timeout on metadata verification")
                exit(1)
            time.sleep(0.1)

        logger.info("INITIATOR: Connected and ready")
        logger.info("=" * 80)

        test_times = []

        # WARMUP
        logger.info("\nWARMUP PHASE")
        for i in range(args.warmup_iters):
            for t in tensors:
                t.zero_()
            torch.cuda.synchronize()

            xfer_handle = agent.initialize_xfer(
                "READ", initiator_descs, target_descs, "target", f"UUID_{i}"
            )
            
            if not xfer_handle:
                logger.error("Transfer initialization failed")
                exit(1)

            start_time = time.perf_counter()
            state = agent.transfer(xfer_handle)
            
            if state == "ERR":
                logger.error("Transfer post failed")
                exit(1)
            
            # Poll for completion
            while True:
                state = agent.check_xfer_state(xfer_handle)
                if state == "ERR":
                    logger.error("Transfer error")
                    exit(1)
                elif state == "DONE":
                    break
                time.sleep(0.00001)

            torch.cuda.synchronize()
            elapsed = time.perf_counter() - start_time
            bw = total_gb / elapsed
            
            logger.info(f"Warmup {i+1}: {elapsed:.4f}s = {bw:.2f} GB/s")
            agent.release_xfer_handle(xfer_handle)

        # TEST
        logger.info("\nTEST PHASE")
        for i in range(args.test_iters):
            for t in tensors:
                t.zero_()
            torch.cuda.synchronize()

            xfer_handle = agent.initialize_xfer(
                "READ", initiator_descs, target_descs, "target", 
                f"UUID_{args.warmup_iters + i}"
            )
            
            if not xfer_handle:
                logger.error("Transfer initialization failed")
                exit(1)

            start_time = time.perf_counter()
            state = agent.transfer(xfer_handle)
            
            if state == "ERR":
                logger.error("Transfer post failed")
                exit(1)
            
            while True:
                state = agent.check_xfer_state(xfer_handle)
                if state == "ERR":
                    logger.error("Transfer error")
                    exit(1)
                elif state == "DONE":
                    break
                time.sleep(0.00001)

            torch.cuda.synchronize()
            elapsed = time.perf_counter() - start_time
            test_times.append(elapsed)
            bw = total_gb / elapsed
            
            logger.info(f"Test {i+1}: {elapsed:.4f}s = {bw:.2f} GB/s")
            agent.release_xfer_handle(xfer_handle)

        # Verify
        logger.info("\nVerifying data...")
        ok = all(torch.allclose(t, torch.ones_like(t), rtol=1e-2) for t in tensors)
        if ok:
            logger.info("✓ Data verification PASSED")
        else:
            logger.error("✗ Data verification FAILED")

        # Statistics
        mean_time = np.mean(test_times)
        std_time = np.std(test_times)
        min_time = np.min(test_times)
        max_time = np.max(test_times)
        
        mean_bw = total_gb / mean_time
        peak_bw = total_gb / min_time
        min_bw = total_gb / max_time
        
        logger.info("\n" + "=" * 80)
        logger.info("FINAL RESULTS")
        logger.info("=" * 80)
        logger.info(f"Transfer size: {total_gb:.4f} GB")
        logger.info(f"Iterations: {args.test_iters}")
        logger.info("-" * 80)
        logger.info(f"Mean bandwidth: {mean_bw:.2f} GB/s")
        logger.info(f"Peak bandwidth: {peak_bw:.2f} GB/s")
        logger.info(f"Min bandwidth:  {min_bw:.2f} GB/s")
        logger.info("-" * 80)
        logger.info(f"Mean time: {mean_time:.4f}s (±{std_time:.4f}s)")
        logger.info("=" * 80)

        agent.remove_remote_agent("target")
        agent.invalidate_local_metadata(args.ip, args.port)

    agent.deregister_memory(reg_descs)
    logger.info("\nTest complete!")


if __name__ == "__main__":
    main()
```

My Script:
```
UCX_TLS=cuda_ipc,cuda_copy,sm,tcp,self python3 nixl_h100_nvlink.py --ip 127.0.0.1 --port 3005 --mode target &
UCX_TLS=cuda_ipc,cuda_copy,sm,tcp,self python3 nixl_h100_nvlink.py --ip 127.0.0.1 --mode initiator
```

UCX is built with CUDA support:
```
# Memory domain: cuda_cpy
#     Component: cuda_cpy
#             allocate: unlimited
#             register: unlimited, cost: 0 nsec
#         memory types: host (access,reg), cuda (access,alloc,reg,detect,dmabuf), cuda-managed (access,alloc,reg,cache,detect)
#
#      Transport: cuda_copy
#         Device: cuda
#           Type: accelerator
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 10000.00/ppn + 0.00 MB/sec
#              latency: 8000 nsec
#             overhead: 0 nsec
#            put_short: <= 4294967295
#            put_zcopy: unlimited, up to 1 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_short: <= 4294967295
#            get_zcopy: unlimited, up to 1 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 0 bytes
#        iface address: 8 bytes
#       error handling: none
#
#
# Memory domain: cuda_ipc
#     Component: cuda_ipc
#             register: unlimited, cost: 0 nsec
#           remote key: 192 bytes
#           memory invalidation is supported
#         memory types: cuda (access,reg,cache)
#
#      Transport: cuda_ipc
#         Device: cuda
#           Type: intra-node
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 400000.00/ppn + 0.00 MB/sec
#              latency: 1000 nsec
#             overhead: 7000 nsec
#            put_zcopy: unlimited, up to 1 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 1 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 8 bytes
#        iface address: 4 bytes
#       error handling: peer failure
```

Thanks in advance!

## 评论 (10)

### brminich · 2025-11-20

looks like GPU memory is not properly recognized. 
Can you pls run this app with `UCX_LOG_LEVEL=debug` and provide the output

### Marmot-C · 2025-11-21

Hi @brminich , thank you for the reply! The log messages are as follows:

<details>
<summary>Click to expand logs</summary>

```
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:43 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:44 NIXL H100 NVLink Bandwidth Test
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:45 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:46 Mode: target
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:47 GPU: 0 - NVIDIA H100 80GB HBM3
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:43 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:44 NIXL H100 NVLink Bandwidth Test
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:45 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:46 Mode: initiator
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:47 GPU: 1 - NVIDIA H100 80GB HBM3
[1763745250.293985] [h001:2082100:0]           debug.c:1157 UCX  DEBUG using signal stack 0x14ea6e63e000 size 181440
[1763745250.296153] [h001:2082100:0]             cpu.c:338  UCX  DEBUG measured tsc frequency 2000.095 MHz after 0.68 ms
[1763745250.296187] [h001:2082100:0]            init.c:120  UCX  DEBUG /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucs.so.0 loaded at 0x14ea6e6d6000
[1763745250.296199] [h001:2082100:0]            init.c:122  UCX  DEBUG cmd line: python3 nixl_h100_nvlink.py --ip 127.0.0.1 --port 3005 --mode target 
[1763745250.296216] [h001:2082100:0]          module.c:72   UCX  DEBUG ucs library path: /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucs.so.0
[1763745250.296218] [h001:2082100:0]          module.c:304  UCX  DEBUG loading modules for ucs
[1763745250.296437] [h001:2082100:0]            time.c:22   UCX  DEBUG arch clock frequency: 2000094814.81 Hz
[1763745250.296543] [h001:2082100:0]     ucp_context.c:2339 UCX  INFO  Version 1.19.0 (loaded from /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucp.so.0)
[1763745250.296550] [h001:2082100:0]     ucp_context.c:2087 UCX  DEBUG estimated number of endpoints is 1
[1763745250.296551] [h001:2082100:0]     ucp_context.c:2094 UCX  DEBUG estimated number of endpoints per node is 1
[1763745250.296554] [h001:2082100:0]     ucp_context.c:2105 UCX  DEBUG estimated bcopy bandwidth is 6081740800.000000
[1763745250.296558] [h001:2082100:0]     ucp_context.c:2164 UCX  DEBUG allocation method[0] is md 'sysv'
[1763745250.296560] [h001:2082100:0]     ucp_context.c:2164 UCX  DEBUG allocation method[1] is md 'posix'
[1763745250.296563] [h001:2082100:0]     ucp_context.c:2176 UCX  DEBUG allocation method[2] is 'thp'
[1763745250.296564] [h001:2082100:0]     ucp_context.c:2164 UCX  DEBUG allocation method[3] is md '*'
[1763745250.296565] [h001:2082100:0]     ucp_context.c:2176 UCX  DEBUG allocation method[4] is 'mmap'
[1763745250.296566] [h001:2082100:0]     ucp_context.c:2176 UCX  DEBUG allocation method[5] is 'heap'
[1763745250.296576] [h001:2082100:0]          module.c:304  UCX  DEBUG loading modules for uct
[1763745250.298890] [h001:2082100:0]          module.c:304  UCX  DEBUG loading modules for uct_cuda
[1763745250.301149] [h001:2082100:0]          module.c:304  UCX  DEBUG loading modules for uct_ib
[1763745250.317301] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 0 for bus id 4c:00.0
[1763745250.317338] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 1 for bus id 5d:00.0
[1763745250.368811] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.368846] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 2 for bus id 1b:00.0
[1763745250.368849] [h001:2082100:0]            topo.c:560  UCX  DEBUG ibp27s0: bdf_name 0000:1b:00.0 sys_dev 2
[1763745250.370041] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.370043] [h001:2082100:0]            topo.c:564  UCX  DEBUG lo: system device unknown
[1763745250.370189] [h001:2082100:0]    cuda_copy_md.c:110  UCX  DEBUG dmabuf is supported on cuda device 0
[1763745250.370561] [h001:2082100:0]     cuda_ipc_md.c:491  UCX  DEBUG fabric_info: state=3 status=0 uuid=00000000:00000000:00000000:00000000
[1763745250.370563] [h001:2082100:0]     cuda_ipc_md.c:514  UCX  DEBUG multi-node NVLINK support is disabled
[1763745250.374444] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_0) failed: 95
[1763745250.375209] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_0: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.381386] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:02.0/0000:1a:00.0'
[1763745250.381418] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 3 for bus id 1a:00.0
[1763745250.381419] [h001:20821[1763745250.294028] [h001:2082112:0]           debug.c:1157 UCX  DEBUG using signal stack 0x15103d82a000 size 181440
[1763745250.296170] [h001:2082112:0]             cpu.c:338  UCX  DEBUG measured tsc frequency 1998.791 MHz after 0.68 ms
[1763745250.296205] [h001:2082112:0]            init.c:120  UCX  DEBUG /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucs.so.0 loaded at 0x15103d8c2000
[1763745250.296223] [h001:2082112:0]            init.c:122  UCX  DEBUG cmd line: python3 nixl_h100_nvlink.py --ip 127.0.0.1 --port 3005 --mode initiator 
[1763745250.296239] [h001:2082112:0]          module.c:72   UCX  DEBUG ucs library path: /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucs.so.0
[1763745250.296242] [h001:2082112:0]          module.c:304  UCX  DEBUG loading modules for ucs
[1763745250.296687] [h001:2082112:0]            time.c:22   UCX  DEBUG arch clock frequency: 1998791111.11 Hz
[1763745250.296789] [h001:2082112:0]     ucp_context.c:2339 UCX  INFO  Version 1.19.0 (loaded from /scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/libucp.so.0)
[1763745250.296796] [h001:2082112:0]     ucp_context.c:2087 UCX  DEBUG estimated number of endpoints is 1
[1763745250.296797] [h001:2082112:0]     ucp_context.c:2094 UCX  DEBUG estimated number of endpoints per node is 1
[1763745250.296800] [h001:2082112:0]     ucp_context.c:2105 UCX  DEBUG estimated bcopy bandwidth is 6081740800.000000
[1763745250.296803] [h001:2082112:0]     ucp_context.c:2164 UCX  DEBUG allocation method[0] is md 'sysv'
[1763745250.296804] [h001:2082112:0]     ucp_context.c:2164 UCX  DEBUG allocation method[1] is md 'posix'
[1763745250.296808] [h001:2082112:0]     ucp_context.c:2176 UCX  DEBUG allocation method[2] is 'thp'
[1763745250.296809] [h001:2082112:0]     ucp_context.c:2164 UCX  DEBUG allocation method[3] is md '*'
[1763745250.296810] [h001:2082112:0]     ucp_context.c:2176 UCX  DEBUG allocation method[4] is 'mmap'
[1763745250.296811] [h001:2082112:0]     ucp_context.c:2176 UCX  DEBUG allocation method[5] is 'heap'
[1763745250.296821] [h001:2082112:0]          module.c:304  UCX  DEBUG loading modules for uct
[1763745250.298893] [h001:2082112:0]          module.c:304  UCX  DEBUG loading modules for uct_cuda
[1763745250.301159] [h001:2082112:0]          module.c:304  UCX  DEBUG loading modules for uct_ib
[1763745250.317306] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 0 for bus id 4c:00.0
[1763745250.317344] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 1 for bus id 5d:00.0
[1763745250.369991] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.370044] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 2 for bus id 1b:00.0
[1763745250.370046] [h001:2082112:0]            topo.c:560  UCX  DEBUG ibp27s0: bdf_name 0000:1b:00.0 sys_dev 2
[1763745250.370701] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.370703] [h001:2082112:0]            topo.c:564  UCX  DEBUG lo: system device unknown
[1763745250.370845] [h001:2082112:0]    cuda_copy_md.c:110  UCX  DEBUG dmabuf is supported on cuda device 0
[1763745250.371173] [h001:2082112:0]     cuda_ipc_md.c:491  UCX  DEBUG fabric_info: state=3 status=0 uuid=00000000:00000000:00000000:00000000
[1763745250.371175] [h001:2082112:0]     cuda_ipc_md.c:514  UCX  DEBUG multi-node NVLINK support is disabled
[1763745250.375235] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_0) failed: 95
[1763745250.376498] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_0: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.381456] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:02.0/0000:1a:00.0'
[1763745250.381485] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 3 for bus id 1a:00.0
[1763745250.381487] [h001:2000:0]            topo.c:560  UCX  DEBUG mlx5_0: bdf_name 0000:1a:00.0 sys_dev 3
[1763745250.381446] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_0: vendor_id 0x15b3 device_id 4129
[1763745250.382052] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_0: mkey_by_name_reserve is not supported
[1763745250.382053] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_0: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.382215] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_0: ODP is supported, version 2: memory=host
[1763745250.382792] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac7a010 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.382912] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.382914] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_0' (InfiniBand channel adapter) with 1 ports
[1763745250.382944] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.382954] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.382961] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.382970] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_0: dmabuf is supported
[1763745250.382978] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.383272] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_0: opened DEVX md log_max_qp=17
[1763745250.384241] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.384497] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.385467] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_0: relaxed order memory access is disabled
[1763745250.385737] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM flush-mr memory registration status "Success" range 0xac77000..0xac77008 iova 0x0 mkey_index 0x0
[1763745250.386036] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_0, syndrome 0x172df6: Remote I/O error
[1763745250.386037] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_0: XGVMI is not supported
[1763745250.386039] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_0: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.393434] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.393461] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_0 because it has no selected transport resources
[1763745250.393467] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_0: md=0xac31730 md->flags=0x3f51f7f flush_rkey=0x172900
[1763745250.393813] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.393814] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_0
[1763745250.393818] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac7a010 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.393819] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac7a010 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.393870] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac7a010 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.399183] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_1) failed: 95
[1763745250.400061] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_1: md open by 82112:0]            topo.c:560  UCX  DEBUG mlx5_0: bdf_name 0000:1a:00.0 sys_dev 3
[1763745250.381511] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_0: vendor_id 0x15b3 device_id 4129
[1763745250.382075] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_0: mkey_by_name_reserve is not supported
[1763745250.382076] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_0: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.382229] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_0: ODP is supported, version 2: memory=host
[1763745250.382792] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25d010 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.382924] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.382926] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_0' (InfiniBand channel adapter) with 1 ports
[1763745250.382952] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.382959] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.382964] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_0: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.382973] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_0: dmabuf is supported
[1763745250.382980] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.383331] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_0: opened DEVX md log_max_qp=17
[1763745250.384303] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.384549] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.385512] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_0: relaxed order memory access is disabled
[1763745250.385802] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_0: KSM flush-mr memory registration status "Success" range 0xa25a000..0xa25a008 iova 0x0 mkey_index 0x0
[1763745250.386034] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_0, syndrome 0x172df6: Remote I/O error
[1763745250.386036] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_0: XGVMI is not supported
[1763745250.386037] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_0: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.393428] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.393456] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_0 because it has no selected transport resources
[1763745250.393462] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_0: md=0xa214550 md->flags=0x3f51f7f flush_rkey=0x173500
[1763745250.393801] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.393803] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_0
[1763745250.393807] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25d010 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.393808] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa25d010 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.393869] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25d010 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.399485] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_1) failed: 95
[1763745250.400571] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_1: md open 'uct_ib_efa_md_ops' failed, trying next
[1763745250.406027] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_1: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.406032] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_1: bdf_name 0000:1b:00.0 sys_dev 2
[1763745250.406043] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_1: vendor_id 0x15b3 device_id 4129
[1763745250.406647] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_1: mkey_by_name_reserve is not supported
[1763745250.406649] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_1: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.406810] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_1: ODP is supported, version 2: memory=host
[1763745250.406978] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac782b0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.407038] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.407040] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_1' (InfiniBand channel adapter) with 1 ports
[1763745250.407047] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.407051] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.407055] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.407061] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_1: dmabuf is supported
[1763745250.407064] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.407356] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_1: opened DEVX md log_max_qp=17
[1763745250.408388] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.408644] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.409766] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_1: relaxed order memory access is disabled
[1763745250.410093] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.410320] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_1, syndrome 0x172df6: Remote I/O error
[1763745250.410322] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_1: XGVMI is not supported
[1763745250.410323] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_1: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.418003] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.418028] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_1 because it has no selected transport resources
[1763745250.418033] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_1: md=0xac77810 md->flags=0x3f51f7f flush_rkey=0x220200
[1763745250.418427] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.418429] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_1
[1763745250.418431] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac782b0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.418432] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac782b0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.418476] [h001:2082100:0]           async.c:187  UCX  DEBUG releasby 'uct_ib_efa_md_ops' failed, trying next
[1763745250.405990] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_1: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.405996] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_1: bdf_name 0000:1b:00.0 sys_dev 2
[1763745250.406013] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_1: vendor_id 0x15b3 device_id 4129
[1763745250.406655] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_1: mkey_by_name_reserve is not supported
[1763745250.406656] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_1: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.406816] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_1: ODP is supported, version 2: memory=host
[1763745250.406987] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa259eb0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.407085] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.407087] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_1' (InfiniBand channel adapter) with 1 ports
[1763745250.407096] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.407101] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.407106] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_1: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.407115] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_1: dmabuf is supported
[1763745250.407117] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.407410] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_1: opened DEVX md log_max_qp=17
[1763745250.408337] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.408597] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.409753] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_1: relaxed order memory access is disabled
[1763745250.410030] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_1: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.410326] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_1, syndrome 0x172df6: Remote I/O error
[1763745250.410328] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_1: XGVMI is not supported
[1763745250.410329] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_1: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.417997] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.418023] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_1 because it has no selected transport resources
[1763745250.418028] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_1: md=0xa25a810 md->flags=0x3f51f7f flush_rkey=0x220100
[1763745250.418421] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.418423] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_1
[1763745250.418426] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa259eb0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.418427] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa259eb0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.418491] [h001:2082112:0]           async.c:187  UCX  DEBUG rele async handler 0xac782b0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.423780] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_2) failed: 95
[1763745250.424661] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_2: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.430441] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_2: PF sysfs path is '/sys/devices/pci0000:37/0000:37:01.0/0000:38:00.0/0000:39:02.0/0000:3c:00.0'
[1763745250.430477] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 4 for bus id 3c:00.0
[1763745250.430479] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_2: bdf_name 0000:3c:00.0 sys_dev 4
[1763745250.430489] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_2: vendor_id 0x15b3 device_id 4129
[1763745250.431081] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_2: mkey_by_name_reserve is not supported
[1763745250.431082] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_2: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.431244] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_2: ODP is supported, version 2: memory=host
[1763745250.431411] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31490 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.431473] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.431474] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_2' (InfiniBand channel adapter) with 1 ports
[1763745250.431480] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.431484] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.431488] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.431493] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_2: dmabuf is supported
[1763745250.431495] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.431791] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_2: opened DEVX md log_max_qp=17
[1763745250.432699] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.432954] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.433835] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_2: relaxed order memory access is disabled
[1763745250.434110] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.434406] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_2, syndrome 0x172df6: Remote I/O error
[1763745250.434407] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_2: XGVMI is not supported
[1763745250.434409] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_2: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.440871] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.440895] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_2 because it has no selected transport resources
[1763745250.440900] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_2: md=0xac337e0 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.441541] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.441542] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_2
[1763ease async handler 0xa259eb0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.424087] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_2) failed: 95
[1763745250.425171] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_2: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.430389] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_2: PF sysfs path is '/sys/devices/pci0000:37/0000:37:01.0/0000:38:00.0/0000:39:02.0/0000:3c:00.0'
[1763745250.430446] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 4 for bus id 3c:00.0
[1763745250.430448] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_2: bdf_name 0000:3c:00.0 sys_dev 4
[1763745250.430466] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_2: vendor_id 0x15b3 device_id 4129
[1763745250.431088] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_2: mkey_by_name_reserve is not supported
[1763745250.431089] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_2: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.431245] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_2: ODP is supported, version 2: memory=host
[1763745250.431422] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa2142b0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.431516] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.431518] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_2' (InfiniBand channel adapter) with 1 ports
[1763745250.431526] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.431531] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.431537] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_2: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.431545] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_2: dmabuf is supported
[1763745250.431547] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.431847] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_2: opened DEVX md log_max_qp=17
[1763745250.432762] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.433008] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.433851] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_2: relaxed order memory access is disabled
[1763745250.434174] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_2: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.434410] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_2, syndrome 0x172df6: Remote I/O error
[1763745250.434411] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_2: XGVMI is not supported
[1763745250.434412] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_2: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.441371] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.441396] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_2 because it has no selected transport resources
[1763745250.441410] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_2: md=0xa25b950 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.441688] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.441689] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_2
[1745250.441544] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31490 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.441549] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31490 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.441581] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31490 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.446190] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_3) failed: 95
[1763745250.446960] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_3: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.452289] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_3: PF sysfs path is '/sys/devices/pci0000:48/0000:48:01.0/0000:49:00.0/0000:4a:02.0/0000:4d:00.0'
[1763745250.452311] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 5 for bus id 4d:00.0
[1763745250.452312] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_3: bdf_name 0000:4d:00.0 sys_dev 5
[1763745250.452321] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_3: vendor_id 0x15b3 device_id 4129
[1763745250.452859] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_3: mkey_by_name_reserve is not supported
[1763745250.452860] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_3: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.453021] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_3: ODP is supported, version 2: memory=host
[1763745250.453177] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31930 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.453235] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.453236] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_3' (InfiniBand channel adapter) with 1 ports
[1763745250.453242] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.453245] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.453249] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.453255] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_3: dmabuf is supported
[1763745250.453256] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.453556] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_3: opened DEVX md log_max_qp=17
[1763745250.454492] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.454750] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.455699] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_3: relaxed order memory access is disabled
[1763745250.455974] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.456264] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_3, syndrome 0x172df6: Remote I/O error
[1763745250.456265] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_3: XGVMI is not supported
[1763745250.456267] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_3: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.462958] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.462981] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_3 because 763745250.441691] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa2142b0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.441697] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa2142b0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.441742] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa2142b0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.446916] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_3) failed: 95
[1763745250.448002] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_3: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.452480] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_3: PF sysfs path is '/sys/devices/pci0000:48/0000:48:01.0/0000:49:00.0/0000:4a:02.0/0000:4d:00.0'
[1763745250.452504] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 5 for bus id 4d:00.0
[1763745250.452506] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_3: bdf_name 0000:4d:00.0 sys_dev 5
[1763745250.452516] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_3: vendor_id 0x15b3 device_id 4129
[1763745250.453046] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_3: mkey_by_name_reserve is not supported
[1763745250.453048] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_3: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.453185] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_3: ODP is supported, version 2: memory=host
[1763745250.453325] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25aba0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.453392] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.453394] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_3' (InfiniBand channel adapter) with 1 ports
[1763745250.453402] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.453406] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.453409] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_3: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.453415] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_3: dmabuf is supported
[1763745250.453417] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.453616] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_3: opened DEVX md log_max_qp=17
[1763745250.454551] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.454802] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.455745] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_3: relaxed order memory access is disabled
[1763745250.456038] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_3: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.456267] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_3, syndrome 0x172df6: Remote I/O error
[1763745250.456268] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_3: XGVMI is not supported
[1763745250.456269] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_3: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.463440] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.463464] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_3 becauit has no selected transport resources
[1763745250.462989] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_3: md=0xac772c0 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.463600] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.463601] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_3
[1763745250.463603] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31930 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.463605] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31930 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.463635] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31930 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.468057] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_4) failed: 95
[1763745250.468826] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_4: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.474227] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_4: PF sysfs path is '/sys/devices/pci0000:59/0000:59:01.0/0000:5a:00.0/0000:5b:02.0/0000:5e:00.0'
[1763745250.474250] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 6 for bus id 5e:00.0
[1763745250.474251] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_4: bdf_name 0000:5e:00.0 sys_dev 6
[1763745250.474261] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_4: vendor_id 0x15b3 device_id 4129
[1763745250.474802] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_4: mkey_by_name_reserve is not supported
[1763745250.474803] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_4: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.474945] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_4: ODP is supported, version 2: memory=host
[1763745250.475103] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac79e10 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.475158] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.475160] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_4' (InfiniBand channel adapter) with 1 ports
[1763745250.475165] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.475168] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.475172] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.475177] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_4: dmabuf is supported
[1763745250.475179] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.475462] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_4: opened DEVX md log_max_qp=17
[1763745250.476397] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.476657] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.477643] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_4: relaxed order memory access is disabled
[1763745250.477921] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.478213] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_4, syndrome 0x172df6: Remote I/O error
[1763745250.478214] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlse it has no selected transport resources
[1763745250.463472] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_3: md=0xa263110 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.463746] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.463747] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_3
[1763745250.463750] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25aba0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.463751] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa25aba0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.463788] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25aba0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.468781] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_4) failed: 95
[1763745250.469868] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_4: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.474342] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_4: PF sysfs path is '/sys/devices/pci0000:59/0000:59:01.0/0000:5a:00.0/0000:5b:02.0/0000:5e:00.0'
[1763745250.474366] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 6 for bus id 5e:00.0
[1763745250.474367] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_4: bdf_name 0000:5e:00.0 sys_dev 6
[1763745250.474377] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_4: vendor_id 0x15b3 device_id 4129
[1763745250.474910] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_4: mkey_by_name_reserve is not supported
[1763745250.474911] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_4: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.475051] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_4: ODP is supported, version 2: memory=host
[1763745250.475188] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25c9f0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.475249] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.475250] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_4' (InfiniBand channel adapter) with 1 ports
[1763745250.475255] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.475259] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.475263] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_4: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.475269] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_4: dmabuf is supported
[1763745250.475270] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.475514] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_4: opened DEVX md log_max_qp=17
[1763745250.476457] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.476709] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.477674] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_4: relaxed order memory access is disabled
[1763745250.477984] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_4: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.478216] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_4, syndrome 0x172df6: Remote I/O error
[1763745250.478217] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUGx5_4: XGVMI is not supported
[1763745250.478218] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_4: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.485442] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.485466] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_4 because it has no selected transport resources
[1763745250.485470] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_4: md=0xac78d40 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.485736] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.485738] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_4
[1763745250.485740] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac79e10 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.485741] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac79e10 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.485772] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac79e10 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.490899] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_5) failed: 95
[1763745250.491980] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_5: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.496444] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_5: PF sysfs path is '/sys/devices/pci0000:97/0000:97:01.0/0000:98:00.0/0000:99:02.0/0000:9c:00.0'
[1763745250.496468] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 7 for bus id 9c:00.0
[1763745250.496469] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_5: bdf_name 0000:9c:00.0 sys_dev 7
[1763745250.496479] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_5: vendor_id 0x15b3 device_id 4129
[1763745250.497041] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_5: mkey_by_name_reserve is not supported
[1763745250.497042] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_5: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.497213] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_5: ODP is supported, version 2: memory=host
[1763745250.497376] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.497435] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.497437] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_5' (InfiniBand channel adapter) with 1 ports
[1763745250.497442] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.497445] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.497449] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.497454] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_5: dmabuf is supported
[1763745250.497456] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.497740] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_5: opened DEVX md log_max_qp=17
[1763745250.498690] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_5: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.498952] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_5: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.499938] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_5: relaxed order memory access is disabled
[1763745250.500228] [h001:2082100:0]    ib_mlx5dv_md.c mlx5_4: XGVMI is not supported
[1763745250.478221] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_4: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.484946] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.484969] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_4 because it has no selected transport resources
[1763745250.484973] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_4: md=0xa25ba30 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.485590] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.485591] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_4
[1763745250.485593] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25c9f0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.485594] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa25c9f0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.485637] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25c9f0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.490153] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_5) failed: 95
[1763745250.490944] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_5: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.496375] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_5: PF sysfs path is '/sys/devices/pci0000:97/0000:97:01.0/0000:98:00.0/0000:99:02.0/0000:9c:00.0'
[1763745250.496427] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 7 for bus id 9c:00.0
[1763745250.496428] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_5: bdf_name 0000:9c:00.0 sys_dev 7
[1763745250.496443] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_5: vendor_id 0x15b3 device_id 4129
[1763745250.497043] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_5: mkey_by_name_reserve is not supported
[1763745250.497044] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_5: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.497207] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_5: ODP is supported, version 2: memory=host
[1763745250.497377] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.497463] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.497464] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_5' (InfiniBand channel adapter) with 1 ports
[1763745250.497471] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.497475] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.497478] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_5: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.497485] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_5: dmabuf is supported
[1763745250.497487] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.497794] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_5: opened DEVX md log_max_qp=17
[1763745250.498748] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_5: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.499003] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_5: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.499978] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_5: relaxed order memory access is disabled
[1763745250.500290] [h001:2082112:0]    ib_mlx5dv_m:140  UCX  DEBUG mlx5_5: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.500525] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_5, syndrome 0x172df6: Remote I/O error
[1763745250.500526] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_5: XGVMI is not supported
[1763745250.500527] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_5: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.507765] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.507788] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_5 because it has no selected transport resources
[1763745250.507793] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_5: md=0xac78d10 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.508125] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.508127] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_5
[1763745250.508129] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.508130] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.508159] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31a00 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.513469] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_6) failed: 95
[1763745250.514289] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_6: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.519131] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_6: PF sysfs path is '/sys/devices/pci0000:97/0000:97:01.0/0000:98:00.0/0000:99:03.0/0000:9d:00.0'
[1763745250.519155] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 8 for bus id 9d:00.0
[1763745250.519157] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_6: bdf_name 0000:9d:00.0 sys_dev 8
[1763745250.519166] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_6: vendor_id 0x15b3 device_id 4129
[1763745250.519708] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_6: mkey_by_name_reserve is not supported
[1763745250.519709] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_6: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.519831] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_6: ODP is supported, version 2: memory=host
[1763745250.519976] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31730 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.520031] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.520033] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_6' (InfiniBand channel adapter) with 1 ports
[1763745250.520038] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.520042] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.520045] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.520051] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_6: dmabuf is supported
[1763745250.520053] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.520258] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_6: opened DEVX md log_max_qp=17
[1763745250.520887] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_id.c:140  UCX  DEBUG mlx5_5: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.500527] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_5, syndrome 0x172df6: Remote I/O error
[1763745250.500528] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_5: XGVMI is not supported
[1763745250.500529] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_5: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.507829] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.507855] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_5 because it has no selected transport resources
[1763745250.507862] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_5: md=0xa263920 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.508142] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.508144] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_5
[1763745250.508146] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.508148] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.508192] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25ceb0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.513563] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_6) failed: 95
[1763745250.514786] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_6: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.519695] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_6: PF sysfs path is '/sys/devices/pci0000:97/0000:97:01.0/0000:98:00.0/0000:99:03.0/0000:9d:00.0'
[1763745250.519720] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 8 for bus id 9d:00.0
[1763745250.519721] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_6: bdf_name 0000:9d:00.0 sys_dev 8
[1763745250.519732] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_6: vendor_id 0x15b3 device_id 4129
[1763745250.520242] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_6: mkey_by_name_reserve is not supported
[1763745250.520243] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_6: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.520368] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_6: ODP is supported, version 2: memory=host
[1763745250.520508] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa265b40 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.520581] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.520582] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_6' (InfiniBand channel adapter) with 1 ports
[1763745250.520589] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.520593] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.520597] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_6: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.520604] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_6: dmabuf is supported
[1763745250.520606] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.520814] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_6: opened DEVX md log_max_qp=17
[1763745250.521293] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkendex 0x0
[1763745250.521164] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.521821] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_6: relaxed order memory access is disabled
[1763745250.522137] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.522243] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_6, syndrome 0x172df6: Remote I/O error
[1763745250.522245] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_6: XGVMI is not supported
[1763745250.522246] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_6: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.523345] [h001:2082100:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x10
[1763745250.523347] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query rc_verbs resources: No such device
[1763745250.523348] [h001:2082100:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x0
[1763745250.523349] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query ud_verbs resources: No such device
[1763745250.523350] [h001:2082100:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0xd4
[1763745250.523351] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query dc_mlx5 resources: No such device
[1763745250.523351] [h001:2082100:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x14
[1763745250.523352] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query rc_mlx5 resources: No such device
[1763745250.523353] [h001:2082100:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x4
[1763745250.523354] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query ud_mlx5 resources: No such device
[1763745250.527351] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.527352] [h001:2082100:0]     ucp_context.c:1246 UCX  DEBUG No tl resources found for md mlx5_6
[1763745250.527354] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_6 because it has no selected transport resources
[1763745250.527359] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_6: md=0xac78d10 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.528133] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.528134] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_6
[1763745250.528136] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31730 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.528138] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31730 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.528168] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31730 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.532554] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_7) failed: 95
[1763745250.533336] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_7: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.538783] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_7: PF sysfs path is '/sys/devices/pci0000:b7/0000:b7:01.0/0000:b8:00.0/0000:b9:02.0/0000:bc:00.0'
[1763745250.538805] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 9 for bus id bc:00.0
[1763745250.538807] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_7: bdf_name 0000:bc:00.0 sys_dev 9
[1763745250.538816] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_7: vendor_id 0x15b3 device_id 4129
[1763745250.539382] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_7: mkey_by_name_reserve is not suppory_index 0x0
[1763745250.521545] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.522164] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_6: relaxed order memory access is disabled
[1763745250.522522] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_6: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.522617] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_6, syndrome 0x172df6: Remote I/O error
[1763745250.522618] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_6: XGVMI is not supported
[1763745250.522619] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_6: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.523987] [h001:2082112:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x10
[1763745250.523988] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query rc_verbs resources: No such device
[1763745250.523990] [h001:2082112:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x0
[1763745250.523990] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query ud_verbs resources: No such device
[1763745250.523992] [h001:2082112:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0xd4
[1763745250.523992] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query dc_mlx5 resources: No such device
[1763745250.523993] [h001:2082112:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x14
[1763745250.523994] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query rc_mlx5 resources: No such device
[1763745250.523995] [h001:2082112:0]       ib_device.c:1272 UCX  DEBUG no compatible IB ports found for flags 0x4
[1763745250.523996] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query ud_mlx5 resources: No such device
[1763745250.528083] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.528085] [h001:2082112:0]     ucp_context.c:1246 UCX  DEBUG No tl resources found for md mlx5_6
[1763745250.528086] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_6 because it has no selected transport resources
[1763745250.528091] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_6: md=0xa263f00 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.528430] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.528431] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_6
[1763745250.528433] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa265b40 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.528434] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa265b40 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.528474] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa265b40 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.533292] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_7) failed: 95
[1763745250.534386] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_7: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.538877] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_7: PF sysfs path is '/sys/devices/pci0000:b7/0000:b7:01.0/0000:b8:00.0/0000:b9:02.0/0000:bc:00.0'
[1763745250.538902] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 9 for bus id bc:00.0
[1763745250.538903] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_7: bdf_name 0000:bc:00.0 sys_dev 9
[1763745250.538913] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_7: vendor_id 0x15b3 device_id 4129
[1763745250.539434] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_7: mkey_by_name_reserve is not supported
[1763745250.539441] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_7: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.539575] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_7: ODP is supported, version 2: memory=host
[1763745250.539724] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.539797] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.539798] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_7' (InfiniBand channel adapter) with 1 ports
[1763745250.539805] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.539808] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.539812] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.539818] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_7: dmabuf is supported
[1763745250.539820] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.540118] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_7: opened DEVX md log_max_qp=17
[1763745250.540990] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.541259] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.542275] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_7: relaxed order memory access is disabled
[1763745250.542579] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.542811] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_7, syndrome 0x172df6: Remote I/O error
[1763745250.542813] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_7: XGVMI is not supported
[1763745250.542814] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_7: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.549544] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.549569] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_7 because it has no selected transport resources
[1763745250.549575] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_7: md=0xa263e30 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.550197] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.550198] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_7
[1763745250.550200] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.550202] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa25ceb0 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.550245] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25ceb0 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.554778] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_8) failed: 95
[1763745250.555564] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_8: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.560917] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_8: PF sysfs path is '/sys/devices/pci0000:c7/0000:c7:01.0/0000:c8:00.0/0000:c9:02.0/0000:cc:00.0'
[1763745250.560941] [h001:2082112:0]            topo.c:304  UCX  ted
[1763745250.539387] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_7: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.539535] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_7: ODP is supported, version 2: memory=host
[1763745250.539686] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.539751] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.539753] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_7' (InfiniBand channel adapter) with 1 ports
[1763745250.539759] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.539762] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.539765] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_7: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.539771] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_7: dmabuf is supported
[1763745250.539773] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.540064] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_7: opened DEVX md log_max_qp=17
[1763745250.541052] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.541310] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.542236] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_7: relaxed order memory access is disabled
[1763745250.542518] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_7: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.542814] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_7, syndrome 0x172df6: Remote I/O error
[1763745250.542815] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_7: XGVMI is not supported
[1763745250.542816] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_7: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.550017] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.550040] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_7 because it has no selected transport resources
[1763745250.550046] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_7: md=0xac78d10 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.550336] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.550338] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_7
[1763745250.550340] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.550341] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31a00 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.550371] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31a00 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.555520] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_8) failed: 95
[1763745250.556603] [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_8: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.561042] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_8: PF sysfs path is '/sys/devices/pci0000:c7/0000:c7:01.0/0000:c8:00.0/0000:c9:02.0/0000:cc:00.0'
[1763745250.561064] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 10 for bus id cc:00.0
[1763745250.561069] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_8: bdf_name 0000:cc:00.0 sys_dev 10
[1763745250.561079] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_8: vendor_id 0x15b3 device_id 4129
[1763745250.561590] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_8: mkey_by_name_reserve is not supported
[1763745250.561591] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_8: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.561722] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_8: ODP is supported, version 2: memory=host
[1763745250.561872] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac31860 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.561929] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.561930] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_8' (InfiniBand channel adapter) with 1 ports
[1763745250.561936] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.561940] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.561943] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.561948] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_8: dmabuf is supported
[1763745250.561950] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.562279] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_8: opened DEVX md log_max_qp=17
[1763745250.563131] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.563388] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.564257] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_8: relaxed order memory access is disabled
[1763745250.564535] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.564825] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_8, syndrome 0x172df6: Remote I/O error
[1763745250.564826] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_8: XGVMI is not supported
[1763745250.564827] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_8: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.571254] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.571277] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_8 because it has no selected transport resources
[1763745250.571283] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_8: md=0xac7e8e0 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.571914] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.571915] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_8
[1763745250.571917] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac31860 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.571919] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac31860 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.571949] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac31860 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.576460] [h001:2082100:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_9) failed: 95
[1763745250.577248]DEBUG added sys_dev 10 for bus id cc:00.0
[1763745250.560947] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_8: bdf_name 0000:cc:00.0 sys_dev 10
[1763745250.560957] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_8: vendor_id 0x15b3 device_id 4129
[1763745250.561525] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_8: mkey_by_name_reserve is not supported
[1763745250.561527] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_8: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.561677] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_8: ODP is supported, version 2: memory=host
[1763745250.561837] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa265700 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.561911] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.561913] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_8' (InfiniBand channel adapter) with 1 ports
[1763745250.561919] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.561922] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.561926] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_8: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.561932] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_8: dmabuf is supported
[1763745250.561934] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.562231] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_8: opened DEVX md log_max_qp=17
[1763745250.563191] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.563437] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.564271] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_8: relaxed order memory access is disabled
[1763745250.564594] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_8: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.564826] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_8, syndrome 0x172df6: Remote I/O error
[1763745250.564828] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_8: XGVMI is not supported
[1763745250.564829] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_8: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.571753] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.571780] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_8 because it has no selected transport resources
[1763745250.571785] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_8: md=0xa26d0d0 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.572068] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.572069] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_8
[1763745250.572072] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa265700 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.572073] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa265700 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.572116] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa265700 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.577203] [h001:2082112:0]       ib_efa_md.c:39   UCX  DEBUG efadv_query_device(mlx5_9) failed: 95
[1763745250.578297] [h001:2082112:0]           ib_md.c:1058 UCX  DEBUG mlx5_9: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.582755] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_9: PF sysfs path is '/sys/devices/pci0000:d7/0000:d7:01.0/0000:d8:00.0/0000:d9:02.0/0000:dc:00.0'
[1763745250.582783] [h001:2082112:0]            topo.c:304  UCX  DEBUG added sys_dev 11 for bus id dc:00.0
[1763745250.582784] [h001:2082112:0]            topo.c:560  UCX  DEBUG mlx5_9: bdf_name 0000:dc:00.0 sys_dev 11
[1763745250.582794] [h001:2082112:0]       ib_device.c:535  UCX  DEBUG mlx5_9: vendor_id 0x15b3 device_id 4129
[1763745250.583325] [h001:2082112:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_9: mkey_by_name_reserve is not supported
[1763745250.583326] [h001:2082112:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_9: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.583463] [h001:2082112:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_9: ODP is supported, version 2: memory=host
[1763745250.583632] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa25c070 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.583715] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.583717] [h001:2082112:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_9' (InfiniBand channel adapter) with 1 ports
[1763745250.583722] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.583726] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.583730] [h001:2082112:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.583737] [h001:2082112:0]           ib_md.c:1244 UCX  DEBUG mlx5_9: dmabuf is supported
[1763745250.583738] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.584051] [h001:2082112:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_9: opened DEVX md log_max_qp=17
[1763745250.584945] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM dm memory registration status "Success" range 0x15126e88c000..0x15126e88c020 iova 0x0 mkey_index 0x0
[1763745250.585208] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x15126e88c000 atomic mkey_index 0x0
[1763745250.586179] [h001:2082112:0]           ib_md.c:1202 UCX  DEBUG mlx5_9: relaxed order memory access is disabled
[1763745250.586461] [h001:2082112:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM flush-mr memory registration status "Success" range 0xa266000..0xa266008 iova 0x0 mkey_index 0x0
[1763745250.586757] [h001:2082112:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_9, syndrome 0x172df6: Remote I/O error
[1763745250.586758] [h001:2082112:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_9: XGVMI is not supported
[1763745250.586759] [h001:2082112:0]           ib_md.c:1062 UCX  DEBUG mlx5_9: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.593599] [h001:2082112:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.593625] [h001:2082112:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_9 because it has no selected transport resources
[1763745250.593631] [h001:2082112:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_9: md=0xa26f110 md->flags=0x3f51f7f flush_rkey=0x1fff00
[1763745250.594278] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.594280] [h001:2082112:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_9
[1763745250.594282] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa25c070 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.594284] [h001:2082112:0]      [h001:2082100:0]           ib_md.c:1058 UCX  DEBUG mlx5_9: md open by 'uct_ib_efa_md_ops' failed, trying next
[1763745250.582700] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/infiniband/mlx5_9: PF sysfs path is '/sys/devices/pci0000:d7/0000:d7:01.0/0000:d8:00.0/0000:d9:02.0/0000:dc:00.0'
[1763745250.582721] [h001:2082100:0]            topo.c:304  UCX  DEBUG added sys_dev 11 for bus id dc:00.0
[1763745250.582722] [h001:2082100:0]            topo.c:560  UCX  DEBUG mlx5_9: bdf_name 0000:dc:00.0 sys_dev 11
[1763745250.582733] [h001:2082100:0]       ib_device.c:535  UCX  DEBUG mlx5_9: vendor_id 0x15b3 device_id 4129
[1763745250.583295] [h001:2082100:0]    ib_mlx5dv_md.c:1953 UCX  DEBUG mlx5_9: mkey_by_name_reserve is not supported
[1763745250.583297] [h001:2082100:0]    ib_mlx5dv_md.c:1936 UCX  DEBUG mlx5_9: dp_ordering support: force=1 ooo_rw_rc=1 ooo_rw_dc=1
[1763745250.583456] [h001:2082100:0]    ib_mlx5dv_md.c:1705 UCX  DEBUG mlx5_9: ODP is supported, version 2: memory=host
[1763745250.583633] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac79250 [id=53 ref 1] uct_ib_handle_async_event() to hash
[1763745250.583690] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.583692] [h001:2082100:0]       ib_device.c:646  UCX  DEBUG initialized device 'mlx5_9' (InfiniBand channel adapter) with 1 ports
[1763745250.583697] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: cuda GPUDirect RDMA is not detected by checking /sys/kernel/mm/memory_peers/nv_mem/version
[1763745250.583700] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: cuda GPUDirect RDMA is detected by checking /sys/module/nvidia_peermem/version
[1763745250.583703] [h001:2082100:0]           ib_md.c:1217 UCX  DEBUG mlx5_9: rocm GPUDirect RDMA is not detected by checking /dev/kfd
[1763745250.583709] [h001:2082100:0]           ib_md.c:1244 UCX  DEBUG mlx5_9: dmabuf is supported
[1763745250.583711] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1763745250.584001] [h001:2082100:0]    ib_mlx5dv_md.c:2444 UCX  DEBUG mlx5_9: opened DEVX md log_max_qp=17
[1763745250.585007] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM dm memory registration status "Success" range 0x14ea74000000..0x14ea74000020 iova 0x0 mkey_index 0x0
[1763745250.585257] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM atomic-key memory registration status "Success" range (nil)..0x20 iova 0x14ea74000000 atomic mkey_index 0x0
[1763745250.586208] [h001:2082100:0]           ib_md.c:1202 UCX  DEBUG mlx5_9: relaxed order memory access is disabled
[1763745250.586523] [h001:2082100:0]    ib_mlx5dv_md.c:140  UCX  DEBUG mlx5_9: KSM flush-mr memory registration status "Success" range 0xac37000..0xac37008 iova 0x0 mkey_index 0x0
[1763745250.586754] [h001:2082100:0]         ib_mlx5.h:998  UCX  DEBUG mlx5dv_devx_general_cmd(ALLOW_OTHER_VHCA_ACCESS) failed on mlx5_9, syndrome 0x172df6: Remote I/O error
[1763745250.586755] [h001:2082100:0]    ib_mlx5dv_md.c:2497 UCX  DEBUG mlx5_9: XGVMI is not supported
[1763745250.586757] [h001:2082100:0]           ib_md.c:1062 UCX  DEBUG mlx5_9: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1763745250.594082] [h001:2082100:0]          uct_md.c:96   UCX  DEBUG failed to query srd resources: No such device
[1763745250.594106] [h001:2082100:0]     ucp_context.c:1661 UCX  DEBUG closing md mlx5_9 because it has no selected transport resources
[1763745250.594111] [h001:2082100:0]    ib_mlx5dv_md.c:2533 UCX  DEBUG mlx5_9: md=0xac7e8e0 md->flags=0x3f51f7f flush_rkey=0x200000
[1763745250.594381] [h001:2082100:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1763745250.594382] [h001:2082100:0]       ib_device.c:667  UCX  DEBUG destroying ib device mlx5_9
[1763745250.594384] [h001:2082100:0]           async.c:172  UCX  DEBUG removed async handler 0xac79250 [id=53 ref 1] uct_ib_handle_async_event() from hash
[1763745250.594386] [h001:2082100:0]           async.c:575  UCX  DEBUG removing async handler 0xac79250 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.594429] [h001:2082100:0]           async.c:187  UCX  DEBUG release async handler 0xac79250 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.640275] [h001:2082100:0]     ucp_context.c:1784 UCX  DEBUG register host memory on: self, cuda_cpy, knem
[1763745250.640278] [h001:2082100:0]     ucp_context.c:1784 UCX  DEBUG register cuda memory on: cuda_cpy, cuda_ipc
[1763745250.640279] [h001:2082100:0]     ucp_context.c:1784 UCX  DEBUG register cuda-managed memory on: cuda_cpy
[1763745250.640280] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rocm memory
[1763745250.640281] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rocm-managed memory
[1763745250.640282] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rdma memory
[1763745250.640283] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-host memory
[1763745250.640283] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-device memory
[1763745250.640284] [h001:2082100:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-managed memory
[1763745250.640307] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool rcache_mp: align 8, maxelems 4294967295, elemsize 144
[1763745250.640897] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac793c0 [id=53 ref 1] ucs_mem_region_destroy_internal() to hash
[1763745250.640966] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.641087] [h001:2082100:0]          module.c:304  UCX  DEBUG loading modules for ucm
[1763745250.712768] [h001:2082100:0]     ucp_context.c:2412 UCX  DEBUG created ucp context ucp_context_0 0xac0fba0 [8 mds 9 tls] features 0x5e tl bitmap 0x1ff 0x0
[1763745250.712833] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool self_msg_desc: align 64, maxelems 4294967295, elemsize 8200
[1763745250.712837] [h001:2082100:0]            self.c:247  UCX  DEBUG created self iface id 0x3f65c28911702501 send_size 8192
[1763745250.712848] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[0]=0xac7e0d0 using self/memory on worker 0xac46150
[1763745250.712873] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: align 64, maxelems 4294967295, elemsize 8205
[1763745250.712875] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: align 64, maxelems 4294967295, elemsize 131090
[1763745250.713960] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac78140 [id=61 ref 1] uct_tcp_query_devices() to hash
[1763745250.713970] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 61 events 0x5 mode thread_spinlock
[1763745250.713975] [h001:2082100:0]       tcp_iface.c:613  UCX  DEBUG tcp_iface 0xac7e900: listening for connections (fd=61) on 172.18.49.211:50895 netif ibp27s0
[1763745250.714141] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.714675] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[1]=0xac7e900 using tcp/ibp27s0 on worker 0xac46150
[1763745250.714696] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: align 64, maxelems 4294967295, elemsize 8205
[1763745250.714698] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: align 64, maxelems 4294967295, elemsize 131090
[1763745250.714886] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac2ef80 [id=63 ref 1] uct_tcp_query_devices() to hash
[1763745250.714893] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 63 events 0x5 mode thread_spinlock
[1763745250.714895] [h001      async.c:575  UCX  DEBUG removing async handler 0xa25c070 [id=53 ref 1] uct_ib_handle_async_event()
[1763745250.594330] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa25c070 [id=53 ref 0] uct_ib_handle_async_event()
[1763745250.639378] [h001:2082112:0]     ucp_context.c:1784 UCX  DEBUG register host memory on: self, cuda_cpy, knem
[1763745250.639382] [h001:2082112:0]     ucp_context.c:1784 UCX  DEBUG register cuda memory on: cuda_cpy, cuda_ipc
[1763745250.639383] [h001:2082112:0]     ucp_context.c:1784 UCX  DEBUG register cuda-managed memory on: cuda_cpy
[1763745250.639384] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rocm memory
[1763745250.639385] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rocm-managed memory
[1763745250.639386] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering rdma memory
[1763745250.639386] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-host memory
[1763745250.639387] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-device memory
[1763745250.639388] [h001:2082112:0]     ucp_context.c:1772 UCX  DEBUG no memory domain supports registering ze-managed memory
[1763745250.639420] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool rcache_mp: align 8, maxelems 4294967295, elemsize 144
[1763745250.640069] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa265700 [id=53 ref 1] ucs_mem_region_destroy_internal() to hash
[1763745250.640158] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 53 events 0x1 mode thread_spinlock
[1763745250.640298] [h001:2082112:0]          module.c:304  UCX  DEBUG loading modules for ucm
[1763745250.712783] [h001:2082112:0]     ucp_context.c:2412 UCX  DEBUG created ucp context ucp_context_0 0xa1f29c0 [8 mds 9 tls] features 0x5e tl bitmap 0x1ff 0x0
[1763745250.712865] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool self_msg_desc: align 64, maxelems 4294967295, elemsize 8200
[1763745250.712871] [h001:2082112:0]            self.c:247  UCX  DEBUG created self iface id 0xdd4760e22d053e71 send_size 8192
[1763745250.712882] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[0]=0xa261b10 using self/memory on worker 0xa216100
[1763745250.712911] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: align 64, maxelems 4294967295, elemsize 8205
[1763745250.712913] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: align 64, maxelems 4294967295, elemsize 131090
[1763745250.714204] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa259d40 [id=61 ref 1] uct_tcp_query_devices() to hash
[1763745250.714216] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 61 events 0x5 mode thread_spinlock
[1763745250.714222] [h001:2082112:0]       tcp_iface.c:613  UCX  DEBUG tcp_iface 0xa26e710: listening for connections (fd=61) on 172.18.49.211:49879 netif ibp27s0
[1763745250.714420] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.714899] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[1]=0xa26e710 using tcp/ibp27s0 on worker 0xa216100
[1763745250.714920] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: align 64, maxelems 4294967295, elemsize 8205
[1763745250.714922] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: align 64, maxelems 4294967295, elemsize 131090
[1763745250.715081] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa211da0 [id=63 ref 1] uct_tcp_query_devices() to hash
[1763745250.715088] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 63 events 0x5 mode thread_spinlock
[1763745250.715091] [h001:2082112:0]       tcp_iface.c:613  UCX  DEBUG tcp_iface 0xa26f110: listening for connections (fd=63) on 127.0.0.1:52331 netif lo
[1763745250.715111] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.715115] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.715151] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.715152] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.715168] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[2]=0xa26f110 using tcp/lo on worker 0xa216100
[1763745250.715239] [h001:2082112:0]         mm_sysv.c:97   UCX  DEBUG   mm failed to allocate 33023 bytes with hugetlb
[1763745250.715277] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool mm_recv_desc: align 64, maxelems 4294967295, elemsize 8368
[1763745250.715285] [h001:2082112:0]         mm_sysv.c:97   UCX  DEBUG   mm failed to allocate 4292720 bytes with hugetlb
[1763745250.715295] [h001:2082112:0]           mpool.c:281  UCX  DEBUG mpool mm_recv_desc: allocated chunk 0x15103d040018 of 4296680 bytes with 512 elements
[1763745250.716267] [h001:2082112:0]        mm_iface.c:734  UCX  DEBUG created mm iface 0xa26faa0 FIFO id 0x1b0038 va 0x15103d459000 size 36864 (128 x 256 elems)
[1763745250.716292] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[3]=0xa26faa0 using sysv/memory on worker 0xa216100
[1763745250.716367] [h001:2082112:0]        mm_posix.c:607  UCX  DEBUG   allocated posix shared memory at 0x15103d037000 length 36864
[1763745250.716377] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool mm_recv_desc: align 64, maxelems 4294967295, elemsize 8368
[1763745250.717572] [h001:2082112:0]        mm_posix.c:373  UCX  DEBUG   shared memory mmap(addr=(nil), length=6291456, flags= HUGETLB, fd=67) failed: Invalid argument
[1763745250.717577] [h001:2082112:0]        mm_posix.c:607  UCX  DEBUG   allocated posix shared memory at 0x15103cc1e000 length 4296704
[1763745250.717582] [h001:2082112:0]           mpool.c:281  UCX  DEBUG mpool mm_recv_desc: allocated chunk 0x15103cc1e018 of 4296680 bytes with 512 elements
[1763745250.718017] [h001:2082112:0]        mm_iface.c:734  UCX  DEBUG created mm iface 0xa25f3b0 FIFO id 0xc0000010401fc540 va 0x15103d037000 size 36864 (128 x 256 elems)
[1763745250.718041] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[4]=0xa25f3b0 using posix/memory on worker 0xa216100
[1763745250.718066] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[5]=0xa2158f0 using cuda_copy/cuda on worker 0xa216100
[1763745250.719803] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[6]=0xa212900 using cuda_ipc/cuda on worker 0xa216100
[1763745250.719829] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_scopy_iface_tx_mp: align 64, maxelems 4294967295, elemsize 736
[1763745250.719835] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[7]=0xa26d0d0 using cma/memory on worker 0xa216100
[1763745250.719850] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool uct_scopy_iface_tx_mp: align 64, maxelems 4294967295, elemsize 736
[1763745250.719854] [h001:2082112:0]      ucp_worker.c:1433 UCX  DEBUG created interface[8]=0xa26d620 using knem/memory on worker 0xa216100
[1763745250.719860] [h001:2082112:0]      ucp_worker.c:1150 UCX  DEBUG selected scalable tl bitmap: 0x1ff 0x0 (9 tls)
[1763745250.720352] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa211b70 [id=60 ref 1] ucp_worker_iface_activate() to hash
[1763745250.720362] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 60 events 0x0 mode thread_spinlock
[1763745250.720509] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.720687] [h00:2082100:0]       tcp_iface.c:613  UCX  DEBUG tcp_iface 0xac423f0: listening for connections (fd=63) on 127.0.0.1:50291 netif lo
[1763745250.714913] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.714916] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.714951] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.714952] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.714974] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[2]=0xac423f0 using tcp/lo on worker 0xac46150
[1763745250.715047] [h001:2082100:0]         mm_sysv.c:97   UCX  DEBUG   mm failed to allocate 33023 bytes with hugetlb
[1763745250.715079] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool mm_recv_desc: align 64, maxelems 4294967295, elemsize 8368
[1763745250.715085] [h001:2082100:0]         mm_sysv.c:97   UCX  DEBUG   mm failed to allocate 4292720 bytes with hugetlb
[1763745250.715096] [h001:2082100:0]           mpool.c:281  UCX  DEBUG mpool mm_recv_desc: allocated chunk 0x14ea4ade5018 of 4296680 bytes with 512 elements
[1763745250.716123] [h001:2082100:0]        mm_iface.c:734  UCX  DEBUG created mm iface 0xac42b70 FIFO id 0x1b0036 va 0x14ea6e26d000 size 36864 (128 x 256 elems)
[1763745250.716148] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[3]=0xac42b70 using sysv/memory on worker 0xac46150
[1763745250.716223] [h001:2082100:0]        mm_posix.c:607  UCX  DEBUG   allocated posix shared memory at 0x14ea6e264000 length 36864
[1763745250.716232] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool mm_recv_desc: align 64, maxelems 4294967295, elemsize 8368
[1763745250.717562] [h001:2082100:0]        mm_posix.c:373  UCX  DEBUG   shared memory mmap(addr=(nil), length=6291456, flags= HUGETLB, fd=67) failed: Invalid argument
[1763745250.717571] [h001:2082100:0]        mm_posix.c:607  UCX  DEBUG   allocated posix shared memory at 0x14ea4a9cc000 length 4296704
[1763745250.717576] [h001:2082100:0]           mpool.c:281  UCX  DEBUG mpool mm_recv_desc: allocated chunk 0x14ea4a9cc018 of 4296680 bytes with 512 elements
[1763745250.718041] [h001:2082100:0]        mm_iface.c:734  UCX  DEBUG created mm iface 0xac7c3b0 FIFO id 0xc0000010401fc534 va 0x14ea6e264000 size 36864 (128 x 256 elems)
[1763745250.718048] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[4]=0xac7c3b0 using posix/memory on worker 0xac46150
[1763745250.718088] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[5]=0xac7cc70 using cuda_copy/cuda on worker 0xac46150
[1763745250.720464] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[6]=0xac32d40 using cuda_ipc/cuda on worker 0xac46150
[1763745250.720489] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_scopy_iface_tx_mp: align 64, maxelems 4294967295, elemsize 736
[1763745250.720493] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[7]=0xac0f2e0 using cma/memory on worker 0xac46150
[1763745250.720508] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool uct_scopy_iface_tx_mp: align 64, maxelems 4294967295, elemsize 736
[1763745250.720511] [h001:2082100:0]      ucp_worker.c:1433 UCX  DEBUG created interface[8]=0xac7d210 using knem/memory on worker 0xac46150
[1763745250.720517] [h001:2082100:0]      ucp_worker.c:1150 UCX  DEBUG selected scalable tl bitmap: 0x1ff 0x0 (9 tls)
[1763745250.721016] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac2bab0 [id=60 ref 1] ucp_worker_iface_activate() to hash
[1763745250.721024] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 60 events 0x0 mode thread_spinlock
[1763745250.721173] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721364] [h001:21:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.720844] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.720999] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721232] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721444] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721615] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721784] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721952] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722120] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722290] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722459] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722628] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722798] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722964] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723133] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723196] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa20e590 [id=62 ref 1] ucp_worker_iface_activate() to hash
[1763745250.723201] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 62 events 0x0 mode thread_spinlock
[1763745250.723207] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723209] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723238] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723240] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723253] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723255] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723274] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723275] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723342] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723346] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723382] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723383] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723395] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723396] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723420] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723421] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723433] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723435] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723456] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723457] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723514] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723516] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723553] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723554] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723565] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723567] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723591] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723592] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723602] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723604] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723624] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723625] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723691] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723693] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723730] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723731] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723742] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723744] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723765] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723766] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723775] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723777] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723796] [h001:2082112:0]         082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721535] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721702] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.721868] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722029] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722193] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722360] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722534] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722698] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.722873] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723035] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723207] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723378] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723554] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723731] [h001:2082100:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.723792] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac2b770 [id=62 ref 1] ucp_worker_iface_activate() to hash
[1763745250.723796] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 62 events 0x0 mode thread_spinlock
[1763745250.723801] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723804] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723850] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723851] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723865] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723867] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723919] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723920] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723933] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723937] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723994] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723995] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724008] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724010] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724054] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724055] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724067] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724069] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724108] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724109] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724121] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724123] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724142] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724143] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724153] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724155] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724173] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724174] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724186] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724187] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724206] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724207] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724219] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724221] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724240] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724241] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724251] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724252] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724271] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724272] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724283] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724284] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724303] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724306] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724316] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724317] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724335] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724336] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724346] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724348] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724366] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724367] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724377] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724379] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724402] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724402] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724412] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724414] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724433] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724434] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724445] [h001:2082100:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724447] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724465] [h001:2082100:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724466] [h001:2082100:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724476] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac2cb60 [id=64 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724481] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 64 events 0x0 mode thread_spinlock
[1763745250.724487] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac1dad0 [id=66 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724491] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 66 events 0x0 mode thread_spinlock
[1763745250.724497] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac32a90 [id=68 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724500] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 68 events 0x0 mode thread_spinlock
[1763745250.724503] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac79250 [id=69 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724505] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 69 events 0x0 mode thread_spinlock
[1763745250.726981] [h001:2082100:0]           async.c:247  UCX  DEBUG added async handler 0xac2d9d0 [id=70 ref 1] uct_rdmacm_cm_get_device_context() to hash
[1763745250.726986] [h001:2082100:0]           async.c:521  UCX  DEBUG listening to async event fd 70 events 0x1 mode thread_spinlock
[1763745250.726992] [h001:2082100:0]       rdmacm_cm.c:981  UCX  DEBUG created rdmac   topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723799] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723811] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723813] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723854] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723854] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723867] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723869] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723922] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723923] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.723937] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.723939] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.723994] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.723994] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724006] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724008] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724046] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724047] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724059] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.724061] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.724100] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745250.724101] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745250.724112] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa20f980 [id=64 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724117] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 64 events 0x0 mode thread_spinlock
[1763745250.724124] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa2008f0 [id=66 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724127] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 66 events 0x0 mode thread_spinlock
[1763745250.724134] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa2158b0 [id=68 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724137] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 68 events 0x0 mode thread_spinlock
[1763745250.724140] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa204670 [id=69 ref 1] ucp_worker_iface_activate() to hash
[1763745250.724142] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 69 events 0x0 mode thread_spinlock
[1763745250.727005] [h001:2082112:0]           async.c:247  UCX  DEBUG added async handler 0xa210830 [id=70 ref 1] uct_rdmacm_cm_get_device_context() to hash
[1763745250.727011] [h001:2082112:0]           async.c:521  UCX  DEBUG listening to async event fd 70 events 0x1 mode thread_spinlock
[1763745250.727017] [h001:2082112:0]       rdmacm_cm.c:981  UCX  DEBUG created rdm_cm 0xac7d770 with event_channel 0xac433e0 (fd=70)
[1763745250.727007] [h001:2082100:0]      tcp_sockcm.c:225  UCX  DEBUG created tcp_sockcm 0xac75de0
[1763745250.727130] [h001:2082100:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x14ea6e210000 to <no debug data> mem_type_ep:cuda
[1763745250.727250] [h001:2082100:0]          wireup.c:1267 UCX  DEBUG   ep 0x14ea6e210000: am_lane <none> wireup_msg_lane <none> cm_lane <none> keepalive_lane <none> reachable_mds 0x10
[1763745250.727254] [h001:2082100:0]          wireup.c:1290 UCX  DEBUG   ep 0x14ea6e210000: lane[0]:  5:cuda_copy/cuda.0 md[4]        -> addr[0].md[4]/cuda_cpy/sysdev[0] seg 0 rma_bw#0
[1763745250.727255] [h001:2082100:0]          wireup.c:1293 UCX  DEBUG   ep 0x14ea6e210000: err mode 0, flags 0x1
[1763745250.727279] [h001:2082100:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x14ea6e210058 to <no debug data> mem_type_ep:cuda-managed
[1763745250.727293] [h001:2082100:0]          wireup.c:1267 UCX  DEBUG   ep 0x14ea6e210058: am_lane <none> wireup_msg_lane <none> cm_lane <none> keepalive_lane <none> reachable_mds 0x10
[1763745250.727296] [h001:2082100:0]          wireup.c:1290 UCX  DEBUG   ep 0x14ea6e210058: lane[0]:  5:cuda_copy/cuda.0 md[4]        -> addr[0].md[4]/cuda_cpy/sysdev[0] seg 0 rma_bw#0
[1763745250.727297] [h001:2082100:0]          wireup.c:1293 UCX  DEBUG   ep 0x14ea6e210058: err mode 0, flags 0x1
[1763745250.727299] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_requests: align 64, maxelems 4294967295, elemsize 312
[1763745250.727300] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_rkeys: align 64, maxelems 4294967295, elemsize 112
[1763745250.727302] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_reg_bufs: align 64, maxelems 4294967295, elemsize 8216
[1763745250.727306] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 153
[1763745250.727307] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 1113
[1763745250.727308] [h001:2082100:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 65625
[1763745250.727310] [h001:2082100:0]       mpool_set.c:129  UCX  DEBUG mpool_set:ucp_am_bufs, sizes map 0x80000440, largest size 65536, mpools num 3
[1763745250.727316] [h001:2082100:0]      ucp_worker.c:1631 UCX  DEBUG worker 0xac46150: using cpu atomics
[1763745250.727345] [h001:2082100:0]          parser.c:2368 UCX  INFO  UCX_* env variables: UCX_TLS=cuda_ipc,cuda_copy,sm,tcp,self UCX_LOG_LEVEL=debug UCX_PROTO_ENABLE=n
[1763745250.727567] [h001:2082100:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x14ea6e2100b0 to <no debug data> from api call
[1763745250.727718] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.727909] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.727985] [h001:2082100:0]            sock.c:90   UCX  DEBUG   ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.727988] [h001:2082100:0]         tcp_net.c:61   UCX  DEBUG   speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.728039] [h001:2082100:0]            topo.c:935  UCX  DEBUG   /sys/class/net/lo: sysfs path undetected
[1763745250.728040] [h001:2082100:0]            topo.c:888  UCX  DEBUG   lo: pci bandwidth undetected, using maximal value
[1763745250.728078] [h001:2082100:0]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 self cfg#1 rma_am(tcp/ibp27s0)  amo_am(tcp/ibp27s0)  am(tcp/ibp27s0)  ka(tcp/ibp27s0)
[1763745250.728080] [h001:2082100:0]          wireup.c:1267 UCX  DEBUG   ep 0x14ea6e2100b0: am_lane 0 wireup_msg_lane 0 cm_lane <none> keepalive_lane 0 reachable_mds 0xdf
[1763745250.728084] [h001:2082100:0]          wireup.c:1290 UCX  DEBUG   ep 0x14ea6e2100b0: lane[0]:  1:tcp/ibp27s0.0 md[macm_cm 0xa1f10f0 with event_channel 0xa202850 (fd=70)
[1763745250.727033] [h001:2082112:0]      tcp_sockcm.c:225  UCX  DEBUG created tcp_sockcm 0xa1f1660
[1763745250.727145] [h001:2082112:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x15103cbd1000 to <no debug data> mem_type_ep:cuda
[1763745250.727261] [h001:2082112:0]          wireup.c:1267 UCX  DEBUG   ep 0x15103cbd1000: am_lane <none> wireup_msg_lane <none> cm_lane <none> keepalive_lane <none> reachable_mds 0x10
[1763745250.727265] [h001:2082112:0]          wireup.c:1290 UCX  DEBUG   ep 0x15103cbd1000: lane[0]:  5:cuda_copy/cuda.0 md[4]        -> addr[0].md[4]/cuda_cpy/sysdev[1] seg 0 rma_bw#0
[1763745250.727267] [h001:2082112:0]          wireup.c:1293 UCX  DEBUG   ep 0x15103cbd1000: err mode 0, flags 0x1
[1763745250.727289] [h001:2082112:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x15103cbd1058 to <no debug data> mem_type_ep:cuda-managed
[1763745250.727303] [h001:2082112:0]          wireup.c:1267 UCX  DEBUG   ep 0x15103cbd1058: am_lane <none> wireup_msg_lane <none> cm_lane <none> keepalive_lane <none> reachable_mds 0x10
[1763745250.727305] [h001:2082112:0]          wireup.c:1290 UCX  DEBUG   ep 0x15103cbd1058: lane[0]:  5:cuda_copy/cuda.0 md[4]        -> addr[0].md[4]/cuda_cpy/sysdev[1] seg 0 rma_bw#0
[1763745250.727306] [h001:2082112:0]          wireup.c:1293 UCX  DEBUG   ep 0x15103cbd1058: err mode 0, flags 0x1
[1763745250.727309] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_requests: align 64, maxelems 4294967295, elemsize 312
[1763745250.727310] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_rkeys: align 64, maxelems 4294967295, elemsize 112
[1763745250.727311] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_reg_bufs: align 64, maxelems 4294967295, elemsize 8216
[1763745250.727315] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 153
[1763745250.727317] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 1113
[1763745250.727318] [h001:2082112:0]           mpool.c:136  UCX  DEBUG mpool ucp_am_bufs: align 64, maxelems 4294967295, elemsize 65625
[1763745250.727319] [h001:2082112:0]       mpool_set.c:129  UCX  DEBUG mpool_set:ucp_am_bufs, sizes map 0x80000440, largest size 65536, mpools num 3
[1763745250.727325] [h001:2082112:0]      ucp_worker.c:1631 UCX  DEBUG worker 0xa216100: using cpu atomics
[1763745250.727356] [h001:2082112:0]          parser.c:2368 UCX  INFO  UCX_* env variables: UCX_TLS=cuda_ipc,cuda_copy,sm,tcp,self UCX_LOG_LEVEL=debug UCX_PROTO_ENABLE=n
[1763745250.727619] [h001:2082112:0]          ucp_ep.c:407  UCX  DEBUG created ep 0x15103cbd10b0 to <no debug data> from api call
[1763745250.727813] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728044] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728103] [h001:2082112:0]            sock.c:90   UCX  DEBUG   ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745250.728106] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG   speed of lo is UNKNOWN, assuming 100 Mbps
[1763745250.728135] [h001:2082112:0]            topo.c:935  UCX  DEBUG   /sys/class/net/lo: sysfs path undetected
[1763745250.728136] [h001:2082112:0]            topo.c:888  UCX  DEBUG   lo: pci bandwidth undetected, using maximal value
[1763745250.728176] [h001:2082112:0]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 self cfg#1 rma_am(tcp/ibp27s0)  amo_am(tcp/ibp27s0)  am(tcp/ibp27s0)  ka(tcp/ibp27s0)
[1763745250.728178] [h001:2082112:0]          wireup.c:1267 UCX  DEBUG   ep 0x15103cbd10b0: am_lane 0 wireup_msg_lane 0 cm_lane <none> keepalive_lane 0 reachable_mds 0xdf
[1763745250.728182] [h001:2082112:0]          wireup.c:1290 UCX  DEBUG   ep 0x15103cbd10b0: lane[0]:  1:tcp/ibp27s0.0 md[1]           -> addr[1].md[1]/tcp/sysdev[2] seg 8192 am am_bw#0 keepalive wireup
[1763745250.728186] [h001:2082112:0]          wireup.c:1293 UCX  DEBUG   ep 0x15103cbd10b0: err mode 1, flags 0x1
[1763745250.728195] [h001:2082112:0]          tcp_ep.c:260  UCX  DEBUG   tcp_ep 0xa25d510: created on iface 0xa26e710, fd -1
[1763745250.728201] [h001:2082112:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xa25d510: CLOSED -> CONNECTING for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745250.728215] [h001:2082112:0]          tcp_ep.c:620  UCX  DIAG    tcp_iface 0xa26e710: net.ipv4.conf.ibp27s0.rp_filter is set to strict mode (1), connections may fail
[1763745250.728224] [h001:2082112:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xa25d510: CONNECTING -> CONNECTING for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745250.728297] [h001:2082112:0]            sock.c:358  UCX  DEBUG   connect(fd=73, src_addr=172.18.49.211:42679 dest_addr=172.18.49.211:49879): Success
[1763745250.728310] [h001:2082112:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xa25d510: CONNECTING -> WAITING_ACK for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745250.728437] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728610] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728782] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728944] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729113] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729282] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729463] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729631] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729801] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729975] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730144] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730310] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730481] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730662] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730834] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.01]           -> addr[1].md[1]/tcp/sysdev[2] seg 8192 am am_bw#0 keepalive wireup
[1763745250.728088] [h001:2082100:0]          wireup.c:1293 UCX  DEBUG   ep 0x14ea6e2100b0: err mode 1, flags 0x1
[1763745250.728099] [h001:2082100:0]          tcp_ep.c:260  UCX  DEBUG   tcp_ep 0xac7bdd0: created on iface 0xac7e900, fd -1
[1763745250.728105] [h001:2082100:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xac7bdd0: CLOSED -> CONNECTING for the [172.18.49.211:50895]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745250.728125] [h001:2082100:0]          tcp_ep.c:620  UCX  DIAG    tcp_iface 0xac7e900: net.ipv4.conf.ibp27s0.rp_filter is set to strict mode (1), connections may fail
[1763745250.728135] [h001:2082100:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xac7bdd0: CONNECTING -> CONNECTING for the [172.18.49.211:50895]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745250.728220] [h001:2082100:0]            sock.c:358  UCX  DEBUG   connect(fd=73, src_addr=172.18.49.211:57781 dest_addr=172.18.49.211:50895): Success
[1763745250.728237] [h001:2082100:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xac7bdd0: CONNECTING -> WAITING_ACK for the [172.18.49.211:50895]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745250.728358] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728531] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728694] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.728855] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729018] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729183] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729358] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729529] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729706] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.729870] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730052] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730211] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730382] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730549] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.730725] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[2025-11-21 12:14:10 NIXL INFO    _api.py:361 Backend UCX was instantiated
2025-11-21 12:14:10 NIXL INFO    _api.py:251 Initialized NIXL agent: target
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:54 NIXL agent created (listen_port=3005)
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:55 Check UCX log above for transport selection!
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:56 Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!
2025-11-21 12:14:10 NIXL INFO    _api.py:361 Backend UCX was instantiated
2025-11-21 12:14:10 NIXL INFO    _api.py:251 Initialized NIXL agent: initiator
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:54 NIXL agent created (listen_port=0)
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:55 Check UCX log above for transport selection!
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:56 Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:71 Transfer size: 5.0000 GB (10 x (1024, 2, 32, 4096))
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:72 Iterations: warmup=3, test=10
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:71 Transfer size: 5.0000 GB (10 x (1024, 2, 32, 4096))
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:73 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:72 Iterations: warmup=3, test=10
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:76 Registering GPU memory with NIXL...
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:73 ================================================================================
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:76 Registering GPU memory with NIXL...
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:81 Memory registered
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:85 
TARGET: Listening on port 3005...
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:81 Memory registered
2025-11-21 12:14:10 NIXL INFO    nixl_h100_nvlink.py:124 
INITIATOR: Waiting for target...
2025-11-21 12:14:12 NIXL INFO    nixl_h100_nvlink.py:127 INITIATOR: Connecting to 127.0.0.1:3005
'
[1763745250.731004] [h001:2082112:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.731115] [h001:2082112:1]            sock.c:424  UCX  DEBUG [172.18.49.211:49879]<->[172.18.49.211:42679] is a connected pair
[1763745250.731125] [h001:2082112:1]          tcp_ep.c:260  UCX  DEBUG tcp_ep 0x151030000e30: created on iface 0xa26e710, fd 75
[1763745250.731128] [h001:2082112:1]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x151030000e30: CLOSED -> RECV_MAGIC_NUMBER
[1763745250.731134] [h001:2082112:1]          tcp_cm.c:843  UCX  DEBUG tcp_iface 0xa26e710: accepted connection from 172.18.49.211:42679 on 172.18.49.211:49879 to tcp_ep 0x151030000e30 (fd 75)
[1763745250.731157] [h001:2082112:1]           mpool.c:281  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: allocated chunk 0x151030000ee0 of 1049176 bytes with 8 elements
[1763745250.731171] [h001:2082112:1]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x151030000e30: RECV_MAGIC_NUMBER -> ACCEPTING
[1763745250.731178] [h001:2082112:1]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x151030000e30: ACCEPTING -> CONNECTED for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:Rx]
[1763745250.731222] [h001:2082112:1]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0xa25d510: WAITING_ACK -> CONNECTED for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [Tx:-]
[1763745250.731231] [h001:2082112:1]           mpool.c:281  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: allocated chunk 0x151030101330 of 66136 bytes with 8 elements
[1763745250.771384] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771487] [h001:2082112:0]           mpool.c:281  UCX  DEBUG   mpool ucp_rkeys: allocated chunk 0xadde240 of 16472 bytes with 128 elements
[1763745250.771606] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771704] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771792] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771877] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771961] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772051] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772142] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772235] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772314] [h001:2082112:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745252.960050] [h001:2082112:2]          ucp_ep.c:407  UCX  DEBUG created ep 0x15103cbd1108 to <no debug data> from api call
[1763745252.960347] [h001:2082112:2]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745252.960601] [h001:2082112:2]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745252.960667] [h001:2082112:2]            sock.c:90   UCX  DEBUG   ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745252.960672] [h001:2082112:2]         tcp_net.c:61   UCX  DEBUG   speed of lo is UNKNOWN, assuming 100 Mbps
[1763745252.960704] [h0011763745250.730906] [h001:2082100:0]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745250.731018] [h001:2082100:1]            sock.c:424  UCX  DEBUG [172.18.49.211:50895]<->[172.18.49.211:57781] is a connected pair
[1763745250.731028] [h001:2082100:1]          tcp_ep.c:260  UCX  DEBUG tcp_ep 0x14ea3c000e30: created on iface 0xac7e900, fd 75
[1763745250.731030] [h001:2082100:1]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x14ea3c000e30: CLOSED -> RECV_MAGIC_NUMBER
[1763745250.731036] [h001:2082100:1]          tcp_cm.c:843  UCX  DEBUG tcp_iface 0xac7e900: accepted connection from 172.18.49.211:57781 on 172.18.49.211:50895 to tcp_ep 0x14ea3c000e30 (fd 75)
[1763745250.731057] [h001:2082100:1]           mpool.c:281  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp: allocated chunk 0x14ea3c000ee0 of 1049176 bytes with 8 elements
[1763745250.731071] [h001:2082100:1]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x14ea3c000e30: RECV_MAGIC_NUMBER -> ACCEPTING
[1763745250.731079] [h001:2082100:1]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x14ea3c000e30: ACCEPTING -> CONNECTED for the [172.18.49.211:50895]<->[172.18.49.211:50895]:0 connection [-:Rx]
[1763745250.731116] [h001:2082100:1]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0xac7bdd0: WAITING_ACK -> CONNECTED for the [172.18.49.211:50895]<->[172.18.49.211:50895]:0 connection [Tx:-]
[1763745250.731126] [h001:2082100:1]           mpool.c:281  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp: allocated chunk 0x14ea3c101330 of 66136 bytes with 8 elements
[1763745250.771178] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771270] [h001:2082100:0]           mpool.c:281  UCX  DEBUG   mpool ucp_rkeys: allocated chunk 0xb7fadc0 of 16472 bytes with 128 elements
[1763745250.771365] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771474] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771572] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771663] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771749] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771833] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.771918] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772007] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745250.772091] [h001:2082100:0]    cuda_copy_md.c:585  UCX  DEBUG cuMemRetainAllocationHandle(&alloc_handle, (void*)address) failed: invalid argument
[1763745252.960931] [h001:2082100:a]            sock.c:424  UCX  DEBUG [172.18.49.211:50895]<->[172.18.49.211:37009] is a connected pair
[1763745252.960946] [h001:2082100:a]          tcp_ep.c:260  UCX  DEBUG tcp_ep 0x14ea44000cd0: created on iface 0xac7e900, fd 77
[1763745252.960950] [h001:2082100:a]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x14ea44000cd0: CLOSED -> RECV_MAGIC_NUMBER
[1763745252.960959] [h001:2082100:a]          tcp_cm.c:843  UCX  DEBUG tcp_iface 0xac7e900: accepted connection from 172.18.49.211:37009 on 172.18.49.211:50895 to tcp_ep 0x14ea44000cd0 (fd 77)
[1763745252.960984] [h001:2082100:2]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x14ea44000cd0: RECV_MAGIC_NUMBER -> ACCEPTING
[1763745252.961019] [h001:2082100:2]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x14ea4402025-11-21 12:14:13 NIXL INFO    nixl_h100_nvlink.py:99 TARGET: Initiator connected
2025-11-21 12:14:13 NIXL INFO    nixl_h100_nvlink.py:101 TARGET: Sent descriptors, ready for transfers
2025-11-21 12:14:13 NIXL INFO    nixl_h100_nvlink.py:157 INITIATOR: Connected and ready
2025-11-21 12:14:13 NIXL INFO    nixl_h100_nvlink.py:158 ================================================================================
2025-11-21 12:14:13 NIXL INFO    nixl_h100_nvlink.py:163 
WARMUP PHASE
00cd0: ACCEPTING -> CONNECTED for the [172.18.49.211:50895]<->[172.18.49.211:49879]:0 connection [-:Rx]
[1763745253.057064] [h001:2082100:3]          ucp_ep.c:407  UCX  DEBUG created ep 0x14ea6e210108 to <no debug data> from api call
[1763745253.057314] [h001:2082100:3]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745253.057542] [h001:2082100:3]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745253.057603] [h001:2082100:3]            sock.c:90   UCX  DEBUG   ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745253.057605] [h001:2082100:3]         tcp_net.c:61   UCX  DEBUG   speed of lo is UNKNOWN, assuming 100 Mbps
[1763745253.057636] [h001:2082100:3]            topo.c:935  UCX  DEBUG   /sys/class/net/lo: sysfs path undetected
[1763745253.057637] [h001:2082100:3]            topo.c:888  UCX  DEBUG   lo: pci bandwidth undetected, using maximal value
[1763745253.057698] [h001:2082100:3]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 intra-node cfg#2 rma_am(tcp/ibp27s0)  amo_am(tcp/ibp27s0)  am(tcp/ibp27s0 cuda_ipc/cuda)  ka(tcp/ibp27s0)
[1763745253.057703] [h001:2082100:3]          wireup.c:1267 UCX  DEBUG   ep 0x14ea6e210108: am_lane 0 wireup_msg_lane 0 cm_lane <none> keepalive_lane 0 reachable_mds 0xee
[1763745253.057706] [h001:2082100:3]          wireup.c:1290 UCX  DEBUG   ep 0x14ea6e210108: lane[0]:  1:tcp/ibp27s0.0 md[1]           -> addr[1].md[1]/tcp/sysdev[2] seg 8192 am am_bw#0 keepalive wireup
[1763745253.057709] [h001:2082100:3]          wireup.c:1290 UCX  DEBUG   ep 0x14ea6e210108: lane[1]:  6:cuda_ipc/cuda.0 md[5]         -> addr[6].md[5]/cuda_ipc/sysdev[1] seg 0 rma_bw#0
[1763745253.057710] [h001:2082100:3]          wireup.c:1293 UCX  DEBUG   ep 0x14ea6e210108: err mode 1, flags 0x2
[1763745253.057714] [h001:2082100:3]          tcp_ep.c:260  UCX  DEBUG   tcp_ep 0x14ea40038290: created on iface 0xac7e900, fd -1
[1763745253.057719] [h001:2082100:3]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x14ea40038290: CLOSED -> CONNECTING for the [172.18.49.211:50895]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745253.057737] [h001:2082100:3]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x14ea40038290: CONNECTING -> WAITING_ACK for the [172.18.49.211:50895]<->[172.18.49.211:49879]:0 connection [-:Rx]
[1763745253.057772] [h001:2082100:2]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0x14ea44000cd0: purge outstanding operations with status Request canceled
[1763745253.057777] [h001:2082100:2]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x14ea44000cd0: CONNECTED -> CLOSED for the [172.18.49.211:50895]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745253.057778] [h001:2082100:2]          tcp_ep.c:412  UCX  DEBUG tcp_ep 0x14ea44000cd0: destroyed on iface 0xac7e900
[1763745253.067963] [h001:2082100:3]       wireup_ep.c:567  UCX  DEBUG   ep 0x14ea6e210108: wireup_ep 0x14ea40005a70 set next_ep 0x14ea40038290
[1763745253.067966] [h001:2082100:3]          wireup.c:2003 UCX  DEBUG   ep 0x14ea6e210108: send wireup request (flags=0x4051)
[1763745253.068001] [h001:2082100:2]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x14ea40038290: WAITING_ACK -> CONNECTED for the [172.18.49.211:50895]<->[172.18.49.211:49879]:0 connection [Tx:Rx]
[1763745253.068637] [h001:2082100:2]       wireup_ep.c:457  UCX  DEBUG ep 0x14ea6e210108: destroy wireup ep 0x14ea40005a70
[1763745253.074125] [h001:2082100:0]           mpool.c:281  UCX  DEBUG mpool ucp_requests: allocated chunk 0xb803284 of 41044 bytes with 128 elements
[h001:2082100:2:2082259] Caught signal 11 (Segmentation fault: invalid permissions for mapped object at address 0x14ea00000000)
==== backtrace (tid:2082259) ====
 0 0x000000000003ebf0 __GI___sigaction()  :0
 1 0x0000000000190acd __memmove_avx512_unaligned_erms()  :0
 2 0x000000000008fc91 ucp_get()  ???:0
 3 0x0000000000029b69 uct_tcp_ep_am_bcopy()  ???:0
 4 0x000000000008f81a ucp_get()  ???:0
 5 0x00000000000905a1 ucp_get_req_handler()  ???:0
 6 0x0000000000027a10 uct_tcp_ep_handle_io_err()  ???:0
 7 0x000000000002aedd uct_tcp_iface_progress()  ???:0
 8 0x000000000007ac9c ucs_event_set_wait()  ???:0
 9 0x000000000002ae17 uct_tcp_iface_progress()  ???:0
10 0x000000000006187a ucp_worker_progress()  ???:0
11 0x000000000003f131 nixlUcxSharedThread::run()  :0
12 0x00000000000df0e6 execute_native_thread_routine()  /home/task_176276935360828/conda-bld/gcc_compilers_1762769419537/work/build/x86_64-conda-linux-gnu/libstdc++-v3/src/c++11/../../../../../libstdc++-v3/src/c++11/thread.cc:104
13 0x000000000008a19a start_thread()  ???:0
14 0x000000000010f210 __clone3()  :0
=================================
:2082112:2]            topo.c:935  UCX  DEBUG   /sys/class/net/lo: sysfs path undetected
[1763745252.960714] [h001:2082112:2]            topo.c:888  UCX  DEBUG   lo: pci bandwidth undetected, using maximal value
[1763745252.960778] [h001:2082112:2]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 intra-node cfg#2 rma_am(tcp/ibp27s0)  amo_am(tcp/ibp27s0)  am(tcp/ibp27s0 cuda_ipc/cuda)  ka(tcp/ibp27s0)
[1763745252.960783] [h001:2082112:2]          wireup.c:1267 UCX  DEBUG   ep 0x15103cbd1108: am_lane 0 wireup_msg_lane 0 cm_lane <none> keepalive_lane 0 reachable_mds 0xee
[1763745252.960787] [h001:2082112:2]          wireup.c:1290 UCX  DEBUG   ep 0x15103cbd1108: lane[0]:  1:tcp/ibp27s0.0 md[1]           -> addr[1].md[1]/tcp/sysdev[2] seg 8192 am am_bw#0 keepalive wireup
[1763745252.960789] [h001:2082112:2]          wireup.c:1290 UCX  DEBUG   ep 0x15103cbd1108: lane[1]:  6:cuda_ipc/cuda.0 md[5]         -> addr[6].md[5]/cuda_ipc/sysdev[0] seg 0 rma_bw#0
[1763745252.960790] [h001:2082112:2]          wireup.c:1293 UCX  DEBUG   ep 0x15103cbd1108: err mode 1, flags 0x2
[1763745252.960794] [h001:2082112:2]          tcp_ep.c:260  UCX  DEBUG   tcp_ep 0xade6080: created on iface 0xa26e710, fd -1
[1763745252.960801] [h001:2082112:2]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xade6080: CLOSED -> CONNECTING for the [172.18.49.211:49879]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745252.960818] [h001:2082112:2]          tcp_ep.c:620  UCX  DIAG    tcp_iface 0xa26e710: net.ipv4.conf.ibp27s0.rp_filter is set to strict mode (1), connections may fail
[1763745252.960830] [h001:2082112:2]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xade6080: CONNECTING -> CONNECTING for the [172.18.49.211:49879]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745252.960887] [h001:2082112:2]            sock.c:358  UCX  DEBUG   connect(fd=77, src_addr=172.18.49.211:37009 dest_addr=172.18.49.211:50895): Success
[1763745252.960902] [h001:2082112:2]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0xade6080: CONNECTING -> WAITING_ACK for the [172.18.49.211:49879]<->[172.18.49.211:50895]:0 connection [-:-]
[1763745252.961084] [h001:2082112:3]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0xade6080: WAITING_ACK -> CONNECTED for the [172.18.49.211:49879]<->[172.18.49.211:50895]:0 connection [Tx:-]
[1763745253.068285] [h001:2082112:3]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745253.068521] [h001:2082112:3]            topo.c:938  UCX  DEBUG   /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745253.208208] [h001:2082112:0]           mpool.c:281  UCX  DEBUG mpool ucp_requests: allocated chunk 0xade6134 of 41044 bytes with 128 elements
[1763745253.208336] [h001:2082112:0]           flush.c:387  UCX  DEBUG flush_nbx ep 0x15103cbd1108
[1763745257.481267] [h001:2082112:3]            sock.c:546  UCX  DEBUG recv(77) failed: Connection reset by peer
[1763745257.481283] [h001:2082112:3]          tcp_ep.c:1260 UCX  DIAG  tcp_ep 0xade6080 (state=CONNECTED): recv(77) failed: Connection reset by remote peer
[1763745257.481285] [h001:2082112:3]          tcp_ep.c:1053 UCX  DEBUG tcp_ep 0xade6080: remote disconnected
[1763745257.481288] [h001:2082112:3]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0xade6080: purge outstanding operations with status Connection reset by remote peer
[1763745257.481300] [h001:2082112:3]          tcp_ep.c:507  UCX  DEBUG tcp_ep 0xade6080: calling error handler (flags: 1)
[1763745257.481305] [h001:2082112:3]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0xade6080: CONNECTED -> CLOSED for the [172.18.49.211:49879]<->[172.18.49.211:50895]:0 connection [Tx:-]
[1763745257.481309] [h001:2082112:3]      ucp_worker.c:545  UCX  DEBUG worker 0xa216100: error handler called for UCT EP 0xade6080: Connection reset by remote peer
[1763745257.481318] [h001:2082112:3]          ucp_ep.c:1477 UCX  DEBUG ep 0x15103cbd1108: set_ep_failed status Connection reset by remote peer on lane[0]=0xade6080
[1763745257.481323] [h001:2082112:3]          ucp_ep.c:1440 UCX  DEBUG ep 0x15103cbd1108: discarding lanes
[1763745257.481335] [h001:2082112:3]          ucp_ep.c:1448 UCX  DEBUG ep 0x15103cbd1108: discard uct_ep[0]=0xade6080
[1763745257.481338] [h001:2082112:3]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0xade6080: purge outstanding operations with status Request canceled
[1763745257.481340] [h001:2082112:3]          ucp_ep.c:1448 UCX  DEBUG ep 0x15103cbd1108: discard uct_ep[1]=0x151034037c90
[1763745257.481343] [h001:2082112:3]          ucp_ep.c:3510 UCX  DEBUG ep 0x15103cbd1108: calling user error callback 0x15103dc10cf0 with arg 0x151034003ad0 and status Connection reset by remote peer
[1763745257.481355] [h001:2082112:3]          ucp_ep.c:1755 UCX  DEBUG ep 0x15103cbd1108 flags 0x22509a cfg_index 2: close_nbx(flags=0x1)
[1763745257.481360] [h001:2082112:3]          ucp_ep.c:1289 UCX  DEBUG ep 0x15103cbd1108: destroy
[1763745257.481362] [h001:2082112:3]          ucp_ep.c:1607 UCX  DEBUG ep 0x15103cbd1108: cleanup lanes
[1763745257.481364] [h001:2082112:3]          ucp_ep.c:1618 UCX  DEBUG ep 0x15103cbd1108: pending & destroy uct_ep[0]=0x151030145b90
[1763745257.481368] [h001:2082112:3]          ucp_ep.c:1618 UCX  DEBUG ep 0x15103cbd1108: pending & destroy uct_ep[1]=0x151030145b90
[1763745257.481372] [h001:2082112:3]          ucp_ep.c:1354 UCX  DEBUG ep 0x15103cbd1108: unprogress iface 0xa26e710 tcp/ibp27s0
[1763745257.481378] [h001:2082112:3]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0xade6080: purge outstanding operations with status Request canceled
[1763745257.481388] [h001:2082112:3]          tcp_ep.c:412  UCX  DEBUG tcp_ep 0xade6080: destroyed on iface 0xa26e710
[1763745257.481391] [h001:2082112:3]          ucp_ep.c:1354 UCX  DEBUG ep 0x15103cbd1108: unprogress iface 0xa212900 cuda_ipc/cuda
Traceback (most recent call last):
  File "/scratch/gautschi/wang6199/nixl/nixl_h100_nvlink.py", line 280, in <module>
    main()
  File "/scratch/gautschi/wang6199/nixl/nixl_h100_nvlink.py", line 186, in main
    state = agent.check_xfer_state(xfer_handle)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/scratch/gautschi/wang6199/miniconda3/envs/vllm-nixl/lib/python3.12/site-packages/nixl_cu12/_api.py", line 613, in check_xfer_state
    status = self.agent.getXferStatus(handle._handle)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
nixl_cu12._bindings.nixlRemoteDisconnectError: NIXL_ERR_REMOTE_DISCONNECT
[1763745257.604657] [h001:2082112:0]          ucp_ep.c:1755 UCX  DEBUG ep 0x15103cbd10b0 flags 0x204091 cfg_index 1: close_nbx(flags=0x0)
[1763745257.604664] [h001:2082112:0]           flush.c:387  UCX  DEBUG close ep 0x15103cbd10b0
[1763745257.692591] [h001:2082112:0]      ucp_worker.c:2912 UCX  DEBUG destroy worker 0xa216100
[1763745257.692601] [h001:2082112:0]      ucp_worker.c:2898 UCX  DEBUG worker 0xa216100: destroy all endpoints
[1763745257.692604] [h001:2082112:0]          ucp_ep.c:1282 UCX  DEBUG ep 0x15103cbd10b0: purge uct_ep[0]=0xa25d510
[1763745257.692609] [h001:2082112:0]          ucp_ep.c:1289 UCX  DEBUG ep 0x15103cbd10b0: destroy
[1763745257.692611] [h001:2082112:0]          ucp_ep.c:1607 UCX  DEBUG ep 0x15103cbd10b0: cleanup lanes
[1763745257.692613] [h001:2082112:0]          ucp_ep.c:1618 UCX  DEBUG ep 0x15103cbd10b0: pending & destroy uct_ep[0]=0xa25d510
[1763745257.692616] [h001:2082112:0]          ucp_ep.c:1354 UCX  DEBUG ep 0x15103cbd10b0: unprogress iface 0xa26e710 tcp/ibp27s0
[1763745257.692866] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693101] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693262] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693424] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693582] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693742] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.693895] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694055] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694208] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694359] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694517] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694665] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694821] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.694973] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695127] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695279] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695335] [h001:2082112:0]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0xa25d510: purge outstanding operations with status Request canceled
[1763745257.695343] [h001:2082112:0]          ucp_ep.c:1710 UCX  DEBUG ep 0x15103cbd10b0: flags 0x204488 close flushed callback for request 0xadef3c0
[1763745257.695397] [h001:2082112:0]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0xa25d510: CONNECTED -> CLOSED for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745257.695401] [h001:2082112:0]          tcp_ep.c:412  UCX  DEBUG tcp_ep 0xa25d510: destroyed on iface 0xa26e710
[1763745257.695407] [h001:2082112:0]      ucp_worker.c:2898 UCX  DEBUG worker 0xa216100: destroy internal endpoints
[1763745257.695408] [h001:2082112:0]          ucp_ep.c:1282 UCX  DEBUG ep 0x15103cbd1000: purge uct_ep[0]=0xa204730
[1763745257.695410] [h001:2082112:0]          ucp_ep.c:1289 UCX  DEBUG ep 0x15103cbd1000: destroy
[1763745257.695411] [h001:2082112:0]          ucp_ep.c:1607 UCX  DEBUG ep 0x15103cbd1000: cleanup lanes
[1763745257.695412] [h001:2082112:0]          ucp_ep.c:1618 UCX  DEBUG ep 0x15103cbd1000: pending & destroy uct_ep[0]=0xa204730
[1763745257.695413] [h001:2082112:0]          ucp_ep.c:1354 UCX  DEBUG ep 0x15103cbd1000: unprogress iface 0xa2158f0 cuda_copy/cuda
[1763745257.695416] [h001:2082112:0]          ucp_ep.c:1282 UCX  DEBUG ep 0x15103cbd1058: purge uct_ep[0]=0xa2045d0
[1763745257.695417] [h001:2082112:0]          ucp_ep.c:1289 UCX  DEBUG ep 0x15103cbd1058: destroy
[1763745257.695418] [h001:2082112:0]          ucp_ep.c:1607 UCX  DEBUG ep 0x15103cbd1058: cleanup lanes
[1763745257.695419] [h001:2082112:0]          ucp_ep.c:1618 UCX  DEBUG ep 0x15103cbd1058: pending & destroy uct_ep[0]=0xa2045d0
[1763745257.695419] [h001:2082112:0]          ucp_ep.c:1354 UCX  DEBUG ep 0x15103cbd1058: unprogress iface 0xa2158f0 cuda_copy/cuda
[1763745257.695424] [h001:2082112:0]      ucp_worker.c:243  UCX  DEBUG worker 0xa216100: remove active message handlers
[1763745257.695537] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695687] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695835] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.695984] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696133] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696287] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696442] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696593] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696743] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.696898] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697048] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697197] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697348] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697496] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697646] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697800] [h001:2082112:0]            topo.c:938  UCX  DEBUG /sys/class/net/ibp27s0: PF sysfs path is '/sys/devices/pci0000:15/0000:15:01.0/0000:16:00.0/0000:17:03.0/0000:1b:00.0'
[1763745257.697858] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.697861] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.697891] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.697892] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.697905] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.697907] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.697928] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.697929] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.697940] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.697942] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.697962] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.697963] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.697973] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.697975] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.697994] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.697995] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698005] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698007] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698026] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698027] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698036] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698038] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698057] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698057] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698067] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698069] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698087] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698091] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698101] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698102] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698122] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698123] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698136] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698138] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698157] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698158] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698168] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698170] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698190] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698191] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698201] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698203] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698222] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698223] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698233] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698235] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698254] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698254] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698265] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698267] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698286] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698287] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698297] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698299] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698318] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698319] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698329] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698331] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698349] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698350] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698360] [h001:2082112:0]            sock.c:90   UCX  DEBUG ioctl(req=35142, ifr_name=lo) failed: Operation not supported
[1763745257.698365] [h001:2082112:0]         tcp_net.c:61   UCX  DEBUG speed of lo is UNKNOWN, assuming 100 Mbps
[1763745257.698384] [h001:2082112:0]            topo.c:935  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1763745257.698385] [h001:2082112:0]            topo.c:888  UCX  DEBUG lo: pci bandwidth undetected, using maximal value
[1763745257.698416] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_reg_bufs destroyed
[1763745257.698418] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_am_bufs destroyed
[1763745257.698420] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_am_bufs destroyed
[1763745257.698420] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_am_bufs destroyed
[1763745257.698428] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_rkeys destroyed
[1763745257.698439] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool ucp_requests destroyed
[1763745257.698448] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa210830 [id=70 ref 1] uct_rdmacm_cm_get_device_context() from hash
[1763745257.698449] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa210830 [id=70 ref 1] uct_rdmacm_cm_get_device_context()
[1763745257.698455] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa210830 [id=70 ref 0] uct_rdmacm_cm_get_device_context()
[1763745257.698463] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool self_msg_desc destroyed
[1763745257.698465] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa211b70 [id=60 ref 1] ucp_worker_iface_activate() from hash
[1763745257.698467] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa211b70 [id=60 ref 1] ucp_worker_iface_activate()
[1763745257.698469] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa211b70 [id=60 ref 0] ucp_worker_iface_activate()
[1763745257.698470] [h001:2082112:0]       tcp_iface.c:874  UCX  DEBUG tcp_iface 0xa26e710: destroying
[1763745257.698472] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa259d40 [id=61 ref 1] uct_tcp_query_devices() from hash
[1763745257.698473] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa259d40 [id=61 ref 1] uct_tcp_query_devices()
[1763745257.698475] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa259d40 [id=61 ref 0] uct_tcp_query_devices()
[1763745257.698477] [h001:2082112:0]          tcp_ep.c:359  UCX  DEBUG tcp_ep 0x151030000e30: purge outstanding operations with status Request canceled
[1763745257.698498] [h001:2082112:0]          tcp_cm.c:96   UCX  DEBUG tcp_ep 0x151030000e30: CONNECTED -> CLOSED for the [172.18.49.211:49879]<->[172.18.49.211:49879]:0 connection [-:-]
[1763745257.698499] [h001:2082112:0]          tcp_ep.c:412  UCX  DEBUG tcp_ep 0x151030000e30: destroyed on iface 0xa26e710
[1763745257.698513] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp destroyed
[1763745257.698522] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp destroyed
[1763745257.698529] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa20e590 [id=62 ref 1] ucp_worker_iface_activate() from hash
[1763745257.698530] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa20e590 [id=62 ref 1] ucp_worker_iface_activate()
[1763745257.698532] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa20e590 [id=62 ref 0] ucp_worker_iface_activate()
[1763745257.698534] [h001:2082112:0]       tcp_iface.c:874  UCX  DEBUG tcp_iface 0xa26f110: destroying
[1763745257.698535] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa211da0 [id=63 ref 1] uct_tcp_query_devices() from hash
[1763745257.698536] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa211da0 [id=63 ref 1] uct_tcp_query_devices()
[1763745257.698538] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa211da0 [id=63 ref 0] uct_tcp_query_devices()
[1763745257.698541] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_tcp_iface_rx_buf_mp destroyed
[1763745257.698542] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_tcp_iface_tx_buf_mp destroyed
[1763745257.698547] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa20f980 [id=64 ref 1] ucp_worker_iface_activate() from hash
[1763745257.698548] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa20f980 [id=64 ref 1] ucp_worker_iface_activate()
[1763745257.698550] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa20f980 [id=64 ref 0] ucp_worker_iface_activate()
[1763745257.698808] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool mm_recv_desc destroyed
[1763745257.698827] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa2008f0 [id=66 ref 1] ucp_worker_iface_activate() from hash
[1763745257.698828] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa2008f0 [id=66 ref 1] ucp_worker_iface_activate()
[1763745257.698831] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa2008f0 [id=66 ref 0] ucp_worker_iface_activate()
[1763745257.699247] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool mm_recv_desc destroyed
[1763745257.699262] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa2158b0 [id=68 ref 1] ucp_worker_iface_activate() from hash
[1763745257.699263] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa2158b0 [id=68 ref 1] ucp_worker_iface_activate()
[1763745257.699265] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa2158b0 [id=68 ref 0] ucp_worker_iface_activate()
[1763745257.699271] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa204670 [id=69 ref 1] ucp_worker_iface_activate() from hash
[1763745257.699272] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa204670 [id=69 ref 1] ucp_worker_iface_activate()
[1763745257.699274] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa204670 [id=69 ref 0] ucp_worker_iface_activate()
[1763745257.699281] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_scopy_iface_tx_mp destroyed
[1763745257.699285] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool uct_scopy_iface_tx_mp destroyed
[1763745257.699332] [h001:2082112:0]           async.c:172  UCX  DEBUG removed async handler 0xa265700 [id=53 ref 1] ucs_mem_region_destroy_internal() from hash
[1763745257.699333] [h001:2082112:0]           async.c:575  UCX  DEBUG removing async handler 0xa265700 [id=53 ref 1] ucs_mem_region_destroy_internal()
[1763745257.699387] [h001:2082112:0]           async.c:187  UCX  DEBUG release async handler 0xa265700 [id=53 ref 0] ucs_mem_region_destroy_internal()
[1763745257.699507] [h001:2082112:0]           mpool.c:194  UCX  DEBUG mpool rcache_mp destroyed
```

</details>

### brminich · 2025-12-01

pls do not set `UCX_PROTO_ENABLE=n`, old protocols do not support RMA with GPU memory.
Why do you set it?

### brminich · 2025-12-05

@Marmot-C does removing `UCX_PROTO_ENABLE=n` help?

### Jeffwan · 2025-12-09

@brminich I have a quick question, is the nixl[cu12] comes with cuda_ipc support? Do i need to rebuild ucx & nixl from source? 

### brminich · 2025-12-09

should be supported
cc @ovidiusm to confirm

### Marmot-C · 2025-12-09

> [@Marmot-C](https://github.com/Marmot-C) does removing `UCX_PROTO_ENABLE=n` help?

Hi @brminich , yes it helped, now the bandwidth is about 275GB/s. The `UCX_PROTO_ENABLE=n` variable was somehow set by default... However when i try to test it on vLLM with PD disaggregation using NiXL as backend, there doesn't seem to be any improvement switching to NVLink. Are there any hints on the setup or suggestions for profiling the bottleneck? Thank you!

### brminich · 2025-12-09

how do you switch to NVLINK? Can you pls provide output of  `UCX_PROTO_INFO=y` to check what transport was selected?

### meatball-spaghetti · 2026-01-15

Hello @brminich @Marmot-C  I’m experiencing the same issue, so I’m sharing my test results.

If I remove the rc option, it doesn’t work. getting an OOM error

I think the primary reason is a failure in resource creation permissions or sharing. 
For UCX to utilize cuda_ipc, it must create and exchange IPC handles between GPUs
if any part of this process fails, it silently falls back to rc_mlx5

My Docker configuration is as follows.

```
docker stop vllm-prefill
docker rm vllm-prefill
docker run -it -d \
    --network host \
    --ipc host \
    --pid host \
    --name vllm-prefill \
    --gpus 'all' \
    --shm-size=128GB \
    --ulimit memlock=-1 \
    --cap-add IPC_LOCK \
    --cap-add SYS_PTRACE \
    -v "/mnt/logs:/logs" \
    --privileged \
    --entrypoint sleep \
    vllm/vllm-openai:v0.11.0 infinity
```

Test Result 
```
root@soonh-001:/logs/docker_run/pd/nixlconnector# UCX_PROTO_INFO=y  UCX_MEMTYPE_CACHE=n UCX_LOG_LEVEL=INFO UCX_TLS=cuda_ipc,cuda_copy,sm,rc,self python3 nixl_h100_nvlink.py --ip 127.0.0.1 --mode initiator
2026-01-15 03:09:51 NIXL INFO    nixl_h100_nvlink.py:43 ================================================================================
2026-01-15 03:09:51 NIXL INFO    nixl_h100_nvlink.py:44 NIXL H100 NVLink Bandwidth Test
2026-01-15 03:09:51 NIXL INFO    nixl_h100_nvlink.py:45 ================================================================================
2026-01-15 03:09:51 NIXL INFO    nixl_h100_nvlink.py:46 Mode: initiator
2026-01-15 03:09:51 NIXL INFO    nixl_h100_nvlink.py:47 GPU: 1 - NVIDIA H100 80GB HBM3
[1768475391.352635] [soonh-001:115648:0]     ucp_context.c:2339 UCX  INFO  Version 1.19.0 (loaded from /usr/local/ucx/lib/libucp.so.0)
[1768475392.060999] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------+
[1768475392.061007] [soonh-001:115648:0]   | ucp_context_0 self cfg#0 | remote memory write by ucp_put* from host memory to host    |
[1768475392.061009] [soonh-001:115648:0]   +--------------------------+--------------------------------------------+----------------+
[1768475392.061013] [soonh-001:115648:0]   |            0..4294967295 | short                                      | cuda_copy/cuda |
[1768475392.061014] [soonh-001:115648:0]   +--------------------------+--------------------------------------------+----------------+
[1768475392.061041] [soonh-001:115648:0]   +--------------------------+------------------------------------------------------------------------------+
[1768475392.061044] [soonh-001:115648:0]   | ucp_context_0 self cfg#0 | remote memory write by ucp_put*(fast-completion) from host memory to host    |
[1768475392.061047] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------+----------------+
[1768475392.061049] [soonh-001:115648:0]   |            0..4294967295 | short                                                       | cuda_copy/cuda |
[1768475392.061051] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------+----------------+
[1768475392.061078] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.061081] [soonh-001:115648:0]   | ucp_context_0 self cfg#0 | remote memory write by ucp_put*(multi) from host memory to host    |
[1768475392.061084] [soonh-001:115648:0]   +--------------------------+---------------------------------------------------+----------------+
[1768475392.061086] [soonh-001:115648:0]   |            0..4294967295 | short                                             | cuda_copy/cuda |
[1768475392.061087] [soonh-001:115648:0]   +--------------------------+---------------------------------------------------+----------------+
[1768475392.061126] [soonh-001:115648:0]   +--------------------------+----------------------------------------------------+
[1768475392.061128] [soonh-001:115648:0]   | ucp_context_0 self cfg#0 | active message by ucp_am_send* from host memory    |
[1768475392.061130] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------+--+
[1768475392.061132] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------+--+
[1768475392.061144] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.061146] [soonh-001:115648:0]   | ucp_context_0 self cfg#0 | active message by ucp_am_send* with reply flag from host memory    |
[1768475392.061148] [soonh-001:115648:0]   +--------------------------+-----------------------------------------------------------------+--+
[1768475392.061149] [soonh-001:115648:0]   +--------------------------+-----------------------------------------------------------------+--+
[1768475392.061461] [soonh-001:115648:0]          parser.c:2359 UCX  WARN  unused environment variable: UCX_PREFIX
[1768475392.061461] [soonh-001:115648:0]          parser.c:2359 UCX  WARN  (set UCX_WARN_UNUSED_ENV_VARS=n to suppress this warning)
[1768475392.061470] [soonh-001:115648:0]          parser.c:2368 UCX  INFO  UCX_* env variables: UCX_TLS=cuda_ipc,cuda_copy,sm,rc,self UCX_MEMTYPE_CACHE=n UCX_CUDA_IPC_ALLOC=mmap UCX_LOG_LEVEL=INFO UCX_PROTO_INFO=y
[1768475392.061922] [soonh-001:115648:0]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 self cfg#1 rma(rc_mlx5/mlx5_0:1)  amo(rc_mlx5/mlx5_0:1)  am(rc_mlx5/mlx5_0:1 rc_mlx5/mlx5_0:1)  ka(ud_mlx5/mlx5_0:1)
[1768475392.068548] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------+
[1768475392.068555] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put* from host memory to host    |
[1768475392.068559] [soonh-001:115648:0]   +--------------------------+------------+------------------------------------------------+
[1768475392.068562] [soonh-001:115648:0]   |                    0..2K | short      | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.068564] [soonh-001:115648:0]   |               2049..8256 | copy-in    | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.068566] [soonh-001:115648:0]   |                8257..inf | zero-copy  | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.068568] [soonh-001:115648:0]   +--------------------------+------------+------------------------------------------------+
[1768475392.068653] [soonh-001:115648:0]   +--------------------------+------------------------------------------------------------------------------+
[1768475392.068656] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(fast-completion) from host memory to host    |
[1768475392.068658] [soonh-001:115648:0]   +--------------------------+-----------------------------+------------------------------------------------+
[1768475392.068661] [soonh-001:115648:0]   |                    0..2K | short                       | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.068663] [soonh-001:115648:0]   |               2049..9383 | copy-in                     | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.068666] [soonh-001:115648:0]   |                9384..inf | zero-copy                   | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.068668] [soonh-001:115648:0]   +--------------------------+-----------------------------+------------------------------------------------+
[1768475392.068739] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.068742] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(multi) from host memory to host    |
[1768475392.068744] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
[1768475392.068746] [soonh-001:115648:0]   |                  0..1395 | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.068748] [soonh-001:115648:0]   |                1396..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.068750] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
[1768475392.069423] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.069427] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put* from host memory to cuda/dev[1]    |
[1768475392.069428] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
[1768475392.069431] [soonh-001:115648:0]   |                    0..2K | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.069434] [soonh-001:115648:0]   |               2049..8256 | copy-in           | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.069435] [soonh-001:115648:0]   |                8257..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.069436] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
[1768475392.069507] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------------------------------+
[1768475392.069510] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(fast-completion) from host memory to cuda/dev[1]    |
[1768475392.069512] [soonh-001:115648:0]   +--------------------------+------------------------------------+------------------------------------------------+
[1768475392.069517] [soonh-001:115648:0]   |                    0..2K | short                              | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.069519] [soonh-001:115648:0]   |               2049..9383 | copy-in                            | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.069522] [soonh-001:115648:0]   |                9384..inf | zero-copy                          | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.069524] [soonh-001:115648:0]   +--------------------------+------------------------------------+------------------------------------------------+
[1768475392.069601] [soonh-001:115648:0]   +--------------------------+---------------------------------------------------------------------------+
[1768475392.069604] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(multi) from host memory to cuda/dev[1]    |
[1768475392.069606] [soonh-001:115648:0]   +--------------------------+--------------------------+------------------------------------------------+
[1768475392.069608] [soonh-001:115648:0]   |                  0..1395 | short                    | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.069610] [soonh-001:115648:0]   |                1396..inf | zero-copy                | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.069613] [soonh-001:115648:0]   +--------------------------+--------------------------+------------------------------------------------+
[1768475392.069862] [soonh-001:115648:0]   +--------------------------+----------------------------------------------------+
[1768475392.069866] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send* from host memory    |
[1768475392.069867] [soonh-001:115648:0]   +--------------------------+---------------------------+------------------------+
[1768475392.069871] [soonh-001:115648:0]   |                  0..2038 | short                     | rc_mlx5/mlx5_0:1/path0 |
[1768475392.069873] [soonh-001:115648:0]   |               2039..8184 | copy-in                   | rc_mlx5/mlx5_0:1/path0 |
[1768475392.069876] [soonh-001:115648:0]   |              8185..11552 | multi-frag copy-in        | rc_mlx5/mlx5_0:1/path0 |
[1768475392.069879] [soonh-001:115648:0]   |               11553..inf | multi-frag zero-copy      | rc_mlx5/mlx5_0:1/path0 |
[1768475392.069881] [soonh-001:115648:0]   +--------------------------+---------------------------+------------------------+
[1768475392.070032] [soonh-001:115648:0]   +--------------------------+---------------------------------------------------------------------+
[1768475392.070035] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send*(fast-completion) from host memory    |
[1768475392.070036] [soonh-001:115648:0]   +--------------------------+--------------------------------------------+------------------------+
[1768475392.070039] [soonh-001:115648:0]   |                  0..2038 | short                                      | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070041] [soonh-001:115648:0]   |               2039..8184 | copy-in                                    | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070043] [soonh-001:115648:0]   |               8185..9279 | multi-frag copy-in                         | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070046] [soonh-001:115648:0]   |                9280..inf | multi-frag zero-copy                       | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070048] [soonh-001:115648:0]   +--------------------------+--------------------------------------------+------------------------+
[1768475392.070586] [soonh-001:115648:0]   +--------------------------+-----------------------------------------------------------+
[1768475392.070588] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send*(multi) from host memory    |
[1768475392.070590] [soonh-001:115648:0]   +--------------------------+----------------------------------+------------------------+
[1768475392.070593] [soonh-001:115648:0]   |                   0..514 | short                            | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070595] [soonh-001:115648:0]   |                515..8184 | zero-copy                        | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070597] [soonh-001:115648:0]   |                8185..inf | multi-frag zero-copy             | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070599] [soonh-001:115648:0]   +--------------------------+----------------------------------+------------------------+
[1768475392.070758] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.070761] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send* with reply flag from host memory    |
[1768475392.070762] [soonh-001:115648:0]   +--------------------------+-------------------------------------------+------------------------+
[1768475392.070766] [soonh-001:115648:0]   |                  0..2030 | short                                     | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070769] [soonh-001:115648:0]   |               2031..8176 | copy-in                                   | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070770] [soonh-001:115648:0]   |              8177..11552 | multi-frag copy-in                        | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070772] [soonh-001:115648:0]   |               11553..inf | multi-frag zero-copy                      | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070774] [soonh-001:115648:0]   +--------------------------+-------------------------------------------+------------------------+
[1768475392.070919] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------------------------------+
[1768475392.070923] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send* with reply flag(fast-completion) from host memory    |
[1768475392.070926] [soonh-001:115648:0]   +--------------------------+------------------------------------------------------------+------------------------+
[1768475392.070928] [soonh-001:115648:0]   |                  0..2030 | short                                                      | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070929] [soonh-001:115648:0]   |               2031..8176 | copy-in                                                    | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070932] [soonh-001:115648:0]   |               8177..9279 | multi-frag copy-in                                         | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070935] [soonh-001:115648:0]   |                9280..inf | multi-frag zero-copy                                       | rc_mlx5/mlx5_0:1/path0 |
[1768475392.070937] [soonh-001:115648:0]   +--------------------------+------------------------------------------------------------+------------------------+
[1768475392.071098] [soonh-001:115648:0]   +--------------------------+---------------------------------------------------------------------------+
[1768475392.071101] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | active message by ucp_am_send* with reply flag(multi) from host memory    |
[1768475392.071102] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------+------------------------+
[1768475392.071105] [soonh-001:115648:0]   |                   0..514 | short                                            | rc_mlx5/mlx5_0:1/path0 |
[1768475392.071106] [soonh-001:115648:0]   |                515..8176 | zero-copy                                        | rc_mlx5/mlx5_0:1/path0 |
[1768475392.071108] [soonh-001:115648:0]   |                8177..inf | multi-frag zero-copy                             | rc_mlx5/mlx5_0:1/path0 |
[1768475392.071112] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------+------------------------+
2026-01-15 03:09:52 NIXL INFO    _api.py:354 Backend UCX was instantiated
2026-01-15 03:09:52 NIXL INFO    _api.py:244 Initialized NIXL agent: initiator
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:54 NIXL agent created (listen_port=0)
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:55 Check UCX log above for transport selection!
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:56 Should see 'cuda_ipc' or 'cuda_copy', NOT 'tcp'!
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:71 Transfer size: 5.0000 GB (10 x (1024, 2, 32, 4096))
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:72 Iterations: warmup=3, test=10
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:73 ================================================================================
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:76 Registering GPU memory with NIXL...
[1768475392.100789] [soonh-001:115648:0]   +--------------------------+-------------------------------------------------------------+
[1768475392.100797] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put* from host memory to cuda    |
[1768475392.100800] [soonh-001:115648:0]   +--------------------------+------------+------------------------------------------------+
[1768475392.100803] [soonh-001:115648:0]   |                    0..2K | short      | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.100806] [soonh-001:115648:0]   |               2049..8256 | copy-in    | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.100808] [soonh-001:115648:0]   |                8257..inf | zero-copy  | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.100810] [soonh-001:115648:0]   +--------------------------+------------+------------------------------------------------+
[1768475392.100889] [soonh-001:115648:0]   +--------------------------+------------------------------------------------------------------------------+
[1768475392.100891] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(fast-completion) from host memory to cuda    |
[1768475392.100894] [soonh-001:115648:0]   +--------------------------+-----------------------------+------------------------------------------------+
[1768475392.100896] [soonh-001:115648:0]   |                    0..2K | short                       | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.100897] [soonh-001:115648:0]   |               2049..9383 | copy-in                     | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.100899] [soonh-001:115648:0]   |                9384..inf | zero-copy                   | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.100902] [soonh-001:115648:0]   +--------------------------+-----------------------------+------------------------------------------------+
[1768475392.100989] [soonh-001:115648:0]   +--------------------------+--------------------------------------------------------------------+
[1768475392.100992] [soonh-001:115648:0]   | ucp_context_0 self cfg#1 | remote memory write by ucp_put*(multi) from host memory to cuda    |
[1768475392.100994] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
[1768475392.100996] [soonh-001:115648:0]   |                  0..1395 | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475392.100999] [soonh-001:115648:0]   |                1396..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475392.101001] [soonh-001:115648:0]   +--------------------------+-------------------+------------------------------------------------+
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:81 Memory registered
2026-01-15 03:09:52 NIXL INFO    nixl_h100_nvlink.py:124
INITIATOR: Waiting for target...
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:127 INITIATOR: Connecting to 127.0.0.1:3005
[1768475394.390800] [soonh-001:115648:1]      ucp_worker.c:1903 UCX  INFO    ucp_context_0 intra-node cfg#2 rma(rc_mlx5/mlx5_0:1)  amo(rc_mlx5/mlx5_0:1)  am(rc_mlx5/mlx5_0:1 rc_mlx5/mlx5_0:1 cuda_ipc/cuda)  ka(ud_mlx5/mlx5_0:1)
[1768475394.391027] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------------------------+
[1768475394.391032] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put* from host memory to host    |
[1768475394.391033] [soonh-001:115648:1]   +--------------------------------+------------+------------------------------------------------+
[1768475394.391037] [soonh-001:115648:1]   |                          0..2K | short      | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391039] [soonh-001:115648:1]   |                     2049..8256 | copy-in    | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391041] [soonh-001:115648:1]   |                      8257..inf | zero-copy  | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391043] [soonh-001:115648:1]   +--------------------------------+------------+------------------------------------------------+
[1768475394.391125] [soonh-001:115648:1]   +--------------------------------+------------------------------------------------------------------------------+
[1768475394.391128] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(fast-completion) from host memory to host    |
[1768475394.391130] [soonh-001:115648:1]   +--------------------------------+-----------------------------+------------------------------------------------+
[1768475394.391134] [soonh-001:115648:1]   |                          0..2K | short                       | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391136] [soonh-001:115648:1]   |                     2049..9383 | copy-in                     | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391138] [soonh-001:115648:1]   |                      9384..inf | zero-copy                   | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391140] [soonh-001:115648:1]   +--------------------------------+-----------------------------+------------------------------------------------+
[1768475394.391220] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------------------------+
[1768475394.391222] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(multi) from host memory to host    |
[1768475394.391224] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
[1768475394.391226] [soonh-001:115648:1]   |                        0..1395 | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391228] [soonh-001:115648:1]   |                      1396..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391230] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
[1768475394.391553] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------------------------+
[1768475394.391556] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put* from host memory to cuda/dev[1]    |
[1768475394.391558] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
[1768475394.391560] [soonh-001:115648:1]   |                          0..2K | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391562] [soonh-001:115648:1]   |                     2049..8256 | copy-in           | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391564] [soonh-001:115648:1]   |                      8257..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391566] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
[1768475394.391641] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------------------------------------------------+
[1768475394.391644] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(fast-completion) from host memory to cuda/dev[1]    |
[1768475394.391646] [soonh-001:115648:1]   +--------------------------------+------------------------------------+------------------------------------------------+
[1768475394.391649] [soonh-001:115648:1]   |                          0..2K | short                              | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391651] [soonh-001:115648:1]   |                     2049..9383 | copy-in                            | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391653] [soonh-001:115648:1]   |                      9384..inf | zero-copy                          | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391655] [soonh-001:115648:1]   +--------------------------------+------------------------------------+------------------------------------------------+
[1768475394.391736] [soonh-001:115648:1]   +--------------------------------+---------------------------------------------------------------------------+
[1768475394.391738] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(multi) from host memory to cuda/dev[1]    |
[1768475394.391741] [soonh-001:115648:1]   +--------------------------------+--------------------------+------------------------------------------------+
[1768475394.391743] [soonh-001:115648:1]   |                        0..1395 | short                    | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.391745] [soonh-001:115648:1]   |                      1396..inf | zero-copy                | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.391747] [soonh-001:115648:1]   +--------------------------------+--------------------------+------------------------------------------------+
[1768475394.391989] [soonh-001:115648:1]   +--------------------------------+----------------------------------------------------+
[1768475394.391992] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send* from host memory    |
[1768475394.391993] [soonh-001:115648:1]   +--------------------------------+---------------------------+------------------------+
[1768475394.391997] [soonh-001:115648:1]   |                        0..2038 | short                     | rc_mlx5/mlx5_0:1/path0 |
[1768475394.391999] [soonh-001:115648:1]   |                     2039..8184 | copy-in                   | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392001] [soonh-001:115648:1]   |                    8185..11552 | multi-frag copy-in        | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392003] [soonh-001:115648:1]   |                     11553..inf | multi-frag zero-copy      | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392005] [soonh-001:115648:1]   +--------------------------------+---------------------------+------------------------+
[1768475394.392160] [soonh-001:115648:1]   +--------------------------------+---------------------------------------------------------------------+
[1768475394.392163] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send*(fast-completion) from host memory    |
[1768475394.392164] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------+------------------------+
[1768475394.392167] [soonh-001:115648:1]   |                        0..2038 | short                                      | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392170] [soonh-001:115648:1]   |                     2039..8184 | copy-in                                    | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392172] [soonh-001:115648:1]   |                     8185..9279 | multi-frag copy-in                         | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392174] [soonh-001:115648:1]   |                      9280..inf | multi-frag zero-copy                       | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392176] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------+------------------------+
[1768475394.392715] [soonh-001:115648:1]   +--------------------------------+-----------------------------------------------------------+
[1768475394.392718] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send*(multi) from host memory    |
[1768475394.392719] [soonh-001:115648:1]   +--------------------------------+----------------------------------+------------------------+
[1768475394.392722] [soonh-001:115648:1]   |                         0..514 | short                            | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392724] [soonh-001:115648:1]   |                      515..8184 | zero-copy                        | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392726] [soonh-001:115648:1]   |                      8185..inf | multi-frag zero-copy             | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392727] [soonh-001:115648:1]   +--------------------------------+----------------------------------+------------------------+
[1768475394.392884] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------------------------+
[1768475394.392887] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send* with reply flag from host memory    |
[1768475394.392888] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------+------------------------+
[1768475394.392891] [soonh-001:115648:1]   |                        0..2030 | short                                     | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392893] [soonh-001:115648:1]   |                     2031..8176 | copy-in                                   | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392896] [soonh-001:115648:1]   |                    8177..11552 | multi-frag copy-in                        | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392898] [soonh-001:115648:1]   |                     11553..inf | multi-frag zero-copy                      | rc_mlx5/mlx5_0:1/path0 |
[1768475394.392900] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------+------------------------+
[1768475394.393053] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------------------------------------------------+
[1768475394.393060] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send* with reply flag(fast-completion) from host memory    |
[1768475394.393062] [soonh-001:115648:1]   +--------------------------------+------------------------------------------------------------+------------------------+
[1768475394.393065] [soonh-001:115648:1]   |                        0..2030 | short                                                      | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393067] [soonh-001:115648:1]   |                     2031..8176 | copy-in                                                    | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393069] [soonh-001:115648:1]   |                     8177..9279 | multi-frag copy-in                                         | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393071] [soonh-001:115648:1]   |                      9280..inf | multi-frag zero-copy                                       | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393073] [soonh-001:115648:1]   +--------------------------------+------------------------------------------------------------+------------------------+
[1768475394.393241] [soonh-001:115648:1]   +--------------------------------+---------------------------------------------------------------------------+
[1768475394.393244] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send* with reply flag(multi) from host memory    |
[1768475394.393245] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------+------------------------+
[1768475394.393249] [soonh-001:115648:1]   |                         0..514 | short                                            | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393251] [soonh-001:115648:1]   |                      515..8176 | zero-copy                                        | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393253] [soonh-001:115648:1]   |                      8177..inf | multi-frag zero-copy                             | rc_mlx5/mlx5_0:1/path0 |
[1768475394.393256] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------+------------------------+
[1768475394.569407] [soonh-001:115648:1]   +--------------------------------+-------------------------------------------------------------+
[1768475394.569416] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put* from host memory to cuda    |
[1768475394.569418] [soonh-001:115648:1]   +--------------------------------+------------+------------------------------------------------+
[1768475394.569421] [soonh-001:115648:1]   |                          0..2K | short      | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.569423] [soonh-001:115648:1]   |                     2049..8256 | copy-in    | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.569424] [soonh-001:115648:1]   |                      8257..inf | zero-copy  | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.569425] [soonh-001:115648:1]   +--------------------------------+------------+------------------------------------------------+
[1768475394.569503] [soonh-001:115648:1]   +--------------------------------+------------------------------------------------------------------------------+
[1768475394.569507] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(fast-completion) from host memory to cuda    |
[1768475394.569508] [soonh-001:115648:1]   +--------------------------------+-----------------------------+------------------------------------------------+
[1768475394.569512] [soonh-001:115648:1]   |                          0..2K | short                       | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.569515] [soonh-001:115648:1]   |                     2049..9383 | copy-in                     | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.569517] [soonh-001:115648:1]   |                      9384..inf | zero-copy                   | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.569520] [soonh-001:115648:1]   +--------------------------------+-----------------------------+------------------------------------------------+
[1768475394.569600] [soonh-001:115648:1]   +--------------------------------+--------------------------------------------------------------------+
[1768475394.569603] [soonh-001:115648:1]   | ucp_context_0 intra-node cfg#2 | remote memory write by ucp_put*(multi) from host memory to cuda    |
[1768475394.569604] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
[1768475394.569606] [soonh-001:115648:1]   |                        0..1395 | short             | rc_mlx5/mlx5_0:1/path0                         |
[1768475394.569609] [soonh-001:115648:1]   |                      1396..inf | zero-copy         | rc_mlx5/mlx5_0:1 50% on path0 and 50% on path1 |
[1768475394.569611] [soonh-001:115648:1]   +--------------------------------+-------------------+------------------------------------------------+
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:157 INITIATOR: Connected and ready
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:158 ================================================================================
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:163
WARMUP PHASE
[1768475394.672061] [soonh-001:115648:0]   +--------------------------------+-------------------------------------------------------------------+
[1768475394.672068] [soonh-001:115648:0]   | ucp_context_0 intra-node cfg#2 | remote memory read by ucp_get*(multi) into cuda/GPU1 from cuda    |
[1768475394.672071] [soonh-001:115648:0]   +--------------------------------+------------------------------------------+------------------------+
[1768475394.672072] [soonh-001:115648:0]   |                              0 | copy-out                                 | rc_mlx5/mlx5_0:1/path0 |
[1768475394.672074] [soonh-001:115648:0]   |                         1..inf | zero-copy                                | cuda_ipc/cuda          |
[1768475394.672076] [soonh-001:115648:0]   +--------------------------------+------------------------------------------+------------------------+
[1768475394.688032] [soonh-001:115648:0]   +--------------------------------+---------------------------------------------------------+
[1768475394.688041] [soonh-001:115648:0]   | ucp_context_0 intra-node cfg#2 | active message by ucp_am_send*(egr) from host memory    |
[1768475394.688044] [soonh-001:115648:0]   +--------------------------------+--------------------------------+------------------------+
[1768475394.688045] [soonh-001:115648:0]   |                        0..2038 | short                          | rc_mlx5/mlx5_0:1/path0 |
[1768475394.688048] [soonh-001:115648:0]   |                     2039..8184 | copy-in                        | rc_mlx5/mlx5_0:1/path0 |
[1768475394.688049] [soonh-001:115648:0]   |                    8185..11552 | multi-frag copy-in             | rc_mlx5/mlx5_0:1/path0 |
[1768475394.688051] [soonh-001:115648:0]   |                     11553..inf | multi-frag zero-copy           | rc_mlx5/mlx5_0:1/path0 |
[1768475394.688054] [soonh-001:115648:0]   +--------------------------------+--------------------------------+------------------------+
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:198 Warmup 1: 0.0226s = 221.46 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:198 Warmup 2: 0.0220s = 227.14 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:198 Warmup 3: 0.0217s = 230.09 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:202
TEST PHASE
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 1: 0.0220s = 227.46 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 2: 0.0209s = 239.22 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 3: 0.0206s = 242.96 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 4: 0.0204s = 245.32 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 5: 0.0208s = 240.30 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 6: 0.0206s = 242.96 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 7: 0.0208s = 240.31 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 8: 0.0207s = 241.90 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 9: 0.0209s = 239.46 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:238 Test 10: 0.0207s = 241.86 GB/s
2026-01-15 03:09:54 NIXL INFO    nixl_h100_nvlink.py:242
Verifying data...
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:245 ✓ Data verification PASSED
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:259
================================================================================
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:260 FINAL RESULTS
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:261 ================================================================================
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:262 Transfer size: 5.0000 GB
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:263 Iterations: 10
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:264 --------------------------------------------------------------------------------
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:265 Mean bandwidth: 240.09 GB/s
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:266 Peak bandwidth: 245.32 GB/s
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:267 Min bandwidth:  227.46 GB/s
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:268 --------------------------------------------------------------------------------
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:269 Mean time: 0.0208s (±0.0004s)
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:270 ================================================================================
2026-01-15 03:09:55 NIXL INFO    nixl_h100_nvlink.py:276
Test complete!

```


### brminich · 2026-01-30

@Archmilio I see  in your logs that cuda_ipc is indeed used for gpu to gpu reads
```
68475394.672061] [soonh-001:115648:0]   +--------------------------------+-------------------------------------------------------------------+
[1768475394.672068] [soonh-001:115648:0]   | ucp_context_0 intra-node cfg#2 | remote memory read by ucp_get*(multi) into cuda/GPU1 from cuda    |
[1768475394.672071] [soonh-001:115648:0]   +--------------------------------+------------------------------------------+------------------------+
[1768475394.672072] [soonh-001:115648:0]   |                              0 | copy-out                                 | rc_mlx5/mlx5_0:1/path0 |
[1768475394.672074] [soonh-001:115648:0]   |                         1..inf | zero-copy                                | cuda_ipc/cuda          |
[1768475394.672076] [soonh-001:115648:0]   +--------------------------------+------------------------------------------+------------------------+
```
If you remove RC transports there is nothing left for notifs (cuda_ips does not support it), that's why it fails
