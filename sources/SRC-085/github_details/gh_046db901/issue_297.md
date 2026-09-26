# [Issue #297] 投机采样推理问题

source: https://github.com/SafeAILab/EAGLE/issues/297
state: closed | updated: 2025-09-14T03:10:22Z
labels: 

## 正文

请问如果草稿模型未经过训练，我推理后得到的是未经加速的正确结果，还是错误的结果？

## 评论 (2)

### hongyanz · 2025-09-13

正确结果，但有可能比vanilla decoding还要慢，因为drafted tokens检查都不通过，完全依赖大模型生成token。

### Abigbigbig · 2025-09-14

感谢您的解答
