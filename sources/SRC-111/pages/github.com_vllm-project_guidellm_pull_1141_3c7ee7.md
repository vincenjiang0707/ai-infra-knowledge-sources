source: https://github.com/vllm-project/guidellm/pull/1141

## Conversation

Contributor

|
Hi |

Report Real-Time Factor (RTF) and its inverse (RTFx) for requests that carry input audio, the standard measures of transcription speed. RTF is end-to-end request latency divided by input audio duration; RTFx is the reciprocal, expressing seconds of audio processed per second of wall-clock time. Requests without input audio yield None rather than zero, so they are excluded from the distributions instead of dragging them toward zero, and text-only benchmarks report no RTF distribution at all. The console table is skipped entirely when no benchmark processed audio. Resolves[vllm-project#833]Signed-off-by: Tazril Ali <tazril.ali@goripples.com>

[Tazril](https://github.com/Tazril)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7d305a9d8a362e7d74152a71b57f860bc3dd3181..d39e424fbf9f0edf4353fc3dc31bc45474c34981)the feature/audio-rtf-metrics branch from

[to](https://github.com/vllm-project/guidellm/commit/7d305a9d8a362e7d74152a71b57f860bc3dd3181)

`7d305a9`


`d39e424`

[Compare](https://github.com/vllm-project/guidellm/compare/7d305a9d8a362e7d74152a71b57f860bc3dd3181..d39e424fbf9f0edf4353fc3dc31bc45474c34981)

September 12, 2026 09:09

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Resolves #833

Reports Real-Time Factor (RTF) and its inverse (RTFx) for requests that carry input audio, the standard measures of transcription speed. RTF is end-to-end request latency divided by input audio duration; RTFx is the reciprocal, expressing seconds of audio processed per second of wall-clock time. Values below 1.0 RTF (above 1.0 RTFx) mean the server is keeping up with real-time audio.

Everything needed was already plumbed through:

`audio_seconds`

is populated on`UsageMetrics`

by the OpenAI and vLLM backends and the data finalizer, and`request_latency`

already exists, so this derives the two ratios from them.## Changes

— adds`GenerativeRequestStats`

`audio_seconds`

,`real_time_factor`

, and`inverse_real_time_factor`

computed fields, following the existing`tokens_per_second`

pattern.— compiles both into distributions, so they appear under`GenerativeAudioMetricsSummary`

`metrics.audio`

in JSON/YAML reports alongside the existing audio data.Console— a Real-Time Factor table that is skipped entirely for workloads without input audio.CSV— RTF/RTFx columns, emitted only when a run carried audio.Docs— both metrics documented in`docs/guides/metrics.md`

.## Design note

`GenerativeMetricsSummary`

is shaped around input/output/total triples, which does not fit a per-request ratio, so RTF and RTFx are plain`StatusDistributionSummary`

fields compiled through a small`_compile_ratio`

helper.That helper returns

`None`

for requests without input audio rather than coercing to`0.0`

as some surrounding metrics do. This matters for mixed workloads: coercing would pull RTF toward zero for every text request and silently report the server as faster than it is. Requests without audio are therefore excluded from the distribution, and a text-only benchmark reports no RTF distribution at all rather than a distribution of zeros. Both behaviours are covered by tests.## Question for maintainers

For streaming and realtime transcription I used

total request latencyas the numerator, on the reading that it is what a user actually waits for. An argument exists for time-to-final-transcript instead. Happy to switch if you prefer the latter — it is a one-line change plus tests.## Testing

`ruff check`

,`ruff format --check`

,`mypy`

over`src/guidellm`

(224 files), and`mdformat`

all clean.`tests/unit/utils/test_audio.py`

could not run locally —`torchcodec`

fails to load its native library on macOS, and those 14 failures reproduce on an unmodified tree. The new metrics were verified against synthetic request stats rather than a live transcription run, so validation against a real audio backend would be worthwhile.## git log

commit

d39e424Author: Tazril Ali tazril.ali@goripples.com

Date: Sat Sep 12 14:36:39 2026 +0530

Signed-off-by: Tazril Ali tazril.ali@goripples.com