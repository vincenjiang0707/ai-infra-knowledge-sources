source: https://github.com/vllm-project/guidellm/pull/897

# Fix explicit fill-value overwrite detection in arg parser - #897

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

[mergify[bot]](https://github.com/mergify[bot]) merged 1 commit into

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

|
Hi |

[harivilasp](https://github.com/harivilasp)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1d81d13f3c5a6a5d6132ed1dc26d303d206137b2..381a5f5bb74dc20c2ffa44110b4dbbaaf20883e9)the fix/arg-string-fill-value-overwrite branch from

[to](https://github.com/vllm-project/guidellm/commit/1d81d13f3c5a6a5d6132ed1dc26d303d206137b2)

`1d81d13`


`381a5f5`

[Compare](https://github.com/vllm-project/guidellm/compare/1d81d13f3c5a6a5d6132ed1dc26d303d206137b2..381a5f5bb74dc20c2ffa44110b4dbbaaf20883e9)

July 6, 2026 01:43


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 6, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

It looks good to me, blocking an overwrite when none is allowed.

|
Queued — the merge queue status continues in |

|
It appears that CI is failing due to a handshake error that appears to be unrelated to your changes. |

Track explicit list assignments separately from sparse fill values so null and custom fill values retain normal overwrite protection. Generated-by: Codex GPT-5 Signed-off-by: harivilasp <harivilasp@gmail.com>

[harivilasp](https://github.com/harivilasp)

[force-pushed](https://github.com/vllm-project/guidellm/compare/381a5f5bb74dc20c2ffa44110b4dbbaaf20883e9..eacde439ba11111645441f3a07b0d73b168e2ffe)the fix/arg-string-fill-value-overwrite branch from

[to](https://github.com/vllm-project/guidellm/commit/381a5f5bb74dc20c2ffa44110b4dbbaaf20883e9)

`381a5f5`


`eacde43`

[Compare](https://github.com/vllm-project/guidellm/compare/381a5f5bb74dc20c2ffa44110b4dbbaaf20883e9..eacde439ba11111645441f3a07b0d73b168e2ffe)

July 7, 2026 19:17

|
|


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This seems to work -- even if the detailed error message isn't getting through the CLI. (Not a problem with this PR, since the "Invalid key=value expression" error for `value:x`

is also getting lost, and we only get a generic "Input should be a valid dictionary or object".)

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

FYI -- that was just because our CI requires two core group approvals to trigger automatic merging. 😁 |

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Prevent the argument-string parser from treating explicitly assigned list values as sparse padding when they equal the configured fill value.

## Details

`null`

values and custom fill values such as`0`

.## Test Plan

`tox -e test-unit -- tests/unit/utils/test_arg_string.py -q`

- 53 passed`tox -q`

-`lint-check`

passed;`type-check`

failed in`.tox/type-check/lib/python3.14/site-packages/numpy/__init__.pyi:737`

with`Type statement is only supported in Python 3.12 and greater`

## Related Issues

## git log

commit

eacde43Author: harivilasp harivilasp@gmail.com

Date: Sun Jul 5 14:02:05 2026 -0700

Generated-by: Codex GPT-5

Signed-off-by: harivilasp harivilasp@gmail.com