# [Issue #123] Understanding the latency of NCCL

source: https://github.com/NVIDIA/nccl-tests/issues/123
state: open | updated: 2025-05-14T09:05:45Z
labels: 

## 正文

Dear developers,

I am profiling the latency of NCCL Ring algorithm using below command on variable number of GPUs.
```bash
NCCL_ALGO=Ring NCCL_MAX_NCHANNELS=1 NCCL_DEBUG=INFO ./all_reduce_perf -b 8 -e 128 -f 2 -n 100 -g GPU_NUM
```

Before we start, I think theoretically the latency of Ring-AllReduce is `2*(GPU_NUM - 1)*network_latency`, according to the ring algorithm. I test on a DGX-A100 machine, where the P2P-write latency should be 3us around (results from p2pBandwidthLatency test).  Then I get the below results
| GPU_NUM | comm times| expected time (us)|actual time (us) | diff|
| --- | ---|---|---| ---|
| 2 |2 | ~6| 10 | 4 |
| 3 | 4| ~12|13.76| 1.76|
|4 | 6|~18|16.88| -1.12 |
|5 | 8|~24|20.8| -3.2 |
|6| 10|~30|25.2| -4.8 |
|7| 12|~36|29.5| -6.5 |
|8| 14|~42|33.7| -8.3 |

I have several questions.
1. For GPU_NUM=2, why the actual time is so much larger than expected time? Is there a handshake procedure that produce multiple times of latency like TCP does?
2. For GPU_NUM=8, why the actual time is smaller than expected time? Would it be the reason that threads in a warp can overlap each other's latency (i.e, while thread 1 doing step 1, thread 0 may be doing step 0)?



## 评论 (5)

### sjeaugey · 2022-12-14

>  I think theoretically the latency of Ring-AllReduce is 2*(GPU_NUM - 1)*network_latency

This formula is correct, but `network_latency` should be called `max_latency`. In all your tests there is no network (it's single node so using intra-node communication), but if you have a mix of intra-node and inter-node, what matters is the max latency and that's usually the network latency.

> the P2P-write latency should be 3us around (results from p2pBandwidthLatency test)

The latency from `p2pBandwidthLatency` does not necessarily reflect the NCCL latency. I'm not very familiar with the p2pBandwidthLatency implementation, but they are probably very different from what NCCL needs to do. NCCL uses 3 different protocols: LL, LL128 and Simple, which have different latencies (~1us, ~2us and ~6us), different bandwidth as well (50%, 95% and 100%), and other differences impacting their performance.
If you look at the total NCCL operation time, you also need to factor in the CUDA launch time and some overhead (~5us).

Finally, when you run with `-g NUM_GPUS`, all GPUs are handled by a single thread and that causes extra latency as the CPU is the bottleneck. Launching with `-t NUM_GPUS` or better, compile with MPI support and launch one process per GPU and `--bind-to numa` will give much cleaner results as each GPU will have a dedicated CPU.

Feel free to run again with `-t NUM_GPUS`, and try `NCCL_PROTO=LL`, `NCCL_PROTO=LL128` and `NCCL_PROTO=SIMPLE`. You should hopefully be able to deduce the latency of each protocol. That's how we compute them ourselves, to tune our internal models predicting the performance of each protocol/algorithm.


### ConnollyLeon · 2022-12-15

@sjeaugey Thanks for your reply and your correcting.

>The latency from p2pBandwidthLatency does not necessarily reflect the NCCL latency. I'm not very familiar with the p2pBandwidthLatency implementation, but they are probably very different from what NCCL needs to do.

The source code `p2pBandwidthLatency` is available here: [link](https://github.com/NVIDIA/cuda-samples/blob/master/Samples/5_Domain_Specific/p2pBandwidthLatencyTest/p2pBandwidthLatencyTest.cu).  Similar to NCCL, they use cuda runtime api like `cudaDeviceEnablePeerAccess` to enable peer access, but use `dest[i] = src[i];` to do data copy while NCCL uses asm instruction directly. I think using asm makes NCCL has lower latency, isn't it?

> NCCL uses 3 different protocols: LL, LL128 and Simple, which have different latencies (~1us, ~2us and ~6us), different bandwidth as well (50%, 95% and 100%), and other differences impacting their performance.

And I have tested the three protocols, and find similar conclusion on latency. 

> Feel free to run again with -t NUM_GPUS, and try NCCL_PROTO=LL, NCCL_PROTO=LL128 and NCCL_PROTO=SIMPLE. You should hopefully be able to deduce the latency of each protocol. That's how we compute them ourselves, to tune our internal models predicting the performance of each protocol/algorithm.

I test NCCL again with `-t` and assign specific protocols. Then I got these results: 

|#GPU | LL Total Lat | LL Avg Lat | LL128 Total Lat | LL128 Avg Lat | Simple Total Lat | Simple Avg Lat|
|-- | -- | -- | -- | -- | -- | --|
|2 | ~12 | 6 | ~20 | 10 | ~25 | 12.5 |
|3 | ~13.5 | 3.375 | ~22 | 5.5 | ~35 | 8.75|
|4 | ~15 | 2.5 | ~24 | 4 | ~43 | 7.17|
|5 | ~17 | 2.125 | ~26 | 3.25 | ~53 | 6.625|
|6 | ~17.6 | 1.76 | ~28 | 2.8 | ~60 | 6|
|7 | ~19 | 1.58 | ~30 | 2.5 | ~72 | 6|
|8 | ~21 | 1.5 | ~32 | 2.29 | ~84 | 6|

For 8 cards case, I get the similar results (~1us, ~2us, and ~6us) as you have mentioned. But for 2 cards case, the average latency seems to be worse. What would be the problems?

### shenyt-sanshui · 2025-05-14

>But for 2 cards case, the average latency seems to be worse

@ConnollyLeon Regarding this issue, do you know the reason now? Why does the Avg latency  increase when the number of cards decreases?

### shenyt-sanshui · 2025-05-14

>But for 2 cards case, the average latency seems to be worse

I guess there might be certain fixed overheads that remain constant regardless of GPU count reduction. This could potentially explain why the total execution time doesn’t decrease proportionally when fewer GPUs are used.

 @sjeaugey  could you kindly verify if this interpretation holds true?  I've also observed on 8xH120 systems that the latency remains around 12μs even when using  just two GPUs. 



### sjeaugey · 2025-05-14

As I mentioned in my previous comment, there is a fixed launch latency + initialization time you need to substract if you want to then divide by the number of GPUs.

Your base time (12us) still seems high to me though. I just ran a quick test on a DGX H100 and I get a base time of ~7.5us on 2 GPUs.
