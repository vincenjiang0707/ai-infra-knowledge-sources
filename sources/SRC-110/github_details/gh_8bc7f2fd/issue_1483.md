# [Issue #1483] [Feature] 希望性能测试时支持真实数据集的定长定长输入/输出功能

source: https://github.com/modelscope/evalscope/issues/1483
state: closed | updated: 2026-07-24T07:11:33Z
labels: enhancement

## 正文

## 功能描述 / Feature Description

希望 EvalScope 的 `Perf` 模块能够在支持自定义真实数据集（如 ShareGPT）的基础上，**原生增加工具侧的“定长 I/O 控制参数”（Input Padding/Truncation & Output ignore_eos）** 。以便用户能够在保留真实业务语义的前提下，进行严格的控制变量压测。

## 需求背景 / Background

在真实的 LLM 生产环境中，单纯使用 Random 合成数据集进行压测，在某些情况，如MTP中，不能检验出真实的吞吐提升。引入真实数据集进行压测至关重要，原因如下：

1. **Prefill 阶段与 Prefix Caching 收益评估**：
2. Random 数据的 Token 毫无重复，导致前缀缓存（Prefix Caching / RadixAttention）命中率几乎为 0；而真实数据包含大量重复的 System Prompt，能极大加速 TTFT。缺乏真实数据支持，无法评估引擎缓存优化的真实收益。
3. **MTP (Multi-Token Prediction) 与投机解码 (Speculative Decoding) 的失效**：MTP 和投机解码的核心收益依赖于 Draft Model 对 Target Model 输出的接受率 (Acceptance Rate)。真实人类语言具有强烈的统计学规律和语义连贯性（低熵），Draft Model 预测准确率高，加速比明显；而 Random 数据集的 Token 序列熵极高且毫无逻辑，Draft Model 根本无法预测，导致接受率趋近于 0。使用 Random 数据不仅测不出 MTP 的加速收益，反而会因为额外的 Draft 计算导致性能下降，产生严重的误判。

## 预期行为 / Expected Behavior

期望 `Perf` 模块在 CLI 参数或 `Arguments` 中增加以下控制能力：

1. **输入侧定长控制 (Input Length Override)**：
   新增类似 `--target-input-len` 的参数。当加载真实文本数据集时，工具能在底层调用 Tokenizer，自动对 Prompt 进行精确的截断（Truncation）或填充（Padding），使其严格对齐到目标 Token 长度，以便测试特定上下文长度下的 Prefill 性能。



非常期待官方团队的评估与反馈，感谢！

## 评论 (2)

### Yunnglin · 2026-07-16

Hi @AiKiAi-stack，感谢建议，输入侧定长功能已实现并合并（#1495）。

用法（单轮真实文本数据集 `openqa`/`longalpaca`/`line_by_line`/单轮 `share_gpt`，需配 `--tokenizer-path`）：

```bash
evalscope perf --model qwen2.5 --url http://127.0.0.1:8000/v1/chat/completions \
  --dataset share_gpt_zh --tokenizer-path /path/to/tokenizer \
  --dataset-args '{"target_input_len": 2048, "input_len_mode": "cap"}'
```

`cap`：超长截断、短的保留；`drop`：超长截断、短的丢弃（每条恰好定长）。

未做 padding：补齐会注入人造 token，反而破坏你关注的 MTP/Prefix-Cache 真实性；需严格统一定长可用 `random` 数据集设 `--min-prompt-length == --max-prompt-length`。输出侧 `ignore_eos`/`max_tokens` 框架已支持，可组合使用。文档已更新，欢迎试用！

### AiKiAi-stack · 2026-07-24

感谢 @Yunnglin 和官方团队的快速响应！我已经试用了 `cap` 和 `drop` 模式，非常实用。我也完全认同官方关于“不做 Padding”的设计思路

但我之所以依然希望加入“拼接”的能力，是因为在实际压测中有一个测试痛点：**缺乏超长上下文（128K/256K）的真实数据**。
目前开源的真实指令集（如 LongAlpaca）大多集中在 4K-8K，当我们想测 128K 的 Prefill 性能时：
1. 用 `drop` 模式：根本没有足够的 128K 原生样本，数据集会被大量过滤。
2. 用 `cap` 模式：短文本被原样保留，导致长短不一，且依然测不出模型在 128K 下的真实性能瓶颈。
3. 用 `random` 模式：虽然能严格定长，但失去了真实业务的低熵特征，测不出 MTP 的真实收益。

因此，我想把这个需求转化为一个 **Feature Request**：能否在 EvalScope 的**数据预处理/加载阶段（提前）**，支持一种 **“长上下文前缀注入 ”** 机制？

**具体设想：**
允许用户通过参数（如 `--long-prefix-file`）指定一个真实的超长文本（如一本书或长财报）。在加载短 prompt 数据集时，框架在底层**提前**将这段真实长文本作为 `System Prompt`（或前缀）与短 `User Prompt` 拼接，并截断/对齐到目标长度（如 128K）。

**这样做的优势：**
1. **保持真实性**：注入的依然是真实的自然语言 Token，保持了低熵特征，完美满足 MTP 和 Prefix-Cache 的测试要求，比 Padding 和 Random 更贴近真实的 RAG/长文档问答业务。
2. **解决数据荒**：让用户无需自己写复杂的离线脚本，就能轻松构造出 128K/256K 的定长压测集。

希望官方能评估一下该需求是否有必要在框架层面原生支持，我个人认为这对长文本压测场景非常有帮助。当然，如果能通过其他更优雅的形式或配置来实现这个目标也非常欢迎！再次感谢团队的努力！
