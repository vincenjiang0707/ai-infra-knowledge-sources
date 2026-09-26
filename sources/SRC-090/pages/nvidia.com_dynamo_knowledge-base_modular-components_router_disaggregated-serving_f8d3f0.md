source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving
lastmod: 2026-09-24T19:58:16.636Z

# Disaggregated Serving

Dynamo supports disaggregated serving where prefill (prompt processing) and decode (token generation) are handled by separate worker pools. The frontend activates an internal prefill router when it discovers compatible typed prefill and decode services.

For the high-level deployment matrix, see [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide). For the router flags used in this setup, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).

If prefill and decode workers span topology domains such as zones or racks, use [Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/topology-aware-kv-transfer) to constrain or bias decode routing toward workers in the selected prefill worker’s transfer domain.

## Automatic Prefill Router Activation

The prefill router is automatically created when:

- A decode worker is registered with
`WorkerType.Decode`

, for example via`register_model()`

with`ModelType.Chat | ModelType.Completions`

. - A prefill service in the same Runtime namespace is registered with the same model name and
`WorkerType.Prefill`

.

Key characteristics of the prefill router:

**Always disables active block tracking**(`track_active_blocks=false`

) since prefill workers do not perform decode.**Runs between preprocessing and decode routing**and returns handoff metadata for the selected decode worker.**Uses decode-only routing when no prefill router is active.**Once a request has been dispatched to prefill, a prefill or handoff failure is returned to the request; it does not retry through an aggregated decode-only path.

Key characteristics of the decode routing stage in disaggregated mode:

**Disables overlap scoring**(`overlap_score_credit=0`

) because decode routing should not chase prefix reuse.**Disables KV reuse assumption**(`assume_kv_reuse=false`

) unless the backend can truly deduplicate transferred blocks.**Disables prefill-token tracking**(`track_prefill_tokens=false`

) so decode-side load reflects decode work rather than already-completed prompt work.

The Rust router contains an experimental conditional bypass path for programmatic or embedded configurations. It can keep a cache-hot request on a selected decode worker instead of performing remote prefill. The standard `dynamo.frontend`

and standalone Python router CLIs do not expose that configuration, so ordinary CLI deployments follow the prefill-handoff-decode flow documented below.

## Setup Example

When both workers are registered, requests are automatically routed.

The automatic disaggregated routing setup described here is currently supported by the integrated `dynamo.frontend`

path. It is not provided as a single turnkey mode by the standalone Python router (`python -m dynamo.router`

). If you build this topology with standalone routers, you must launch and connect the prefill and decode routing stages yourself and handle request handoff, including the `disaggregated_params`

returned by prefill. For an advanced reference, see the [Global Router](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/components/src/dynamo/global_router), which composes local prefill and decode router pools explicitly.

## Request Flow

The following diagram shows an overview of the major components in disaggregated serving:

When topology-aware KV transfer is enabled, the prefill router also derives decode `RoutingConstraints`

from the selected prefill worker’s runtime topology metadata before the request enters the decode router.