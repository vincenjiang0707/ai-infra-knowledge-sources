# [Issue #1630] Setting `min_query_count` for GPTJ

source: https://github.com/mlcommons/inference/issues/1630
state: closed | updated: 2026-05-07T00:40:03Z
labels: inference v4.0, Stale

## 正文

Running GPTJ even on accelerated systems can be quite demanding, as the Server latency constraint of 20 seconds suggests. For systems close to this threshold, meeting the minimum run duration of 10 minutes would require processing just over 30 samples.

However, when trying to set `min_query_count` in `user.conf` (or indeed in `mlperf.conf` proper) e.g.:
<pre>
gptj.SingleStream.min_query_count = 100
gptj.SingleStream.max_query_count = 100
gptj.SingleStream.performance_sample_count_override = 13368
gptj.SingleStream.target_latency = 19000
</pre>
I still see in `mlperf_log_summary.txt`:
<pre>
min_query_count : 13368
max_query_count : 100
</pre>
with the following experiment summary:
<pre>
================================================
MLPerf Results Summary
================================================
SUT name : KILT_SERVER
Scenario : SingleStream
Mode     : PerformanceOnly
90th percentile latency (ns) : xxxxxxxxxx
Result is : INVALID
  Min duration satisfied : Yes
  Min queries satisfied : NO
  Early stopping satisfied: Yes
Recommendations:
 * The test exited early, before enough queries were issued.
   See the detailed log for why this may have occurred.
Early Stopping Result:
 * Processed at least 64 queries (100).
 * Would discard 2 highest latency queries.
 * Early stopping 90th percentile estimate: yyyyyyyyyy
 * Not enough queries processed for 99th percentile
 early stopping estimate (would need to process at
 least 662 total queries).
</pre>

Is there any reason why LoadGen enforces this? I know that we agreed that the minimum number of queries for Offline should cover the whole dataset, e.g. `min_query_count == performance_sample_count_override == 13368` for GPTJ. It may be OK for Offline and Server, but for GPTJ SingleStream at 20 seconds per sample we would be looking at over 3 days (and double that for a power run!)

@mrmhodak @pgmpablo157321 

## 评论 (14)

### arjunsuresh · 2024-02-20

yes. This was discussed in the inference WG when Nvidia proposed the equal issue mode for GPTJ amd LLAMA2.  But for power runs, just a 5 minute ranging run is enough as we had demonstrated in the v3.1 round.

### psyhtest · 2024-02-20

> This was discussed in the inference WG when Nvidia proposed the equal issue mode for GPTJ amd LLAMA2.

Is there anything in the rules on this?

> But for power runs, just a 5 minute ranging run is enough as we had demonstrated in the v3.1 round.

Doesn't the power workflow mandate (and the submission checker enforce) runs of equal duration?

### mrasquinha-g · 2024-02-20

Power ranging run does not need to follow the min query count.

### nv-ananjappa · 2024-02-20

@nv-jinhosuh Please provide your feedback to Arjun/Anton.

### arjunsuresh · 2024-02-20

@psyhtest yes. There is no rule that mandates a ranging mode run of same duration of a testing run. We have shown that a 5-minute ranging mode run works pretty well in doing a real power estimate in v3.1

### nv-jinhosuh · 2024-02-20

@psyhtest @arjunsuresh We have enabled GPT-J SingleStream equal issue mode during last round (3.1). 
https://github.com/mlcommons/inference/blob/v3.1/mlperf.conf
https://github.com/mlcommons/inference/pull/1470

In sum, Early Stopping is in general 'wrong' if it is used other than 'server' scenarios, given the workload is non-uniform. One of the way we used as a work-around is to enable equal issue mode as it utilizes all the samples equally in the set, and if the total number of samples ran is multiple of total set size, the Early Stopping statistics works more friendly.

### nv-jinhosuh · 2024-02-20

