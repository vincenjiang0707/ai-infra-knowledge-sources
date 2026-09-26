# [Issue #1437] 微调 PaddleOCR-VL 后模型名称建议重命名为 model.safetensors

source: https://github.com/PaddlePaddle/ERNIE/issues/1437
state: open | updated: 2026-02-26T12:07:30Z
labels: 

## 正文

微调 PaddleOCR-VL 后模型名称建议重命名为 `model.safetensors` ，目前微调后的名称为 `model-00001-of-00001.safetensors`，不方便分发，容易引起困惑。

<img width="1044" height="503" alt="Image" src="https://github.com/user-attachments/assets/f05fced6-d8ca-476b-9a25-444bcdcbadf0" />

model.safetensors.index.json 里面的名称是否应该也一起修改？

关联 issue：https://github.com/PaddlePaddle/PaddleX/issues/5012

## 评论 (1)

### xingmingyyj · 2026-02-26

好的，后续模型仅保存一个出一个safetensors文件时，文件名称使用`model.safetensors`.
