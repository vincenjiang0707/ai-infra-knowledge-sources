source: https://github.com/vllm-project/guidellm/pull/871

## Conversation

The scheduler has no concept of a GenerationRequest so move the request settings out as a separate object in a tuple. Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

3 tasks

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jul 2, 2026

## Summary Continuation of PR[#871]. ## Details - Add `requeue_delay_column` to the column mapper - Add `synthetic_text` dataset support for requeue delay - Add basic tests in `test_synthetic.py` ## Test Plan - `tox` ## Related Issues - Resolves[#871]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 14:45:28 2026 -0400 Fix interface between data and scheduler The scheduler has no concept of a GenerationRequest so move the request settings out as a separate object in a tuple. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]254da7a[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 15:48:32 2026 -0400 Move requeue delay to request settings Signed-off-by: Samuel Monson <smonson@redhat.com> commit]e69d65e[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 16:19:12 2026 -0400 Fixup Tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]a12e135[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 14:56:34 2026 -0400 Add requeue_delay_column to column mapper Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8732459[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 15:26:06 2026 -0400 synthetic text dataset support for requeue delay Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f600d71[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 16:25:51 2026 -0400 Add basic tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]a24430b[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 17:44:40 2026 -0400 Don't clear request_info after _process_next_request Signed-off-by: Samuel Monson <smonson@redhat.com> commit]0a1a2a5[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:18:32 2026 -0400 Rework random number generation logic Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]97a6076[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:20:55 2026 -0400 Rework random number generation logic x2 Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]738257b[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:29:52 2026 -0400 fix: Call correct random generator Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]6a2dea3[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:33:36 2026 -0400 Don't round in FloatRangeSampler Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]25048e9[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:38:09 2026 -0400 Set minimum val of calc_min to 0.0 instead of 1 Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> --------- Co-authored-by: Samuel Monson <smonson@irbash.net> Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>]8b68f67

[SkiHatDuckie](https://github.com/SkiHatDuckie)added a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…ject#876]) ## Summary Continuation of PR[vllm-project#871]. ## Details - Add `requeue_delay_column` to the column mapper - Add `synthetic_text` dataset support for requeue delay - Add basic tests in `test_synthetic.py` ## Test Plan - `tox` ## Related Issues - Resolves[vllm-project#871]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 14:45:28 2026 -0400 Fix interface between data and scheduler The scheduler has no concept of a GenerationRequest so move the request settings out as a separate object in a tuple. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]254da7a[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 15:48:32 2026 -0400 Move requeue delay to request settings Signed-off-by: Samuel Monson <smonson@redhat.com> commit]e69d65e[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 29 16:19:12 2026 -0400 Fixup Tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]a12e135[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 14:56:34 2026 -0400 Add requeue_delay_column to column mapper Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8732459[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 15:26:06 2026 -0400 synthetic text dataset support for requeue delay Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f600d71[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jul 1 16:25:51 2026 -0400 Add basic tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]a24430b[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 17:44:40 2026 -0400 Don't clear request_info after _process_next_request Signed-off-by: Samuel Monson <smonson@redhat.com> commit]0a1a2a5[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:18:32 2026 -0400 Rework random number generation logic Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]97a6076[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:20:55 2026 -0400 Rework random number generation logic x2 Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]738257b[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:29:52 2026 -0400 fix: Call correct random generator Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]6a2dea3[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:33:36 2026 -0400 Don't round in FloatRangeSampler Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> commit]25048e9[Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Date: Thu Jul 2 15:38:09 2026 -0400 Set minimum val of calc_min to 0.0 instead of 1 Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> --------- Co-authored-by: Samuel Monson <smonson@irbash.net> Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>]8b68f67

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Restores the originally planned per-request requeue delay.

## Details

Requeue delay is the time between completing a request in a conversation and scheduling the next one. It is also sometimes referred to as "think time". This feature was added back in v0.6.0 but was not exposed on a useable interface.

## Test Plan

## Related Issues

## Use of AI

## git log

commit

1a374e8Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 29 14:45:28 2026 -0400

commit

a84dc99Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 29 15:48:32 2026 -0400

commit

a425f5fAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 29 16:19:12 2026 -0400

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com