# [Issue #1329] Submission checker error with 3d-unet

source: https://github.com/mlcommons/inference/issues/1329
state: closed | updated: 2026-05-15T00:42:58Z
labels: Stale

## 正文

Got the following error when run submission checker. 

[2023-02-08 05:37:40,235 submission_checker.py:1645 ERROR] closed/Intel/results/1-node-2S-SPR-PyTorch-INT8/3d-unet-99.9/Offline/performance/run_1/mlperf_log_detail.txt performance_sample_count, found 0, needs to be >= 43
[2023-02-08 05:37:40,235 submission_checker.py:1696 INFO] Target latency: None, Latency: 14079230289064, Scenario: Offline
[2023-02-08 05:37:40,235 submission_checker.py:2336 ERROR] closed/Intel/results/1-node-2S-SPR-PyTorch-INT8/3d-unet-99.9/Offline/performance/run_1 has issues

While in mlperf.conf https://github.com/mlcommons/inference/blob/c4a19872d9e7ba2fe2d5b8a4c3d3c02e82233785/mlperf.conf#L14 performance_sample_count_override is 0. What is the correct performance_sample_count_override for 3dunet in 3.0?
# set to 0 to let entire sample set to be performance sample
3d-unet.*.performance_sample_count_override = 0



## 评论 (4)

### pgmpablo157321 · 2023-02-10

This error seems very weird, since if you set `performance_sample_count_override`, the `performance_sample_count` should be the size of the dataset.
https://github.com/mlcommons/inference/blob/c4a19872d9e7ba2fe2d5b8a4c3d3c02e82233785/loadgen/test_settings_internal.cc#L117-L119

For 3d-unet this should be 43. You could try to set this value to 43 and see if this solves your issue, but it should work with 0.

### najeeb5 · 2023-02-23

Any updates on this issue?


### nv-ananjappa · 2023-04-18

@rnaidu02 Can this be closed?

### github-actions[bot] · 2026-05-15

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
