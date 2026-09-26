source: https://github.com/vllm-project/guidellm/pull/605

# Feat/cross rate early exit - #605

[mergify[bot]](https://github.com/mergify[bot])merged 9 commits into

## Conversation

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/0d2a43485e058c2c5586f37f5e00fe975af6c665..069838317e2bab5e7ada99094dd716390b40d645)the feat/cross-rate-early-exit branch from

[to](https://github.com/vllm-project/guidellm/commit/0d2a43485e058c2c5586f37f5e00fe975af6c665)

`0d2a434`


`0698383`

[Compare](https://github.com/vllm-project/guidellm/compare/0d2a43485e058c2c5586f37f5e00fe975af6c665..069838317e2bab5e7ada99094dd716390b40d645)

February 23, 2026 14:27

[sjmonson](https://github.com/sjmonson)self-requested a review

February 23, 2026 18:37

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ed54a859a62869a49f8cecfae4fbe2d66238ce8e..6ffc31d745cd6ded98a889e1ec81ed255e639c9d)the feat/cross-rate-early-exit branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/ed54a859a62869a49f8cecfae4fbe2d66238ce8e)

`ed54a85`


`6ffc31d`

[Compare](https://github.com/vllm-project/guidellm/compare/ed54a859a62869a49f8cecfae4fbe2d66238ce8e..6ffc31d745cd6ded98a889e1ec81ed255e639c9d)

February 24, 2026 15:07

|
You can do this by running: |

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6ef8cff9c79ad687cf9dc67a4a6df8b9ea4fd630..634455dfc3b86d9485e03041b461bd5b5aebfc23)the feat/cross-rate-early-exit branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/6ef8cff9c79ad687cf9dc67a4a6df8b9ea4fd630)

`6ef8cff`


`634455d`

[Compare](https://github.com/vllm-project/guidellm/compare/6ef8cff9c79ad687cf9dc67a4a6df8b9ea4fd630..634455dfc3b86d9485e03041b461bd5b5aebfc23)

June 29, 2026 10:38


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 29, 2026

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/sweep.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-41c2a462a880cdf989ca6946e5a6a4b34ffb5cd28dd583a2d0bf9d00b566f5ad)Outdated

[README.md](https://github.com/vllm-project/guidellm/pull/605/files#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)Outdated

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/871d39a4f7db2a9bf53258b5a4f9f1941f043e4b..f9758df15bdb3701f58e4ef4ba7fda1074443221)the feat/cross-rate-early-exit branch from

