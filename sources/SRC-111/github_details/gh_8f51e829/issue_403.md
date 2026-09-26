# [Issue #403] Online docs are not updating

source: https://github.com/vllm-project/guidellm/issues/403
state: closed | updated: 2026-06-25T19:58:57Z
labels: internal

## 正文


### Discussed in https://github.com/vllm-project/guidellm/discussions/396

<div type='discussions-op-text'>

<sup>Originally posted by **tukwila** October  9, 2025</sup>
I found guidellm benchmark test example pull request (https://github.com/vllm-project/guidellm/pull/328) is merged into main but not published in https://blog.vllm.ai/guidellm/main/examples/; what can i do to complete this demo content？ </div>

## 评论 (1)

### tukwila · 2025-10-11

@sjmonson 
I tried to find out the problem and the following is result:
1. ci job: cleanup-ui-pr-preview in action: development-cleanup.yml is just for ui commit except docs commit; so i'm not sure if this job should be corrected, for example:
https://github.com/vllm-project/guidellm/actions/runs/18418700153/job/52488292661;

2. anther job: ui-pr-preview in development.yml is the same:
https://github.com/vllm-project/guidellm/actions/runs/18161932896/job/51694675090?pr=328

maybe these jobs are reasonable, so i will submit totally new ci job as bug fix to update gh-pages branch. If any problem, pls correct me. :)

