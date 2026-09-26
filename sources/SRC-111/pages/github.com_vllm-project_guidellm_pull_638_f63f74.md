source: https://github.com/vllm-project/guidellm/pull/638

# Fix HTML on main and disable by default - #638

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c561d97c9d0822d628af97bd14c5880a9ff4a735..e632dc750d1554fa8f074f5eaf2b1000935a8a47)the fix/disable_html branch from

[to](https://github.com/vllm-project/guidellm/commit/c561d97c9d0822d628af97bd14c5880a9ff4a735)

`c561d97`


`e632dc7`

[Compare](https://github.com/vllm-project/guidellm/compare/c561d97c9d0822d628af97bd14c5880a9ff4a735..e632dc750d1554fa8f074f5eaf2b1000935a8a47)

March 16, 2026 20:39


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 16, 2026

[src/guidellm/settings.py](https://github.com/vllm-project/guidellm/pull/638/files/e632dc750d1554fa8f074f5eaf2b1000935a8a47#diff-9e53343eb57495c8164a5448c076b7f3504c652e3e11188963e5b6d8d3a58405)


[dbutenhof](https://github.com/dbutenhof)added the

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Apr 22, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Something I failed to notice during the scramble to get v0.5.4 out is that the HTML CI only generates the new version template on release, so tagging it with the current dev version will not work. Also just remove it from the defaults in preparation for phasing it out entirely.

## Use of AI

`## WRITTEN BY AI ##`

)