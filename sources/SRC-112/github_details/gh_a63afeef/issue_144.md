# [Issue #144] MVP graph of realized_model_tflop/s/gpu & MFU / 已实现模型 TFLOP/s/GPU 和 MFU 的 MVP 图表

source: https://github.com/SemiAnalysisAI/InferenceX/issues/144
state: open | updated: 2026-07-04T05:07:42Z
labels: p0, p1, frontend

## 正文

create these 2 graphs y-selector behind an feature flag (while we calcuate the properly formula with attention flops)
- Model TFLOP/s vs Interactivity
- MFU (percentage) vs Interactivity
- Model TFLOP/s vs e2e Latency
- MFU (percentage) vs e2e Latency


realized_model_tflops = 2 * N * tok/s/gpu

where N is num of active params

num of active params for 
llama = 70 billion params
gptoss = 5.1B active params
deepseek = 37B active params

MFU = realized_model_tflops / theortical_tflops

theortical_tflops dense is
h100 fp8 = 1,979 TFLOP/s
h200 fp8 = 1,979 TFLOP/s
b200 fp8 = 4,500 TFLOP/s
b200 fp4 = 9.000 TFLOP/s
b300 fp8 = 4,500 TFLOP/s
b300 fp4 = 13,500 TFLOP/s
gb200 fp8 = 5,000TFLOP/s
gb200 fp4 = 10,000TFLOP/s
gb300 fp8 = 5,000TFLOP/s
gb300 fp4 = 15,000TFLOP/s

mi300 fp8 = 2,615 TFLOP/s
mi325 fp8 = 2,615 TFLOP/s
mi355 fp8 = 5,033 TFLOP/s
mi355 fp4 = 10,066 TFLOP/s

## 中文说明
跟踪所有集群上的软件版本 (BKC)。


## 评论 (1)

### cquil11 · 2025-10-24

"p3" 🤣 
