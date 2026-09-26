# [Issue #222] [QUESTION] Can fp8_paged_mqa_logits support next_n > 2?

source: https://github.com/deepseek-ai/DeepGEMM/issues/222
state: open | updated: 2026-04-13T06:56:11Z
labels: 

## 正文

I noticed that the [code](https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/apis/attention.hpp#L166) here in `fp8_paged_mqa_logits` only supports next_n <= 2. May I ask what the reason for this is? Additionally, what modifications would be needed to support next_n > 2? 
Any reply would be very helpful.

## 评论 (4)

### LyricZhao · 2025-12-05

Internally at DeepSeek, we don't use `next_n > 2`. But the NV https://github.com/deepseek-ai/DeepGEMM/tree/nv_dev branch supports such features.

### Paiiiiiiiiiiiiii · 2025-12-07

> Internally at DeepSeek, we don't use `next_n > 2`. But the NV https://github.com/deepseek-ai/DeepGEMM/tree/nv_dev branch supports such features.

I noticed that there is one line (DG_HOST_ASSERT(next_n == 1 or next_n == 2 or next_n == 4);), So now it still dont support nextn=3?

### aiyxxj · 2025-12-31

> Internally at DeepSeek, we don't use `next_n > 2`. But the NV https://github.com/deepseek-ai/DeepGEMM/tree/nv_dev branch supports such features.

I'd like to know if there are any plans to support nextn>2 on the main branch.

### hpz4311 · 2026-04-13

Hello, has this issue been finally resolved? I directly removed the assertion for next_n, and I found that running the test script works fine with next_n = 3, next_n = 4, and so on. Is it okay to just remove the assertion?
