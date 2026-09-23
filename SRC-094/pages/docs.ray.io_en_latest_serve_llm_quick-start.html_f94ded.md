source: https://docs.ray.io/en/latest/serve/llm/quick-start.html
lastmod: 

# Quickstart[#](https://docs.ray.io#quickstart)

## Prerequisites[#](https://docs.ray.io#prerequisites)

```
pip install "ray[llm]"
```

Before you start:

**GPU**: most models need at least one GPU. The examples below use small Qwen models that fit on a single A10G or L4. Set`accelerator_type`

to a GPU available in your cluster.**Gated models**: to pull gated weights (for example, Llama) from the Hugging Face Hub, set`HF_TOKEN`

in the deployment’s`runtime_env`

. See[Deployment initialization](https://docs.ray.io/user-guides/deployment-initialization.html).

For a full description of every configuration field used below, see the [Configuration reference](https://docs.ray.io/user-guides/configuration.html).

## Deployment through OpenAiIngress[#](https://docs.ray.io#deployment-through-openaiingress)

You can deploy LLM models using either the builder pattern or bind pattern.

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
llm_config = LLMConfig(
model_loading_config={
"model_id": "qwen-0.5b",
"model_source": "Qwen/Qwen2.5-0.5B-Instruct",
},
deployment_config={
"autoscaling_config": {
"min_replicas": 1,
"max_replicas": 2,
}
},
# Pass the desired accelerator type (e.g. A10G, L4, etc.)
accelerator_type="A10G",
# You can customize the engine arguments (e.g. vLLM engine kwargs)
engine_kwargs={
"tensor_parallel_size": 2,
},
)
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

```
from ray import serve
from ray.serve.llm import LLMConfig
from ray.serve.llm.deployment import LLMServer
from ray.serve.llm.ingress import OpenAiIngress, make_fastapi_ingress
llm_config = LLMConfig(
model_loading_config=dict(
model_id="qwen-0.5b",
model_source="Qwen/Qwen2.5-0.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1, max_replicas=2,
)
),
# Pass the desired accelerator type (e.g. A10G, L4, etc.)
accelerator_type="A10G",
# You can customize the engine arguments (e.g. vLLM engine kwargs)
engine_kwargs=dict(
tensor_parallel_size=2,
),
)
# Deploy the application
server_options = LLMServer.get_deployment_options(llm_config)
server_deployment = serve.deployment(LLMServer).options(
**server_options).bind(llm_config)
ingress_options = OpenAiIngress.get_deployment_options(
llm_configs=[llm_config])
ingress_cls = make_fastapi_ingress(OpenAiIngress)
ingress_deployment = serve.deployment(ingress_cls).options(
**ingress_options).bind([server_deployment])
serve.run(ingress_deployment, blocking=True)
```

You can query the deployed models with either cURL or the OpenAI Python client:

```
curl -X POST http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer fake-key" \
-d '{
"model": "qwen-0.5b",
"messages": [{"role": "user", "content": "Hello!"}]
}'
```

```
from openai import OpenAI
# Initialize client
client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake-key")
# Basic chat completion with streaming
response = client.chat.completions.create(
model="qwen-0.5b",
messages=[{"role": "user", "content": "Hello!"}],
stream=True
)
for chunk in response:
if chunk.choices[0].delta.content is not None:
print(chunk.choices[0].delta.content, end="", flush=True)
```

For deploying multiple models, you can pass a list of [ LLMConfig](https://docs.ray.io/api/doc/ray.serve.llm.LLMConfig.html#ray.serve.llm.LLMConfig) objects to the

`OpenAiIngress`

deployment:```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
llm_config1 = LLMConfig(
model_loading_config=dict(
model_id="qwen-0.5b",
model_source="Qwen/Qwen2.5-0.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1, max_replicas=2,
)
),
accelerator_type="A10G",
)
llm_config2 = LLMConfig(
model_loading_config=dict(
model_id="qwen-1.5b",
model_source="Qwen/Qwen2.5-1.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1, max_replicas=2,
)
),
accelerator_type="A10G",
)
app = build_openai_app({"llm_configs": [llm_config1, llm_config2]})
serve.run(app, blocking=True)
```

```
from ray import serve
from ray.serve.llm import LLMConfig
from ray.serve.llm.deployment import LLMServer
from ray.serve.llm.ingress import OpenAiIngress, make_fastapi_ingress
llm_config1 = LLMConfig(
model_loading_config=dict(
model_id="qwen-0.5b",
model_source="Qwen/Qwen2.5-0.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1, max_replicas=2,
)
),
accelerator_type="A10G",
)
llm_config2 = LLMConfig(
model_loading_config=dict(
model_id="qwen-1.5b",
model_source="Qwen/Qwen2.5-1.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1, max_replicas=2,
)
),
accelerator_type="A10G",
)
# deployment #1
server_options1 = LLMServer.get_deployment_options(llm_config1)
server_deployment1 = serve.deployment(LLMServer).options(
**server_options1).bind(llm_config1)
# deployment #2
server_options2 = LLMServer.get_deployment_options(llm_config2)
server_deployment2 = serve.deployment(LLMServer).options(
**server_options2).bind(llm_config2)
# ingress
ingress_options = OpenAiIngress.get_deployment_options(
llm_configs=[llm_config1, llm_config2])
ingress_cls = make_fastapi_ingress(OpenAiIngress)
ingress_deployment = serve.deployment(ingress_cls).options(
**ingress_options).bind([server_deployment1, server_deployment2])
# run
serve.run(ingress_deployment, blocking=True)
```

## Production deployment[#](https://docs.ray.io#production-deployment)

For production deployments, Ray Serve LLM provides utilities for config-driven deployments. You can specify your deployment configuration with YAML files:

```
# config.yaml
applications:
- args:
llm_configs:
- model_loading_config:
model_id: qwen-0.5b
model_source: Qwen/Qwen2.5-0.5B-Instruct
accelerator_type: A10G
deployment_config:
autoscaling_config:
min_replicas: 1
max_replicas: 2
- model_loading_config:
model_id: qwen-1.5b
model_source: Qwen/Qwen2.5-1.5B-Instruct
accelerator_type: A10G
deployment_config:
autoscaling_config:
min_replicas: 1
max_replicas: 2
import_path: ray.serve.llm:build_openai_app
name: llm_app
route_prefix: "/"
```

```
# config.yaml
applications:
- args:
llm_configs:
- models/qwen-0.5b.yaml
- models/qwen-1.5b.yaml
import_path: ray.serve.llm:build_openai_app
name: llm_app
route_prefix: "/"
```

```
# models/qwen-0.5b.yaml
model_loading_config:
model_id: qwen-0.5b
model_source: Qwen/Qwen2.5-0.5B-Instruct
accelerator_type: A10G
deployment_config:
autoscaling_config:
min_replicas: 1
max_replicas: 2
```

```
# models/qwen-1.5b.yaml
model_loading_config:
model_id: qwen-1.5b
model_source: Qwen/Qwen2.5-1.5B-Instruct
accelerator_type: A10G
deployment_config:
autoscaling_config:
min_replicas: 1
max_replicas: 2
```

To deploy with either configuration file:

```
serve run config.yaml
```

For monitoring and observability, see [Observability](https://docs.ray.io/user-guides/observability.html).

## Next steps[#](https://docs.ray.io#next-steps)

Once you can deploy and query a model, the [User guides](https://docs.ray.io/user-guides/index.html) cover the next steps:

**Configure the deployment**: every field is documented in the[Configuration reference](https://docs.ray.io/user-guides/configuration.html).**Scale across GPUs and nodes**:[Cross-node parallelism](https://docs.ray.io/user-guides/cross-node-parallelism.html)distributes a model with tensor and pipeline parallelism.[Data parallel attention](https://docs.ray.io/user-guides/data-parallel-attention.html)raises throughput by replicating the model.**Tune latency and throughput**:[Prefill/decode disaggregation](https://docs.ray.io/user-guides/prefill-decode.html),[KV cache offloading](https://docs.ray.io/user-guides/kv-cache-offloading.html), and[Prefix-aware routing](https://docs.ray.io/user-guides/prefix-aware-routing.html).**Serve LoRA adapters**:[Multi-LoRA deployment](https://docs.ray.io/user-guides/multi-lora.html).**Monitor in production**:[Observability and monitoring](https://docs.ray.io/user-guides/observability.html).

To understand how these pieces fit together, see the [Architecture](https://docs.ray.io/architecture/index.html) docs.