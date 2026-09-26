source: https://github.com/vllm-project/guidellm/pull/745

# Enable multiprocessing support for trace replay strategy - #745

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5fbe5f50ab81f206e058e8d9d77f2858f47678ca..9383101260c06b96d386b82ccabaeed8a35c107d)the trace-replay-multiprocess branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/5fbe5f50ab81f206e058e8d9d77f2858f47678ca)

`5fbe5f5`


`9383101`

[Compare](https://github.com/vllm-project/guidellm/compare/5fbe5f50ab81f206e058e8d9d77f2858f47678ca..9383101260c06b96d386b82ccabaeed8a35c107d)

May 31, 2026 10:10

[VincentG1234](https://github.com/VincentG1234)marked this pull request as ready for review

May 31, 2026 10:11


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 1, 2026

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/745/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/745/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/745/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9383101260c06b96d386b82ccabaeed8a35c107d..85c2f48a7aea594c3a6c2970606086c60ffd8d68)the trace-replay-multiprocess branch from

[to](https://github.com/vllm-project/guidellm/commit/9383101260c06b96d386b82ccabaeed8a35c107d)

`9383101`


`85c2f48`

[Compare](https://github.com/vllm-project/guidellm/compare/9383101260c06b96d386b82ccabaeed8a35c107d..85c2f48a7aea594c3a6c2970606086c60ffd8d68)

June 4, 2026 18:20

Move trace replay timing from ReplayProfile/TraceReplayStrategy into the dataset pipeline so each request carries its own scheduling metadata: - trace_synthetic deserializer emits a relative_timestamp column (offset from the earliest sorted trace event) - GenerativeColumnMapper maps it to relative_timestamp_column - GenerativeRequestFinalizer attaches RequestSettings on GenerationRequest - WorkerGroupState copies request.settings into RequestInfo at enqueue TraceReplayStrategy no longer holds a global relative_timestamps list. next_request_time schedules dequeue at benchmark start; resolve_dequeued_target_start applies start_time + time_scale * relative_timestamp per request at dequeue. This removes the single-process constraint and enables correct multiprocess trace replay timing. ReplayProfile keeps only time_scale (from rate) and default max_requests when data_samples truncates the dataset. Add integration test exercising the full trace_synthetic → mapper → finalizer → TraceReplayStrategy multiprocess path, plus unit test updates. Signed-off-by: Vincent Gimenes <vincent.gimenes@gmail.com>

[VincentG1234](https://github.com/VincentG1234)

[force-pushed](https://github.com/vllm-project/guidellm/compare/85c2f48a7aea594c3a6c2970606086c60ffd8d68..25484a64d8afc95d7467074b2ac235c448c35f10)the trace-replay-multiprocess branch from

[to](https://github.com/vllm-project/guidellm/commit/85c2f48a7aea594c3a6c2970606086c60ffd8d68)

`85c2f48`


`25484a6`

[Compare](https://github.com/vllm-project/guidellm/compare/85c2f48a7aea594c3a6c2970606086c60ffd8d68..25484a64d8afc95d7467074b2ac235c448c35f10)

June 5, 2026 10:58


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 5, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Looks good and seems to run with no issues!

###
**
**[Copilot](https://github.com/apps/copilot-pull-request-reviewer)
AI
left a comment

**left a comment**

[Copilot](https://github.com/apps/copilot-pull-request-reviewer)AI

There was a problem hiding this comment.

## Pull request overview

This PR enables multiprocess execution for the trace replay scheduling strategy by moving per-request timing data into the dataset pipeline (`RequestSettings.relative_timestamp`

) and resolving the effective scheduled start time at dequeue, eliminating the prior shared counter race that forced single-process replay.

**Changes:**

- Add
`RequestSettings`

and propagate it from dataset finalizers →`GenerationRequest`

→`RequestInfo`

at enqueue time. - Introduce
`SchedulingStrategy.resolve_dequeued_target_start()`

and update`TraceReplayStrategy`

to compute`start_time + time_scale * relative_timestamp`

per request at dequeue. - Update trace synthetic deserialization/mapping to emit and map a
`relative_timestamp`

column; add/adjust unit and integration tests for the new multiprocess replay path.

### Reviewed changes

Copilot reviewed 16 out of 16 changed files in this pull request and generated 3 comments.

## Show a summary per file

| File | Description |
|---|---|
| tests/unit/scheduler/test_trace_replay.py | Updates trace replay strategy unit tests for the new dequeue-time resolution behavior and removal of single-process limit. |
| tests/unit/data/test_finalizers.py | Adds unit coverage ensuring `relative_timestamp_column` becomes `GenerationRequest.settings` . |
| tests/unit/data/deserializers/test_trace_synthetic.py | Adds coverage that trace_synthetic emits sorted per-row `relative_timestamp` . |
| tests/unit/benchmark/test_replay_profile.py | Updates replay profile tests to reflect removal of stored timestamp lists and default `max_requests` behavior. |
| tests/integration/scheduler/test_trace_replay_multiprocess.py | Adds integration test exercising the end-to-end dataset → settings → multiprocess trace replay scheduling behavior. |
| src/guidellm/schemas/request.py | Adds `settings: RequestSettings` to `GenerationRequest` for per-request scheduling metadata. |
| src/guidellm/schemas/info.py | Introduces `RequestSettings` and attaches it to `RequestInfo` (with deep-copy support). |
src/guidellm/schemas/init.py |
Exports `RequestSettings` from the schemas package. |
| src/guidellm/scheduler/worker.py | Applies dequeue-time target start resolution and uses the effective start time for scheduling. |
| src/guidellm/scheduler/worker_group.py | Copies per-request settings into `RequestInfo` during enqueue. |
| src/guidellm/scheduler/strategies.py | Adds the `resolve_dequeued_target_start()` hook and updates `TraceReplayStrategy` implementation accordingly. |
| src/guidellm/data/schemas/base.py | Adds `relative_timestamp_column` to the known dataset column names list. |
| src/guidellm/data/preprocessors/mappers.py | Maps dataset `relative_timestamp` → `relative_timestamp_column` . |
| src/guidellm/data/finalizers/generative.py | Finalizer now derives `RequestSettings` from `relative_timestamp_column` . |
| src/guidellm/data/deserializers/trace_synthetic.py | Emits `relative_timestamp` per row (offset from earliest sorted timestamp). |
| src/guidellm/benchmark/profiles/replay.py | Removes strategy-held timestamp list; keeps `time_scale` and derives default `max_requests` from trace row count. |

💡 [Add Copilot custom instructions](https://github.com/vllm-project/guidellm/new/main?filename=.github/instructions/*.instructions.md) for smarter, more guided reviews. [Learn how to get started](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/745/files/25484a64d8afc95d7467074b2ac235c448c35f10#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/745/files/25484a64d8afc95d7467074b2ac235c448c35f10#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)

[src/guidellm/schemas/info.py](https://github.com/vllm-project/guidellm/pull/745/files/25484a64d8afc95d7467074b2ac235c448c35f10#diff-179053f40e2947d9c41d6c3d78a225bdb58b06d99bc62c0a3bcad6e15c19adda)

|
^ Sorry missclick |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 5, 2026

## Merge Queue Status
This pull request spent
|


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 5, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

This seems like a good solution to get trace working for now. We'll need do a larger refactor later for more advanced trace formats that have more advanced requirements. One downside of this design is everything gets queued at the same time, which could be a problem for large datasets, but it would take some work to fix that without concurrency problems.

[src/guidellm/schemas/request.py](https://github.com/vllm-project/guidellm/pull/745/files/25484a64d8afc95d7467074b2ac235c448c35f10#diff-9257f47eca60528ee4d982b23ddd3a59847b18591b36768dccd41bc1cb1cb3d0)

|
Looks like e2e tests broke temporarily. |

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary:

Trace replay previously forced single-process execution because timestamps were assigned at dequeue time via a shared

`next_request_index()`

counter, causing ordering races under multiprocessing (#620). This PR sources per-request trace offsets from the dataset pipeline via`RequestSettings.relative_timestamp`

, following thedesign in #735.

## Details

`trace_synthetic`

deserializer emits a`relative_timestamp`

column (offset fromthe earliest sorted trace event)

`GenerativeColumnMapper`

maps it to`relative_timestamp_column`

`GenerativeRequestFinalizer`

attaches`RequestSettings`

on`GenerationRequest`

`WorkerGroupState`

copies`request.settings`

into`RequestInfo`

at enqueue`resolve_dequeued_target_start()`

on`SchedulingStrategy`

; trace replayapplies

`start_time + time_scale * relative_timestamp`

at dequeue`TraceReplayStrategy.next_request_time`

returns benchmark start (immediate dequeue)`processes_limit = 1`

on trace replay`ReplayProfile`

keeps`time_scale`

only; default`max_requests`

derived from trace row count## Test Plan:

`--processes > 1`

and verify inter-arrival timing matches the trace## Related Issues

#735

## git log

commit

25484a6Author: Vincent Gimenes vincent.gimenes@gmail.com

Date: Fri Jun 5 11:16:54 2026 +0200

Signed-off-by: Vincent Gimenes vincent.gimenes@gmail.com