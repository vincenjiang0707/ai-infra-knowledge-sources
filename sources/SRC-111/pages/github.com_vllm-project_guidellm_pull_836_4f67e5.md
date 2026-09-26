source: https://github.com/vllm-project/guidellm/pull/836

# Remove "rate" as an alias for profile parameters - #836

Merged

Merged

## Conversation

We no longer have a global --rate, so no further purpose is served by allowing the name "rate" as an alias for "streams", "max_concurrency", and "sweep_size" in the relevant profiles. Remove the alias, and with it the "adapter" validators that allowed applying rate lists to scalar parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jun 23, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 23, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

Remove the "rate" alias for profile parameters. The profiles that used to process the global `--rate` value (async, concurrent, replay, sweep, throughput) accepted "rate" as an alias for the native internal parameter, and those which don't accept lists mapped from the rate list to a single value. Now that the global `--rate` option no longer exists, this logic has no value. We remove it, accepting only the "native" parameter, and letting Pydantic handle validation errors if a user attempts to pass a list for a scalar value. (For convenience, we still map a specified scalar into a list for async and concurrent profiles.) - [x] Unit tests - [x] Integration tests - [x] e2e tests - [x] Assorted manual test runs N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 23 08:42:04 2026 -0400 Remove "rate" as an alias for profile parameters We no longer have a global --rate, so no further purpose is served by allowing the name "rate" as an alias for "streams", "max_concurrency", and "sweep_size" in the relevant profiles. Remove the alias, and with it the "adapter" validators that allowed applying rate lists to scalar parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]1ae1ddc

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

Remove the "rate" alias for profile parameters. The profiles that used to process the global `--rate` value (async, concurrent, replay, sweep, throughput) accepted "rate" as an alias for the native internal parameter, and those which don't accept lists mapped from the rate list to a single value. Now that the global `--rate` option no longer exists, this logic has no value. We remove it, accepting only the "native" parameter, and letting Pydantic handle validation errors if a user attempts to pass a list for a scalar value. (For convenience, we still map a specified scalar into a list for async and concurrent profiles.) - [x] Unit tests - [x] Integration tests - [x] e2e tests - [x] Assorted manual test runs N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 23 08:42:04 2026 -0400 Remove "rate" as an alias for profile parameters We no longer have a global --rate, so no further purpose is served by allowing the name "rate" as an alias for "streams", "max_concurrency", and "sweep_size" in the relevant profiles. Remove the alias, and with it the "adapter" validators that allowed applying rate lists to scalar parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]1ae1ddc

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Remove the "rate" alias for profile parameters. ## Details The profiles that used to process the global `--rate` value (async, concurrent, replay, sweep, throughput) accepted "rate" as an alias for the native internal parameter, and those which don't accept lists mapped from the rate list to a single value. Now that the global `--rate` option no longer exists, this logic has no value. We remove it, accepting only the "native" parameter, and letting Pydantic handle validation errors if a user attempts to pass a list for a scalar value. (For convenience, we still map a specified scalar into a list for async and concurrent profiles.) ## Test Plan - [x] Unit tests - [x] Integration tests - [x] e2e tests - [x] Assorted manual test runs ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 23 08:42:04 2026 -0400 Remove "rate" as an alias for profile parameters We no longer have a global --rate, so no further purpose is served by allowing the name "rate" as an alias for "streams", "max_concurrency", and "sweep_size" in the relevant profiles. Remove the alias, and with it the "adapter" validators that allowed applying rate lists to scalar parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]1ae1ddc

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Remove the "rate" alias for profile parameters.

## Details

The profiles that used to process the global

`--rate`

value (async, concurrent, replay, sweep, throughput) accepted "rate" as an alias for the native internal parameter, and those which don't accept lists mapped from the rate list to a single value.Now that the global

`--rate`

option no longer exists, this logic has no value. We remove it, accepting only the "native" parameter, and letting Pydantic handle validation errors if a user attempts to pass a list for a scalar value. (For convenience, we still map a specified scalar into a list for async and concurrent profiles.)## Test Plan

## Related Issues

N/A

## Use of AI

Assisted-by: Cursor

## git log

commit

1ae1ddcAuthor: David Butenhof dbutenho@redhat.com

Date: Tue Jun 23 08:42:04 2026 -0400

Assisted-by: Cursor

Signed-off-by: David Butenhof dbutenho@redhat.com