source: https://docs.nvidia.com/dynamo/zh-CN/dev/reinforcement-learning/kv-aware-load-balancing
lastmod: 2026-09-23T23:30:39.914Z

KV-Aware Load Balancing for RL Rollouts


KV-Aware Load Balancing for RL Rollouts

Dynamo uses the same router for RL and other inference workloads. What changes is the objective: measure serving efficiency together with framework-owned sample freshness and acceptance. Dynamo routes requests; it does not decide whether a trajectory is on-policy or useful for training.

Use the [router configuration reference](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning) for complete flag definitions and defaults.

## Choose a Starting Strategy

Start with one baseline and one mechanism justified by the workload. Do not enable KV routing, queueing, affinity, priority, offload, and custom policies in the same first experiment.

## Establish the Baseline

Use round-robin to measure the cost of simple distribution:

Record the effective worker set, request errors, generated tokens, time to first token, inter-token latency, end-to-end latency, queue depth, and framework accepted or fresh sample counts. Use the same cold- or warm-cache procedure for every comparison.

Round-robin is a control, not a universal recommendation. Verify that every intended worker is eligible and receives traffic before trusting the baseline.

## Evaluate Prefix Reuse

Enable KV-aware routing when prompts share token prefixes:

For parallel samples that arrive before the first worker publishes KV events, add a short predicted-placement window:

Treat `5`

seconds as a starting value. Tune it against the observed gap between routing and usable KV events. Confirm that equivalent prompts use the same model, tokenizer, cache salt, LoRA identity, and token sequence; the router cannot recover reuse hidden by the request representation.

If one cache-rich worker receives too much work, compare overlap-credit decay or a lower overlap credit while holding the request schedule fixed. Use `--load-aware`

as the control that accounts for active load without crediting prefix reuse:

## Map the Setting to the Framework

Configure the frontend that actually receives rollout traffic; do not launch a second frontend just to copy a generic command.

When workers advertise router configuration, verify the effective worker-set values in the frontend logs. Worker settings can replace frontend defaults rather than merge with them.

## Use Affinity and Queueing Deliberately

`X-Dynamo-Session-ID`

identifies a session but does not enable affinity. Enable affinity only when related turns must remain on one worker:

Prefer ordinary KV-aware routing when cache state is enough. Affinity does not create a backend conversation, enforce a policy version, or update workers when a session ends.

Add router queueing only after measuring dispatch and engine queue pressure. Compare first-come, first-served (`fcfs`

) for tail behavior with weighted shortest processing time (`wspt`

) for mixed prompt lengths. Use bounded service classes; never encode rollout IDs, users, or policy versions as queue classes or Prometheus labels.

## Handle Worker Loss and Overload

Discovery and leases remove lost workers from the eligible set so new rollouts use healthy capacity. Requests already assigned to a failed worker fail unless request migration is enabled. Because a replacement worker does not inherit the failed worker’s KV cache, migrated and newly routed requests can require a fresh prefill.

Enable best-effort migration for supported in-flight requests by setting a positive limit on the frontend:

Migration is off by default and has request-shape limitations. See [Request Migration](https://docs.nvidia.com/dynamo/dev/kubernetes/fault-tolerance/request-migration) before relying on it for rollout continuity.

For bursty workloads, configure [Request Rejection](https://docs.nvidia.com/dynamo/dev/kubernetes/fault-tolerance/request-rejection) so the frontend returns HTTP 529 when every eligible worker exceeds the selected load threshold. The framework can then retry under its own attempt and sample-acceptance policy instead of allowing queueing delay to grow without a bound. Rejection is also off by default.

## Measure Useful Work

Keep model, hardware, prompts, arrival schedule, concurrency, output limits, worker count, parallelism, cache state, and update cadence fixed. Run at least three measured repetitions after warm-up.

Report:

- request success, generated tokens, queue time, latency, and per-worker load
- KV-cache hits and queries when cache reuse is the mechanism
- completed and accepted trajectory groups, not only individual requests
- stale or rejected samples and rollout-phase time
- the causal explanation for the result

Many RL workloads wait for every required sample in a group. Measure the time from first dispatch to the final accepted attempt and identify the slowest request’s queue, prefill, and decode contribution. A faster mean request that does not improve group completion or useful training output is not a win.

The router does not filter workers by RL policy version. Gate synchronous updates in the framework, or enforce bounded staleness and sample acceptance there.

## Diagnose Common Problems

Use the [metrics catalog](https://docs.nvidia.com/dynamo/dev/reference/observability/metrics-catalog#router-metrics) for exact metric names and [Profile and Simulate RL Rollouts](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-profiling-and-simulation) to correlate framework, router, and worker behavior.