FWIW, offline doesn't use Early Stopping, and Server Early Stopping is okay (statistics is on binomial process). SingleStream/MultiStream is using Early Stopping where ES has to estimate the latency distribution and then it can decide the pass/fail upon target latency. Without Equal Issue mode, ES will trigger failure rather randomly.

### arjunsuresh · 2024-02-20

Thank you @nv-jinhosuh for explaining. But GPT-J equal issue mode was enforced in the submission checker only 2 weeks back - https://github.com/mlcommons/inference/pull/1610/files#diff-4aea9ab8b222eed4a7096c6707e8e37682594dcb485d9b7450ad1b2e7155a853R45. I guess in the last round it was done for Server scenario but not for others. 

This change came after the random seeds are released. So, there is a concern on what to do with the submission which were taken before this rule was enforced. Can you please point to any rule which mandates equal issue mode for the required models? We'll also need to add this check in the submission checker going forward. 

### nv-jinhosuh · 2024-02-20

@arjunsuresh I believe GPT-J SS equal issue mode was added last round as in the above links, not two weeks ago: https://github.com/mlcommons/inference/blob/ce189bda3e3519b3b363e9f7ecf533c1cb0ab57e/mlperf.conf#L43

I don't think we have any policy set up for equal issue mode requirement. As above, Equal Issue mode is to alleviate the inconvenience Early Stopping is causing. Even if conceptually they are a separate thing, I believe we have to talk about the two altogether.
Unfortunately what benchmark/scenario uses Equal Issue mode is all over the place at the moment because we have not discussed it throughly in the WG. We need some inputs from statistics experts (original contributor Caitlyn for example) to the fundamentals of what the Early Stopping impact is and what the mitigation should be (say, Equal Issue mode is enough, of should we change metrics, on what benchmarks/scenarios etc).

### arjunsuresh · 2024-02-20

My apologies @nv-jinhosuh I got misled by the commit diff. But in v3.1 for some reason the equal issue mode was not effective.  

### nv-jinhosuh · 2024-02-20

@arjunsuresh Unfortunately I have no idea why it didn't work out last round on your side. But I believe NVIDIA's SS submission indeed was using it (as it was enforced by LoadGen). Rather than saying it's important it was working last round or this round, what I am trying to point out here is:
- Without Equal Issue mode, your SingleStream/MultiStream measurements would be incorrect, as your latency distribution is not representing the whole dataset, and based on the random seed, you will notice unacceptable variation.
- Without Equal Issue mode, Early Stopping may trigger PASS/FAIL in rather unexpected way and once it triggers you will not be able to easily workaround by bumping up/down min_query_count and/or min_duration.
- Without Equal Issue mode, your test and audit test may go separate ways, although GPT-J is not required for audit test so it's probably not a concern to you.

I do understand the hardship of running the test for multiple days (as I had to do that too). This is a known issue that we don't have clear answers yet: should we reduce samples in the input set, or should we allow using reduced sample set (for example)?

### arjunsuresh · 2024-02-20

@nv-jinhosuh I completely understand that I had the same concern when we were able to run just [100 queries](https://github.com/mlcommons/inference_results_v3.1/blob/main/open/CTuning/results/amd_zen4_workstation-reference-gpu-pytorch-v2.0.1-default_config/gptj-99/singlestream/performance/run_1/mlperf_log_summary.txt#L45) in the last round and able to infer an offline result as well. I believe it happened because we did the test on [July 15](https://github.com/mlcommons/inference_results_v3.1/blob/main/open/CTuning/results/amd_zen4_workstation-reference-gpu-pytorch-v2.0.1-default_config/gptj-99/singlestream/performance/run_1/mlperf_log_detail.txt#L8) - and this change came in August. 

We do not have any issue this round with equal issue mode - we have already completed the runs with equal issue mode. My question was more to point to the rules if someone raises a concern with it and also to add this check in the submission checker for 4.1 so that everyone is forced to follow it. 

### nv-jinhosuh · 2024-02-20

Thanks @arjunsuresh That explains. I opened this issue https://github.com/mlcommons/inference/issues/1634 for future discussions.

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
