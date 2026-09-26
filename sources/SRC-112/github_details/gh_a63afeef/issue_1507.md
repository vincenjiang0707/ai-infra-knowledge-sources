# [Issue #1507] Inference engine startup included in GPU metric capture / 推理引擎启动阶段被纳入 GPU 指标采集

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1507
state: open | updated: 2026-07-04T05:17:42Z
labels: 

## 正文

**Describe the bug**
Current scripts in the benchmarks/single_node directory (e.g., https://github.com/SemiAnalysisAI/InferenceX/blob/adbaae52ddf2569ddf2e793f5ad0a56f2f2a4d13/benchmarks/single_node/qwen3.5_fp8_mi325x.sh) follow this pattern to establish GPU monitoring for every InferenceX benchmark run:

1) start_gpu_monitor
2) Start LLM inference engine as a background process (e.g. SGLang, vLLM)
3) wait_for_server_ready
4) Run benchmark for the model (key result to report for InferenceX benchmark)
5) stop_gpu_monitor

As-is, the GPU energy consumption and other metrics can be skewed by irregularities in LLM inference engine startup (compilation, kernel autotuning, etc) and the 5-second sleeps used while waiting for the server to start (waiting on the /health route). While cross-referencing other logs can identify some timestamps that fall outside of the actual benchmark window, there is no direct correspondence within the CSV itself.

**Expected behavior**
Monitoring data should only correspond to the benchmark execution window. Alternatively, providing a way to identify which portion of the data corresponds to benchmark execution would also be acceptable.

**Potential solutions**
Adding a marker in the `gpu_metrics.csv` or delaying the `start_gpu_monitor` calls until the benchmark is ready to run (moving step 1 above to just before step 4) can assist in disambiguating the results.

**Additional context**
The startup costs of pinned versions of vLLM (likely similar for other engines) should be relatively consistent for a GitHub action runner, but the inference engine's startup performance can change over successive versions. The ability to separate startup costs from the benchmark data is important.

## 中文说明
当前基准测试脚本在推理引擎启动之前就开始 GPU 监控（`start_gpu_monitor`），导致 `gpu_metrics.csv` 中包含引擎启动阶段（编译、内核自动调优、等待 /health 路由的休眠等）的能耗和指标数据，这会影响基准测试指标的准确性。建议将 GPU 监控延迟到基准测试实际运行前启动，或在 CSV 中添加标记以区分启动阶段和基准测试执行窗口的数据。


## 评论 (2)

### functionstackx · 2026-05-19

hi @thomas-primalabs currently gpu metrics `PowerX` is in an WIP feature and not promoted to production dashboard yet. your current that we need to have an marker after warmup or something. if u would like to contribute something like this, help to coordinate. what is ur email

### thomas-primalabs · 2026-05-19

Hi @functionstackx. We can certainly work together and make a proper PR, depending on what works best for InferenceX. You can reach me for private discussion at thomas@primalabs.ai
