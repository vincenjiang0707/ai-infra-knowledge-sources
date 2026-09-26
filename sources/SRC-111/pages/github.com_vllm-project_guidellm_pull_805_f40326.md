source: https://github.com/vllm-project/guidellm/pull/805

# Disable reloading parent schemas by default - #805

Merged

Merged

## Conversation

`ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 17, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

That simple?

Tests failed with 429 ... I retriggered the unit tests, but apparently the e2e job wasn't actually complete yet.

Collaborator
Author

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

Collaborator

|
I'm glad it was simple. Thanks for fixing this. |

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

## Summary `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. ## Details Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 16:47:21 2026 -0400 Disable reloading parent schemas by default `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]b424c98

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

## Summary `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. ## Details Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 16:47:21 2026 -0400 Disable reloading parent schemas by default `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]b424c98

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. ## Details Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 16:47:21 2026 -0400 Disable reloading parent schemas by default `ReloadableBaseModel` instances will walk the entire list of `ReloadableBaseModel` and `StandardBaseModel` subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method. Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date `reload_schema()` or `model_rebuild(force=True)` must be called on the parents after all child schema changes have been made. Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]b424c98

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

`ReloadableBaseModel`

instances will walk the entire list of`ReloadableBaseModel`

and`StandardBaseModel`

subclasses to check if any depend on the instance. This is slow and expensive so disable by default until we can find a better method.## Details

Disabling this means that the order of imports matter when generating model schemas. To ensure that parents of reloadable models are fully up to date

`reload_schema()`

or`model_rebuild(force=True)`

must be called on the parents after all child schema changes have been made.## Use of AI

## git log

commit

b424c98Author: Samuel Monson smonson@redhat.com

Date: Wed Jun 17 16:47:21 2026 -0400

Assisted-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com