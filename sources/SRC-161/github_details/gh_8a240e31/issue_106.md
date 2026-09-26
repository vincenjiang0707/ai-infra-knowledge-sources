# [Issue #106] add baseline choice

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/106
state: closed | updated: 2025-12-04T09:22:42Z
labels: 

## 正文

Is there any chance to add a new torch native base line?

## 评论 (1)

### xslingcn · 2025-10-30

Hi, thanks for the question! At the moment the baselines on web is manually specified in https://github.com/flashinfer-ai/flashinfer-bench/blob/main/web/apps/web/data/baselines.ts
If you want to see aggregated fast_p results against your customized baselines, one way to do it is to update the baseline file and serve the leaderboard locally.

To serve the leaderboard, you could clone the repo and inside the web/ folder run
`npm install && FLASHINFER_TRACE_PATH=<PATH_TO_YOUR_TRACE> npm --filter @flashinfer-bench/web dev`
Remember to set FLASHINFER_TRACE_PATH to where you store the traces. Otherwise it would look for traces under /tmp/flashinfer-trace.
You should be then able to view the leaderboard at http://localhost:3000/.

We don't yet have a feature to dynamically switch the baselines on the web, but would love to support that soon!
