# [Issue #1546] [Bug]在GPQA‑Diamond数据集上判题有误

source: https://github.com/modelscope/evalscope/issues/1546
state: closed | updated: 2026-08-06T04:33:56Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [ ] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [ ] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

模型是DeepSeekV4  Flash dspark，开启thinking，在GPQA‑Diamond数据集上，会有概率提取不出模型答案，导致判题错误。例如下例：
```json
{"index": 195, "target": "B", "messages": [{"id": "0b812c57", "content": "Answer the following multiple choice question. The last line of your response should be of the following format: 'ANSWER: [LETTER]' (without quotes) where [LETTER] is one of A,B,C,D. Think step by step before answering.\n\n Consider a 1-dimensional relativistic harmonic oscillator with mass $m$ and maximum amplitude $A$ obeying Hook's law ($F=-kx$). What is the maximum speed  $v_max$ of the mass? The speed of light is $c$.\n\nA) $v_{max}=c\\sqrt{1+\\frac{1}{(1-\\frac{kA^2}{2m})^2}}$\nB) $v_{max}=c\\sqrt{1-\\frac{1}{(1+\\frac{kA^2}{2mc^2})^2}}$\nC) $v_{max}=\\sqrt{\\frac{kA^2}{m}}$\nD) $v_{max}=c\\sqrt{1+\\frac{1}{(1-\\frac{kA^2}{2mc^2})}}$", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}, {"id": "f5c6a1f7", "content": "We need answer physics. Need think step by step but final format ANSWER: [LETTER]. Question: 1-dimensional relativistic harmonic oscillator with mass m and maximum amplitude A obeying Hook's law F=-kx. What is maximum speed? Options.\n\nRelativistic harmonic oscillator with Hooke's law? Force F = -kx. Need relativistic equation: dp/dt = -kx where p = γ m v. At maximum amplitude A, v=0, potential energy? Work done by force? F = -kx so potential energy V = (1/2) k x^2. At x=A, v=0, total energy = mc^2 + (1/2) k A^2 (rest energy plus potential). At x=0, potential zero, kinetic relativistic energy = (γ -1) m c^2 = (1/2) k A^2. So γ = 1 + kA^2/(2 m c^2). Then v/c = sqrt(1 - 1/γ^2) = sqrt(1 - 1/(1 + kA^2/(2mc^2))^2). So v_max = c sqrt{1 - 1/(1 + kA^2/(2mc^2))^2}. Option B.\n\nNeed answer.</think>ANSWER: B", "source": "generate", "metadata": null, "internal": null, "perf_metrics": {"latency": 43.85242365999147, "ttft": 32.16595136001706, "input_tokens": 220, "output_tokens": 274, "tpot": 0.04280759084239711}, "role": "assistant", "tool_calls": null, "model": "DeepSeek-V4-Flash"}], "agent_trace": null, "sample_score": {"score": {"value": {"acc": 0.0}, "extracted_prediction": "", "prediction": "We need answer physics. Need think step by step but final format ANSWER: [LETTER]. Question: 1-dimensional relativistic harmonic oscillator with mass m and maximum amplitude A obeying Hook's law F=-kx. What is maximum speed? Options.\n\nRelativistic harmonic oscillator with Hooke's law? Force F = -kx. Need relativistic equation: dp/dt = -kx where p = γ m v. At maximum amplitude A, v=0, potential energy? Work done by force? F = -kx so potential energy V = (1/2) k x^2. At x=A, v=0, total energy = mc^2 + (1/2) k A^2 (rest energy plus potential). At x=0, potential zero, kinetic relativistic energy = (γ -1) m c^2 = (1/2) k A^2. So γ = 1 + kA^2/(2 m c^2). Then v/c = sqrt(1 - 1/γ^2) = sqrt(1 - 1/(1 + kA^2/(2mc^2))^2). So v_max = c sqrt{1 - 1/(1 + kA^2/(2mc^2))^2}. Option B.\n\nNeed answer.</think>ANSWER: B", "explanation": null, "metadata": {}, "main_score_name": null}, "sample_id": 195, "group_id": 195, "sample_metadata": {"correct_answer": "$v_{max}=c\\sqrt{1-\\frac{1}{(1+\\frac{kA^2}{2mc^2})^2}}$", "incorrect_answers": ["$v_{max}=c\\sqrt{1+\\frac{1}{(1-\\frac{kA^2}{2mc^2})}}$", "$v_{max}=c\\sqrt{1+\\frac{1}{(1-\\frac{kA^2}{2m})^2}}$", "$v_{max}=\\sqrt{\\frac{kA^2}{m}}$"]}}}
```

