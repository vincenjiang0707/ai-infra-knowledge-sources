# [Issue #2106] [Issue]: segfault at cuMemCreate of ncclCuMemHostEnable in "misc/cudawrap.cc"

source: https://github.com/NVIDIA/nccl/issues/2106
state: open | updated: 2026-09-03T08:07:54Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

When running sglang with a Qwen3.5 model, a segmentation fault occurs at a very early stage. The following is the stack trace:

```bash
> !!!!!!! Segfault encountered !!!!!!!
>   File "./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c", line 0, in 0x00007d8764c4532f
>   File "./nptl/pthread_kill.c", line 44, in __pthread_kill_implementation
>   File "./nptl/pthread_kill.c", line 78, in __pthread_kill_internal
>   File "./nptl/pthread_kill.c", line 89, in __GI___pthread_kill
>   File "../sysdeps/posix/raise.c", line 26, in __GI_raise
>   File "./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c", line 0, in 0x00007d8764c4532f
>   File "<unknown>", line 0, in cuMemCreate
>   File "misc/cudawrap.cc", line 92, in ncclCuMemHostEnable()
>   File "misc/cudawrap.cc", line 202, in ncclCuMemHostEnable()
>   File "misc/cudawrap.cc", line 280, in initOnceFunc
>   File "./nptl/pthread_once.c", line 116, in __pthread_once_slow
>   File "misc/cudawrap.cc", line 298, in ncclCudaLibraryInit()
>   File "/dvs/p4/build/sw/gpgpu/nccl/gitfusion/stable/src/init.cc", line 1852, in ncclCommInitRank
>   File "<unknown>", line 0, in ffi_call
>   File "<unknown>", line 0, in _PyObject_MakeTpCall
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in _PyObject_Call_Prepend
>   File "<unknown>", line 0, in _PyObject_MakeTpCall
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in _PyObject_Call_Prepend
>   File "<unknown>", line 0, in _PyObject_MakeTpCall
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in _PyObject_Call_Prepend
>   File "<unknown>", line 0, in PyObject_Call
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in _PyObject_Call_Prepend
>   File "<unknown>", line 0, in PyObject_Call
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in _PyObject_Call_Prepend
>   File "<unknown>", line 0, in _PyObject_MakeTpCall
>   File "<unknown>", line 0, in _PyEval_EvalFrameDefault
>   File "<unknown>", line 0, in PyEval_EvalCode
>   File "<unknown>", line 0, in PyRun_StringFlags
>   File "<unknown>", line 0, in PyRun_SimpleStringFlags
>   File "<unknown>", line 0, in Py_RunMain
>   File "<unknown>", line 0, in Py_BytesMain
>   File "<unknown>", line 0, in _start
>   File "<unknown>", line 0, in 0xffffffffffffffff
> 
```

### Steps to Reproduce the Issue

I found that the issue occurs on two AMD EPYC servers with RTX 4090 GPUs, but never on Intel platforms (yet). Interestingly, other AMD servers do not exhibit this problem.

Below is a minimal NCCL example that reproduces the segmentation fault on the affected servers. After setting NCCL_CUMEM_HOST_ENABLE=0, both the NCCL test program and sglang run correctly.

The problematic commit was identified using git bisect. See the log below:

```
git bisect start
# status: waiting for both good and bad commits
# bad: [6da422082f910a8dd230f7e42e26ece4dc37bccc] Merge NCCL 2.30.3-1 release to master
git bisect bad 6da422082f910a8dd230f7e42e26ece4dc37bccc
# status: waiting for good commit(s), bad commit known
# good: [80f6bda4378b99d99e82b4d76a633791cc45fef0] NCCL 2.25.1-1
git bisect good 80f6bda4378b99d99e82b4d76a633791cc45fef0
# bad: [cc36cea3a7e321eea8cc75b158996f6dca44bd4c] Bring in GPUNetIO v2.0.1-rc1
git bisect bad cc36cea3a7e321eea8cc75b158996f6dca44bd4c
# bad: [8df9d2443cafdd89050db1e93be8a1f70b0a58fc] adds avg operator to non-gin symk reduce scatter kernels
git bisect bad 8df9d2443cafdd89050db1e93be8a1f70b0a58fc
# bad: [59242d7c385fa91f68e19a1327b1cde0c485b291] Add inspector's extract_git_version.sh to fix build issue
git bisect bad 59242d7c385fa91f68e19a1327b1cde0c485b291
# bad: [0d1ece2b43ba1d85c76746ce63505f6db6b6b2f4] Exclude ongoing issues from auto-closing logic
git bisect bad 0d1ece2b43ba1d85c76746ce63505f6db6b6b2f4
# bad: [8171af656bb3c47c8fc60b7cd49ae0c7494de664] NCCL 2.26.6-1
git bisect bad 8171af656bb3c47c8fc60b7cd49ae0c7494de664
# good: [145e67e70745c5f78f18334f82de29dbe59bde63] Update ext-profiler example
git bisect good 145e67e70745c5f78f18334f82de29dbe59bde63
# bad: [3000e3c797b4b236221188c07aa09c1f3a0170d4] NCCL 2.26.5-1
git bisect bad 3000e3c797b4b236221188c07aa09c1f3a0170d4
# bad: [0524aef7a0333bc79d885e392812519087eab71f] NCCL 2.26.3-1
git bisect bad 0524aef7a0333bc79d885e392812519087eab71f
# first bad commit: [0524aef7a0333bc79d885e392812519087eab71f] NCCL 2.26.3-1
```

