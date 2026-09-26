source: https://github.com/vllm-project/guidellm/pull/916

# Add a setting to configure the default working dir - #916

Merged

Merged

## Conversation

Previously it was possible set the output directory for all outputs with a single environment variable. This was removed with the v0.7.0 refactor as now each output manages its own path. However, its still useful to set a default output directory for special environments such as containers where we may want to redirect all outputs to a volume by default. Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

[Containerfile](https://github.com/vllm-project/guidellm/pull/916/files/dd4ed2fbd97b0ce6631ddfcca2b3f7d95a302bfb#diff-5fcdf9b4580789697d834d1456a22bcfaa236d668fc180cad4775afc36ed5914)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 9, 2026

Contributor

|
Queued — the merge queue status continues in |

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7f92482ab6e04ded9504e25529428d06584a8929..48b7cae59bb6f91c2c0569866c7c57733d7a190d)the feat/fallback_wd branch from

[to](https://github.com/vllm-project/guidellm/commit/7f92482ab6e04ded9504e25529428d06584a8929)

`7f92482`


`48b7cae`

[Compare](https://github.com/vllm-project/guidellm/compare/7f92482ab6e04ded9504e25529428d06584a8929..48b7cae59bb6f91c2c0569866c7c57733d7a190d)

July 9, 2026 18:51


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 9, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

The Containerfiles are still using the

`GUIDELLM_OUTPUT_DIR`

environment variable which no longer exists. There is still a valid use-case for having a separate default directory from the current one so this PR adds back that functionality. Individual outputs will still override the path in its entirety.## Use of AI

## git log

commit

be587bcAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 8 13:45:52 2026 -0400

commit

dd4ed2fAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 8 14:07:09 2026 -0400

commit

48b7caeAuthor: Samuel Monson smonson@redhat.com

Date: Thu Jul 9 14:48:59 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com