# [Issue #22] 底层跨group的kv cache传输用的是什么库呢？

source: https://github.com/LLMServe/DistServe/issues/22
state: closed | updated: 2025-01-09T13:54:03Z
labels: 

## 正文

这一块可以简单介绍一下嘛

## 评论 (12)

### CSEEduanyu · 2024-07-11

@PKUFlyingPig 

### CSEEduanyu · 2024-07-11

请问下大佬 为什么代码里看kv cache需要swap到cpu上呢？所以传输kv cache还是会过CPU内存？为什么不能走nvlink直连呢

### PKUFlyingPig · 2024-07-11

不会 swap 到 cpu 上，走的 nvlink

### dongluw · 2024-07-13

> 不会 swap 到 cpu 上，走的 nvlink

请问如果prefill和decoding instance不在同一个node的情况是怎么传kv cache的呢？


### GindaChen · 2024-07-14

> > 不会 swap 到 cpu 上，走的 nvlink
> 
> 请问如果prefill和decoding instance不在同一个node的情况是怎么传kv cache的呢？

因为我们的testbed没有infiniband，所以如果把PD分离在不同的node上的话kv cache transfer的延迟会很大。如果你们有跨机高带宽网络的话欢迎PR！实现方式可以参考 [Splitwise (vLLM prototype)](https://github.com/vllm-project/vllm/pull/2809)。

当前DistServe的版本会通过调整GPU Placement strategy使得集群整体满足optimal Prefill/Decode placement，从而只需要PD在相同的stage里面传KV。具体细节可以参考我们paper里面low-affinity placement的算法。

### CSEEduanyu · 2024-07-18

> > > 不会 swap 到 cpu 上，走的 nvlink
> > 
> > 
> > 请问如果prefill和decoding instance不在同一个node的情况是怎么传kv cache的呢？
> 
> 因为我们的testbed没有infiniband，所以如果把PD分离在不同的node上的话kv cache transfer的延迟会很大。如果你们有跨机高带宽网络的话欢迎PR！实现方式可以参考 [Splitwise (vLLM prototype)](https://github.com/vllm-project/vllm/pull/2809)。
> 
> 当前DistServe的版本会通过调整GPU Placement strategy使得集群整体满足optimal Prefill/Decode placement，从而只需要PD在相同的stage里面传KV。具体细节可以参考我们paper里面low-affinity placement的算法。

我看现在是通过CUDA的IPC handle来跨进程传递kv_cache指针 这里可以直接用CUDA的统一虚拟内存寻址吗？ 这个方案大佬当时有研究过嘛

### jianzi123 · 2024-07-23

@GindaChen Gi 大佬，我想尝试下

### liweiqing1997 · 2024-08-09

我希望利用 NCCL 的点对点通讯协议（P2P）将 VLLM 的 KVCACHE 从预填充（prefill）节点传输到解码（decode）节点，以实现分离式推理。由于 VLLM 的 KVCACHE 存储为张量列表，每次传输 128 个块时，我需要发送大约 16,384 个块切片。由于这些切片在显存中的分布是非连续的，循环发送的效率非常低，导致通信带宽未能得到充分利用。
因此，我考虑将这些切片拼接成一个连续的大张量进行收发。在接收端，节点会将该大张量拆分，并根据切片索引将数据写回到对应的位置。不过，这一过程非常耗时，因为涉及的切片数量高达 16,384 个。我想了解是否可以利用 CUDA 运算来并行化这一过程，从而提高性能？
此外，我的这种分离式 KVCACHE 传输方式是否存在设计上的问题？您是否有更好的建议？



### ddqspace-xyz · 2024-08-15

传输的代码在这里：https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/util/py_block_migration.cc

### chenhongyu2048 · 2024-09-06

看起来现在是基于cuda ipc和memcpy实现的传输？我记得似乎这种方式没法实现跨节点的通信？...

### interestingLSY · 2024-09-09

Yes, we are currently using CUDA IPC memory handler with cudaMemcpy now, and this blocks us from performing inter-node KV-cache transmission. If you want to send the KV cache to another node, you may need to use nvshmem

### FuHaoTHU · 2025-01-09

> 不会 swap 到 cpu 上，走的 nvlink

（1）应该是prefill instance和decoding instance间的kv cache传输直接走NVlink，对应代码中的migrate_blocks；然后decoding阶段会触发swap到cpu上的卸载操作，以提供更大的kv cache容量，对应代码中的swap_blocks，请问这样理解对吗？
（2）我观察到随着request rate的提高，吞吐率先是线性提高，然后进入瓶颈阶段，同时decoding阶段的swap操作触发频率提高。尽管cpu上的swap空间提供了更大的kv cache存储能力，但是此时有限的gpu算力和频繁的swap操作带来的开销是否是该阶段的瓶颈因素？（假设不增加gpu数量）在硬件和软件层面上如何进行进一步的优化？
