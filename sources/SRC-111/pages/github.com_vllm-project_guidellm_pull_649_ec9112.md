source: https://github.com/vllm-project/guidellm/pull/649

# Add turn and conversation trackers to the request - #649

Merged

Merged

## Conversation


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 19, 2026


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Typo, but probably not worth blocking the change ...

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/649/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/35591a814bc7ed080b63bba9ecc44d95ed12e65c..9bf5eb4a0ba03565ea62d79d5104efde3e287aea)the feat/multiturn_trackers branch from

[to](https://github.com/vllm-project/guidellm/commit/35591a814bc7ed080b63bba9ecc44d95ed12e65c)

`35591a8`


`9bf5eb4`

[Compare](https://github.com/vllm-project/guidellm/compare/35591a814bc7ed080b63bba9ecc44d95ed12e65c..9bf5eb4a0ba03565ea62d79d5104efde3e287aea)

March 19, 2026 20:00

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9bf5eb4a0ba03565ea62d79d5104efde3e287aea..dcf6abace9bc4bc19ab5037c8fc8ae2a408cdb08)the feat/multiturn_trackers branch from

[to](https://github.com/vllm-project/guidellm/commit/9bf5eb4a0ba03565ea62d79d5104efde3e287aea)

`9bf5eb4`


`dcf6aba`

[Compare](https://github.com/vllm-project/guidellm/compare/9bf5eb4a0ba03565ea62d79d5104efde3e287aea..dcf6abace9bc4bc19ab5037c8fc8ae2a408cdb08)

March 19, 2026 20:01


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 19, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 19, 2026

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds a conversation id and turn index to requests. This allows users to post-process different views of turn-by-turn metrics.

## Test Plan

Run a benchmark and verify the fields are present:

## Use of AI

`## WRITTEN BY AI ##`

)