source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/overview
lastmod: 2026-09-24T19:58:16.636Z

AI Simulate (Experimental)


AI Simulate (Experimental)

Experimental simulation and configuration-search tools for Dynamo deployments

**Experimental.** AI Simulate is intended for evaluation and feedback, not production capacity
planning. Its Python APIs, configuration schemas, search results, and deployment output may
change without a standard deprecation period. It provides no SLA, accuracy, or
configuration-optimality guarantees.

AI Simulate is a standalone Python distribution in the Dynamo repository. It contains simulation
and configuration-search tools that use Dynamo models and replay without making those tools part
of the stable `ai-dynamo`

Python API.

## Spica

[Spica](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/overview) is AI Simulate’s first package. It searches engine, router, Planner, and
parallelism settings with a black-box optimizer, accepts pinned G2 host-offload settings, and
conditionally searches router cache-hit weights. It evaluates candidates with Dynamo Replay and
supports scalar and Pareto-front objectives.

Spica requires the matching Dynamo runtime from the same source revision. Follow the
[Spica development setup](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/overview#develop), then invoke the package module:

The `dynamo-planner`

container builds and installs this distribution. AI Simulate is not included
in the `ai-dynamo`

wheel and does not add an `ai-dynamo[spica]`

extra or a console script.