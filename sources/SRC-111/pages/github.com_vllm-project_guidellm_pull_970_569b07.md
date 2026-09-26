source: https://github.com/vllm-project/guidellm/pull/970

# Prevent .env files from tainting tests - #970

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 28, 2026

Contributor

|
Queued — the merge queue status continues in |

Collaborator

|
Maybe we should just disable |

Collaborator
Author

I find it useful for always setting the two settings that I need; one to make it so multiprocessing works on mac, and the other to enable debug logging. |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 28, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This is a follow up to #751. I discovered that .env files were not addressed by my prior fix.

## Details

## Test Plan

Just run the tests normally and with a .env file that includes values that cause problems with the tests, like

`GUIDELLM__LOGGING__CONSOLE_LOG_LEVEL=DEBUG`

## Related Issues

## Use of AI

## git log

commit

0acbbb4Author: Jared O'Connell joconnel@redhat.com

Date: Mon Jul 27 17:46:08 2026 -0400

Signed-off-by: Jared O'Connell joconnel@redhat.com