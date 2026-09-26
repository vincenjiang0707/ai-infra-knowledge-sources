# [Issue #7] Ada Lovelace support

source: https://github.com/deepseek-ai/DeepEP/issues/7
state: open | updated: 2026-09-19T09:28:02Z
labels: 

## 正文

Hi team,
Thank you for your excellent work, I wonder if this repo could support  Ada Lovelace architecture such as L20 GPU.

Thanks

## 评论 (9)

### NorthSecond · 2025-02-25

> First of all, I'm not a member of the team. 

In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.

### haswelliris · 2025-02-25

Could you please confirm whether the Ada Lovelace architecture GPUs support GPU Direct RDMA (GDR) and GPU Direct Async (IBGDA)? If so, DeepEP should also be able to run on this architecture.

### wangzhen2271 · 2025-03-11

> > First of all, I'm not a member of the team.
> 
> In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.

Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?

![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)

### Xiaofei-fei · 2025-06-10

> > > First of all, I'm not a member of the team.
> > 
> > 
> > In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.
> 
> Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?
> 
> ![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)

Hi，I wonder have you successfully deployed deepep on L20?

### MengYu10151 · 2025-08-19

> > > > First of all, I'm not a member of the team.
> > > 
> > > 
> > > In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.
> > 
> > 
> > Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?
> > ![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)
> 
> Hi，I wonder have you successfully deployed deepep on L20?
Hi, @Xiaofei-fei I met the same issue as u, have you deployed it successfully?


### Xiaofei-fei · 2025-08-19

> > > > > First of all, I'm not a member of the team.
> > > > 
> > > > 
> > > > In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.
> > > 
> > > 
> > > Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?
> > > ![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)
> > 
> > 
> > Hi，I wonder have you successfully deployed deepep on L20?
> > Hi, [@Xiaofei-fei](https://github.com/Xiaofei-fei) I met the same issue as u, have you deployed it successfully?

We have resolved most of the issues in intranode mode and can now run together with sglang, but some problems are still being worked on.

### Xiaofei-fei · 2025-09-08

> > > > > First of all, I'm not a member of the team.
> > > > 
> > > > 
> > > > In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.
> > > 
> > > 
> > > Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?
> > > ![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)
> > 
> > 
> > Hi，I wonder have you successfully deployed deepep on L20?
> > Hi, [@Xiaofei-fei](https://github.com/Xiaofei-fei) I met the same issue as u, have you deployed it successfully?

btw，I noticed your technical talk on deploying DeepEP on PCIe GPUs, and I am very interested in the idea of merging low-latency and normal-related kernels. Could you please provide a contact so that I can discuss the technical details further?

### MengYu10151 · 2025-09-08

> > > > > > First of all, I'm not a member of the team.
> > > > > 
> > > > > 
> > > > > In my understanding, as long as you have cluster environments with RDMA (usually IB NICs and the corresponding software environment ), NVLink between GPUs, and those environments meet the NVSHMEM requirements, it may be usable.
> > > > 
> > > > 
> > > > Can not work. NVSHMEM does not rely on NVLink. I've tried it on one node with 8 L20 cards. It just won't run successfully. After running for a while, it will report an error. It seems that a certain kernel execution has gone wrong. Can Lyric Zhao give me some hints?
> > > > ![Image](https://github.com/user-attachments/assets/0ac31b46-8f7d-46a3-b37f-1cb732e05d3e)
> > > 
> > > 
> > > Hi，I wonder have you successfully deployed deepep on L20?
> > > Hi, [@Xiaofei-fei](https://github.com/Xiaofei-fei) I met the same issue as u, have you deployed it successfully?
> 
> btw，I noticed your technical talk on deploying DeepEP on PCIe GPUs, and I am very interested in the idea of merging low-latency and normal-related kernels. Could you please provide a contact so that I can discuss the technical details further?

Really appreciate for your attention to our work！Actually we‘ve already submit a PR to support normal mode w/o NVL [https://github.com/deepseek-ai/DeepEP/pull/375](url) ，and you can contact me via wechat  misty10151，thx：）

### 0z5a · 2026-09-19

I’d like to investigate a bounded Ada/L20 compatibility pass here.
@haswelliris 

I noticed that the non-NVLink normal-mode implementation is already present in hybrid-ep through #375, so I am not proposing another PCIe backend.
