# [Issue #105] How to dump the fast_p chart as figure at local?

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/105
state: open | updated: 2025-10-30T12:37:35Z
labels: 

## 正文

Do you know how to dump a [figure/chart](https://bench.flashinfer.ai/) like this from trace offline?

<img width="1394" height="883" alt="Image" src="https://github.com/user-attachments/assets/f96e3850-c678-405a-8199-4a4ca8744e17" />

## 评论 (1)

### xslingcn · 2025-10-30

Hi, thanks for the question!
If you want the exact interactive, aggregated fast_p chart as the leaderboard, the best way is to serve the leaderboard webapp from your local trace set.

Just clone the repo, and inside the web/ folder run
`npm install && FLASHINFER_TRACE_PATH=<PATH_TO_YOUR_TRACE> npm --filter @flashinfer-bench/web dev`
Remember to set `FLASHINFER_TRACE_PATH` to where you store the traces. Otherwise it would look for traces under `/tmp/flashinfer-trace`.
You should be then able to view the leaderboard at http://localhost:3000.

For static figures, I think we had a script [here](https://github.com/flashinfer-ai/flashinfer-bench/blob/main/examples/win_at_p.py). It's been there for a while, so I'm not sure if it's up to date. cc @YiyanZhai 
We'll update a leaderboard set up guide soon!
