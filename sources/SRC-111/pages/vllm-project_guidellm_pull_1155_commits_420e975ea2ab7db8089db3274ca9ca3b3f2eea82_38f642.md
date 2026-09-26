source: https://github.com/vllm-project/guidellm/pull/1155/commits/420e975ea2ab7db8089db3274ca9ca3b3f2eea82

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

#
Implement `copies`

feature for synthetic traces
#1155

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

Open

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 6 commits into

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

[jaredoconnell:feat/synthetic-trace-copies](https://github.com/jaredoconnell/guidellm/tree/feat/synthetic-trace-copies)

Open

##
Changes from **1 commit**

Commits

[
](https://github.com/vllm-project/guidellm/pull/1155/files)

Show all changes

6 commits
Select commit
Hold shift + click to select a range

[
](https://github.com/vllm-project/guidellm/pull/1155/commits/a51227195796bc12e91a9ccd7a9571fe3ece816d)Sep 16, 2026

`a512271`

Implement `copies` feature for synthetic traces

jaredoconnell [
](https://github.com/vllm-project/guidellm/pull/1155/commits/420e975ea2ab7db8089db3274ca9ca3b3f2eea82)Sep 16, 2026

`420e975`

Fix min_concurrent_sessions flattening all requests in trace_synthetic

jaredoconnell [
](https://github.com/vllm-project/guidellm/pull/1155/commits/d9891a47554c480ef2b55ac359652e1233826f32)Sep 19, 2026

`d9891a4`

Preserve relative timestamps of conversations in WEKA traces

jaredoconnell [
](https://github.com/vllm-project/guidellm/pull/1155/commits/e6d896a8dece90d52503e033852e2cb4bae7b773)Sep 19, 2026

`e6d896a`

Add copy offset setting

jaredoconnell [
](https://github.com/vllm-project/guidellm/pull/1155/commits/ccddae13efbafcc8ad629507810fff4f1d192fbb)Sep 19, 2026

`ccddae1`

Address review comments

jaredoconnell [
](https://github.com/vllm-project/guidellm/pull/1155/commits/2654056165bb2e1f945880f98a5bed27cd35e21c)Sep 23, 2026

`2654056`

Address review comments, simplifying code

jaredoconnell ##
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

Fix min_concurrent_sessions flattening all requests in trace_synthetic

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

- Loading branch information

commit 420e975ea2ab7db8089db3274ca9ca3b3f2eea82

## There are no files selected for viewing

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)[20 changes: 20 additions & 0 deletions 20](https://github.com/vllm-project/guidellm/blob/main/CODEOWNERS#L2)

[tests/unit/data/deserializers/test_trace_session_timing.py](https://github.com#diff-05edbd9a070376986a5184a9cde71a6d56838a82778d50c202506c3ef9fc0aa0)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
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

dbutenhofmarked this conversation as resolved.## Uh oh!

There was an error while loading. Please reload this page.