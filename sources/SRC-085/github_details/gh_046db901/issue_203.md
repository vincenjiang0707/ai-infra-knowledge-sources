# [Issue #203] When will EAGLE3 support Qwen- QWQ model？

source: https://github.com/SafeAILab/EAGLE/issues/203
state: open | updated: 2025-07-02T08:55:38Z
labels: 

## 正文

(empty)

## 评论 (2)

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012

### Ximingwang-09 · 2025-07-02

> 我们已基于官方训练代码成功训练 Eagle3 版本的 Qwen3-8B 和 Qwen3-30B-A3B，并已开源。在单块 H200 GPU 上使用 sglang 推理框架，Qwen3-8B 搭配 Eagle3 的性能提升从 186 个 token/秒提升至 365 个 token/秒，Qwen3-30B-A3B 搭配 Eagle3 的性能提升从 147 个 token/秒提升至 231 个 token/秒。
> 
> 我们使用了ultra_200k测试集，并在Qwen3上重新进行推理，重新生成数据，作为最终的训练集。总共使用了600K个对话作为训练集。
> 
> https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3
> 
> https://huggingface.co/Tengyunw/qwen3_8b_eagle3
> 
> 此外，我们还发布了一份报告，详细介绍了如何复现 Eagle3 的训练过程。报告链接如下，如有需要，可供参考。
> 
> https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA
> 
> https://zhuanlan.zhihu.com/p/1923763301432662012

Great Work! But If we are using it in a Chinese context, how should we control the dataset ratio？The target model has also undergone fine-tuning
