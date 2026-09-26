source: https://github.com/vllm-project/guidellm/pull/681

# Remove "uv" ecosystem from yaml - #681

Merged

Merged

## Conversation

dependabot is now suggesting all package upgrades, and we really only want automated security updates: we'll decide when to update verions via a separate process not just based on "availability". It appears there's no entirely clear/reliable way to do that except from the GitHub advanced security UI, and it appears that defining the `github-actions` ecosystem behavior in the yaml file won't affect the existing UI configuration for other ecosystems; so try just removing the `uv` ecosystem configuration... Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

Apr 1, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 1, 2026


[dbutenhof](https://github.com/dbutenhof)added the

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Apr 7, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

dependabot is now suggesting all possible package upgrades, when we really only want automated security updates: we'll decide when to update versions via a separate process not just based on "availability".

## Details

It appears there's no entirely clear/reliable way to do that except from the GitHub advanced security UI, and it appears that defining the

`github-actions`

ecosystem behavior in the yaml file won't affect the existing UI configuration for other ecosystems; so try just removing the`uv`

ecosystem configuration...## Test Plan

Merge and wait ...

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)