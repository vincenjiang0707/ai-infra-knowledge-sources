# [Issue #1786] Log() is async using thread - causing issues in timing between first token CacheToken() and SampleComplete() calls

source: https://github.com/mlcommons/inference/issues/1786
state: closed | updated: 2026-07-24T00:31:29Z
labels: inference v5.0, Stale

## 正文

Hi,

I have found that, we are using async logging mechanism using thread, when generate accuracy log entries (content of responses, either first token or sample response). This mechanism is working fine for writing sample responses between different samples, as they are independent with each other and therefore there's no rule to abide by. Say accuracy log bitstream in hex for sample X can be generated in memory later than sample Y that followed sample X.

https://github.com/mlcommons/inference/blob/c3c68ee61896e1e4d74b096565b627e14422337d/loadgen/loadgen.cc#L153
https://github.com/mlcommons/inference/blob/c3c68ee61896e1e4d74b096565b627e14422337d/loadgen/logging.cc#L1291

Now, this causes a problem for any network that needs to log first token response and final sample response into the memory, as we put a rule where first token has to arrive before sample response. Calling the completion API, i.e. FirstTokenComplete and QuerySamplesComplete, guarantees recording the timing of them. However, when running an accuracy run, even though calls to completion of first token and sample response are called strictly in order, the writing content of them into memory is not guaranteed to happen in order, due to async logging nature upon threading.

This causes a failure when sample response is trying to write log into memory when token response, for any reason, got delayed. More specifically, in below line for example, since token entry hasn't written into, the token_records_ couldn't find the entry on the index for sample response, and LoadGen would hit into segfault:
https://github.com/mlcommons/inference/blob/c3c68ee61896e1e4d74b096565b627e14422337d/loadgen/logging.cc#L298

This is a pretty serious bug, with no simple fix I can quickly think of.
@nvzhihanj @ashwin @pgmpablo157321 @mrmhodak FYI

## 评论 (7)

### mrmhodak · 2024-07-17

Good find, @nv-jinhosuh. 

Adding it as a topic to WG discussion next week. Are there any short term impacts on the upcoming submission?

### nv-jinhosuh · 2024-07-17

@mrmhodak Some people may hit segfault during Accuracy run and/or audit test while running Llama2 or Mixtral - it may require non-trivial fix from their end to avoid it. Same goes for LoadGen fix to handle this properly once and for all.

### arjunsuresh · 2024-07-18

We are seeing this error on a server scenario test run
```
:::MLLOG {"key": "error_runtime", "value": "Attempted to record a sample latency before it's first token latency", "time_ms": 0.840219, "namespace": "mlperf::logging", "event_type": "POINT_IN_TIME", "metadata": {"is_error": true, "is_warning": false, "file": "logging.cc", "line_no": 414, "pid": 144270, "tid": 144335}}
```

### nv-jinhosuh · 2024-07-18

@arjunsuresh If you saw this on Accuracy run, it is likely due to above issue. If you saw this in performance run, it might be due to 0-length response Mixtral generates, which you may be able to counter in the harness (may be nontrivial).

### arjunsuresh · 2024-07-19

Thank you @nv-jinhosuh for your reply. It was an issue in our implementation - the implementation was sending the whole sample response to the loadgen in one go like for non-LLM benchmarks. It is fine now :)

### mrmhodak · 2024-07-23

Not enough time to fix in this round. Injecting a delay fixes the issue. 

Must fix for 5.0

### github-actions[bot] · 2026-07-24

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
