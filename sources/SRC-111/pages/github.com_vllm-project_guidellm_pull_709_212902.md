source: https://github.com/vllm-project/guidellm/pull/709

# Checks for no valid requests in processed dataset - #709

Merged

Merged

## Conversation

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e0d76410625a4872c8865baa6ac8c23267cfba9e..b4424c88cf7bb5956965a979282222ca1b2e8422)the fix/dataset-fixes branch from

[to](https://github.com/vllm-project/guidellm/commit/e0d76410625a4872c8865baa6ac8c23267cfba9e)

`e0d7641`


`b4424c8`

[Compare](https://github.com/vllm-project/guidellm/compare/e0d76410625a4872c8865baa6ac8c23267cfba9e..b4424c88cf7bb5956965a979282222ca1b2e8422)

April 28, 2026 20:37


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Apr 28, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 28, 2026

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)Outdated

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)Outdated

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Apr 29, 2026

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

See my new comments above.


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 1, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

My concerns are resolved. Leaving the comments open that [@dbutenhof](https://github.com/dbutenhof) added to in-case any of those still need to be addressed.


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 1, 2026

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/709/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)

This scenario would previously cause a deadlock on pending. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7e4e9aa7a5505a74a886f946cfd9c8f0364e6389..8ce61968765556001dc3e2145a56fd4f72430354)the fix/dataset-fixes branch from

[to](https://github.com/vllm-project/guidellm/commit/7e4e9aa7a5505a74a886f946cfd9c8f0364e6389)

`7e4e9aa`


`8ce6196`

[Compare](https://github.com/vllm-project/guidellm/compare/7e4e9aa7a5505a74a886f946cfd9c8f0364e6389..8ce61968765556001dc3e2145a56fd4f72430354)

May 5, 2026 15:06

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds warnings and errors so that problems in the datasets are visible, rather than silently failing.

In main, if the dataset isn't processed correctly, GuideLLM deadlocks while the datasets are pending.

## Details

## Test Plan

Currently, due to the other bugs, this command triggers the problem:

## Use of AI

`## WRITTEN BY AI ##`

)