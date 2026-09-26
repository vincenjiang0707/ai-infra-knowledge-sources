# [Issue #1357] 关于 ERNIE-KIT 微调 PaddleOCR-VL 模型时自定义 prompt 和多印章处理的咨询

source: https://github.com/PaddlePaddle/ERNIE/issues/1357
state: closed | updated: 2026-02-14T03:01:59Z
labels: 

## 正文

问题描述
在使用 ERNIE-KIT 工具微调 PaddleOCR-VL 模型时，是否支持自定义 prompt，而不仅限于论文中提到的以下四种固定 prompt？
TASKS = {
    "ocr": "OCR:",
    "table": "Table Recognition:",
    "formula": "Formula Recognition:",
    "chart": "Chart Recognition:",
}



业务场景说明
从图片中提取印章信息，并输出为结构化的数据格式（例如 JSON 结构体）。希望了解是否可以通过微调 PaddleOCR-VL 模型来实现这一目标。

如果可以微调实现，想了解关于数据方面的输入格式，例如
1. 多印章的场景：同一张图片中可能包含多个印章，需要如何组织数据格式
2.如何表示多印章的标注信息，输出结构体的字段定义示例


自己通过网络、开源代码和paddle文档，已完成以下工作
1. 已经阅读PaddleOCR-VL-0.9B的训练文档，有ERNIE-4.5-0.3B-Paddle的训练经验
https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/best_practices/ERNIE-4.5-0.3B-Paddle.md
https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/best_practices/PaddleOCR-VL-0.9B.md

2. 阅读paddleocr-vl进行推理的部份源码
```python
        if not model_settings["use_layout_detection"]:
            prompt_label = prompt_label if prompt_label else "ocr"
            if prompt_label.lower() == "chart":
                model_settings["use_chart_recognition"] = True
            assert prompt_label.lower() in [
                "ocr",
                "formula",
                "table",
                "chart",
            ], f"Layout detection is disabled (use_layout_detection=False). 'prompt_label' must be one of ['ocr', 'formula', 'table', 'chart'], but got '{prompt_label}'."
```
3. 阅读论文


## 评论 (2)

### forBlank · 2025-11-15

@hurun 你好，
1、多印章的场景：用 PP-DocLayoutV2 将多印章图像拆分成多张单印章图像，再使用 PaddleOCR-VL-0.9B 进行单印章识别；
2、印章表示：直接用文本表示印章内容，如需结构化表示可自定义需要的字段；
3、自定义 prompt：在构建数据样本时，使用自定义的字段作为查询 Query 即可，数据格式可参考 https://github.com/PaddlePaddle/ERNIE/blob/develop/docs/paddleocr_vl_sft_zh.md#32-%E6%95%B0%E6%8D%AE%E9%9B%86%E5%87%86%E5%A4%87

### nepeplwu · 2026-02-14

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
