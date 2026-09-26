source: https://github.com/vllm-project/guidellm/issues/1158

### Problem Statement

When benchmarking multi-tenant or Multi-LoRA serving on vLLM (e.g., running --enable-lora with multiple adapters loaded), GuideLLM currently only allows targeting a single model or adapter per benchmarking run via the --model parameter.

To benchmark multiple adapters simultaneously today, users must execute multiple detached GuideLLM instances

Fragmented Reporting: There is no way to generate a single, unified SLO report that captures global vLLM server metrics (P99 latency, TTFT, throughput) alongside per-adapter performance breakdowns.

Inaccurate KV-Cache Contention Modeling: Running separate, uncoordinated benchmark processes fails to accurately simulate how vLLM’s single global PagedAttention memory pool degrades under synchronized, multi-tenant memory pressure and cache eviction.

Lack of Traffic Distribution Simulation: Real-world production traffic across adapters is rarely equal. Infrastructure engineers cannot model non-uniform workloads (e.g., 70% traffic to hr-bot, 20% to legal-bot, and 10% to sql-bot) in a single run.

### Proposed Solution

Introduce native Multi-LoRA / Multi-Tenant Workload Simulation to GuideLLM, enabling a single benchmark execution to target multiple models/adapters dynamically with configurable traffic distributions and concurrency ratios.

Key Architectural Changes:

Data Profile & Sampling Extension (guidellm.core.data):

Introduce a multi-tenant workload profile that accepts a map of adapter names and their respective traffic weights or concurrency targets (e.g., hr-bot:0.7,legal-bot:0.2,sql-bot:0.1).

e.g :

```
guidellm run \
--backend kind=openai_http,target=http://localhost:8000 \
--data kind=multi_tenant,adapters=hr-bot:0.7,legal-bot:0.2,sql-bot:0.1
```


or something of that nature.

### Alternatives Considered

*No response*

### Usage Examples

### Additional Context

*No response*

## Problem Statement

When benchmarking multi-tenant or Multi-LoRA serving on vLLM (e.g., running --enable-lora with multiple adapters loaded), GuideLLM currently only allows targeting a single model or adapter per benchmarking run via the --model parameter.

To benchmark multiple adapters simultaneously today, users must execute multiple detached GuideLLM instances

Fragmented Reporting: There is no way to generate a single, unified SLO report that captures global vLLM server metrics (P99 latency, TTFT, throughput) alongside per-adapter performance breakdowns.

Inaccurate KV-Cache Contention Modeling: Running separate, uncoordinated benchmark processes fails to accurately simulate how vLLM’s single global PagedAttention memory pool degrades under synchronized, multi-tenant memory pressure and cache eviction.

Lack of Traffic Distribution Simulation: Real-world production traffic across adapters is rarely equal. Infrastructure engineers cannot model non-uniform workloads (e.g., 70% traffic to hr-bot, 20% to legal-bot, and 10% to sql-bot) in a single run.

## Proposed Solution

Introduce native Multi-LoRA / Multi-Tenant Workload Simulation to GuideLLM, enabling a single benchmark execution to target multiple models/adapters dynamically with configurable traffic distributions and concurrency ratios.

Key Architectural Changes:

Data Profile & Sampling Extension (guidellm.core.data):

Introduce a multi-tenant workload profile that accepts a map of adapter names and their respective traffic weights or concurrency targets (e.g., hr-bot:0.7,legal-bot:0.2,sql-bot:0.1).

e.g :

or something of that nature.

## Alternatives Considered

No response## Usage Examples

## Additional Context

No response