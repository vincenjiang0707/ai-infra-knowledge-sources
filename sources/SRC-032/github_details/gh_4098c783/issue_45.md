# [Issue #45] call aclnnInplaceMaskedFillScalar failed

source: https://github.com/Ascend/pytorch/issues/45
state: open | updated: 2024-08-13T03:48:15Z
labels: 

## 正文

transformers 推理llm，在计算maskattn出现报错

RuntimeError: call aclnnInplaceMaskedFillScalar failed, detail:EZ1001: mask expected scalar type DT_BOOL but found DT_FLOAT.

## 评论 (1)

### yunyiyun · 2024-08-13

数据类型报错，看下输入数据情况
