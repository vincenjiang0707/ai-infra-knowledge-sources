source: https://github.com/vllm-project/guidellm/pull/800/commits/1bad39c7d2c8b95ce6ea51cccebe4662fdbd6f46

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

# feat: add LiteLLM backend for multi-provider benchmarking #800

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

Open

[RheagalFire](https://github.com/RheagalFire)wants to merge 3 commits into

[vllm-project:main](https://github.com/vllm-project/guidellm/tree/main)

##
*base:*
main

Could not load branches

Branch not found:

**{{ refName }}**
Loading

Could not load tags

Nothing to show

Loading

### Are you sure you want to change the base?

Some commits from the old base branch may be removed from the timeline,
and old review comments may become outdated.

[RheagalFire:feat/add-litellm-provider](https://github.com/RheagalFire/guidellm/tree/feat/add-litellm-provider)

Open

##
Changes from **1 commit**

Commits

[
](https://github.com/vllm-project/guidellm/pull/800/files)

Show all changes

3 commits
Select commit
Hold shift + click to select a range

##
**
File filter
**

### Filter by extension

## **Conversations**

Failed to load comments.

Loading

## **Jump to**

Jump to file

Failed to load files.

Loading

##### Diff view

##### Diff view

fix: raise litellm minimum to 1.83, remove upper cap, regen lockfile

- Bump minimum litellm version to >=1.83.0 (post supply-chain fix) - Remove <1.87.0 upper bound to allow latest releases - Regenerate uv.lock via tox run -e lock - Fix ruff formatting issues Signed-off-by: Aarish Alam <arishalam121@gmail.com>

- Loading branch information

commit 1bad39c7d2c8b95ce6ea51cccebe4662fdbd6f46


Some comments aren't visible on the classic Files Changed page.

## There are no files selected for viewing

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| Original file line number | Diff line number | Diff line change |
|---|---|---|
|
|

Comment on lines
+260
to
+263

Collaborator

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

We discourage the use of `getattr`

. Have you looked into statically typing `chunk`

so that you can avoid `getattr`

? The type appears to be `ModelResponseStream`

.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
Oops, something went wrong.

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.

jaredoconnellThere was a problem hiding this comment.

## Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. Learn more.

Have you verified that we only need the messages from the format output? Looking it looks like ChatCompletionsRequestHandler.format() builds a full body (e.g. max_completion_tokens / ignore_eos from request.output_metrics.text_tokens, tools, etc.), but only messages are passed into litellm.acompletion(). The rest appears to end up in arguments.model_dump_json() for GenerationResponse.request_args. Can you confirm whether those body fields are intentionally not forwarded, or if request-level output token limits should also be sent to LiteLLM?