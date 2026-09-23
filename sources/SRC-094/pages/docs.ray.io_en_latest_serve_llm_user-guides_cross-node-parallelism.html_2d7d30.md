source: https://docs.ray.io/en/latest/serve/llm/user-guides/cross-node-parallelism.html
lastmod: 

# Cross-node parallelism[#](https://docs.ray.io#cross-node-parallelism)

Ray Serve LLM supports cross-node tensor parallelism (TP) and pipeline parallelism (PP), which distribute model inference across multiple GPUs and nodes. Use cross-node parallelism to:

Deploy models that don’t fit on a single GPU or node.

Scale model serving across your cluster’s available resources.

Use Ray’s placement group strategies to control worker placement for performance or fault tolerance.


Note

By default, Ray Serve LLM uses the `PACK`

placement strategy, which tries to place workers on as few nodes as possible. If workers can’t fit on a single node, they automatically spill to other nodes. This enables cross-node deployments when single-node resources are insufficient.

## Tensor parallelism[#](https://docs.ray.io#tensor-parallelism)

Tensor parallelism splits model weights across multiple GPUs, with each GPU processing a portion of the model’s tensors for each forward pass. This approach is useful for models that don’t fit on a single GPU.

The following example shows how to configure tensor parallelism across 2 GPUs:

```
import vllm
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Configure a model with tensor parallelism across 2 GPUs
# Tensor parallelism splits model weights across GPUs
llm_config = LLMConfig(
model_loading_config=dict(
model_id="llama-3.1-8b",
model_source="meta-llama/Llama-3.1-8B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=2,
)
),
accelerator_type="L4",
engine_kwargs=dict(
tensor_parallel_size=2,
max_model_len=8192,
),
)
# Deploy the application
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

## Pipeline parallelism[#](https://docs.ray.io#pipeline-parallelism)

Pipeline parallelism splits the model’s layers across multiple GPUs, with each GPU processing a subset of the model’s layers. This approach is useful for very large models where tensor parallelism alone isn’t sufficient.

The following example shows how to configure pipeline parallelism across 2 GPUs:

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Configure a model with pipeline parallelism across 2 GPUs
# Pipeline parallelism splits model layers across GPUs
llm_config = LLMConfig(
model_loading_config=dict(
model_id="llama-3.1-8b",
model_source="meta-llama/Llama-3.1-8B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=1,
)
),
accelerator_type="L4",
engine_kwargs=dict(
pipeline_parallel_size=2,
max_model_len=8192,
),
)
# Deploy the application
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

## Combined tensor and pipeline parallelism[#](https://docs.ray.io#combined-tensor-and-pipeline-parallelism)

For extremely large models, you can combine both tensor and pipeline parallelism. The total number of GPUs is the product of `tensor_parallel_size`

and `pipeline_parallel_size`

.

The following example shows how to configure a model with both TP and PP (4 GPUs total):

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Configure a model with both tensor and pipeline parallelism
# This example uses 4 GPUs total (2 TP * 2 PP)
llm_config = LLMConfig(
model_loading_config=dict(
model_id="llama-3.1-8b",
model_source="meta-llama/Llama-3.1-8B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=1,
)
),
accelerator_type="L4",
engine_kwargs=dict(
tensor_parallel_size=2,
pipeline_parallel_size=2,
max_model_len=8192,
enable_chunked_prefill=True,
max_num_batched_tokens=4096,
),
)
# Deploy the application
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

## Custom placement groups[#](https://docs.ray.io#custom-placement-groups)

You can customize how Ray places vLLM engine workers across nodes using `placement_group_config`

with either `bundle_per_worker`

(simple) or `bundles`

(advanced).

### Basic configuration with bundle_per_worker[#](https://docs.ray.io#basic-configuration-with-bundle-per-worker)

Use the `bundle_per_worker`

option inside `placement_group_config`

to specify resources for each worker without manually creating the full bundle list. Ray automatically replicates this bundle based on `tensor_parallel_size * pipeline_parallel_size`

. This field is mutually exclusive with `bundles`

.

Note

In each bundle dict, `CPU`

and `GPU`

are numeric amounts. If you omit either key, it is treated as **0** — set both explicitly when your workers need CPUs and GPUs (there is no implicit default GPU when you only specify CPU, or vice versa).

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Configure a model with bundle_per_worker for simple resource specification
# Ray automatically replicates this bundle based on tp * pp (2 bundles total)
llm_config = LLMConfig(
model_loading_config=dict(
model_id="qwen-0.5b",
model_source="Qwen/Qwen2.5-0.5B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=1,
)
),
engine_kwargs=dict(
tensor_parallel_size=2,
max_model_len=1024,
max_num_seqs=32,
),
# Simple: specify resources per worker, auto-replicated by tp*pp
placement_group_config=dict(
bundle_per_worker={"GPU": 1, "CPU": 1},
),
)
# Deploy the application
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```

### Advanced configuration with bundles[#](https://docs.ray.io#advanced-configuration-with-bundles)

For full control over bundle specification and placement strategy, use `placement_group_config`

with `bundles`

. This accepts a dictionary with `bundles`

(a list of resource dictionaries) and `strategy`

(placement strategy).

Ray Serve LLM uses the `PACK`

strategy by default, which tries to place workers on as few nodes as possible. If workers can’t fit on a single node, they automatically spill to other nodes. For more details on all available placement strategies, see [Ray Core’s placement strategies documentation](https://docs.ray.io/ray-core/scheduling/placement-group.html#pgroup-strategy).

Note

Data parallel deployments automatically override the placement strategy to `STRICT_PACK`

because each replica must be co-located for correct data parallel behavior.

While you can specify the degree of tensor and pipeline parallelism, the specific assignment of model ranks to GPUs is managed by the vLLM engine and can’t be directly configured through the Ray Serve LLM API. Ray Serve automatically injects accelerator type labels into bundles and merges the first bundle with replica actor resources (CPU, GPU, memory).

The following example shows how to use the `SPREAD`

strategy to distribute workers across multiple nodes for fault tolerance:

```
from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app
# Configure a model with custom placement group using SPREAD strategy
# SPREAD distributes workers across nodes for fault tolerance
llm_config = LLMConfig(
model_loading_config=dict(
model_id="llama-3.1-8b",
model_source="meta-llama/Llama-3.1-8B-Instruct",
),
deployment_config=dict(
autoscaling_config=dict(
min_replicas=1,
max_replicas=1,
)
),
accelerator_type="L4",
engine_kwargs=dict(
tensor_parallel_size=4,
max_model_len=8192,
),
placement_group_config=dict(
bundles=[{"GPU": 1}] * 4,
strategy="SPREAD",
),
)
# Deploy the application
app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
```