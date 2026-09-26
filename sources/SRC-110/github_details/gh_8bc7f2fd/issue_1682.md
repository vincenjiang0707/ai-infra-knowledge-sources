# [Issue #1682] [bug] omni_doc_bench_v1_6，GLM-OCR两阶段模型，测评精度数值异常

source: https://github.com/modelscope/evalscope/issues/1682
state: open | updated: 2026-08-31T06:51:36Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

- glm-ocr模型是两阶段模型，需要先经过layout模型再使用recognize模型
- evalscope当前仅支持E2E模型，无法处理像glm-ocr或paddleocr-vl等模型，导致最终精度差异很大
- 官方测评 `95.445` vs evalscope测评 `73.0`

```python
from evalscope import run_task
from evalscope.config import TaskConfig
task_cfg = TaskConfig(
    model='glm-ocr',
    api_url='http://10.24.9.1:7092/v1',
    api_key='EMPTY_TOKEN',
    datasets=['omni_doc_bench_v1_6'],
    sandbox={'enabled': True},
    seed=42,
    eval_batch_size=8,
    repeats=1,
    timeout=600,
    generation_config={"do_sample":True, "max_tokens": 32768, "temperature":0.0, "top_p": 0.00001, "repetition_penalty": 1.1, "extra_body": {"chat_template_kwargs":{"enable_thinking": False}}}, # 对齐官方
    work_dir='outputs/outputs_glm',
)
run_task(task_cfg=task_cfg)
```
<img width="713" height="337" alt="Image" src="https://github.com/user-attachments/assets/b49079f5-3f1b-45aa-a4cc-59a07bb43a64" />


> 以下官方测试
```python
glmocr parse datasets/OmniDocBench/images \
--set pipeline.maas.enabled false \
--set pipeline.ocr_api.api_host 10.24.9.1 \
--set pipeline.ocr_api.api_port 7092 \
--set pipeline.ocr_api.model glm-ocr\
--set pipeline.result_format.enable_merge_formula_numbers false \
--set pipeline.layout.model_dir models/ocr/PP-DocLayoutV3_safetensors \
--layout-device cpu \
--output ./results_samples_0831

sudo docker run -it \
    -v datasets/OmniDocBench/OmniDocBench.json:/workspace/gt/your_gt.json:ro \
    -v results_samples_0831_md:/workspace/data_md/predictions:ro \
    -v results_samples_0831_md_metric:/workspace/result \
    --entrypoint bash \
    docker.gh-proxy.org/ghcr.io/zeng-weijun/omnidocbench-eval:repro-ubuntu2204 \
    -c '
printf "end2end_eval:
    metrics:
        text_block:
            metric: [Edit_dist]
        display_formula:
            metric: [Edit_dist, CDM]
        table:
            metric: [TEDS, Edit_dist]
        reading_order:
            metric: [Edit_dist]
    dataset:
        dataset_name: end2end_dataset
        ground_truth:
            data_path: /workspace/gt/your_gt.json
        prediction:
            data_path: /workspace/data_md/predictions
        match_method: quick_match
        match_workers: 4
        quick_match_truncated_timeout_sec: 300
        timeout_fallback_max_chunk_span: 10
        timeout_fallback_order_penalty: 0.10
" > configs/custom.yaml && \
python -c "import sys; sys.setrecursionlimit(10000); exec(open(\"pdf_validation.py\").read())" --config configs/custom.yaml
'

         text_block_Edit_dist  display_formula_CDM  table_TEDS  table_TEDS_structure_only  reading_order_Edit_dist  overall
GLM-OCR                 0.039               96.772      93.463                     96.071                    0.138   95.445
```


## EvalScope 版本（必填）
2026/08/31，latest commit
Commit: 664af6091d7e7ef316838020e9a546542976bd2b

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 运行环境

- 操作系统：ubuntu20.04
- Python版本：python3.10

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (1)

### Yunnglin · 2026-08-31

感谢反馈。EvalScope 当前按端到端方式评测：输入整页图片并直接获取 Markdown，不会执行 GLM-OCR 所需的 layout 阶段；而官方流程包含 `PP-DocLayoutV3 + glm-ocr`，因此两组结果暂不可直接比较。

请确认您的 API 是否已封装完整的 layout + recognize pipeline。若仅提供 recognize 服务，需要先封装完整 pipeline 再接入 EvalScope。我们也会评估后续对多阶段 OCR pipeline 的支持。
