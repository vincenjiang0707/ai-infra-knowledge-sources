source: https://github.com/vllm-project/guidellm/pull/578

# Fix multiple main CI failures - #578

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Feb 2, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

The mdformat version changes check out ... I wish there was a practical way to avoid duplicating the version dependencies between the two files, but I'm not familiar with the capabilities of the precommit YAML...

(OK ... looks like there's actually a [sync-with-uv](https://pypi.org/project/sync-with-uv/) hook for pre-commit that *will* sync with `pyproject.toml`

dependencies. I wonder if that'd work here ... but I won't even suggest experimenting with that for this PR. 😆 Might be fun to try later...)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixes two separate problems with CI that are causing failures on

`main`

and PRs.## Details

`apt`

is used to install`ffmpeg`

without calling`apt update`

. The runner repo cache has now desyned enough that this is causing a package download failure.## Test Plan

CI should pass

## Use of AI

`## WRITTEN BY AI ##`

)