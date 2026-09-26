# [Issue #323] Compatibility for Slack

source: https://github.com/gpu-mode/kernelbot/issues/323
state: closed | updated: 2025-09-02T11:35:16Z
labels: 

## 正文

Hi, thank you creating such an amazing tool. I would love to implement this to my company's slack channel as an alternative to help researchers launch distributed training job on AWS instances with Ray framework. I don't know if it's compatible. I would appreciate some advice.

## 评论 (1)

### msaroufim · 2025-08-08

Hi @luongthecong123 so recently we did do a big refactor that makes the codebase more modular, the way I'd go about this is refactoring the Discord specific bits to also support Slack and refactor the Github/Modal specific bits to also support the Ray job scheduler

I'm certainly open to reviewing PRs if you'd like to merge your code here directly but we probably won't have time on our core team to make this happen
