source: https://github.com/vllm-project/guidellm/pull/729

## Conversation

Contributor

|
This pull request has merge conflicts that must be resolved before it can be |

[sjarvie](https://github.com/sjarvie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/02902219f9fd6915952834fda4295c58b4acce42..27886059afe5a11cc3d017a73d0ba773b7c7e789)the worktree-multi-image-benchmark branch from

[to](https://github.com/vllm-project/guidellm/commit/02902219f9fd6915952834fda4295c58b4acce42)

`0290221`


`2788605`

[Compare](https://github.com/vllm-project/guidellm/compare/02902219f9fd6915952834fda4295c58b4acce42..27886059afe5a11cc3d017a73d0ba773b7c7e789)

May 21, 2026 22:21

Contributor

|
This pull request has merge conflicts that must be resolved before it can be |

[sjmonson](https://github.com/sjmonson)self-requested a review

May 27, 2026 15:26

Contributor

|
Hi |

Implement multi-image benchmarking for vision-language models to measure latency impact of multiple frames per request. Changes: - MultiImageDatasetConfig schema for datasets with N images per request - 720p image generator with base64 encoding and reproducible seeding - CLI parameter: --images-per-request (single or comma-separated list) - MultiImageBenchmark programmatic API for pytest integration - 14 unit tests covering config validation and image generation - Documentation with usage examples The feature enables benchmarking how TTFT and ITL scale with increasing frame counts, useful for video analysis pipelines.

[sjarvie](https://github.com/sjarvie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/27886059afe5a11cc3d017a73d0ba773b7c7e789..a0510f30e9ab27d9313625ae1135a5d50e9b3f9e)the worktree-multi-image-benchmark branch from

[to](https://github.com/vllm-project/guidellm/commit/27886059afe5a11cc3d017a73d0ba773b7c7e789)

`2788605`


`a0510f3`

[Compare](https://github.com/vllm-project/guidellm/compare/27886059afe5a11cc3d017a73d0ba773b7c7e789..a0510f30e9ab27d9313625ae1135a5d50e9b3f9e)

June 14, 2026 23:49

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Add benchmarking capability to measure latency impact of multiple images (frames) per request in GuideLLM. This enables testing how TTFT and ITL scale with multi-frame vision inputs.

Schema: New`MultiImageDatasetConfig`

extending synthetic data generation with images_per_request parameterGenerator: 720p synthetic image generation with base64 encoding and reproducible seedingCLI: New`--images-per-request`

parameter supporting single or comma-separated values (e.g.,`1,2,5`

)API:`MultiImageBenchmark`

programmatic class for pytest integration## Test Plan

## Implementation Details

Files Created:`src/guidellm/data/schemas.py`

— MultiImageDatasetConfig`src/guidellm/data/generators/multi_image.py`

— Image generator (720p)`src/guidellm/data/generators/__init__.py`

— Module exports`src/guidellm/benchmark/multi_image.py`

— Programmatic API`tests/unit/data/test_multi_image_config.py`

— Config validation tests`tests/unit/data/generators/test_multi_image_generator.py`

— Generator testsFiles Modified:`src/guidellm/data/deserializers/synthetic.py`

— MultiImageDatasetConfig support`src/guidellm/cli/benchmark/run.py`

— CLI parameter`src/guidellm/benchmark/__init__.py`

— API exports`docs/getting-started/benchmark.md`

— Usage guide with examples## Usage Examples

CLI (single image count):CLI (multi-variant):Programmatic:## git log

commit

a0510f3Author: shanejarvie shane@specter.co

Date: Thu May 21 15:04:23 2026 -0700