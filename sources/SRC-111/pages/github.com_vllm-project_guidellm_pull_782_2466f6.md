source: https://github.com/vllm-project/guidellm/pull/782

# Fix unpicklable lambda collate_fn in TorchDataLoader for Python 3.14 - #782

Merged

Merged

## Conversation

Python 3.14 changed the default multiprocessing start method on Linux to forkserver, which requires DataLoader worker arguments to be picklable. The lambda batch: batch[0] passed as collate_fn is not picklable, causing a PicklingError at runtime. Replace it with a module-level _collate_first function. Signed-off-by: Radoslav Gerganov <rgerganov@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 8, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 8, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

Jun 8, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Python 3.14 changed the default multiprocessing start method on Linux to forkserver, which requires DataLoader worker arguments to be picklable. The lambda batch: batch[0] passed as collate_fn is not picklable, causing a PicklingError at runtime. Replace it with a module-level _collate_first function.

## Details

This is a regression introduced with recent CLI refactoring

## Use of AI

## git log

commit

3d285dbAuthor: Radoslav Gerganov rgerganov@gmail.com

Date: Mon Jun 8 16:07:33 2026 +0300

Signed-off-by: Radoslav Gerganov rgerganov@gmail.com