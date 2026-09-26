# [Issue #1762] [Issue]: Mismatch in function signature of Primitives constructor

source: https://github.com/ROCm/rccl/issues/1762
state: closed | updated: 2025-07-18T14:11:29Z
labels: Under Investigation

## 正文

### Problem Description

For Primitives object constructor, the function signature is different for different protocols.
Simple:
```
Primitives(
      int tid, int nthreads, int const *recvPeers, int const *sendPeers,
      void const *inputBuf, void *outputBuf, uint64_t redOpArg, uint8_t group=0,
      uint8_t connIndexRecv = 0, uint8_t connIndexSend = 0, struct ncclDevWorkColl* collWork = nullptr,
      struct ncclDevWorkP2p* p2pWork = nullptr, int stepSize_ = 0, int mode = primsModeDefault
    )

```
LL/LL128:
```
Primitives(
      const int tid, const int nthreads, int const *recvPeers, int const *sendPeers,
      void const *inputBuf, void *outputBuf, uint64_t redOpArg, uint8_t group=0,
      uint8_t connIndexRecv=0, uint8_t connIndexSend=0, struct ncclDevWorkColl* e = nullptr,
      bool ipcReg = false, bool netReg = false, int stepSize_ = 0
    )

```
This caused issues in device collective headers. For example in src/device/all_gather.h. The way prims obj is constructed applies to all 3 protocols:

```
Primitives<T, RedOp, FanSymmetric<1>, 0, Proto, 0, isNetOffload> prims
        (tid, workNthreads, &ring->prev, &ring->next, inputBuf, outputBuf, work->redOpArg, 0, work->connIndex, work->connIndex, work, NULL, isNetOffload ? NCCL_MAX_NET_SIZE : 0);
```

As a result, I encounter following build error:

```
buck-out/v2/gen/fbsource/20f942d859d3bbba/third-party/rccl/__rccl_objects__/buck-headers/all_gather.h:73:135: error: implicit conversion of NULL constant to 'bool' [-Werror,-Wnull-conversion]
   72 |       Primitives<T, RedOp, FanSymmetric<1>, 0, Proto, 0, isNetOffload> prims
   73 |         (tid, workNthreads, &ring->prev, &ring->next, inputBuf, outputBuf, work->redOpArg, 0, work->connIndex, work->connIndex, work, NULL, isNetOffload ? NCCL_MAX_NET_SIZE : 0);
      |                                                                                                                                       ^~~~
      |                                                                                                                                       false
buck-out/v2/gen/fbsource/20f942d859d3bbba/third-party/rccl/__rccl_objects__/buck-headers/all_gather.h:209:5: note: in instantiation of function template specialization '(anonymous namespace)::runRing<signed char, FuncSum<signed char>, ProtoLL, 4, false>' requested here
  209 |     runRing<T, RedOp, ProtoLL, COLL_UNROLL>(tid, nthreads, work);
```

I have to explicitly add "-Wno-error=null-conversion" in compiler flag to suppress the error. It seems that neither passing null pointer to bool variable ipcReg or passing `isNetOffload ? NCCL_MAX_NET_SIZE : 0` to bool variable is `netReg` is intended. So suppressing this compiler error seems very risky.

Tested on RCCL commit 12315c25 06/19/2025. Please take a look

### Operating System

Linux 6.4

### CPU

AMD EPYC 9654 96-Core Processor

### GPU

AMD instinct mi300x

### ROCm Version

6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### ppanchad-amd · 2025-06-24

Hi @dmwu. Internal ticket has been created to investigate this issue. Thanks!

### tcgu-amd · 2025-07-07

Hi @dmwu, sorry for the delay the response, and thanks for reaching out! This indeed appears to be a bug due to a recent merge from upstream. A fix will be available in a future update soon. Thanks! 

### tcgu-amd · 2025-07-17

Hi @dmwu, I have created a patch https://github.com/ROCm/rccl/pull/1819/files. This is temporary workaround that should fix the issue you are seeing. However, the definitive fix where the discrepancies between the constructor signatures are resolved is going to have to come from NCCL upstream. Thanks!
