# [Issue #1412] Update submission checker for v3.1

source: https://github.com/mlcommons/inference/issues/1412
state: closed | updated: 2026-05-13T00:44:06Z
labels: Stale

## 正文

- [x] Add v3.1 config
- [x] Add DLRMv2 checks
- [x] Add GPT-J checks, with additional check for generation length (multiple metric)
- [x] Update to the last power version
- [x] Update seeds

## 评论 (4)

### arjunsuresh · 2023-06-22

@pgmpablo157321 The update to the latest power version can happen with [this PR](https://github.com/mlcommons/power-dev/pull/316) unless the power WG updates anything else. 

### arjunsuresh · 2023-07-11

@pgmpablo157321 We need to add GPT-J details [here](https://github.com/mlcommons/inference/blob/master/mlperf.conf) right?

### pgmpablo157321 · 2023-07-12

@arjunsuresh I am not sure, I see there is another conf file [here](https://github.com/mlcommons/inference/blob/master/language/gpt-j/mlperf.conf) that also doesn’t have the gpt-j details.

@badhri-intel @rnaidu02 Do you know if we need to put any values for gpt-j here?

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
