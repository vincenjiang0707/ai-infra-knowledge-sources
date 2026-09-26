# [Issue #2380] [Issue]: segment fault at ncclTuningCostModelInit tracing

source: https://github.com/NVIDIA/nccl/issues/2380
state: closed | updated: 2026-09-08T21:09:16Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

```
2026-08-31 12:27:50 [k8s-slave03:00956] *** Process received signal ***
2026-08-31 12:27:50 [k8s-slave03:00956] Signal: Segmentation fault (11)
2026-08-31 12:27:50 [k8s-slave03:00956] Signal code:  (-6)
2026-08-31 12:27:50 [k8s-slave03:00956] Failing at address: 0x3bc
2026-08-31 12:27:50 [k8s-slave03:00956] [ 0] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x45330)[0x7d1d0c3eb330]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 1] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x19badc)[0x7d1d0c541adc]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 2] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x6ada8)[0x7d1d0c410da8]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 3] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x6b5a2)[0x7d1d0c4115a2]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 4] /usr/local/nccl/lib/libnccl.so.2(+0xbd72c)[0x7d1d0c8f372c]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 5] /usr/local/nccl/lib/libnccl.so.2(+0xbe74b)[0x7d1d0c8f474b]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 6] /usr/local/nccl/lib/libnccl.so.2(+0x246023)[0x7d1d0ca7c023]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 7] /usr/local/nccl/lib/libnccl.so.2(+0x24a248)[0x7d1d0ca80248]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 8] /usr/local/nccl/lib/libnccl.so.2(+0xf006e)[0x7d1d0c92606e]
2026-08-31 12:27:50 [k8s-slave03:00956] [ 9] /usr/local/nccl/lib/libnccl.so.2(+0xf387d)[0x7d1d0c92987d]
2026-08-31 12:27:50 [k8s-slave03:00956] [10] /usr/local/nccl/lib/libnccl.so.2(+0xc826b)[0x7d1d0c8fe26b]
2026-08-31 12:27:50 [k8s-slave03:00956] [11] /usr/local/nccl/lib/libnccl.so.2(+0xc9790)[0x7d1d0c8ff790]
2026-08-31 12:27:50 [k8s-slave03:00956] [12] /usr/local/nccl/lib/libnccl.so.2(+0xcb6ba)[0x7d1d0c9016ba]
2026-08-31 12:27:50 [k8s-slave03:00956] [13] /usr/local/nccl/lib/libnccl.so.2(+0xcdce1)[0x7d1d0c903ce1]
2026-08-31 12:27:50 [k8s-slave03:00956] [14] /usr/local/nccl/lib/libnccl.so.2(ncclGroupEnd+0x37)[0x7d1d0c903ee7]
2026-08-31 12:27:50 [k8s-slave03:00956] [15] /workspace/nccl-tests/build/all_gather_perf(+0xc375)[0x6397395d8375]
2026-08-31 12:27:50 [k8s-slave03:00956] [16] /workspace/nccl-tests/build/all_gather_perf(+0x103ef)[0x6397395dc3ef]
2026-08-31 12:27:50 [k8s-slave03:00956] [17] /workspace/nccl-tests/build/all_gather_perf(+0x81bd)[0x6397395d41bd]
2026-08-31 12:27:50 [k8s-slave03:00956] [18] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x2a1ca)[0x7d1d0c3d01ca]
2026-08-31 12:27:50 [k8s-slave03:00956] [19] /usr/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x8b)[0x7d1d0c3d028b]
2026-08-31 12:27:50 [k8s-slave03:00956] [20] /workspace/nccl-tests/build/all_gather_perf(+0xb2c5)[0x6397395d72c5]
```

### Steps to Reproduce the Issue

`NCCL_DEBUG_SUBSYS=tuning NCCL_DEBUG=trace NCCL_ALGO=pat nccl-tests/build/reduce_scatter_perf`

### NCCL Version

v2.31.2

### Your platform details

_No response_

### Error Message & Behavior

reason: https://github.com/NVIDIA/nccl/blob/fd168324a3dc0c9080fd4881b6c7f4bb252a95a2/src/tuning/cost_model.cc#L365

need guard for `ncclAlgoStr[algo], ncclProtoStr[proto]` in case `algo` or `proto` is `-1`.

## 评论 (4)

### xiaofanl-nvidia · 2026-09-08

++ @keithc-nvi to take a look

### keithc-nvi · 2026-09-08

Thank you for the report, taking a look at that issue.

### keithc-nvi · 2026-09-08

@fishautumn Can you provide more information about the reproducer?  Specifically looking for the following:

- Nvidia platform (hopper, blackwell, etc...)
- Scale (number of processes (GPUs), nodes, processes per node)
- Any additional command line arguments and environment vars.

### keithc-nvi · 2026-09-08

This issue has been fixed in `dev` branch, https://github.com/NVIDIA/nccl/commit/62d10969a22fae6e2feb27aa14cc05444e22391d, and should be part of the next NCCL release. 
