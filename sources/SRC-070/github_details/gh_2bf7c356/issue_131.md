# [Issue #131] Ways to do overlapping of computation and commucation.

source: https://github.com/deepseek-ai/DeepEP/issues/131
state: closed | updated: 2026-09-20T01:56:34Z
labels: 

## 正文

Hello, I'm trying to use DeepEP and intergate it into Megatron (with this commit https://github.com/NVIDIA/Megatron-LM/commit/0d389f5e9935957b146c12b1dcdddc35cf9deb85),  and accomplish overlapping of computation and commucation, I've noticed DeepEP is using previous_event and async_finish args in dispatch and combine methods to support the overlapping , whereas the FlexTokenDispatcher in that commit doesn't adopt any of them. For me, there are two ways to do that:
* modify FlexTokenDispatcher and pass args previous_event,  async_finish etc. to make use of DeepEP's overlapping interface。
* keep FlexTokenDispatcher as it is, and manage the stream and event outside by myself before calling dispatch and combine under the context of torch.cuda.stream(),  which means DeepEP's pevious_event,  async_finish won't be used. 

Can you guys give me some suggestions about the two ways in term of performance?

## 评论 (1)

### LyricZhao · 2025-04-25

I highly recommend you to use the first way, as the current DeepEP design may fail to cover some edge cases for the second (e.g. some `record_stream`/reuse GPU mem problems).

In terms of performance, I guess no diff between these if they can perfectly overlap.
