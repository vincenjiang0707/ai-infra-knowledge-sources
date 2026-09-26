# [Issue #211] Eagle-3 for LLAMA4

source: https://github.com/SafeAILab/EAGLE/issues/211
state: closed | updated: 2025-07-24T23:39:18Z
labels: 

## 正文

Thanks for this awesome project.

It would be great to see Lllama 4 eagle-3 support ;) 

Best regards,
T.C

## 评论 (5)

### hongyanz · 2025-04-24

We are working on Llama4. Please stay tuned.

### tchaton · 2025-04-24

@hongyanz This is awesome. Super keen to try it out ! What is the ETA for it ?


Also, would it be possible to share the scripts once done. I am really keen to learn more about it.

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012


### jiahe7ay · 2025-07-02

@tchaton 

### hongyanz · 2025-07-24

@tchaton We have updated our Readme with multiple llama-4 EAGLE-3 head by the community.
