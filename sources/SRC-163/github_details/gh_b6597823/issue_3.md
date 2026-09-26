# [Issue #3] An Trick of Enhancing LLM Serving Throughput with KV Cache Pipeline Strategy

source: https://github.com/LLMServe/DistServe/issues/3
state: closed | updated: 2024-07-25T15:47:07Z
labels: enhancement

## 正文

Hi, your DistServe paper is pretty good and insightful, thanks a lot for the ideas and implementations! These days, I got an idea  exploring further into the domain of prefill-decode disaggregation, but not sure if it can work. If appropriate, I want to share it here. I would deeply appreciate your perspective on this concept, given your expertise :)

My observations are:
- LLM serving throughput is mainly bottlenecked at GPU memory capacity (KV cache).
- In prefill-decode disaggregation setting, prefill machine memory is oftern underutilized as KV cache is only stored at decode machine.
- KV cache occupies memory until the decoding process ends and the request results are returned. However, the KV caches across different layers are accessed sequentially, with data in a layer remaining idle until accessed during the next iteration (token).

Based on these points, I propose a **KV cache pipeline** strategy between prefill machines and decode machines, i.e.  KV caches are partitioned along layer axis, after computing attention for a given layer, its KV cache is immediately swapped out to the local prefill machine, and pre swap in next iteration.

Given the available 900 GBps or 1.8 TBps NVLink bandwidth, it looks work. How do you think? If you also find this approach potentially feasible, perhaps I could contribute some code to the DistServe repository during my spare time to see its effect in practice.

## 评论 (5)

### PKUFlyingPig · 2024-05-20

Nice observation, the GPU memory utilization imbalance between prefill and decode machine is actually a problem. With your optimization, we can support more requests in the decoding machine, increase the decoding batch size and thus achieve better GPU utilization. My concern is that the decoding time is quite fast for each iteration (~50ms), the swapping overhead may overshadow the benefits if not implemented judiciously. 

### chenzhuofu · 2024-05-20

Yes, it's hard to implement in such fine-grained setting, however, I think it's not really impossible given the such large GPU-GPU memory bandwidth (and often our prefill and decode machine reside on the same node). In the other side, maybe we can also try figuring out if there is better idea to eliminate imblance.

### interestingLSY · 2024-06-11

Brilliant idea. Your observation really makes sense, since currently in our implementation, we do not utilize GPU memory on prefill GPUs for KV cache storage. This may result in gpu memory being underutilized, and furthermore lead to performance degration.

Im the meantime, I have three concerns:

The first one is that, compared with the bandwidth of GPU memory (VRAM), the bandwidth of NVLink seems to be insufficient if you swap all KV cache to prefill instances. Here is a list of recent GPUs and their VRAM/NVLink bandwidth:

| GPU | VRAM BW (GB/s) | NVLink BW (GB/s) | VRAM : NVLink BW Ratio |
| :----: | :----: | :----: | :----: |
| A100 40G SXM | 1560 | 600 |  2.6 | 
| A100 80G SXM | 2040 | 600 | 3.4 | 
| H100 80G SXM | 3360 | 900 | 3.73 | 
| B100 | ~8000 | 1800 | 4.44 |

We can see that the ratio of VRAM bandwidth and NVLink bandwidth ranges from 2.6 to 4.4.

Assume that the size of the KV cache is $M$, and we want to store $\alpha \\%$ KV cache on the prefill instance. In order to avoid performance degration, the following equation must hold:

$$\alpha M / BW_{NVLink} + T_{overhead} \le 100 M / BW_{VRAM} + T_{other}$$

Where $T_{other}$ is the time consumption of other operations (e.g. GEMM, layernorm), and $T_{overhead}$ is the overhead for KV cache swapping.

If we assume both $T = 0$, we will have $\alpha \le \frac{BW_{NVLink}}{BW_{VRAM}} \cdot 100$. On an A100 80G SXM GPU where the BW ratio is $3.4$, we can only store $30\\%$ KV cache on the prefill instance.

The second one is that, will KV cache swapping interfere with Tensor Parallelism (TP)? To my knowledge, Tensor Parallelism heavily relys on the latency and throughput of the interconnect between GPUs. Will KV cache swapping affect the efficiency of TP?

The final concern is that, what does "600 GBps" means in NVLink? Is it the bandwidth of a single P2P connection, or the total bandwidth available for a single GPU, or the aggregated bandwidth of all GPUs?

