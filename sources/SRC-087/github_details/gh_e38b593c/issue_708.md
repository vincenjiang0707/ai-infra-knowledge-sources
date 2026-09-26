# [Issue #708] [RFC]: Adding step-based iteration during training on par with epoch-step

source: https://github.com/vllm-project/speculators/issues/708
state: open | updated: 2026-07-02T19:22:15Z
labels: RFC

## 正文

### Motivation.

I use your library to train DFlash on my own data and I have quite a large dataset (>1M samples) and I often encounter problems unrelated to the library itself while running training. For example vLLM server shutdown or NCCL communication errors. As I have a lot of data even 1 epoch takes tens of hours, so facing those minor problems is almost inevitable. However, both validation and saving occur quite rarely. Though I found out that I can save checkpoints more often, I still can not continue training from exactly the same checkpoint in the middle of the epoch (as far as I understand).

### Proposed Change.

Thus said, I think it would beneficial for the community to implement the version of training code that would be based on the number of iterations rather than on the number of epochs. Moreover, it could make validation more ofter and more controllable. I suppose the number of batches used for validation could also be controlled by user with the default fallback options preserving current behaviour.

### Any Other Things.

_No response_

## 评论 (1)

### fynnsu · 2026-07-02

I think #603 should have made it easier to resume partway through an epoch if an errors occurs. Please take a look and let me know if that fits your use case.
