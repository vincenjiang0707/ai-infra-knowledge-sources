# [Issue #390] Will nccl-test support testing for NCCL EP?

source: https://github.com/NVIDIA/nccl-tests/issues/390
state: open | updated: 2026-07-31T06:52:43Z
labels: 

## 正文

Hi. 
Will nccl-test support testing for NCCL EP? If not, how can I test the performance of NCCL EP?

## 评论 (2)

### artpol84 · 2026-07-30

NCCL EP performance is measured with `ep_bench`.
See https://github.com/NVIDIA/nccl-extensions/

https://github.com/NVIDIA/nccl-extensions/blob/main/nccl_ep/ep_bench.cu

### wanggeng09825 · 2026-07-31

Thank you for your time.
I missed ep_bench, and I asked a silly question.
