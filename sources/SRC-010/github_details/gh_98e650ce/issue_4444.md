# [Issue #4444] How does the Qwen3.5 model disable thinking?

source: https://github.com/InternLM/lmdeploy/issues/4444
state: closed | updated: 2026-04-07T02:20:07Z
labels: awaiting response, Stale

## 正文

```bash
lmdeploy serve api_server /home/cheng/model/Qwen3.5-27B-AWQ \
--tp 4 \
--cache-max-entry-count 0.8 \
--log-level INFO \
--max-concurrent-requests 4 \
--model-name Qwen3.5-27B-AWQ \
--backend turbomind \
--max_batch_size 64 \
--api-key abc123 \
--server-port 8000 \
--cache-block-seq-len 32 \
```



## 评论 (4)

### SongXiaoMao · 2026-03-22

This one doesn't seem to recognize the image request, how do I need to enable multimodality?

### lvhan028 · 2026-03-22

Turbomind engine hasn't support Qwen3.5 vision encoder yet. 
You can use pytorch engine instead. But unfortunately the multimodal feature was accidently disabled in v0.12.2. 
Please use the latest main branch.

### github-actions[bot] · 2026-04-01

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-04-07

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