## EvalScope 版本（必填）
v0.16.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

```sh
evalscope eval \
    --model "DeepSeek-V4-Flash" \
    --api-url http://127.0.0.1:30000/v1 \
    --api-key EMPTY \
    --eval-type openai_api \
    --generation-config '{"max_tokens":120000,"top_p":1,"temperature":1,"timeout":6000,"stream":true,"extra_body":{"chat_template_kwargs":{"thinking":true}}}' \
    --datasets gpqa_diamond \
    --dataset-args '{"gpqa_diamond":{"local_path":"gpqa","subset_list":["gpqa_diamond"]}}' \
    --eval-batch-size 198 \
    --ignore-errors
```

## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (1)

### Yunnglin · 2026-08-06

感谢反馈，已在 #1549 修复并合并到 main。

**根因**（两个，都会导致您这条样本被判 0 分）：

1. `parse_answers` 的答案正则允许捕获组匹配到纯空格。您的输出里模型先复述了提示词要求的格式 `ANSWER: [LETTER]`，这个复述被正则先匹配到、捕获到一个空格，strip 后为空，真正的 `ANSWER: B` 就被跳过了。现已要求捕获组必须以字母或数字开头。

2. 更关键的是：**配置的 `filters` 对选择题类基准完全不生效**。框架的 `filter_prediction()` 会先跑过滤器、再把过滤后的文本传给 `extract_answer()`，但选择题的实现丢弃了这个参数、重新去读原始输出，导致 `dataset_args.filters` 被静默忽略。也就是说在此之前，您即使自己配 `remove_until` 也没法绕过这个问题。现已修好。

**关于 `</think>`**：您的输出里只有闭合的 `</think>` 而没有开头的 `<think>`，这是因为 Qwen3/DeepSeek 系的 chat template 会把 `<think>` 预填进 prompt，模型续写只吐出闭合标签。框架的自动剥离逻辑要求标签成对，所以这种情况不会被剥离，思考内容会留在输出里干扰答案提取。建议按以下任一方式处理（推荐第一种）：

1. **在推理服务侧开启 reasoning parser**：sglang 启动时加 `--reasoning-parser`（取值见 sglang 文档）。这样思考内容会通过独立的 `reasoning_content` 字段返回，框架会自动识别，`prediction` 里不再包含思考过程。
2. **配置过滤器**：`--dataset-args '{"gpqa_diamond": {"filters": {"remove_until": "</think>"}}}'`
3. **用裁判模型兜底**：设置 `judge_strategy=llm_recall` 并提供 `judge_model_args`，规则提取失败的样本会交给裁判模型重新判定（仅在规则得分不满分时才调用，不会带来全量开销）。我们实测过您这条样本：规则判定 acc=0.0，`llm_recall` 下 acc=1.0。

**还未修复的部分**（如遇到可以再开 issue）：当输出里完全没有规范的 `ANSWER:` 行时，兜底逻辑会扫描全文取最后一个大写字母，且不校验它是否属于合法选项，例如 `ANSWER: [B] because XYZ` 会得到 `Z`。这一项需要单独评估对存量分数的影响，本次没有一起改。

