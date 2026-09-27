# [Issue #4442] [Feature] TurboMind Engine: Add Vision Encoder support for Qwen3.5 model

source: https://github.com/InternLM/lmdeploy/issues/4442
state: closed | updated: 2026-04-04T02:19:23Z
labels: awaiting response, Stale

## 正文

### Motivation

Currently it seems that TurboMind Engine does not support the Vision Encoder of Qwen3.5 model.
Is stated in note [3] under the table at
https://lmdeploy.readthedocs.io/en/latest/supported_models/supported_models.html#turbomind-on-cuda-platform

Would be great if support for the Qwen3.5 vision encoder could be added for 'TurboMind' engine.

### Related resources

_No response_

### Additional context

_No response_

## 评论 (5)

### windreamer · 2026-03-21

This should already been fixed in #4430 . Could you please try it and feedback to us?

### lvhan028 · 2026-03-21

Hi, @hfassold 
Unfortunately, we don't have plans to implement this in the short term in the same way we did for the Qwen2/2.5 vision encoder. However, we do have a medium-term plan to implement it directly in "src/turbomind", likely targeting late April or May.

### hfassold · 2026-03-21

Thanks for the information, looking forward !
@windreamer - see the answer of @lvhan028 

### github-actions[bot] · 2026-03-29

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-04-04

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
