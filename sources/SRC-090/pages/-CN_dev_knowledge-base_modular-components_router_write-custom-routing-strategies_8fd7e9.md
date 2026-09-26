source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/modular-components/router/write-custom-routing-strategies
lastmod: 2026-09-23T23:38:42.209Z

# Write Custom Routing Strategies

**Experimental.** A custom worker-selection policy controls how Dynamo filters and scores eligible workers, then selects one. Dynamo still owns discovery, eligibility, queueing, reservations, accounting, and metrics.

## How It Works

This feature replaces the worker-ranking part of Dynamo’s routing pipeline. A `WorkerFilter`

can exclude a host-eligible worker, a `WorkerScorer`

assigns a finite cost to each remaining worker, Dynamo adds costs from all configured scorers, and a `WorkerPicker`

chooses one row from the scored candidates. Filters run in declaration order. Each scorer receives all surviving workers in one call and writes one cost per worker. Rejecting every worker returns an error. Lower costs rank first by convention, but the picker can implement deterministic selection, sampling, tie-breaking, or policy-local state. Dynamo continues to own discovery, eligibility, score validation, accounting, and reservation.

For multiple compile-checked policies, see the [custom policy examples](https://github.com/ai-dynamo/dynamo/tree/main/examples/router/custom-policy-example). Repository contributors who use a coding agent must also provide the [worker-selection API rules](https://github.com/ai-dynamo/dynamo/blob/main/lib/kv-router/src/scheduling/CLAUDE.md).

## Use a Built-In Policy First

The Dynamo frontend ships built-in worker-selection policies, in [ lib/router-plugins](https://github.com/ai-dynamo/dynamo/tree/main/lib/router-plugins). Selecting one needs router-policy YAML only — no policy crate, no rebuild, no private image. See

[Worker-Selection Policies](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning#worker-selection-policies)for the available types and how to select one.

Write your own policy when no shipped policy expresses the rule you need. The rest of this page covers that case; a custom policy is added alongside the shipped ones, so you keep both.

## Choose the Policy Stage

An external policy owns its filters, scorers, and picker. Dynamo’s default scorer and picker are internal and can change with the built-in routing algorithm.

## Public Plugin API and Compatibility

Use `dynamo_kv_router::plugins`

for plugin registration and these modules for plugin contracts:

Dynamo owns scheduler queues, eligibility checks, reservations, lifecycle synchronization, and the default selector implementation. Low-level host interfaces such as `WorkerSelector`

are used to connect Dynamo components; external plugins use `WorkerSelectionPolicy`

.

Existing plugin imports and the `WorkerSelectionPolicyRegistry`

name remain available through compatibility re-exports until version 1.7. They refer to the same types and traits, so existing policies can register into `RouterPluginRegistry`

without adapters. Migrate imports to `plugins::worker_selection`

, rename the registry to `RouterPluginRegistry`

, and use `register_worker_selection`

for worker policies. The compatibility exports, registry alias, worker-only `register`

method, and frontend `worker_selection_policy_factory`

setter are scheduled for removal in 1.7.

## Build the Policy

### Create the Policy and Catalog Crates

Set the Dynamo checkout and policy project paths:

Add `dynamo-kv-router`

from the same checkout that builds the frontend or EPP:

### Filter Workers

A filter answers a hard yes-or-no question about one worker that already passed Dynamo’s eligibility checks. Return `true`

to keep the worker or `false`

to remove it. Use a filter only when the worker must not receive the request; use a scorer for preferences.

This filter keeps workers with at least the configured number of device-resident overlap blocks:

Dynamo runs filters in declaration order before scoring. A worker must pass every configured filter. If no workers remain, selection returns an error.

Pass filters to `WorkerSelectionPolicy::new_with_filters`

. If the policy has no hard requirement, omit filters and use `WorkerSelectionPolicy::new`

.

### Score Workers

A scorer expresses a preference without excluding a worker. It writes one finite cost for each worker into a host-owned output slice. Lower total cost is better by convention.

This scorer ranks workers by active requests above the batch minimum:

Dynamo calls `score`

once per scorer after filtering. The output slice matches the candidate order and length. Write every entry with a finite cost; an unwritten or invalid cost stops selection before picking.

A policy can stack multiple scorers. Dynamo calls them in declaration order and adds their costs. Dynamo rejects a non-finite contribution or total.

### Pick a Worker

A picker makes the final choice after filtering and scoring. It sees every remaining worker and its total cost, then returns one row index. Most policies pick the lowest cost, but a picker can instead sample, break ties, or use policy-local state.

This picker selects the lowest-cost row:

Candidate order is unspecified, so inspect explicit values instead of relying on row order. Dynamo rejects an out-of-range index before accounting or reservation.

### Parse Parameters and Create the Factory

The provider runs once at startup. Parse and validate all parameters there, then capture the validated values in the factory:

Dynamo calls the returned factory once per routing partition. Branch on the typed `WorkerType::Aggregated`

, `WorkerType::Prefill`

, `WorkerType::Decode`

, or `WorkerType::Encode`

role when worker pools need different components. Use the partition identity for distinct model or routing-group state.

### Register the Policy

Expose a registration function from the policy crate:

Call this function from the catalog:

Choose a stable, unique type name. Unknown types, duplicate registrations, and invalid parameters stop startup.

### Configure an Instance

Create `$POLICY_DIR/worker-selection.yaml`

:

The `type`

selects a registered provider. The `name`

identifies one configured instance. `worker_selection.aggregated`

, `worker_selection.prefill`

, `worker_selection.decode`

, and `worker_selection.encode`

select the matching worker pools. An omitted role uses Dynamo’s built-in policy; one role does not fall back to another role’s selection.

`worker_selection.encode`

applies only to a surface-carrying encode worker set that constructs the standard KV chooser. It does not configure the surface-less multimodal encoder hop: `EncoderRouter`

selects those workers independently with round-robin routing.

For prefill and decode, the selection order is the role-specific CLI or environment override, `DYN_ROUTER_WORKER_SELECTION_POLICY`

, the matching YAML selection, and then Dynamo’s built-in policy. For aggregated and encode, the order is `DYN_ROUTER_WORKER_SELECTION_POLICY`

, the matching YAML selection, and then the built-in policy. Set any selection to `default`

to use the built-in policy for that scope.

Role selections are startup settings. Configure them in the worker-selection YAML, with the CLI flags or environment variables above, or through the Python `KvRouterConfig`

constructor. They are not part of serialized `KvRouterConfig`

JSON, and `KvRouterConfig.from_json`

rejects those keys.

### Check the Policy and Catalog

Add one focused test for each policy decision and one registration test for every type name.

## Shared Plugin Construction

The catalog registers plugin providers once. `RouterPluginRegistry::resolve_plugins`

validates the selected configuration and returns a `RouterPlugins`

bundle containing the configured factories. Both the HTTP frontend and Python router pass this bundle to the shared router construction path. Each router receives fresh plugin instances; factories run during construction, not for each request.

Rust embedders start with the host registry, which includes the default policy, then register their catalog:

Each worker policy is constructed once per routing partition. An empty bundle retains the default selector.

## Available Signals

Worker identity and ordinary request metadata are always available. Dynamo calculates optional per-worker signals only for groups that a filter, scorer, or picker requests.

Routing cache resources start only if a component requests `CACHE`

. `serve_indexer`

and `enable_session_prefix_index`

also require `CACHE`

.

### Request Context

### Session Context

`session_context()`

returns `None`

when the request has no session metadata. This policy-facing view contains selected session metadata; it is not Dynamo’s internal request envelope. When present, it provides:

The [custom policy examples](https://github.com/ai-dynamo/dynamo/blob/main/examples/router/custom-policy-example/README.md) use `input_trigger()`

to give tool-result turns a cache-local picker path.

### Soft Session Affinity

Set `--router-session-affinity-mode soft`

with a session-affinity TTL to let a custom policy influence an existing session binding. The current binding enters the normal selection pipeline as `affinity_target()`

. The policy still receives the full host-eligible candidate set, subject to its own filters, and may select another worker. Dynamo rebinds the session after dispatch returns a response stream.

Match both fields when a policy wants to recognize the target. A target with `dp_rank: None`

matches every rank on its worker; a populated rank matches only that worker-rank pair. The target can be absent from the candidate table when the worker is unavailable or a custom filter rejects it.

Hard affinity remains the default. A hard binding and every explicit request target take the exact-target path instead of advisory custom selection. A selection, setup, or dispatch failure before a response stream leaves the previous soft binding intact. An error or cancellation after the stream is returned does not roll back a completed rebind.

The [custom policy examples](https://github.com/ai-dynamo/dynamo/blob/main/examples/router/custom-policy-example/README.md) include an overload-aware soft pinning policy that retains the advisory target until its active-request count exceeds a configured threshold, then selects the least-loaded alternative. Its two-Mocker walkthrough holds the first request open and verifies an `A -> B -> B`

worker sequence: overload moves the second request to B, and the third request retains B after load drains, proving that the plugin-selected dispatch updated the binding.

### Worker Identity and Cost

### Optional Worker Inputs

If a component needs no optional worker data, return `WorkerInputs::NONE`

. Combine exact groups with `|`

, such as `WorkerInputs::CACHE | WorkerInputs::LOAD`

.

The GPU, CPU, and disk overlap accessors return raw tier counts. A missing tier or worker entry is zero; Dynamo does not substitute its weighted effective-overlap estimate. Each custom scorer chooses how to combine the raw counts.

A filter or scorer reads groups through `WorkerCandidate::cache()`

or `load()`

. A picker reads index-aligned views through `WorkerInputView`

; its cache view supports `get(row)`

and `iter()`

. Each component must declare every group it reads; another component requesting a group does not grant access.

`WorkerCandidate::preferred_taint_multiplier()`

and `ScoredWorkerCandidate::preferred_taint_multiplier()`

return the optional cost multiplier from preferred routing constraints. A filter, scorer, or picker must request `WorkerInputs::PREFERRED_TAINT`

before reading the multiplier. Without that declaration, the component receives `None`

, even when another component requested the multiplier. Exact hard-pinned requests also do not materialize it. Required routing constraints remain host-enforced eligibility rules.

## Link the Policy Into Dynamo

Both paths use the same policy crate, catalog, and YAML file. Choose the process that owns worker selection.

###### Python Frontend

###### EPP

Add the catalog to the Python binding manifest. Keep the dependency alias `dynamo-worker-selection-policy-catalog`

:

Your catalog is registered alongside the [policies Dynamo ships](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/write-custom-routing-strategies#use-a-built-in-policy-first), not instead of them, so both remain selectable. Your catalog cannot reuse a shipped policy’s type name; the registry rejects the duplicate at startup rather than overriding it.

Build the extension with the linked catalog:

The role-specific CLI flags override the matching YAML fields for this process. In this command, `prefill-least-busy`

replaces `worker_selection.prefill`

, and `least-busy`

replaces `worker_selection.decode`

.

The linked extension also applies custom policies in `python3 -m dynamo.router`

. That process waits for a worker model card so it can choose built-in or custom policy behavior from the card’s typed role. `DYN_ROUTER_MODEL_CARD_WAIT_SECS`

bounds the startup wait and defaults to 600 seconds.

## Policy Contract

- Return
`true`

from a filter to keep a worker and`false`

to reject it. - Expect filters to run in declaration order before scoring. Rejecting every worker returns an error.
- Return finite scorer costs.
- Return a valid picker row.
- Treat candidate order as unspecified.
- Request only the signal groups that the component reads.
- Keep blocking I/O and panics out of
`keep`

,`score`

, and`pick`

. - Keep policy state local to the factory-created policy unless cross-partition sharing is a deliberate requirement.
- Build the policy against the same Dynamo revision as the frontend or EPP.
- If a signal adds work, storage, allocation, or another scan, run the worker-selection benchmark.

The [example README](https://github.com/ai-dynamo/dynamo/blob/main/examples/router/custom-policy-example/README.md) contains the in-tree package names and build-check commands. For the built-in cost model, see [Routing Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/routing-concepts). For the standalone selection lifecycle, see [Standalone Selection Service](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/standalone-selection).

## Default Policy Plugin

To give a worker role its own default-policy settings, select `dynamo-default-cost-fn`

:

The provider also accepts `overlap_score_credit_decay`

, `decode_active_request_weight`

, `host_cache_hit_weight`

, `disk_cache_hit_weight`

, and `shared_cache_multiplier`

. Omitted parameters inherit router configuration. Values must be finite and non-negative. Per-request score and temperature overrides do not apply to this policy. The builtin skips cache inputs at zero overlap credit and for plain disaggregated decode.