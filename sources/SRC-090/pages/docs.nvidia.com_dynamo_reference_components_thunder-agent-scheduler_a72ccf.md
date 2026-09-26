source: https://docs.nvidia.com/dynamo/reference/components/thunder-agent-scheduler
lastmod: 2026-09-24T19:58:16.636Z

# ThunderAgent Scheduler Reference

Control-loop flags, constraints, capacity behavior, and scheduler log records

`dynamo.thunderagent_router`

is experimental. The command-line interface and lifecycle contract can change.

The ThunderAgent scheduler uses the program working set as a fraction of each worker’s retention budget. With SGLang HiCache enabled, the budget is the sum of published GPU KV capacity and host HiCache capacity. Mooncake capacity is excluded because it is conditional content-addressed storage rather than guaranteed per-program retention.

## Control-Loop Configuration

All `KvRouter`

flags accepted by `dynamo.router`

, including `--router-temperature`

, `--use-kv-events`

, and `--router-track-output-blocks`

, are also accepted and forwarded.

## Constraints

The service rejects configurations that violate any of these relationships:

The control loop has three bands:

- At or above
`pause-threshold`

, pause acting programs until utilization reaches`pause-target`

. - From
`soft-demote-threshold`

up to`pause-threshold`

, lower program priority without pausing. - Resume only after utilization falls at least
`resume-hysteresis`

below`pause-threshold`

.

## Session Inputs

Programs are keyed by the normalized `session_id`

. Use the canonical headers defined in [Session IDs](https://docs.nvidia.com/dynamo/agents/session-i-ds):

`X-Dynamo-Session-ID`

`X-Dynamo-Parent-Session-ID`

`X-Dynamo-Session-Final`


Requests without session identity bypass program admission and pause/resume.

## Scheduler Logs

The scheduler emits pause-side and resume-side summaries at INFO level.

`paused`

: acting programs paused during the tick`marked`

: reasoning programs marked to pause at the next tool boundary`util`

: worker utilization before and after the pause cycle

`resumed`

: programs resumed during the tick`still_paused`

: programs remaining in the paused table

Lower the log level for `dynamo.thunderagent_router`

to DEBUG for per-program records:

For request-level tracing, enable `DYN_REQUEST_TRACE=1`

on the frontend. Explicit harness tool spans additionally require `DYN_REQUEST_TRACE_TOOL_EVENTS_ZMQ_ENDPOINT`

and a configured publisher. See [Request Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/request-traces).

## Related Pages

- Run the ThunderAgent Scheduler
[ThunderAgent Scheduler Design](https://docs.nvidia.com/dynamo/agents/thunder-agent-program-scheduler)[Priority Scheduling](https://docs.nvidia.com/dynamo/agents/priority-scheduling)