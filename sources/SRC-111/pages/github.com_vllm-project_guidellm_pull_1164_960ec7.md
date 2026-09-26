source: https://github.com/vllm-project/guidellm/pull/1164

# feat(docs): add Chinese translation pilot - #1164

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

|
Hi |

Signed-off-by: tangming1996 <ming.tang@daocloud.io> Assisted-by: Codex GPT-5

[tangming1996](https://github.com/tangming1996)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d6963ce80a04e74700ca7294cfec32f087b518bc..a346155202ccfde39aa236614af026a0ef1bbec3)the codex/docs-i18n-pilot branch from

[to](https://github.com/vllm-project/guidellm/commit/d6963ce80a04e74700ca7294cfec32f087b518bc)

`d6963ce`


`a346155`

[Compare](https://github.com/vllm-project/guidellm/compare/d6963ce80a04e74700ca7294cfec32f087b518bc..a346155202ccfde39aa236614af026a0ef1bbec3)

September 20, 2026 03:05


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 21, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Seems like a good start. I used Codex to compare the Chinese and English versions and it didn't find any major differences. In the future it would be nice to have a shared skill which makes that process easier.

The one thing I don't love how the Chinese documentation is nested under the English docs so I looked around and found [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/) which seems great but has some problem with our docs which is probably caused by another plugin. Though there is the question of if we switch to another docs system due to all of the [drama in mkdocs right now](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/). For now I am approving and we can address some of that later.

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I don't love the nesting, either; but the point was to avoid changing the existing infrastructure, and in the short term that makes sense. I'd also tried some Google translate checks on the Chinese text, and it looks fine. It'll be more interesting to see how Google Translate does on our more technical details as we get further into this project... 😁

I was a little concerned about the fixed `.translation-sources.json`

and its implications, which is why I didn't approve earlier. But I do kinda like the automatic detection that the translation is out of date with changed English source, and recording the SHA is a straightforward way to manage that under human supervision.

So, sure ... this may not be the best permanent solution or organization, but it's a good start.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This PR introduces a minimal Simplified Chinese documentation pilot for GuideLLM. It translates the documentation homepage and installation guide, adds page-aware language switching, and introduces automated source-drift detection so translations cannot silently become outdated.

The implementation is intentionally limited in scope. It validates the internationalization workflow and its maintenance cost without requiring the entire documentation site to be translated or blocking changes to the canonical English documentation.

## Details

`docs/zh/`

.`zh-CN`

when viewing translated pages.`docs/zh/.translation-sources.json`

to map translated pages to their canonical English sources.The design addresses the primary maintenance risks of translated documentation:

## Test Plan

Run the translation metadata validation:

Run the translation validator unit tests:

Run the repository lint checks:

Build the documentation site:

Validate the language-switcher JavaScript:

Manually verify in the generated documentation site:

the English homepage switches to the Chinese homepage;

the English installation page switches to the Chinese installation page;

translated pages switch back to their corresponding English pages;

untranslated English pages fall back to the Chinese homepage;

Chinese pages use lang="zh-CN";

versioned Mike paths are preserved by the language selector;

a stale translation displays a warning linking to the latest English source.

Validation completed locally:

## Related Issues

## Use of AI

The implementation and tests were developed with AI assistance and were manually reviewed and validated using the test plan above.

## git log

commit

a346155Author: tangming1996 ming.tang@daocloud.io

Date: Sun Sep 20 10:48:45 2026 +0800

Assisted-by: Codex GPT-5

Signed-off-by: tangming1996 ming.tang@daocloud.io