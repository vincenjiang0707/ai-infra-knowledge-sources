# [Issue #1246] Question about Group Assignment for P2P Primitives

source: https://github.com/ROCm/rccl/issues/1246
state: closed | updated: 2024-12-03T15:16:11Z
labels: Under Investigation

## 正文

Hi Everyone,

I am using rccl 6.1.2. For the P2P tests, such as scatter and gather, I find that the logic in the appendWorkElemP2p and finishWorkP2p functions of enqueue.cc entails the following:

- If there's both send and recv on a channel, group is 2: 2 64-thread warps for send and 2 for recv.
- If there's only recv, group is 1: 4 warps only for recv.
- If there's only send, group is 2: 2 warps operate on send and 2 warps are idle!

I wanted to understand the reasoning behind the last item, i.e., when there's only send primitives. This happens in the following situations:

- In gather, all GPUs except the root have only send primitives to the root.
- In scatter, the root GPU has only send primitives to all other GPUs.

Best,
Alireza

## 评论 (2)

### schung-amd · 2024-10-31

Hi @arkhadem, are you seeing this in practice, or inferring from the source code? If the former, what's your hardware configuration (i.e. number and type of GPU)? 

### schung-amd · 2024-12-03

Closing for now as I need some clarification on the question to give a definitive answer. Feel free to comment here with clarification and we can reopen if necessary.
