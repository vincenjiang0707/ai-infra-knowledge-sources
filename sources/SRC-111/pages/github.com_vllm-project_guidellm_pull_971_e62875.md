source: https://github.com/vllm-project/guidellm/pull/971

# docs: document the plot output kind - #971

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 5 commits into

Merged

## Conversation

Add plot to the supported output types list and a PLOT entry under Supported File Formats covering the supported image formats (PNG, JPG, SVG, PDF) and the dpi parameter. Signed-off-by: Pragadeesh122 <pragan189@gmail.com>


[dbutenhof](https://github.com/dbutenhof)added

[documentation](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adocumentation)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Jul 28, 2026

[dbutenhof](https://github.com/dbutenhof)self-requested a review

July 28, 2026 11:34


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 28, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Thanks! But a few comments ...

[docs/guides/outputs.md](https://github.com/vllm-project/guidellm/pull/971/files/898ee94d9584f43df7ba2095ad74664438cdd2c3#diff-2d63fdeb0d723a694c00fd52ba668fe90d4f28dcec7f4a5c48e2d635ac32a57c)Outdated

[docs/guides/outputs.md](https://github.com/vllm-project/guidellm/pull/971/files/898ee94d9584f43df7ba2095ad74664438cdd2c3#diff-2d63fdeb0d723a694c00fd52ba668fe90d4f28dcec7f4a5c48e2d635ac32a57c)Outdated

Drop the dpi mention from the output-types summary line (kept in the PLOT bullet) and add a usage example per review. Signed-off-by: Pragadeesh122 <pragan189@gmail.com>

Contributor
Author

|
Thanks |

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 29, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

The

`plot`

output kind shipped without documentation (#969). This documents it in`docs/guides/outputs.md`

.## Details

`plot`

to the "Supported output types" list underCLI Output Configuration, noting that it additionally accepts a`dpi`

parameter.PLOTentry underSupported File Formatscovering the supported image formats (PNG, JPG/JPEG, SVG, PDF), the default-to-`.png`

behavior for a pathless/extension-less output, and the`dpi`

parameter (default`100`

).Details verified against

`src/guidellm/benchmark/outputs/plot.py`

(`_ALLOWED_PLOT_SUFFIXES`

, the`dpi`

field default, and the`validate_plot_suffix`

behavior).## Test Plan

`tox -e lint-check`

passes (mdformat clean).## Related Issues

## git log

commit

6b96c37Author: Pragadeesh122 pragan189@gmail.com

Date: Mon Jul 27 18:19:58 2026 -0500

commit

dcb9a89Author: Pragadeesh122 pragan189@gmail.com

Date: Tue Jul 28 14:15:38 2026 -0500

Signed-off-by: Pragadeesh122 pragan189@gmail.com