# [Issue #1397] max_duration_ms setting does not work in Offline scenario

source: https://github.com/mlcommons/inference/issues/1397
state: closed | updated: 2026-05-13T00:44:08Z
labels: Stale

## 正文

I wanted to use the `TestSettings.max_duration_ms` to stop a bechmark run when it takes too long to finish. (see PR https://github.com/mlcommons/mobile_app_open/pull/718)

The setting works as expected in the `SingleStream` but not in the `Offline` scenario. In the `Offline` scenario, the benchmark does not stop and the result is valid.

Is this behavior expected? Or is it a bug?

<details>
<summary>Log for SingleStream scenario</summary>
 
```
================================================
MLPerf Results Summary
================================================
SUT name : TFLite
Scenario : SingleStream
Mode     : PerformanceOnly
90th percentile latency (ns) : 16271459
Result is : INVALID
  Min duration satisfied : Yes
  Min queries satisfied : NO
  Early stopping satisfied: NO
Recommendations:
 * The test exited early, before enough queries were issued.
   See the detailed log for why this may have occurred.
Early Stopping Result:
 * Only processed 58 queries.
 * Need to process at least 64 queries for early stopping.

================================================
Additional Stats
================================================
QPS w/ loadgen overhead         : 62.30
QPS w/o loadgen overhead        : 62.36

Min latency (ns)                : 14380417
Max latency (ns)                : 35529416
Mean latency (ns)               : 16035073
50.00 percentile latency (ns)   : 15707375
90.00 percentile latency (ns)   : 16271459
95.00 percentile latency (ns)   : 18694292
97.00 percentile latency (ns)   : 19629375
99.00 percentile latency (ns)   : 35529416
99.90 percentile latency (ns)   : 35529416

================================================
Test Parameters Used
================================================
samples_per_query : 1
target_qps : 1000
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 100
max_duration (ms): 900
min_query_count : 100
max_query_count : 0
qsl_rng_seed : 10003631887983097364
sample_index_rng_seed : 17183018601990103738
schedule_rng_seed : 12134888396634371638
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 830

No warnings encountered during test.

1 ERROR encountered. See detailed log.
2023-06-15 12:05:54.124221: I flutter/cpp/binary/main.cc:407] Accuracy: 65.38%

Process finished with exit code 0
```
</details>


<details>
<summary>Log for Offline scenario</summary>
 
```
================================================
MLPerf Results Summary
================================================
SUT name : TFLite
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 105.135
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 951158708
Max latency (ns)                : 951158708
Mean latency (ns)               : 951158708
50.00 percentile latency (ns)   : 951158708
90.00 percentile latency (ns)   : 951158708
95.00 percentile latency (ns)   : 951158708
97.00 percentile latency (ns)   : 951158708
99.00 percentile latency (ns)   : 951158708
99.90 percentile latency (ns)   : 951158708

================================================
Test Parameters Used
================================================
samples_per_query : 100
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 100
max_duration (ms): 900
min_query_count : 1
max_query_count : 0
qsl_rng_seed : 10003631887983097364
sample_index_rng_seed : 17183018601990103738
schedule_rng_seed : 12134888396634371638
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 830

No warnings encountered during test.

No errors encountered during test.

Process finished with exit code 0
```

</details>

The `loadgen` version used is defined here:
https://github.com/mlcommons/mobile_app_open/blob/4d82d1c186823e38a82867cc4f0116d6bfb1ea8f/WORKSPACE#L118-L129

If you need any other information. Please let me know. Thanks.

## 评论 (9)

### anhappdev · 2023-06-20

Testing with the latest release (`v3.0`) gave me the same result. `max_duration_ms` setting does not work in Offline scenario.

### arjunsuresh · 2023-06-21

The variable usages are a bit confusing in the loadgen code and so I do not have a full understanding of what's happening. But I believe this is the expected behavior as can be seen [here](https://github.com/mlcommons/inference/blob/master/loadgen/issue_query_controller.cc#L516). In the offline scenario, there is only a single query and all samples are part of it (but at some places in the code, samples are considered as queries). Probably this is why `max_duration` has no effect in the Offline scenario like `max_query_count`.

But, say you want to enforce max_duration=100000 ms = 100s, a way to do this will be to change the target_qps because in the Offline scenario the number of queries is approximately target_qps * 1.1 * min_duration_in_seconds and **all of these always get executed.**

I see that, you are using the default (also minimum) target_qps of 1, so the way to enforce the max_duration will be to use min_duration setting. 

But if you want to do this transparently for any device without knowing its performance ahead, I don't think it is possible as of now. What we do is run a small test run, get the performance of the system, and then use that value for further runs. 

### anhappdev · 2023-06-22

@arjunsuresh Thank you for the information. I will look into the workaround you suggested.
I see there is a `AbortTest()` in loadgen. Do you think this function will work in an Offline scenario?

### arjunsuresh · 2023-06-22

You're welcome. AbortTest() should be working. Just that on a benchmarking system it cannot be used with a timer as then it can interfere with the performance results in Offline/Server scenarios.

### anhappdev · 2023-06-29

> Just that on a benchmarking system it cannot be used with a timer as then it can interfere with the performance results in Offline/Server scenarios.

Can you explain this a bit more? Since the `max_duration` did not work in the Offline scenario, I want to try with `AbortTest()`, but `AbortTest()` should not be used in the Offline scenario?

BTW, does it make sense to update/fix `loadgen` to make the `max_duration` work in the Offline scenario? IMO, `max_duration` should work in any scenarios, right?

### arjunsuresh · 2023-06-29

You can use AbortTest - but checking the test duration using "time" function call cannot be done during a benchmark run. Probably a timeout option [like this](https://stackoverflow.com/a/12698328) can be used.

In singlestream and multistream - a query has 1 or 8 samples. Before issuing the next query loadgen can do any operations as they won't get timed as part of the benchmark run. But in the case of offline scenario, only a single query is there containing all the samples. So, there is no free time for loadgen to call the time function and check the max_duration.  

### anhappdev · 2023-07-10

Thank you for the explanation. We will try to implement the `AbortTest()` function. I will close this issue.

### anhappdev · 2023-07-25

We did try to implement `AbortTest()` (tracked in https://github.com/mlcommons/mobile_app_open/issues/749) but it did not work as expected. When calling `AbortTest()`, the app just hangs forever and `StartTest()` never finished.

For reference, the implementation can be reviewed here:
https://github.com/mlcommons/mobile_app_open/compare/master...749/abort-running-benchmark

Can someone take a look if `AbortTest()` ever worked? I can only find a test for `StartTest()` but not `AbortTest()`.

https://github.com/mlcommons/inference/blob/fd6486a0483de3175c67bdd84576eb5f4f406be7/loadgen/tests/basic.cc#L94-L101

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
