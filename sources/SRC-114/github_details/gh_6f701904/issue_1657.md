# [Issue #1657] Units in the summary file for llama offline results are wrong

source: https://github.com/mlcommons/inference/issues/1657
state: closed | updated: 2026-05-06T00:40:57Z
labels: Stale

## 正文

For llama benchmarks, the submission checker uses tokens per second for Offline, but samples per second for Server. https://github.com/mlcommons/inference/blob/master/tools/submission/submission_checker.py#L1385

However, the summary.csv still [use](https://github.com/mlcommons/inference/blob/master/tools/submission/submission_checker.py#L2543-L2544) samples/second as the header to report Offline results for all models. This can cause confusion and mislead readers since the units here are wrong. Orders of magnitude different between offline and server.

Should this be changed to tokens/sec just for llama? Thanks

## 评论 (3)

### yeandy · 2024-02-29

For example, if mlperf_log_summary.txt reports 1 sample/sec and 100 tokens/sec for Server, and reports 1.1 sample/sec and 110 tokens/sec for Offline, the submission checker will produce summary.csv with:

- Server (queries/s): 1
- Offline (samples/s): 110

### swasson488 · 2024-03-07

-Benchmark comprehensibility is crucial to MLCommons' success. We have to explain and justify the results and metrics to a broader audience than just ML experts. We will engage with the press, who will write up the results for their readership. Also, MLPerf results are often used for marketing purposes. Both of these channels engage a wider audience of interested parties seeking to understand the results.

-Token/s is widely used and understood in the industry for LLM performance characterization beyond MLPerf. Reporting results in that metric makes the outcome more readily understandable to more people.

-Reporting one set of results in tokens/s and another related set in samples/s will likely lead to confusion on the part of many observers. 

-The initial rationale for using different metrics for Offline and Server has been eroded with the move to reporting completed rather than scheduled work. Per Zhihan Jiang: 

"In v4.0, we used different metrics for Offline and Server because Server used  "scheduled samples per second” initially which could not be directly converted to “token per second” (you don’t know the token/sample ahead of time in loadgen). 

But later we applied “result samples per second” for Llama2 (and this round for all the benchmarks), I second that we should use “results token per second” for server to align with Offline."

-There has been some discussion of sticking with the current plan for 4.0 and then changing the metrics later in 4.1. However, the Llama 2 benchmark is brand new. Any change made later will compromise comparability with this round's results. We would be better off making a change now and avoiding further complications down the road.

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
