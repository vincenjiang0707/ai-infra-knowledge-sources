source: https://github.com/vllm-project/guidellm/pull/900

# Fix safe_add sign handling for the first value - #900

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Contributor

|
Hi |

Signed-off-by: harivilasp <harivilasp@gmail.com>

[harivilasp](https://github.com/harivilasp)

[force-pushed](https://github.com/vllm-project/guidellm/compare/11361d20ffa151f882a2c2f05e78f6b265e04235..77ad69631d845f235d12f224a8d20903fde48bc1)the fix/safe-add-first-sign branch from

[to](https://github.com/vllm-project/guidellm/commit/11361d20ffa151f882a2c2f05e78f6b265e04235)

`11361d2`


`77ad696`

[Compare](https://github.com/vllm-project/guidellm/compare/11361d20ffa151f882a2c2f05e78f6b265e04235..77ad69631d845f235d12f224a8d20903fde48bc1)

July 6, 2026 01:22

Contributor
Author

resolved |

Contributor
Author

|
|

Contributor

## ☑️ Command disallowed due to
|


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 6, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

The code change looks good. I'm a little curious how this was found; so far as I can see, the function isn't actually *used* except in unit tests. 😁

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixes

`safe_add`

so the first value respects`signs[0]`

instead of always being added as positive.## Details

`safe_add`

.## Test Plan

`uv run pytest tests/unit/utils/test_functions.py -q`

`uv run ruff check`

`uv run ruff format --check --diff`

`uv run mypy --check-untyped-defs src/guidellm`

`uv run pre-commit run --all-files`

## Validation

`pytest`

on`tests/unit/utils/test_functions.py`

passed with`40 passed`

.`ruff check`

passed.`ruff format --check --diff`

passed.`mypy --check-untyped-defs src/guidellm`

passed.`pre-commit run --all-files`

passed.## Related Issues

## git log

commit

77ad696Author: harivilasp harivilasp@gmail.com

Date: Sun Jul 5 18:19:50 2026 -0700

Signed-off-by: harivilasp harivilasp@gmail.com