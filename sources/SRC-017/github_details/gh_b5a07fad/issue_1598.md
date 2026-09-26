# [Issue #1598] why NCCL_MAX_NCHANNELS cannot limit ncclDevKernel_SendRecv grid size

source: https://github.com/NVIDIA/nccl/issues/1598
state: open | updated: 2026-09-22T03:27:28Z
labels: 

## 正文

Hi, recently I try to use NCCL_MAX_NCHANNELS = 10 to limit nccl:all_to_all operation grid_size(SM counts) from torch/distributed/distributed_c10d.py(3881): all_to_all_single, but result shows that grid_size is 16, which is still larger than 10. So is it a problem with the usage or a misunderstanding on my part ?
`export NCCL_MAX_NCHANNELS=10 export NCCL_MIN_NCHANNELS=10`
![Image](https://github.com/user-attachments/assets/309ea549-0e2b-43f8-aea0-bac761340385)

@sjeaugey Looking forward to your answer, thanks very much!

## 评论 (12)

### sjeaugey · 2025-02-10

You should use `NCCL_MAX_CTAS=10`. Or better, change your code to set config.maxCTAs=10 for the communicators which need that (instead of applying that to all communicators).

### Graham1025 · 2025-02-10

> You should use `NCCL_MAX_CTAS=10`. Or better, change your code to set config.maxCTAs=10 for the communicators which need that (instead of applying that to all communicators).

Thanks a lot! Yes, I also try NCCL_MAX_CTAS=20 env variable, and I run a nccl api all2all test，but the result is not what i expects. However, when i change all2all to allReduce, that works. So what are the differences？@sjeaugey Looking forward to your answer, thanks very much!

![Image](https://github.com/user-attachments/assets/9297378d-066b-474f-9dd9-4cddd10762e2)

![Image](https://github.com/user-attachments/assets/0acb656c-63da-4139-9773-5472cf8f8e84)

![Image](https://github.com/user-attachments/assets/25742801-26bf-4681-ac8b-de9d5949ee4a)


### sjeaugey · 2025-02-10

The number of send/recv channels is controlled by `NCCL_MAX_P2P_NCHANNELS`. `NCCL_MAX_NCHANNELS` controls the number of channels for rings and trees algorithms; `NCCL_NVLS_NCHANNELS` controls the number of channels of the NVLS/NVLSTree algorithms.

`NCCL_MAX_CTAS` should cap the number of channels for all use cases though. If not, then it's probably a bug.

### Graham1025 · 2025-02-10

> The number of send/recv channels is controlled by `NCCL_MAX_P2P_NCHANNELS`. `NCCL_MAX_NCHANNELS` controls the number of channels for rings and trees algorithms; `NCCL_NVLS_NCHANNELS` controls the number of channels of the NVLS/NVLSTree algorithms.
> 
> `NCCL_MAX_CTAS` should cap the number of channels for all use cases though. If not, then it's probably a bug.

@sjeaugey Thanks for your reply! I also try NCCL_MAX_P2P_NCHANNELS, the result is the same as NCCL_MAX_CTAS.

export NCCL_MAX_NCHANNELS=20
export NCCL_MIN_NCHANNELS=20
export NCCL_MAX_P2P_NCHANNELS=20
export NCCL_MAX_CTAS=20
export NCCL_MIN_CTAS=20
111245132…        1320694    9145  32    1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (3)    4              52  ncclDevKernel_SendRecv(nccl…
 111291944…        1320695    9148  32    1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (2)    3              40  ncclDevKernel_SendRecv(nccl…
 111357154…        1328515    9151  32    1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (1)    2              28  ncclDevKernel_SendRecv(nccl…
 111424034…        1325155    9154  32    1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (0)    1              16  ncclDevKernel_SendRecv(nccl…


Weird, when i change limit num to 8, it works again
export NCCL_MAX_P2P_NCHANNELS=8
export NCCL_MAX_CTAS=8
export NCCL_MIN_CTAS=8

118547991…        4539163    4333  8     1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (3)    4              52  ncclDevKernel_SendRecv(nccl…
 118594824…        4535010    4336  8     1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (2)    3              40  ncclDevKernel_SendRecv(nccl…
 118706158…        3941193    4339  8     1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (1)    2              28  ncclDevKernel_SendRecv(nccl…
 118815569…        3940011    4342  8     1     1     640   1     1     96       0.007         0.082                                                            NVIDIA A100-SXM4-80GB (0)    1              16  ncclDevKernel_SendRecv(nccl…

### sjeaugey · 2025-02-10

I'm not sure I understand. In your original comment, you mentioned you wanted to use 10 channels only, and NCCL was using 16.

Now if you set the max value to 20, then we'd still use 16, given 20 is higher than 16.

### Graham1025 · 2025-02-11

> I'm not sure I understand. In your original comment, you mentioned you wanted to use 10 channels only, and NCCL was using 16.
> 
> Now if you set the max value to 20, then we'd still use 16, given 20 is higher than 16.

@sjeaugey Sorry, in my last comment, I change the channels num to 20 by export NCCL_MAX_CTAS=20
, and I expect grid_size can limit to 20, but the trace result shows that it is 32;  However，when I change the channels num to 8 by export NCCL_MAX_CTAS=8, the trace result shows it is 8, in this low number, it works again. This phenomenon puzzles me. 

### Graham1025 · 2025-02-11

```bash
> > I'm not sure I understand. In your original comment, you mentioned you wanted to use 10 channels only, and NCCL was using 16.
> > Now if you set the max value to 20, then we'd still use 16, given 20 is higher than 16.
> 
> [@sjeaugey](https://github.com/sjeaugey) Sorry, in my last comment, I change the channels num to 20 by export NCCL_MAX_CTAS=20 , and I expect grid_size can limit to 20, but the trace result shows that it is 32; However，when I change the channels num to 8 by export NCCL_MAX_CTAS=8, the trace result shows it is 8, in this low number, it works again. This phenomenon puzzles me.
```

@sjeaugey hi，I seem to find related code, here is a pow2Up operation. So why use pow2Up, not pow2Down? 

![Image](https://github.com/user-attachments/assets/6a9ad0a5-c9c2-49b6-9148-c659f2865ebf)

### jfc4050 · 2025-05-16

Hello! I think i'm seeing something similar. I'm setting MIN_CTAS at 32 for NCCL ops (via ProcessGroup options). 
i also tried adding these one by one to see if it would help
```
export NVTE_EXT_MARGIN_SM=32
export NVTE_BWD_LAYERNORM_SM_MARGIN=32
export NVTE_FWD_LAYERNORM_SM_MARGIN=32
export NCCL_MIN_CTAS=32
export NCCL_MIN_NCHANNELS=32
export NCCL_MIN_P2P_NCHANNELS=32
export NCCL_NCHANNELS_PER_NET_PEER=32
```

I'm seeing my alltoalls and send/recv running with 2-8 SMs, and i get very poor BW utilization. AG/RS on the other hand show expected behavior of using exactly 32 SMs. So maybe its P2P backed operations specifically that don't respect this value?

also seems like this person was dealing with the same: https://github.com/NVIDIA/nccl/issues/1680

### wanggeng09825 · 2026-03-23

> The number of send/recv channels is controlled by `NCCL_MAX_P2P_NCHANNELS`. `NCCL_MAX_NCHANNELS` controls the number of channels for rings and trees algorithms; `NCCL_NVLS_NCHANNELS` controls the number of channels of the NVLS/NVLSTree algorithms.
> 
> `NCCL_MAX_CTAS` should cap the number of channels for all use cases though. If not, then it's probably a bug.

Hi，since "The number of send/recv channels is controlled by `NCCL_MAX_P2P_NCHANNELS`", if we don`t config NCCL_MAX_P2P_NCHANNELS, in nccl 2.28-9 func ncclResult_t ncclTopoComputerP2pChannels(struct ncclComm*comm)，p2pnChannels inited by nChannels which come from ring/tree. I wonder why p2p`s channels inited by ring/tree. 

Looking forward to your reply. Thank you for your time.

### sjeaugey · 2026-03-23

> I wonder why p2ps channels inited by ring/tree.

It is indeed not great. If you consider an NVLink domain, it kind of makes sense: the number of SMs needed to achieve peak NVLink bandwidth on allreduce and alltoall are linked.

But in the case of a hybrid NVLink + network system, then the number of SMs needed to achieve peak bandwidth is a fraction of what we need for allreduce. Still, latency-wise, using a lot of SMs can help a lot when we have a lot of peers.

So, yes it's kind of weird to base the number of P2P channels on the number of collective channels. It's imperfect. But in many situations it works well.

### wanggeng09825 · 2026-03-24

```bash
> > I wonder why p2ps channels inited by ring/tree.
> 
> It is indeed not great. If you consider an NVLink domain, it kind of makes sense: the number of SMs needed to achieve peak NVLink bandwidth on allreduce and alltoall are linked.
> 
> But in the case of a hybrid NVLink + network system, then the number of SMs needed to achieve peak bandwidth is a fraction of what we need for allreduce. Still, latency-wise, using a lot of SMs can help a lot when we have a lot of peers.
> 
> So, yes it's kind of weird to base the number of P2P channels on the number of collective channels. It's imperfect. But in many situations it works well.
```

I have another question. In nccl 2.28-9, groupsize inited by NCCL_MAX_DEV_WORK_P2P_PER_BATCH when computer rounds for p2p task. I wonder why use NCCL_MAX_DEV_WORK_P2P_PER_BATCH and why its value is 8 .

Thank you for your patience.
BTW, I'm a fan of yours from China.

### LiRunGuo · 2026-09-22

I can reproduce this on current master (2.32.3-1). `ncclTopoComputeP2pChannels()` caps `p2pnChannels` through `nChannels`, which already honors `maxCTAs`, but then rounds it up with `pow2Up()`. So any maxCTAs that isn't a power of 2 is exceeded by send/recv / all-to-all kernels. Test: 4x H200, `alltoall_perf`, SendRecv grid size measured with nsys:

| `NCCL_MAX_CTAS` | coll / p2p channels | SendRecv grid |
|---|---|---|
| 3 | 3 / 4 | up to 4 |
| 5 | 5 / 8 | up to 8 |
| 6 | 6 / 8 | up to 8 |

I'll open a PR that clamps `p2pnChannels` to `pow2Down(maxCTAs)` after the round-up. It keeps the power-of-2 requirement, and the default maxCTAs is unchanged. This is the communicator-level cap, so it should be independent of the per-call `ncclAlltoAllConfig` fix being reviewed for #2421. Happy to adjust if you'd rather handle it there.

