source: https://github.com/vllm-project/guidellm/pull/987

# Fix encoded audio sample frame metrics - #987

Merged

Merged

## Conversation

Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>

[fedirz](https://github.com/fedirz)

[force-pushed](https://github.com/vllm-project/guidellm/compare/99a6240a8237b2d7fbc8cae31592b1d72fa9723f..a0e22679e1f0f36e5feb13350194fae9e86f97fc)the fix/985-audio-sample-count branch from

[to](https://github.com/vllm-project/guidellm/commit/99a6240a8237b2d7fbc8cae31592b1d72fa9723f)

`99a6240`


`a0e2267`

[Compare](https://github.com/vllm-project/guidellm/compare/99a6240a8237b2d7fbc8cae31592b1d72fa9723f..a0e22679e1f0f36e5feb13350194fae9e86f97fc)

August 3, 2026 17:38


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 6, 2026

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

[cmiyai](https://github.com/cmiyai)pushed a commit to cmiyai/guidellm that referenced this pull request

Aug 14, 2026

## Summary - report audio_samples as encoded output frames instead of the decoded sample rate - define encoded frame semantics from output rate and decoded duration - add regression coverage for non-one-second and resampled audio - update truncated-audio expectations to reflect encoded frames ## Tests - uv run tox -e tests -- tests/unit/utils/test_audio.py -k reports (2 passed) - uv run tox -e lint-check (passed) - uv run tox -e type-check (passed) - uv run ruff check src/guidellm/utils/audio.py tests/unit/utils/test_audio.py (passed) The complete audio unit module was also attempted. Its real codec tests cannot run on this host because FFmpeg is absent, so TorchCodec cannot load its shared libraries; 9 mock-only tests passed and 16 codec-dependent tests failed during library loading. Fixes[vllm-project#985]--- # git log commit[Author: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> Date: Mon Aug 3 10:37:32 2026 -0700 fix: report encoded audio sample frames Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> --------- Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>]a0e2267

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

## Tests

The complete audio unit module was also attempted. Its real codec tests cannot run on this host because FFmpeg is absent, so TorchCodec cannot load its shared libraries; 9 mock-only tests passed and 16 codec-dependent tests failed during library loading.

Fixes #985

## git log

commit

a0e2267Author: Fedir Zadniprovskyi github.g1k56@simplelogin.com

Date: Mon Aug 3 10:37:32 2026 -0700

Signed-off-by: Fedir Zadniprovskyi github.g1k56@simplelogin.com