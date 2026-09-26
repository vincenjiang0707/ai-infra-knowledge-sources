# [Issue #1606] ifbench评测集指标问题

source: https://github.com/modelscope/evalscope/issues/1606
state: open | updated: 2026-09-01T10:02:39Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [ ] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [ ] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

<img width="1758" height="494" alt="Image" src="https://github.com/user-attachments/assets/0efbd3a6-3620-4fee-98de-cd56f754c167" />

## EvalScope 版本（必填）
v1.9.1

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

 evalscope eval \
  --model qwen3.5 \
  --eval-batch-size 32 \
  --dataset-args '{"gsm8k": {"few_shot_num": 5}, "ceval": {"few_shot_num": 4}, "ifeval": {"few_shot_num": 0},"ifbench": {"few_shot_num": 0}}' \
  --generation-config '{"max_tokens": 8192, "temperature": 1.0, "top_k":20, "top_p":0.95, "extra_body": {"chat_template_kwargs": {"enable_thinking": false}}}' \
  --api-url http://127.0.0.1:8800/v1 \
  --api-key EMPTY \
  --eval-type openai_api \
  --datasets ifbench \
## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (7)

### Yunnglin · 2026-08-20

你好，截图已收到，可以看到三个 Qwen3.5 模型的 ifbench 指标数值都在正常范围内。但 issue 中没有文字说明你认为哪里有问题，请补充以下信息：

1. **具体问题是什么？** 分数偏低？指标缺失？还是和预期/其他工具对不上？

2. **如果觉得分数低**：IFBench 设计上比 IFEval 难很多，论文中同量级模型（Tülu-3-8B-DPO）也只有 25.5%，你的结果与之吻合。另外你用了 `temperature: 1.0`，高温会拉低指令遵循分数，建议降到 0.0~0.7 重试。

3. **如果怀疑指标计算有误**：请贴完整运行日志（`outputs/<timestamp>/logs/`），留意是否有 `Error calculating ifbench metrics` 行——ifbench 异常会静默跳过，只在日志中报错。

4. **请补充 OS、Python 版本及安装方式**（是否 `pip install 'evalscope[ifbench]'`）。

### joan126 · 2026-08-20

1 问题：分数偏低，官方3.5-9B模型的ifbench 分数是64.5      官方3.5-4B分数是59.2；参考 ：https://www.modelscope.cn/models/Qwen/Qwen3.5-4B

2 这个我尝试过了，temperature:0.3 对于分数提升没有什么帮助

3 是遇到过计算错误：
`2026-08-20 14:23:28 - evalscope - ERROR: Error calculating ifbench metrics:                                                                     
**********************************************************************                                                                          
  Resource 'averaged_perceptron_tagger_eng' not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('averaged_perceptron_tagger_eng')

  For more information see: https://www.nltk.org/data.html

  Attempted to load 'taggers/averaged_perceptron_tagger_eng/'

  Searched in:
    - '/root/nltk_data'
    - '/usr/local/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/local/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'`

但是最后计算的时候是294条，应该把错误的排除掉了吧
4 python : 3.12.13
 OS:Linux c3cd8df77ec2 5.15.0-94-generic #104-Ubuntu SMP Tue Jan 9 15:25:40 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

安装方式：pip install 'evalscope[ifbench]'

### Yunnglin · 2026-08-20

请按下面配置重跑。Qwen3.5 默认是 **Thinking 模式**（会先输出 `<think>` 推理过程再回答），官方 IFBench 分数大概率也是这个模式下测的；**Non-thinking 模式**是直接回答，更快但指令遵循类任务通常会低一些。你之前的配置是「Non-thinking 模式 + Thinking 模式的采样参数」，所以分数偏低。

先下载 NLTK 数据避免报错：

```bash
python -c "import nltk; nltk.download('averaged_perceptron_tagger_eng')"
```

**Thinking 模式（复现官方分数，推荐）：**

