# [Issue #80] How to replace enable_xformers_memory_efficient_attention in xformers？

source: https://github.com/Ascend/pytorch/issues/80
state: closed | updated: 2025-10-24T02:23:01Z
labels: 

## 正文

The source code uses functions such as self.pipe.enable_xformers_memory_efficient_attention() and self.pipe.enable_attention_slicing() to speed up model inference. 

What command should be used instead in Ascend's PyTorch? 



<img width="1290" height="519" alt="Image" src="https://github.com/user-attachments/assets/93db9567-1978-4fc2-a3a3-a0bf177349b7" />

## 评论 (2)

### yunyiyun · 2025-10-15

目前暂不原生支持xFormers训练，如需使用xFormers中的FlashAttentionScore融合算子的迁移，用户可参考[FlashAttentionScore](https://www.hiascend.com/document/detail/zh/Pytorch/710/ptmoddevg/trainingmigrguide/performance_tuning_0034.html)章节进行替换。

https://www.hiascend.com/document/detail/zh/Pytorch/710/ptmoddevg/trainingmigrguide/performance_tuning_0034.html

### yiiizuo · 2025-10-24

I have resolved this issue.
