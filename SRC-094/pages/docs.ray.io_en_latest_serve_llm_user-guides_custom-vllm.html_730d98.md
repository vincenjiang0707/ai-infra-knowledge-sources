source: https://docs.ray.io/en/latest/serve/llm/user-guides/custom-vllm.html
lastmod: 

# Custom vLLM models[#](https://docs.ray.io#custom-vllm-models)

This page provides an example of serving a custom vLLM model with Ray Serve LLM.

The example model is a custom reward model composed of Qwen3-0.6B with its vocabulary LM head replaced by a scalar reward head. The model reuses vLLM’s Qwen3 backbone, scores the last token, and returns the reward through vLLM’s `/classify`

endpoint.

## How does Ray Serve LLM support custom vLLM models?[#](https://docs.ray.io#how-does-ray-serve-llm-support-custom-vllm-models)

Ray Serve LLM serves any architecture that vLLM supports. When your model isn’t a [built-in vLLM architecture](https://docs.vllm.ai/en/stable/models/supported_models.html), you add it with a [vLLM plugin](https://docs.vllm.ai/en/stable/design/plugin_system.html): a custom package that registers the architecture in vLLM’s model registry without patching vLLM. Ray Serve LLM then serves it through the same OpenAI-compatible API as any other model.

## Prerequisites[#](https://docs.ray.io#prerequisites)

Install Ray with the LLM extra:

```
pip install "ray[llm]"
```

## Write the plugin[#](https://docs.ray.io#write-the-plugin)

Compose the plugin as an installable Python package. The following is an example layout:

```
qwen3-reward-plugin/ # project directory -- run `pip install .` here
├── setup.py # packaging metadata and the vLLM entry point
└── qwen3_reward_plugin/ # the importable package
├── __init__.py # register(): adds the architecture to vLLM's model registry
├── qwen3_rm.py # Qwen3CustomRewardModel: the model class
└── serve_hook.py # RewardModelServer: registers the plugin in the Ray Serve LLM replica
```

### Model class[#](https://docs.ray.io#model-class)

Subclass vLLM’s `Qwen3ForCausalLM`

to reuse its backbone, then attach the reward head and a last-token classification pooler. See the full model class [here](https://github.com/ray-project/ray/tree/master/doc/source/llm/doc_code/serve/custom_vllm/qwen3_reward_plugin/qwen3_rm.py).

### Register the architecture[#](https://docs.ray.io#register-the-architecture)

vLLM calls `register()`

in every process it starts, the driver, the engine core, and each rank worker, through vLLM’s `load_general_plugins()`

.

```
"""vLLM plugin entry point: register the custom architecture."""
def register() -> None:
from vllm import ModelRegistry
if "Qwen3CustomRewardModel" not in ModelRegistry.get_supported_archs():
ModelRegistry.register_model(
"Qwen3CustomRewardModel",
"qwen3_reward_plugin.qwen3_rm:Qwen3CustomRewardModel",
)
```

### Package it[#](https://docs.ray.io#package-it)

Declare the `vllm.general_plugins`

entry point in `setup.py`

. vLLM discovers the package and runs `register()`

when the package installs.

```
from setuptools import setup
setup(
name="qwen3-reward-plugin",
version="0.1.0",
packages=["qwen3_reward_plugin"],
# vLLM discovers and runs this entry point in every process (the engine core
# and each rank worker) via load_general_plugins().
entry_points={
"vllm.general_plugins": [
"qwen3_reward = qwen3_reward_plugin:register",
],
},
)
```

Install the plugin into the image your Ray cluster runs, alongside vLLM, so every node and every vLLM engine and worker process can discover it:

```
pip install . # from the plugin project directory
```

## Deploy the model[#](https://docs.ray.io#deploy-the-model)

Configure the model as a pooling deployment, enable direct streaming, then launch it with the Python API or a YAML config.

### Configure the model[#](https://docs.ray.io#configure-the-model)

Set `runner="pooling"`

because a reward model encodes rather than generates, and use `engine_kwargs.hf_overrides`

to select the custom architecture and configure a single regression score (`num_labels=1`

, `problem_type="regression"`

for an identity activation).

The plugin entry point registers the architecture in the vLLM engine and worker processes. Ray Serve LLM also resolves and validates the architecture while it builds the engine configuration, so register it there too: point `server_cls`

at an `LLMServer`

subclass whose import calls `register()`

.

```
"""LLMServer subclass for ``LLMConfig.server_cls``: importing it registers the plugin."""
from ray.llm._internal.serve.core.server.llm_server import LLMServer
from qwen3_reward_plugin import register
register()
class RewardModelServer(LLMServer):
pass
```

### Enable direct streaming[#](https://docs.ray.io#enable-direct-streaming)

Serve with [direct streaming](https://docs.ray.io/direct-streaming.html) so vLLM’s native `/classify`

route is exposed. Export both environment variables before starting Serve:

```
export RAY_SERVE_ENABLE_HA_PROXY=1
export RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING=1
```

### Deploy[#](https://docs.ray.io#deploy)

Deploy with the Python API or an equivalent YAML config:

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Serve Qwen3-0.6B with a scalar reward head from the `qwen3_reward_plugin`
# vLLM plugin (pip install it into your cluster image).
llm_config = LLMConfig(
model_loading_config=dict(
model_id="qwen3-reward",
model_source="Qwen/Qwen3-0.6B",
),
# vLLM's entry point registers the architecture in the engine and worker
# processes. Ray Serve LLM also resolves it while building the engine config.
server_cls="qwen3_reward_plugin.serve_hook:RewardModelServer",
engine_kwargs=dict(
runner="pooling",
hf_overrides=dict(
architectures=["Qwen3CustomRewardModel"],
num_labels=1,
problem_type="regression",
),
max_model_len=4096,
),
)
# Requires direct streaming so vLLM's native /classify route is exposed.
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

Save this as `app.py`

and run it to deploy.

```
# config.yaml
applications:
- args:
llm_configs:
- model_loading_config:
model_id: qwen3-reward
model_source: Qwen/Qwen3-0.6B
# Register the plugin architecture in the Ray Serve LLM processes.
server_cls: qwen3_reward_plugin.serve_hook:RewardModelServer
engine_kwargs:
runner: pooling
hf_overrides:
architectures:
- Qwen3CustomRewardModel
num_labels: 1
problem_type: regression
max_model_len: 4096
import_path: ray.serve.llm:build_openai_app
name: custom_vllm_app
route_prefix: "/"
```

Deploy it with `serve run custom_vllm_config.yaml`

.

## Query the model[#](https://docs.ray.io#query-the-model)

Run the following command to verify your model is serving. This query sends text to the `/classify`

endpoint and reads the scalar reward from `data[0].probs[0]`

. Until you provide trained reward-head weights (see the next section), this value is arbitrary.

```
import requests
response = requests.post(
"http://localhost:8000/classify",
json={"model": "qwen3-reward", "input": "The capital of France is Paris."},
).json()
print(response["data"][0]["probs"][0]) # scalar reward
```

```
curl -X POST http://localhost:8000/classify \
-H "Content-Type: application/json" \
-d '{
"model": "qwen3-reward",
"input": "The capital of France is Paris."
}'
```

## Provide the reward-head weights[#](https://docs.ray.io#provide-the-reward-head-weights)

The reward head is a separate `Linear(hidden_size, 1)`

whose weights are not part of the base Hugging Face checkpoint, so the model loads them from a file system or an object store. The path is plugin-specific. In this example, the model reads it from the `RM_REWARD_HEAD_PATH`

environment variable. Include the weights file in your image and set the variable through the deployment’s `runtime_env`

:

```
llm_config = LLMConfig(
# ... same fields as above ...
runtime_env=dict(env_vars=dict(RM_REWARD_HEAD_PATH="/path/to/reward_head.pt")),
)
```

## See also[#](https://docs.ray.io#see-also)

[Direct streaming](https://docs.ray.io/direct-streaming.html): how Ray Serve LLM serves vLLM’s native routes.