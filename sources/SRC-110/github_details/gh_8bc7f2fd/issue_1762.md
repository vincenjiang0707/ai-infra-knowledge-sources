# [Issue #1762] 是否接入jev类选择模型

source: https://github.com/modelscope/evalscope/issues/1762
state: open | updated: 2026-09-22T12:03:57Z
labels: enhancement

## 正文

## 功能描述 / Feature Description
希望 EvalScope 支持接入 TypeSafe 的 Jev 模型，并将其作为评测执行模型，用于 MMLU、CMMLU、C-Eval 等多项选择类评测集。

## 需求背景 / Background

传统选择题评测通常依赖模型生成文本，再从文本中解析 A/B/C/D 等答案。这种方式可能受到额外解释文本、输出格式和答案解析规则的影响。
根据 TypeSafe 官方介绍，Jev 的 Choice 原语可以直接返回选项、概率分布和 confidence，无需先生成自然语言再解析结果。这一能力与 MMLU 等选择类评测任务非常匹配：
- 减少答案文本解析带来的不确定性；
- 直接获得结构化的选项结果；
- 可以保留概率和 confidence 信息；
- 适合作为 EvalScope 中的独立评测执行模型。

## 预期行为 / Expected Behavior
希望支持类似以下命令：
export TYPESAFE_API_KEY=your_api_key

evalscope eval \
  --model jev-latest \
  --eval-type jev_api \
  --datasets mmlu \
  --limit 5
具体期望包括：
1. 新增 Jev 模型 API 适配器，并接入 EvalScope 现有的模型注册机制。
2. 支持通过 TYPESAFE_API_KEY 配置认证信息。
3. 将评测样本中的题目、选项和必要上下文转换为 Jev API 所需的 state。
4. 使用 Jev 的 Choice 能力完成多项选择题评测。
5. 将 Jev 返回的选择结果转换为 EvalScope 统一的模型输出格式，例如 A、B、C、D。
6. 保留 Jev 返回的概率分布和 confidence，便于结果分析。
7. 兼容 EvalScope 现有的并发、超时、重试、缓存和评测报告机制。
8. 对不适用于 Jev 的传统生成参数进行明确说明，或安全忽略。
9. 增加单元测试和至少一个选择类 benchmark 的 smoke test。
10. 补充使用文档，说明模型配置、API Key、支持的 benchmark 以及限制条件。

## 其他信息 / Additional Information

Jev 官方介绍：https://docs.typesafe.ai/introduction

## 评论 (1)

### IRONICBo · 2026-09-22

One implementation detail worth preserving: do not collapse the Jev result to only `A/B/C/D` at the adapter boundary. Store the selected option, full distribution, confidence, question-spec hash, and model version; then report accuracy together with calibration (Brier/ECE), abstention behavior, and request failures.

The cache key should include the ordered choices and the full question specification, not just the prompt text. We hit the same boundary in Jev Social: route confidence describes the decision itself, while downstream browser execution success is a separate outcome and should never be inferred from that confidence.

