source: https://github.com/vllm-project/guidellm/pull/534

# Added option to log errors from backends - #534

Merged

[sjmonson](https://github.com/sjmonson)merged 5 commits into

Merged

## Conversation

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jan 16, 2026

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/534/files/2abae0ae0b73864667c7eebdc898110b86bce22e#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jan 16, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

I've found that it would be a lot more convenient to see the backend's errors in the logs for several tasks I've done.

This simply adds an environment variable to enable this logging.

## Details

## Test Plan

Run a benchmark with failing requests with the environment variable set to true. The errors should print out to the console.

## Use of AI

`## WRITTEN BY AI ##`

)