# [Issue #1049] [Bug]: max_duration at high concurrency double-reports in-flight requests, causing a KeyError abort or a shutdown hang

source: https://github.com/vllm-project/guidellm/issues/1049
state: closed | updated: 2026-08-27T19:10:58Z
labels: 

## 正文

### Bug Description

When a run ends on a `max_duration` constraint with many requests in flight, the same request can be reported **twice** — once as `cancelled` by the worker's cancel loop, and once as `completed`/`errored` by its own in-flight task. The scheduler's bookkeeping is not tolerant of that, so the run ends in one of two ways:

1. **Abort** — `Error processing received update: '<request_id>'` (a `KeyError`), which sets `error_event`, and every worker then dies with `received error signal`.
2. **Hang** — all requests reach a terminal state, `end_processing_time` is set, `processing_requests` reaches 0, but `Scheduler.run()` never returns.

On `main` (963d1a15), 10 runs at `max_concurrency=500` with `max_duration=8`: **3 hung, 3 aborted, 4 completed cleanly.** It is timing dependent, so it does not reproduce every run, but it is frequent at high concurrency.

### Root cause

Captured directly by printing the status that raises in `WorkerGroupState.received_callback`:

```
raising_status='completed' request_id=6a00e914-f015-40fe-8af2-342f2da41a24 err=KeyError: '6a00e914-f015-40fe-8af2-342f2da41a24'
```

So a **`completed`** update arrives for a request that is no longer in `_processing_request_ids`, because a `cancelled` update for the same request already removed it.

The sequence:

1. Request is in flight; the main process has its id in `_processing_request_ids`.
2. The duration constraint fires. `WorkerProcess._process_requests` calls `processing_task.cancel()` (`worker.py:240`) and then immediately `await self._cancel_requests_loop()` (`worker.py:243`). `cancel()` only *schedules* cancellation — the request tasks have not processed their `CancelledError` yet.
3. `_cancel_requests_loop` walks `self.turns_queue` and calls `state.abort()` (`worker.py:326-327`), which returns **every node that is not completed, including nodes an in-flight task still owns**, and sends a `cancelled` update for each. The main process removes the id (the `errored`/`cancelled` branch at `worker_group.py:750` uses guarded removes) and does `processed_requests += 1`.
4. The in-flight task, which was about to finish anyway, completes and sends its own `completed` update. `worker_group.py:744-746` then does an unguarded `self._processing_request_ids.remove(info.request_id)` → **`KeyError`** (manifestation 1).

When the timing works out so the second update does not hit the unguarded `remove`, the counters still drift instead: both branches do `processed_requests += 1` for the same request, so `processed_requests` overshoots `created_requests`, the equality check at `worker_group.py:684` never holds, `shutdown_event` is never set, and `request_updates()` loops forever (manifestation 2).

Both manifestations therefore come from the same cause: **a request that is cancelled by the cancel loop while its own task is still running gets two terminal updates.**

### Expected Behavior

A `max_duration` run should end cleanly at any concurrency: exactly one terminal update per request, and `Scheduler.run()` returns.

### Steps to Reproduce

No model or server needed — this is scheduler-only, with an in-process backend that just sleeps:

```python
# race.py
from __future__ import annotations
import asyncio, sys, time, uuid
from typing import Any
from pydantic import BaseModel, Field
from guidellm.scheduler import (
    BackendInterface, NonDistributedEnvironment, Scheduler, ThroughputStrategy,
)
from guidellm.scheduler.constraints import MaxDurationConstraint, MaxDurationConstraintArgs
from guidellm.scheduler.schemas import ConversationGraph, ConversationNode
from guidellm.schemas import RequestSettings


class MockRequest(BaseModel):
    payload: str
    id_: str = Field(default_factory=lambda: str(uuid.uuid4()))


class MockConversationGraph(ConversationGraph[MockRequest]):
    """Bound graph type so IPC deserialization restores MockRequest nodes."""


class MockBackend(BackendInterface):
    @property
    def processes_limit(self): return None
    @property
    def requests_limit(self): return None
    def info(self) -> dict[str, Any]: return {"type": "race"}
    async def process_startup(self): pass
    async def validate(self): pass
    async def process_shutdown(self): pass
    async def resolve(self, request, request_info, request_history):
        request_info.timings.request_start = time.time()
        await asyncio.sleep(1.0)
        request_info.timings.request_end = time.time()
        yield f"r_{request.payload}", request_info


def graphs():
    i = 0
    while True:
        yield MockConversationGraph(
            graph_id=str(uuid.uuid4()),
            nodes={"t0": ConversationNode(
                node_id="t0", agent_id="d",
                request=MockRequest(payload=f"q{i}"), settings=RequestSettings())},
            edges=[])
        i += 1


async def main(conc: int, duration: float):
    if hasattr(Scheduler, "singleton_instance"):
        Scheduler.singleton_instance = None
    n = 0
    async for _resp, _req, _info, _state in Scheduler().run(
        requests=graphs(), backend=MockBackend(),
        strategy=ThroughputStrategy(max_concurrency=conc),
        env=NonDistributedEnvironment(),
        max_duration=MaxDurationConstraint(
            args=MaxDurationConstraintArgs(seconds=duration)).create_constraint(),
    ):
        n += 1
    print(f"clean exit after {n} updates")


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]), float(sys.argv[2])))
```

```bash
for i in 1 2 3 4 5 6 7 8 9 10; do timeout 40 python race.py 500 8; echo "run$i exit=$?"; done
```

`exit=124` is the hang; a `RuntimeError: error_event is set in WorkerProcessGroup` preceded by `Error processing received update: '<uuid>'` is the abort; `clean exit after N updates` is a good run. On my machine (Apple M1, 10 worker processes, `spawn`) 6 of 10 runs failed.

To see the raising status directly, temporarily add a print to the `except` in `WorkerGroupState.received_callback`:

```python
print(f"DIAG raising_status={request_info.status!r} request_id={request_info.request_id} err={type(err).__name__}: {err}", file=sys.stderr, flush=True)
```

### Possible fixes

I did not want to guess which direction you prefer, so I have not opened a PR:

1. **Await cancellation before reporting.** In `_process_requests`, await the cancelled `processing_task` (and its child request tasks) before `_cancel_requests_loop` walks `turns_queue`, so each task reports its own terminal status and the cancel loop only reports what is genuinely still queued.
2. **Do not cancel nodes that a task owns.** Have `DAGExecutionState.abort()` skip claimed nodes (or have `_cancel_requests_loop` skip them) and let the owning task emit the terminal update.
3. **Make the bookkeeping idempotent** in `_update_state_request_counts` — guard the `completed`/`pending`/`in_progress` removes the way the `cancelled` branch already is, and ignore a second terminal update for a request that is already finalized. This alone would stop the crash and the count drift even if a duplicate slips through, and looks like a sensible safety net regardless of which of the above is chosen.

### Environment

- guidellm `main` @ 963d1a15
- Python 3.12.10, macOS (Apple M1), `spawn` start method, 10 worker processes
- Found while benchmarking #1042 at 500–2000 concurrency; that PR neither causes nor fixes this (it reproduces on `main` without it).


## 评论 (1)

### sjmonson · 2026-08-25

Thanks for debugging this! I think I ran into this issue a few weeks back but couldn't reliably reproduce it. I think a combination fixes (1) and (3) makes the most sense. (2) is not a bad idea either but it seems less intuitive that calling `state.abort()` would skip certain nodes.
