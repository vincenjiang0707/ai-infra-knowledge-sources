source: https://docs.nvidia.com/dynamo/v1.3.0/digest/tokenspeed-day-0
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Day 0 support for TokenSpeed

A short launch note for running TokenSpeed with Dynamo — May 2026

[TokenSpeed](https://lightseek.org/blog/lightseek-tokenspeed.html) ([GitHub](https://github.com/lightseekorg/tokenspeed)) launched today as LightSeek’s new inference engine for agentic workloads. The initial repo is a preview, with more model coverage and runtime features landing over the next few weeks.

Two pieces are worth calling out. First, TokenSpeed includes new MLA kernel work for long-context Kimi-style workloads on Blackwell. Second, TokenSpeed has a native C++ scheduler in `tokenspeed-scheduler/`

that models request flow and cache operations as explicit state machines, while Python remains the runtime and integration layer.

Dynamo now has day-0 support for running TokenSpeed as a Dynamo backend through `python -m dynamo.tokenspeed`

. The Dynamo frontend remains the user-facing OpenAI-compatible API entrypoint and handles request routing, streaming responses, and cancellation.

See the [Kimi K2.5 TokenSpeed recipe](https://github.com/ai-dynamo/dynamo/tree/main/recipes/kimi-k2.5/tokenspeed/agg/nvidia) for the current Dynamo launch recipe.

Things are moving quickly. Upstream TokenSpeed calls out ongoing work on model coverage, P/D, EPLB, KV store, Mamba cache, VLM, metrics, Hopper optimization, and related runtime features.