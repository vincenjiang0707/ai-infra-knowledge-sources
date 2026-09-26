# [Issue #198] When will the EAGLE3 support for Qwen2

source: https://github.com/SafeAILab/EAGLE/issues/198
state: open | updated: 2025-07-02T08:51:02Z
labels: 

## 正文

I'm impressed with Eagle3's inference performance. However, I noticed that it doesn't support Qwen2 yet. When will Qwen2 support be available?

## 评论 (4)

### luoruijie · 2025-04-10

I also want konw when will Qwen2.5 suuport be available?

### chtaihei-ust-hk · 2025-04-29

Also Qwen3

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012

### jiahe7ay · 2025-07-02

@garycaokai @luoruijie @chtaihei-ust-hk 
