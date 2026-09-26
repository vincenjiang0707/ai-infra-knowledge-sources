# [Issue #385] Failed to retrieve results from inference request.

source: https://github.com/triton-inference-server/perf_analyzer/issues/385
state: open | updated: 2025-05-28T20:36:05Z
labels: 

## 正文

What is the reason for this issue? `Failed to retrieve results from inference request.`


## 评论 (1)

### debermudez · 2025-05-28

This is usually because the measurement interval was too short for any responses to come back.
Can you provide the command you ran? This will help us debug.

