source: https://github.com/vllm-project/guidellm/pull/1042

# Pull pending requests into a worker only when a consumer is waiting - #1042

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

[himanshu1573](https://github.com/himanshu1573)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a23942f49885544d3792fd683e11c6d6801dd9c9..a409fa9e5f3518e5cf0ae3b5b29f4e54a3e44acc)the fix/worker-receive-on-demand branch from

[to](https://github.com/vllm-project/guidellm/commit/a23942f49885544d3792fd683e11c6d6801dd9c9)

`a23942f`


`a409fa9`

[Compare](https://github.com/vllm-project/guidellm/compare/a23942f49885544d3792fd683e11c6d6801dd9c9..a409fa9e5f3518e5cf0ae3b5b29f4e54a3e44acc)

August 24, 2026 17:39

[himanshu1573](https://github.com/himanshu1573)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a409fa9e5f3518e5cf0ae3b5b29f4e54a3e44acc..df47d21092a63b8b62aeb5b283367e0d0e1a468a)the fix/worker-receive-on-demand branch from

[to](https://github.com/vllm-project/guidellm/commit/a409fa9e5f3518e5cf0ae3b5b29f4e54a3e44acc)

`a409fa9`


`df47d21`

[Compare](https://github.com/vllm-project/guidellm/compare/a409fa9e5f3518e5cf0ae3b5b29f4e54a3e44acc..df47d21092a63b8b62aeb5b283367e0d0e1a468a)

August 24, 2026 17:48

|
I'll need to runs some tests on this before we can consider merging. High concurrency (500 to 2000 conc) + max duration constraint is a higher priority for us than this max_requests == conc use-case and I am worried eliminating buffering will cause issues. |

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Aug 24, 2026

## Summary Every request handled by worker **0** is reported with `scheduler_node_id == -1` instead of `0` ([#1043]). The three assignments in `src/guidellm/scheduler/worker.py` use `self.messaging.worker_index or -1`. The `or -1` is meant as a fallback for `worker_index is None`, but `0` is falsy too, so the first worker's index is replaced by the "unknown" sentinel. This corrupts the per-worker view of the benchmark output that you need when debugging scheduling behaviour (I hit it while working on[#1041]/[#1042]). ## Details - `_prepare_node`, and both loops in `_cancel_requests_loop`, now use the worker's own `self.worker_index` (an `int` that is always set in `__init__` and already used for `strategy.next_request_time(worker_index=self.worker_index)`), so no `None` fallback is needed at these sites. - Regression test `TestWorkerProcessMultiturn::test_worker_index_zero_reported_as_scheduler_node_id` builds a worker with `worker_index=0` and checks `scheduler_node_id == 0` on both the dequeue path and the cancel path. ## Test Plan - Regression test fails on `main` (`AssertionError: assert -1 == 0`) and passes with this change. - `python -m pytest tests/unit/scheduler/test_worker.py -q` → 11 passed, 12 xfailed (main: 10 passed, 12 xfailed; the xfails are pre-existing). - `ruff check` / `ruff format --check` on both files: clean. - `mypy --check-untyped-defs src/guidellm/scheduler/worker.py`: no issues. ## Related Issues - Resolves[#1043]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent Code and test were produced with Claude Code under my direction and review; the commit carries the `Generated-by:` trailer. 🤖 Generated with [Claude Code]([https://claude.com/claude-code]) --- # git log commit[Author: Himanshu Prajapati <himanshuprajapati15072003@gmail.com> Date: Mon Aug 24 23:10:57 2026 +0530 Report worker 0 correctly in RequestInfo.scheduler_node_id `self.messaging.worker_index or -1` treats worker index 0 as missing because 0 is falsy, so every request handled by the first worker was reported with the -1 "unknown" sentinel. Use the worker's own `self.worker_index`, which is always set, at the three sites. Adds a regression test covering both the dequeue path (_prepare_node) and the cancel path (_cancel_requests_loop) for worker 0. Fixes]2132b89[#1043]Generated-by: Claude Code Co-Authored-By: Claude <noreply@anthropic.com> Signed-off-by: Himanshu Prajapati <himanshuprajapati15072003@gmail.com> --------- Co-Authored-By: Claude <noreply@anthropic.com> Generated-by: Claude Code Signed-off-by: Himanshu Prajapati <himanshuprajapati15072003@gmail.com>

With multiple worker processes, a worker's messaging receive thread pulled from the shared pending queue unconditionally: one item into its local receive buffer (size 1) and, when that was full, a second one held in the thread while it retried the put. A worker whose async_limit slots were all busy therefore still removed two extra requests from the shared queue, and idle workers could not start them. In a burst with max_concurrency == max_requests this left a few requests waiting on a busy worker while other workers had free slots. Gate the worker-side pull on real demand: get()/get_sync() register a waiting consumer (a counter plus a threading.Event) and the receive thread only takes from the shared queue when more consumers are waiting than items are buffered. While there is no demand it blocks on the event (poll_interval as the backstop) instead of polling, and only counts toward the stop condition once shutdown_event is set, so stop() still terminates the thread. Because Queue.get(timeout) holds the queue's read lock while it polls, a worker waiting on a momentarily empty shared queue blocks the others; use a shorter timeout for the worker-side get to keep that window small. Adds a regression test that fails on main: a worker copy with no consumer must not take messages off the shared pending queue. Fixes[vllm-project#1041]Generated-by: Claude Code Co-Authored-By: Claude <noreply@anthropic.com> Signed-off-by: Himanshu Prajapati <himanshuprajapati15072003@gmail.com>

[himanshu1573](https://github.com/himanshu1573)

[force-pushed](https://github.com/vllm-project/guidellm/compare/df47d21092a63b8b62aeb5b283367e0d0e1a468a..2f23fd70c8ea6ce319909e435ea3a4b3fd56601d)the fix/worker-receive-on-demand branch from

[to](https://github.com/vllm-project/guidellm/commit/df47d21092a63b8b62aeb5b283367e0d0e1a468a)

`df47d21`


`2f23fd7`

[Compare](https://github.com/vllm-project/guidellm/compare/df47d21092a63b8b62aeb5b283367e0d0e1a468a..2f23fd70c8ea6ce319909e435ea3a4b3fd56601d)

August 24, 2026 19:39

|
Thanks — that's a fair concern, so I measured it rather than argue it. Summary: the first version of this PR did cost CPU (a 1 ms idle poll), so I've replaced it with an event-driven wake-up; with that, throughput and in-flight concurrency at 500–2000 +
completed req/s |
451.7 |
453.3 |
1803.7 |
1802.4 |
mean in-flight |
486.9 |
486.0 |
1848 |
1845 |
peak in-flight |
500 |
500 |
2000 |
2000 |
worker-tree CPU (avg) |
105% |
97% |
246% |
228% |
Burst case (
Happy to run any other configuration you'd like to see, or to adjust the approach if you'd prefer a different trade-off. ## benchmark script```
"""Scheduler-only benchmark: real WorkerProcessGroup + messaging, in-process mock backend, no HTTP.
usage: sched_bench.py <max_concurrency> <duration_s> <response_delay_s>
"""
from __future__ import annotations
import asyncio, json, sys, time, uuid
from typing import Any
from pydantic import BaseModel, Field
from guidellm.scheduler import (BackendInterface, NonDistributedEnvironment, Scheduler, ThroughputStrategy)
from guidellm.scheduler.constraints import MaxDurationConstraint, MaxDurationConstraintArgs
from guidellm.scheduler.schemas import ConversationGraph, ConversationNode
from guidellm.schemas import RequestSettings
class MockRequest(BaseModel):
payload: str
id_: str = Field(default_factory=lambda: str(uuid.uuid4()))
class MockConversationGraph(ConversationGraph[MockRequest]):
"""Bound graph type so IPC deserialization restores MockRequest nodes."""
class MockBackend(BackendInterface):
def __init__(self, response_delay: float = 1.0):
self._response_delay = response_delay
@property
def processes_limit(self): return None
@property
def requests_limit(self): return None
def info(self) -> dict[str, Any]: return {"type": "mock_bench", "delay": self._response_delay}
async def process_startup(self): pass
async def validate(self): pass
async def process_shutdown(self): pass
async def resolve(self, request, request_info, request_history):
request_info.timings.request_start = time.time()
await asyncio.sleep(self._response_delay)
request_info.timings.request_end = time.time()
yield f"response_for_{request.payload}", request_info
def graphs():
i = 0
while True:
yield MockConversationGraph(
graph_id=str(uuid.uuid4()),
nodes={"turn_0": ConversationNode(node_id="turn_0", agent_id="default",
request=MockRequest(payload=f"req_{i}"), settings=RequestSettings())},
edges=[])
i += 1
async def main(conc: int, duration: float, delay: float):
if hasattr(Scheduler, "singleton_instance"):
Scheduler.singleton_instance = None
scheduler = Scheduler()
constraint = MaxDurationConstraint(args=MaxDurationConstraintArgs(seconds=duration)).create_constraint()
counts = {"completed": 0, "errored": 0, "cancelled": 0}
starts: list[float] = []
samples: list[tuple[float, int]] = [] # (t, processing_requests)
last_state = None
t0 = None
printed = False
async for resp, req, info, state in scheduler.run(
requests=graphs(), backend=MockBackend(delay), strategy=ThroughputStrategy(max_concurrency=conc),
env=NonDistributedEnvironment(), max_duration=constraint,
):
now = time.time()
if t0 is None: t0 = state.start_time
samples.append((now, state.processing_requests))
if info.status in counts:
counts[info.status] += 1
if info.status == "completed" and info.timings.resolve_start is not None:
starts.append(info.timings.resolve_start)
last_state = state
if state.end_processing_time is not None and state.processing_requests == 0 and not printed:
printed = True # print once processing drains, before shutdown (main can hang there)
emit(counts, starts, samples, t0, conc, duration, delay, last_state, final=False)
emit(counts, starts, samples, t0, conc, duration, delay, last_state, final=True)
def emit(counts, starts, samples, t0, conc, duration, delay, last_state, final):
tw, acc = 0.0, 0.0
for (ta, pa), (tb, _) in zip(samples, samples[1:]):
acc += pa * (tb - ta); tw += (tb - ta)
mean_conc = acc / tw if tw else 0.0
started_2s = sum(1 for s in starts if s - t0 < 2.0)
out = {
"conc": conc, "duration": duration, "delay": delay, "final": final,
"procs": last_state.num_processes if last_state else None,
"completed": counts["completed"], "errored": counts["errored"], "cancelled": counts["cancelled"],
"created": last_state.created_requests if last_state else None,
"req_per_s": round(counts["completed"] / duration, 1),
"ideal_req_per_s": conc / delay,
"mean_processing": round(mean_conc, 1),
"max_processing": max(p for _, p in samples) if samples else 0,
"started_in_first_2s": started_2s,
}
print(json.dumps(out), flush=True)
if __name__ == "__main__":
asyncio.run(main(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
``` |

|
Hi
Under load the receive thread still pulls back-to-back — the only buffering removed is the 1 buffered + 1 in-hand item a One heads-up unrelated to this PR: at the Happy to run any other configuration you'd like to see. The branch is squashed to a single commit ( |

|
Filed the shutdown problem I mentioned as |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 27, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Approving due to above results.

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Aug 27, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

When

`max_concurrency == max_requests`

(a simultaneous burst) with multiple worker processes, a few requests do not start immediately. They wait until an earlier requeston the same workerfinishes, even though other workers have free slots, and which requests stall differs run to run (#1041).The scheduler side is fine:

`WorkerProcess._process_requests_loop`

acquires the`asyncio.Semaphore(async_limit)`

before creating each request task, and each task blocks in`messaging.get()`

. The over-fetch happens one layer down, in`InterProcessMessagingQueue._receive_messages_task_thread`

, which pulls from the shared`pending_queue`

unconditionally:`buffer_receive_queue`

(`max_buffer_receive_size=1`

, set in`WorkerProcessGroup.create_processes`

).`pending_item`

variable and retries`sync_put`

until space frees up.So a worker whose

`async_limit`

slots are all busy still removestwo extrarequests from the shared queue (one buffered, one in hand). They are no longer visible to other workers and can only start once a slot onthisworker frees. A standalone check confirms it: a worker copy with no consumer at all pulls 2 of 10 queued items. This matches the reporter's "2 more than slots" observation, and in my runs every over-limit worker held exactly`async_limit + 1`

or`async_limit + 2`

requests, never more.This PR makes the worker's receive thread take a request off the shared queue only when one of that worker's request tasks is actually waiting for it.

## Details

`InterProcessMessaging._has_receive_demand()`

: true when more consumers are waiting on`buffer_receive_queue`

than there are items already buffered. Demand is tracked by a counter that`get()`

/`get_sync()`

increment before waiting and decrement in`finally`

; all production callers use`get()`

from the worker's event loop, so the counter has a single writer.`get()`

also sets a`threading.Event`

(`receive_demand_event`

, created in`start()`

so the object stays picklable for`spawn`

). In`InterProcessMessagingQueue._receive_messages_task_thread`

, workers (`worker_index is not None`

) skip`pending_queue.get()`

while there is no demand and block on that event with`poll_interval`

as the backstop — no polling while idle. The clear-then-recheck ordering makes a wake-up impossible to lose: a consumer that registers after the recheck sets the event after the clear, so`wait()`

returns immediately. The main-process side (receiving from`done_queue`

) is unchanged.`stop()`

relies on the thread observing an empty source`STOP_REQUIRED_QUEUE_EMPTY_COUNT`

times, so while gated the thread counts toward that only once`shutdown_event`

is set. The`requests_generated_event`

stop path is unaffected: the thread keeps waiting for demand and exits once it actually observes the shared queue empty.`InterProcessMessagingManagerQueue`

inherits the same thread, so it is covered.`InterProcessMessagingPipe`

is untouched: it assigns work to a worker's pipe at send time, which is a separate concern.`# noqa: PLR0912`

added to the queue receive thread; the sibling send thread already carries the same marker.`multiprocessing.Queue.get(timeout)`

acquires the queue's read lock and keeps it while it polls, so one worker waiting on a momentarily empty shared queue blocks the others for the whole timeout. With demand-gated pulls workers arrive at the queue in bursts, so the worker-side`get`

now uses`poll_interval / 10`

; the stop logic is unaffected (`STOP_REQUIRED_QUEUE_EMPTY_COUNT`

empty polls still gate every exit path).## Test Plan

Reproduction (before the fix)with guidellm's own`mock-server`

(no model needed), Apple M1, 10 worker processes,`async_limit=5`

each:`GUIDELLM__MAX_WORKER_PROCESSES=1`

controlReporter's second scenario,

`--profile kind=concurrent,streams=17 --constraint kind=max_requests,count=17`

(15–16/17 in the issue):17/17, 17/17, 17/17after the fix.Regression test`tests/unit/utils/test_messaging.py::TestInterProcessMessagingQueue::test_worker_receive_pulls_only_on_demand`

(6 parametrizations: 3 configs × fork/spawn):`main`

(the worker buffers an item with no consumer;`stop()`

then hangs because the thread is holding a second item);Unit tests, lint, types:High concurrency +(real`max_duration`

`WorkerProcessGroup`

, 10 processes, in-process backend sleeping 1 s per request, 10 s runs; the mock-server saturates an M1 above ~300 streams so HTTP was taken out of the loop):`main`

@500`main`

@2000Burst case (

`max_concurrency = max_requests = 50`

, 6 runs each):`main`

42–45/50 started immediately, ~1.0 s to dispatch all 50; PR 50/50 ×6, 0.05–0.15 s.Caveat: at the

`max_duration`

cutoff, roughly half of the runs onboth`main`

and this PR either raise`Error processing received update: '<id>'`

(a KeyError in`_update_state_request_counts`

) or never return from`scheduler.run()`

. That is a pre-existing cancel-ordering race in`WorkerProcess._cancel_requests_loop`

(it`abort()`

s nodes that in-flight tasks still own before those tasks have processed their cancellation); this PR neither causes nor fixes it — reported separately.## Related Issues

## Use of AI

Investigation, code, and tests were produced with Claude Code under my direction and review; the commit carries the

`Generated-by:`

trailer. I reproduced the bug and verified the fix end-to-end locally.🤖 Generated with Claude Code

## git log

commit

2f23fd7Author: Himanshu Prajapati himanshuprajapati15072003@gmail.com

Date: Mon Aug 24 23:07:26 2026 +0530

Co-Authored-By: Claude noreply@anthropic.com

Generated-by: Claude Code

Signed-off-by: Himanshu Prajapati himanshuprajapati15072003@gmail.com