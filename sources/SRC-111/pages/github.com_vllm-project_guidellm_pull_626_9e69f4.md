source: https://github.com/vllm-project/guidellm/pull/626

# docs: add documentation for passing sampling parameters via --backend-kwargs - #626

Merged

Merged

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Mar 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

I don't see anything obviously wrong, but I have some suggestions and comments. While waiting for more expert feedback from Sam, I'm going to just post this as "comment" rather than "request changes" for now ...

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This looks ready once the linting errors are fixed. You can run it with

```
python -m mdformat README.md DEVELOPING.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/ src/ tests/
```


…-kwargs Add a new "Passing Sampling Parameters" section to the backends documentation that explains how to pass sampling parameters (temperature, top_p, top_k, etc.) to the backend server using the --backend-kwargs option with the extras.body field. Address review feedback: - Restore llama-server hyperlink - Use GuideLLM (project) vs `guidellm` (CLI) consistently - Add missing article ("the safetensors repository") - Use > [!IMPORTANT] and > [!NOTE] callout syntax Signed-off-by: Yuchen Fama <yuchengu@gmail.com> Made-with: Cursor


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 10, 2026

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files/8a5c3842398fca911c8f4cb2a0b704d7b9612270#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated

[docs/guides/backends.md](https://github.com/vllm-project/guidellm/pull/626/files/8a5c3842398fca911c8f4cb2a0b704d7b9612270#diff-9e22ffdf136f548e3af2454c52bf60d001f3f83a5258b17529a7d0353ba3af78)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 11, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Looks good ... but it needs another rebase.

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Yuchen Fama <yuchengu@gmail.com>

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Yuchen Fama <yuchengu@gmail.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 12, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Thanks ... the notes are rendering correctly now. If the CI passes (and GitHub Actions seem to be backed up ...) I think we'll be good to go.


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 12, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Add a new "Passing Sampling Parameters" section to

`docs/guides/backends.md`

that documents how to pass sampling parameters (e.g.,`temperature`

,`top_p`

,`top_k`

) to the backend server via the`--backend-kwargs`

CLI option.This is a common source of confusion for users, as the correct syntax requires nesting sampling parameters under

`extras.body`

(i.e.,`--backend-kwargs '{"extras": {"body": {"temperature": 0.6}}}'`

) rather than passing them directly as top-level backend arguments.## Details

Added a new

`## Passing Sampling Parameters`

section to`docs/guides/backends.md`

`extras.body`

field structure for passing sampling parameters`temperature`

,`top_p`

, and`top_k`

usage`GenerationRequestArguments`

sub-fields (`body`

,`headers`

,`params`

)`api_key`

`--backend-args`

is a legacy alias for`--backend-kwargs`

## Test Plan

Documentation-only change; no functional code changes

## Related Issues