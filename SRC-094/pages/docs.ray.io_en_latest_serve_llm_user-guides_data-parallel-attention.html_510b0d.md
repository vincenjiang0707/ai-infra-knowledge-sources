source: https://docs.ray.io/en/latest/serve/llm/user-guides/data-parallel-attention.html
lastmod: 

# Data parallel attention[#](https://docs.ray.io#data-parallel-attention)

Deploy LLMs with data parallel attention for increased throughput and better resource utilization, especially for sparse MoE (Mixture of Experts) models.

Data parallel attention creates multiple coordinated inference engine replicas that process requests in parallel. This pattern is most effective when combined with expert parallelism for sparse MoE models, where attention (QKV) layers are replicated across replicas while MoE experts are sharded. This separation provides:

**Increased throughput**: Process more concurrent requests by distributing them across multiple replicas.**Better resource utilization**: Especially beneficial for sparse MoE models where not all experts are active for each request.**KV cache scalability**: Add more KV cache capacity across replicas to handle larger batch sizes.**Expert saturation**: Achieve higher effective batch sizes during decoding to better saturate MoE layers.

## When to use data parallel attention[#](https://docs.ray.io#when-to-use-data-parallel-attention)

Consider this pattern when:

**Sparse MoE models with MLA**: You’re serving models with Multi-head Latent Attention (MLA) where KV cache can’t be sharded along the head dimension. MLA reduces KV cache memory requirements, making data parallel replication more efficient.**High throughput requirements**: You need to serve many concurrent requests and want to maximize throughput.**KV-cache limited**: Adding more KV cache capacity increases throughput, and data parallel attention effectively increases KV cache capacity across replicas.

**When not to use data parallel attention:**

**Low to medium throughput**: If you can’t saturate the MoE layers, data parallel attention adds unnecessary complexity.**Non-MoE models**: The main benefit is lifting effective batch size for saturating experts, which doesn’t apply to dense models.**Sufficient tensor parallelism**: For models with GQA (Grouped Query Attention), use tensor parallelism (TP) first to shard KV cache up to`TP_size <= num_kv_heads`

. Beyond that, TP requires KV cache replication—at that point, data parallel attention becomes a better choice.

## Basic deployment[#](https://docs.ray.io#basic-deployment)

The following example shows how to deploy with data parallel attention. Each data parallel deployment requires `num_replicas * data_parallel_size * tensor_parallel_size`

GPUs.

```
from ray import serve
from ray.serve.llm import LLMConfig, build_dp_openai_app
# Configure the model with data parallel settings
config = LLMConfig(
model_loading_config={
"model_id": "microsoft/Phi-tiny-MoE-instruct"
},
deployment_config={
"num_replicas": 2
},
engine_kwargs={
"data_parallel_size": 2, # Number of DP replicas
"tensor_parallel_size": 1, # TP size per replica
# Reduced for CI compatibility
"max_model_len": 1024,
"max_num_seqs": 32,
},
)
app = build_dp_openai_app({
"llm_config": config
})
serve.run(app, blocking=True)
```

## Production YAML configuration[#](https://docs.ray.io#production-yaml-configuration)

For production deployments, use a declarative YAML configuration file:

```
applications:
- name: dp_llm_app
route_prefix: /
import_path: ray.serve.llm:build_dp_openai_app
args:
llm_config:
model_loading_config:
model_id: Qwen/Qwen2.5-0.5B-Instruct
deployment_config:
num_replicas: 2
engine_kwargs:
data_parallel_size: 4
tensor_parallel_size: 2
```

Deploy with CLI:

```
serve deploy dp_config.yaml
```

## Configuration parameters[#](https://docs.ray.io#configuration-parameters)

### Required parameters[#](https://docs.ray.io#required-parameters)

`data_parallel_size`

: Number of data parallel replicas within a data parallel group. Must be a positive integer and passed in via`engine_kwargs`

.

### Deployment configuration[#](https://docs.ray.io#deployment-configuration)

`num_replicas`

: Can be set to any positive integer, unset (defaults to 1), or`"auto"`

to enable autoscaling based on request queue length.

Note

Within a data parallel deployment, `num_replicas`

under the `deployment_config`

refers to the number of data parallel groups, which translates to `num_replicas * data_parallel_size`

data parallel replicas (equivalent to the number of Ray serve replicas). Each data parallel replica inherently runs a vLLM data parallel server.

## Understanding data parallel replica coordination[#](https://docs.ray.io#understanding-data-parallel-replica-coordination)

In data parallel attention, all data parallel replicas within a data parallel group work together as a cohesive unit by leveraging Ray Serve’s gang scheduling capability:

