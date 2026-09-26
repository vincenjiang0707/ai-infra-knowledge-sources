source: https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/overview
lastmod: 2026-09-24T19:58:16.636Z

# Router

Choose a request path, understand worker selection, and operate KV-aware routing.

The Dynamo KV router selects an eligible worker using reusable KV cache state and projected active load. Use it when prefix reuse should influence placement; use a non-KV routing mode when your deployment needs only load balancing or an externally selected worker.

## Start With Your Request Path

Choose the page that matches where requests enter Dynamo:

For a topology comparison and the configuration boundary between the Frontend and workers, see the [Router Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide).

## Follow a Request Through the Router

- The request host tokenizes and normalizes the request.
- The router filters workers that cannot serve it.
- The router scores eligible workers using cache overlap and projected load.
- Aggregated deployments run on the selected worker, while disaggregated deployments select separate prefill and decode workers. Workers publish KV lifecycle events when available; set
`--no-router-kv-events`

to predict cache state when the router cannot consume them.

Read [KV-Aware Routing](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/system-architecture/kv-aware-routing) for the architecture-level flow. Read [Routing Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/routing-concepts) for the cost model, [Router Filtering](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-filtering) for eligibility, and [Deficit Round Robin Queue Scheduling](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/deficit-round-robin) for policy-class arbitration.

## Continue by Task

The [Frontend Configuration Reference](https://docs.nvidia.com/dynamo/dev/reference/components/frontend-configuration#router) is the canonical source for embedded-router flags, environment variables, defaults, and boolean forms.