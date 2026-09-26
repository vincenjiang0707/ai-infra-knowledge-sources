# [Issue #241] 放出来的代码都不管能不能跑通的吗？

source: https://github.com/SafeAILab/EAGLE/issues/241
state: closed | updated: 2025-07-02T08:46:19Z
labels: 

## 正文

真服了，各种报错

## 评论 (9)

### jiahe7ay · 2025-06-23

亲测，代码是能直接一次跑通的。你看下是不是环境没有配对

### mmdbhs · 2025-06-24

> 真服了，各种报错

deepspeed使用0.16.0版本可以正常跑，不要用0.17.1，一堆报错

### Arcmoon-Hu · 2025-06-24

![Image](https://github.com/user-attachments/assets/153b02eb-9957-4323-bada-48f70f3f6737)

> 亲测，代码是能直接一次跑通的。你看下是不是环境没有配对

同学，你跑的是eagle3吗，我跑的时候代入自己数据集，然后forward的时候，这一段对应不起来啊，因为那个self.t2d的gather，维度对应不上吧

### jiahe7ay · 2025-06-24

@Arcmoon-Hu  你数据集太小了，所以使用comom_counter之后获取高频词的词量少于draft_vocab_size的32000大小，我最开始测试也会这样，后面直接跑全数据集就没有这个错了


### Arcmoon-Hu · 2025-06-25

> [@Arcmoon-Hu](https://github.com/Arcmoon-Hu) 你数据集太小了，所以使用comom_counter之后获取高频词的词量少于draft_vocab_size的32000大小，我最开始测试也会这样，后面直接跑全数据集就没有这个错了

确实

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012

### jiahe7ay · 2025-07-02

@Arcmoon-Hu 可以参考一下，我刚复现了qwen3的egale3了

### Arcmoon-Hu · 2025-07-02

> [@Arcmoon-Hu](https://github.com/Arcmoon-Hu) 可以参考一下，我刚复现了qwen3的egale3了

牛逼，我后来也跑通了，但是请问一下，吞吐量测试的时候有测试并发的性能吗？我是使用了sglang测试的， 单卡的时候确实速度飞起，接近两倍的提升，acc len达到3～5吧，但是并发一高，速度和吞吐就直线下降。。。比单模型部署低的多，但是原论文里的实验看着是batch size虽然增加但加速比还是有1.x至少不慢于单模型

![Image](https://github.com/user-attachments/assets/97ca1f43-271b-49f9-8843-0cd4972cbc3a)

### jiahe7ay · 2025-07-02

@Arcmoon-Hu 我刚刚测了一下，并发一高确实性能下降挺明显的，没有达到论文的效果。
