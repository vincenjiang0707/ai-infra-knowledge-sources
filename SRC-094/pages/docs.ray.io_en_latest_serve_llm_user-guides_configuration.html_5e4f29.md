source: https://docs.ray.io/en/latest/serve/llm/user-guides/configuration.html
lastmod: 

# Configuration reference[#](https://docs.ray.io#configuration-reference)

[ LLMConfig](https://docs.ray.io/api/doc/ray.serve.llm.LLMConfig.html#ray.serve.llm.LLMConfig) is the central configuration object for a Ray Serve LLM deployment. It describes which model to serve, which engine and hardware to run it on, how to scale it, and how to expose it. You pass one

`LLMConfig`

per model to a builder such as [, or you write the equivalent YAML.](https://docs.ray.io/api/doc/ray.serve.llm.build_openai_app.html#ray.serve.llm.build_openai_app)

`build_openai_app`

This page documents every field. For the design behind these abstractions, see [Core components](https://docs.ray.io/architecture/core.html).

## Minimal configuration[#](https://docs.ray.io#minimal-configuration)

Only `model_loading_config`

is required. Every other field has a default. The example also sets `accelerator_type`

so replicas schedule onto the right GPU:

```
from ray.serve.llm import LLMConfig
llm_config = LLMConfig(
model_loading_config=dict(
model_id="qwen-0.5b",
model_source="Qwen/Qwen2.5-0.5B-Instruct",
),
accelerator_type="A10G",
)
```

## Top-level fields[#](https://docs.ray.io#top-level-fields)

Field |
Type |
Default |
Description |
|---|---|---|---|
|
dict or |
required |
Which model to serve and where to load it from. See |
|
dict |
|
Arguments forwarded to the inference engine (vLLM). See |
|
str |
|
The accelerator the model runs on, for example |
|
dict |
|
Hardware-specific config (GPU, TPU, CPU). Inferred from |
|
dict |
|
Resource bundles and placement strategy for engine workers. See |
|
dict |
|
Ray Serve deployment options such as autoscaling and replicas. See |
|
dict or |
|
LoRA adapter settings. See |
|
dict |
|
Ray runtime environment applied to the replica and engine workers (for example, |
|
str |
|
The inference engine. |
|
str or class |
|
Custom server class, for example |
|
dict |
|
Experimental knobs. See |
|
bool |
|
Export engine metrics through the Ray Prometheus port. See |
|
|
default |
Initialization callbacks. See |

## Model loading[#](https://docs.ray.io#model-loading)

`model_loading_config`

is validated against [ ModelLoadingConfig](https://docs.ray.io/api/doc/ray.serve.llm.ModelLoadingConfig.html#ray.serve.llm.ModelLoadingConfig):

Field |
Type |
Default |
Description |
|---|---|---|---|
|
str |
required |
The ID end users pass as |
|
str or |
|
Where to load weights from. When unset, defaults to |
|
str |
|
Where to load the tokenizer from. When unset, the tokenizer is loaded from the model source. Hugging Face IDs only. |

`model_source`

accepts several forms:

```
# Hugging Face Hub ID
model_loading_config=dict(model_id="qwen", model_source="Qwen/Qwen2.5-0.5B-Instruct")
# Local path
model_loading_config=dict(model_id="qwen", model_source="/mnt/models/qwen")
# Cloud storage mirror (S3, GCS, or Azure)
model_loading_config=dict(
model_id="qwen",
model_source=dict(bucket_uri="s3://my-bucket/path/to/qwen"),
)
```

A cloud mirror is validated against [ CloudMirrorConfig](https://docs.ray.io/api/doc/ray.serve.llm.CloudMirrorConfig.html#ray.serve.llm.CloudMirrorConfig) and supports

`s3://`

, `gs://`

, `abfss://`

, and `azure://`

URIs. Mirroring weights from cloud storage avoids per-replica Hugging Face downloads. See [Deployment initialization](https://docs.ray.io/deployment-initialization.html).

## Engine arguments[#](https://docs.ray.io#engine-arguments)

`engine_kwargs`

are passed straight through to the engine, so any vLLM engine argument is valid here. Commonly used ones:

Argument |
Description |
|---|---|
|
Number of GPUs to shard each model replica across. See |
|
Number of pipeline stages, used to span nodes. |
|
Maximum context length (prompt plus generated tokens). |
|
Fraction of GPU memory the engine may use for weights and KV cache. |
|
Maximum number of sequences batched together per step. |
|
KV connector settings for prefill/decode and cache offloading. See |

For the full list, see the [vLLM engine arguments](https://docs.vllm.ai/en/latest/serving/engine_args.html). `disable_log_stats=True`

is rejected when `log_engine_metrics`

is enabled, because engine metrics require log stats.

## Accelerators and placement[#](https://docs.ray.io#accelerators-and-placement)

Set `accelerator_type`

to the accelerator each replica should be scheduled on. Common GPU values include `A10G`

, `A100`

, `H100`

, `H200`

, `L4`

, `L40S`

, and `T4`

. TPUs such as `TPU-V4`

and `TPU-V5P`

are also supported. `A10`

is normalized to `A10G`

. An unsupported value raises a validation error.

`accelerator_config`

is inferred from `accelerator_type`

(or from `placement_group_config`

bundles) and rarely needs to be set explicitly.

Use `placement_group_config`

to control how engine workers are packed onto nodes, for example for multi-node tensor or pipeline parallelism. Provide either `bundle_per_worker`

(auto-replicated by `tensor_parallel_size * pipeline_parallel_size`

) or an explicit `bundles`

list, plus an optional `strategy`

:

```
# One GPU bundle per worker, spread across nodes
placement_group_config=dict(
bundle_per_worker={"CPU": 1, "GPU": 1},
strategy="SPREAD",
)
# Explicit bundle list
placement_group_config=dict(
bundles=[{"CPU": 1, "GPU": 1}] * 4,
strategy="STRICT_PACK",
)
```

`strategy`

is one of `PACK`

, `STRICT_PACK`

, `SPREAD`

, or `STRICT_SPREAD`

. See [Cross-node parallelism](https://docs.ray.io/cross-node-parallelism.html) for worked examples.

## Deployment options[#](https://docs.ray.io#deployment-options)

`deployment_config`

holds standard Ray Serve `@serve.deployment`

options. Supported keys: `name`

, `num_replicas`

, `ray_actor_options`

, `max_ongoing_requests`

, `autoscaling_config`

, `max_queued_requests`

, `user_config`

, `health_check_period_s`

, `health_check_timeout_s`

, `graceful_shutdown_wait_loop_s`

, `graceful_shutdown_timeout_s`

, `logging_config`

, and `request_router_config`

.

```
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=4,
),
max_ongoing_requests=64,
)
```

Set `num_replicas="auto"`

to let Serve autoscale. Use `request_router_config`

to plug in a custom router, for example for [prefix-aware routing](https://docs.ray.io/prefix-aware-routing.html). For the meaning of each option, see the [Ray Serve deployment configuration](https://docs.ray.io/en/latest/serve/configure-serve-deployment.html) docs.

## LoRA[#](https://docs.ray.io#lora)

When `lora_config`

is set, the deployment serves LoRA adapters on top of the base model. It is validated against [ LoraConfig](https://docs.ray.io/api/doc/ray.serve.llm.LoraConfig.html#ray.serve.llm.LoraConfig):

Field |
Type |
Default |
Description |
|---|---|---|---|
|
str |
|
Cloud storage path ( |
|
int |
|
Maximum adapters loaded on each replica, evicted LRU. |
|
float |
|
Per-adapter download timeout in seconds. A value |
|
int |
|
Maximum adapter download retries. |

See [Multi-LoRA deployment](https://docs.ray.io/multi-lora.html) for the full workflow.

## Experimental configs[#](https://docs.ray.io#experimental-configs)

`experimental_configs`

is a dictionary of opt-in knobs that may change between releases:

Key |
Description |
|---|---|
|
How long to batch streaming responses before flushing them. Defaults to |
|
Number of ingress (router) replicas. |

## YAML equivalent[#](https://docs.ray.io#yaml-equivalent)

A config-file (YAML) deployment. `LLMConfig`

fields map one to one onto YAML keys:

```
applications:
- args:
llm_configs:
- model_loading_config:
model_id: qwen-0.5b
model_source: Qwen/Qwen2.5-0.5B-Instruct
accelerator_type: A10G
engine_kwargs:
tensor_parallel_size: 2
max_model_len: 8192
deployment_config:
autoscaling_config:
min_replicas: 1
max_replicas: 4
import_path: ray.serve.llm:build_openai_app
name: llm_app
route_prefix: "/"
```

Deploy it with `serve run config.yaml`

.

## See also[#](https://docs.ray.io#see-also)

[Quickstart](https://docs.ray.io/quick-start.html): deploy and query a model.: the generated API docs.`LLMConfig API reference`