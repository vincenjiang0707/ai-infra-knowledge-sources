source: https://docs.nvidia.com/dynamo/v1.3.0/components/router/priority-scheduling
lastmod: 2026-09-24T19:58:16.636Z

# Priority Scheduling

Priority scheduling lets a client mark one request as more important than another. Dynamo exposes two related request fields:

`nvext.agent_hints.priority`

is a soft priority used by router policy scoring and supported backend engines.`nvext.agent_hints.strict_priority`

is an unsigned router pending-queue tier. Higher tiers always precede lower tiers.

For HTTP requests, send the same values in `x-dynamo-request-priority`

and
`x-dynamo-request-strict-priority`

. Header values override the corresponding `nvext.agent_hints`

fields.

## Priority Layers

Priority can affect three different layers. They are configured separately.

These layers are additive. `strict_priority`

does not propagate to backend engine scheduling; use `priority`

for that layer.

## Router Queue Priority

The router queue only matters when requests are held before dispatch. If a request can be routed immediately, there is no pending queue to reorder and the priority hint will not change TTFT at the router layer.

`--router-queue-threshold`

controls when the router starts holding requests. A request waits in the router queue while every eligible worker is above the configured threshold. The queue drains when capacity is available, and higher-priority requests are selected according to the queue key:

The strict tier is compared first. FCFS, LCFS, or Weighted Shortest Processing Time (WSPT) still computes the secondary key and orders requests within the same tier.

The default policy is `fcfs`

, which uses the priority value as a positive arrival-time bump. Higher values move the request earlier in the queue. Negative priority values are clamped to zero for router queueing, so a request cannot be pushed behind normal first-come, first-served ordering by sending a negative priority.

For the flag-level semantics, default value, and backend caveats, see [Router Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning#routing-behavior).

## Backend Engine Priority

The backend receives the same Dynamo semantic priority, but each engine has its own native scheduling convention. Dynamo handles that conversion internally.

Do not negate `nvext.agent_hints.priority`

in client code for vLLM. If a test shows lower user values receiving better TTFT, first check whether the benchmark harness or endpoint path inverted the value before it reached Dynamo.

## What Priority Does Not Do

Priority is not Kubernetes `PriorityClass`

, GPU preemption, or a hard admission control policy. It does not reserve capacity for high-priority requests.

Strict priority applies only to requests already parked in one scheduler queue. It does not preempt admitted work, impose ordering across router replicas or upstream queues, or guarantee backend engine execution order. An eligible new arrival can still be admitted directly while other requests are pending.

Priority also does not show an effect unless there is contention at a layer that uses it:

- Router priority needs a non-empty router queue.
- Engine priority needs backend priority scheduling enabled and engine-side queueing or preemption opportunities.
- Cache priority needs memory pressure and a priority-aware eviction policy.

## Verify Priority Is Working

Use a benchmark that can send different `nvext.agent_hints.priority`

values on individual requests. For AIPerf, use a version with per-request `extra`

payload support. Older AIPerf versions may only support global `--extra-inputs`

, which is not enough for mixed-priority tiers in the same run.

For router-priority validation:

- Use a fixed request count or burst-style test so every priority tier gets the same number of measured requests.
- Keep the model, input length, output length, streaming mode, and endpoint path identical across priority tiers.
- Run at enough load for requests to wait in the router queue. Watch
and confirm it is greater than zero during the measured window.`dynamo_frontend_router_queue_pending_requests`

- Configure the backend priority flag separately if the test is meant to measure engine scheduling, not only router queue ordering.

Expected result: higher Dynamo priority values should receive better TTFT under contention. If lower values win, first check whether the client, benchmark harness, or gateway path negated the priority before it reached Dynamo.