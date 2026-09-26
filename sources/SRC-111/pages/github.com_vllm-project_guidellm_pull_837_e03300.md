source: https://github.com/vllm-project/guidellm/pull/837

# Upgrade 0.6 torch dependencies - #837

Merged

Merged

## Conversation

We want to release a GuideLLM container image for RHAI 3.5, supporting full multimodal testing. However, RHAI 3.5 builds torch 2.11.0 and torchcodec 0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11. This upgrade the dependencies. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

Jun 23, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 23, 2026

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge |

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Upgrade torch and torchcodec dependencies for RHAI 3.5 compatibility

## Details

We want to release a GuideLLM container image for RHAI 3.5, supporting full multimodal testing. However, RHAI 3.5 provides torch 2.11.0 and torchcodec 0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11.

This upgrades the dependencies.

## Test Plan

Manually run the audio, image, and video workloads against Qwen/Qwen3-0.6B model (which I had running) as well as Qwen/Qwen3-VL-2B-Instruct (referenced by documentation).

In this case the results (and ultimate success) are interesting but not really the point: it does not appear that the torch/torchcodec package upgrade caused problems in GuideLLM orchestration.

## Related Issues

https://redhat.atlassian.net/browse/AIPCC-16597

## Use of AI

## git log

commit

292f458Author: David Butenhof dbutenho@redhat.com

Date: Tue Jun 23 09:14:27 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com