# [Issue #1373] 问一下paddleocr_VL 表格微调训练的格式

source: https://github.com/PaddlePaddle/ERNIE/issues/1373
state: open | updated: 2025-12-17T03:57:08Z
labels: 

## 正文

[ERNIE](https://github.com/PaddlePaddle/ERNIE/tree/release/v1.4)/[docs](https://github.com/PaddlePaddle/ERNIE/tree/release/v1.4/docs)
/paddleocr_vl_sft_zh.md 中建议为OTSL 格式，但是为什么我是用表格数据输入原始模型部署后输出的是markdown格式，到底应该用哪种格式去微调表格？

## 评论 (2)

### bailvwangzi · 2025-11-19

用otsl，可能是pipeline后处理的步骤给转的markdown

### forBlank · 2025-12-17

@xutongxi @bailvwangzi 感谢关注，微调表格使用的是 OTSL 格式，如何从表格获取 OTSL 标注可参考 #1396 ，为了便于观察表格识别结果，推理输出的 OTSL 格式会经过后处理成 HTML 格式，再用 markdown 表示 HTML，转换代码可参考 [convert_otsl_to_html](https://github.com/PaddlePaddle/PaddleX/blob/release/3.3/paddlex/inference/pipelines/paddleocr_vl/uilts.py#L810)