**Rank assignment**: Each replica receives a unique rank (0 to`data_parallel_size-1`

) from Ray Serve’s controller to start a vLLM data parallel server.**Request distribution**: Ray Serve’s request router distributes requests across replicas using load balancing.**Collective operations**: Replicas coordinate for collective operations (e.g., all-reduce, dispatch and combine) required by the model.**Synchronization**: All data parallel replicas in a data parallel group must be present and healthy. MoE layers use all-to-all collectives to route tokens to experts across DP ranks. If any data parallel replica is unavailable, these collectives hang and tokens can’t reach experts assigned to that rank.**Fault tolerance**: If any data parallel replica in a data parallel group fails, the entire group becomes unavailable because the remaining replicas can’t complete collective operations. While Ray Serve controller detects the failure and restarts the entire group, other data parallel groups keep serving requests without any downtime if`num_replicas > 1`

.

There’s no coordination overhead introduced by Ray Serve LLM:

**Startup**: Data parallel ranks are assigned when Ray Serve’s controller creates the data parallel replica.**Runtime**: No coordination overhead during request processing.

For more details, see [Data parallel attention](https://docs.ray.io/architecture/serving-patterns/data-parallel.html).

## Test your deployment[#](https://docs.ray.io#test-your-deployment)

Test with a chat completion request:

```
curl -X POST "http://localhost:8000/v1/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer fake-key" \
-d '{
"model": "Qwen/Qwen2.5-0.5B-Instruct",
"messages": [
{"role": "user", "content": "Explain data parallel attention"}
],
"max_tokens": 100,
"temperature": 0.7
}'
```

You can also test programmatically:

```
from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="fake-key"
)
response = client.chat.completions.create(
model="Qwen/Qwen2.5-0.5B-Instruct",
messages=[
{"role": "user", "content": "Explain data parallel attention"}
],
max_tokens=100
)
print(response.choices[0].message.content)
```

## Combining with other patterns[#](https://docs.ray.io#combining-with-other-patterns)

### Data parallel + Prefill-decode disaggregation[#](https://docs.ray.io#data-parallel-prefill-decode-disaggregation)

You can combine data parallel attention with prefill-decode disaggregation to scale both phases independently while using DP within each phase. This pattern is useful when you need high throughput for both prefill and decode phases.

The following example shows a complete, functional deployment:

```
from ray import serve
from ray.serve.llm import LLMConfig, build_pd_openai_app
# Configure prefill with data parallel attention
prefill_config = LLMConfig(
model_loading_config={
"model_id": "microsoft/Phi-tiny-MoE-instruct"
},
engine_kwargs={
"data_parallel_size": 2, # 2 DP replicas for prefill
"tensor_parallel_size": 1,
"kv_transfer_config": {
"kv_connector": "NixlConnector",
"kv_role": "kv_both",
},
# Reduced for CI compatibility
"max_model_len": 1024,
"max_num_seqs": 32,
},
)
# Configure decode with data parallel attention
decode_config = LLMConfig(
model_loading_config={
"model_id": "microsoft/Phi-tiny-MoE-instruct"
},
engine_kwargs={
"data_parallel_size": 2, # 2 DP replicas for decode
"tensor_parallel_size": 1,
"kv_transfer_config": {
"kv_connector": "NixlConnector",
"kv_role": "kv_both",
},
# Reduced for CI compatibility
"max_model_len": 1024,
"max_num_seqs": 32,
},
)
# Build and deploy the PD application (3-tier: ingress -> decode -> prefill)
# PDDecodeServer orchestrates remote prefill then runs local decode.
app = build_pd_openai_app(
{
"prefill_config": prefill_config,
"decode_config": decode_config,
}
)
serve.run(app, blocking=True)
```

This configuration creates:

**Prefill phase**: 2 data parallel replicas for processing input prompts**Decode phase**: 2 data parallel replicas for generating tokens**PDDecodeServer**: Orchestrates remote prefill then runs local decode**OpenAI ingress**: Provides OpenAI-compatible API endpoints

With this setup, you can:

Optimize prefill and decode phases independently based on workload characteristics

Use data parallel attention within each phase for increased throughput


Note

This example uses 4 GPUs total (2 for prefill, 2 for decode). Adjust the `data_parallel_size`

values based on your available GPU resources.

Note

For this example to work, you need to have NIXL installed. See the [Prefill/decode disaggregation](https://docs.ray.io/prefill-decode.html) guide for prerequisites and installation instructions.

## See also[#](https://docs.ray.io#see-also)

[Data parallel attention](https://docs.ray.io/architecture/serving-patterns/data-parallel.html)- Data parallel attention architecture details[Prefill/decode disaggregation](https://docs.ray.io/prefill-decode.html)- Prefill-decode disaggregation guide[Serving patterns](https://docs.ray.io/architecture/serving-patterns/index.html)- Overview of serving patterns[Quickstart](https://docs.ray.io/quick-start.html)- Basic LLM deployment examples