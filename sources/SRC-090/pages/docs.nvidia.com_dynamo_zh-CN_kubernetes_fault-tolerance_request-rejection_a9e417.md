source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/fault-tolerance/request-rejection
lastmod: 2026-09-24T19:58:16.636Z

# Request Rejection

Request rejection (load shedding) rejects new requests when every eligible worker is overloaded,
rather than accepting work that could exhaust GPU memory or degrade latency for in-flight requests.
Dynamo returns **HTTP 529** for overload by default so clients can distinguish an available but busy
service from **HTTP 503**, which indicates that the service is unavailable.

Rejection is **off by default**. Each threshold is independently opt-in: setting one numeric threshold
enables only that check. You do not need `--admission-control`

; that compatibility flag is ignored.


How it works:The busy-detection formulas, data-parallel rank aggregation, worker-load event processing, and worker-side overflow queue are documented in[Request Rejection Architecture].

### Choose the load signals

Use the signals that match the workers you want to protect:

- Set
`--active-decode-blocks-threshold`

for decode workers. The value is the fraction of available KV cache blocks in use, from`0.0`

through`1.0`

. - Set
`--active-prefill-tokens-threshold`

for an absolute prefill-token limit. - Set
`--active-prefill-tokens-threshold-frac`

when the prefill limit should scale with the worker’s`max_num_batched_tokens`

value.

The checks use OR logic. If you configure more than one threshold, exceeding any configured threshold marks that data-parallel rank as busy. A worker is rejected only after all of its ranks are busy, and a request is shed only when every eligible worker is busy.

Start conservatively, observe the rejection rate and latency, and then raise the limits. For example,
a decode-block threshold of `0.75`

sheds earlier than `0.90`

.

### Enable rejection on the Frontend

Configure thresholds on the **Frontend** component. Decode-block rejection also requires KV router
mode because that mode initializes the worker-load metrics path. For long-output workloads, enable
output-block tracking so generated tokens contribute to the observed KV cache load.

`--router-track-output-blocks`

is especially important for long generations. Without it, a workload
can fill KV cache with generated tokens without crossing the load value observed by the router.

You can configure just one signal. For example, a prefill-only deployment can omit the decode-block
threshold and KV-specific options. To disable rejection, remove all three threshold settings or set
their environment-variable values to `None`

.

See [Frontend Configuration](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#fault-tolerance)
for the complete flag, environment-variable, and validation reference.

### Adjust thresholds at runtime

Optional. Use the Frontend admin API to change thresholds for a discovered model without redeploying.
The API is available by default. Set `DYN_DISABLE_FRONTEND_ADMIN_API`

to a truthy value to turn it
off, which unregisters both `busy_threshold`

routes so they return 404.

Set one or more thresholds:

Read the stored thresholds:

A numeric value enables only its corresponding check. The router applies the new configuration when
the next worker-load or runtime-configuration update arrives, so the change might not affect a routing
decision immediately. This endpoint does not enable `--router-mode kv`

or
`--router-track-output-blocks`

; set those when the Frontend starts.

### Add a worker-side hard cap

Optional. A worker can independently cap concurrent engine work and queue only a small burst. Set
`--engine-request-limit N`

(or `DYN_ENGINE_REQUEST_LIMIT`

) on the **worker** component:

When all `N`

engine slots and the overflow queue are full, the worker rejects the request and the
Frontend returns HTTP 529. `DYN_DYNAMO_REQUEST_QUEUE_LIMIT`

controls the advanced overflow-queue
size, defaults to `16`

, must be at least `2`

, and has an effect only when the engine limit is set. The
effective cap is `N + Q`

in-flight requests per worker.

See [Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration#operations) for the exact
fields and [Worker-Side Request Admission](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-rejection-architecture#worker-side-request-admission)
for the queue implementation.

### Verify rejection

Inspect the configured thresholds and worker-load metrics:

Generate enough load to exceed the configured threshold, then confirm:

- The client receives HTTP 529.
`dynamo_frontend_model_rejection_total`

increases for the affected`model`

and`endpoint`

.- Worker-side hard-cap tests increase
`dynamo_rejection_request_total`

when both the engine and queue are full.

For all metric fields and labels, see
[Cancellation and Rejection](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#cancellation-and-rejection).

## Troubleshoot Decode-Block Rejection

If decode-block load does not produce HTTP 529 responses:

-
Confirm that

`GET /busy_threshold`

shows a numeric`active_decode_blocks_threshold`

for the model. -
Confirm that the Frontend started with

`--router-mode kv`

. -
For long-output workloads, confirm that the Frontend started with

`--router-track-output-blocks`

. -
Check that the Frontend receives worker updates:

-
Check Frontend logs for worker-monitor subscription warnings.

-
Confirm that each worker publishes its total KV block count:

-
Verify the event-plane configuration and connectivity between the Frontend and workers.


`--router-track-active-blocks`

is a separate routing option. Busy rejection depends on configured
thresholds and worker-load events; it does not require that internal router tracking flag.

## Configure Client Retries

Retry HTTP 529 responses with exponential backoff and jitter. Do not retry every HTTP 503 as if it were overload; 503 indicates that Dynamo currently has no available service path.

If an existing client only understands 503 retry semantics, set
`DYN_HTTP_OVERLOAD_STATUS_CODE=503`

on the Frontend. The variable accepts values from 200 through
999. Informational values from 100 through 199, invalid values, and out-of-range values fall back to
529. The value is read and cached on first use.

## Related Documentation

[Request Rejection Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-rejection-architecture)- Busy detection, event flow, and admission internals[Frontend Configuration](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#fault-tolerance)- Thresholds, overload status, and admin API[Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration#operations)- Worker-side engine and queue limits[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#cancellation-and-rejection)- Rejection and admission metrics[Request Migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration)- Recovering in-flight requests after worker failure