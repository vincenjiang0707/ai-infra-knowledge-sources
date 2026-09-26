# [Issue #859] ValueError: No nodes that satisfied the given filer. Try changing the filter.

source: https://github.com/modelscope/evalscope/issues/859
state: closed | updated: 2026-07-08T06:28:13Z
labels: bug, rageval

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [√] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [√] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [√] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

用ragas生成测试数据集时报错ValueError: No nodes that satisfied the given filer. Try changing the filter.   

## EvalScope 版本（必填）

v1.0.2

## 使用的工具

RAGAS v0.2.14

## 执行的代码或指令

from evalscope.run import run_task
from evalscope.utils.logger import get_logger

generate_testset_task_cfg = {
    "eval_backend": "RAGEval", 
    "eval_config": {
        "tool": "RAGAS",
        "testset_generation": {
            "docs": ["**.txt"], 
            "test_size": 10,
            "output_file": "outputs/test1/qwen_testset.json",
            "knowledge_graph": "outputs/test1/qwen_knowledge_graph.json",
            "generator_llm": {
                "model_name": "qwen2.5-vl-72b-instruct",
                "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",
                "api_key": "*****",
                "generation_config": {
                    "temperature": 0.7,
                    "max_tokens": 1024  
                }
            },
            
            "embeddings": {
                "model_name": "Qwen3-Embedding-0.6B",  
                "api_base": "******",
                "api_key": "EMPTY",  
                "dimension": 1024
            },
            "language": "chinese"  
        }
    },
}

logger = get_logger()
run_task(task_cfg=generate_testset_task_cfg)

## 错误日志

Traceback (most recent call last):
  File "test.py", line 35, in <module>
    run_task(task_cfg=generate_testset_task_cfg)
  File ".venv\Lib\site-packages\evalscope\run.py", line 28, in run_task
    return run_single_task(task_cfg, run_time)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\evalscope\run.py", line 39, in run_single_task
    result = run_non_native_backend(task_cfg, outputs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\evalscope\run.py", line 89, in run_non_native_backend
    backend_manager.run()
  File ".venv\Lib\site-packages\evalscope\backend\rag_eval\backend_manager.py", line 88, in run
    self.run_ragas(testset_args, eval_args)
  File ".venv\Lib\site-packages\evalscope\backend\rag_eval\backend_manager.py", line 58, in run_ragas
    generate_testset(TestsetGenerationArguments(**testset_args))
  File ".venv\Lib\site-packages\evalscope\backend\rag_eval\ragas\tasks\testset_generation.py", line 109, in generate_testset
    persona_list = get_persona(llm=wrapped_llm, kg=knowledge_graph, language=args.language)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\evalscope\backend\rag_eval\ragas\tasks\testset_generation.py", line 66, in get_persona
    return generate_personas_from_kg(llm=llm, kg=kg, num_personas=3, persona_generation_prompt=persona_prompt)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\ragas\testset\persona.py", line 95, in generate_personas_from_kg
    raise ValueError(
ValueError: No nodes that satisfied the given filer. Try changing the filter. 

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

已经尝试过修改min_num_tokens=0，仍无法解决。


## 评论 (2)

### Yunnglin · 2026-06-02

PR #1383 已合并，将 RAGAS 升级到 0.4.x 并对 RAG eval 模块做了重构。该 issue 涉及 RAGAS testset generation 中 persona 节点过滤的报错（`No nodes that satisfied the given filter`），属于 RAGAS 内部 KG 节点筛选逻辑问题，需要在新版本上验证。

请从最新 main 分支安装后再次尝试，并反馈是否仍能复现。如新版本仍有问题，我们会进一步跟进。

### Yunnglin · 2026-07-08

This issue was reported against the legacy RAGEval / RAGAS 0.2.x path.

RAG evaluation has been refactored in PR #1383, and RAGAS has been upgraded to the 0.4.x series. The original error (`No nodes that satisfied the given filter`) is related to RAGAS testset generation / KG node filtering in the old stack, so the first step is to verify with the latest main branch.

Closing this for now as a legacy RAGEval issue. If it can still be reproduced on the latest main branch, please reopen with:

1. EvalScope commit / version
2. RAGAS version
3. Full config
4. Minimal docs sample
5. Complete traceback

We'll continue from there if the issue still exists.

