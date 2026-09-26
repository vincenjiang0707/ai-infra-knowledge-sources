source: https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-the-dynamo-frontend
lastmod: 2026-09-25T12:26:00.485Z

# Using the Dynamo Frontend

In this topology, the Dynamo Frontend receives each request and selects the worker most likely to already hold the prompt’s KV cache prefix. Use it when clients send requests directly to a Dynamo Frontend Service. If a Kubernetes Gateway receives requests first, use [GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo) instead.

Turning it on in a DynamoGraphDeployment (DGD) takes two steps: switch the **Frontend** into KV mode, and have the **workers** publish KV cache events so the router knows what each worker has cached. This is a [how-to](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd) for an existing deployment. For the routing cost model and concepts, see [Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts); for the full flag and env reference, see the [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide).

### Put the Frontend in KV mode

Set `--router-mode kv`

on the Frontend container, or the equivalent `DYN_ROUTER_MODE=kv`

environment variable:

That alone gives you cache-aware routing using load signals. To make routing decisions from real cache contents, complete the next step.

### Publish KV events from the workers

For the router to track which blocks each worker holds, workers must publish KV cache events. On a vLLM worker, add `--kv-events-config`

:

This is the half that the [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide) does not show. Without it, the router falls back to load-only decisions even in `kv`

mode.

The Frontend and worker snippets above are drawn from the [disagg-kv-router recipe](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/recipes/qwen3-32b/vllm/disagg-kv-router/deploy.yaml), where six prefill workers publish KV events and the Frontend routes across them.

## Tuning Knobs

The KV router scores each worker as `prefill_load_scale * adjusted_prefill_blocks + decode_blocks`

, where cache-overlap credit subtracts from the prefill load. Two knobs shift that balance; set them as Frontend `args`

(or the `DYN_*`

env equivalents). Start with the defaults and adjust only if you have a measured TTFT or ITL problem.

For the flag/env/default reference, see the [Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router); for the full cost-model detail and every related flag, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#tuning-guidelines).

### Cache-Overlap Credit

`--router-kv-overlap-score-credit`

(env `DYN_ROUTER_KV_OVERLAP_SCORE_CREDIT`

) is the primary cache-reuse knob. It credits device-local prefix overlap against a worker’s prefill load, biasing requests toward workers that already hold the prompt’s prefix.

**Range:**`0.0`

to`1.0`

.**Default:**`1.0`

.**Raise toward**to prioritize cache reuse and lower TTFT — the router more aggressively co-locates requests that share a prefix.`1.0`

**Lower toward**to spread load more evenly and lower ITL, at the cost of more redundant prefills.`0.0`

`0.0`

ignores prefix caches entirely and skips building the local indexer (equivalent to load-only routing).

Most deployments should leave this at `1.0`

. Lower it only when cache-rich workers are getting overloaded while others sit idle.

### Prompt-Side Load Weight

`--router-prefill-load-scale`

(env `DYN_ROUTER_PREFILL_LOAD_SCALE`

) scales the prompt-side prefill load after overlap credit is applied, setting how much prompt work counts relative to decode-side block load.

**Minimum:**`0.0`

(ignore prompt-side load).**Default:**`1.0`

. No hard maximum — values above`1.0`

weight prefill more heavily.**Raise above**when long prompts are saturating workers and you want the router to steer new requests away from workers already doing heavy prefill.`1.0`

**Lower below**when decode-side pressure dominates and you want routing driven mainly by active decode blocks.`1.0`


### Route on Load Only

`--no-router-kv-events`

(env `DYN_ROUTER_USE_KV_EVENTS=false`

) disables event tracking; the router predicts cache state from its own routing decisions with TTL-based expiration instead of consuming real KV events. Use it only when you are not confident the backend emits KV events correctly.

## Routing with Disaggregated Serving

In a disaggregated graph, the router operates over prefill and decode workers separately. The prefill workers publish KV events (the second step above) and the router selects among them; the internal prefill router activates automatically. See [Router with Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving).

## Related Pages

[KV-Aware Routing on Kubernetes](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/overview)— compare the Frontend and GAIE topologies.[Using GAIE with Dynamo](https://docs.nvidia.com/dynamo/kubernetes/kv-aware-routing/using-gaie-with-dynamo)— place endpoint selection in the Dynamo EPP.[Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide)— deployment modes, full CLI and env reference.[Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts)— cost model and worker selection.[Router with Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving)— prefill/decode routing.