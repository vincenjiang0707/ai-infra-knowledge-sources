source: https://github.com/vllm-project/guidellm/pull/569

# Replace various key=value string parsers with a single utility - #569

Merged

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2cb80bd0a70fb8166b248d6cf46ac80e64e1d583..5d724ce5b5c1a4ce157708210a647141f96a46ff)the feat/arg_parser branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/2cb80bd0a70fb8166b248d6cf46ac80e64e1d583)

`2cb80bd`


`5d724ce`

[Compare](https://github.com/vllm-project/guidellm/compare/2cb80bd0a70fb8166b248d6cf46ac80e64e1d583..5d724ce5b5c1a4ce157708210a647141f96a46ff)

April 15, 2026 17:00

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/f21b3f0be7517e8c61cac78468b4a4fb463bd409..55745f22673fd26731b6eda88f92c067ef51e459)the feat/arg_parser branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/f21b3f0be7517e8c61cac78468b4a4fb463bd409)

`f21b3f0`


`55745f2`

[Compare](https://github.com/vllm-project/guidellm/compare/f21b3f0be7517e8c61cac78468b4a4fb463bd409..55745f22673fd26731b6eda88f92c067ef51e459)

April 29, 2026 18:20

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 5, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Minor comments from a first pass without getting deep into the algorithms ... but it looks good.

[src/guidellm/data/config.py](https://github.com/vllm-project/guidellm/pull/569/files#diff-05f6fabf037b3138ac60d681c8cd90cb5aef4716d48e67d2f97888886c3e7e7f)

[src/guidellm/utils/arg_string.py](https://github.com/vllm-project/guidellm/pull/569/files#diff-22db3b4a51c0951f3af03c4a9cf04aaf25dec193303f3318a308985be24a350b)Outdated

[src/guidellm/utils/arg_string.py](https://github.com/vllm-project/guidellm/pull/569/files#diff-22db3b4a51c0951f3af03c4a9cf04aaf25dec193303f3318a308985be24a350b)Outdated

[src/guidellm/utils/arg_string.py](https://github.com/vllm-project/guidellm/pull/569/files#diff-22db3b4a51c0951f3af03c4a9cf04aaf25dec193303f3318a308985be24a350b)

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

May 5, 2026 18:48

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 5, 2026

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 6, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good to me. And basic data args are working for me.

Collaborator

|
A test is failing. It looks like maybe you changed the error message under that condition. |

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

This looks great. Minor issue: you added the external get/set methods in the arg string parser class, which aren't used, and aren't tested. If we're going to have them, they should be tested.

[src/guidellm/utils/arg_string.py](https://github.com/vllm-project/guidellm/pull/569/files/23cb0ee6c209e5d16938470f85015ae351475652#diff-22db3b4a51c0951f3af03c4a9cf04aaf25dec193303f3318a308985be24a350b)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Replaces various config string handlers with a new

`ArgString`

format.## Details

Replaces the dataset config parser with a more advance "arg_string" parser with support for nested and list config structures. For example:

Renders to

Also added some glue logic to allow this format anywhere on the CLI that supports JSON. This code should be considered temporary as it will mostly be replaced through the rest of the CLI refactor.

Also open to suggestions for a better name then "arg_string"; a 2-4 letter acronym like JSON or YAML would be good.

## Test Plan

The following benchmark should run without errors and have ~384 ISL per request (make sure to check startup logs confirm

`backend-kwargs`

and`warmup`

are configured):## Use of AI

`## WRITTEN BY AI ##`

)