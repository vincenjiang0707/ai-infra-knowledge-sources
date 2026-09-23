source: https://docs.ray.io/en/latest/serve/llm/user-guides/sglang.html
lastmod: 

# SGLang integration[#](https://docs.ray.io#sglang-integration)

Ray Serve LLM provides an OpenAI-compatible API that integrates with [SGLang](https://docs.sglang.ai/) via the `server_cls`

parameter on `LLMConfig`

. Most `engine_kwargs`

that work with `sglang serve`

also work here, giving you SGLang’s feature set through Ray Serve’s distributed deployment capabilities.

The integration uses `SGLangServer`

, a custom server class that wraps SGLang’s in-process engine and exposes chat, completions, embeddings, tokenize, and detokenize endpoints through the standard Ray Serve LLM protocol.

This compatibility means you can:

Use SGLang’s RadixAttention and other optimizations with Ray Serve’s production features

Deploy SGLang models with autoscaling, multi-model serving, and advanced routing

Serve models across multiple nodes with tensor and pipeline parallelism


Note

Community SGLang support is in early development. Track progress and provide feedback at [ray-project/ray#61114](https://github.com/ray-project/ray/issues/61114).

## Prerequisites[#](https://docs.ray.io#prerequisites)

```
pip install "ray[llm]" "sglang[all,ray]"
```

Set the following environment variable before running any example:

**CUDA:**`RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES=0`

**ROCm:**`RAY_EXPERIMENTAL_NOSET_HIP_VISIBLE_DEVICES=0`

**Intel GPU:**`RAY_EXPERIMENTAL_NOSET_ZE_AFFINITY_MASK=0`


## Online serving (single node)[#](https://docs.ray.io#online-serving-single-node)

Deploy a single-node SGLang model with autoscaling. The `server_cls`

parameter tells Ray Serve LLM to use the `SGLangServer`

instead of the default vLLM engine.

```
from ray.llm._internal.serve.engines.sglang import SGLangServer
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
llm_config = LLMConfig(
model_loading_config={
"model_id": "Llama-3.1-8B-Instruct",
"model_source": "unsloth/Llama-3.1-8B-Instruct",
},
deployment_config={
"autoscaling_config": {
"min_replicas": 1,
"max_replicas": 2,
}
},
server_cls=SGLangServer,
engine_kwargs={
"trust_remote_code": True,
"model_path": "unsloth/Llama-3.1-8B-Instruct",
"tp_size": 1,
"mem_fraction_static": 0.8,
},
)
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

```
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="fake-key")
# Chat completions
print("=== Chat Completions ===")
chat_response = client.chat.completions.create(
model="Llama-3.1-8B-Instruct",
messages=[
{"role": "user", "content": "List 3 countries and their capitals."},
],
temperature=0,
max_tokens=64,
)
print(chat_response.choices[0].message.content)
# Text completions
print("\n=== Text Completions ===")
completion_response = client.completions.create(
model="Llama-3.1-8B-Instruct",
prompt="San Francisco is a",
temperature=0,
max_tokens=30,
)
print(completion_response.choices[0].text)
```

```
# Chat completions
curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "Llama-3.1-8B-Instruct",
"messages": [{"role": "user", "content": "List 3 countries and their capitals."}],
"temperature": 0,
"max_tokens": 64
}'
# Text completions
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "Llama-3.1-8B-Instruct",
"prompt": "San Francisco is a",
"max_tokens": 30,
"temperature": 0
}'
```

**Run:**

```
RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES=0 serve run serve_sglang_example:app
```

## Online serving (multi-node with TP+PP)[#](https://docs.ray.io#online-serving-multi-node-with-tp-pp)

Deploy a large model across multiple nodes using tensor parallelism (TP=4) and pipeline parallelism (PP=2). This requires 2 nodes with 4 GPUs each (8 GPUs total).

For single-node deployments, `SGLangServer`

auto-generates a placement group with one bundle holding all local GPUs and a `STRICT_PACK`

strategy — you don’t need to pass `placement_group_config`

.

For multi-node deployments, you **must** supply `placement_group_config`

explicitly with **one bundle per node**, where each bundle holds that node’s full GPU allocation (e.g. `{"CPU": 1, "GPU": 4}`

for a 4-GPU node). This is required because `SGLangServer`

uses sglang’s `RayEngine`

backend, which indexes the placement group by node — every tp/pp rank assigned to a given node reuses the same bundle index, so a single bundle must contain that node’s entire GPU set. The number of bundles in `placement_group_bundles`

equals the number of nodes the deployment spans.

```
from ray.llm._internal.serve.engines.sglang import SGLangServer
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
llm_config = LLMConfig(
model_loading_config={
"model_id": "Llama-3.1-70B-Instruct",
"model_source": "meta-llama/Llama-3.1-70B-Instruct",
},
deployment_config={
"autoscaling_config": {
"min_replicas": 1,
"max_replicas": 2,
"target_ongoing_requests": 4,
}
},
# SGLangServer (RayEngine) requires one bundle per node, with each
# bundle holding that node's full GPU allocation. RayEngine indexes the
# placement group by node, so every tp/pp rank assigned to a given node
# reuses the same bundle index. With 2 nodes of 4 GPUs each, that means
# 2 bundles of {"GPU": 4}; STRICT_SPREAD assigns each bundle to a different node.
placement_group_config={
"placement_group_bundles": [
{"CPU": 1, "GPU": 4},
{"CPU": 1, "GPU": 4},
],
"placement_group_strategy": "STRICT_SPREAD",
},
server_cls=SGLangServer,
engine_kwargs={
"model_path": "meta-llama/Llama-3.1-70B-Instruct",
"tp_size": 4,
"pp_size": 2,
"mem_fraction_static": 0.8,
},
)
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

**Run:**

```
RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES=0 serve run sglang_multinode_example:app
```

## Limitations[#](https://docs.ray.io#limitations)

The following SGLang features are available upstream but not yet integrated into Ray Serve LLM. Community contributions are welcome:

**Engine replicas:**Multiple engine replicas within a single deployment. See[ray-project/ray#62480](https://github.com/ray-project/ray/issues/62480).**Observability:**Engine-level metrics (e.g. KV cache utilization, request queue depth).**Prefill disaggregation:**Separating prefill and decode phases across different workers.**Wide EP:**Wide expert parallelism for Mixture-of-Experts models.**Elastic EP:**Fault-tolerant expert parallelism with dynamic rank health tracking.**Transcriptions and score:**The`/v1/audio/transcriptions`

and`/v1/score`

endpoints.

## Dependencies[#](https://docs.ray.io#dependencies)

SGLang’s in-process engine overrides Python signal handlers on startup. The `SGLangServer.__init__`

includes a workaround that saves and restores signal handlers around engine initialization. If you encounter issues with graceful shutdown, this is a known area of friction.

## See also[#](https://docs.ray.io#see-also)

[Quickstart](https://docs.ray.io/quick-start.html)- Basic LLM deployment examples[Cross-node parallelism](https://docs.ray.io/cross-node-parallelism.html)- Cross-node parallelism with placement groups