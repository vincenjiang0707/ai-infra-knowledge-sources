# [Issue #445] does GenAI perf support multi-turn with custom dataset?

source: https://github.com/triton-inference-server/perf_analyzer/issues/445
state: open | updated: 2025-10-28T16:22:12Z
labels: 

## 正文

I have a requirement to convert a custom synthetic dataset to genai-perf compatible, that multi-turn dataset has system prompt and multiple user/assistant prompts stored as messages[]. 

After reading the doc, https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/multi_turn.html, it is unclear how the text field would capture multi-turn values with system/prefix prompt. 

Another question, can the inputs.json from the output be used as input for re-runs?


## 评论 (3)

### leigao97 · 2025-10-28

I am also curious about the design of multi-turn custom dataset. Based on my understanding, the requests within the same session are sent serially with the `delay` values from the input jsonl file. However, I am not sure how the first request from different sessions would be sent. Are they sent based on poisson process? Does genai-perf rearrange the sessions in the dataset? Can I manually assign timestamp for the first turn from different sessions?
@the-david-oy Do you have any comments? Thank you in advance.

### the-david-oy · 2025-10-28

Thanks for your questions. Yes, you can provide a timestamp for the first request in each session. If you do so, I believe the delay for each request must be provided or will be assumed to be 0. You would do so by passing the `--fixed-schedule` flag to notify GenAI-perf that it is a fixed schedule you are passing in.

The multi-turn functionality means the previous turns would be prepended to the current turn when sent. The worker sending requests for the session keeps track of the turns to date and prepends those conversation turns to the next request. GenAI-Perf is being deprecated in favor of [AIPerf](https://github.com/ai-dynamo/aiperf). If you have any more questions, please ask there. AIPerf almost has parity with the recent addition of multi-turn, plus it adds a lot more functionality that should make your benchmarking more scalable, flexible, and valuable.

### leigao97 · 2025-10-28

Thank you for your answers. I will check out AIPerf. 
