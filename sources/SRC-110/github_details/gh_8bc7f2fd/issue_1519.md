# [Issue #1519] 性能评测结果表增加 I/O token 标注列，提升同模型不同配置下延迟差异的可解释性

source: https://github.com/modelscope/evalscope/issues/1519
state: closed | updated: 2026-07-28T02:21:11Z
labels: enhancement

## 正文

# 功能描述 / Feature Description

在性能评测（Perf）Web UI 的结果列表表格中，增加一列 I→O tok（输入 token 数 → 输出 token 数），用于展示每次测试的输入输出 token 配置。

## 需求背景 / Background

当前性能评测结果表中，同一模型、相同并发配置下，如果输入 token 数量不同，最低延迟会有明显差异。但缺少 I/O token 标注列，用户无法直观理解为什么延迟不同。

示例：
如下面的图
<img width="1300" height="508" alt="Image" src="https://github.com/user-attachments/assets/11a4365f-696f-4aec-bb04-17cb8baaae99" />
- dogress-DeepSeek-V4-Flash，最低延迟 9.30s
- dogress-DeepSeek-V4-Flash，最低延迟 3.62s
- dogress-DeepSeek-V4-Flash，最低延迟 4.20s
三行都是同一模型、同样并发（1,4,8,16），但延迟从 3.62s 到 9.30s 不等。没有 token 信息时，用户会困惑甚至误判模型性能。

## 预期行为 / Expected Behavior
<img width="1323" height="502" alt="Image" src="https://github.com/user-attachments/assets/5d0fe37c-011a-48cc-8885-cc01a59a4fb6" />
在性能评测结果表格中增加 I→O tok 列，显示格式如 `30000→100t`。

这样用户可以一眼看出：

1. 第一行延迟高是因为输入 token 多（30000t vs 10000t）
2. 第二行和第三行输入相同，但输出 token 不同（100t vs 300t），延迟也有差异

提升结果的可读性和可解释性，避免用户误判。

## 其他信息 / Additional Information

如果这个建议被采纳，我可以提交 PR 来实现该功能。


## 评论 (1)

### Yunnglin · 2026-07-28

Thanks for the detailed proposal and the offer to contribute a PR!

Since this change touched shared backend/frontend code that we were already
working on for #1521, we went ahead and implemented it directly in #1526:

- `GET /api/v1/perf/list` now returns `avg_input_tokens` / `avg_output_tokens`
  (succeed-request-weighted averages of the measured values, which stay
  accurate even when the configured token counts are ranges or unset);
- the performance list shows a new `I→O tok` column rendered as `30000→100t`,
  on both the desktop table and the mobile card view.

This will be closed automatically once #1526 is merged. Feedback on the PR is
very welcome — and sorry for taking this one off your hands; contributions are
always appreciated!

