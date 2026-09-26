source: https://github.com/vllm-project/guidellm/pull/620

# [FEAT] Add replay from trace strategy - #620

[sjmonson](https://github.com/sjmonson)merged 28 commits into

## Conversation

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/008633f59878cbb3d33376aa680dcb99bde3ee57..a66034b2cc3e07c47cf11392b91f5b526d4fe7c7)the add-strategy-replay-from-trace branch from

[to](https://github.com/vllm-project/guidellm/commit/008633f59878cbb3d33376aa680dcb99bde3ee57)

`008633f`


`a66034b`

[Compare](https://github.com/vllm-project/guidellm/compare/008633f59878cbb3d33376aa680dcb99bde3ee57..a66034b2cc3e07c47cf11392b91f5b526d4fe7c7)

March 4, 2026 13:32

|
This pull request has merge conflicts that must be resolved before it can be |

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7f893fb2b8514200eef656fda529c2bdffa47b2d..780be20d971851a2d5817906c2bbb98d828de119)the add-strategy-replay-from-trace branch from

[to](https://github.com/vllm-project/guidellm/commit/7f893fb2b8514200eef656fda529c2bdffa47b2d)

`7f893fb`


`780be20`

[Compare](https://github.com/vllm-project/guidellm/compare/7f893fb2b8514200eef656fda529c2bdffa47b2d..780be20d971851a2d5817906c2bbb98d828de119)

March 18, 2026 13:12

[VincentG1234](https://github.com/VincentG1234)marked this pull request as ready for review

March 18, 2026 13:13

[sjmonson](https://github.com/sjmonson)self-requested a review

March 18, 2026 19:18

|
It will be great to get an example of "How to get the JSONL" because i don't find solutions in litellm for example. |

|
Yeah that’s true, most frameworks won’t produce this exact JSONL directly. That’s kind of intentional. The idea here is to define a minimal, framework-agnostic canonical replay format, not something tied to a specific tracing stack. In practice, the required fields already exist almost everywhere (timestamp, input token count, output token count), just under slightly different names, so a small mapping step is usually enough. I agree it’s not the best UX on its own, but it felt like the right minimal base for the feature. Then we can iterate on top of it with helpers / converters for common sources like LiteLLM or Langfuse. And we can extend it later (e.g. optional prompt field, multiple timestamp formats, richer metadata) without breaking the core idea. But happy to adjust the direction if maintainers prefer something more opinionated or integrated from the start. |


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 17, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Sorry for the silence on this. There are a few things with this PR that break other use-cases. I am still working on a more complete review but here are a few low hanging problems.

[src/guidellm/utils/trace_io.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-1c7c16f7cf3a3fbc51fa0636da71086d0e5c7ca7b7d7f839fec7d063ce84481d)

[src/guidellm/scheduler/__init__.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-0df5d49074c92062b70fda45e56aac9f3e19f02f83a9b04f1758c02abfe688da)Outdated

[src/guidellm/scheduler/__init__.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-0df5d49074c92062b70fda45e56aac9f3e19f02f83a9b04f1758c02abfe688da)Outdated

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

[src/guidellm/utils/trace_io.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-1c7c16f7cf3a3fbc51fa0636da71086d0e5c7ca7b7d7f839fec7d063ce84481d)

[src/guidellm/data/trace_io.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-1f116edd0b920101abb8a5097cb45455b24c59d2fb22392061dc58d28f16e933)Outdated

|
Thanks a lot for the detailed review, I really appreciate your time. I’m fully aligned with your feedback, especially on the replay handling in the entrypoint, which is a key part of the PR. I agree that introducing a special case here is not ideal and should be avoided. I’ll refactor this to make it cleaner and better aligned with the existing design. |

[VincentG1234](https://github.com/VincentG1234)marked this pull request as draft

April 20, 2026 07:49

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/780be20d971851a2d5817906c2bbb98d828de119..7d76d5f62945119a80e2a25765ef9afb6bd31575)the add-strategy-replay-from-trace branch from

[to](https://github.com/vllm-project/guidellm/commit/780be20d971851a2d5817906c2bbb98d828de119)

`780be20`


`7d76d5f`

[Compare](https://github.com/vllm-project/guidellm/compare/780be20d971851a2d5817906c2bbb98d828de119..7d76d5f62945119a80e2a25765ef9afb6bd31575)

April 22, 2026 15:10

[VincentG1234](https://github.com/VincentG1234)marked this pull request as ready for review

April 27, 2026 08:56

|
Hi Thanks again for the feedback. I’ve completed the refactor and addressed the main review points. Key updates:
Would appreciate another look when you have time. Optional: I also put together a small Colab notebook to try the feature quickly if useful: |

[sjmonson](https://github.com/sjmonson)self-requested a review

April 28, 2026 14:09


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Apr 28, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

A couple of comments mostly around documentation consistency...

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/620/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/620/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Apr 29, 2026

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/620/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/620/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e17eb3daf7970a68a5f351a1770091c037b7837a..b6c56f3705d71d1d7c04005a30aabba6b7ad0c02)the add-strategy-replay-from-trace branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/e17eb3daf7970a68a5f351a1770091c037b7837a)

`e17eb3d`


`b6c56f3`

[Compare](https://github.com/vllm-project/guidellm/compare/e17eb3daf7970a68a5f351a1770091c037b7837a..b6c56f3705d71d1d7c04005a30aabba6b7ad0c02)

April 30, 2026 16:30


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 1, 2026

[src/guidellm/utils/trace_io.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-1c7c16f7cf3a3fbc51fa0636da71086d0e5c7ca7b7d7f839fec7d063ce84481d)Outdated

|
I tried running a test with |

Thanks for testing this and for sharing the dataset. I can reproduce the issue on my side as well, including with a smaller subset of the trace. I’ll investigate it and work on a fix as soon as possible. At first glance, this seems related to how replay handles large/bursty traces and high-token-count requests. I’ll follow up once I have a clearer diagnosis and a fix. |

|
Hi First, synthetic prompt generation now builds one reusable base prompt and creates each request prompt by adding a unique prefix before slicing to the requested input length. This keeps prompts cache-resistant while avoiding the previous expensive per-request generation path. Second, trace replay is temporarily limited to one process. With multiple processes, there is currently a race condition where some scheduled requests can be consumed out of order or never sent, which leaves the benchmark waiting forever. Capping replay to one process is a workaround, but it makes the benchmark complete reliably; the only expected limitation is for extreme traces where one scheduling process may become a bottleneck. I tested this with the shared JSONL trace: the benchmark no longer hangs and starts correctly after roughly 50 seconds. On a representative subset, the previous prompt generation path was at least 10x slower... |

Yeah... I don't love this idea, but fine for now. I see the dataset generation as temporary/fallback anyways since what we want longer term is to base the tokens off of the mooncake token ids.
Also works for now. Fixing this requires a way for the dataset to inform on request scheduling so we'll scope something out. |

|
For multiprocessing, I think I may have found a fairly minimal approach that avoids the replay deadlock while keeping the implementation relatively clean, but I agree it’s probably better scoped for a follow-up PR. For the Mooncake token-id direction, unless I miss something, I think the current prefix invalidation approach can remain compatible with a more structure-aware strategy later on. Roughly, unrelated prompts would still receive different invalidating prefixes, while prompts sharing a common prefix could intentionally reuse the same initial invalidating block and only diverge later with unique suffix markers. Example: base prompt: prompt 1: prompt 2 (totally unrelated to prompt 1): prompt 3 (shares the same prefix structure as prompt 2 up to block D): This keeps prompts cache-resistant globally while still allowing controlled shared-prefix behavior between related requests. The same idea could likely be extended recursively for deeper shared-prefix structures. |

|
augment review |

|


**reviewed**

[augmentcode](https://github.com/apps/augmentcode)BotMay 11, 2026

[src/guidellm/benchmark/profiles.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-abcf32987c69e483665371f42096bf49b8d65cf4651c5c95cccac96684119f10)

[src/guidellm/benchmark/profiles.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-abcf32987c69e483665371f42096bf49b8d65cf4651c5c95cccac96684119f10)

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)

[src/guidellm/data/deserializers/trace_synthetic.py](https://github.com/vllm-project/guidellm/pull/620/files#diff-9b3a8fcf26ad7c63c39d01040383973f3dc65cdb632745df7ec15b0ff70b97d3)

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

…les as sole trace row cap Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

…and docs Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

…and docs Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

…generation Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/8a9c700d50087a5cd5d9025d2654c10b1671514e..3084876bae3b451714e55c49d82c2e0ace5983cc)the add-strategy-replay-from-trace branch from

[to](https://github.com/vllm-project/guidellm/commit/8a9c700d50087a5cd5d9025d2654c10b1671514e)

`8a9c700`


`3084876`

[Compare](https://github.com/vllm-project/guidellm/compare/8a9c700d50087a5cd5d9025d2654c10b1671514e..3084876bae3b451714e55c49d82c2e0ace5983cc)

May 18, 2026 15:23


**requested changes**

[sjmonson](https://github.com/sjmonson)May 18, 2026


There was a problem hiding this comment.

Sorry to go back on my approval, but I am still seeing issues with the `data.jsonl`

above. After 15 requests it hangs. Can someone else validate they can run that dataset for at least 100 requests or so.

```
guidellm benchmark \
--data ./data.jsonl \
--data-args type_=trace_synthetic \
--profile replay \
--rate 1000.0 \
--request-format /v1/completions
```

Hello To accelerate the replay and reduce the intervals, it should be something like: `--rate 0.001` The current behavior is a bit counter-intuitive at first glance though. I can also improve the CLI/docs wording to make it clearer that the rate acts as a multiplier on the original intervals. We could also consider inverting the behavior in the future, since people tend to interpret it as a speed-up factor. |

Oh my bad, that's what I get for not rereading the documentation after coming back to this.
Yeah its a little counterintuitive when the option is just |


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 18, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

LGTM, Thanks for being such an attentive contributor!

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 5, 2026

## Summary: Trace replay previously forced single-process execution because timestamps were assigned at dequeue time via a shared `next_request_index()` counter, causing ordering races under multiprocessing ([#620]). This PR sources per-request trace offsets from the dataset pipeline via `RequestSettings.relative_timestamp`, following the design in[#735]. ## Details - `trace_synthetic` deserializer emits a `relative_timestamp` column (offset from the earliest sorted trace event) - `GenerativeColumnMapper` maps it to `relative_timestamp_column` - `GenerativeRequestFinalizer` attaches `RequestSettings` on `GenerationRequest` - `WorkerGroupState` copies `request.settings` into `RequestInfo` at enqueue - Add `resolve_dequeued_target_start()` on `SchedulingStrategy`; trace replay applies `start_time + time_scale * relative_timestamp` at dequeue - `TraceReplayStrategy.next_request_time` returns benchmark start (immediate dequeue) - Remove `processes_limit = 1` on trace replay - `ReplayProfile` keeps `time_scale` only; default `max_requests` derived from trace row count ## Test Plan: - [x] Unit tests pass - [x] Manual trace replay benchmark with `--processes > 1` and verify inter-arrival timing matches the trace ## Related Issues[#735]## - [x] I used an AI coding assistant while working on this PR --- # git log commit[Author: Vincent Gimenes <vincent.gimenes@gmail.com> Date: Fri Jun 5 11:16:54 2026 +0200 Enable multiprocess trace replay via per-request RequestSettings Move trace replay timing from ReplayProfile/TraceReplayStrategy into the dataset pipeline so each request carries its own scheduling metadata: - trace_synthetic deserializer emits a relative_timestamp column (offset from the earliest sorted trace event) - GenerativeColumnMapper maps it to relative_timestamp_column - GenerativeRequestFinalizer attaches RequestSettings on GenerationRequest - WorkerGroupState copies request.settings into RequestInfo at enqueue TraceReplayStrategy no longer holds a global relative_timestamps list. next_request_time schedules dequeue at benchmark start; resolve_dequeued_target_start applies start_time + time_scale * relative_timestamp per request at dequeue. This removes the single-process constraint and enables correct multiprocess trace replay timing. ReplayProfile keeps only time_scale (from rate) and default max_requests when data_samples truncates the dataset. Add integration test exercising the full trace_synthetic → mapper → finalizer → TraceReplayStrategy multiprocess path, plus unit test updates. Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com> --------- Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>]25484a6

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

`replay`

benchmarking strategy that reproduces real-world request patterns from trace log files (.jsonl)`max_requests`

and`max_seconds`

cli options to limit the number of requests processed from a trace## Motivation

This change addresses issue #597 by enabling users to benchmark their vLLM servers using real production traces. Instead of synthetic load patterns, users can now replay exact request arrival times and token distributions from their actual workloads for more realistic performance testing.

## Changes

`TraceReplayStrategy`

scheduler strategy for timestamp-based request dispatching`ReplayProfile`

class for configuring trace-based benchmarking parameters`TraceSyntheticDatasetDeserializer`

to generate prompts matching trace input/output lengths`TraceReader`

utility for reading .jsonl trace files with timestamp, input_length, output_length fields`Entrypoint`

to handle replay profile and dataset configuration`max_requests`

and`max_seconds`

truncation support to limit trace replay length## Testing

`pytest tests/unit/scheduler/test_trace_replay.py`

(pass)`pytest tests/unit/benchmark/test_replay_profile.py`

(pass)`pytest tests/unit/data/deserializers/test_trace_synthetic.py`

(pass)Added tests: scheduling accuracy, boundary conditions, malformed trace handling, empty trace cases, max_requests truncation

test it in practice quickly with NB COLAB

## Next Steps (this PR)

## Out of Scope (future PRs or not)

## Use of AI