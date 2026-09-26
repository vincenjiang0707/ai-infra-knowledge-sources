source: https://github.com/vllm-project/guidellm/pull/1153/commits/a314fe9683a4c99066e1a73bd8591449bb2bdfd1

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

# OTeL trace support #1153

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 8 commits into

[vllm-project:main](https://github.com/vllm-project/guidellm/tree/main)

##
*base:*
main

**{{ refName }}**

### Are you sure you want to change the base?

[jaredoconnell:feat/otel-trace-support](https://github.com/jaredoconnell/guidellm/tree/feat/otel-trace-support)

#
[
OTeL trace support
](https://github.com#top)
#1153

##
Changes from **1 commit**

[
Show all changes
8 commits
](https://github.com/vllm-project/guidellm/pull/1153/files)

[
MVP of OTeL Trace Support
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/99b5247aaa37b153ca889e493f188d75517bac98)Sep 11, 2026

`99b5247`

[
Add preceeding_nodes request metric
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/ca08ad452303cbf8f0cbf472bbfeda88ed9042dc)Sep 15, 2026

`ca08ad4`

[
Complete OTel Support
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/f9cde77b686cb49766b237f90aeaf28ca9d73780)Sep 15, 2026

`f9cde77`

[
Remove synthetic option to simplify initial implementation
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/0fb0fbb0d9996bed546de89ae1e6f192427d417f)Sep 16, 2026

`0fb0fbb`

[
Address review comments
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/a314fe9683a4c99066e1a73bd8591449bb2bdfd1)Sep 19, 2026

`a314fe9`

[
Address review comments
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/311a36a6db4ad14938cb9330e6ec08de66e29ccd)Sep 23, 2026

`311a36a`

[
Require inputs needed for each format
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/85b1f47eec27095563b5709e1ddd2c3f838b7422)Sep 23, 2026

`85b1f47`

[
Improve handling of tool calls in OTeL deserializers
jaredoconnell ](https://github.com/vllm-project/guidellm/pull/1153/commits/b5bfce10079172ab1187830052c5fd47278c2a02)Sep 23, 2026

`b5bfce1`

##
**
File filter
**

### Filter by extension

## **Conversations**

## **Jump to**

##### Diff view

##### Diff view

Remove speculative defensive code Document actually needed defensive code Remove responses support for future consideration And more. Assisted-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

- Loading branch information

## There are no files selected for viewing

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

| Original file line number | Diff line number | Diff line change |
|---|---|---|
|
|

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

If we are treating these as full examples they should probably all have constraints set. Also `--data-loader kind=pytorch,samples=2`

should be removed. Also technically a lot of these are setting the default value. Maybe change `time_scale=2.0`

on the `trace_synthetic`

example, remove the split option from WEKA and OTEL.

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

I didn't add too many options to these since they're just basic examples of using huggingface as the data source. I added time scale to the trace synthetic example. I added a constraint.

**dbutenhof**marked this conversation as resolved.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

dbutenhofmarked this conversation as resolved.## Uh oh!

There was an error while loading. Please reload this page.