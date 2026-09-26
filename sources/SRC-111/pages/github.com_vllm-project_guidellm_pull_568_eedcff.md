source: https://github.com/vllm-project/guidellm/pull/568

# Add multimodal benchmarking usage docs - #568

Merged

Merged

## Conversation

Signed-off-by: Mark Kurtz <mark.kurtz@neuralmagic.com>

Signed-off-by: Mark Kurtz <mark.kurtz@neuralmagic.com>

Signed-off-by: michelia <michelia@seal.io> Signed-off-by: Mark Kurtz <mark.kurtz@neuralmagic.com>

[markurtz](https://github.com/markurtz)

[force-pushed](https://github.com/vllm-project/guidellm/compare/125b659257bb4581765a568d51da8a57c6825342..2d7503b68e8d9264d5792b5cd145c3a1e88f7c77)the features/docs-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/125b659257bb4581765a568d51da8a57c6825342)

`125b659`


`2d7503b`

[Compare](https://github.com/vllm-project/guidellm/compare/125b659257bb4581765a568d51da8a57c6825342..2d7503b68e8d9264d5792b5cd145c3a1e88f7c77)

January 30, 2026 15:37

###
**
**[Copilot](https://github.com/apps/copilot-pull-request-reviewer)
AI
left a comment

**left a comment**

[Copilot](https://github.com/apps/copilot-pull-request-reviewer)AI
Contributor


There was a problem hiding this comment.

## Pull request overview

This PR adds documentation for benchmarking multimodal models (image, video, and audio) with GuideLLM using OpenAI-compatible endpoints, and links these guides into the broader docs navigation.

**Changes:**

- Added dedicated guides for image, video, and audio benchmarking, covering setup, data loading, request formatting, metrics, and example
`guidellm benchmark`

commands. - Introduced a multimodal benchmarking index page that explains prerequisites and links to each modality-specific guide.
- Updated the main Guides index to surface the new multimodal benchmarking docs.

### Reviewed changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 5 comments.

## Show a summary per file

| File | Description |
|---|---|
`docs/guides/multimodal/image.md` |
New guide for benchmarking vision-language models with image inputs, including data-column mapping, request formatting, metrics, and VQA/captioning examples. |
`docs/guides/multimodal/video.md` |
New guide for benchmarking video-language models with video inputs, including data loading, video request formatting, metrics, and QA/captioning examples. |
`docs/guides/multimodal/audio.md` |
New guide for benchmarking audio models for ASR, translation, and audio chat, with detailed encoder options, metrics, and three example benchmark commands. |
`docs/guides/multimodal/index.md` |
New multimodal overview page describing prerequisites and linking to image, video, and audio benchmarking guides. |
`docs/guides/index.md` |
Adds a “Multimodal Benchmarking” card that links the main Guides index to the new multimodal documentation. |

💡 [Add Copilot custom instructions](https://github.com/vllm-project/guidellm/new/main/.github/instructions?filename=*.instructions.md) for smarter, more guided reviews. [Learn how to get started](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/0bc91791041e8e168f4c608d36111a2a78b0dfd1#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)Outdated

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/0bc91791041e8e168f4c608d36111a2a78b0dfd1#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)Outdated

[docs/guides/multimodal/index.md](https://github.com/vllm-project/guidellm/pull/568/files/0bc91791041e8e168f4c608d36111a2a78b0dfd1#diff-821bf1c34ff37e7bd45a5b32af26bb2ac7fe4a48aa9339def92ca4cb54821e11)Outdated

[docs/guides/multimodal/image.md](https://github.com/vllm-project/guidellm/pull/568/files/0bc91791041e8e168f4c608d36111a2a78b0dfd1#diff-ea5312b9bc94da6fc9c861c14719d56147c3024d95e07cda6e41cdd06c844341)Outdated

[docs/guides/multimodal/video.md](https://github.com/vllm-project/guidellm/pull/568/files/0bc91791041e8e168f4c608d36111a2a78b0dfd1#diff-cc87975f18b72eb0905aa3098a253a31c8d5cdecff1e2b390214da3e746d6b4f)Outdated

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>


**reviewed**

[sjmonson](https://github.com/sjmonson)Jan 30, 2026

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)


**requested changes**

[sjmonson](https://github.com/sjmonson)Jan 30, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Overall just a few nits around explaining arguments. There is also a lot of redundancy around explaining column mapping, output files, etc that would possible be better to have dedicated docs for with backlinks, but we can address that in a future PR.

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)Outdated

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)Outdated

[docs/guides/multimodal/image.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-ea5312b9bc94da6fc9c861c14719d56147c3024d95e07cda6e41cdd06c844341)

[docs/guides/multimodal/audio.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-211a7cddeb62ad15e4989cecc17526419622efd7c8acfa247f811a1047c7c5fc)

[docs/guides/multimodal/video.md](https://github.com/vllm-project/guidellm/pull/568/files/df169747680082f4b32ab221e197cee590a14a54#diff-cc87975f18b72eb0905aa3098a253a31c8d5cdecff1e2b390214da3e746d6b4f)Outdated

Co-authored-by: Samuel Monson <smonson@redhat.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Samuel Monson <smonson@redhat.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Samuel Monson <smonson@redhat.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Samuel Monson <smonson@redhat.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>

Co-authored-by: Samuel Monson <smonson@redhat.com> Signed-off-by: Mark Kurtz <mark.j.kurtz@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jan 30, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR adds documentation for benchmarking multimodal models (image, video, and audio) with GuideLLM using OpenAI-compatible endpoints, and links these guides into the broader docs navigation.

## Details

## Test Plan

## Use of AI

`## WRITTEN BY AI ##`

)