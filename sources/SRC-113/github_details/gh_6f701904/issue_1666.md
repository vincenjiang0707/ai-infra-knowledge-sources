# [Issue #1666] Specified provider 'CUDAExecutionProvider' is not in available provider names.Available providers: 'AzureExecutionProvider, CPUExecutionProvider'

source: https://github.com/mlcommons/inference/issues/1666
state: closed | updated: 2026-05-05T00:38:37Z
labels: Stale

## 正文

when I run
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios --model=bert-99 --implementation=reference --device=cuda --backend=onnxruntime --category=edge --division=open --quiet
the error is
/home/zhaohc/cm/lib/python3.10/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py:69: UserWarning: Specified provider 'CUDAExecutionProvider' is not in available provider names.Available providers: 'AzureExecutionProvider, CPUExecutionProvider'
  warnings.warn(
2024-03-23 12:50:23.216456985 [W:onnxruntime:, graph.cc:3593 CleanUnusedInitializersAndNodeArgs] Removing initializer 'bert.pooler.dense.bias'. It is not used by any node and should be removed from the model.
2024-03-23 12:50:23.216514497 [W:onnxruntime:, graph.cc:3593 CleanUnusedInitializersAndNodeArgs] Removing initializer 'bert.pooler.dense.weight'. It is not used by any node and should be removed from the model.
the result is
zhaohc710-reference-gpu-onnxruntime-v1.17.1-default_config
+---------+--------------+----------+-------+-----------------+---------------------------------+
|  Model  |   Scenario   | Accuracy |  QPS  | Latency (in ms) | Power Efficiency (in samples/J) |
+---------+--------------+----------+-------+-----------------+---------------------------------+
| bert-99 | SingleStream |    -     |   -   |      X 0.0      |                                 |
| bert-99 |   Offline    |    -     | 2.657 |        -        |                                 |
+---------+--------------+----------+-------+-----------------+---------------------------------+

## 评论 (4)

### psyhtest · 2024-03-22

Can you be more specific please?

### KingICCrab · 2024-03-23

================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : SingleStream
Mode     : PerformanceOnly
90th percentile latency (ns) : 700060891
Result is : INVALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: NO
Recommendations:
Early Stopping Result:
 * Only processed 10 queries.
 * Need to process at least 64 queries for early stopping.

================================================
Additional Stats
================================================
QPS w/ loadgen overhead         : 1.57
QPS w/o loadgen overhead        : 1.57

Min latency (ns)                : 597931992
Max latency (ns)                : 700060891
Mean latency (ns)               : 635649808
50.00 percentile latency (ns)   : 632335750
90.00 percentile latency (ns)   : 700060891
95.00 percentile latency (ns)   : 700060891
97.00 percentile latency (ns)   : 700060891
99.00 percentile latency (ns)   : 700060891
99.90 percentile latency (ns)   : 700060891

================================================
Test Parameters Used
================================================
samples_per_query : 1
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 0
max_duration (ms): 0
min_query_count : 10
max_query_count : 10
qsl_rng_seed : 13281865557512327830
sample_index_rng_seed : 198141574272810017
schedule_rng_seed : 7575108116881280410
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 10833

No warnings encountered during test.

No errors encountered during test.

### arjunsuresh · 2024-04-11

If the installed software stack (cuda version, onnxruntime version and cudnn version) is not supported for CUDA execution, then cuda execution provider won't work and execution happens on the CPU. It would be nice if CM can detect this and fail nicely - but this is not there at the moment. To make the code run, we can change the version of the dependencies by adding `--adr.onnxruntime.version=1.16.3` to the run command or change the cuda runtime version like `--adr.cuda.version=11.8`. 

### github-actions[bot] · 2026-05-05

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
