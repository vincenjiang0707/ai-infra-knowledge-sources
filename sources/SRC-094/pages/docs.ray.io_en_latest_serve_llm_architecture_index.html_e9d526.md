source: https://docs.ray.io/en/latest/serve/llm/architecture/index.html
lastmod: 

# Architecture[#](https://docs.ray.io#architecture)

How Ray Serve LLM is built: the components a deployment is made of, how a request flows through them, and the patterns that scale serving across GPUs and nodes. Read these to extend the system or to reason about performance. To deploy models, see the [User guides](https://docs.ray.io/user-guides/index.html) instead.

Start with the overview, then read the pages relevant to your use case:

[Architecture overview](https://docs.ray.io/overview.html): the components of a deployment (engine, server, ingress) and how a request flows through them. Read this first.[Core components](https://docs.ray.io/core.html): the key abstractions and extension points, including the engine protocol,`LLMConfig`

, the builder functions, and custom server classes.[Serving patterns](https://docs.ray.io/serving-patterns/index.html): distributed patterns (data parallel attention, prefill-decode disaggregation) and how they compose.[Request routing](https://docs.ray.io/routing-policies.html): how a replica is selected for each request, the built-in policies, and how to write a custom router.