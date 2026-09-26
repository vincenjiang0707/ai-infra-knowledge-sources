# [Issue #361] Why is 1e9 used as the denominator here instead of 1024³ while calculate Bw?

source: https://github.com/NVIDIA/nccl-tests/issues/361
state: closed | updated: 2025-11-28T03:14:17Z
labels: 

## 正文

https://github.com/NVIDIA/nccl-tests/blob/4bc314aa27ae3cd57a7cca80d6da31777bca49dd/src/all_reduce.cu#L60

## 评论 (1)

### sjeaugey · 2025-11-26

It's a matter of unit. We could report GB/s or GiB/s.

NCCL started with PCI which is usually measured with powers of 10, then added NVLink which was also using power of 10, then added networking which is again powers of 10 (of bits/second rather than Bytes/second, but still). And aside from the IMB benchmark which IIRC reports powers of two (or used to), I have the feeling that the norm for benchmarking has moved to powers of ten.
