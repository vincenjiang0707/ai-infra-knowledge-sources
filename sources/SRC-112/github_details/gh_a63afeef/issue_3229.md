# [Issue #3229] Qwen3.8-Flash-Next FP8 SGLang AgentX on H200 results from AIPerf and from Site

source: https://github.com/SemiAnalysisAI/InferenceX/issues/3229
state: closed | updated: 2026-09-18T14:06:27Z
labels: 

## 正文

https://github.com/SemiAnalysisAI/InferenceX/actions/runs/33038487711/job/98406760985#step:5:215 shows 4 GPUs and also the SGLang command line is setup for 4 GPUs, but the site https://inferencex.semianalysis.com/inference/qwen-3-8-flash-next?g_model=Qwen3.8-Flash-Next&g_rundate=2026-09-15&i_metric=y_outputTputPerGpu&i_xmode=interactivity&i_gpus=h200_sglang&i_optimal=0&i_best=0&i_conclabel=1&i_seq=agentic-traces&i_dates=2026-08-27 shows 16 GPUs.

Also, AIPerf shows about 217 tok/s output per user at P90 and the site shows 13.

I may be misunderstanding the site and AIPerf of course, but decided to notify anyway just in case there's some error somewhere, sorry if this is a mistake on my part.

Thanks a lot for the site and the results!

## 评论 (2)

### functionstackx · 2026-09-17

@ivanbaldo that is concurrency 16 agents not 16 gpus

# of gpus is tep4 so 4 gpus

<img width="224" height="168" alt="Image" src="https://github.com/user-attachments/assets/01ea43c3-cf89-4e4d-bb43-8fd8870e7596" />

### ivanbaldo · 2026-09-18

Hi, thanks for answering!

Here it says 16 chips:

<img width="406" height="597" alt="Image" src="https://github.com/user-attachments/assets/ef789e20-e5e7-4d1d-a0ce-c9941975b19b" />

Also there it says a P90 of 13.53 which I can't find on the AIPerf results.

Thanks for double-checking this.
