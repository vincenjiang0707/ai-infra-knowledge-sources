# [Issue #242] where is the training data and test data?

source: https://github.com/SafeAILab/EAGLE/issues/242
state: closed | updated: 2025-07-07T08:41:48Z
labels: 

## 正文

well, when I run the train script as u said in readme, but I didn't find u provide the training data and test data. Moreover, according  to your paper, u used sharegpt-68k and ultrachic-200k as your train data? And maybe use 10% for test?

## 评论 (7)

### charmway · 2025-06-13

same

### Siegfried-qgf · 2025-06-13

same. The code is a mass

### Eureca2017 · 2025-06-23

same

### rainkert · 2025-07-01

same


### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012

### jiahe7ay · 2025-07-04

We have now open-sourced our training data regenerated using Qwen3-8B.  https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3

### youngze0016 · 2025-07-07

> We have now open-sourced our training data regenerated using Qwen3-8B. https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3

thanks! I will have a try!

