source: https://github.com/vllm-project/guidellm/pull/1018

# fix: keep GHCR latest/stable as multi-arch manifests - #1018

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 2 commits into

Merged

[mergify[bot]](https://github.com/mergify[bot]) merged 2 commits into

[mergify[bot]](https://github.com/mergify[bot])merged 2 commits into

## Conversation

Contributor

|
Hi |

Stop weekly retag from selecting arch-specific tags (e.g. vX.Y.Z-arm64) and use skopeo --all so latest/stable stay amd64+arm64 for Docker/K8s/OpenShift. Signed-off-by: AmitChaubey <amit.katyayana@gmail.com>

[amit-chaubey](https://github.com/amit-chaubey)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1e5b5977669ad2bdfb86a0c21b106ce79210bd69..8d8c6ebeda79a200787265f515f6bd68f227ef5c)the fix/ghcr-latest-stable-multiarch branch from

[to](https://github.com/vllm-project/guidellm/commit/1e5b5977669ad2bdfb86a0c21b106ce79210bd69)

`1e5b597`


`8d8c6eb`

[Compare](https://github.com/vllm-project/guidellm/compare/1e5b5977669ad2bdfb86a0c21b106ce79210bd69..8d8c6ebeda79a200787265f515f6bd68f227ef5c)

August 11, 2026 15:02


**requested changes**

[sjmonson](https://github.com/sjmonson)Aug 11, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Overall seems reasonable with a gripe about the tests.

[scripts/test_container_image_tags.sh](https://github.com/vllm-project/guidellm/pull/1018/files/8d8c6ebeda79a200787265f515f6bd68f227ef5c#diff-cd6741c0db8eb75188608882fd057d9231372f669bc1f3d532411e62d867ba09)Outdated

[.github/workflows/container-maintenance.yml](https://github.com/vllm-project/guidellm/pull/1018/files/8d8c6ebeda79a200787265f515f6bd68f227ef5c#diff-703f180d9c5e736ded0faf78a036f354ff7d5d7f1a8219b362aa7d1db1d94f7c)Outdated

Remove standalone tag-selection test script and restore concurrency whitespace in container-maintenance workflow. Signed-off-by: AmitChaubey <amit.katyayana@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 11, 2026

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

Contributor
Author

|
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Stop weekly retag from selecting arch-specific tags (e.g.

`vX.Y.Z-arm64`

) and use`skopeo --all`

so`latest`

/`stable`

stay amd64+arm64 for Docker/K8s/OpenShift.## Summary

`ghcr.io/vllm-project/guidellm:latest`

was ending up as a single-arch arm64 image, which causes`Exec format error`

on linux/amd64 hosts (including OpenShift). The weekly Container Image Maintenance workflow selected arch-specific tags like`v0.7.0-arm64`

for`:latest`

, and plain`skopeo copy`

flattened multi-arch indexes when retagging`:stable`

/`:latest`

. This PR fixes tag selection, preserves full multi-arch manifests, adds a CI verification gate, and documents supported tags/platforms in the README.## Details

`*-amd64`

,`*-arm64`

) when choosing sources for`:stable`

and`:latest`

`skopeo copy --all`

so multi-arch indexes are preserved during retag`linux/amd64`

+`linux/arm64`

) before/after retag`scripts/container_image_tags.sh`

and local tests in`scripts/test_container_image_tags.sh`

`README.md`

## Test Plan

`./scripts/test_container_image_tags.sh`

(unit cases + live GHCR inspect)Container Image Maintenance(`workflow_dispatch`

) to heal live`:latest`

/`:stable`

`docker buildx imagetools inspect ghcr.io/vllm-project/guidellm:latest`

shows both`linux/amd64`

and`linux/arm64`

`:latest`

on an amd64 node (and arm64 if available)## Related Issues

## Use of AI

## git log

commit

8d8c6ebAuthor: AmitChaubey amit.katyayana@gmail.com

Date: Tue Aug 11 14:50:56 2026 +0100

commit

39dfeffAuthor: AmitChaubey amit.katyayana@gmail.com

Date: Tue Aug 11 16:34:51 2026 +0100

Signed-off-by: AmitChaubey amit.katyayana@gmail.com