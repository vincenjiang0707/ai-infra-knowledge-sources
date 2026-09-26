source: https://docs.nvidia.com/dynamo/agents/thunder-agent-program-scheduler
lastmod: 2026-09-24T19:58:16.636Z

# ThunderAgent Program Scheduler

Program-level scheduling with tool-boundary pause/resume on top of KV-aware routing


Experimental — not a released component.Run it from a source checkout, not from a`pip install ai-dynamo`

. The CLI flags, session headers, and lifecycle hooks are all unstable and will change.

`dynamo.thunderagent_router`

is a standalone Dynamo router that schedules at the granularity of an agent run — the whole `LLM turn → tool call → next turn`

loop — instead of individual requests. It wraps Dynamo’s native KV router and adds a program-level scheduler with tool-boundary pause/resume on top of KV-aware routing, porting the scheduler from the [ThunderAgent](https://arxiv.org/abs/2602.13692) paper (Kang et al., 2026).

## The Problem

Agentic workloads (SWE-bench, browser-use, anything with a tool loop) make many short LLM calls separated by non-GPU work: `docker exec`

, `pytest`

, `curl`

, waiting on a subagent. Between turns the agent’s KV cache stays resident, holding blocks while doing nothing. A request-level router (vLLM’s, SGLang’s, Dynamo’s stock `KvRouter`

) sees each turn but not the agent behind it, which costs you two ways:

**Cache-occupancy blowup.**With N agents at step K, the working set is`N × step_K_context`

, most of it idle between turns. The engine evicts useful blocks under pressure or refuses admission, and every next turn pays a re-prefill tax.**No tool-boundary backpressure.**The router can’t defer a hot session at a natural pause point — it can only cancel in-flight requests or queue them, both worse than waiting until the agent is between turns.

## The Scheduler

The algorithm groups requests by `program_id`

(the header-derived `session_id`

) and runs an outer scheduler that moves each program through `(REASONING | ACTING) × (ACTIVE | PAUSED)`

. A program enters ACTING at a tool boundary. Under memory pressure the scheduler pauses ACTING programs — logically, with no decode preemption — so the engine is free to evict their KV. When utilization drops it resumes the smallest-token programs first, BFD-packing them back under threshold. The payoff is working-set accounting that counts programs rather than requests, plus pause/resume aimed at tool boundaries rather than arbitrary tokens.

This is an in-path Dynamo service that owns a `KvRouter`

directly and registers as a model handler, so there is no extra proxy hop, and it reads real `prompt_tokens + completion_tokens`

off each response rather than estimating token counts from raw bytes.

### Scheduler Tick

A single background task runs every `--scheduler-interval-seconds`

(default `5.0`

). Each tick takes a capacity snapshot and runs three phases in a fixed order:

Resume runs **before** pause on purpose (upstream ThunderAgent ordering): a program paused this tick cannot resume until the next tick, which prevents a program from being paused and immediately resumed within one tick.

### Tool-Boundary Pause/Resume Semantics

**Pause**is logical. The scheduler picks the smallest ACTING programs on an over-threshold worker first and pauses them; if no ACTING candidate exists it marks the smallest REASONING program for pause at its next tool boundary. There is no decode preemption — a paused program’s in-flight turn is allowed to finish, and the program is held out of admission until a later tick resumes it.**Resume**is greedy and BFD-packed. When a worker has headroom (see the control loop below), the scheduler resumes the smallest-token paused programs first, fitting each back under threshold and accounting for`buffer_per_program`

. Resumed requests get a transient priority boost so they re-enter ahead of fresh admissions, and a forced-resume cap (`--resume-timeout-seconds`

) guarantees no program is starved indefinitely.

### Program Lifetime

A program is created on its first turn, keyed by `session_id`

. Public session identity is carried in headers such as `x-dynamo-session-id`

, `x-dynamo-parent-session-id`

, and `x-dynamo-session-final`

. Program bookkeeping must still be bounded by router policy, such as idle expiry or token-weight decay.

## Utilization-Driven Control Loop

Pause/resume is driven by per-worker utilization — the program working set as a fraction of the worker’s retention budget. With SGLang HiCache enabled, Dynamo reads the worker’s published GPU KV and host HiCache capacities and uses their sum. The host tier is included so native GPU-to-host spill can happen before this scheduler pauses programs. Mooncake is excluded: it is conditional content-addressed storage, not guaranteed per-program retention. The loop has three bands:

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

, `--use-kv-events`

, `--router-track-output-blocks`

, …) are also accepted and forwarded.

## Architecture

## Observability

The scheduler emits a per-tick INFO summary on each side of the control loop, so both pause and resume activity are visible at INFO without enabling DEBUG. Per-program detail stays at DEBUG.

**Pause side** — logged when a worker pauses or marks any program in a tick:

`paused`

is the number of ACTING programs paused this tick, `marked`

is the number of REASONING programs marked for pause at their next tool boundary, and `util=X -> Y`

is the worker utilization before and after the pause cycle.

**Resume side** — logged when a worker resumes any program in a tick:

`resumed`

is the number of programs resumed this tick and `still_paused`

is the size of the paused table afterward. This line is symmetric to the pause-side summary; before it existed, pause was observable at INFO but resume was only visible at DEBUG, leaving a gap when reconstructing a control-loop cycle from INFO logs alone.

**Per-program detail (DEBUG):**

Enable these by lowering the log level for `dynamo.thunderagent_router`

. They give the exact program identities behind each INFO summary count.

For per-request tracing (token counts, cache hits, worker placement), the router also integrates with [Agent Tracing](https://docs.nvidia.com/dynamo/agents/agent-tracing#enable-output): set `DYN_REQUEST_TRACE=1`

on the frontend to land a `request_end`

record per LLM call. Harness tool-event spans are separate: they require `DYN_REQUEST_TRACE_TOOL_EVENTS_ZMQ_ENDPOINT`

plus a configured publisher.

## Reproducing with upstream Harbor and Pi

The maintained end-to-end path uses upstream Harbor to create SWE-bench containers and Pi with the Dynamo provider inside each container. The complete source build, ThunderAgent arm, stock KV arm, stable-session setup, and scaling procedure live in the [ thunderagent_router README](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/thunderagent_router/README.md#harborpi-ab-walkthrough).

## References

- ThunderAgent paper:
[arxiv.org/abs/2602.13692](https://arxiv.org/abs/2602.13692) - Upstream ThunderAgent reference:
[HaoKang-Timmy/ThunderAgent](https://github.com/HaoKang-Timmy/ThunderAgent) - Pi Dynamo provider:
[ai-dynamo/agent-plugins](https://github.com/ai-dynamo/agent-plugins/tree/main/pi-plugin) - Dynamo KV router:
[Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide) [Session IDs](https://docs.nvidia.com/dynamo/agents/session-i-ds),[Agent Tracing](https://docs.nvidia.com/dynamo/agents/agent-tracing), and[Agent Hints](https://docs.nvidia.com/dynamo/agents/agent-hints)