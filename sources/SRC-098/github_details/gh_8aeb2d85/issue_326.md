# [Issue #326] all gather / all reduce showing unidirectional bandwidth peak performance

source: https://github.com/NVIDIA/nccl-tests/issues/326
state: open | updated: 2025-06-27T20:52:27Z
labels: 

## 正文

Hi team, 

I ran all_gather and all_reduce benchmark on the system (8 H100 GPU, NVlink) and the results show that the bandwidth is saturated at ~360 GB/s for busbw although I am using fairly large data size (16GB). 

Given that NVLink's peak bi-directional bandwidth is 900 GB/s, the measured 360 GB/s suggests I am only achieving uni-directional bandwidth.

Could you explain why I might be observing only uni-directional bandwidth during these operations? Furthermore, are there specific configurations/environment vars/optimizations I can use to leverage the full bi-directional bandwidth for all_gather and all_reduce operations in this setup?

Thank you.

./build/all_gather_perf -b 128M -e 16384M -f 2 -g 8
![Image](https://github.com/user-attachments/assets/7b58329d-7968-4eea-aa34-08dfa09ac3db)

./build/all_reduce_perf -b 128M -e 16384M -f 2 -g 8
![Image](https://github.com/user-attachments/assets/aa06267a-7c83-4987-a915-311badb070f8)

## 评论 (2)

### sjeaugey · 2025-06-24

360 GB/s is exactly what we'd expect on H100. See my GTC talk every year on NVIDIA on demand, there is always a slide with the expected NCCL performance on DGX platforms.

### BitCalSaul · 2025-06-27

Hi @asdfvg123 @sjeaugey , I have a quick question about NCCL all_gather_perf.

In my setup, I have 6 GPUs, and each rank has 80MB of data that needs to be gathered by all other ranks, so that after the operation, each rank ends up with 480MB (80MB × 6).

I would like to measure the ideal performance using NCCL tests. Is the following command correctly representing this scenario?

`NCCL_PROTO=Simple ./build/all_gather_perf -b 80M -e 80M -g 6 -d float`

Does this configuration mean that each rank sends 80MB and receives data from all others (totaling 480MB per rank), and is it the correct way to benchmark such an AllGather pattern?

Thanks a lot in advance!
