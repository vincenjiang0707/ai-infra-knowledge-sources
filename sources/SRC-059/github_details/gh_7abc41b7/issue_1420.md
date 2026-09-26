# [Issue #1420] paddocr-vl 微调如何冻结视觉参数以减少显存占用

source: https://github.com/PaddlePaddle/ERNIE/issues/1420
state: open | updated: 2026-01-22T08:38:29Z
labels: 

## 正文

(empty)

## 评论 (2)

### forBlank · 2026-01-13

ERNIEKit 暂时不支持，我们将在后续 PaddleFormers 的更新中支持该功能

### forBlank · 2026-01-22

PaddleFormers 1.0 已发布，可以在输入参数中传入 freeze_config=freeze_vision 冻结视觉参数，SFT 训练可以参考 [PaddleFormers & PaddleOCR-VL Best Practices](https://github.com/PaddlePaddle/PaddleFormers/tree/release/v1.0/examples/best_practices/PaddleOCR-VL)
