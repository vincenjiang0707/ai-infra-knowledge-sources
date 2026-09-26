source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/concepts/fault-tolerance/request-rejection-architecture
lastmod: 2026-09-24T19:58:16.636Z

# Request Rejection Architecture

Worker-load event processing, busy-state aggregation, overload errors, and hard worker admission limits.

Dynamo implements request rejection (load shedding) at two layers: Frontend routing can avoid workers reported as busy, and each worker can enforce a hard request-plane concurrency cap.

For deployment steps, see [Request Rejection](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-rejection). For exact
configuration fields, see [Frontend Configuration](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#fault-tolerance)
and [Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration#operations).

## Request Flow

The router distinguishes two failure classes:

**Overloaded**means workers are registered but every eligible worker is busy. The Frontend returns HTTP 529 by default.**Unavailable**means no usable service path exists. The Frontend returns HTTP 503.

`DYN_HTTP_OVERLOAD_STATUS_CODE`

can change the overload response code for client compatibility. Values
from 200 through 999 are accepted. Informational values from 100 through 199, invalid values, and
out-of-range values fall back to 529. The value is read and cached on first use.

## Independently Enabled Signals

All three busy thresholds are `None`

by default. Setting a numeric value activates only that signal;
there is no master admission-control switch.

For each data-parallel rank, the monitor evaluates the configured checks with OR logic:

The fractional and absolute prefill checks can be enabled separately or together. A worker is not excluded until all of its data-parallel ranks are busy, which avoids discarding capacity on ranks that can still admit work.

Decode-block rejection depends on the KV router worker-load path. `--router-mode kv`

initializes that
path. `--router-track-output-blocks`

adds generated output tokens to the router’s observed active-block
count; without it, long outputs can consume KV cache without appearing in the tracked load. The
separate `--router-track-active-blocks`

option affects the router cost model and is not a prerequisite
for busy rejection.

## Worker Load Monitoring

`KvWorkerMonitor`

:

- Subscribes to worker KV and prefill load events.
- Stores per-worker, per-rank values such as
`active_decode_blocks`

,`kv_total_blocks`

,`active_prefill_tokens`

, and`max_num_batched_tokens`

. - Recalculates the busy set when load or runtime configuration changes.
- Publishes the current busy set to the router.

A `POST /busy_threshold`

update changes the stored threshold configuration. It does not synchronously
recompute every worker. The next worker-load or runtime-configuration update triggers reevaluation, so
a new threshold can take a short time to change routing decisions.

## Rejection Path

When a request arrives:

- The push router resolves the registered workers for the model.
- If at least one busy threshold is configured, the router removes workers in the current busy set.
- If registered workers exist but no eligible worker remains, the router returns
`PipelineError::ServiceOverloaded`

. - The HTTP layer maps overload to the configured overload status, 529 by default.
- The Frontend increments
`dynamo_frontend_model_rejection_total`

.

The Frontend also exports the latest observed worker values through
`dynamo_frontend_worker_active_decode_blocks`

and
`dynamo_frontend_worker_active_prefill_tokens`

, which help distinguish missing telemetry from a
threshold that is simply too high.

## Worker-Side Request Admission

A worker can impose a hard cap independently of Frontend busy detection. Setting
`--engine-request-limit N`

creates `N`

engine slots. Requests that arrive while those slots are full
enter a small Dynamo overflow queue of size `Q`

. When the engine and queue are both full, the worker
returns `Server overloaded: worker at capacity`

; the Frontend maps the resulting
`ResourceExhausted`

error to HTTP 529 and temporarily skips that worker on the next routing decision.

The effective maximum is `N + Q`

requests. `DYN_DYNAMO_REQUEST_QUEUE_LIMIT`

defaults to `16`

, is an
advanced override, must be at least `2`

, and is read only when the engine limit is enabled.

### Overflow Channel Sizing

The channel capacity is `Q - 1`

because one dispatcher task can hold a request between the queue and
an engine slot. This produces an exact `N + Q`

cap for `Q >= 2`

. A value of `1`

would still require a
channel capacity of one and could permit two queued requests, which is why the supported minimum is
`2`

.

Worker admission exports:

`dynamo_rejection_request_total`

`dynamo_engine_request`

`dynamo_request_queue`


See [Cancellation and Rejection](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#cancellation-and-rejection)
for metric types and labels.

## Related Documentation

[Request Rejection](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-rejection)- Enable, tune, verify, and troubleshoot load shedding[Frontend Configuration](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#fault-tolerance)- Threshold and overload response fields[Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration#operations)- Worker hard-cap fields[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture#active-worker-health-checks)- Worker health monitoring