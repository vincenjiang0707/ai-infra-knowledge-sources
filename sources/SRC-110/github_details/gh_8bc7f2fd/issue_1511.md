# [Issue #1511] [需求] 模型性能压测支持延迟类指标的 min 统计（TTFT / TPOT / ITL / Latency）

source: https://github.com/modelscope/evalscope/issues/1511
state: closed | updated: 2026-07-24T10:20:59Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题


## 需求描述
当前 EvalScope 已支持对基于 OpenAI API 的模型服务进行推理性能评测，输出延迟与吞吐等指标，包括：

1. Summary：平均延迟类指标（如 avg_ttft、avg_tpot、avg_latency）
2. Percentile：1% / 5% / … / 99% / max

在实际性能分析中，除了均值、分位和最大值外，最小值（min） 同样重要，例如：
1. 评估服务在理想/低负载条件下的最佳延迟表现（best-case）
2. 与 max、p99 对照，观察延迟分布跨度
2. 排查异常偏高的均值是否由少数慢请求拉高，还是整体水位偏高

## 建议方案
1. 在百分位结果（benchmark_percentile.json / 控制台表）中增加 min 行（即P0百分位），覆盖 TTFT、TPOT、ITL、Latency 等延迟指标

感谢支持！

## 评论 (4)

### balala21 · 2026-07-24

另外就是最新的evalscope v1.9.1 的控制台打印结果不如之前的清晰了，延迟这边几个指标前面都没有显式打印是最大最小还是平均了，之前的打印字段不管是命名还是类别好像更规范一些
这是之前的
<img width="364" height="547" alt="Image" src="https://github.com/user-attachments/assets/d9616505-7b3a-441e-9777-1f883a99cf00" />
这是现在的
<img width="479" height="522" alt="Image" src="https://github.com/user-attachments/assets/a3c107d1-7a67-4a24-b3cc-74e482b718d5" />

### Yunnglin · 2026-07-24

已在 #1517 支持并合并到 main 🎉

**1. 延迟指标新增 min（P0）**
`benchmark_percentile.json` 与控制台的 Percentile 表新增了 `min` 列（位于最左，与 `max` 对称），覆盖 TTFT / TPOT / ITL / Latency 及吞吐、token 数等全部指标，方便查看 best-case 延迟与分布跨度：

```
┌────────────────┬────────┬────────┬─── … ───┬────────┐
│ Metric         │    min │     1% │   …     │    max │
├────────────────┼────────┼────────┼─── … ───┼────────┤
│ Avg TTFT (ms)  │ 366.48 │ 366.48 │   …     │ 638.76 │
│ Avg TPOT (ms)  │  15.06 │  15.06 │   …     │  21.79 │
└────────────────┴────────┴────────┴─── … ───┴────────┘
```

**2. Summary 表指标语义更清晰**
针对你反馈的「延迟指标没标是 avg 还是 max/min」的问题，Summary 表中所有均值类指标已统一加上 `Avg` 前缀：`TTFT/TPOT/ITL (ms)` → `Avg TTFT/TPOT/ITL (ms)`，多轮的 First/Subsequent-Turn TTFT、Decoded Tok/Iter 同理；吞吐、缓存命中率等非均值指标保持不变。

请拉取最新 main 后试用，如有问题欢迎继续反馈～


### balala21 · 2026-07-24

已验证，非常感谢~


### balala21 · 2026-07-24

不过，我有一个疑问，就是我发4个请求，25%就是只有1个请求比他小，为什么25%z之前的ITL分数有差异呢？

测试指令为：
`Evalscope perf --model /data/models_zoo/Meta-Llama-3-8B-Instruct  --url ”" --api-key "EMPTY" --parallel 1 --number 4 --dataset random --tokenizer-path "/data/models_zoo/Meta-Llama-3-8B-Instruct" --min-prompt-length 2048 --
max-prompt-length 2048 --min-tokens 1024 --max-tokens 1024 --extra-args '{"ignore_eos": true}'  --warmup-num 1`

<img width="2090" height="673" alt="Image" src="https://github.com/user-attachments/assets/363ff5b6-cfff-4f76-9c7b-87a968309dae" />
