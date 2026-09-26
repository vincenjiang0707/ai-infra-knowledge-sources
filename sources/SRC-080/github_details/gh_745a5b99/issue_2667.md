# [Issue #2667] Fast KLD metric

source: https://github.com/vllm-project/llm-compressor/issues/2667
state: closed | updated: 2026-08-29T00:55:04Z
labels: enhancement, good first issue, stale

## 正文

followup to https://github.com/vllm-project/llm-compressor/issues/2646#issue-4323565620

looking for the fastest way to calculate an accurate kl divergence metric using vllm inference, i think this would involve 2 models being served on vllm concurrently to avoid disk writes and calculating the kld in an online manner.

## 评论 (4)

### HDCharles · 2026-04-29

@jayakumarpujar 

### jayakumarpujar · 2026-04-29

@HDCharles Done with the changes. Ready for review

### github-actions[bot] · 2026-07-29

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-08-29

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
