# [Issue #1699] hi，感谢开源工具，请问是否支持自定metric，有些bench不想用acc，例如extract_match等

source: https://github.com/modelscope/evalscope/issues/1699
state: closed | updated: 2026-09-07T07:44:49Z
labels: 

## 正文

(empty)

## 评论 (1)

### Yunnglin · 2026-09-07

感谢关注！EvalScope 支持自定义 metric：可以继承 `Metric` 并通过 `@register_metric` 注册，然后在对应 benchmark 的 `BenchmarkMeta.metric_list` 中配置使用。

不过目前标准 benchmark 的 metric 由其 adapter 定义，暂不支持通过 CLI / `TaskConfig` 直接将 `acc` 动态替换为 `extract_match`。如果您的场景需要从模型输出中提取特定字段后再匹配，可以实现并注册一个 `extract_match` metric，并在自定义 benchmark adapter 中替换默认的 `metric_list`。

可参考现有的 `exact_match` 实现：`evalscope/metrics/nlp/metrics.py`。如果方便的话，也欢迎补充具体 benchmark、输入输出样例和期望的提取规则，我们可以进一步评估是否适合作为通用能力支持。
