# [Issue #2453] Max CKPTS to save Support

source: https://github.com/AI-Hypercomputer/maxtext/issues/2453
state: closed | updated: 2026-04-28T18:21:53Z
labels: feature request

## 正文

### Feature or Model Request

Hi MaxText maintainers! I'm traininng LLMs with MaxText recently and I noticed MaxText does not support **specifying the max number of ckpts to save** to avoid blowing up the storage on system. 
I have a working, minimal implementation and I wonder this is a desired feature on the main branch. If yes, I'd love to open a PR!

### Additional Context

_No response_

## 评论 (2)

### RissyRan · 2026-01-26

Thanks for reaching out!

We do have this `checkpoint_period` [config](https://github.com/AI-Hypercomputer/maxtext/blob/96f137523896f5e51e17f3d6f82ed2404c928885/src/MaxText/configs/base.yml#L53) and `max_num_checkpoints_to_keep` [config](https://github.com/AI-Hypercomputer/maxtext/blob/96f137523896f5e51e17f3d6f82ed2404c928885/src/MaxText/configs/base.yml#L54) to specify how many checkpoints you'd like to store during the training. Will this help?

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.
