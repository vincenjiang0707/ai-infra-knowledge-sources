source: https://github.com/vllm-project/guidellm/pull/1079

# Bound token events by when they occur - #1079

Merged

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/61f9c9fded48f00d7acf2e6419058ab641af123d..1eb54755cf3043d156f1a2b27b8f3546578cc6c6)the feat/throughput_vs branch from

[to](https://github.com/vllm-project/guidellm/commit/61f9c9fded48f00d7acf2e6419058ab641af123d)

`61f9c9f`


`1eb5475`

[Compare](https://github.com/vllm-project/guidellm/compare/61f9c9fded48f00d7acf2e6419058ab641af123d..1eb54755cf3043d156f1a2b27b8f3546578cc6c6)

September 2, 2026 15:18

7 tasks

Only count thoughput that falls within start/stop and only count TTFTs that fall fully inside start/stop. Assisted-by: Codex Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1eb54755cf3043d156f1a2b27b8f3546578cc6c6..2f312d087a937e0188be198e8c88782dfd1c9d2a)the feat/throughput_vs branch from

[to](https://github.com/vllm-project/guidellm/commit/1eb54755cf3043d156f1a2b27b8f3546578cc6c6)

`1eb5475`


`2f312d0`

[Compare](https://github.com/vllm-project/guidellm/compare/1eb54755cf3043d156f1a2b27b8f3546578cc6c6..2f312d087a937e0188be198e8c88782dfd1c9d2a)

September 14, 2026 22:04

TTFT, TTFOT, and ITL are all events the occur during the part of the request. When calculating which events are inside the main phase (happen after warmup and before cooldown) we want to bound by the event itself rather than the request. For first token also be a bit more strict and ensure that the whole event is within latency bounds. Signed-off-by: Samuel Monson <smonson@redhat.com>

When getting prefill events within the main range switch to including requests that partially overlap the main phase. This matches how other metrics are handled. It is still debatable which approch is better, since we are on a bit of a time crunch to get this out stick with this approch for now and do more testing in post. Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2f312d087a937e0188be198e8c88782dfd1c9d2a..b70695cebb03dafcb725545ea3a6a4e7e5830666)the feat/throughput_vs branch from

[to](https://github.com/vllm-project/guidellm/commit/2f312d087a937e0188be198e8c88782dfd1c9d2a)

`2f312d0`


`b70695c`

[Compare](https://github.com/vllm-project/guidellm/compare/2f312d087a937e0188be198e8c88782dfd1c9d2a..b70695cebb03dafcb725545ea3a6a4e7e5830666)

September 15, 2026 16:05

Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>


[sjmonson](https://github.com/sjmonson)changed the title

Sep 15, 2026

[sjmonson](https://github.com/sjmonson)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema)and

[jaredoconnell](https://github.com/jaredoconnell)and removed request for

[dbutenhof](https://github.com/dbutenhof)

September 15, 2026 18:45

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

September 15, 2026 18:45


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 15, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Hmm. Code is straightforward; comments and documentation seem a bit inconsistent about token event metrics, but while some suggest these should be open, all actual calls are closed. Since I'm not sure which is right either (logic kinda breaks down here, and I understand why someone might run a warmup phase to completion and then start metrics clean to avoid the whole issue) ... I'm not objecting. I also want to think a bit more before approving.

[src/guidellm/benchmark/schemas/accumulator.py](https://github.com/vllm-project/guidellm/pull/1079/files/91637e5655c83f6d5d10e593988c925e34eef141#diff-e73c95dad9126d4792d1e44f55efd731323c091d121150aa8af790d86cdc822d)

[src/guidellm/benchmark/schemas/metrics.py](https://github.com/vllm-project/guidellm/pull/1079/files/91637e5655c83f6d5d10e593988c925e34eef141#diff-afc9e694b983a862e3aa3613a213c97508b3fd79ddc5280fa110f304b56f4672)Outdated

[src/guidellm/benchmark/schemas/metrics.py](https://github.com/vllm-project/guidellm/pull/1079/files/91637e5655c83f6d5d10e593988c925e34eef141#diff-afc9e694b983a862e3aa3613a213c97508b3fd79ddc5280fa110f304b56f4672)

[src/guidellm/benchmark/schemas/accumulator.py](https://github.com/vllm-project/guidellm/pull/1079/files/91637e5655c83f6d5d10e593988c925e34eef141#diff-e73c95dad9126d4792d1e44f55efd731323c091d121150aa8af790d86cdc822d)

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 15, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 15, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

5 tasks

[PatilHrushikesh](https://github.com/PatilHrushikesh)pushed a commit to PatilHrushikesh/guidellm that referenced this pull request

Sep 21, 2026

## Summary Modify the request bounding code to use different event bounds for each latency event. See[vllm-project#1078]for more details. ## Test Plan Run a benchmark with warmup and verify differences in collected ttft, token throughput, etc. Note that when running a shorter concurrent run with rampup+warmup vs a longer run with no rampup+warmup the results of the shorter run should be closer than without this patch. ```sh guidellm run \ --backend kind=openai_http,target=[http://127.0.0.1:8000]--profile kind=concurrent,rampup_duration=45,warmup=75 \ --override profile.streams 200 --data "kind=synthetic_text,prompt_tokens=500,output_tokens=512" \ --constraint kind=max_duration,seconds=275 ``` ## Related Issues - Resolves[vllm-project#1078]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 1 21:06:45 2026 +0000 Clip metrics by start/stop Only count thoughput that falls within start/stop and only count TTFTs that fall fully inside start/stop. Assisted-by: Codex Signed-off-by: Samuel Monson <smonson@redhat.com> commit]202b75d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Sep 14 18:01:01 2026 -0400 Bound token latency events by when they occur TTFT, TTFOT, and ITL are all events the occur during the part of the request. When calculating which events are inside the main phase (happen after warmup and before cooldown) we want to bound by the event itself rather than the request. For first token also be a bit more strict and ensure that the whole event is within latency bounds. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]efb8314[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 12:00:18 2026 -0400 Switch TTFT and TTFOT to open range When getting prefill events within the main range switch to including requests that partially overlap the main phase. This matches how other metrics are handled. It is still debatable which approch is better, since we are on a bit of a time crunch to get this out stick with this approch for now and do more testing in post. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b70695c[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 17:48:30 2026 +0000 Fix and add tests Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com> commit]308d051[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 18:25:59 2026 +0000 Add a little documentation for warmup/cooldown Assisted-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com> commit]91637e5[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 16:21:12 2026 -0400 Address review Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: Codex Assisted-by: Cursor Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>]72fc6d5

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Modify the request bounding code to use different event bounds for each latency event. See #1078 for more details.

## Test Plan

Run a benchmark with warmup and verify differences in collected ttft, token throughput, etc. Note that when running a shorter concurrent run with rampup+warmup vs a longer run with no rampup+warmup the results of the shorter run should be closer than without this patch.

`guidellm run \ --backend kind=openai_http,target=http://127.0.0.1:8000 --profile kind=concurrent,rampup_duration=45,warmup=75 \ --override profile.streams 200 --data "kind=synthetic_text,prompt_tokens=500,output_tokens=512" \ --constraint kind=max_duration,seconds=275`

## Related Issues

## Use of AI

## git log

commit

202b75dAuthor: Samuel Monson smonson@redhat.com

Date: Tue Sep 1 21:06:45 2026 +0000

commit

efb8314Author: Samuel Monson smonson@redhat.com

Date: Mon Sep 14 18:01:01 2026 -0400

commit

b70695cAuthor: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 12:00:18 2026 -0400

commit

308d051Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 17:48:30 2026 +0000

commit

91637e5Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 18:25:59 2026 +0000

commit

72fc6d5Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 16:21:12 2026 -0400

Assisted-by: Codex

Assisted-by: Cursor

Generated-by: Cursor

Signed-off-by: Samuel Monson smonson@redhat.com