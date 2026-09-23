source: https://docs.ray.io/en/latest/serve/llm/architecture/serving-patterns/index.html
lastmod: 

# Serving patterns[#](https://docs.ray.io#serving-patterns)

Architecture documentation for distributed LLM serving patterns.

## Overview[#](https://docs.ray.io#overview)

Ray Serve LLM supports several serving patterns that can be combined for complex deployment scenarios:

[Data parallel attention](https://docs.ray.io/data-parallel.html): scale throughput by running multiple coordinated engine replicas that process requests in parallel, replicating attention while sharding requests across the replicas.[Prefill-decode disaggregation](https://docs.ray.io/prefill-decode.html): optimize resource utilization by separating prompt processing from token generation.

These patterns are composable and can be mixed to meet specific requirements for throughput, latency, and cost optimization.

These pages describe how each pattern works. For step-by-step configuration, see the matching how-to guides: [Data parallel attention](https://docs.ray.io/user-guides/data-parallel-attention.html) and [Prefill/decode disaggregation](https://docs.ray.io/user-guides/prefill-decode.html).