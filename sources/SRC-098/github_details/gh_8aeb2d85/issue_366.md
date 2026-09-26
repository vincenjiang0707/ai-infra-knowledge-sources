# [Issue #366] ALL_Reduce_Perf with NVLS in one node(8GPUs)

source: https://github.com/NVIDIA/nccl-tests/issues/366
state: open | updated: 2026-01-09T03:28:57Z
labels: 

## 正文

I’d like to ask a question. For NVIDIA servers equipped with SHARP（for example, B300）, when running single-node Allreduce operations with the NVLS algorithm, should the factor between algorithm bandwidth and bus bandwidth be 1 instead of 2(n-1)/n? However, in this case, it seems that the algorithm bandwidth still falls short of the NVLink bandwidth.

## 评论 (1)

### AddyLaddy · 2026-01-09

`nccl-tests` is just a benchmarking tool and it has no information about what algorithms and accelerations the NCCL library is using. So for consistency when comparing NVLink SHARP and non-NVLS performance, we continue to calculate the the BusBW using the same formula.
But you can look at NVLS BusBw as effectively the NVLink BW you would need to achieve the AllReduce performance using say the RING or non accelerated algorithms.

Also remember the advertised NVLink rates such as 900GB/s are the raw line rate before any protocol or error correction overheads. NCCL will then add it's own protocol and synchronization overheads.
To measure the raw "memcpy" speed of NVLink I'd recommend using a tool like `nvloom` or `nvbandwidth`
