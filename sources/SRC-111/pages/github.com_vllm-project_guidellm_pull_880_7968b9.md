source: https://github.com/vllm-project/guidellm/pull/880

# Update documentation for `--override`

- #880

Merged

Merged

## Conversation

Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[documentation](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adocumentation)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jul 2, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)Jul 2, 2026

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/880/files/5d63487bd242f31824bfaf428dac776bacd456d2#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 2, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 2, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good. Though it may make sense to include a complete command example somewhere.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Documentation for `--override` was missing from v0.7.0. ## Details Our documentation didn't clearly cover the use of `--override profile.<key>` to specify multiple profile strategy "rates", and v0.7.0 deliberately didn't mention `--override constraint[<n>].<key>`. Remedy this for v0.7.1, which implements the constraint override. ## Test Plan N/A ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Thu Jul 2 08:09:43 2026 -0400 Update documentation for `--override` Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]5d63487[Author: David Butenhof <dbutenho@redhat.com> Date: Thu Jul 2 10:56:42 2026 -0400 Fix throughput Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>]3ef210e

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Documentation for

`--override`

was missing from v0.7.0.## Details

Our documentation didn't clearly cover the use of

`--override profile.<key>`

to specify multiple profile strategy "rates", and v0.7.0 deliberately didn't mention`--override constraint[<n>].<key>`

. Remedy this for v0.7.1, which implements the constraint override.## Test Plan

N/A

## Related Issues

N/A

## Use of AI

Assisted-by: Cursor

## git log

commit

5d63487Author: David Butenhof dbutenho@redhat.com

Date: Thu Jul 2 08:09:43 2026 -0400

commit

3ef210eAuthor: David Butenhof dbutenho@redhat.com

Date: Thu Jul 2 10:56:42 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com