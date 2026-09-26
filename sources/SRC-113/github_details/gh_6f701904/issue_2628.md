# [Issue #2628] MLPerf v6.1 LoadGen <> Endpoints++ submission checker issues

source: https://github.com/mlcommons/inference/issues/2628
state: closed | updated: 2026-07-27T17:06:26Z
labels: 

## 正文

First we want to define the folder hierarchy of the endpoints log (which is similar to the current hierarchy):
```
<systems>/
  <benchmark>/
      <scenario>/
         config.yaml       # <- settings for the loadgen++, similar to mlperf.conf and user.conf
         performance/
            results_summary.json # <-- similar to the mlperf_log_details.txt
         accuracy/
            accuracy_results.json  # <-- contains the score of the accuracy runs (which is run back to back with the perf)
         audit/
            audit_<audit_name>.json        # e.g. audit_output_caching_test.json, for TEST04
```
Optional:
- reports.txt  # <-- similar to the mlperf_log_summary.txt

Opening items:

- [x] 1. The current submission checker issue doesn’t parse the Qwen-VL interactive logs (@zihaok and pablo to finalize once Rashid pushed the PR for accuracy)
- [x] 2. Edge Agentic benchmark log is not recognized (@Palanivelg reported this - @pgmpablo157321 will help add the support, helpful if there is a set of log) -> model name is qwen3.6-27B; Zihao to send the logs to Pablo once it's ready.
- [x] 3. Accuracy score file (results.json) needs to be uniformed (@arekay-nv is working on) - ETA Friday for first PR, ETA Tuesday for the final version
- [x] 4. Early stopping for SingleStream/Server not implemented in endpoints - we will waive it for endpoints and use min_samples for now (@wu6u3tw ) - Zhihan will bring up in next Tuesday's meeting
- [x] 5. TEST09 (OSL length check for GPT-OSS performance dataset): not implemented, discuss whether we should do it in endpoints or submission checker (@pgmpablo157321 will include that in the submission checker - compare average OSL of GPT-OSS results_summary.json to the threshold) https://github.com/mlcommons/inference/tree/master/compliance/TEST09#example-gpt-oss-120b  - ETA Pablo by next Tuesday EoD
- [x] 6. Whether we allow separate perf/accuracy run through endpoints? <- we want to advocate for no, will collect feedback next Tuesday

@pgmpablo157321 @tanvi-mlcommons @anandhu-eng @hanyunfan @mrmhodak  FYI

## 评论 (11)

### arekay-nv · 2026-07-10

[PR](https://github.com/mlcommons/endpoints/pull/400) is making the accuracy scores uniform.

### nvzhihanj · 2026-07-10

Seed inclusion is added: https://github.com/mlcommons/endpoints/pull/389

### arav-agarwal2 · 2026-07-13

Is there a place where we're generating example logs / results files with the accuracy scores / seed inclusion changes? That would be helpful to have a gold-standard view on what the data should look like for the current version of the endpoints loadgen.


### arekay-nv · 2026-07-13

@arav-agarwal2 i am working on an [endpoints PR](https://github.com/mlcommons/endpoints/pull/400) that will clean it up a bit. Can share some sample outputs with you once this gets merged.

### attafosu · 2026-07-14

@nvzhihanj @arekay-nv The main concern I have is on the early stopping waiver. If the min_samples is not enforced at the 270k samples (or slightly lower) in lieu of the ES, the outcome isn't quite the same vs legacy loadgen. We've had some extensive deliberations on it #2188. Unless we're waiving it for the legacy loadgen submissions, this is going to lead to some non-negligible perf difference (we've seen cases where server target qps has had to be tuned down just to satisfy ES)

### nvzhihanj · 2026-07-14

@attafosu we are aware of that discussion. We did some empirical investigation to bridge the loadgen server run with early stopping and endpoints loadgen++ run without early stopping, and doesn't seem we are observing a meaningful difference in the server results (we provided the logs to the MLC and WG earlier in the Google drive).

I agree in the long term we should 1) relax the threshold from 99% (which we already did in endpoints v0.7 If you remember); 2) have some statistical model implemented or a stricter min_samples. ES is a heavy lifting at this point from the submission, so we are proposing to lift it for now.

### hanyunfan · 2026-07-15

@mrmhodak Could you review this one and work on it offline?

### nvzhihanj · 2026-07-15

@attafosu as a reference, we discussed it in one of the post-mortem item here: https://docs.google.com/document/d/1Z2riBFQn6OoPIQtFDq7TunjyHldWsEA_dlKh6VysfVo/edit?tab=t.0#heading=h.8steharewt6x (6.0 post-mortem). Doesn't seem like the WGM note captured it (it might be missed by the notetaker)

### pgmpablo157321 · 2026-07-16

I have opened PRs for the following item 
  
> 2. Edge Agentic benchmark log is not recognized (@Palanivelg reported this - @pgmpablo157321 will help add the support, helpful if there is a set of log) -> model name is qwen3.6-27B; Zihao to send the logs to Pablo once it's ready.

https://github.com/mlcommons/inference/pull/2629

> 5. TEST09 (OSL length check for GPT-OSS performance dataset): not implemented, discuss whether we should do it in endpoints or submission checker (@pgmpablo157321 will include that in the submission checker - compare average OSL of GPT-OSS results_summary.json to the threshold) https://github.com/mlcommons/inference/tree/master/compliance/TEST09#example-gpt-oss-120b - ETA Pablo by next Tuesday EoD

https://github.com/mlcommons/inference/pull/2633

Finally, there is also one updating the expected folder structure to match the one described here
https://github.com/mlcommons/inference/pull/2630

Please review them as soon as possible

### nvzhihanj · 2026-07-17

Pending PR for early stopping, which has both post-processing and integration: https://github.com/mlcommons/endpoints/pull/417
@attafosu @psyhtest please try it out

### nvzhihanj · 2026-07-17

Earlying stopping has been merged. The report will contain early stopping report by default
