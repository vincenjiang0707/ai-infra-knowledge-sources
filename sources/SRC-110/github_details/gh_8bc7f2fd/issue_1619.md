# [Issue #1619] eval-batch-size为什么不生效

source: https://github.com/modelscope/evalscope/issues/1619
state: closed | updated: 2026-08-24T05:57:06Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

openapi模式下，eval-batch-size为啥设置了但是无效

## EvalScope 版本（1.9.1）

## 使用的工具
- [x] Native / 原生框架

## 执行的代码或指令
```
task_cfg = {
    "model": "Qwen3.5-9B", 
    "eval_type": "openai_api",
    "eval-batch-size": 10,
    "api_url": "http://127.0.0.1:8000/v1",
    "api_key": "dummy",
    "datasets": ["cmmlu"],
    "dataset_args": {
        "cmmlu": {
        	"system_prompt": NO_THINK_PROMPT
        }
    },
    "generation_config": {
        "max_tokens": 1024,
        "temperature": 0.01,
        "top_p": 0.95,
        'extra_body':{'chat_template_kwargs': {'enable_thinking': False}}
    },
    "work_dir": "./outputs_cmmlu_qwen35_9b",
    "debug": False,
#    "limit": 1
}
```
## 错误日志

vllm服务端running始终是`1`，waiting始终是`0`

## 运行环境

- 操作系统：Alibaba Cloud Linux 3.2104
- Python版本：3.19

## 其他信息

文档里明确写了：
> 评测批量大小，作用于以下阶段：
> 推理阶段：并发请求数（service模式）或批量大小（checkpoint模式）

我看也没有eval-type，service模式这个选项，我用的open_api模式，不知道为啥使用是只有一个请求正在处理


## 评论 (1)

### Yunnglin · 2026-08-24

感谢反馈，这个问题定位到了，是配置项名字写错了但框架没报错导致的。

**原因**：你写的是 `"eval-batch-size"`（连字符），而 `TaskConfig` 的字段名是 `eval_batch_size`（下划线）。连字符形式只在命令行上成立（`--eval-batch-size`），Python dict / YAML / JSON 里必须用下划线。更糟的是当前版本会**静默忽略**这个无法识别的 key，所以 `eval_batch_size` 一直是默认值 `1`，推理线程池只有一个 worker，vLLM 端自然就是 `running=1, waiting=0`。

**修复方法**：

```python
task_cfg = {
    "model": "Qwen3.5-9B",
    "eval_type": "openai_api",
    "eval_batch_size": 10,      # 下划线，不是连字符
    ...
}
```

**关于文档里的「service 模式」**：这是旧版术语，对应现在的 `eval_type="openai_api"`，你的用法是对的，文档措辞该更新。

我们会在后续版本改进两点：

1. 无法识别的配置项不再静默忽略，而是直接报错并提示最接近的正确字段名，例如：
   ```
   'eval-batch-size' is not a valid TaskConfig field -- did you mean 'eval_batch_size'?
   ```
2. `openai_api` 模式下 `eval_batch_size` 未显式指定时，默认值从 `1` 提升到 `8`（与文档描述一致），避免默认串行请求。

