source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/agents/thunder-agent-program-scheduler
lastmod: 2026-09-23T23:30:39.914Z

# ThunderAgent Program Scheduler

Program-level scheduling with tool-boundary pause/resume on top of KV-aware routing


Experimental — not a released component.Run it from a source checkout, not from a`pip install ai-dynamo`

. The CLI flags, the`nvext.agent_context`

schema, and the lifecycle hooks are all unstable and will change. Build and launch specifics live next to the code in[.]`components/src/dynamo/thunderagent_router/README.md`


`dynamo.thunderagent_router`

is a standalone Dynamo router that schedules at the
granularity of an agent run — the whole `LLM turn → tool call → next turn`

loop —
instead of individual requests. It wraps Dynamo’s native KV router and adds a
program-level scheduler with tool-boundary pause/resume on top of KV-aware
routing, porting the scheduler from the [ThunderAgent](https://arxiv.org/abs/2602.13692)
paper (Kang et al., 2026).

## The Problem

Agentic workloads (SWE-bench, browser-use, anything with a tool loop) make many
short LLM calls separated by non-GPU work: `docker exec`

, `pytest`

, `curl`

,
waiting on a subagent. Between turns the agent’s KV cache stays resident, holding
blocks while doing nothing. A request-level router (vLLM’s, SGLang’s, Dynamo’s
stock `KvRouter`

) sees each turn but not the agent behind it, which costs you two
ways:

**Cache-occupancy blowup.**With N agents at step K, the working set is`N × step_K_context`

, most of it idle between turns. The engine evicts useful blocks under pressure or refuses admission, and every next turn pays a re-prefill tax.**No tool-boundary backpressure.**The router can’t defer a hot trajectory at a natural pause point — it can only cancel in-flight requests or queue them, both worse than waiting until the agent is between turns.

## The Scheduler

The algorithm groups requests by `program_id`

(the `trajectory_id`

from
`nvext.agent_context`

) and runs an outer scheduler that moves each program
through `(REASONING | ACTING) × (ACTIVE | PAUSED)`

. A program enters ACTING at a
tool boundary. Under memory pressure the scheduler pauses ACTING programs —
logically, with no decode preemption — so the engine is free to evict their KV.
When utilization drops it resumes the smallest-token programs first, BFD-packing
them back under threshold. The payoff is working-set accounting that counts
programs rather than requests, plus pause/resume aimed at tool boundaries rather
than arbitrary tokens.

This is an in-path Dynamo service that owns a `KvRouter`

directly and registers
as a model handler, so there is no extra proxy hop, and it reads real
`prompt_tokens + completion_tokens`

off each response rather than estimating
token counts from raw bytes.

### Scheduler Tick

A single background task runs every `--scheduler-interval-seconds`

(default
`5.0`

). Each tick takes a capacity snapshot and runs three phases in a fixed
order:

Resume runs **before** pause on purpose (upstream ThunderAgent ordering): a
program paused this tick cannot resume until the next tick, which prevents a
program from being paused and immediately resumed within one tick.

### Tool-Boundary Pause/Resume Semantics

**Pause**is logical. The scheduler picks the smallest ACTING programs on an over-threshold worker first and pauses them; if no ACTING candidate exists it marks the smallest REASONING program for pause at its next tool boundary. There is no decode preemption — a paused program’s in-flight turn is allowed to finish, and the program is held out of admission until a later tick resumes it.**Resume**is greedy and BFD-packed. When a worker has headroom (see the control loop below), the scheduler resumes the smallest-token paused programs first, fitting each back under threshold and accounting for`buffer_per_program`

. Resumed requests get a transient priority boost so they re-enter ahead of fresh admissions, and a forced-resume cap (`--resume-timeout-seconds`

) guarantees no program is starved indefinitely.

### Program Close (trajectory_final)

A program is created on its first turn (keyed by `trajectory_id`

) and otherwise
lives ACTIVE↔PAUSED for the process lifetime — a single LLM `finish_reason`

cannot
mark a *program* done, since the agent typically keeps issuing turns. To release a
program deterministically, the harness sets the optional terminal marker
** nvext.agent_context.trajectory_final: true** on a final request (e.g. on the
agent’s

`agent_end`

). When the router sees it, it **deletes the program from its table (and paused set) and short-circuits the request — it is never forwarded to a worker**(the response is an empty completion). This frees the program’s scheduling bookkeeping so its tokens stop counting against worker utilization.

The close is best-effort from the harness side; if it never arrives (crash, black-box
harness) the program lingers in the table, but its token weight decays toward zero so it
stops counting against worker utilization — the scheduling impact self-heals even without
an explicit close. `pi-dynamo-provider`

fires the close automatically on `agent_end`

/
`session_shutdown`

(a dedicated `max_tokens: 1`

request — a reactive agent loop only
learns a turn was terminal from its response, so a run’s end is typically known only
after its last real turn already returned, leaving no live turn to flag).

## Utilization-Driven Control Loop

Pause/resume is driven by per-worker utilization — the program working set as a fraction of the worker’s KV pool. The loop has three bands:

- At or above
`pause-threshold`

, the worker is over-subscribed; the tick pauses ACTING programs until utilization falls back to`pause-target`

. - In the
`[soft-demote-threshold, pause-threshold)`

band, programs are soft-demoted (a negative priority jump) but not paused — early backpressure before a hard pause is needed. - Resume only fires once utilization has dropped at least
`resume-hysteresis`

below`pause-threshold`

, so the loop does not oscillate between pause and resume on the threshold boundary.


Constraint:`pause-target <= pause-threshold`

. The service rejects configs that violate it (along with`0 <= resume-hysteresis <= pause-threshold`

and`0 <= soft-demote-threshold <= pause-threshold`

).

All `KvRouter`

flags from `dynamo.router`

(`--router-temperature`

,
`--use-kv-events`

, `--router-track-output-blocks`

, …) are also accepted and
forwarded. See the
[folder README](https://docs.nvidia.com/dynamo/v1.2.1/components/src/dynamo/thunderagent_router/README.md) for the
remaining service flags (`--endpoint`

, `--model-name`

, `--model-path`

, tool-call
and reasoning parsers).

## Architecture

## Observability

The scheduler emits a per-tick INFO summary on each side of the control loop, so both pause and resume activity are visible at INFO without enabling DEBUG. Per-program detail stays at DEBUG.

**Pause side** — logged when a worker pauses or marks any program in a tick:

`paused`

is the number of ACTING programs paused this tick, `marked`

is the
number of REASONING programs marked for pause at their next tool boundary, and
`util=X -> Y`

is the worker utilization before and after the pause cycle.

**Resume side** — logged when a worker resumes any program in a tick:

`resumed`

is the number of programs resumed this tick and `still_paused`

is the
size of the paused table afterward. This line is symmetric to the pause-side
summary; before it existed, pause was observable at INFO but resume was only
visible at DEBUG, leaving a gap when reconstructing a control-loop cycle from
INFO logs alone.

**Per-program detail (DEBUG):**

Enable these by lowering the log level for `dynamo.thunderagent_router`

. They
give the exact program identities behind each INFO summary count.

For per-request tracing (token counts, cache hits, worker placement, tool-event
timelines), the router also integrates with [Agent Tracing](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-tracing):
set `DYN_AGENT_TRACE=1`

on the frontend to land a `request_end`

record per LLM
call plus the harness tool-event timeline.

## Reproducing the MiniMax-M2 Results

The headline numbers (program-aware scheduling vs KV-routing-only on the same
hardware, ~12-16% throughput improvement on SWE-bench-Lite with two TP4
MiniMax-M2 replicas on a single 8×H100 node) and the exact launch/repro commands
live in the
[folder README](https://docs.nvidia.com/dynamo/v1.2.1/components/src/dynamo/thunderagent_router/README.md).

## References

- ThunderAgent paper:
[arxiv.org/abs/2602.13692](https://arxiv.org/abs/2602.13692) - Upstream ThunderAgent reference:
[HaoKang-Timmy/ThunderAgent](https://github.com/HaoKang-Timmy/ThunderAgent) - Repro fork (mini-swe-agent + agent_context injector):
[ishandhanani/ThunderAgent](https://github.com/ishandhanani/ThunderAgent) - Dynamo KV router:
[Router Guide](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/kv-cache-aware-routing) `nvext.agent_context`

schema:[nvext reference](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/nvidia-request-extensions-nvext#agent-context)[Agent Tracing](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-tracing)and[Agent Hints](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-hints)