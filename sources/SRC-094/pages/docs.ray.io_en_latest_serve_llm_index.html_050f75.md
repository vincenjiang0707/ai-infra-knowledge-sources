source: https://docs.ray.io/en/latest/serve/llm/index.html
lastmod: 

# Serving LLMs[#](https://docs.ray.io#serving-llms)

Ray Serve LLM deploys large language models in production. It builds on Ray Serve primitives for distributed, multi-node LLM serving and exposes an OpenAI-compatible API.

## Key features[#](https://docs.ray.io#key-features)

OpenAI-compatible API for chat, completions, and embeddings.

Multi-node, multi-model deployment with autoscaling and load balancing.

Parallelism strategies: tensor, pipeline, expert, and data parallel attention.

Prefill-decode disaggregation to scale the prefill and decode phases independently.

Custom request routing, including prefix-aware routing for higher cache hit rates.

Multi-LoRA serving on a shared base model.

Engine-agnostic backends such as vLLM and SGLang.

Built-in metrics and Grafana dashboards.


## Install[#](https://docs.ray.io#install)

Ray Serve LLM ships with Ray. Install it with the `llm`

extra:

```
pip install "ray[llm]"
```

This pulls in vLLM and the OpenAI-compatible server stack. You need a GPU to run most models. The [Quickstart](https://docs.ray.io/quick-start.html) covers prerequisites, supported hardware, and gated-model setup.

## Deploy your first model[#](https://docs.ray.io#deploy-your-first-model)

Define an [ LLMConfig](https://docs.ray.io/api/doc/ray.serve.llm.LLMConfig.html#ray.serve.llm.LLMConfig), build an OpenAI-compatible app, and run it:

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

Once it is running, query it with any OpenAI client at `http://localhost:8000/v1`

. See the [Quickstart](https://docs.ray.io/quick-start.html) for client snippets, multi-model apps, and config-driven (YAML) deployments.

## Find your path[#](https://docs.ray.io#find-your-path)

**New here?**Start with the[Quickstart](https://docs.ray.io/quick-start.html)to deploy and query a model.**Configuring a deployment?**The[Configuration reference](https://docs.ray.io/user-guides/configuration.html)explains every`LLMConfig`

field.**Scaling up?**The[User guides](https://docs.ray.io/user-guides/index.html)cover parallelism, routing, caching, LoRA, and observability.**Want the internals?**The[Architecture](https://docs.ray.io/architecture/index.html)docs explain components, request flow, and serving patterns.**Deploying a specific model?**The[Examples](https://docs.ray.io/examples.html)walk through small, medium, large, vision, and reasoning models end to end.**Hitting an issue?**Check[Troubleshooting](https://docs.ray.io/troubleshooting.html)and[Benchmarks](https://docs.ray.io/benchmarks.html).