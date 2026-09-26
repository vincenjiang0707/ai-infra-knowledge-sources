# [Issue #2022] [collective op][cuda graph] capture collective ops but got an HIP error: operation not permitted when stream is capturing

source: https://github.com/ROCm/rccl/issues/2022
state: closed | updated: 2026-03-25T08:22:25Z
labels: status: assessed

## 正文

### Problem Description

Hi, all

We are LLM developers and running the LLM models on MI355*8 single node. We have encountered an cuda graph(hip graph) capture issue when launching our LLM application. It is urgent issue and may block the customer's project.
After deep dive, we have found the `torch.dist.all_reduce` cannot be captured by cuda graph.
Here is the associated code:
https://github.com/ROCm/vllm/blob/dev/perf/vllm/v1/worker/dp_utils.py#L52

Here is the small reproducer python file:
```
import os
import torch
import torch.distributed as dist
import multiprocessing as mp

def worker(rank, world_size):
    os.environ['MASTER_ADDR'] = '127.0.0.1'
    os.environ['MASTER_PORT'] = '29502'
    os.environ['RANK'] = str(rank)
    os.environ['WORLD_SIZE'] = str(world_size)
    os.environ['LOCAL_RANK'] = str(rank)

    device = torch.device(f"cuda:{rank}")
    torch.cuda.set_device(device)

    backend = "nccl"
    dist.init_process_group(backend=backend, rank=rank, world_size=world_size)

    tensor = torch.ones(1, device=device, dtype=torch.float32)
    group = dist.group.WORLD

    graph = torch.cuda.CUDAGraph()
    stream = torch.cuda.Stream()

    try:
        with torch.cuda.stream(stream):
            graph.capture_begin()
            tensor += 1.0
            dist.all_reduce(tensor, group=group)
            graph.capture_end()
        print(f"Rank {rank}: Unexpected success")
    except Exception as e:
        print(f"Rank {rank}: Expected failure - {e}")

    dist.destroy_process_group()

def main():
    world_size = 8
    if torch.cuda.device_count() < world_size:
        print(f"Error: {world_size} GPUs required, but only {torch.cuda.device_count()} available")
        return

    ctx = mp.get_context("spawn")
    processes = []
    for rank in range(world_size):
        p = ctx.Process(target=worker, args=(rank, world_size))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
```
The reproducing command is `python -u reproducer.py`.

Then the issue can be reproduced. Here is the error log. The core error message is **operation not permitted when stream is capturing**
```
Rank 6: Expected failure - NCCL error in: /app/pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:94, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.27.7
ncclUnhandledCudaError: Call to CUDA function failed.
Last error:
Cuda failure 'operation not permitted when stream is capturing'
terminate called after throwing an instance of 'c10::AcceleratorError'
  what():  HIP error: operation not permitted when stream is capturing
Search for `hipErrorStreamCaptureUnsupported' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

