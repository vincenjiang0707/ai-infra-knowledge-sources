# [Issue #1634] Early Stopping / Equal Issue mode into Policy for 4.1

source: https://github.com/mlcommons/inference/issues/1634
state: closed | updated: 2026-05-07T00:39:59Z
labels: Stale

## 正文

There was a discussion on how to make Early Stopping more user friendly in https://github.com/mlcommons/inference/issues/1095 

This issue was closed without being added into real policy and implementation though. And in order to get there, we need opinions from the statistics expert like @ckstanton.

Today, we use Equal Issue mode for a couple of different reasons:
- Early Stopping used in SingleStream/MultiStream where it has to estimate the true latency distribution from samples, could trip the decision in rather unexpected way. This was manifested when the benchmark has non-uniform workload samples (either sample size is different or the work required to process a sample may different to the other sample). Most of those cases were due to number of samples the test ran is not large enough. By the law of large number, everything becomes more reliable as we run near infinite number of samples. But we all want short run, for our convenience. Equal Issue mode helped as we controlled number of samples to minimal, while making samples in the entire set visited equally likely.
- Offline (Early Stopping is either not used) or Server (Early Stopping is legal regardless of non-uniformaty by running on the binomial process) scenarios. In these cases, we want the overall performance metrics (offline QPS, server QPS, TPS, TPOT, TTFT etc) to be less variable. Overall reasoning why Equal Issue mode helps is indeed the same as above - it helps capturing the metrics upon entire sample set.

In short, I think equal issue mode should be enabled for all the scenarios if the benchmark handles non-uniform workload samples; it prohibits metrics from being suffered by the high variance upon random seeds, without running the test extensively long. We would need extensive discussions on this matter, especially in the connection to Early Stopping. We may want to revisit the above issue https://github.com/mlcommons/inference/issues/1095 and discuss how to make ES more user friendly as well.

There is a concern that Equal Issue mode enforces users to run test very long. We also want to attack this problem, but in the way the solution is legit for metrics to capture the behaviors of the networks on input datasets, and it may involve separate discussions like reducing the input sample set size.

FWIW There's also a concern about Early Stopping on Token Latency: https://github.com/mlcommons/inference/pull/1596#issuecomment-1920237469

## 评论 (4)

### nv-jinhosuh · 2024-02-20

@ashwin @nvzhihanj @arjunsuresh @psyhtest @ckstanton @pgmpablo157321 FYI

### arjunsuresh · 2024-02-20

Thank you @nv-jinhosuh for bringing up this discussion. It is clear why we need equal issue mode. Other than longer runtime -- it is not terrible as the accuracy run takes the same time anyway, we haven't seen any issue with it. But someone not familiar with equal issue mode can be surprised by seeing strange `min_query_count` values in the mlperf_log. I believe all we need is good documentation and rule for equal issue mode so that everyone is aware of it. 

We were using `max_duration` for singlestream runs and equal issue mode means this no longer can be done. This is not a major issue as anyway for offline scenario we cannot use max_duration. 

### arjunsuresh · 2024-03-07

I would like to add another related point here for discussion - can submitters override the `min_query_count` parameter? It would be good to document what all parameters the submitters can override and what all need to be controlled solely by loadgen. 

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
