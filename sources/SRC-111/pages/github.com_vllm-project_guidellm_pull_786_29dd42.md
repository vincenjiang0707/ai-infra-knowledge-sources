source: https://github.com/vllm-project/guidellm/pull/786

# Constraints refactor - #786

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 7 commits into

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)self-requested a review

June 9, 2026 20:44


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

A few comments on a very quick first pass ... I'll delve deeper tomorrow morning.

[src/guidellm/scheduler/constraints/args.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-c8c34409034d2c6ca1215dfdc92fe7116e871dcab575ba4009cb16504695bad3)Outdated

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 9, 2026

[src/guidellm/scheduler/constraints/saturation.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-79ab5e822d3d7f17056f07ceb5ac0412f153eca36d177dc644f007f31a276eee)Outdated

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated

[src/guidellm/scheduler/constraints/error.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-6c93b401da3810f357ca2992124fe874419e670f6e612618ab146d0d88946f8a)Outdated

[src/guidellm/scheduler/constraints/request.py](https://github.com/vllm-project/guidellm/pull/786/files#diff-5ffeaa1a32967eab4ff3b429eb6b9a96cd5dae96d5452524550ef03357854cf8)

Uses a new format with a kind discriminator and separate args classes. Includes translation layer for the old CLI format to use the new constraints format. Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Remove old create method, remove unnecessary comments, and remove unnecessary static function. Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/14f5a45dfa63793129a6f4a3811ecb727738b0af..f813642b8e2df6090a13f1c2af2f0011b633c7c9)the feat/constraints-refactor branch from

[to](https://github.com/vllm-project/guidellm/commit/14f5a45dfa63793129a6f4a3811ecb727738b0af)

`14f5a45`


`f813642`

[Compare](https://github.com/vllm-project/guidellm/compare/14f5a45dfa63793129a6f4a3811ecb727738b0af..f813642b8e2df6090a13f1c2af2f0011b633c7c9)

June 10, 2026 17:44

Collaborator
Author

|
This is now rebased and ready for ew-review. |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 10, 2026

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files/14f5a45dfa63793129a6f4a3811ecb727738b0af#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated

[src/guidellm/scheduler/constraints/factory.py](https://github.com/vllm-project/guidellm/pull/786/files/f813642b8e2df6090a13f1c2af2f0011b633c7c9#diff-1669637323f7f440b0e7d421b497bd7550ddcb3bc2a3ed09af636720c406a538)Outdated

…raint Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e0debc938f7a0827594ecd3ccf1a39d74e5cbdeb..05ca95fdf8bd251cee3d4431e338331e580d2969)the feat/constraints-refactor branch from

[to](https://github.com/vllm-project/guidellm/commit/e0debc938f7a0827594ecd3ccf1a39d74e5cbdeb)

`e0debc9`


`05ca95f`

[Compare](https://github.com/vllm-project/guidellm/compare/e0debc938f7a0827594ecd3ccf1a39d74e5cbdeb..05ca95fdf8bd251cee3d4431e338331e580d2969)

June 10, 2026 22:01


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 11, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

This is now rebased and ready for ew-review.


Ew ... 😆


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 11, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Looks good. Tested locally with a bunch of constraints and all seem to work.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

15 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Uses a new format with a

`kind`

discriminator and separate args classes. Includes translation layer for the old CLI format to use the new constraints format.## Details

`max_duration`

instead of`max_seconds`

since it's more generic and with the follow up refactor we can do`--constraint kind=max_duration,seconds=120`

, which would enable`--constraint kind=max_duration,minutes=2`

, or in the new format`--constraint max_duration seconds=120`

## Test Plan

## Related Issues

## Use of AI

## git log

commit

d6a2313Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 9 14:22:47 2026 -0400

commit

04c6960Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 9 15:57:43 2026 -0400

commit

03046f3Author: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 10 11:56:26 2026 -0400

commit

1e73fcaAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 10 13:11:01 2026 -0400

commit

f813642Author: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 10 13:26:28 2026 -0400

commit

f89bd7bAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 10 17:51:12 2026 -0400

commit

05ca95fAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 10 17:54:39 2026 -0400

Assisted-by: Cursor AI Claude Opus 4.6

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com