```
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <nccl.h>

#define CHECK_CUDA(cmd) do {                         \
    cudaError_t e = cmd;                             \
    if (e != cudaSuccess) {                          \
        printf("CUDA error %s:%d '%s'\n",            \
               __FILE__, __LINE__, cudaGetErrorString(e)); \
        exit(EXIT_FAILURE);                          \
    }                                                \
} while(0)

#define CHECK_NCCL(cmd) do {                         \
    ncclResult_t r = cmd;                            \
    if (r != ncclSuccess) {                          \
        printf("NCCL error %s:%d '%s'\n",            \
               __FILE__, __LINE__, ncclGetErrorString(r)); \
        exit(EXIT_FAILURE);                          \
    }                                                \
} while(0)

int main() {
    int nDev = 2;
    int devs[2] = {0, 1};

    ncclComm_t comms[2];
    cudaStream_t streams[2];

    // 每个 GPU 上的数据
    float *sendbuff[2];
    float *recvbuff[2];

    size_t count = 4;

    // 初始化 communicator
    CHECK_NCCL(ncclCommInitAll(comms, nDev, devs));

    for (int i = 0; i < nDev; i++) {
        CHECK_CUDA(cudaSetDevice(devs[i]));
        CHECK_CUDA(cudaStreamCreate(&streams[i]));

        CHECK_CUDA(cudaMalloc(&sendbuff[i], count * sizeof(float)));
        CHECK_CUDA(cudaMalloc(&recvbuff[i], count * sizeof(float)));

        float host[4] = {1.0f * (i+1), 2.0f, 3.0f, 4.0f};
        CHECK_CUDA(cudaMemcpy(sendbuff[i], host,
                              count * sizeof(float),
                              cudaMemcpyHostToDevice));
    }

    // 启动 group（推荐写法）
    CHECK_NCCL(ncclGroupStart());
    for (int i = 0; i < nDev; i++) {
        CHECK_CUDA(cudaSetDevice(devs[i]));
        CHECK_NCCL(ncclAllReduce(
            sendbuff[i],
            recvbuff[i],
            count,
            ncclFloat,
            ncclSum,
            comms[i],
            streams[i]
        ));
    }
    CHECK_NCCL(ncclGroupEnd());

    // 等待完成
    for (int i = 0; i < nDev; i++) {
        CHECK_CUDA(cudaSetDevice(devs[i]));
        CHECK_CUDA(cudaStreamSynchronize(streams[i]));
    }

    // 打印结果
    for (int i = 0; i < nDev; i++) {
        float host[4];
        CHECK_CUDA(cudaMemcpy(host, recvbuff[i],
                              count * sizeof(float),
                              cudaMemcpyDeviceToHost));
        printf("GPU %d result: ", i);
        for (int j = 0; j < count; j++) {
            printf("%f ", host[j]);
        }
        printf("\n");
    }

    // 释放资源
    for (int i = 0; i < nDev; i++) {
        cudaSetDevice(devs[i]);
        cudaFree(sendbuff[i]);
        cudaFree(recvbuff[i]);
        cudaStreamDestroy(streams[i]);
        ncclCommDestroy(comms[i]);
    }

    return 0;
}
```

