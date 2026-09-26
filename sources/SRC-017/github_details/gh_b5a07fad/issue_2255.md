# [Issue #2255] [Question]: Does NCCL GIN (GDAKI backend) support ConnectX-6 NICs?

source: https://github.com/NVIDIA/nccl/issues/2255
state: closed | updated: 2026-08-10T00:09:59Z
labels: question

## 正文

### Question

We are testing NCCL GIN on machines equipped with ConnectX-6 (CX6) NICs. The GIN initialization completes without errors (doca_gpu_create, QP creation, and QP state transitions all succeed), but at runtime, GPU-initiated RDMA operations (both put_signal and signal) silently fail — the WQE appears to be posted, yet the remote signal is never incremented, causing waitSignal to hang indefinitely. No errors are reported even with DOCA_GPUNETIO_LOG=6.

The same tests pass on ConnectX-7 (CX7) NICs. We have also verified that CX6 hardware does support GPU-initiated RDMA (including atomics) through a separate DevX-based implementation.Could you confirm whether CX6 is a supported NIC for GIN / GDAKI, or if CX7+ is a hard requirement? 

## 评论 (3)

### pakmarkthub · 2026-06-30

Hi @Ben286 ,

Yes, it supports CX-6. What is the difference between your CX-6 and CX-7? Are these on two different systems/clusters? Or did you test on the same nodes and replace the NICs with CX-7 and observed that it worked?

### Ben286 · 2026-07-03

https://github.com/NVIDIA/nccl/issues/1957. We eventually determined that this is the same issue, and I commented on that issue thread.

### xiaofanl-nvidia · 2026-08-10

Thanks. Closing dead issue. 