[to](https://github.com/vllm-project/guidellm/commit/871d39a4f7db2a9bf53258b5a4f9f1941f043e4b)

`871d39a`


`f9758df`

[Compare](https://github.com/vllm-project/guidellm/compare/871d39a4f7db2a9bf53258b5a4f9f1941f043e4b..f9758df15bdb3701f58e4ef4ba7fda1074443221)

July 2, 2026 13:31


**requested changes**

[sjmonson](https://github.com/sjmonson)Jul 7, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Comments below are copies of the feedback I left over slack. Regarding `stop_all`

I think we need a new field, maybe `stopping_scope: Literal["current", "all"]`

ideally this is defined on `ConstraintArgs`

and not the scheduler state but in order to guarantee you are mapping to the correct constraint it might have to be in both places. In which case each constraint should pass its value of `stopping_scope`

from its `ConstraintArgs`

into the scheduler state it maintains.

[src/guidellm/benchmark/profiles/asynchronous.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-5e2311a4fbd8afc3bb3cf7f32311b7144d5a067f46506309dbaa6a2ca73aa3c8)Outdated

[src/guidellm/benchmark/profiles/concurrent.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-669b161868bd7dc88be40e19fbb46f6657669d8c2745c889cd4cb5d62266f237)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

| if action.request_processing == "stop_all": | ||
| logger.info( | ||
| f"Stopping rate escalation: constraint '{name}' " | ||
| f"triggered (request_processing=stop_all)" | ||
| ) |

There was a problem hiding this comment.

stop_all is not for stopping all benchmarks, its for stopping all distributed processes in a multi-node benchmark. We still plan to support that so stop_all cannot be hijacked for this.

There was a problem hiding this comment.

Fixed — added stopping_scope field on ConstraintArgs (defaults to "current"), propagated to SchedulerUpdateAction. _should_stop_escalating now checks that instead of stop_all.

[src/guidellm/benchmark/profiles/sweep.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-41c2a462a880cdf989ca6946e5a6a4b34ffb5cd28dd583a2d0bf9d00b566f5ad)

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/f9758df15bdb3701f58e4ef4ba7fda1074443221..96f0e3e005cadb4d440b4da3f066bdb2bcb88cda)the feat/cross-rate-early-exit branch from

[to](https://github.com/vllm-project/guidellm/commit/f9758df15bdb3701f58e4ef4ba7fda1074443221)

`f9758df`


`96f0e3e`

[Compare](https://github.com/vllm-project/guidellm/compare/f9758df15bdb3701f58e4ef4ba7fda1074443221..96f0e3e005cadb4d440b4da3f066bdb2bcb88cda)

July 8, 2026 09:49

|
Thanks Implemented stopping_scope on ConstraintArgs as suggested, propagated to SchedulerUpdateAction. All constraint types pass it through, default is "current". Removed rate/stream sorting — user order is preserved. When stopping_scope="all" is configured, ascending order is validated at profile construction. |


**requested changes**

[sjmonson](https://github.com/sjmonson)Jul 8, 2026

[src/guidellm/benchmark/profiles/concurrent.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-669b161868bd7dc88be40e19fbb46f6657669d8c2745c889cd4cb5d62266f237)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This sounds like a good idea. Although there's a voice in the back of my head with a weird concern about arbitrarily sorting the rate/streams list ... I also can't convince myself there's any reasonable motivation for requiring an out-of-order list.

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/605/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[src/guidellm/benchmark/profiles/asynchronous.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-5e2311a4fbd8afc3bb3cf7f32311b7144d5a067f46506309dbaa6a2ca73aa3c8)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/605/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

|
Thanks |

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/605/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Tested and works for me

|
Tick the box to add this pull request to the merge queue (same as
|

When running multiple rates (constant, poisson, concurrent profiles) or sweeping, stop escalating to higher rates if a failure constraint (over-saturation, max errors, error rate) triggers at a lower rate. - Sort rates/streams ascending in AsyncProfile and ConcurrentProfile - Add _should_stop_escalating() on base Profile class using stop_all as the failure signal (vs stop_local for normal completions) - Skip failure check after throughput phase in SweepProfile since over-saturation is expected at maximum load - Log warning when rate order is changed by sorting - Update CLI help and README with multi-rate documentation - Add comprehensive unit tests for all profile types Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

- Simplify _should_stop_escalating param docstring (not a precondition) - Consolidate sweep.py early-exit comments into one clear block - Revert README multi-rate sentence, move docs to getting-started/benchmark.md - Add early-exit behavior notes to Concurrent, Constant, Poisson, Sweep sections Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

|
Tick the box to add this pull request to the merge queue (same as
|

|
Queued — the merge queue status continues in |


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 14, 2026


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 14, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Just a minor nitpick in constraints/saturation.py. Otherwise, all seems to be working for me.

[src/guidellm/scheduler/constraints/saturation.py](https://github.com/vllm-project/guidellm/pull/605/files/1e429538e22d77b2ac94d1a86d40982a9987edf5#diff-79ab5e822d3d7f17056f07ceb5ac0412f153eca36d177dc644f007f31a276eee)

Co-authored-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Signed-off-by: Uri Shaket <ushaket@redhat.com>

|
Linter is complaining. That's on me, the trailing docstring |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 14, 2026

|
|

## Merge Queue Status
This pull request spent
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 14, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This PR adds cross-rate early-exit behavior for multi-rate benchmark profiles so benchmarks stop escalating once a terminal failure condition is hit at a lower rate/stream. It also makes rate/stream ordering deterministic (ascending) and updates user-facing docs/help text to reflect multi-rate semantics and skip behavior.

## Details

`request_processing=stop_all`

) from the previous benchmark state.`AsyncProfile.next_strategy()`

to stop scheduling higher rates after a terminal failure; continue normally on`stop_local`

.`ConcurrentProfile.next_strategy()`

with the same early-exit behavior for stream escalation.`SweepProfile.next_strategy()`

so`synchronous`

and`throughput`

always run, with early-exit applied only during async-rate continuation.`--rate`

semantics, multi-value behavior, and failure-triggered skipping.`stop_local`

)`stop_all`

)## Test Plan

`pytest tests/unit/benchmark/test_profiles.py`

`pytest tests/unit/benchmark -k profile`

`guidellm benchmark ... --profile constant --rate 1 --rate 5 --rate 10`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)## git log

commit

577e1b9Author: Uri Shaket ushaket@redhat.com

Date: Sun Feb 15 13:56:30 2026 +0200

commit

db62346Author: Uri Shaket ushaket@redhat.com

Date: Mon Jun 29 16:40:30 2026 +0300

commit

3789518Author: Uri Shaket ushaket@redhat.com

Date: Wed Jul 8 12:46:36 2026 +0300

commit

95b52fdAuthor: Uri Shaket ushaket@redhat.com

Date: Wed Jul 8 13:34:14 2026 +0300

commit

d98ba5dAuthor: Uri Shaket ushaket@redhat.com

Date: Thu Jul 9 20:49:15 2026 +0300

commit

1e42953Author: Uri Shaket ushaket@redhat.com

Date: Sun Jul 12 10:37:56 2026 +0300

commit

3a3a847Author: Uri Shaket ushaket@redhat.com

Date: Tue Jul 14 20:40:28 2026 +0300

commit

d058ff2Author: Uri Shaket ushaket@redhat.com

Date: Tue Jul 14 21:00:02 2026 +0300

commit

ce09cdaAuthor: Uri Shaket ushaket@redhat.com

Date: Tue Jul 14 21:03:52 2026 +0300

Co-authored-by: Cursor cursoragent@cursor.com

Co-authored-by: SkiHatDuckie 63932363+SkiHatDuckie@users.noreply.github.com

Signed-off-by: Uri Shaket ushaket@redhat.com