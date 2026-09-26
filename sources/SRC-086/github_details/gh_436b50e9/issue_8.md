# [Issue #8] megatron-llm模型的支持

source: https://github.com/FasterDecoding/Medusa/issues/8
state: closed | updated: 2023-09-13T17:58:44Z
labels: 

## 正文

请问支持megatron-llm模型吗？迁移到megatron-llm有什么注意事项吗？

## 评论 (2)

### leeyeehoo · 2023-09-13

你好，目前只支持vicuna7/13/33b。可以refer我们的roadmap，如果有什么建议可以comment。谢谢！

### ctlllll · 2023-09-13

如果想迁移到megatron进行训练，可以参考我们的[训练脚本](https://github.com/FasterDecoding/Medusa/blob/main/medusa/train/train.py)，改动的地方非常少，应该比较容易迁移。也欢迎提PR添加训练脚本~
