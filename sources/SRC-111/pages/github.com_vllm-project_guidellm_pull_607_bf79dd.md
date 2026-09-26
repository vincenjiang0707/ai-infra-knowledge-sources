source: https://github.com/vllm-project/guidellm/pull/607

# Instant ttft oversaturation - #607

Merged

Merged

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)Feb 23, 2026

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Feb 27, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

One nit, did not check test. Also I will do a manual regression verification on a few other common use-cases before merging.

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/607/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/35fb0292f40f22fdda6f0f3b8ce35ce825ac6b03..451860d2cfa652238626c01e2f78f151158313c9)the instant-ttft-oversaturation branch from

[to](https://github.com/vllm-project/guidellm/commit/35fb0292f40f22fdda6f0f3b8ce35ce825ac6b03)

`35fb029`


`451860d`

[Compare](https://github.com/vllm-project/guidellm/compare/35fb0292f40f22fdda6f0f3b8ce35ce825ac6b03..451860d2cfa652238626c01e2f78f151158313c9)

March 1, 2026 11:34

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/92b8ccd39763d47e8201dcc2003f50060ccac516..845aea8a608e871f276da5bcbd15d824acd41dd1)the instant-ttft-oversaturation branch from

[to](https://github.com/vllm-project/guidellm/commit/92b8ccd39763d47e8201dcc2003f50060ccac516)

`92b8ccd`


`845aea8`

[Compare](https://github.com/vllm-project/guidellm/compare/92b8ccd39763d47e8201dcc2003f50060ccac516..845aea8a608e871f276da5bcbd15d824acd41dd1)

March 2, 2026 19:45

Signed-off-by: Uri Shaket <ushaket@redhat.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/845aea8a608e871f276da5bcbd15d824acd41dd1..f9267cb241779e9b99146a66e220fabe5cf08866)the instant-ttft-oversaturation branch from

[to](https://github.com/vllm-project/guidellm/commit/845aea8a608e871f276da5bcbd15d824acd41dd1)

`845aea8`


`f9267cb`

[Compare](https://github.com/vllm-project/guidellm/compare/845aea8a608e871f276da5bcbd15d824acd41dd1..f9267cb241779e9b99146a66e220fabe5cf08866)

March 3, 2026 01:15


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 3, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

After some stress testing, no noticeable impact to scheduling performance. Did not test oversaturation detection but code changes seem reasonable.

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

When over-saturation detection is enabled (

`--detect-saturation`

), the constraint can only receive TTFT data after a request fully completes. With large models and long contexts, no request completes within the`minimum_duration`

window (default 30s), so the constraint falls back to concurrent slope alone and stops prematurely.This PR adds time-bounded instant TTFT notifications: when over-saturation detection is enabled, worker processes monitor for first-token arrival during streaming and send a

`"first_token_arrived"`

status update before the request completes. This gives the constraint real TTFT data for a two-signal decision. Notifications are sent only during the first`minimum_duration`

seconds of the benchmark to limit IPC overhead.## Details

`"first_token_arrived"`

to`RequestInfo.status`

literal (`schemas/info.py`

)`WorkerProcess`

— spawns an async task per request that detects`first_token_iteration`

and sends a`"first_token_arrived"`

update (`scheduler/worker.py`

)`minimum_duration`

seconds via`instant_ttft_duration`

(`scheduler/worker.py`

)`"first_token_arrived"`

in`WorkerGroupState`

— no request count changes, passes through to constraints (`scheduler/worker_group.py`

)`minimum_duration`

from`OverSaturationConstraint`

to configure worker TTFT duration (`scheduler/worker_group.py`

)`"first_token_arrived"`

and`"completed"`

in the constraint, deduplicated by request ID (`scheduler/constraints/saturation.py`

)## Test Plan

`pytest tests/unit/scheduler/ tests/unit/schemas/ tests/unit/backends/`

— 1077 passed`pre-commit run --files`

on changed files — all checks pass`--detect-saturation`

on a large model with long context (>10k tokens) that the benchmark no longer stops prematurely## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)