Exception raised from c10_hip_check_implementation at /app/pytorch/c10/hip/HIPException.cpp:45 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x9c (0x7fe5b9c341bc in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x374e1 (0x7fe5eaa6d4e1 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10_hip.so)
frame #2: c10::hip::c10_hip_check_implementation(int, char const*, char const*, int, bool) + 0x1f1 (0x7fe5eaa6d371 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10_hip.so)
frame #3: at::cuda::CUDAGraph::~CUDAGraph() + 0xb9 (0x7fe5ed360e59 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_hip.so)
frame #4: <unknown function> + 0xd479b6 (0x7fe600a6d9b6 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_python.so)
frame #5: <unknown function> + 0xd47c4a (0x7fe600a6dc4a in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_python.so)
frame #6: <unknown function> + 0x3c8520 (0x7fe6000ee520 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_python.so)
frame #7: <unknown function> + 0x3c8bc5 (0x7fe6000eebc5 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_python.so)
frame #8: /usr/bin/python() [0x59e53d]
frame #9: /usr/bin/python() [0x566be8]
frame #10: _PyEval_EvalFrameDefault + 0xb11 (0x54a6f1 in /usr/bin/python)
frame #11: PyEval_EvalCode + 0x99 (0x620799 in /usr/bin/python)
frame #12: /usr/bin/python() [0x65c44b]
frame #13: /usr/bin/python() [0x6574d6]
frame #14: PyRun_StringFlags + 0x63 (0x653403 in /usr/bin/python)
frame #15: PyRun_SimpleStringFlags + 0x3e (0x65310e in /usr/bin/python)
frame #16: Py_RunMain + 0x4b2 (0x650742 in /usr/bin/python)
frame #17: Py_BytesMain + 0x2d (0x60962d in /usr/bin/python)
frame #18: <unknown function> + 0x29d90 (0x7fe601887d90 in /lib/x86_64-linux-gnu/libc.so.6)
frame #19: __libc_start_main + 0x80 (0x7fe601887e40 in /lib/x86_64-linux-gnu/libc.so.6)
frame #20: _start + 0x25 (0x6094a5 in /usr/bin/python)
```

We have checked the RCCL commit and found there is one commit that sync with NCCL 2.9 version code and support the cuda graph capture for collective ops. Here is the associated commit:
https://github.com/ROCm/rccl/commit/6021329af0a510abeab15280786644f4f1eaf840#diff-6445d3902b6d88df81be2bc5a58abf93b3aa3417132fdf27a0659815d20ec719

However, we have still found the capture failure issue for RCCL allreduce.
The using RCCL version is 2.27.7
```
root@smci355-ccs-aus-m01-25:/home/zejchen/rocm_vllm/vllm/evaluation/dp_attn# python -c "import torch; print(f'NCCL version: {torch.cuda.nccl.version()}')"
NCCL version: (2, 27, 7)
```

Thank you.

### Operating System

Ubuntu 22.04.5 LTS

### CPU

AMD EPYC 9575F 64-Core Processor

### GPU

AMD MI355*8

### ROCm Version

ROCm 7.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (12)

### zejunchen-zejun · 2025-10-31

Hi, @wenkaidu @gilbertlee-amd 
Could you help take a look?
Thank you

### thananon · 2025-10-31

Hi, we have encountered this issue before and this is due to ROCm 7.0 behavior change to match CUDA. We no longer allow certain operations when graph is capturing.

In most case, including this one (from the attached log) is originated from PyTorch c10d, not RCCL. We have been working with PyTorch team to investigate this issue.

To further debug this, you can set `AMD_LOG_LEVEL=4` and see grep for `hipError`. You should see the offending call that invalidated the graph during graph capturing.


### zejunchen-zejun · 2025-11-01

Hi, @thananon 

Thank you for help!
`we have encountered this issue before and this is due to ROCm 7.0 behavior change to match CUDA. We no longer allow certain operations when graph is capturing.`
Thank you for explanation. You mean the **torch.dist.all_reduce** also cannot be captured by cuda graph, so the ROCm 7.0 has been already aligned with CUDA behavior for now right?

`To further debug this, you can set AMD_LOG_LEVEL=4 and see grep for hipError. You should see the offending call that invalidated the graph during graph capturing.`
I add the env flag and rerun the reproducer file. The piece of log is shown as below:

```
:3:hip_device.cpp           :661 : 695595924030 us: [pid:516671 tid: 0x7efdb4954000] hipGetDevicePropertiesR0600: Returned hipSuccess :
:3:hip_device_runtime.cpp   :687 : 695595924963 us: [pid:516671 tid: 0x7efdb4954000] ^[[32m hipGetDevice ( 0x7ffc469db394 ) ^[[0m
:3:hip_device_runtime.cpp   :699 : 695595924967 us: [pid:516671 tid: 0x7efdb4954000] hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :687 : 695595925034 us: [pid:516671 tid: 0x7efdb4954000] ^[[32m hipGetDevice ( 0x7ffc469db2cc ) ^[[0m
:3:hip_device_runtime.cpp   :699 : 695595925037 us: [pid:516671 tid: 0x7efdb4954000] hipGetDevice: Returned hipSuccess : 0
:3:hip_memory.cpp           :775 : 695595925075 us: [pid:516671 tid: 0x7efdb4954000] ^[[32m hipFree ( char array:<null> ) ^[[0m
:3:hip_memory.cpp           :776 : 695595925077 us: [pid:516671 tid: 0x7efdb4954000] hipFree: Returned hipErrorStreamCaptureUnsupported :
:3:hip_device_runtime.cpp   :687 : 695595925152 us: [pid:516673 tid: 0x7f0d18d4e000] ^[[32m hipGetDevice ( 0x7fffd6ba5d64 ) ^[[0m
:3:hip_device_runtime.cpp   :687 : 695595925152 us: [pid:516676 tid: 0x7ff56ee9a000] ^[[32m hipGetDevice ( 0x7ffcd08226b4 ) ^[[0m
:3:hip_device_runtime.cpp   :687 : 695595925155 us: [pid:516678 tid: 0x7ff08cbfb000] ^[[32m hipGetDevice ( 0x7ffd4561dfc4 ) ^[[0m
:3:hip_device_runtime.cpp   :687 : 695595925156 us: [pid:516674 tid: 0x7f4b2216b000] ^[[32m hipGetDevice ( 0x7fffdf18eb24 ) ^[[0m
```

From the above log, it seems the **hipFree** is called by `torch.dist.all_reduce` and are not supported to be captured by hip graph.
`hip_memory.cpp           :776 : 695595925077 us: [pid:516671 tid: 0x7efdb4954000] hipFree: Returned hipErrorStreamCaptureUnsupported`

May I know if there is any plan to support capture it ? Or we need to align with CUDA behavior because AMD lets users use torch.cuda for their application.

Thank you for help.
CC: @wuhuikx 

### amd-nicknick · 2025-11-03

Hi @thananon, I inspected this issue further and it seems to be this line offending stream capture:
https://github.com/ROCm/rccl/blob/62ab7a22d741ab4f214b6b185b77d030ba7bb85b/src/init.cc#L2442

Is this `hipFree` call expected here?

Call stack from torch:
<img width="1306" height="192" alt="Image" src="https://github.com/user-attachments/assets/3ea1ff87-af10-4259-9eb0-0aa92fd099c4" />

Disassembling `ncclCommInitRankDev` also confirms it is a `hipFree` call with `NULL`
<img width="1378" height="101" alt="Image" src="https://github.com/user-attachments/assets/db97e6a5-810d-4463-8991-3e42ec2dcc1a" />

I'm curious if NCCL would occur the same problem, @zejunchen-zejun, could you try your reproducer on a Nvidia system to confirm? It seems like this line originates from NCCL and is still present there.

### zejunchen-zejun · 2025-11-03

Hi, @amd-nicknick 
Thank you for help.
We will run the reproducer on B200 machine and check the behavior.

### wuhuikx · 2025-11-03

cc @sunway513 @HaiShaw @carlushuang for awareness.

### zejunchen-zejun · 2025-11-03

Hi, @amd-nicknick @thananon 
I tested the reproducer on B200 and the behavior is `torch.dist.all_reduce cannot be captured by cuda graph on NV platform`.
So I think the ROCm's behavior does match the CUDA.

Here is the log I got on B200:
```
Rank 0: Expected failure - NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:94, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.27.5
ncclUnhandledCudaError: Call to CUDA function failed.
Last error:
Cuda failure 'operation not permitted when stream is capturing'
```

### amd-nicknick · 2025-11-04

Hi @zejunchen-zejun, thanks for trying out on NV system. I dug deeper into PyTorch and my initial speculation is this is expected.
In the repro script you provided, the NCCL communication is initialized lazily (on first `all_reduce`). But since graph capture had already started, it cannot be do so. (@thananon please correct me if my understanding is incorrect.)

If `device_id` is passed into `dist.init_process_group`, it will trigger PyTorch to eagerly initialize NCCL comm, which your repro script will no longer fail, and the HIP graph can be replayed correctly.
```
device = torch.device(f"cuda:{rank}")
torch.cuda.set_device(device)
dist.init_process_group(backend=backend, rank=rank, world_size=world_size, device_id=device)
```

Please give this change a try, it also means that vllm is tripping over some other problem, let's track that on the original ticket: https://github.com/ROCm/hip/issues/3876

### thananon · 2025-11-04

Hi, yes. This should match CUDA behavior.

```
hipFree: Returned hipErrorStreamCaptureUnsupported :
```

From what we see here, RCCL is initializing and try to call `hipFree()`. I think `hipFree()` is on a default stream and that stream is in capturing mode which is now prohibited. The solution would be to initialize RCCL outside of stream capturing. If you scroll up on your log, you should see that the stream is getting into capture mode prior to this line and we should figure out who is calling stream capture. I do not think that is RCCL.


I think what @amd-nicknick suggested could work.

### zejunchen-zejun · 2025-11-05

Hi, @amd-nicknick @thananon 
Thank you for help. You are right. It makes perfect sense.
The first torch.dist op will trigger the lazy initialization of RCCL, which calls the hipFree internally. This runtime op will block the cuda graph capture. That's why the reproducer failed.
When we move one torch.dist op outside of the cuda graph capture context to trigger the initialization, the reproducer run successfully and there is no such error seen.

The vllm(our application) has the same issue. The first communication op in vllm is torch.dist.all_reduce, which leads to the hip error: hipErrorStreamCaptureUnsupported.
But here key question is the torch.dist.all_reduce is **not** under the cuda graph capture context, so it **shouldn't** be captured by hip graph. Let's move the question to the original issue: https://github.com/ROCm/hip/issues/3876

Thank you.

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2785

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
