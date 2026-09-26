# [Issue #65] flash_attn.flash_attn_varlen_qkvpacked_func 有替换的算子吗

source: https://github.com/Ascend/pytorch/issues/65
state: open | updated: 2025-08-31T03:37:52Z
labels: 

## 正文

(empty)

## 评论 (2)

### yunyiyun · 2025-07-04

https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0027.html
将flash_attn_varlen_qkvpacked_func的输入qkv unpad成三个输入q,k,v，然后参考flash_attn_varlen_func就可以替换了

### hayd-zju · 2025-08-31

请问flash_attn_varlen_qkvpacked_func的输出和torch_npu.npu_fusion_attention的输出是否一致呢

