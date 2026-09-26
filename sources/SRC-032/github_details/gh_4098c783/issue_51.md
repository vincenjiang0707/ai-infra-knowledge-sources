# [Issue #51] torch_npu aten::_transformer_encoder_layer_fwd, 运行时有警告出现，该模块未使用NPU而是使用CPU计算

source: https://github.com/Ascend/pytorch/issues/51
state: open | updated: 2024-10-15T07:52:24Z
labels: 

## 正文

CAUTION: The operator 'aten::_transformer_encoder_layer_fwd' is not currently supported on the NPU backend and will fall back to run on the CPU. This may have performance implications. 

torch 2.1.0

How can I compute it on NPU 

## 评论 (2)

### yunyiyun · 2024-09-21

你是用到了TransformerEncoderLayer吗？如果用到了，一种规避方案是在调用该层的forward前，把其中的任意一个入参设置为requires_grad=True，走训练模式

### zezhishao · 2024-10-15

遇到了同样的问题，希望能够解决一下。
