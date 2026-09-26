# [Issue #610] NIXL performance benchmarking anomaly

source: https://github.com/ai-dynamo/nixl/issues/610
state: closed | updated: 2026-04-17T18:18:00Z
labels: Network

## 正文

Hi Nixl maintainers, 

I was trying to benchmark NIXL performance over 200G IB network on GH200 nodes. However, I find there is a big performance difference between READ and WRITE ops, see the following screenshot: 

<img width="750" height="419" alt="Image" src="https://github.com/user-attachments/assets/dc893a29-0031-4e29-9e04-e23a28c2d99d" />

I wonder what causes such a big performance difference and the sudden performance drop for WRITE at 100MB messages. My code is here: https://github.com/uccl-project/uccl/blob/main/p2p/benchmarks/benchmark_nixl.py

Best,
Yang

## 评论 (10)

### yosefe · 2025-07-28

Hi @YangZhou1997 , can yous pls provide the output of "ibv_devinfo -vv" and "ucx_info -bvd" on the system?
Also, which version of NIXL was used in the benchmark?
Thanks!

### YangZhou1997 · 2025-07-28

Sure, attached. 

[ibv.txt](https://github.com/user-attachments/files/21474925/ibv.txt)
[ucx.txt](https://github.com/user-attachments/files/21474926/ucx.txt)

I am using nixl [6f09815](https://github.com/ai-dynamo/nixl/tree/6f0981500a9c723e9d5a926898595c414be66e44). 

Note that the previous results are achieved when transferring over CPU memory in GH200. 

Here are the results over GPU memory in GH200. 

NIXL READ over GPU memory: 
<img width="594" height="220" alt="Image" src="https://github.com/user-attachments/assets/5528d80a-1788-42fa-8d63-1a20fafd9e3d" />

NIXL WRITE over GPU memory: 
<img width="594" height="220" alt="Image" src="https://github.com/user-attachments/assets/4ac7f608-f191-4f74-8043-93e37a0c6058" />


### iyastreb · 2025-07-30

1) I see that you are using UCX 1.18, which does not have a few important performance improvements that were added recently.
Could you please try with UCX master branch?

2) On my side I test performance using nixlbench, and here are results. I ran with batch size = 1
```
For host memory:
nixlbench --etcd-endpoints=http://ptyche0358:2379 --initiator_seg_type=DRAM --target_seg_type=DRAM --start_block_size=1024 --max_block_size=1073741824 --num_iter=10000 --op_type=READ // WRITE
```
<img width="1979" height="1180" alt="Image" src="https://github.com/user-attachments/assets/13b3d960-873c-41c4-b580-a382ce0ff6b9" />

So I see a performance peak around 256KB (because with UCX master we are using 4 lanes), and I also see that READ is a bit slower than WRITE, but not more than 25-30%. Still this needs to be investigated. IMO WRITE BW could be also more, close to 100 GBps, because we are using 4 IB lanes.

4) For GPU memory:
```
nixlbench --etcd-endpoints=http://ptyche0358:2379 --initiator_seg_type=VRAM --target_seg_type=VRAM --start_block_size=1024 --max_block_size=1073741824 --num_iter=10000 --op_type=READ // WRITE
```
<img width="1980" height="1180" alt="Image" src="https://github.com/user-attachments/assets/374d8828-62f2-46ad-b771-0a25ae155b46" />
So for GPU memory it's pretty much the same, reaching 120GBps (GB, not Gb, because on NVLink).

5) Do you have MNNVL in your setup? Normally for GPU memory the communication should go over multi node NVLink, therefore BW should be significantly better than with IB devices

6) If you still see a huge gap between READ and WRITE, could you please run your benchmark with `UCX_PROTO_INFO=y` option and attach here the output for both operations?

### YangZhou1997 · 2025-07-30

HI @iyastreb , thank you for sharing the results. I will try the more recent UCX. My testbed is two GH200 nodes each with one GPU, so the two GPUs go through 200Gbps IB. Meanwhile, I wonder in your side how the nixlbench performs across nodes via 400Gbps IB/RoCE. I am lacking such a testbed, thus I cannot measure it. 

### iyastreb · 2025-07-31

As for READ performance, I'm sure it's because of the recently enabled error handling in NIXL, that does not work well with old UCX 1.18. So please upgrade to master, or at least UCX 1.19.

Regarding nixlbench performance on high-BW clusters: currently we are not always reaching the maximum available speed (even what UCX provides), so we are working on improvements

### YangZhou1997 · 2025-08-02

With latest ucx, the read performance gets back to normal. Thank you @iyastreb 

<img width="478" height="175" alt="Image" src="https://github.com/user-attachments/assets/9c5552d9-8006-4853-ab16-394cedcd5e09" />

### YangZhou1997 · 2025-08-05

@iyastreb Just wondering for the read/write figure over IB, you mention 4 IB lanes---do you mean 4 IB NICs each with 25GBps (so they add up to 100GBps), but does the PCIe5 handle 100GBps? Or do you mean 4 RDMA QPs and you are using a 100 GBps NIC? 

My Nixl run on 25GBps NIC (with nixl python interface) can only reach 14GB/s on 256KB (see above), so that's why I am asking about the performance. 

### iyastreb · 2025-08-06

I was testing on setup with 4 IB NICs, each having 50GBps bandwidth (so the overall BW is 200GBps).
With ucx_perftest I was able to reach ~180GBps on the same node (DRAM-DRAM), but nixlbench is much behind it (~70GBps).
I need to repeat my tests on inter-node. Yes, PCIe5 can be a limiting factor here, but I'm not sure what is the cap

### alokprasad · 2026-04-17

@YangZhou1997 what are the config/steps u used for running NIXLbench over RDMA

### YangZhou1997 · 2026-04-17

Hi @alokprasad, It has been a long time, but you can probably check this file https://github.com/uccl-project/uccl/blob/main/.github/workflows/nixlbench_test.sh