backtrace of above program in gdb:
```
(gdb) where
#0  0x00007fffdb4ccf82 in ?? () from /lib/x86_64-linux-gnu/libcuda.so.1
#1  0x00007fffdb3c0aa4 in ?? () from /lib/x86_64-linux-gnu/libcuda.so.1
#2  0x00007fffdb54879a in ?? () from /lib/x86_64-linux-gnu/libcuda.so.1
#3  0x00007fffdb52d030 in cuMemCreate () from /lib/x86_64-linux-gnu/libcuda.so.1
#4  0x00007fffe18b7182 in ncclCuMemHostEnable () at misc/cudawrap.cc:92
#5  0x00007fffe18b7c65 in ncclCuMemHostEnable () at misc/cudawrap.cc:193
#6  initOnceFunc () at misc/cudawrap.cc:271
#7  0x00007fffe14a1ed3 in __pthread_once_slow (once_control=0x7ffff7dc9c7c <initOnceControl>, init_routine=0x7fffe18b75d0 <initOnceFunc()>) at ./nptl/pthread_once.c:116
#8  0x00007fffe18b7d6b in ncclCudaLibraryInit () at misc/cudawrap.cc:289
#9  0x00007fffe18718ed in ncclCommInitAll (comms=0x7fffffffe0f0, ndev=2, devlist=0x7fffffffe0e8) at init.cc:1749
#10 0x000055555555cc66 in main ()
```
### NCCL Version

2.27.5, or v2.26.3-1 from git bisect

### Your platform details

_No response_

### Error Message & Behavior

From the stack trace, it appears that the issue is triggered by the call to cuMemCreate(&handle, size, &prop, 0) at https://github.com/NVIDIA/nccl/commit/0524aef7a0333bc79d885e392812519087eab71f#diff-1eee8b00ab7a805ce4827cc73de73908f945f739c24fd3aea034f7f9b15d817fR92. However, it is unclear whether the root cause lies in NCCL, the libnvidia-compute library, or even a hardware-related issue.

## 评论 (7)

### clan · 2026-04-17

It seems the issue is related to the NUMA memory configuration: each node is expected to have associated memory, and if not, a segmentation fault occurs.

In that case, could this be a bug in libcuda.so.1? I mean, it should report an error instead of causing a segmentation fault.

### mueslo · 2026-07-24

We also encountered this (in current vLLM, nccl==2.28.9, after Nvidia Driver 535 --> 580 migration, with confirmed memory-less NUMA nodes) and managed to fix it by setting `NCCL_CUMEM_HOST_ENABLE=0`

### xiaofanl-nvidia · 2026-07-25

Thanks @mueslo @clan I've passed the info to CUDA team.. Will let you know if we can confirm where the issue could be.. 

### xiaofanl-nvidia · 2026-07-27

CUDA team suspects this is a bug we fixed in CUDA driver. The fix should be available in r595 and above drivers. 
@clan @mueslo could you try this out to confirm the issue is gone with newer drivers? 

BTW, in terms of CUMEM HOST impact on NCCL: 

NCCL_CUMEM_HOST_ENABLE primarily selects the backing mechanism for the intra-node SHM transport.
  - Enabled, together with NCCL_CUMEM_ENABLE: SHM buffers use NUMA-aware pinned cuMem allocations and CUDA handle export/import.
  - Disabled: SHM falls back to the legacy /dev/shm/mmap implementation.

Therefore, disabling it does not disable collectives, P2P, or SHM communication—it changes the allocation/IPC mechanism.

It also affects:
  - Communicator-abort reliability: the proxy has an additional connection-closing path when cuMem host allocations are active. 
  - Avoiding /dev/shm size and cleanup problems, at the cost of requiring working NUMA support. The user guide explicitly describes improved abort reliability.

### clan · 2026-07-27

> CUDA team suspects this is a bug we fixed in CUDA driver. The fix should be available in r595 and above drivers. [@clan](https://github.com/clan) [@mueslo](https://github.com/mueslo) could you try this out to confirm the issue is gone with newer drivers?

thanks, but I don't have the hardware with the asymmetric NUMA memory on hand. One can test it by using the program above before and after updating the CUDA driver to confirm whether this issue has been solved.


### XingZYu · 2026-09-03

Hi @clan, @xiaofanl-nvidia, @mueslo,

We encountered a similar `cuMemCreate(HOST_NUMA)` issue and successfully traced it to asymmetric CPU/NUMA topology information. Our detailed analysis in [issue 2190](https://github.com/NVIDIA/nccl/issues/2190#issuecomment-5521603669) may help diagnose this case.

### clan · 2026-09-03

yes, see my analysis of the problem and possible solution (in Chinese): https://mp.weixin.qq.com/s/XOpiKAVC0G_T9L5R4afNIQ