Nevertheless, the idea of using GPU memory on the prefill instance is novel and creative. I suggest you to set up some "idea verification" experiments to make sure it works. Please feel free to ask us if you encountered any problems with our code.

### interestingLSY · 2024-06-11

This is the result of running `p2pBandwidthLatencyTest` on a node with 8 NVIDIA A100 80G SXMs. Seems that "600GBps" is the bi-directional bandwidth

```
(base) -[e87ce961d12e]- -[~/cuda-samples/bin/x86_64/linux/release]-
-[09:00 AM]-./p2pBandwidthLatencyTest
[P2P (Peer-to-Peer) GPU Bandwidth Latency Test]
Device: 0, NVIDIA A100-SXM4-80GB, pciBusID: 7, pciDeviceID: 0, pciDomainID:0
Device: 1, NVIDIA A100-SXM4-80GB, pciBusID: a, pciDeviceID: 0, pciDomainID:0
Device: 2, NVIDIA A100-SXM4-80GB, pciBusID: 44, pciDeviceID: 0, pciDomainID:0
Device: 3, NVIDIA A100-SXM4-80GB, pciBusID: 4a, pciDeviceID: 0, pciDomainID:0
Device: 4, NVIDIA A100-SXM4-80GB, pciBusID: 84, pciDeviceID: 0, pciDomainID:0
Device: 5, NVIDIA A100-SXM4-80GB, pciBusID: 8a, pciDeviceID: 0, pciDomainID:0
Device: 6, NVIDIA A100-SXM4-80GB, pciBusID: c1, pciDeviceID: 0, pciDomainID:0
Device: 7, NVIDIA A100-SXM4-80GB, pciBusID: c4, pciDeviceID: 0, pciDomainID:0
Device=0 CAN Access Peer Device=1
Device=0 CAN Access Peer Device=2
Device=0 CAN Access Peer Device=3
Device=0 CAN Access Peer Device=4
Device=0 CAN Access Peer Device=5
Device=0 CAN Access Peer Device=6
Device=0 CAN Access Peer Device=7
Device=1 CAN Access Peer Device=0
Device=1 CAN Access Peer Device=2
Device=1 CAN Access Peer Device=3
Device=1 CAN Access Peer Device=4
Device=1 CAN Access Peer Device=5
Device=1 CAN Access Peer Device=6
Device=1 CAN Access Peer Device=7
Device=2 CAN Access Peer Device=0
Device=2 CAN Access Peer Device=1
Device=2 CAN Access Peer Device=3
Device=2 CAN Access Peer Device=4
Device=2 CAN Access Peer Device=5
Device=2 CAN Access Peer Device=6
Device=2 CAN Access Peer Device=7
Device=3 CAN Access Peer Device=0
Device=3 CAN Access Peer Device=1
Device=3 CAN Access Peer Device=2
Device=3 CAN Access Peer Device=4
Device=3 CAN Access Peer Device=5
Device=3 CAN Access Peer Device=6
Device=3 CAN Access Peer Device=7
Device=4 CAN Access Peer Device=0
Device=4 CAN Access Peer Device=1
Device=4 CAN Access Peer Device=2
Device=4 CAN Access Peer Device=3
Device=4 CAN Access Peer Device=5
Device=4 CAN Access Peer Device=6
Device=4 CAN Access Peer Device=7
Device=5 CAN Access Peer Device=0
Device=5 CAN Access Peer Device=1
Device=5 CAN Access Peer Device=2
Device=5 CAN Access Peer Device=3
Device=5 CAN Access Peer Device=4
Device=5 CAN Access Peer Device=6
Device=5 CAN Access Peer Device=7
Device=6 CAN Access Peer Device=0
Device=6 CAN Access Peer Device=1
Device=6 CAN Access Peer Device=2
Device=6 CAN Access Peer Device=3
Device=6 CAN Access Peer Device=4
Device=6 CAN Access Peer Device=5
Device=6 CAN Access Peer Device=7
Device=7 CAN Access Peer Device=0
Device=7 CAN Access Peer Device=1
Device=7 CAN Access Peer Device=2
Device=7 CAN Access Peer Device=3
Device=7 CAN Access Peer Device=4
Device=7 CAN Access Peer Device=5
Device=7 CAN Access Peer Device=6

***NOTE: In case a device doesn't have P2P access to other one, it falls back to normal memcopy procedure.
So you can see lesser Bandwidth (GB/s) and unstable Latency (us) in those cases.

P2P Connectivity Matrix
     D\D     0     1     2     3     4     5     6     7
     0       1     1     1     1     1     1     1     1
     1       1     1     1     1     1     1     1     1
     2       1     1     1     1     1     1     1     1
     3       1     1     1     1     1     1     1     1
     4       1     1     1     1     1     1     1     1
     5       1     1     1     1     1     1     1     1
     6       1     1     1     1     1     1     1     1
     7       1     1     1     1     1     1     1     1
Unidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0      1      2      3      4      5      6      7
     0 1521.42  16.92  20.20  20.09  17.74  20.42  17.93  18.55
     1  17.06 1533.37  20.18  20.21  17.85  20.39  18.50  20.31
     2  20.21  20.28 1533.37  17.08  17.48  19.74  17.84  18.55
     3  20.08  20.28  17.17 1540.93  17.57  20.42  17.90  18.60
     4  17.74  18.81  17.44  18.68 1536.38  10.65  17.33  17.79
     5  17.17  18.72  17.74  18.81  10.73 1570.35  17.48  17.16
     6  18.23  17.00  18.69  16.86  17.45  16.55 1575.10  10.71
     7  18.28  17.43  18.88  17.70  17.50  17.17  10.84 1571.93
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0      1      2      3      4      5      6      7
     0 1528.86 268.94 269.36 272.10 275.19 274.06 274.26 273.27
     1 265.05 1545.50 270.47 274.10 274.48 274.60 275.12 275.00
     2 269.09 269.87 1550.10 274.45 274.43 273.79 273.39 274.49
     3 269.75 271.95 270.03 1584.69 274.62 274.04 275.45 275.49
     4 270.03 271.74 271.08 275.53 1597.65 274.24 274.52 274.93
     5 270.79 271.23 271.21 274.35 274.50 1584.69 275.15 274.52
     6 271.62 271.07 271.04 271.24 274.98 274.89 1583.08 274.84
     7 271.82 271.57 270.66 270.50 275.11 274.22 275.23 1587.91
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0      1      2      3      4      5      6      7
     0 1552.41  11.10  27.81  28.22  19.19  19.90  19.74  19.07
     1  10.87 1598.47  28.32  28.30  19.45  20.09  20.01  19.51
     2  28.11  28.27 1579.88  10.67  19.73  19.97  20.05  19.50
     3  28.45  28.22  10.28 1600.10  19.32  19.98  19.91  19.82
     4  20.31  21.14  21.01  20.79 1602.56   9.21  18.60  18.54
     5  20.38  20.49  20.83  21.29  11.30 1599.28  19.18  19.12
     6  20.05  20.30  20.18  20.61  19.08  19.25 1600.10   8.47
     7  19.89  20.40  20.30  20.23  19.05  19.15  11.25 1598.47
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0      1      2      3      4      5      6      7
     0 1557.05 416.29 418.96 419.08 420.21 419.28 419.79 419.30
     1 418.74 1553.95 418.73 418.63 419.75 420.01 420.19 419.86
     2 418.96 419.88 1556.27 418.52 420.09 419.53 419.30 418.96
     3 417.51 419.56 418.96 1555.50 419.53 419.30 418.74 419.15
     4 420.97 421.52 421.35 421.30 1605.03 517.80 519.18 516.83
     5 420.25 421.83 420.55 421.08 519.51 1595.20 519.25 512.35
     6 421.79 421.32 421.05 420.62 421.32 520.22 1598.47 518.61
     7 421.34 421.40 420.58 421.01 421.16 421.17 518.15 1600.10
P2P=Disabled Latency Matrix (us)
   GPU     0      1      2      3      4      5      6      7
     0   3.33  23.59  23.60  23.59  24.62  24.50  24.55  24.44
     1  23.58   3.34  23.59  23.59  24.49  24.51  24.32  24.47
     2  23.61  23.63   3.31  23.65  24.50  24.49  24.49  24.49
     3  23.58  23.58  23.57   3.17  24.50  24.49  24.48  24.48
     4  24.67  24.63  24.77  24.76   3.08  24.69  24.76  24.72
     5  24.70  24.52  24.64  24.67  24.72   3.15  24.60  24.61
     6  24.42  24.52  24.59  24.50  24.58  24.60   2.51  24.51
     7  24.34  24.59  24.52  24.62  24.67  24.59  24.48   2.48

   CPU     0      1      2      3      4      5      6      7
     0   2.33   7.27   6.95   6.99   8.54   8.86   8.55   8.41
     1   7.13   2.28   6.93   6.98   8.57   8.52   8.50   8.45
     2   7.04   7.01   2.24   6.93   8.45   8.42   8.43   8.37
     3   6.99   6.99   6.88   2.23   8.52   8.50   8.51   8.53
     4   8.01   7.99   7.90   7.91   2.80   9.56   9.59   9.52
     5   8.00   7.95   7.83   7.85   9.51   2.79   9.62   9.50
     6   8.00   7.96   7.91   7.92   9.53   9.52   2.80   9.59
     7   8.02   7.86   7.83   7.86   9.48   9.50   9.59   2.81
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0      1      2      3      4      5      6      7
     0   3.32   3.38   3.30   3.42   3.38   3.37   3.30   3.30
     1   3.30   3.39   3.30   3.37   3.38   3.30   3.30   3.30
     2   3.25   3.20   3.29   3.20   3.26   3.32   3.21   3.25
     3   3.27   3.21   3.28   3.16   3.22   3.21   3.22   3.26
     4   3.46   3.44   3.49   3.39   3.07   3.39   3.47   3.39
     5   3.39   3.42   3.46   3.44   3.39   3.15   3.49   3.44
     6   2.96   2.97   2.96   2.95   3.01   3.01   2.52   3.02
     7   2.94   2.94   3.00   2.95   3.06   2.96   2.95   2.48

   CPU     0      1      2      3      4      5      6      7
     0   2.78   2.14   2.16   2.17   2.16   2.14   2.13   2.18
     1   2.18   2.58   2.18   2.18   2.17   2.19   2.18   2.18
     2   1.93   1.89   2.33   1.89   1.91   1.91   1.90   1.88
     3   1.92   1.88   1.89   2.30   1.87   1.91   1.87   1.89
     4   2.59   2.47   2.48   2.49   2.87   2.50   2.46   2.50
     5   2.54   2.51   2.51   2.50   2.52   2.87   2.47   2.50
     6   2.51   2.48   2.47   2.47   2.48   2.47   3.07   2.44
     7   2.72   2.51   2.49   2.50   2.51   2.50   2.80   3.03

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
(base) -[e87ce961d12e]- -[~/cuda-samples/bin/x86_64/linux/release]-
-[09:00 AM]-nvidia-smi topo -m
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV12    NV12    NV12    NV12    NV12    NV12    NV12    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU1    NV12     X      NV12    NV12    NV12    NV12    NV12    NV12    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU2    NV12    NV12     X      NV12    NV12    NV12    NV12    NV12    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU3    NV12    NV12    NV12     X      NV12    NV12    NV12    NV12    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU4    NV12    NV12    NV12    NV12     X      NV12    NV12    NV12    SYS     SYS     SYS     SYS     64-127,192-254  1               N/A
GPU5    NV12    NV12    NV12    NV12    NV12     X      NV12    NV12    SYS     SYS     SYS     SYS     64-127,192-254  1               N/A
GPU6    NV12    NV12    NV12    NV12    NV12    NV12     X      NV12    SYS     SYS     SYS     SYS     64-127,192-254  1               N/A
GPU7    NV12    NV12    NV12    NV12    NV12    NV12    NV12     X      SYS     SYS     SYS     SYS     64-127,192-254  1               N/A
NIC0    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS      X      PIX     SYS     SYS
NIC1    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X      SYS     SYS
NIC2    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS      X      PIX
NIC3    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
```

### chenzhuofu · 2024-07-25

Thank you for your careful check! You're right, the `900 GBps` I mentioned is bidirectional. I found its measurement [here](https://docs.nvidia.com/gh200-superchip-benchmark-guide.pdf) (check NVLink-C2C Bandwidth). It looks like the NVLink bandwidth is at least insufficient for now...

So I would close this issue for the moment.  Nevertheless, dicussion with you help me a lot! Hope we can come up some more feasible solution for Prefill machine in the future~

P.S., I really appreciate @interestingLSY calculation in the 1st concern, that helps me organize my thoughts. :D

