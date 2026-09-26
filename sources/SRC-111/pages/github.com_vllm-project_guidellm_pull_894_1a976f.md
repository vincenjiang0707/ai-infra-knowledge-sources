source: https://github.com/vllm-project/guidellm/pull/894

# Bump development dependencies - #894

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Plus unlock versions and add tox-uv, which is used in CI. Changes to tox and pre-commit are unlikely to break development asside from the occasional bug or config migration. Unlike pytest, ruff, or mypy which can add and change rules. Signed-off-by: Samuel Monson <smonson@redhat.com>

Pip has supported dependency groups since 25.1 and this is the recommended method for locking dev dependencies over extras since dependency groups are not shipped in wheels. Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Ruff PLC0415 enforces importing in module scope. We already implicitly require this in source code but in tests a lot of late imports have snuck in. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Give instructions for a uv setup and switch to dev group from dev extra. Signed-off-by: Samuel Monson <smonson@redhat.com>

The previous min tox version was too low for some of the features we use. The uv locked tox runner is used in CI to ensure that tox uses the versions locked in `uv.lock`. Since uv-tox is now included in dev dependencies we can set it as the default runner. Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

July 6, 2026 18:55


[sjmonson](https://github.com/sjmonson)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Jul 6, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 6, 2026

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Bump all of the development dependencies and update the pyproject organization.

## Details

See individual commits for details.

## Test Plan

Exercise normal development workflows such as running tests, installing, etc.

## Related Issues

## Use of AI

## git log

commit

773f8b5Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 16:07:22 2026 -0400

commit

29ebff3Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 17:50:49 2026 -0400

commit

6bcfd62Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 17:59:17 2026 -0400

commit

c53f20bAuthor: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 18:16:11 2026 -0400

commit

5b68760Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 18:31:53 2026 -0400

commit

df14443Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 18:36:00 2026 -0400

commit

a54ac5cAuthor: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 19:17:57 2026 -0400

commit

41e7723Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 19:27:58 2026 -0400

commit

57dc068Author: Samuel Monson smonson@redhat.com

Date: Thu Jul 2 19:44:18 2026 -0400

commit

5769726Author: Samuel Monson smonson@redhat.com

Date: Mon Jul 6 14:27:31 2026 -0400

commit

5e1142cAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jul 6 14:43:53 2026 -0400

commit

96b4deaAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jul 6 14:49:18 2026 -0400

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com