```bash
evalscope eval \
  --model qwen3.5 \
  --eval-batch-size 32 \
  --dataset-args '{"ifbench": {"few_shot_num": 0}}' \
  --generation-config '{"max_tokens": 32768, "temperature": 1.0, "top_p": 0.95, "top_k": 20, "presence_penalty": 1.5}' \
  --api-url http://127.0.0.1:8800/v1 \
  --api-key EMPTY \
  --eval-type openai_api \
  --datasets ifbench
```

**Non-thinking 模式（如需对比）：**

```bash
evalscope eval \
  --model qwen3.5 \
  --eval-batch-size 32 \
  --dataset-args '{"ifbench": {"few_shot_num": 0}}' \
  --generation-config '{"max_tokens": 32768, "temperature": 0.7, "top_p": 0.8, "top_k": 20, "presence_penalty": 1.5, "extra_body": {"chat_template_kwargs": {"enable_thinking": false}}}' \
  --api-url http://127.0.0.1:8800/v1 \
  --api-key EMPTY \
  --eval-type openai_api \
  --datasets ifbench
```

跑完有完整 outputs 可以贴上来再分析。


### joan126 · 2026-08-20


评测命令用的上面推荐的，日志中没有评测错误。思考模式仍未对齐。
Qwen3.5-2B模型
第一种方式：思考模式

┌─────────┬───────────┬──────────────────────────┬──────────┬───────┬─────────┬─────────┐
│ Model   │ Dataset   │ Metric                   │ Subset   │   Num │   Score │ Cat.0   │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_prompt_level_strict │ default  │   300 │  0.2333 │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_inst_level_strict   │ default  │   300 │  0.25   │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_prompt_level_loose  │ default  │   300 │  0.27   │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_inst_level_loose    │ default  │   300 │  0.2967 │ default │
└─────────┴───────────┴──────────────────────────┴──────────┴───────┴─────────┴─────────┘ 
第二种非思考模式

┌─────────┬───────────┬──────────────────────────┬──────────┬───────┬─────────┬─────────┐
│ Model   │ Dataset   │ Metric                   │ Subset   │   Num │   Score │ Cat.0   │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_prompt_level_strict │ default  │   300 │  0.25   │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_inst_level_strict   │ default  │   300 │  0.2733 │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_prompt_level_loose  │ default  │   300 │  0.3033 │ default │
├─────────┼───────────┼──────────────────────────┼──────────┼───────┼─────────┼─────────┤
│ qwen3.5 │ ifbench   │ mean_inst_level_loose    │ default  │   300 │  0.3333 │ default │
└─────────┴───────────┴──────────────────────────┴──────────┴───────┴─────────┴─────────┘ 

### Yunnglin · 2026-08-21

目前没有发现 EvalScope IFBench 评测框架存在问题。使用 `qwen3.5-27b` 并开启 Thinking 测试，258 条样本的 prompt-level loose 约为 78%，与官方结果基本一致。建议检查实际部署的模型版本、Thinking 模式及推理参数。如仍有差异，可以提供完整 outputs 进一步分析。

### heron-yang · 2026-08-27

我也遇到了同样问题，我跑的是qwen3.8 27b 出来结果得分才37


### Yunnglin · 2026-08-27

@heron-yang 感谢补充。Qwen3.8-27B 模型卡公布的 IFBench 分数为 79.5，37 分存在明显差距，但目前还缺少定位信息。

请补充 EvalScope 版本、精确模型 ID/量化方式、推理框架及版本、服务启动命令、完整评测命令，以及脱敏后的 outputs。特别请确认 vLLM 是否配置了 `--reasoning-parser qwen3`。Qwen3.8 默认开启 Thinking；若 reasoning 未被服务端分离而混入 `message.content`，IFBench 的格式、字数等约束会把思考过程一并计入，可能显著拉低分数。

另外请说明“37”对应哪个指标；IFBench 官方通常报告 `prompt-level loose`，需确保比较口径一致。最好再提供一条原始 Chat Completions 响应，以确认 `content` 与 `reasoning_content` 是否正确分离。

