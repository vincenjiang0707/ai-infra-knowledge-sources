# [Issue #8540] [Feature] Implement Image Number Limitation for Image Processors

source: https://github.com/sgl-project/sglang/issues/8540
state: open | updated: 2026-09-23T23:42:53Z
labels: good first issue, Multi-modal

## 正文

### Checklist

- [ ] 1. If the issue you raised is not a feature but a question, please raise a discussion at https://github.com/sgl-project/sglang/discussions/new/choose Otherwise, it will be closed.
- [ ] 2. Please use English, otherwise it will be closed.

### Motivation

At present, there is no limitation on the number of images during the processing of mm data. It is necessary to impose such a limitation to prevent potential OOM and other problems.

(When using fast image processor, the GPU memory usage is roughly **1GiB** for each **4K** image)

### Related resources

Implementation Steps:
1. Define a constant, such as `IMAGE_NUM_LIMITATION = 5`, for each processor.
2. Modify the `baseprocessor` to utilize this constant for request validation.
3. Incorporate a server argument to enable modification of this numerical value.

In case you lack familiarity with the mm data processing pipeline, it is advisable to first refer to [here](https://github.com/zhaochenyang20/Awesome-ML-SYS-Tutorial/blob/main/sglang/code-walk-through/multimodal_request_lifecycle.md)

## 评论 (4)

### wang-zhuoran · 2026-02-24

Hi, I am new to sglang community and I’d like to work on this issue.

I noticed there was a previous attempt in #8553 (now closed). I read through it and saw discussion around where this limit should be enforced (API/front-end validation vs scheduler-side protection) and how the limit should be configured (server arg vs request params).

Could maintainers share what solution/scope would be preferred for a new PR here? I’m happy to follow the recommended design.


### sid22669 · 2026-02-27

Hi, I'd like to work on this issue. Will submit a PR soon.

### theskipper007 · 2026-04-01

I've opened a PR to address this: #21838

It adds a `--max-images-per-request` server argument that caps the number of images per request, with per-processor `IMAGE_MAX_NUM` defaults as fallback (e.g. InternVL already has 12). Includes 13 unit tests.

### hujunchao · 2026-09-09

 Hi! I'd like to revive the work from #19606 (closed by stale bot after 172 days of inactivity). The approach there — a per-processor IMAGE_NUM_LIMITATION default with --limit-mm-data-per-request taking priority — follows the direction hnyls2002 pointed to in #21838.
I've opened #38660 re-implementing this against current main (unit tests all green on an A100). @sid22669 please let me know if you had any further plans for the original work.
