# [Issue #2338] [Tracker] Deprecate llm-d images

source: https://github.com/llm-d/llm-d/issues/2338
state: open | updated: 2026-08-20T15:57:37Z
labels: official-guides, CI/CD, Image builds

## 正文

Actions required:

- llm-d-cuda
    - [ ] Remove building llm-d cuda images from CICD
    - [ ] Update guides to use deepep HT v2
- llm-d-aws
    - [x] Remove building llm-d aws images from CICD
- llm-d-xpu - TBD
- llm-d-xpu-sglang - TBD althought this seems like it will be kept around for a release or two at least
- llm-d-cpu - TBD

## 评论 (1)

### Gregory-Pereira · 2026-08-20

> Remove building llm-d aws images from CICD

Done in: https://github.com/llm-d/llm-d/pull/2334
