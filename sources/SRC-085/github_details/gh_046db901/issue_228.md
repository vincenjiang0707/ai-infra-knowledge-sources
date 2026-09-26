# [Issue #228] Eagle Training Parameters and Hardware Requirements

source: https://github.com/SafeAILab/EAGLE/issues/228
state: open | updated: 2025-07-02T07:45:13Z
labels: 

## 正文

Thank you for your work!

I'm currently trying to reproduce your Eagle-1 and Eagle-3 training.
Could you please share what hardware was used for training, the batch size used, number of epochs, and how long the training took?
You write in the article that Eagle-1 training for a 7B model can take around 1-2 days on an RTX 3090, but in my experiments, it takes way more than that.

Thank you!

## 评论 (1)

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012
