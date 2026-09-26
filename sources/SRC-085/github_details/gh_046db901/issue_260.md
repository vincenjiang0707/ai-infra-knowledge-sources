# [Issue #260] 训练qwen2.5-72B oom，请问如何解决

source: https://github.com/SafeAILab/EAGLE/issues/260
state: closed | updated: 2025-07-29T21:41:20Z
labels: 

## 正文

72B的模型单卡80GB无法正常训练是肯定的，目前使用stage3，已经把优化器和param offload到内存了，但是在deepspeed.initialize阶段还是oom了，请问各位大佬有没有解决方法

## 评论 (3)

### hongyanz · 2025-07-27

单卡训练72B的模型肯定训不了，要加卡

### mmdbhs · 2025-07-28

> 单卡训练72B的模型肯定训不了，要加卡

请问有多卡训练的示例代码吗，我再deepspeed config文件里面设置了TP并没有生效

### hongyanz · 2025-07-29

可以参考这个：https://github.com/sgl-project/SpecForge
