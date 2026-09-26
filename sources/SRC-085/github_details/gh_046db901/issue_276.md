# [Issue #276] Eagle3 训练Acc length为1.9

source: https://github.com/SafeAILab/EAGLE/issues/276
state: closed | updated: 2025-11-14T10:26:01Z
labels: 

## 正文

在Specforge框架下训练Qwen2.5-7B的Draft model,数据是ShareGPT 5W条，训练5个Epoch以以后在gsm8k上进行测试，Acc为0.83，Acc length为1.9.与论文中的结论相比，差距不小。请问应该如何进行提升呢，采用更多的数据还是说对模型方面进行修改，比如选择不同的hidden_states层多次进行测试？

## 评论 (3)

### hongyanz · 2025-08-16

I don't think we have provided any experimental results on Qwen2.5 in the EAGLE-3 paper. Typically, we have observed that on MOE model, EAGLE will have worse performance than dense model.

### jameswu2014 · 2025-11-13

我训练了 QwQ的 draft model，接受长度 最大 1.86，也是很迷

### ShallowMDream · 2025-11-14

> 我训练了 QwQ的 draft model，接受长度 最大 1.86，也是很迷

没再训这个了。之前在Specforge这边说可以尝试更多的数据200K或者500K。在sglang里测试接受长度2左右。
